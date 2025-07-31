# Open Software Week

We are excited to announce our inaugural **NIU Open Software Week**, taking
place in **August 2025** in **London, UK**. This event will bring together researchers, developers, and users of open-source software for some hands-on training, community-building and hacking.

:::{admonition} Application period has ended and selected applicants have been notified.
:class: info

**August 11-15 2025**, [Sainsbury Wellcome Centre](https://maps.app.goo.gl/CzWFFjXJZwX87aMj6)

- ~~**April 16th 2025**: Applications open~~
- ~~**June 6th 2025**: Applications close~~
- ~~**End of June/Early July 2025**: Applicants are notified of acceptance~~
:::

## Schedule

Sessions will run daily between **10:00** and **17:00**.
Here is an overview of the whole week:

<img src="../_static/osw_images/schedule-2025_light-mode.png" alt="A colour-coded table showing the schedule of open software week. The columns are weekdays, and the rows are Morning and Afternoon. All of Monday and Friday will be spent on 'Intro to Python' and 'Hackday', respectively. Tuesday and Wednesday are split into two whole-day main tracks: 'Animals in Motion' and 'BrainGlobe'. On Thursday, one can choose between either a full day of 'Big Imaging Data' or 'Careers Clinic' in the morning and 'Collaborative Coding with git' in the afternoon." class="only-light img-responsive"/>
<img src="../_static/osw_images/schedule-2025_dark-mode.png" alt="A colour-coded table showing the schedule of open software week. The columns are weekdays, and the rows are Morning and Afternoon. All of Monday and Friday will be spent on 'Intro to Python' and 'Hackday', respectively. Tuesday and Wednesday are split into two whole-day main tracks: 'Animals in Motion' and 'BrainGlobe'. On Thursday, one can choose between either a full day of 'Big Imaging Data' or 'Careers Clinic' in the morning and 'Collaborative Coding with git' in the afternoon." class="only-dark img-responsive"/>

There are three **main tracks** targeted to different audiences.
We encourage you to read each track's description and choose the one that best fits your interests.
You can apply for at most 2 of 3 main tracks, and note that [Animals in Motion](track-animals-in-motion) and [BrainGlobe](track-brainglobe)
cannot be combined as they are running in parallel.

:::: {grid} 1 1 3 3

:::{grid-item-card} {fas}`video;sd-text-secondary` Animals in Motion
:img-top: ../_static/osw_images/animals-in-motion-card.png
:link: track-animals-in-motion
:link-type: ref

Use open-source tools to track
and analyse animal motion from video footage.

:::

:::{grid-item-card} {fas}`brain;sd-text-warning` BrainGlobe
:img-top: ../_static/osw_images/brainglobe-card.png
:link: track-brainglobe
:link-type: ref

Use the BrainGlobe ecosystem of computational neuroanatomy tools
to analyse whole-brain microscopy datasets.
:::

:::{grid-item-card} {fas}`microscope;sd-text-primary` Big Imaging Data
:img-top: ../_static/osw_images/big-imaging-data-card.png
:link: track-big-imaging-data
:link-type: ref

Bridging technical gaps and communities to process and analyse
large 3D imaging datasets with open-source tools.

:::

::::

We also offer a series of **satellite events** which are open to all participants and are designed to provide additional training and networking opportunities.
You can apply for any number of satellite events, but note that the ones on Thursday cannot be combined with the [Big Imaging Data](track-big-imaging-data) track.

:::{dropdown} Intro to Python
:name: intro-to-python
:color: primary
:icon: code-square

A beginner-friendly workshop for those who are new to programming and want to learn the basics of Python before diving into the rest of the week.
:::

:::{dropdown} Careers Clinic
:name: careers-clinic
:color: primary
:icon: briefcase

The Careers Clinic will consist of a panel discussion from diverse Research Technology Professionals with a background in life sciences.
We hope for the discussion to benefit those interested in exploring non-traditional career paths in research.
The audience is encouraged to prepare questions for the panellists, and reflect on their own careers.

Panelists include:

- **Mayo Faulkner**, Research Software Engineer at the International Brain Lab
- **Vicki Yorke-Edwards**, Senior Research Data Steward at UCL Advanced Research Computing Centre
- **Batool Almarzouq**, Manager of Imago (Imagery Smart Data Service), part of the Smart Data Research UK programme
- **Laura Porta**, Senior Research Software Engineer in the Neuroinformatics Unit
- **Jonas Hartmann**, Postdoctoral Researcher at UCL Cell + Developmental Biology

If you've signed up for the Careers Clinic, please arrive at the Sainsbury Wellcome Centre
exactly at **11:30** on **Thursday**. This will give you a chance to grab a coffee from the Ground Floor Lecture Theatre before being guided to the 3rd Floor Seminar Room for
the panel discussion, which will start at **11:45**.
:::

:::{dropdown} Collaborative coding with git
:name: collaborative-coding-with-git
:color: primary
:icon: git-pull-request

Learn how to version control your code and collaborate with others using `git` and GitHub. This workshop is open to all but is especially recommended for those who are planning to participate in the following day's hackathon.
:::

:::{dropdown} Hackday
:name: hackday
:color: primary
:icon: people

Put into practice what you have learned during the week and collaborate with others to tackle a real-world problem using open-source tools. The goal will be to end the day with several pull requests to open-source projects.
:::

(target-general-prerequisites)=
## Prerequisites

As this is a hands-on event, you will need to bring your own **laptop** and **charger**. Any fairly recent laptop will be suitable, you don't need a dedicated GPU.

:::{note}
If you already have a working Anaconda or Miniconda installation and have used it to run Python scripts or Jupyter notebooks, you can likely skip ahead to the [additional track-specific prerequisites](target-track-specific-prerequisites).
:::

To prepare your computer for Python development, we recommend following the [Software Carpentries installation instructions](https://carpentries.github.io/workshop-template/install_instructions), in particular:

- [Bash Shell](https://carpentries.github.io/workshop-template/install_instructions/#shell), to run terminal commands
- [Git](https://carpentries.github.io/workshop-template/install_instructions/#git), including a GitHub account
- [Python](https://carpentries.github.io/workshop-template/install_instructions/#python), via the [conda-forge installer](https://conda-forge.org/download/). Please make sure you install a __Python version >= 3.12__ (e.g. 3.12 is fine, 3.10 is not).

You'll also need a code editor (IDE) configured for Python.
If you already have one you're comfortable with, feel free to use it. Otherwise, we recommend:

- [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)

(target-track-specific-prerequisites)=
:::{admonition} Additional track-specific prerequisites
:class: warning

Apart from the general development tools mentioned above, each track may have additional prerequisites. The following links will take you there:
- [Animals in Motion](target-animals-in-motion-prerequisites)
- [BrainGlobe](target-brainglobe-prerequisites)
- [Big Imaging Data](target-imaging-prerequisites)

Please arrive 30 minutes early if you are facing problems installing course prerequisites.
:::

## Funding

The [Animals in Motion](track-animals-in-motion) and the [Big Imaging Data](track-big-imaging-data) tracks have been made possible by [Software Sustainability Institute](https://www.software.ac.uk/) fellowships to **Niko Sirmpilatze** and **Alessandro Felder**, respectively. The NIU Open Software Week is further supported by the [Sainsbury Wellcome Centre](https://www.sainsburywellcome.org/), the [Society for Research Software Engineering](https://society-rse.org/) and [AIBIO-UK](https://aibio.ac.uk/). We thank the [Sainsbury Wellcome Centre](https://www.sainsburywellcome.org/) and the [Gatsby Computational Neuroscience Unit](https://www.ucl.ac.uk/gatsby/gatsby-computational-neuroscience-unit) for providing facilities for the event.

```{image} /_static/osw_images/sponsor-logos.png
:align: center
:width: 80%
:alt: The logos of three Open Software Week sponsors: The Software Sustainability Institute, the Society for RSE and AIBIO UK
```

```{toctree}
:maxdepth: 2
:caption: Index
:hidden:

animals-in-motion
brainglobe
big-imaging-data
```
