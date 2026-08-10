(track-large-array-data-2026)=
# Track: Large Array Data

In many areas of research, large array datasets have become important and wide-spread. Examples include whole-organ images, extracellular electrophysiology, and long behavioural videos — to name just a few. Processing, analyzing and visualising these datasets is made significantly more complex and slow because they do not fit into a typical computer's memory and take up a lot of disk space.

The use of compression algorithms and modern file formats which favour parallel processing enable us to deal with these challenges effectively, but doing this well requires careful consideration of the trade-offs between read and write speeds, disk space used, and portability.

This track will cover the necessary context needed to understand the computational challenges posed by large array datasets, and how to address these challenges using open-source software tools. All sessions will include a significant hands-on component. At the end of the week, participants will know how to write Python code to process a large array dataset (e.g. a 1TB functional imaging dataset) efficiently on their laptop.

::: {admonition} Target audience
:class: note

This course is designed for researchers and students interested in learning about open-source tools for processing large array data with Python. We will favour applicants that have acquired, or are about to acquire, large array data. Participants are encouraged to bring their own data to experiment with, but example data will be provided.
:::

## Course overview

### Core workshop (Monday - Wednesday)

| Time | Theme | Description |
| --- | --- | --- |
| Monday<br>10am-1pm | Introduction and key libraries | Introductory lecture on key concepts; examples of large array data, research enabled, and computational challenges; introduction to [`zarr`](https://zarr.dev/) and [`dask`](https://www.dask.org/). |
| Monday<br>2pm-5pm | Symposium | Participants present their work and network with other participants. |
| Tuesday<br>10am-1pm | Large image data with OME | Introduce the [OME-Zarr specification](https://ngff.openmicroscopy.org/) (following the [OME-Zarr textbook](https://ome-zarr-book.readthedocs.io/)); hands-on tutorial to convert, process, and write large imaging datasets. |
| Tuesday<br>2pm-5pm | Parallel processing | Deeper look at `dask` and its parallelisation functionality in practice. |
| Wednesday<br>10am-1pm | Compression | Introduction to compression algorithms, their use in neuroscience, and trade-offs to consider. |
| Wednesday<br>2pm-5pm | Visualisation | Hands-on tutorial in interactive large data visualisation in collaboration with [HoloViz](https://holoviz.org/). |

### Collaboration days (Thursday - Friday)

The final two days are dedicated to collaboration. We will join forces with participants from the [Animals in Motion](track-animals-in-motion-2026) track to work together on participant-led projects.

* **Skill building:** we'll start with a practical workshop on **Git and GitHub** to equip everyone with the necessary skills for collaborative coding.
* **Project-based work:** participants will self-organise into small teams to tackle projects hands-on. **Coding is not a requirement**; any idea that benefits from collaboration with other attendees is welcome. Potential project ideas include, but are not limited to:
    * *Apply a tool:* use what you've learnt to analyse a new dataset (your own or a public one).
    * *Give feedback:* report bugs and suggest features by raising issues on relevant open-source tools.
    * *Make a contribution:* submit a pull request to an open-source repository.
    * *Collaborative writing:* draft a white paper, blog post, or documentation together.
    * *Prototype an idea:* experiment with a new analysis or method.
* **Presentation:** teams will have the opportunity to share their progress and outcomes on the final afternoon.

## Confirmed Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)
- [Kimberly Meechan](https://github.com/K-Meech)
- [James A. Bednar](https://github.com/jbednar)


(target-large-array-data-prerequisites-2026)=
## Prerequisites

### Hardware
As this is a hands-on workshop, you will need to bring your own laptop. Any fairly recent laptop will be suitable, you don't need a GPU etc.

### Python knowledge
The only prerequisite is a basic knowledge of programming in Python, and the scientific Python ecosystem. For those without
this background, the [preparatory month](https://neuroinformatics.dev/open-software-summer-school/index.html#preparatory-month) 
will equip you with all the skills needed to make the most of this course. 

### Data
Bringing your own data is encouraged but not required.
It's a great chance to get feedback on your data and learn from others.
If you don't have your own data, we will provide example datasets for you to work with.

We expect that participant-led ideas emerging from this track may inspire collaborative projects during the __Collaboration Days__ on Thursday and Friday.


### Set-up

To get your computer ready, make sure you have the following:

- [Bash shell](https://carpentries.github.io/workshop-template/install_instructions/#shell)
- [Git](https://carpentries.github.io/workshop-template/install_instructions/#git) and a [GitHub account](https://github.com/signup)
  - *Windows users*: Installing the Bash shell via Git for Windows also installs Git, so you only need to create a GitHub account.
- [Miniforge](https://conda-forge.org/download/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
- [pixi](https://pixi.prefix.dev/latest/installation/)

You'll also need a code editor (IDE) configured for Python.
If you already have one you're comfortable with, feel free to use it. Otherwise, we recommend:

- [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

:::{note}
Run the commands below using the Bash shell.
:::

Create a conda environment (or equivalent environment manager you are comfortable with) named `large-arrays` with Python 3.13 :

```bash
conda create -n large-arrays python=3.13
```

If you encounter problems setting-up, please get in touch on [the Zulip chat](https://neuroinformatics.zulipchat.com/#narrow/channel/542225-Open-Software-Summer-School) and arrive at the venue 30 minutes early on Monday, so someone can help you.
