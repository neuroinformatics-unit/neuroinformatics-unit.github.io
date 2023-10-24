# Behaviour

## movement
[movement](https://movement.neuroinformatics.dev/) aims to **facilitate the study of animal behaviour in neuroscience** by providing a suite of **Python tools to analyse body movements** across space and time.

At its core, movement handles trajectories of *keypoints*, which are specific body parts of an *individual*. An individual's posture or *pose* is represented by a set of keypoint coordinates, given in 2D (x,y) or 3D (x,y,z). The sequential collection of poses over time forms *pose tracks*. In neuroscience, these tracks are typically extracted from video data using software like [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) or [SLEAP](https://sleap.ai/).

With movement, our vision is to present a consistent interface for pose tracks and to analyse them using modular and accessible tools. We aim to accommodate data from a range of pose estimation packages, in 2D or 3D, tracking a single or multiple individuals. The focus will be on providing functionalities for data cleaning, visualisation and motion quantification.

While movement isn't designed for behaviour classification or action segmentation, it may extract features useful for these tasks. We are planning to develop separate packages for this purpose, which will be compatible with movement and the existing ecosystem of related tools.
