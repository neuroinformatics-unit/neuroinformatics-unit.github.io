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

__Tusday afternoon:__
We'll continue with a hands-on tutorial on using [SLEAP](https://sleap.ai/)—a popular software library for animal pose estimation and tracking.
The typical workflow, from annotating body parts to training a model and generating predictions, is common to most pose estimation tools, including [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut/).

__Wednesday:__
The second day will be dedicated to a practical tutorial on [movement](https://movement.neuroinformatics.dev)—a Python toolbox for analysing animal body movements across space and time.
You'll learn how to load, clean, visualise, and quantify motion tracks, and apply this knowledge to specific use cases through computational exercises.

## Instructors
- [Niko Sirmpilatze](https://github.com/niksirbi)
- [Sofía Miñano](https://github.com/sfmig)
- [Chang Huan Lo](https://github.com/lochhh)

## Pre-requisites

### Hardware
As this is a hands-on workshop, we recommend bringing your own laptop.
A mouse is also recommended for tasks like image annotation.
A dedicated GPU is __not__ required

### Software
Please ensure you have the following installed:
- A Python IDE such as:
  - [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [PyCharm](https://www.jetbrains.com/pycharm/)
  - [JupyterLab](https://jupyter.org/install)
- A working `conda` (or `mamba`) installation. If you don't have it, install via [Miniforge](https://github.com/conda-forge/miniforge).
- A working [Git](https://git-scm.com/) installation.

We will email you at least a week before the event with instructions on installing any additional required software.

### Python knowledge
If you're new to Python, we recommend attending our __Intro to Python__ workshop on Monday, or completing an equivalent course beforehand.
This hands-on session will cover the basics, including data types, control flow, functions, and core libraries—a great way to get up to speed before this event.

### Data
Bringing your own data is encouraged but not required.
This could include video recordings of animal behaviour and/or motion tracks you've already generated.
It's a great chance to get feedback on your data and learn from others.
If you don't have your own data, we will provide example datasets for you to work with.

We expect that participant-led ideas emerging from this track may inspire collaborative projects during the __Hackday__ on Friday.
