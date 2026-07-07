# Video encoding primer and common `ffmpeg` workflows

`ffmpeg` is a very powerful tool to work with video data, but has a few gotchas that can be tricky. Below you can find some recommendations for common workflows and the rationale behind them.

We recommend reading [A primer on video encoding](video-primer.md) first to understand the key concepts discussed below.

## Recommended re-encoding command
For all the rest: recommended to re-encode video first

To re-encode (from SLEAP DOCS, with request for timestamps unchanged)
```bash
ffmpeg -y \
-i input_video.avi \
-c:v libx264 \
-pix_fmt yuv420p \
-preset superfast \
-crf 23 \
-vstats \ # dump video coding stats to vstats_HHMMSS.log file
-fps_mode passthrough \ # to pass timestamps unchanged, relevant if variable frame rate
output_video.mp4
```

- `-y` : overwrite without asking
- `-c`: codec (encoder if applied to input or decoder if applied to output)
- `-c:v _nameofcodec_` --> specified the codec applied to the video (v) stream. If you use `copy` as name, the stream is not re-encoded
	- alternatively `-vcodec`
- `-pix_fmt`: this is mostly for videos to play [in Quicktime and most others](https://trac.ffmpeg.org/wiki/Encode/H.264#Encodingfordumbplayers). These players only support the YUV planar color space with 4:2:0 chroma subsampling for H.264 video.
- `-preset`
- `-crf` is the quality setting for x264 encoder. A CRF of 15 is nearly lossless


If you find the video takes long to decode random frames when scrolling through its timeline, and are willing to accept larger file sizes:
- reduce size of GOP:  More frequent I-frames means larger files but faster seeking. -g 250 (default). -g 10 (would maybe x2 file size) or -g 30 ((one keyframe per second at 30fps)) might be good enough-try
- all intra version (~ 6x file size): set -g to 1 or use -intra



## Counting frames in a video

```bash
ffprobe -v error \
-select_streams v:0 \
-count_frames \
-show_entries stream=nb_read_frames \
-of csv=p=0 \  # output as .csv without headers
<path-to-video>
```
Note that we use `nb_read_frames` rather than `nb_frames`; the latter is faster but less accurate because it gets the frames from the header of the container.


## Check fps of a video

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 <path-to-video>
```

## Extracting frames by index from video as image files
* It is sometimes unclear in ffmpeg whether frames are counting starting from 0 or 1

* Option 1: You can use a select filter (which we know uses 0-based because the docs say so), but it is a bit cumbersome (see [here](https://superuser.com/questions/1009969/how-to-extract-a-frame-out-of-a-video-using-ffmpeg))
```bash
 ffmpeg -i input.mp4 -vf "select='eq(n\,10)+eq(n\,50)+eq(n\,100)'" -vsync vfr frame_%03d.png
```
The select filter **decodes every frame from the beginning of the stream** and simply decides which decoded frames to pass through to the output. It doesn't skip or seek at all — it's a filter that accepts or rejects already-decoded frames based on your expression (e.g., select='eq(pict_type,I)' to pass only keyframes).
Because it decodes everything, it is:
* Frame-accurate — you get exactly the frames matching your condition
* Slow — no shortcuts are taken; the full stream is decoded
We can combine it with -ss (before -i for input seeking behaviour, after -i for output seeking behaviour), for faster speed.

Note about default filenaming in the single pass snippet above: the order of the frames in the select parameter does not matter, because it acts as a logical OR gate for the frame index. As a result, frames are extracted in decode order, that is, in ascending order. In the example above, frame idx = 10 will be saved as frame_001.png, idx=50 --> frame_002.png and idx=100 --> frame_003.png. You may want to add a loop later to rename the files, or alternatively, use a loop and extract each frame in a separate command for clarity. But note that in the per-frame loop: "Total work ≈ sum over frames of (decode from preceding keyframe to that frame), plus N times the ffmpeg startup + file-open overhead.", the overhead is usually larger.

From Claude:
> n is ffmpeg's built-in variable for the zero-based index of the current video frame being decoded. The select filter evaluates the expression for every frame, and only passes through frames where the result is non-zero (truthy). So eq(n,100) returns 1 when ffmpeg is processing frame 100, and 0 otherwise. The + acts as a logical OR.
> -vsync vfr \  # prevent ffmpeg from producing a video with same fps as input.  Without vfr, ffmpeg would duplicate the selected frames to fill the gaps and produce an output with the same fps as the input — so instead of 3 frames you'd get a full-length video with those frames repeated.
> -q:v 2 — output quality for the PNG encoder. Lower is better; 2 gives near-lossless quality. For PNG (lossless by definition) this controls the zlib compression level, so it has no effect on pixel accuracy, only on file size vs. encode speed.
> Without -q:v, ffmpeg defaults to -q:v 3 for PNG, which is one compression level lower effort — the difference in speed is negligible. PNG compression levels (1–9) trade encode time for file size, but the effect is small compared to the time spent decoding the video frames. You can safely drop it.

Tip — for many frames, it's cleaner to use a script:
```bash
frames=(10 50 100 200 350)
for f in "${frames[@]}"; do
  ffmpeg -i input.mp4 -vf "select='eq(n\,$f)'" -vsync vfr "frame_${f}.png"
done
```
This spawns one ffmpeg call per frame, which is slower but easier to manage for large lists.

* Option 2: sleap-io or similar, it provides an array-like interface for a video, then use PIL or imageio to save the file.
Con: it can be slow for later frames
```python
import sleap_io as sio
import imageio.v3 as iio

video = sio.load_video(video_path)

for frame_idx in list_frames_idcs:
    frame = video[frame_idx] # numpy array, RGB, uint8

    # Save as PNG with imageio
    iio.imwrite(f"frame_{frame_idx:0>5d}.png", frame)

```

Note that sleap-io does not re-encode — it reads frames from the original file using whichever backend you have installed (imageio-ffmpeg by default, or OpenCV/PyAV optionally). If the video is not reliably seekable (e.g. a poorly encoded AVI), you can still get wrong frames, same as with raw ffmpeg. the recommendation to re-encode first still applies even when using sleap-io. sleap-io makes the frame access interface nicer, but it doesn't solve the underlying seekability problem of the source video.


* Option 3: use pyav and seek first to nearest keyframe (recommended)
From Claude:
Seeking to a specific frame index requires converting it to a timestamp, seeking to the nearest keyframe before it, then decoding forward until you reach it:

<!-- ```python
import av

target_idx = 324
# indices are 0-based because
# frame.pts starts at 0 for the first frame,
# so current_idx (derived from frame.pts) is also 0-based.

with av.open(video_path) as container:
    stream = container.streams.video[0]
    fps = float(stream.average_rate)

    # Seek to nearest keyframe before target (time in microseconds)
    container.seek(int(target_idx / fps * 1e6))

    for frame in container.decode(stream):
        current_idx = round(frame.pts * float(stream.time_base) * fps)
        if current_idx >= target_idx:
            img = frame.to_ndarray(format="rgb24")
            break
``` -->

`container.seek()` takes microseconds and lands on the nearest keyframe before the target time
`frame.pts * stream.time_base` converts the frame's presentation timestamp to seconds, then multiplying by `fps` gives the frame index
You decode forward from the keyframe until you hit the target
This is fast for any frame because it only decodes from the nearest keyframe, not from the start of the video.


**To avoid issues with floating point error accumulation**, operating with fraction arithmetic via `Fraction` is preferred. Here, we assume frames have uniformly spaced PTS values, i.e. constant frame rate.

`frame.time_base` and `stream.codec_context.framerate` are already Fraction objects in PyAV. Note that PTS (Presentation Timestamp) is always an integer in the container.

<!-- * Why PTS is always an integer:
It's how video containers work at the format level — PTS is stored as an int64 in the container, representing a count of time base units. The time base (a Fraction) is the scaling factor to convert it to seconds. So actual time = pts * time_base, where pts is always a raw integer counter. -->

int() is still worth keeping for `target_pts` because target_pts should theoretically be an exact integer (for constant frame rate video, target_idx / fps / time_base divides out cleanly). Using int() makes this explicit and keeps both sides as integers. If it's not an exact integer due to an unusual fps/time_base combination, int() floors it, which is the safe direction — you'd land on the frame just before rather than just after the target.

```py
import av
from fractions import Fraction

target_idx = 324
# indices are 0-based because
# frame.pts starts at 0 for the first frame,
# so current_idx (derived from frame.pts) is also 0-based.

with av.open(video_path) as container:
    stream = container.streams.video[0]
    fps = stream.codec_context.framerate # Fraction

    # Go to nearest keyframe **before** target (time in microseconds)
    container.seek(int(target_idx / float(fps) * 1e6))

    # Decode from keyframe until we get a frame with PTS >= target
    # (assumes constant fps)
    target_pts = None # initialise
    for frame in container.decode(stream):
        # Compute target_pts from first frame
        # (we need to get frame.time_base from first frame)
        if target_pts is None:
          target_pts = int(Fraction(target_idx) / fps / frame.time_base)

        # Throw an error if PTS for this frame not defined
        # (possible in some containers)
        if frame.pts is None:
          raise ValueError(f"Frame has no PTS — cannot seek accurately")

        # Compare PTS values (both are integers)
        if frame.pts >= target_pts:
            img = frame.to_ndarray(format='rgb24')
            break
```

* Why >= rather than =?
target_pts is computed from target_idx / fps / time_base, which assumes frames are perfectly evenly spaced. But the actual PTS values stored in the stream may not follow this exactly — encoders sometimes adjust PTS values slightly for buffering, B-frames, or timestamp rounding. So the frame you want might be stored with PTS 324323 rather than the 324324 you computed, and == would skip it.
>= handles this by accepting the first frame at or past the target time, which is always the correct frame.


The PTS values stored in the file are the ground truth — they are what the decoder uses to decide when to display each frame. Your computed target_pts is just an approximation derived from metadata (fps, time_base), so the actual stored PTS is always more authoritative. This is exactly why >= is safer than ==; you trust the stored PTS values rather than your computed expectation of what they should be.

Key aspects:
- exact Fraction arithmetic for target_pts,
- integer comparison, and
- >= to handle PTS misalignment.


If you are closer to the end of the video (e.g. you want to extract the last frame), you may want to start searching from a
point closer the end.
```py
# Last frame — seek near the end, then step forward:
with av.open(video_path) as container:
    stream = container.streams.video[0]

    # Seeking lands on the nearest keyframe before the requested point
    container.seek(stream.duration, stream=stream)

    # decodes frames sequentially from the seek position.
    # Each frame is decoded in order from that keyframe onward.
    last = None
    for frame in container.decode(stream):
        last = frame
    img = last.to_ndarray(format="rgb24")
iio.imwrite(output_path, img)
```

The one caveat with PTS comparison: it assumes frames have uniformly spaced PTS values (constant frame rate). For variable frame rate videos this could break.


(target-extracting-clip-from-video)=
## Extracting a clip from a video
* Recommended to always check at the end if the total number of frames in the output clip is what you expect! (See section "Counting frames in a video")

* Input seeking
- in theory for ffmpeg > 2.1 and without stream `copy` it is frame accurate
- but:
> Input-side seeking (-ss before -i): FFmpeg jumps to the nearest preceding keyframe using the container index, then decodes forward to your target timestamp. This is fast because it skips demuxing and decoding the bulk of the stream. The decoded frame at your target timestamp is accurate. The only "inaccuracy" is that the output stream may begin at the keyframe rather than your exact timestamp — relevant when trimming, not when extracting a frame.


* Output seeking
- Slower but more reliable (see [crabs script](https://github.com/SainsburyWellcomeCentre/crabs-exploration/blob/6dd8df17642d0250674c62083057abce03c64fff/crabs/utils/extract_loop_clips.py#L188))


* Stream copy: if there is stream `copy` there is no frame-accuracy, because the stream that is passed to the `input` and `output` gates is not decoded into frames. Even if used with "output" syntax.

* In seeking: how does ffmpeg decide if a frame is in or out?
frame_PTS: the start time of the frame (PRESENTATION TIMESTAMP = PTS)
- `-to` -----> means "include frame if frame_PTS < `-to` value"
- `-ss`------> means "include frame if frame_PTS >= `-ss` value"

* when using `-ss` or `-to` gates, what maters is the START TIME OF THE FRAME, sometimes called the frame PRESENTATION TIMESTAMP or frame PTS. From Claude:

> Output `-ss X` is a gate function i.e. allow only elements starting with timestamp X. Whether elements are decoded frames or original packets depend on the codec option set for that stream.
So if the stream that goes thru the "output gate" is in groups of pictures (e.g. because we have `copy` and the video is not transcoded), then it will let pass one full group of pictures

Note: [Syntax to express time duration in ffmpeg commands](https://ffmpeg.org/ffmpeg-utils.html#time-duration-syntax)

Alternative: via sleap-io (although note that sleap-io does not re-encode)

> the difference between input and output seeking is on where the output stream starts and how much decoding work is done to get there

## Combine image files into a video

See here: https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/

```bash
ffmpeg -r 60 -f image2 -s 1920x1080 -i pic%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4
```

```bash
ffmpeg -r 1 -f image2 -pattern_type glob -i '/path/to/dir/with/images/*.png' \
  -vcodec libx264 -crf 25 -pix_fmt yuv420p \
  /path/to/output/video.mp4
```

```bash
ffmpeg -r 30 -f image2 -s 1024x576 -start_number 11384 -i /Users/sofia/swc/project_movement_dataloader/bboxes-datasets/face_track_annotation/images/%08d.jpg -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4
```
There's a common point of confusion: when extracting frames to image files, FFMPEG defaults to starting output filenames at 1 (e.g., frame0001.png), but internally the frame numbers in filters still use 0-based indexing. You can override this with -start_number 0.


## References
- [FFMPEG's H.264 guide](https://trac.ffmpeg.org/wiki/Encode/H.264])
- [FFMPEG'S Frame accuracy when seeking](https://fftrac-bg.ffmpeg.org/wiki/Seeking)
- [FFMPEG's CRF guide](https://trac.ffmpeg.org/wiki/Encode/H.264#a1.ChooseaCRFvalue)

- [Main options](https://ffmpeg.org/ffmpeg.html#Main-options)
- [Video options](https://ffmpeg.org/ffmpeg.html#Video-Options)
