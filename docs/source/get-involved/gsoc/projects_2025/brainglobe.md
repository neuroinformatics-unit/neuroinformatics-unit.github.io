# GSoC NIU Projects 2025: BrainGlobe

A project can be one of three sizes: small (90 h), medium (175 h) or large  large (350 h). The standard coding period is 12 weeks for medium and large projects, and 8 weeks for small projects. 

However, GSoC contributors can request in their proposal up to a 22-week coding period, if they know they may have other commitments or certain weeks when they will not be able to work full time on their GSoC project. During the project preparation period (called "community bonding period"), both the GSoC contributor and the mentors will agree on a schedule and sign off on it.

If you are interested in any of these projects, [get in touch](https://brainglobe.info/contact.html)! Feel free to open a new topic on [Zulip](https://brainglobe.zulipchat.com/) and tag the potential mentors.

Our working language is English, but our mentors for these projects also speak Italian, French, and German.

:::{dropdown} {fas}`video;sd-text-primary` Improve `cellfinder`'s classification algorithm
<!-- Description -->
BrainGlobe is a community-driven suite of open-source Python tools. The BrainGlobe tools are widely used to process, analyse and visualise images of brains (and other related data) in neuroscientific research.

The BrainGlobe `cellfinder` tool is used to detect cells in large whole-brain images. It uses signal processing to find possible cell candidates and passes them to a customisable classifier to split the candidates into cells and no-cells. `cellfinder` relies heavily on `pytorch` and `keras`.

`cellfinder` currently uses a residual neural network (ResNet) to classify cell candidates, and Deep Learning network architectures have progressed since. In this project, you will explore newer architectures for the classification network as alternatives to ResNet, and see whether they work better and/or faster than the existing implementation.


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
This project is well-suited for a student or a beginner contributor to open source.

**Required skills**

Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**
- Experience working with machine learning
- Experience working with image data


**Potential mentors**
- [@IgorTatarnikov](https://github.com/IgorTatarnikov)
- [@alessandrofelder](https://github.com/alessandrofelder)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [cellfinder paper](https://doi.org/10.1371/journal.pcbi.1009074)
- [cellfinder code](https://github.com/brainglobe/cellfinder)
:::



