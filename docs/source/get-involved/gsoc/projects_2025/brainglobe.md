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

:::{dropdown} {fas}`brain;sd-text-primary` Update atlas packaging scripts to atlas API v2
<!-- Description -->
[Neuroanatomical atlases](https://neuroinformatics.dev/slides-templates-atlases/#/on-templates-and-atlases) define a common coordinate space for the brain, and have been created for many species (mouse, fish, ...) and imaging modalities (MRI, lightsheet microscopy, ...). A central piece of BrainGlobe's ecosystem is the BrainGlobe Atlas API. Importantly, the Atlas API allows the use of any BrainGlobe tool with [many publicly available atlases](https://brainglobe.info/documentation/brainglobe-atlasapi/index.html), by exposing them through the same, consistent Python interface. This is possible thanks to [packaging scripts](https://github.com/brainglobe/brainglobe-atlasapi/tree/main/brainglobe_atlasapi/atlas_generation/atlas_scripts) contributed by the community, that convert public data to a standard format.

The standard format is somewhat limited, and we improve its utility by adhering [to a new community standard for neuroanatomical atlases, "OpenMINDS SANDS"](https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/SANDS/atlas/brainAtlas.html).

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- Modifying atlas packaging Python code to write to OpenMINDS SANDS
- Adapting at least one packaging script to use the new functionality.
- Tests to cover any added/changed functionality.
- Documentation for the new functionality.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours) or Large (~350 hours).

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a student or a beginner contributor to open source.

**Required skills**
- Experience with Python.


**Nice-to-haves**
- Experience working with data standards or data schema
- Experience working with image data

**Potential mentors**
- [@alessandrofelder](https://github.com/alessandrofelder)
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [BrainGlobe atlas API paper](https://doi.org/10.21105/joss.02668)
- [Getting started with OpenMINDS](https://openminds-documentation.readthedocs.io/en/v3.0/shared/getting_started.html)
- [OpenMINDS SANDS BrainAtlas specification](https://openminds-documentation.readthedocs.io/en/v3.0/schema_specifications/SANDS/atlas/brainAtlas.html)
:::


:::{dropdown} {fas}`brain;sd-text-primary` `brainglobe-registration`
<!-- Description -->
The [BrainGlobe `brainglobe-registration` tool](https://github.com/brainglobe/brainglobe-registration) is used to register 2D and 3D images to a common coordinate space defined by an atlas ([`brainglobe-atlasapi'](https://github.com/brainglobe/brainglobe-atlasapi)). This is a crucial step in many neuroscientific analyses, as it allows data from different experiments to be compared and combined.

The current implementation relies on a manual selection of the specific 2D region, or 3D subvolume of the atlas to be used as the registration target. This is a time-consuming process, and can be error-prone. In this project, you would implement and compare methods to automatically select the region to be registered, based on the data itself. This could be done by using an adaptive grid search, ML based techniques, or Bayesian optimisation.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A new preprocessing step in `brainglobe-registration` that automatically selects the region of the atlas to be used as the registration target.
- Quantitative comparison between at least two different methods for selecting the region.
- Tests to cover any added functionality.
- Documentation for the new functionality.
- A [blog](https://brainglobe.info/blog) showcasing the new functionality.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours) or Large (~350 hours) depending on experience.

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate contributor to open source.

**Required skills**
- Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html).
- At least initial understanding of machine learning algorithms

**Nice-to-haves**
- Experience with image registration
- Experience with `ITK` or `elastix`
- Experience working with image data


**Potential mentors**
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)
- [@alessandrofelder](https://github.com/alessandrofelder)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [BrainGlobe developer guide](https://brainglobe.info/community/developers/index.html)
- [elastix manual (pdf)](https://github.com/SuperElastix/elastix/releases/download/5.2.0/elastix-5.2.0-manual.pdf)
- [Bayesian optimisation](https://bayesian-optimization.github.io/BayesianOptimization/2.0.3/)
:::