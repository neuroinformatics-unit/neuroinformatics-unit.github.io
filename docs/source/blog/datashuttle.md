---
blogpost: true
date: 25 April 2024
author: Joe Ziminski, Niko Sirmpilatze
location: London, UK
category: Blog
language: English
image: 1
---

ADD ESTIMATED READING TIME

# Managing neuroscience projects with **datashuttle**
*Create, validate and transfer standardised project folders*

```{image} /_static/blog_images/datashuttle/datashuttle-overview-dark.png
:align: center
:class: only-dark
:width: 650px
```
```{image} /_static/blog_images/datashuttle/datashuttle-overview-light.png
:align: center
:class: only-light
:width: 650px
```
<br>

Maintaining a well-organised neuroscience project is hard. 
Despite the best intentions, folder organisation is low on the priority 
list during hectic data acquisition sessions spent managing complex 
systems and experimental animals. 

However, the cost of small mistakes during data acquisition can be high.
One misplaced character may mean sessions are missed by analysis 
scripts or subject identifications duplicated.
The best protection against such errors is automating the process
through acquisition scripts—resulting in hours spent writing code 
managing the naming and transfer of folders—a task entirely 
unrelated to the central research goals.

In our previous blog, we highlighted the benefits of data standardisation 
for systems neuroscience and introduced the 
[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) 
specification. 
An immediate benefit of a widely-used standard is that the entire community
can contribute to shared tools for project management.
This means individual researchers don't waste time
duplicating data-management code. 

In this blog post we introduce 
[**datashuttle**](https://datashuttle.neuroinformatics.dev/)—a 
tool for the automated creation, 
validation and transfer of projects organised to 
the **NeuroBlueprint** standard. 

## How **datashuttle** is used in an experiment

```{image} /_static/blog_images/datashuttle/tutorial-1-example-file-tree-dark.png
:align: center
:class: only-dark
:width: 400px
```
```{image} /_static/blog_images/datashuttle/tutorial-1-example-file-tree-light.png
:align: center
:class: only-light
:width: 400px
```
<br>

Imagine that you are starting a new experiment and have the first
acquisition session, or behaviour ('behav') and electrophysiological ('ephys')
data. 

The first thing you need to do is create the folders that the acquired 
data will go. **datashuttle** is used there, either through the graphical 
interface (manual) or python API (automated) to ensure folders are free
of typographical errors and formatted to NeuroBlueprint standard.

Then, acquisition data is saved to these folders while the experiment runs.
At the end of the session, **datashuttle** transfers the newly acquired data 
to a central storage machine to be backed up.

Later on in the experiment, you may want to transfer only a subset
of data from the central machine to an analysis machine—for example,
to pilot some behavioural data you will grab the 'test' session for
the first 5 subjects. **datashuttle** allows flexible custom transfers
easily, meaning you don't have to drag and drop these data manually or
write a custom script.

**datashuttle** performs three key functions during an experimental workflow:

1) Creation and live-validation of folders in the 
[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) standard
2)	Transfer of data between acquisition (or analysis) computers and a central storage machine
3)	Logging of all actions for full project provenance

Below we will give a brief tour of the key **datashuttle** features.

## Creating folders with live-validation

To create folders manually through the graphical interface with **datashuttle**, 
it is as simple as entering the subject and session name in the folder and clicking 'create'.


```{image} /_static/blog_images/datashuttle/create-folders-example-dark.png
:align: center
:class: only-dark
:width: 650px
```
```{image} /_static/blog_images/datashuttle/create-folders-example-light.png
:align: center
:class: only-light
:width: 650px
```
<br>

There are a number of convenience shortcuts to ensure you only need to enter 
your custom information. For example, the convenience tags 
(`@DATE@`, `@TIME@`, `@DATETIME@`) will fill the created folder 
with the date / time / datetime.

**datashuttle** performs live-validation of inputs, ensuring 
formatting errors cannot creep into the project:

```{image} /_static/blog_images/datashuttle/validation-bad-dark.png
:align: center
:class: only-dark
:width: 500px
```
```{image} /_static/blog_images/datashuttle/validation-bad-light.png
:align: center
:class: only-light
:width: 500px
```
<br>

Through the Python API, folders can be suggested and created through this 
simple API and slot into acquisition pipelines:

```python
from datashuttle import DataShuttle

project = DataShuttle("my_first_project")

created_folder_paths = project.create_folders(
    "sub-001", "ses-001_@DATE@", ["behav", "funcimg"]
)
```

## Data transfers

It is the end of an experimental acquisition session, and time to 
store your data on the central server for backup. **datashuttle**
allows you to transfer all new data to the central machine
at the click of a 'Transfer' button.

However, the real power comes from customisable transfers, for example
or downloading a subset of data to an analysis machine. Say you wanted
to transfer only the first behavioural session from all subjects
to an analysis PC. 

In the graphical interface, you could fill in the `Custom Transfer` screen
as below and click 'Transfer':

```{image} /_static/blog_images/datashuttle/how-to-transfer-custom-dark.png
:align: center
:class: only-dark
:width: 650px
```
```{image} /_static/blog_images/datashuttle/how-to-transfer-custom-light.png
:align: center
:class: only-light
:width: 650px
```
<br>

and in code, it looks similar:

```python
from datashuttle import DataShuttle

project = DataShuttle("my_first_project")

project.transfer_custom(
    "rawdata", "all_sub", "ses-001_@*@", "behav"
)
```


## Logging
A final feature of datashuttle is logging. Makes it easy. Simple photo

***TODO ADD AN IMAGE OF LOGS IN GRAPHICAL INTERFACE**

## Getting started with **datashuttle**

We have given a whistlestop tour of **datashuttle**'s key features here,
but full details on getting started can be found at our 
[website](https://datashuttle.neuroinformatics.dev/) and
[getting started tutorial](https://datashuttle.neuroinformatics.dev/pages/tutorials/getting_started.html).

We are very keen to get feedback on **datashuttle**. 
Standardisation is incredibly useful, but it should not come at the 
expense of in running day-to-day projects less easily than you currently 
are. **datashuttle** aims to make managing your project easier than 
it currently is – if it is not, we want to hear how it can be improved. 

You can get in contact with get in contact through our
[GitHub Issues](https://github.com/neuroinformatics-unit/datashuttle/issues)
or
[Zulip Chat.](https://neuroinformatics.zulipchat.com/#narrow/stream/405999-DataShuttle)


