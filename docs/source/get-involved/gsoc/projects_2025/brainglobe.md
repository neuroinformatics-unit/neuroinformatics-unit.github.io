# GSoC NIU Projects 2025: BrainGlobe

[BrainGlobe](https://brainglobe.info) is a community-driven suite of open-source Python tools. The BrainGlobe tools are widely used to process, analyse and visualise images of brains (and other related data) in neuroscientific research.
If you are interested in any of these projects, [get in touch](https://brainglobe.info/contact.html)! Feel free to open a new topic on [Zulip](https://brainglobe.zulipchat.com/) and tag the potential mentors.

Our working language is English, but our mentors for these projects also speak Italian, French, and German.

:::{dropdown} {fas}`brain;sd-text-primary` Improve `cellfinder`'s classification algorithm
<!-- Description -->

The [BrainGlobe `cellfinder` tool](https://brainglobe.info/documentation/cellfinder/index.html) is used to detect cells in large whole-brain images. It uses traditional image processing to find possible cell candidates and passes them to a customisable classifier to split the candidates into cells and no-cells. `cellfinder` relies heavily on `pytorch` and `keras`.

`cellfinder` currently uses a residual neural network (ResNet) to classify cell candidates, and deep learning network architectures have progressed since. In this project, you will explore newer architectures for the classification network as alternatives to ResNet, and see whether they work better and/or faster than the existing implementation.


**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A Python implementation of at least one new Deep Learning network architecture in `cellfinder`
- Quantitative comparison between the current and new architecture
- Tests to cover any added functionality.
- Documentation for the new functionality.
- A [blog](https://brainglobe.info/blog) explaining the new network and its advantages and disadvantages.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours) or Large (~350 hours).

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate contributor to open source.

**Required skills**

- Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).
- At least initial understanding of machine learning algorithms

**Nice-to-haves**
- Experience working with machine learning frameworks, in particular `keras` or `pytorch`
- Experience working with image data


**Potential mentors**
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)
- [@alessandrofelder](https://github.com/alessandrofelder)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [BrainGlobe developer guide](https://brainglobe.info/community/developers/index.html)
- [cellfinder paper](https://doi.org/10.1371/journal.pcbi.1009074)
- [cellfinder code](https://github.com/brainglobe/cellfinder)
:::

:::{dropdown} {fas}`brain;sd-text-primary` `cellfinder` support for two-dimensional brain images
<!-- Description -->
The [BrainGlobe `cellfinder` tool](https://brainglobe.info/documentation/cellfinder/index.html) is used to detect cells in large whole-brain images. It uses traditional image processing to find possible cell candidates and passes them to a customisable classifier to split the candidates into cells and no-cells. `cellfinder` relies heavily on `pytorch` and `keras`.

`cellfinder` currently uses a residual neural network (ResNet) to classify cell candidates. This network is designed for three-dimensional whole-brain images, but neuroscientists often take images of two-dimensional slices of the brain. In this project, you would adapt `cellfinder` to support two-dimensional data. This would involve implementing a new neural network suitable for two-dimensional images, as well as refactoring some of the image processing code.


**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A modified implementation of the existing image processing algorithm (blob detection) in `cellfinder` that detects cell candidates in both two- and three-dimensional images
- A Python implementation of a neural network in `cellfinder` that classifies cell candidates from two-dimensional images.
- Tests to cover any added functionality.
- Documentation for the new functionality.
- A [blog](https://brainglobe.info/blog) showcasing the use of `cellfinder` on two-dimensional images of brains.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours).

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate contributor to open source.

**Required skills**

- Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).
- At least initial understanding of machine learning algorithms

**Nice-to-haves**
- Experience working with machine learning frameworks, in particular `keras` or `pytorch`
- Experience working with image data


**Potential mentors**
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)
- [@alessandrofelder](https://github.com/alessandrofelder)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [BrainGlobe developer guide](https://brainglobe.info/community/developers/index.html)
- [cellfinder paper](https://doi.org/10.1371/journal.pcbi.1009074)
- [cellfinder code](https://github.com/brainglobe/cellfinder)
:::

:::{dropdown} {fas}`brain;sd-text-primary` `cellfinder` support for arbitrary number of channels
<!-- Description -->
The [BrainGlobe `cellfinder` tool](https://brainglobe.info/documentation/cellfinder/index.html) is used to detect cells in large whole-brain images. It uses traditional image processing to find possible cell candidates and passes them to a customisable classifier to split the candidates into cells and no-cells. `cellfinder` relies heavily on `pytorch` and `keras`.

`cellfinder` was originally designed to work with two channels: the "background" channel and the "signal" channel. This is a limitation, because sometimes only the signal channel is acquired, or there are several signal channels containing useful information. In this project, you would explore ways to allow `cellfinder` to classify cells based on information from an arbitrary number of channels. This could allow cellfinder to not just detect cells, but classify their type based on their shape and other features. 

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A modified implementation of the existing image processing algorithm (blob detection) in `cellfinder` that can detect cell candidates from an arbitrary number of channels. 
- A modified implementation of the neural network in `cellfinder` that can classify cell candidates from brain images with an arbitrary number of channels.
- Tests to cover any added functionality.
- Documentation for the new functionality.
- A [blog](https://brainglobe.info/blog) showcasing the use of `cellfinder` on images with 1 or 3 channels.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours).

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate contributor to open source.

**Required skills**
- Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).
- At least initial understanding of machine learning algorithms

**Nice-to-haves**
- Experience working with machine learning frameworks, in particular `keras` or `pytorch`
- Experience working with image data


**Potential mentors**
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)
- [@alessandrofelder](https://github.com/alessandrofelder)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [BrainGlobe developer guide](https://brainglobe.info/community/developers/index.html)
- [cellfinder paper](https://doi.org/10.1371/journal.pcbi.1009074)
- [cellfinder code](https://github.com/brainglobe/cellfinder)
:::


:::{dropdown} {fas}`brain;sd-text-primary` Add to BrainGlobe's data visualisation tools
<!-- Description -->
The [BrainGlobe `brainrender` tool](https://brainglobe.info/documentation/brainrender/index.html) is widely used to visualise brain data in a common coordinate space defined by a "brain atlas" (We refer to this data as "atlas-registered" data). However, `brainrender` is inaccessible to people without programming skills. The [`brainrender-napari` tool](https://brainglobe.info/tutorials/visualise-atlas-napari.html) aims to make `brainrender` functionality available to more people through a plugin for the popular open-source graphical image viewer [napari](https://napari.org/stable/). 

Although `brainrender` and `brainrender-napari` share some functionality, some publicly available atlas-registered data is not yet available in `brainrender-napari`. In this project, we would implement code to allow users to visualise publicly available atlas-registered data from mouse and fish brains in `brainrender-napari`

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A Python implementation of a `napari` widget that allows users to download and visualise atlas-registered data.
- Tests to cover any added functionality.
- Documentation for the new functionality.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Small (~90 hours) or Medium (~175 hours).

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a student or a beginner contributor to open source.

**Required skills**
- Experience with Python.


**Nice-to-haves**
- Experience working with data visualisation
- Experience working with image data


**Potential mentors**
- [@alessandrofelder](https://github.com/alessandrofelder)
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [BrainGlobe developer guide](https://brainglobe.info/community/developers/index.html)
- [brainrender paper](https://doi.org/10.7554/eLife.65751)
- [brainrender code](https://github.com/brainglobe/brainrender)
- [brainrender-napari code](https://github.com/brainglobe/brainrender)
- [napari usage tutorials](https://napari.org/stable/tutorials/index.html).
- [napari Plugin documentation](https://napari.org/stable/plugins/index.html), particularly the section on [Building a plugin](https://napari.org/stable/plugins/building_a_plugin/index.html).
:::