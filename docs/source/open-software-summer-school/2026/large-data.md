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


We will cover the following topics during the first three days:
* **Motivation** We will show examples of large array datasets from neuroscience and imaging, discuss what research they enable, in what situations you should acquire them, and the computational challenges they pose.
* **Introduction to the `zarr` and `dask` libraries:** a short introduction to Python libraries that enable you to read, process, and write large array datasets.
* **Chunked, multi-scale file formats for large images:** a short introduction to the OME-Zarr format for large images and a practical tutorial to convert, process and visualise your large image data to OME-Zarr.
* **Parallel processing of large image data with `dask`:** a hands-on tutorial covering `dask`'s parallelisation functionality
* **Compression of large array data:** an introduction to compression algorithms, how they are used in neuroscience, and what trade-offs you should be aware of when using them.


### Collaboration days (Thursday - Friday)

The final two days are dedicated to collaboration. We will join forces with participants from the **Animals in Motion** track to work together on participant-led projects.

* **Skill building:** we'll start with a practical workshop on **Git and GitHub** to equip everyone with the necessary skills for collaborative coding.
* **Project-based work:** participants will self-organize into small teams to tackle projects hands-on. **Coding is not a requirement**; any idea that benefits from collaboration with other attendees is welcome. Potential project ideas include, but are not limited to:
    * **Apply a tool:** use any learned software to analyze a new dataset (your own or a public one).
    * **Give feedback:** raise issues, suggest features, or improve documentation for relevant open-source tools.
    * **Make a contribution:** submit a pull request to an open-source repository (support will be provided).
    * **Collaborative writing:** draft a white paper, blog post, or documentation together.
    * **Prototype an idea:** test a cool new analysis or method on real-world data.
* **Presentation:** you will have the opportunity to report your team's progress on the final afternoon.
## Instructors
- [Alessandro Felder](https://github.com/alessandrofelder)
- [Igor Tatarnikov](https://github.com/IgorTatarnikov)
- [David Stansby](https://github.com/dstansby)
- [Kimberly Meechan](https://github.com/K-Meech)
- [Joe Ziminski](https://github.com/JoeZiminski)


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
