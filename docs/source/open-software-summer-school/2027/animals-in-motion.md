(track-animals-in-motion-2027)=
# Track: Animals in Motion

Machine learning methods for motion tracking have transformed a wide range of scientific disciplines—from neuroscience and biomechanics to conservation and ethology.
Tools such as [DeepLabCut](https://mlabofai.org/deeplabcut) and [SLEAP](https://sleap.ai/) enable researchers to track animal movements in video recordings with impressive accuracy, without the need for physical markers.

However, the variety of available tools can be overwhelming.
It's often unclear which tool is best suited to a given application, or how to get started.
Moreover, generating motion tracks is only the first step:
these tracks must then be further processed, visualised, and analysed to yield meaningful
and interpretable insights into animal behaviour.

::: {admonition} Target audience
:class: note

This course is designed for researchers and students who have collected — or plan to collect — videos of animal behaviour. It is aimed at those interested in using the latest free and open-source tools for tracking animal motion and extracting quantitative behavioural measures.
:::


## Course overview

```{figure} /_static/osw_images/animals-in-motion-2026_overview.png
:alt: A schematic overview of topics covered in the Animals in Motion track.

**A schematic overview of topics covered in the Animals in Motion** track.
While icons of mice are used for illustration, the course content should be applicable to any animal species.

```

### Core workshop (Monday - Wednesday)

| Time | Theme | Description |
| --- | --- | --- |
| Monday<br>Morning | Introduction and key concepts | A big-picture overview of analysis workflows and tools for animal behaviour, followed by a primer on deep learning for computer vision. |
| Monday<br>Afternoon | Symposium | Participants present their work and network with other participants. |
| Tuesday<br>Morning | Pose estimation | A practical tutorial on [SLEAP](https://sleap.ai/)—a popular software library for animal pose estimation and tracking. You will learn how to annotate video frames, train deep learning models, and generate motion tracks from new videos. |
| Tuesday<br>Afternoon | Motion quantification | A practical introduction to [movement](https://movement.neuroinformatics.dev)—a Python package for cleaning, visualising, and analysing motion tracks produced by [SLEAP](https://sleap.ai/), [DeepLabCut](https://deeplabcut.org/) and similar tools. |
| Wednesday<br>Morning | Behaviour segmentation | A primer on decomposing continuous motion into discrete actions. You will learn how to annotate behaviours with [BORIS](https://www.boris.unito.it) and train a supervised behaviour classifier with [scikit-learn](https://scikit-learn.org/stable/index.html). |
| Wednesday<br>Afternoon | Case studies | Real-world case studies (including coding exercises) applying markerless motion tracking and quantification. |


::: {admonition} Course handbook
:class: note

All course materials will be made available as part of the online handbook at <https://animals-in-motion.neuroinformatics.dev> and remain accessible afterwards.

Feel free to look through the handbook to get a sense of its contents, but keep in mind that updates will be made before the 2027 event.

:::

### Collaboration days (Thursday - Friday)

The final two days are dedicated to collaboration. We will join forces with participants from the [Large Array Data](track-large-array-data-2027) track to work together on participant-led projects. See [Collaboration days](target-collaboration-days-2027) for details.

## Confirmed Instructors
- [Niko Sirmpilatze](https://github.com/niksirbi)
- [Sofía Miñano](https://github.com/sfmig)
- [Chang Huan Lo](https://github.com/lochhh)

## Prerequisites

### Hardware
This is a hands-on course, so please bring your own **laptop** and **charger**.
A **mouse** is strongly recommended, especially for tasks like image annotation.
A dedicated **GPU is not required**, though it may speed up some computations.

### Software
See the [software prerequisites](https://animals-in-motion.neuroinformatics.dev/dev/prerequisites.html) section of the course handbook for detailed instructions on installing and configuring the required software. The prerequisites will be updated before the event, and accepted participants will be reminded to complete the setup in advance.

### Python knowledge
If you're new to Python, we recommend signing up for our [asynchronous preparatory course](target-preparatory-month-2027), which runs during the month leading up to the summer school.

### Data
We will provide some example datasets for you to use during the workshop—see the [data prerequisites](https://animals-in-motion.neuroinformatics.dev/dev/prerequisites.html) section of the course handbook for details.
You will be asked to download these prior to the event.
In addition, we encourage you to bring your own data.
This could include video recordings of animal behaviour and/or motion tracks you've already generated.
It's a great chance to get feedback on your data and learn from others, especially during the collaboration days.
