# Behaviour

## movement
[movement](https://movement.neuroinformatics.dev/) aims to **facilitate the study of animal behaviour in neuroscience** by providing a suite of **Python tools to process body movement data** across space and time.

At its core, movement processes trajectories of *keypoints*, which are specific body parts of an *individual*. An individual's posture or *pose* in a given frame is represented by a set of keypoint coordinates, which are given in 2D (x,y) or 3D (x,y,z). The sequential collection of poses over time is referred to as *pose tracks*. In the field of neuroscience, pose tracks are typically extracted from video data using tools like [DeepLabCut](http://www.mackenziemathislab.org/deeplabcut) or [SLEAP](https://sleap.ai/).

movement's goal is to offer a **unified interface for pose tracks** and to **process them via modular and accessible tools**. We aim to support data produced by a variety of pose estimation tools, in **2D or 3D space**, tracking a **single or multiple individuals**. The focus will be on providing functionalities for data cleaning, visualisation and motion quantification.

Movement is not designed for behaviour classification or action segmentation, but it may extract features useful for these tasks. We are planning to develop separate tools for these purposes, which will be compatible with movement.
