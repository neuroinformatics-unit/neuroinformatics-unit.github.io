(track-animals-in-motion)=
# Track: Animals in Motion 

The study of animal behaviour has been transformed by the increasing use of
machine learning-based tools, such as DeepLabCut and SLEAP, which can track the
positions of animals and their body parts from video footage. These tools
have become widely accessible and are now used in a variety of fields,
including neuroscience, ethology, biomechanincs, or any field that requires
the analysis of animals move.

That said, the sheer variery of available tools can be overwhelming, and its
often difficult to know which tool is best suited for a particular
application and how to get started with it.

Moreover, the analysis seldom stops at tracking. Once motion tracks have
been generated, they need to be further processed, visualised and quantified,
in order to get from tracks to meaningful interpretable findings.

This track is aimed ar researchers and students who are interested in
learning about the latest tools for tracking animal motion, and extracting
meaning from the resulting data.


## Course overview

**Computer Vision approaches for animal tracking:** an introduction to current machine learning-based approaches for detecting and tracking animals in videos. We will cover the essential terminology and concepts, and provide an overview of the available tools.

**Pose estimation and tracking:** a hands-on tutorial for one of the most popular approaches for tracking animal motion: pose estimation and tracking.
We will go step-by-step through the workflow of annotating animal body parts, training a model, and running inference on new data to generate predicted motions tracks. We will use the SLEAP package to do that, but the workflow is similar for other packages, such as DeepLabCut.

**Analysing motion tracks:** a practical introduction to [movement](https://movement.neuroinformatics.dev)—an  We will cover the basics of the movement package, and then focus on specific use cases, which will be presented as computational exercises.
Once you have generated motion tracks, you need to process and visualise them. We will use the open-source Python package  to do that. This package provides a diverse set of
tools for loading, cleaning, visualising and quantifying animal motion tracks. We will cover the basics of the package, and then focus on specific use cases, which will be presented as computational exercises.

## Pre-requisites

### Hardware
As this is a hands-on workshop, we recommend that you bring your own laptop.
We also recommend bringing a mouse, as this will make some tasks,
such as image annotation, much easier. A dedicated graphics card (GPU)
is not required.

### Software
You will need an IDE (a code editor) for Python programming.
We recommend one of the following:
- [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [JupyterLab](https://jupyter.org/install)

A working conda (or mamba) installation. If you don't have it, install via [Miniforge](https://github.com/conda-forge/miniforge).

A working [Git](https://git-scm.com/) installation.

We will contact you at least a week before the event with instructions on
how to install some additional specific software packages.

### Python knowledge
If you new to coding with Python, we encourage attendance of our __Intro to Python__ workshop on Monday, or an equivalent course prior to the event. This will be a hands-on introduction to Python programming, and will cover the basics, including data types, control flow, functions, and libraries. This is a great opportunity to get up to speed with Python before the main event.

### Data
Bringing your own data is encouraged, but not strictly required. The data could be in the form of
video recordings of animal behaviour, and/or motion tracks you've already generated from videos.
This is a great opportunity to get help with your data and to learn from others.
We expect that participant-led ideas that gain traction from any of the sub-events above can be taken forward as ideas for the __Hackathon__ on Friday.

If you have no suitable data, we will provide some example datasets for you to work with.