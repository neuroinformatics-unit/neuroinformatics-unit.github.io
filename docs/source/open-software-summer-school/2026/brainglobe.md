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
- Registering whole-brain microscopy images with [`brainreg`](https://github.com/brainglobe/brainreg)
- Segmenting structures in whole brain microscopy images with [`brainglobe-segmentation`](https://github.com/brainglobe/brainglobe-segmentation)
- Detecting cells in large 3D images with [`cellfinder`](https://github./com/brainglobe/cellfinder)
- Analysing cell positions in atlas space with [`brainmapper`](https://github.com/brainglobe/brainglobe-workflows)
- Visualisation of data in atlas space with [`brainrender`](https://github.com/brainglobe/brainrender) and [`brainrender-napari`](https://github.com/brainglobe/brainrender-napari)

__Tuesday afternoon:__
We will introduce BrainGlobe's more advanced interfaces, including 
- Command line for typical workflows.
- Python API to include BrainGlobe in your own scripts
- Experimental tools for stitching, advanced registration and atlas building.

### Collaboration days

The final two days—**Thursday and Friday**—are dedicated to collaboration. We will join forces with participants from the **Extracellular Electrophysiology** track to work together on participant-led projects.

* **Skill building:** we'll start with a practical workshop on **Git and GitHub** to equip everyone with the necessary skills for collaborative coding.
* **Project-based work:** participants will self-organize into small teams to tackle projects hands-on. **Coding is not a requirement**; any idea that benefits from collaboration with other attendees is welcome. Potential project ideas include, but are not limited to:
    * *Apply a tool:* use any learned software to analyze a new dataset (your own or a public one).
    * *Give feedback:* report bugs and suggest features by raising issues on relevant open-source tools.
    * *Make a contribution:* submit a pull request to an open-source repository (support will be provided).
    * *Collaborative writing:* draft a white paper, blog post, or documentation together.
    * *Prototype an idea:* test a cool new analysis or method on real-world data.
* **Presentation:** you will have the opportunity to report your team's progress on the final afternoon.

## Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)
- [Adam Tyson](https://github.com/adamltyson)

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

We expect that participant-led ideas emerging from this track may inspire collaborative projects during the __Collaboration Days__ on Thursday and Friday.
