(track-brainglobe-2026)=
# Track: BrainGlobe

Modern microscopy techniques allow the acquisition of large-scale multidimensional datasets which enables unbiased investigation of brain structure and function. 
However, the analysis of such datasets often requires specialised computational tools and expertise.

The [BrainGlobe Initiative](https://brainglobe.info) addresses this by providing easy-to-use tools to analyse large-scale brain histology data and transform it to a common coordinate space in a species agnostic manner.
This track will cover basic concepts of image analysis using [`napari`](https://napari.org/stable/), brain atlases and common coordinate spaces, and guide participants through hands-on tutorials to learn how to use the BrainGlobe ecosystem of computational neuroanatomy tools.

::: {admonition} Target audience
:class: note

This course is designed for researchers who have acquired or expect to acquire large brain histology datasets. 
It is aimed at those interested in learning about open-source tools for analysing and visualising large microscopy datasets with a specific focus on the BrainGlobe ecosystem.
:::

## Course overview

### Core workshop

We will cover the following topics from **Monday to Wednesday**:

* **Introduction:** a high level overview of the BrainGlobe ecosystem of computational neuroanatomy tools, and what they enable.
* **Image analysis in `napari`:** basic concepts of image analysis using [`napari`](https://napari.org/stable/).
* **Working in a common coordinate space:** a primer on brain atlases, common coordinate spaces and image registration, followed by a hands-on tutorial using [`brainreg`](https://github.com/brainglobe/brainreg) and [`brainglobe-registration`](https://github.com/brainglobe/brainglobe-registration) to map data to a BrainGlobe atlas.
* **Hands-on tutorials:** we will work through the following hands-on tutorials using BrainGlobe's `napari` graphical user interface:
  * Segmenting structures in whole brain microscopy images with [`brainglobe-segmentation`](https://github.com/brainglobe/brainglobe-segmentation).
  * Detecting cells in large 3D images with [`cellfinder`](https://github.com/brainglobe/cellfinder).
  * Analysing cell positions in atlas space with [`brainmapper`](https://github.com/brainglobe/brainglobe-workflows).
  * Visualisation of data in atlas space with [`brainrender`](https://github.com/brainglobe/brainrender) and [`brainrender-napari`](https://github.com/brainglobe/brainrender-napari).
* **Programmatic access:** an introduction to interacting with the BrainGlobe ecosystem via scripting and the command line.

### Collaboration days

The final two days—**Thursday and Friday**—are dedicated to collaboration. We will join forces with participants from the **Extracellular Electrophysiology** track to work together on participant-led projects.

* **Skill building:** we'll start with a practical workshop on **Git and GitHub** to equip everyone with the necessary skills for collaborative coding.
* **Project-based work:** participants will self-organize into small teams to tackle projects hands-on. **Coding is not a requirement**; any idea that benefits from collaboration with other attendees is welcome. Potential project ideas include, but are not limited to:
    * *Apply a tool:* use your new skills to analyze a new dataset (your own or a public one).
    * *Give feedback:* report bugs and suggest features by raising issues on relevant open-source tools.
    * *Make a contribution:* submit a pull request to an open-source repository (support will be provided).
    * *Collaborative writing:* draft a white paper, blog post, or documentation together.
    * *Prototype an idea:* test a cool new analysis idea or method on real-world data.
* **Presentation:** you will have the opportunity to report your team's progress on the final afternoon.

## Confirmed Instructors
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
