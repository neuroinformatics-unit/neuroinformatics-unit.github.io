(track-big-imaging-data)=
# Track: Big Imaging Data

As novel imaging methods such as light-sheet microscopy become more accessible, more researchers collect ever larger imaging data. Transforming this data into scientific insight requires the combined expertise of researchers, imaging facility staff and software engineers, but each of these communities are too often not well-linked to each other. This track aims to bring together image facility staff, imaging researchers and research software engineers to
* engage in hands-on tutorials to handle big microscopy data with open-source software
* build connections between the imaging and software engineering community

The Big Imaging Data track will include
* hands-on introductory tutorials to open-source libraries `zarr` and `dask`
* participant-led discussions of community, collaboration and careers in Big Imaging Data

::: {admonition} Target audience
:class: note

This course is designed for imaging facility staff, image analysts, and imaging researchers interested in getting hands-on experience in, and building community around, free open-source tools to process big imaging data.
:::

## Course overview

__Tuesday morning:__
The technical side of the track will start with an introduction to chunked file formats for big imaging data, such as `OME-zarr`.
We will then proceed to work on hands-on tutorials to
- read and write big imaging data using `zarr`
- process big imaging data lazily and in-parallel with `dask`

__Tuesday afternoon:__
The community side of the track will start with a very short introduction to existing community efforts in both software engineering [^1]_, imaging[^2]_ and image analysis[^3]_.
The participants will then join small discussion groups of their choice circling around the wider question: Where next for careers and community in Big Imaging Data?
The discussions will then be fed back to the wider group, and result in the publication of a blog after the course.

## Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)

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


[^1]: community initiatives around e.g. the [Software Sustainability Institute](https://www.software.ac.uk/), the [Society for Research Software Engineering](https://society-rse.org/about/history/), and The Hidden REF.
[^2]: For example [BioImagingUK](https://www.rms.org.uk/community/networks-affiliates/bioimaginguk-network.html), [Euro-BioImaging](https://www.eurobioimaging.eu/), [Global Bioimaging](https://globalbioimaging.org/)
[^3]: For example [neubias](https://eubias.org/NEUBIAS/), [GloBIAS](https://www.globias.org/)