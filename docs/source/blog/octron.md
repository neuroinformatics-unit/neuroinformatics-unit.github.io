:blogpost: true
:date: April 17, 2026
:author: Sofía Miñano
:location: London, UK
:category: Blog
:language: English
:image: 1

(target-niu-octron)=
# We are working with OCTRON!
*Expanding our collaborations across the animal behaviour ecosystem*

```{image} /_static/blog_images/octron-colab/octron-niu-3.png
:align: center
:width: 70%
```

<br>

We are excited to announce that the [Neuroinformatics Unit](target-home) is teaming up with [OCTRON](https://octron-tracking.github.io/OCTRON-docs/)!

## What is OCTRON?

[OCTRON](https://octron-tracking.github.io/OCTRON-docs/) is a computer vision Python package for segmenting, detecting and tracking animals in videos of behavioural experiments. Originally developed by [Horst Obenhaus](https://github.com/horsto), it wraps foundation models such as [SAM2](https://github.com/facebookresearch/sam2) and [SAM3](https://ai.meta.com/sam3/) in a [napari](https://napari.org)-based pipeline to accelerate the annotation of masks and bounding boxes. It then uses those annotations to train smaller, more portable [YOLO](https://www.ultralytics.com/yolo) models that users can run on their own data.

We think OCTRON is an innovative contribution to the animal behaviour ecosystem: it dramatically accelerates the generation of training data and turns heavy foundation models into tools that lab scientists can use effectively. It is also a great example of the power of open source, stitching together excellent existing libraries, such as [BoxMOT](https://github.com/mikel-brostrom/boxmot) for tracking detections across frames or [Ultralytics](https://github.com/ultralytics/ultralytics) for training YOLO detectors, into a cohesive, scientist-friendly tool.

## Why this collaboration?

Supporting OCTRON is a natural fit for our [mission](https://neuroinformatics.dev/about.html) of empowering scientists with accessible computational tools and facilitating collaboration across the neuroscience community. It also complements our existing behaviour tools nicely: [movement](https://movement.neuroinformatics.dev) covers the steps downstream of pose estimation and detection, while [ethology](https://ethology.neuroinformatics.dev) supports the curation of manual annotations.

## What's the plan?

Over the coming months, we will work alongside the OCTRON team to:

- Make the package more **maintainable** and easier to contribute to, bringing it in line with the NIU software practices and standards.
- Improve **interoperability** with other tools in the NIU suite, such as [movement](https://movement.neuroinformatics.dev).
- Make OCTRON more **accessible** to users across a range of programming backgrounds.
- Contribute **novel approaches** on the scientific side, expanding the feature set of the tool, as this is a joint collaboration in both software and science.

As always, all of this development will happen in the open.

## Stay tuned

Keep an eye on the [OCTRON repository](https://github.com/OCTRON-tracking/OCTRON-gui) and our [Zulip](https://neuroinformatics.zulipchat.com/) for updates.
