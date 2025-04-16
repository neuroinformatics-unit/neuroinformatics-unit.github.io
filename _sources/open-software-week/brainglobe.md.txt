(track-brainglobe)=
# Track: BrainGlobe

The [BrainGlobe Initiative](https://brainglobe.info) provides easy-to-use tools to analyse brain histology data, particularly from whole-brain imaging methods (e.g. serial section two-photon, lightsheet).
This track will guide participants through hands-on tutorials to learn how to use BrainGlobe.

::: {admonition} Target audience
:class: note

This course is designed for researchers and students interested in learning about open-source tools for analysing and visualising whole-brain microscopy data.
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
- Analysing cell positions in atlas space with `brainmapper`
- Visualisation of data in atlas space with `brainrender` and brainrender-napari`

__Wednesday morning:__
We will introduce BrainGlobe's more advanced interfaces, including 
- Command line for typical workflows.
- Python API to include BrainGlobe in your own scripts
- Experimental tools for stitching, advanced registration and atlas building.

__Wednesday afternoon:__
Participants are encouraged to run BrainGlobe on their own data, discuss use cases with the development team and other participants or integrate BrainGlobe into their existing workflows.

## Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)
- [Adam Tyson](https://github.com/adamltyson)

## Pre-requisites

### Hardware
As this is a hands-on workshop, you will need to bring your own laptop. Any fairly recent laptop will be suitable, you don't need a GPU etc.

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

### Apply now!

Fill in [this Google form](https://forms.gle/2UAAzikhSgYArZpX7) to apply. We unfortunately have limited space to accommodate participants. To maximise our impact, we aim to select participants that would benefit the most from the event, and that can bring the experience back to a diverse set of fields. Please be specific in your application and tailor it to the main track(s) that you are planning to attend. There is funding for travel and accommodation available. Applicants will be informed of the outcome by early July.