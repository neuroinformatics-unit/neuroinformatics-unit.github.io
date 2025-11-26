(track-brainglobe-2026)=
# Track: BrainGlobe

The [BrainGlobe Initiative](https://brainglobe.info) provides easy-to-use tools to analyse brain histology data, particularly from whole-brain imaging methods (e.g. serial section two-photon, lightsheet).
This track will guide participants through hands-on tutorials to learn how to use BrainGlobe.

::: {admonition} Target audience
:class: note

This course is designed for researchers and students interested in learning about open-source tools for analysing and visualising brain microscopy data.
:::

## Course overview

__Monday morning:__
We will start with a high-level overview of BrainGlobe's ecosystem of computational neuroanatomy tools, and what they enable.
We will then recap some basic concepts of image analysis using `napari` and ensure everyone has a working installation of BrainGlobe.

__Tuesday morning:__
We will work through the following hands-on tutorials using BrainGlobe's `napari` graphical user interface.
- Registering whole-brain microscopy images with `brainreg`
- Segmenting structures in whole brain microscopy images with `brainglobe-segmentation`
- Detecting cells in large 3D images with `cellfinder`
- Analysing cell positions in atlas space with `brainmapper`
- Visualisation of data in atlas space with `brainrender` and brainrender-napari`

__Tuesday afternoon:__
We will introduce BrainGlobe's more advanced interfaces, including 
- Command line for typical workflows.
- Python API to include BrainGlobe in your own scripts
- Experimental tools for stitching, advanced registration and atlas building.

__Wednesday:__
Participants are encouraged to run BrainGlobe on their own data, discuss use cases with the development team and other 
participants or integrate BrainGlobe into their existing workflows.

## Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)
- [Adam Tyson](https://github.com/adamltyson)

Slides are [available online](https://brainglobe.info/course-whole-brain-microscopy-analysis/).

(target-brainglobe-prerequisites-2026)=
## Prerequisites

### Hardware
As this is a hands-on workshop, you will need to bring your own laptop. Any fairly recent laptop will be suitable, you don't need a GPU etc.

### Python knowledge
The only prerequisite is a basic knowledge of programming in Python, and the scientific Python ecosystem. For those without
this background, the [preparatory month](https://neuroinformatics.dev/open-software-summer-school/index.html#preparatory-month) 
will equip you with all the skills needed to make the most of this course. 

### Data
Bringing your own data is encouraged but not required.
It's a great chance to get feedback on your data and learn from others.
If you don't have your own data, we will provide example datasets for you to work with.

We expect that participant-led ideas emerging from this track may inspire collaborative projects during the __Hackday__ on Friday.
