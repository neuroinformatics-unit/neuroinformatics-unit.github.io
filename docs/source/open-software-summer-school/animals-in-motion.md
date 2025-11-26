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

![](/_static/osw_images/animals-in-motion-overview.png)

### Monday

__morning:__
We'll start with a brief overview of common workflows and tools for analysing animal behaviour, to give you a sense of the big picture.
We'll follow that up with a primer on deep learning for computer vision, going over the key concepts and technologies that underpin most markerless tracking approaches.

__afternoon:__
You will have a chance to present a poster about your work at our symposium event, which will be held jointly with participants from the __Large Array Data__ track of the summer school. It's a great opportunity to get to know each other and explore potential synergies.

### Tuesday:

__morning:__ I
We'll continue with a hands-on tutorial on using [SLEAP](https://sleap.ai/)—a popular software library for animal pose estimation and tracking.
The typical workflow, from annotating body parts to training a model and generating predictions, is common to most pose estimation tools, including [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut/).

__afternoon:__
We will examine the motion tracks predicted by SLEAP, and explore methods for cleaning, visualising, and quantifying them using [movement](https://movement.neuroinformatics.dev)—a Python toolbox we develop.
We will quantify various aspects of motion, such as speed, orientation, distance travelled, etc.


### Wednesday

__morning:__
We will start the day by reviewing a few real-world case studies that illustrate how markerless motion tracking can be applied to answer scientific questions.

__afternoon:__
After lunch, we will give a brief theoretical introduction to behaviour segmentation methods that aim to decompose continuous motion into discrete units of behaviour. We will follow that up with a hands-on tutorial of a specific supervised behaviour segmentation tool.

### Thursday & Friday

These two __Collaboration Days__ are all about working together, so we'll rejoin forces with participants from the __Large Array Data__ track. We expect that participant-led ideas emerging from the two tracks will inspire and motivate interesting projects.

We will start off Thursday with a workshop on Git and GitHub, to set everyone up with the necessary skills that smooth collaborative working, especially when code is involved.

After that we'll self-organise into small teams to tackle projects of interest hands-on and together, in a fun atmosphere.

__Projects don't need to involve coding.__ As long as it's something that would benefit from collaboration with other summer school participants, it's fair game! Here are a few examples of the kinds of projects that could be a great fit:

- **Apply a tool:** Use any software you learned about during the week to analyse an interesting dataset (your own or a public one).
- **Give feedback:** Raise issues on relevant open-source tools. Suggest missing features, report bugs, or flag unclear documentation.
- **Make a contribution:** Submit a pull request to an open-source repository. If it's your first time, don't worry; there'll be plenty of people around to support you.
- **Collaborative writing:** Draft something together, like a blog post, white paper, or improved documentation.
- **Prototype an idea:** Try out a cool new analysis or method on real-world data and share your findings.

We're looking forward to seeing what you come up with! You will get the chance to present your progress on Friday afternoon.


::: {admonition} Course handbook
:class: note

All course materials will be made available as part of the online handbook at <https://animals-in-motion.neuroinformatics.dev> and will remain accessible afterwards.

You are welcome to inspect the handbook and get a sense of its contents, but keep in mind that the materials will be updated and expanded before the 2026 event.

The source code for the handbook is publicly hosted at <https://github.com/neuroinformatics-unit/course-animals-in-motion>.
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
See the [software prerequisites](https://animals-in-motion.neuroinformatics.dev/dev/prerequisites.html#sec-software) section of the course handbook for detailed instructions on installing and configuring the required software. The prerequisites will be updated before the event, and accepted participants will be reminded to complete the setup in advance.

### Python knowledge
If you're new to Python, we recommend signing up for our [asynchronous preparatory course](target-preparatory-month), which runs during the month leading up to the summer school.

### Data
We will provide some example datasets for you to use during the workshop.
You will be asked to download these prior to the event.

In addition, we encourage you to bring your own data.
This could include video recordings of animal behaviour and/or motion tracks you've already generated.
It's a **great chance to get feedback on your data and learn from others**, especially during the __Collaboration Days__ on __Thursday & Friday__.
