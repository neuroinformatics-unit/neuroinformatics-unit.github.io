(track-animals-in-motion)=
# Track: Animals in Motion

Machine learning methods for motion tracking have transformed a wide range of scientific disciplines—from neuroscience and biomechanics to conservation and ethology.
Tools such as [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut/) and [SLEAP](https://sleap.ai/) enable researchers to track animal movements in video recordings with impressive accuracy, without the need for physical markers.

However, the variety of available tools can be overwhelming.
It's often unclear which tool is best suited to a given application, or how to get started.
Moreover, generating motion tracks is only the first step:
these tracks must then be further processed, visualised, and analysed to yield meaningful
and interpretable insights into animal behaviour.

::: {admonition} Target audience
:class: note

This course is designed for researchers and students interested in learning about the latest free open-source tools for tracking animal motion from video footage and extracting quantitative descriptions of behaviour from motion tracks.
:::

## Course overview

__Tuesday morning:__
We'll start with a primer on Computer Vision approaches for detecting and tracking animals in videos.
We'll also cover key concepts and terminology, and provide an overview of the most widely used tools.

__Tuesday afternoon:__
We'll continue with a hands-on tutorial on using [SLEAP](https://sleap.ai/)—a popular software library for animal pose estimation and tracking.
The typical workflow, from annotating body parts to training a model and generating predictions, is common to most pose estimation tools, including [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut/).

__Wednesday:__
The second day will be dedicated to a practical tutorial on [movement](https://movement.neuroinformatics.dev)—a Python toolbox for analysing animal body movements across space and time.
You'll learn how to load, clean, visualise, and quantify motion tracks, and apply this knowledge to specific use cases through computational exercises.

::: {admonition} Course materials
:class: note

All course materials will be made available at <https://animals-in-motion.neuroinformatics.dev/latest/> during the workshop and will remain accessible afterwards.

The source code for the course materials is publicly hosted at <https://github.com/neuroinformatics-unit/course-animals-in-motion>.
:::

## Instructors
- [Niko Sirmpilatze](https://github.com/niksirbi)
- [Sofía Miñano](https://github.com/sfmig)
- [Chang Huan Lo](https://github.com/lochhh)

(target-animals-in-motion-prerequisites)=
## Prerequisites

### Hardware
This is a hands-on course, so please bring your own **laptop** and **charger**.
A **mouse** is strongly recommended, especially for tasks like image annotation.
A dedicated **GPU is not required**, though it may speed up some computations.

### Software
For general software requirements, please see the [prerequisites](target-general-prerequisites) on the main event page and make sure you have these installed and properly configured.

In addition to the general tools, you will need to install
the following specialised software:

::::{tab-set}

:::{tab-item} SLEAP

Please install [SLEAP](https://sleap.ai/) following the [official installation instructions](https://sleap.ai/installation.html).

For this workshop, use **SLEAP version 1.3.4**. Be sure to replace the default version number (e.g. 1.4.1) in the instructions with 1.3.4.

This should create a `conda` environment named `sleap` with the necessary dependencies. You can verify the installation by running:

```bash
conda activate sleap
sleap-label
```
This should launch the SLEAP graphical user interface (GUI).

:::

:::{tab-item} movement

You will also need a separate `conda` environment to use for interactive coding exercises.
This environment will include the [movement](https://movement.neuroinformatics.dev/) and [jupyter](https://jupyter.org/) packages.

We recommend cloning the workshop's GitHub repository and creating the environment using the provided `environment.yaml` file:

```bash
git clone https://github.com/neuroinformatics-unit/animals-in-motion.git
cd animals-in-motion
conda env create -n animals-in-motion-env -f environment.yaml
```

To test your setup, run:
```bash
conda activate animals-in-motion-env
movement launch
```

This should open the [movement GUI](https://movement.neuroinformatics.dev/user_guide/gui.html), i.e. the [napari](https://napari.org/) image viewer with the `movement` plugin docked on the right.

There are other ways to [install the movement package](https://movement.neuroinformatics.dev/user_guide/installation.html).
However, for this workshop, we recommend using the `environment.yaml` file to ensure that all necessary dependencies, including those beyond `movement`, are included.

:::

::::

### Python knowledge
If you're new to Python, we recommend attending our __Intro to Python__ workshop on Monday, or completing an equivalent course beforehand.
This hands-on session will cover the basics, including data types, control flow, functions, and core libraries—a great way to get up to speed before this event.

### Data
Bringing your own data is encouraged but not required.
This could include video recordings of animal behaviour and/or motion tracks you've already generated.
It's a great chance to get feedback on your data and learn from others.
If you don't have your own data, we will provide example datasets for you to work with.

We expect that participant-led ideas emerging from this track may inspire collaborative projects during the __Hackday__ on Friday.
