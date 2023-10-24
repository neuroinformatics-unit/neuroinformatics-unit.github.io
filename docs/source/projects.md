# Projects
## Neuroanatomy
::::{grid} 1 1 1 1

:::{grid-item-card} BrainGlobe
:link: https://brainglobe.info/

The BrainGlobe Initiative exists to facilitate the development of interoperable Python-based tools for computational 
neuroanatomy with three core aims:

* Develop specialist software for specific analysis and visualisation needs
* Develop core tools to help others to build interoperable tools in Python
* Build a community of neuroscientists and developers to share knowledge, build software and engage with the scientific, 
and open-source community (e.g., by organising hackathons).
:::
::::

## Behaviour
::::{grid} 1 1 1 1

:::{grid-item-card} movement
:link: https://movement.neuroinformatics.dev/

Pose estimation tools (such as DeepLabCut and SLEAP) are now commonplace when processing video data of animal 
behaviour. There is not yet a standardised, easy to use way to process the pose tracks from these software packages.

movement aims to provide a consistent modular interface to analyse pose tracks, allowing steps such as data cleaning, 
visualisation and motion quantification. We aim to support a range of pose estimation packages, along with 2D or 3D 
tracking of single or multiple animals. 

:::
::::

## Electrophysiology
::::{grid} 1 1 1 1
:::{grid-item-card} SpikeWrap
:link: https://github.com/neuroinformatics-unit/spikewrap
Spikewrap simplifies the execution and visualisation of extracellular electrophysiology pre-processing and 
spike-sorting pipelines. Taking input organised to our NeuroBlueprint standard, it provides an easy and flexible way to 
process extracellular electrophysiology data from multiple subjects and sessions. 

SpikeWrap is built upon SpikeInterface, abstracting away the implementation details to allow researchers to easily 
test different pipeline configurations.

:::
::::

## Data Management
::::{grid} 1 1 1 1
:gutter: 3

:::{grid-item-card} NeuroBlueprint
:link: https://neuroblueprint.neuroinformatics.dev
NeuroBlueprint is a project folder structure specification designed for systems neuroscience in animal models.
It is inspired by, and based on the BIDS specification, widely used in human neuroimaging.

The NeuroBlueprint specification provides a set of rules and guidelines for project folder organisation, ensuring 
consistent data management within and between labs.
This standardisation makes data-sharing and collaboration much simpler, and allows sharing of analysis tools that 
can operate on predictable folder structures.
:::

:::{grid-item-card} DataShuttle
:link: https://datashuttle.neuroinformatics.dev
DataShuttle is a tool for automated generation of project folders formatted to the NeuroBlueprint specification. 
It also allows these folders to be easily synchronised between computers.
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
