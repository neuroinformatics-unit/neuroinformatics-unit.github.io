# Google Summer of Code

[Google Summer of Code](https://summerofcode.withgoogle.com/) (GSoC) is a global fully online program whose aim is to bring new developers into open source software. It is a great opportunity to gain experience in real-world software development while helping the open source community. Additionally, GSoC contributors receive a stipend from Google. 

Initially focused on university students, since 2022 the program has expanded to welcome students and all beginner contributors to open source who are 18 years and older to participate.

In 2025, NIU is participating as a mentoring organization with GSoC for the first time, pairing candidates with NIU developers to work on ~12-week programming projects. So if you are interested in contributing to open source software, this is a great opportunity to get involved!


## How does GSoC work?
Through the GSoC application process, interested applicants submit project proposals to the various organizations participating in GSoC - in our case, the NIU. Then, the organizations select which proposals they would like to see funded by Google. Successful applicants will spend their summer contributing code to our open source organization under the guidance of our mentoring team. 

Below you can find some more information on the [projects](#gsoc-niu-projects-2025) that we are putting forward for GSoC 2025, and some [guidelines](#apply-to-gsoc-with-niu) to help you with your application.

To learn more about the program, we recommend reading the [GSoC FAQs](https://developers.google.com/open-source/gsoc/faq) and the [GSoC Contributor Guide](https://google.github.io/gsocguides/student/), and having a look at the [2025 Timeline](https://developers.google.com/open-source/gsoc/timeline). For general information, see also the [GSoC website](https://summerofcode.withgoogle.com/).


## GSoC NIU Projects 2025

NIU is offering a variety of projects for GSoC 2025, organized under four of our software tools. Click on a card below to learn more about the project ideas for each tool.

A project can be one of three sizes: small (90 h), medium (175 h) or large  large (350 h). The standard coding period is 12 weeks for medium and large projects, and 8 weeks for small projects. 

However, GSoC contributors can request in their proposal up to a 22-week coding period, if they know they may have other commitments or certain weeks when they will not be able to work full time on their GSoC project. During the project preparation period (called "community bonding period"), both the GSoC contributor and the mentors will agree on a schedule and sign off on it.


::::{grid} 1 1 1 1
:gutter: 4

:::{grid-item-card} {fas}`video;sd-text-primary` `movement`
:link: projects_2025/movement
:link-type: doc
Markerless pose estimation tools based on deep learning, such as [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut) and [SLEAP](https://sleap.ai/), have revolutionised the study of animal behaviour. However, there is currently no user-friendly, general-purpose approach for processing and analysing the trajectories generated by these popular tools. To fill this gap, we're developing [`movement`](https://movement.neuroinformatics.dev/), an open-source Python package that provides a unified data analysis interface across pose estimation frameworks. 
:::

:::{grid-item-card} {fas}`otter;sd-text-primary` `ethology`
:link: projects_2025/ethology
:link-type: doc
[`ethology`](https://github.com/neuroinformatics-unit/ethology) is a Python package in early-development stage, whose aim is to facilitate the application of a wide range of computer vision tasks to animal behaviour research, by providing a unified data analysis interface across these tasks. We plan to support both classic computer vision tasks and deep learning based ones, such as background subtraction, object detection, ID tracking, segmentation, any-point tracking, and any useful combinations between them. 
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` `BrainGlobe`
:link: projects_2025/brainglobe
:link-type: doc
[BrainGlobe](https://brainglobe.info/) is a community-driven suite of open-source Python tools. The BrainGlobe tools are widely used to process, analyse and visualise images of brains (and other related data) in neuroscientific research.
:::

:::{grid-item-card} {fas}`database;sd-text-primary` `datashuttle`
:link: projects_2025/datashuttle
:link-type: doc
[`datashuttle`](https://datashuttle.neuroinformatics.dev/index.html) is a tool to automate neuroscience project folder creation, validation and transfer. It creates and validates projects standardised to the [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/latest/index.html) specification. It also allows these folders to be easily synchronised between computers.
:::

:::{grid-item-card} {fas}`database;sd-text-primary` `spikewrap`
:link: projects_2025/spikewrap
:link-type: doc
[`spikewrap`](https://spikewrap.neuroinformatics.dev/index.html) is a package for managing extracellular electrophysiology analysis.
:::

::::

## Apply to GSoC with NIU

As part of your application to GSoC, you will need to submit a project proposal. To help you with this, we provide some [NIU guidelines](guidelines) on how to write a successful proposal to work with us. 

You may also want to checkout other useful application guides, such as:
- the [GSoC Contributor Guide: writing a proposal](https://google.github.io/gsocguides/student/writing-a-proposal), 
- the [Python Software Foundation guide](https://python-gsoc.org/), 
- the [OpenAstronomy](https://openastronomy.org/gsoc/student_guidelines.html) one, or 
- the [INCF](https://www.incf.org/recommendations-gsoc-contributors) one,

all of which we are closely following. Applicants are given about 2 weeks to complete their applications. For further details see the [GSoC Contributor Guide](https://google.github.io/gsocguides/student/writing-a-proposal).

If you are interested in any of the NIU projects on offer, feel free to get in touch on our [GSoc Zulip channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-GSoC) with any questions. Please reach out in public channels, rather than via DMs or personal conversations - communicating in the open is a big part of open source! However, if you have any concerns you wish to discuss privately (such as accessibility), please contact one of the organisation admins.

For clarity, please always use your full name when getting a [Zulip](https://neuroinformatics.zulipchat.com/) account, when registering for the program, and when submitting your project plan. 


## Team

The NIU GSoC team for 2025 is composed of the following members. To read more about the different roles involved in GSoC, see [GSoC Participant Roles](https://google.github.io/gsocguides/mentor/#participant-roles).

Our working languages are Python and English ;) - but we also speak other languages! We listed any additional languages spoken by the mentors in each of the projects' descriptions.

::::{grid} 3 3 3 3
:gutter: 3
:padding: 5

:::{grid-item-card} Adam Tyson
:img-top: ../../_static/adam_tyson.jpg
:link: https://github.com/adamltyson
:text-align: center


{fab}`github` [@adamltyson](https://github.com/adamltyson)

Organisation administrator
:::

:::{grid-item-card} Sofía Miñano
:img-top: ../../_static/sofia_minano.png
:link: https://github.com/sfmig
:text-align: center

{fab}`github` [@sfmig](https://github.com/sfmig)


Organisation administrator & mentor

:::

:::{grid-item-card} Alessandro Felder
:img-top: ../../_static/alessandro_felder.png
:link: https://github.com/alessandrofelder
:text-align: center

{fab}`github` [@alessandrofelder](https://github.com/alessandrofelder)

Mentor
:::

:::{grid-item-card} Niko Sirmpilatze
:img-top: ../../_static/niko_sirmpilatze.png
:link: https://github.com/niksirbi
:text-align: center

{fab}`github` [@niksirbi](https://github.com/niksirbi)

Mentor

:::

:::{grid-item-card} Igor Tatarnikov
:img-top: ../../_static/igor_tatarnikov.jpg
:link: https://github.com/IgorTatarnikov
:text-align: center

{fab}`github` [@IgorTatarnikov](https://github.com/IgorTatarnikov)

Mentor

:::

:::{grid-item-card} Joe Ziminski
:img-top: ../../_static/joe_ziminski.png
:link: https://github.com/JoeZiminski
:text-align: center

{fab}`github` [@JoeZiminski](https://github.com/JoeZiminski)


Mentor

:::

::::


## Further details

```{toctree}
:maxdepth: 1

projects_2025/index
guidelines
```
