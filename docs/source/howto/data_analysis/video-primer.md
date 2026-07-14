# A primer on video encoding

We often have the mental model of videos being a sequence of standalone images. However, digital videos are typically encoded as streams, whose structure is very different from a sequence of standalone frames. To understand better the differences, we need to clarify some concepts.

We only give a brief and simplified overview here, but if you would like to learn further we provide some useful references at the end of the post.


## Codecs, encoding and decoding
A **video codec** is a piece of software that compresses (encodes) and decompresses (decodes) digital video. 

:::{note}
In this post, we will use encoding and compression to refer to the same concept, even though strictly speaking encoding refers to a change of format only, without necessarily a reduction in file size. However, in the context of video data both concepts largely overlap. Similarly, we will use decoding and decompression as synonyms.

A video codec can also be hardware-based rather than software, but for this blogpost we will focus on software-based ones for simplicity.
:::

A codec is made up of two components: the encoder and the decoder (the word codec is a portmanteau of coder-decoder). The **encoder** compresses the raw video into a bitstream following a specific standard (e.g., H.264). The **decoder** does the reverse: it reconstructs each frame's pixels from the bitstream for playback.


### Why do we need to encode videos?

A clear example of why we encode videos is provided in the [Loopbio blogpost](http://blog.loopbio.com/video-io-1-introduction.html):

> When stored digitally, an uncompressed video needs `width * height * colordepth * framerate * duration` bits. How much is that? 
>
> As an example, one early [client video] had a resolution of 1920x1080, 24 bits color depth and a fast framerate of 120fps. If uncompressed, this video would need 5 971 968 000 bits per second (this is know as bitrate). In other words, a minute of such video would use up around 42GB, or in other words, had we stored these videos raw, we could only have been able to keep around 100 minutes. Our client has around 145 hours of beautiful fish schools footage recorded under the Red See, so there is no way that would work.
>
> Obviously no one uses raw video when storing or transmitting digital video. Our client had around 145 hours of footage, but it was taking only slightly less than 7TB (instead of 2835TB!). This is so because the videos were compressed.

### How does the encoding process reduce the size of a video file? 

An encoder reduces the size of a video by taking advantage of redundancies in the data:
* **Spatial redundancy**: within a single frame, neighbouring pixels are often similar (e.g. a large region of uniform background).
* **Temporal redundancy**: consecutive frames tend to look very much alike, so only what changes between can be stored.
* **Perceptual redundancy**: the human visual system is more sensitive to some aspects than others, so we can discard detail we barely notice (e.g, we perceive differences in brightness more readily than differences in colour).

All these allow encoders to generate smaller video files while still keeping good visual quality.

### What are the tradeoffs?
The encoding process necessarily implies some loss of the original video quality, since we are approximating the raw pixel values using a compressed representation. Importantly, encoding is always a tradeoff between video quality, file size and speed, of which we can only have two out of the three. As stated in [this presentation by Werner Robitza](https://slhck.info/ffmpeg-encoding-course/#/32), that means that:
* If we want a **high-quality video that can be encoded quickly**, the compressed video will necessarily be large.
* If we want a **high-quality video with smaller file size**, we will necessarily have a slower encoding of the data.
* If we want a **small file size and fast encoding**, its quality will be lower.

In terms of processing speed, the encoding process is slower than the decoding process. This is because the encoder needs to solve a complex optimisation problem that determines aspects such as how to partition the frame into blocks, how to allocate bits across the video stream, or the predictions mode to use. The decoder instead is designed to be fast, it simply implements the optimal instructions determined by the encoder.

For scientific applications, retaining video quality is often the most important requirement, but a reasonable file size is also desirable. If working with offline applications, we usually also care less about the speed of encoding.

Below you can find a short video with the basics of video encoding:

<div style="text-align: center;">
<iframe width="190*3" height="119*3" frameborder="0" loading="lazy" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; web-share" allowfullscreen src="https://commons.wikimedia.org/wiki/File:Video_Codecs_101.webm?embedplayer=true"></iframe>

*["Video Codecs 101"](https://commons.wikimedia.org/wiki/File:Video_Codecs_101.webm) by Lou Quillio, licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).*

</div>

## Group of pictures (GoP) and types of frames
A group of pictures (GoP) is the basic unit in a compressed video. It consists of a subset of contiguous frames, which can be of two types. The two types differ by the way the frames are encoded:

* Intra frames, or **I-frames**, are encoded as regular standalone images. To decode an I-frame we do not need information from any other frame. These frames are also called **keyframes**.
* Inter frames are not encoded as a regular standalone image. Instead, computing their pixel content requires decoding the data from other frames. If only data from _previous_ frames is required, the inter frames are called predicted frames or **P-frames**. If data from both _previous_ and _future_ frames is required, the inter frames are also called bi-predictive or **B-frames**,

A GoP is the actual set of frames from one keyframe (I-frame) plus all the inter-frames that follow it up to (but not including) the next keyframe.

<!-- The encoding and decoding of the frames in a group of pictures is independent of the rest of frames: that is, to obtain their full pixel values, we only need the information held in that set of frames, and no other frames outside that group are required.

:::{note}
The above describes a closed group of pictures, which is self-contained and does not allow frames inside the group to depend on frames from outside the group. There are also open group of pictures, which allow frames inside the group to depend on frames in adjacent groups. This allows for slightly better compression, but makes accurate slicing more complicated.
::: -->


::::{dropdown} So if not saved as standalone images, how are inter frames represented? 
:color: info
:icon: info

Let's focus on the simpler case of P-frames. They are encoded in a compact representation, that consists of a **motion vector map**, and a **residual map**.

The **motion vector map** $M$ is the vector field that for each block of pixels in frame `t-1` returns a vector pointing to the most similar block of pixels in frame `t`. The similarity between blocks of pixels is determined via a block matching algorithm. 

The **residual map** $R$ contains the difference in pixel values $I$ between matched blocks of pixels in frame `t-1` and in frame `t`. 

Using both $M$ and $R$, we can decode the pixel values in frame `t` as:

$$
\mathbf{I}^{t}(x, y) = \mathbf{I}^{t-1}\left[(x, y) - \mathbf{M}^{t}(x, y)\right] + \mathbf{R}^{t}(x, y),
$$

where $x,y$ are the coordinates in image space of a specific pixel value.

The basic idea is that if the motion vector estimation is good, the residual map will be quite sparse and therefore the representation will be more compact than holding the full pixel values of frame `t`.

:::{tip}
You can actually visualise the motion vector map in FFMPEG as described in [this presentation by Werner Robitza](https://slhck.info/ffmpeg-encoding-course/#/51).
:::
::::


## Rate control modes and Constant Rate Factor (CRF)
A **rate control mode** is an algorithm that is part of an encoder, and determines how many bits will be used for each frame. This in turn determines the file size and how quality is distributed. 

The **Constant Rate Factor** (CRF) is a type of rate control mode that assigns as many bits per frame as required so that every frame looks roughly equally good to our eyes. In practice, this means a simple static shot (like a talking head against a plain background) gets very few bits assigned to it because it's easy to compress well (there is a lot of spatial redundancy in the background), while a high-motion scene (like confetti flying everywhere) would get more bits per frame to maintain the same perceived quality. 

In science, we usually care more for good quality videos rather than a very small file size, so CRF is often a good algorithm to use. 

:::{dropdown} What are other options?
:color: info
:icon: info
An alternative could be Constant Bit Rate (CBR), which allocates the same number of bits to every second of video, irrespective of how complex each frame is. This is useful for streaming applications, where you need a predictable bandwidth, but it less efficient: it wastes bits on easy scenes, and demanding scenes are left short of them.
:::

If you are using FFMPEG, the CRF value will range from 0 to 51, where 0 is lossless, 23 is the default and 51 is the worst quality. Subjectively, the values between 17-28 are considered close to visually lossless. For further details, please check [FFMPEG's CRF guide](https://trac.ffmpeg.org/wiki/Encode/H.264#a1.ChooseaCRFvalue).

To learn more about rate control modes, we recommend the post by Werner Robitza: [Understanding Rate Control Modes](https://slhck.info/video/2017/03/01/rate-control.html).

## Video containers and index
A **container** is the file format that wraps around the actual video and audio data. It contains the compressed streams (produced by the codec) and additional metadata required to play the video back properly, such as frame rate, resolution or codec info.

:::{dropdown} Muxer and muxing
:color: info
:icon: info
The component that writes the container is called **muxer** and the process of writing it is often called **muxing**. "Muxing" comes from multiplexing, and it refers to the process of taking separate streams (video, audio, subtitles) and combining them into a single container file with a proper index and metadata.
:::

A fundamental part of the metadata added to the container is the **index**. The index maps timestamps to byte positions in the file, and marks which frames are keyframes. 

Video players rely on the index to seek a frame reliably and quickly. To display a frame at the requested timestamp, they look it up in the index to find its byte position and the nearest keyframe to start decoding from. If the index is incomplete, corrupt or imprecise, the video player or another tool relying on the index might land in the wrong spot in the video. 

An MP4 container with an H.264 codec is considered a combination with very mature and reliable indexing.

<!-- :::{dropdown}
:color: info
:icon: info
Containers differ in how robust their index is. They may write it all at the end or incrementally. They may be more or less tolerant to a damaged or missing index. The index they generate can be more or less supported by other tools.
::: -->

<!-- Remuxing to generate a new index if it is corrupt? -->



## Presentation timestamp (PTS)
The presentation timestamp (PTS) of a frame is the time, measured from the start of the video, at which that frame should be displayed (i.e. the start time of the frame).

PTS is stored in the video container as an integer, representing a count of time base units. The time base is defined by the container and it is the scaling factor to convert PTS values to seconds. So the actual time is `time = PTS × time_base`, where PTS is always an integer.

Different container formats use different time bases and rounding conventions, so exact PTS values can vary slightly across them.

## Some desirable characteristics of compressed videos

### Fast random access
Fast random access refers to how quickly you can decode a specific frame. It  is relevant for example, for a seamless experience when scrolling through the timeline of a video.

How is a random frame decoded? Let's focus on an example. With codecs like H.264 in its normal mode (which uses keyframes and interframes), to decode frame number 1247 the decoder would need to: 

1. Go to the nearest *preceding* keyframe (maybe frame 1200). 
2. Decode all 47 frames in between.

This may be slow in some cases, which is why some codecs can be set to "all-intra", meaning all frames are forced to be keyframes. If all frames are essentially standalone images, decoding any of them is fast. However, the file size will increase considerably.


### Frame-accurate seeking

Frame-accurate seeking means that, for a given video and tool used to read it, you can reliably and repeatably land on exactly the frame you request (e.g. frame 1247, not "somewhere near frame 1247").

Frame-accurate seeking is relevant, for example, when visualising manually annotated data overlaid on a video (e.g. keypoints). The annotations defined in frame 1247 should match the image data for that frame, but if frames are not reliably seekable, the video player may be showing a different underlying frame and the labels will seem "out of sync". 

Why may this be the case? It may happen due to:
- An **incomplete, corrupt or imprecise index** (i.e. the mapping from target timestamp to byte position is off).
- An **incorrect frame-to-time mapping**. E.g. if the video has variable frame rate, and the tool reading it assumes a constant one.
- A **video player or tool** that prioritises fast seeking at the expense of accuracy. E.g. if the frame to decode is a B-frame, you can't decode it without decoding the frames it depends on first. Some players or tools do "lazy seek" and simply display the nearest keyframe, rather than the exact frame requested.

To minimise these issues we can:
* use a mature container and codec combination that produces a reliable index,  
* be aware that some tools or video players cut corners for faster seeking. 

If the latter becomes an issue, we can solve it by setting all frames as keyframes ("all-intra") at the expense of a much larger file. A cheaper compromise is to reduce the GOP size: this would not eliminate the issue if the player does lazy seeking, but it would bound the error to at most `GOP size - 1` (249 frames off for a GOP of 250, but only 9 for a GOP of 10).

For the case of `ffmpeg` commands, the seeking behaviour (lazy or not) and its corresponding frame-accuracy guarantees vary depending on the *_order in which the seeking-related arguments_* are passed to the command. See [Common ffmpeg workflows](ffmpeg.md) for more details, and [Extracting a clip from a video](target-extracting-clip-from-video) for a specific example.


## References and further reading
- [Wikipedia: Video codec](https://en.wikipedia.org/wiki/Video_codec)
- [Loopbio blog: An Introduction to Video Compression](http://blog.loopbio.com/video-io-1-introduction.html)
- [FFMPEG's H.264 guide](https://trac.ffmpeg.org/wiki/Encode/H.264])
- [FFMPEG'S Frame accuracy when seeking](https://trac.ffmpeg.org/wiki/Seeking)
- [FFMPEG's CRF guide](https://trac.ffmpeg.org/wiki/Encode/H.264#a1.ChooseaCRFvalue)
- [Understanding rate control modes](https://slhck.info/video/2017/03/01/rate-control.html)
- [What is CRF](https://slhck.info/video/2017/02/24/crf-guide.html)
- [Workshop on digital video](https://github.com/leandromoreira/digital_video_introduction)
- ["Video Codecs 101" (video)](https://commons.wikimedia.org/wiki/File:Video_Codecs_101.webm) by Lou Quillio, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

- [AWS Blogs: GOPs explained](https://aws.amazon.com/blogs/media/part-1-back-to-basics-gops-explained/)
- Liu, H., Liu, W., Chi, Z., Wang, Y., Yu, Y., Chen, J., & Tang, J. (2022). Fast human pose estimation in compressed videos. IEEE Transactions on Multimedia, 25, 1390-1400.
- Mathis, A., & Warren, R. (2018). On the inference speed and video-compression robustness of DeepLabCut. [BioRxiv, 457242](https://www.biorxiv.org/content/10.1101/457242v1).
