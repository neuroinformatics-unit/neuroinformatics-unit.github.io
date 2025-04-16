(track-brainglobe)=
# Track: BrainGlobe

The BrainGlobe Initiative provides easy-to-use tools to analyse brain histology data (e.g. serial section two-photon, lightsheet).
This track will guide participants through hands-on tutorials to learn how to use BrainGlobe.

::: {admonition} Target audience
:class: note

This course is designed for researchers and students interested in learning about open-source tools for analysing brain microscopy data.
:::

## Course overview

__Tuesday morning:__
We will start with a high-level overview of BrainGlobe's ecosystem of computational neuroanatomy tools, and what they enable.
We will then recap some basic concepts of image analysis using `napari` and ensure everyone has a working installation of BrainGlobe.

__Tuesday afternoon:__
We will work through the following hands-on tutorials using BrainGlobe's `napari` graphical user interface.
- Registering whole-brain microscopy images with `brainreg`
- Segmenting structures in whole brain microscopy images with `brainglobe-segmentation`
- Detecting cells in large 3D images with `cellfinder`
- Analysing cell positions in atlas space
- Visualisation of data in atlas space

__Wednesday morning:__
We will introduce BrainGlobe's more advanced interfaces, including 
- command line for typical workflows.
- Python API to include BrainGlobe in your own scripts
- experimental user interfaces for stitching, subvolume registration and template-building.

__Wednesday afternoon:__
Participants are encouraged to run BrainGlobe on their own data, discuss possible uses with the development team and other participants or integrate BrainGlobe into their existing workflows.

## Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)
- [Adam Tyson](https://github.com/adamltyson)

## Pre-requisites

### Hardware
As this is a hands-on workshop, we recommend bringing your own laptop.

### Software
Please ensure you have the following installed:
- A Python IDE such as:
  - [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [PyCharm](https://www.jetbrains.com/pycharm/)
- A working `conda` (or `mamba`) installation. If you don't have it, install via [Miniforge](https://github.com/conda-forge/miniforge).
- A working [Git](https://git-scm.com/) installation.

We will email you at least a week before the event with instructions on installing any additional required software.

### Python knowledge
If you're new to Python, we recommend attending our __Intro to Python__ workshop on Monday, or completing an equivalent course beforehand.
This hands-on session will cover the basics, including data types, control flow, functions, and core libraries—a great way to get up to speed before this event.

### Data
Bringing your own data is encouraged but not required.
It's a great chance to get feedback on your data and learn from others.
If you don't have your own data, we will provide example datasets for you to work with.

We expect that participant-led ideas emerging from this track may inspire collaborative projects during the __Hackday__ on Friday.
