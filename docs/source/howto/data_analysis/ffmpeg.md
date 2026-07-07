# Useful `ffmpeg` commands for working with video data


`ffmpeg` is a very powerful tool to work with video data, but has a few gotchas that can be tricky. Below you can find some recommendations for common workflows and the rationale behind them.


## A minimal primer on video encoding
We often have the mental model of videos being a sequence of standalone images. However, digital videos are typically encoded as video streams, whose structure is very different from a sequence of standalone frames. To understand better the differences, we need to clarify some concepts.

We only give a brief and simplified overview here, but if you would like further details [this blogpost from Loopbio](http://blog.loopbio.com/video-io-1-introduction.html#:~:text=A%20concise%20primer%20on%20video%20compression) is a recommended read (as well as the references at the end of the post).

<!-- ### Encoding and decoding
Encoding is the process of converting raw video into a compressed bitstream following a specific standard (e.g., H.264). Decoding is the reverse process: interpreting a bitstream to reconstruct the pixel data for each frame. In this post, we will use encoding and compression to refer to the same concept, even though strictly speaking encoding refers to a change of format only, without necessarily a reduction in file size. However in the context of video data, both concepts largely overlap.

A clear example of why we encode videos is provided in the [Loopbio blogpost](http://blog.loopbio.com/video-io-1-introduction.html):
> When stored digitally, an uncompressed video needs `width * height * colordepth * framerate * duration` bits. How much is that? As an example, one early video that a client uploaded to loopy had a resolution of 1920x1080, 24 bits color depth and a fast framerate of 120fps. If uncompressed, this video would need 5 971 968 000 bits per second (this is know as bitrate). In other words, a minute of such video would use up around 42GB, or in other words, had we stored these videos raw, we could only have been able to keep around 100 minutes. Our client has around 145 hours of beautiful fish schools footage recorded under the Red See, so there is no way that would work.
>
> Obviously no one uses raw video when storing or transmitting digital video. Our client had around 145 hours of footage, but it was taking only slightly less than 7TB (instead of 2835TB!). This is so because the videos were compressed. -->

### Codecs, encoders and decoders
A video codec is software (or hardware) that compresses (encodes) and decompresses (decodes) digital video (source: Wikipedia). The encoder converts the raw video stream into a compressed binary-encoded bitstream following a specific standard (e.g., H.264). The decoder does the opposite operation: from the bitstream it restores the pixel content of each frame for playback.

:::{note}
In this post, we will use encoding and compression to refer to the same concept, even though strictly speaking encoding refers to a change of format only, without necessarily a reduction in file size. However in the context of video data, both concepts largely overlap. Similarly, we will use decoding and decompression as synonyms.
:::

How does the encoding process compress the size of the video file? It does so by taking advantage of spatial redundancies (i.e. regions of a single frame with a lot or repetition), temporal redundancies (i.e. consecutive frames tend to look very much alike) and the human visual perception particularities (for example, we can distinguish better between bright and dark than between shades of colors). This allows encoders to make for smaller video files while still keeping good visual quality. (TODO: paraphrase this section).

The encoding process necessarily implies some loss of the original video quality, since we are approximating the raw pixel values using a compressed representation. Importantly, encoding is always a tradeoff between video quality, file size and speed, of which we can only have two out of the three. As stated in [this presentation by Werner Robitza](https://slhck.info/ffmpeg-encoding-course/#/32), that means that:
* If we want a high-quality video that can be encoded quickly, the compressed video will necessarily be large
* If we want a high-quality video with smaller file size, we will necessarily have a slower encoding of the data
* If we want a small file size and fast encoding, its quality will be lower

The encoding process is slower than the decoding process, and thus the main "bottleneck". This is because the encoder needs to solve a complex optimisation problem that determines aspects such as how to partition the frame into blocks, the predictions mode to use or how to allocate bits across the video stream. The decoder instead is designed to be fast, it simply implements the optimal instructions computed by the encoder. (TODO: find a nice reference for this)

For scientific applications, retaining video quality is often the most important requirement, but a reasonable file size is also desirable. We usually also care less about the speed of encoding.

Below you can find a short video with the basics of video encoding:

<iframe width="190" height="119" frameborder="0" loading="lazy" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; web-share" allowfullscreen src="https://commons.wikimedia.org/wiki/File:Video_Codecs_101.webm?embedplayer=true"></iframe>

### Group of pictures (GoP) and types of frames
A group of pictures is the basic unit in a compressed video. The encoding and decoding of a group of pictures is independent of the rest of frames: that is, to obtain the full pixel values for all frames in a group of pictures, we only need the information held in that set of frames, and no other frames outside that group are required. In H.264, a group of pictures is made up of 12 frames (TODO: double check).

A GoP is made up two types of frames, which differ by the way the are encoded:
* intra frames, or **I-frames**, are encoded as a regular standalone image; to decode an I-frame we do not need information from any other frames. These frames are also called **keyframes**.
* inter frames are not encoded as a regular standalone image. Instead, decoding their pixel content requires decoding the data from other frames. If only data from previous frames is required, the inter frames are called predicted frames, or **P-frames**. If data from both previous and future frames is required, the inter frames are also called bi-predictive or **B-frames**,


### Motion vector and residual maps
So if not saved as standalone images, how are inter frames represented? Let's focus on the simpler case of P-frames. Rather than saving all their pixel values, P-frames are encoded in a more compact representation, made of two parts:
- a motion vector map, and
- a residual map.

The motion vector map $M$ is the vector field that for each block of pixels in frame `t-1` holds the vector pointing to the most similar block of pixels in frame `t`. The similarity between blocks of pixels is determined via a block matching algorithm. The residual map $R$ contains the difference in pixel values $I$ between matched blocks of pixels in frame `t-1` and in frame `t`. As a result, we can decode the pixel values in frame `t` as:

$$
\mathbf{I}^{t}(x, y) = \mathbf{I}^{t-1}\left[(x, y) - \mathbf{M}^{t}(x, y)\right] + \mathbf{R}^{t}(x, y),
$$

where $x,y$ are the coordinates in image space of a specific pixel value.

The basic idea is that if the motion vector estimation is good, the residual map will be quite sparse and therefore the representation will be more compact than holding the full pixel values of frame `t`.

:::{tip}
You can actually visualise the motion vector map in FFMPEG as described in [this presentation by Werner Robitza](https://slhck.info/ffmpeg-encoding-course/#/51).
:::

NOTE: this section could be a collapsible

### Fast random access
Fast random access is a common desirable characteristic of a compressed video, that refers to how quickly you can decode a specific frame. This is relevant, for example, for a seamless experience when scrolling through the timeline of a video.

How is a random frame decoded? With codecs like H.264 in its normal mode (which use keyframes and interframes), to decode frame 1247 the decoder would need to go to the nearest keyframe first (maybe frame 1200) and then decode all 47 frames in between.

This may be slow in some cases, which is why some codecs can be set to "all-intra", meaning all frames are forced to be keyframes. If all frames are essentially standalone images, decoding any of them is fast. However, the file size will increase considerably.


### Frame accurate seeking

Frame-accurate seeking is another commonly desired quality when working with a video. It means you can reliably and repeatably land on exactly the frame you want (e.g. frame 1247, not "somewhere near frame 1247"). This is relevant, for example, when visualising labelled data overlaid on a video. The labels defined in frame 1247 should match the image data for that frame, but if frames are not reliably seekable, the video player may be showing a different underlying frame and the labels will seem "out of sync". It may also be an issue when extracting frames for labelling: the user may select specific frame numbers to extract from the video, but they may actually extract frames somewhere near but not precisely at those indices.

To understand this issue further, we first need to explain what a video container is. A **container** is the file format that wraps around the actual video and audio data. It contains the compressed streams (produced by the codec) and additional metadata required to play the video back properly, such as frame rate, resolution or codec info.

<!-- The component that writes the container is called **muxer** and the process of **muxing** (from multiplexing, taking separate streams (video, audio, subtitles) and combining them into a single container file with a proper index and metadata) -->

A fundamental part of this metadata is the **index**, which maps timestamps to byte positions in the file, and marks which frames are keyframes. If this index is incomplete, corrupt or imprecise (for example, because the recording was interrupted due to power loss), the video player (or another tool relying on the index to work) might land in the wrong spot in the video. Some containers handle this better than others. The combination of MP4 container with an H.264 codec is a combination with very mature and reliable indexing (TODO: paraphrase).

However, even if the index is correct and the container puts you at exactly the right byte in the file for the requested frame, if that byte corresponds to a B-frame, you can't decode it without first decoding the frames it depends on. Some players or tools cut corners here to achieve fast seeking at the expense of accuracy, and simply seek to the nearest keyframe and call it close enough (this is called "lazy seek"). This leads to frames not being accurately seekable, since the player may return the nearest keyframe rather than the exact frame requested (TODO: paraphrase).

For the case of `ffmpeg` commands, this is further complicated because the seeking behaviour and its corresponding accuracy guarantees vary depending on the *order in which the seeking-related arguments* are passed to the command. See [Extracting a clip from a video](target-extracting-clip-from-video) for a specific example.

One way to eliminate this corner-cutting behaviour of some players and tools is to use "all-intra" encoding, which forces all frames to be intraframes or keyframes. However, this comes at the cost of larger file size. Reducing the GOP size is an alternative, but note that this would not eliminate the issue if the video player does lazy seeking, it would just reduce the error. With the default GOP of 250 frames, a lazy seek could land up to 249 frames away from where you asked. With a GOP of 10 frames, the worst case is 9 frames off.

In conclusion, both an imprecise index, or a video player / tool that silently prioritises fast seeking vs accuracy, may lead to frames not being reliably seekable. We can try to minimise these issues by ensuring that we use a mature container and codec combination that produces a reliable index, and by being aware that this corner-cutting behaviour may occur in specific tools or video players. If this becomes a real issue, we can force the encoder to set all frames as keyframes, at the expense of a significantly larger file size.

<!-- But: if your goal is just to ensure a reliable index for frame extraction, remuxing is sufficient and much faster than re-encoding. Re-encoding only makes sense if you also want to change the codec, adjust quality, shrink the GOP, or switch to all-intra — the things we discussed earlier that address the seeking speed problem rather than the index reliability problem. -->


### Constant Rate Factor (CRF)
The Constant Rate Factor is a type of rate control mode. A **rate control mode** is an algorithm that is part of an encoder, and determines how many bits will be used for each frame. This in turn determines the file size and how quality is distributed.

In science, we usually care more for good quality videos rather than a very small file size, so CRF is often a good rate control mode to use because it instructs the encoder to aim for a certain consistent visual quality across all frames. That is, CRF assigns varying bits per frame such that every frame looks roughly equally good to our eyes. In practice this means a simple static shot (like a talking head against a plain background) gets very few bits assigned because it's easy to compress well (there is a lot of spatial redundancy in the plain background), while a complex high-motion scene (like confetti flying everywhere) would need more bits per frame to maintain the same perceived quality.  For further details on rate control mode, we recommend the post by Werner Robitza [Understanding Rate Control Modes](https://slhck.info/video/2017/03/01/rate-control.html).

:::{note}
An alternative approach would be something like CBR (Constant Bit Rate), where every second of video gets the same number of bits regardless of complexity. That's useful for streaming where you need predictable bandwidth, but it wastes bits on easy scenes and starves hard scenes. (TODO: paraphrase)
:::

If you are using FFMPEG, the CRF value will range from 0 to 51, where 0 is lossless, 23 is the default and 51 is the worst quality. Subjectively, the values between 17-28 are considered close to visually lossless. For further details, please check [FFMPEG's CRF guide](https://trac.ffmpeg.org/wiki/Encode/H.264#a1.ChooseaCRFvalue).




### Presentation timestamp (PTS)
* PTS: the start time of the frame

The encoder assigns PTS values to each frame based on the frame rate and time base, but it has some freedom in how it does this — different encoders (libx264, libx265, etc.) and different container muxers can make slightly different choices about rounding and spacing. Once written to the file, PyAV just reads whatever values the encoder stored.

* Why PTS is always an integer:
It's how video containers work at the format level — PTS is stored as an int64 in the container, representing a count of time base units. The time base (a Fraction) is the scaling factor to convert it to seconds. So actual time = pts * time_base, where pts is always a raw integer counter.



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


## Further reading
- Liu, H., Liu, W., Chi, Z., Wang, Y., Yu, Y., Chen, J., & Tang, J. (2022). Fast human pose estimation in compressed videos. IEEE Transactions on Multimedia, 25, 1390-1400.
- Mathis, A., & Warren, R. (2018). On the inference speed and video-compression robustness of DeepLabCut. [BioRxiv, 457242](https://www.biorxiv.org/content/10.1101/457242v1).
- [Loopbio blog: An Introduction to Video Compression](http://blog.loopbio.com/video-io-1-introduction.html)
- [FFMPEG's H.264 guide](https://trac.ffmpeg.org/wiki/Encode/H.264])
- [FFMPEG'S Frame accuracy when seeking](https://fftrac-bg.ffmpeg.org/wiki/Seeking)
- [FFMPEG's CRF guide](https://trac.ffmpeg.org/wiki/Encode/H.264#a1.ChooseaCRFvalue)
- [Understanding rate control modes](https://slhck.info/video/2017/03/01/rate-control.html)
- [What is CRF](https://slhck.info/video/2017/02/24/crf-guide.html)
- [Workshop on digital video](https://github.com/leandromoreira/digital_video_introduction)
- [Video Codecs 101 (video)](https://commons.wikimedia.org/wiki/File:Video_Codecs_101.webm)


- [Main options](https://ffmpeg.org/ffmpeg.html#Main-options)
- [Video options](https://ffmpeg.org/ffmpeg.html#Video-Options)
