# Projects
## Neuroanatomy
::::{grid} 1 1 1 1

:::{grid-item-card} BrainGlobe
:link: https://brainglobe.info/

The BrainGlobe Initiative exists to facilitate the development of interoperable Python-based tools for computational neuroanatomy.

We have three aims:

* Develop specialist software for specific analysis and visualisation needs
* Develop core tools to help others to build interoperable tools in Python
* Build a community of neuroscientists and developers to share knowledge, build software and engage with the scientific, and open-source community (e.g. by organising hackathons).
:::
::::

## Behaviour
::::{grid} 1 1 1 1

:::{grid-item-card} movement
:link: https://movement.neuroinformatics.dev/

movement aims to **facilitate the study of animal behaviour in neuroscience** by providing a suite of **Python tools to analyse body movements** across space and time.

At its core, movement handles trajectories of *keypoints*, which are specific body parts of an *individual*. An individual's posture or *pose* is represented by a set of keypoint coordinates, given in 2D (x,y) or 3D (x,y,z). The sequential collection of poses over time forms *pose tracks*. In neuroscience, these tracks are typically extracted from video data using software like DeepLabCut or SLEAP.

With movement, our vision is to present a consistent interface for pose tracks and to analyse them using modular and accessible tools. We aim to accommodate data from a range of pose estimation packages, in 2D or 3D, tracking a single or multiple individuals. The focus will be on providing functionalities for data cleaning, visualisation and motion quantification.

While movement isn't designed for behaviour classification or action segmentation, it may extract features useful for these tasks. We are planning to develop separate packages for this purpose, which will be compatible with movement and the existing ecosystem of related tools.
:::
::::

## Electrophysiology
::::{grid} 1 1 1 1
:::{grid-item-card} SpikeWrap
:link: https://github.com/neuroinformatics-unit/spikewrap
Spikewrap is a tool to simplify the execution and visualisation of extracellular electrophysiology pre-processing and spike-sorting pipelines. Taking input organised to our NeuroBlueprint standard, it will provide a flexible way to process an entire project's electrophysiological data with an easy-to-use interface.

Under the hood Spikewrap utilises the power of SpikeInterface, an open-source tool with many contributors in the electrophysiology analysis field. Spikewrap aims to abstract away the implementation details to allow researchers to test different pipeline configurations with the click of a button.

We actively contribute to the development of SpikeInterface, ensuring that our efforts benefit existing community projects.
:::
::::

## Data Management
::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card} NeuroBlueprint
:link: https://neuroblueprint.neuroinformatics.dev
NeuroBlueprint is a project folder structure specification designed for systems neuroscience in animal models.
It is inspired by, and based on the BIDS specification, widely used in human neuroimaging.

The NeuroBlueprint specification provides a set of rules and guidelines for project folder organisation, ensuring consistent data management within and between labs.
This standardisation makes data-sharing and collaboration much simpler, and allows sharing of analysis tools that can operate on predictable folder structures.

Read the specification on the website, or discuss and contribute at GitHub.
:::

:::{grid-item-card} DataShuttle
:link: https://datashuttle.neuroinformatics.dev
Datashuttle is a neuroscience-project manager tool that simplifies building project folders and transferring data.

Datashuttle includes tools for automated generation and transfer of project folders formatted to the NeuroBlueprint specification.

It also contains features to assist in data transfer, including:
* Manage files across multiple data-collection computers by synchronising
  all data to with a centrally stored project.
* Easily manage data transfers for processing and analysis by selecting only a sub-set of data to move (e.g. specific subjects, sessions or data types).
:::

::::

## Developer Tools
::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card} Python Cookiecutter
:link: https://github.com/neuroinformatics-unit/python-cookiecutter
The Python Cookiecutter template allows quick and easy setup of new python projects.
Projects built using this template contain pre-set configurations for code quality checks, formatting,
automated testing (pytest, both locally and through GitHub Actions), versioning and release on PyPI.
:::

:::{grid-item-card} Actions
:link: https://github.com/neuroinformatics-unit/actions
The actions repository hosts reliable, maintained and versioned GitHub Actions
workflows for common tasks such as linting, testing, and releasing Python projects to PyPI.
:::
::::
