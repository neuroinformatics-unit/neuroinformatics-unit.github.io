---
blogpost: true
date: 25 April 2024
author: Joe Ziminski, Niko Sirmpilatze
location: London, UK
category: Blog
language: English
image: 1
---



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

**Maintaining a well-organised neuroscience project is hard.**

Although everyone can appreciate the benefits of a tidy project
folder, the practicalities of running an experiment often gets 
in the way. Folder organisation 
is low on the list of priorities when it
comes to acquisition sessions spent managing complex systems 
and experimental animals.

However, the cost of small mistakes during data acquisition can be high.
One misplaced character may mean sessions are missed by analysis 
scripts or subject identifications duplicated.
The best protection against such errors is automating the process
through acquisition scripts—resulting in hours spent writing code 
managing the naming and transfer of folders—a task entirely 
unrelated to the central research goals.

In our previous blog, we highlighted the benefits of data standardisation 
for systems neuroscience, introducing the 
[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) 
specification. 
An immediate benefit of a widely-used standard is that the entire community
can contribute to shared tools for project management.
This means individual researchers don't waste time
writing data-management code. 

In this blog post we introduce 
[**datashuttle**](https://datashuttle.neuroinformatics.dev/)—a 
tool for the automated creation, 
validation and transfer of projects organised to 
the **NeuroBlueprint** standard. **datashuttle** aims to
drop into existing acquisition pipelines, reducing errors
associated with manual folder creation and removing the need
to write your down data-management code.

Below we give a whistlestop tour of **datashuttle** and it's key
features. More information is available at the 
[datashuttle](https://datashuttle.neuroinformatics.dev/) 
website.

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
acquisition session, or behaviour (`behav`) 
and electrophysiological (`ephys`) data. 

The first thing typically done prior to acquiring data is to
create the folders that the data will be stored in. 
**datashuttle** can be used to quickly create the standardised
project folders in which to store the acquired data. 
Using **datashuttle** as apposed to manual creation or using custom
scripts is that it ensures no formatting errors creep in.

At the end of the session once data is acquired, 
**datashuttle** transfers the newly acquired data 
to a central storage machine to be backed up.

Later on in the experiment, you may want to transfer only a subset
of data from the central machine to an analysis machine. You may 
want to pilot a behavioural data analysis, and grab
for example only the behavioural 'test' session for
the first 5 subjects. **datashuttle** allows flexible custom transfers
easily, meaning you don't have to drag and drop these data manually or
write a custom script.

And that really is all there is to **datashuttle**, a tool to drop into acquisition
workflows to make folder creation and transfer more convenient and ensure standardisation.
Below we will give a brief tour of these key **datashuttle** features.

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

and folders can be created in an equivalent way through the Python API:

```python
from datashuttle import DataShuttle

project = DataShuttle("my_first_project")

created_folder_paths = project.create_folders(
    "sub-001", "ses-001_@DATE@", ["behav", "funcimg"]
)
```

## Data Transfer

At the end of an acquisition session, **datashuttle**
allows you to transfer all new data to the central machine
at the click of a `Transfer` button.

However, the real power comes from customisable transfers, for 
example downloading a subset of data to an analysis machine. Say you wanted
to transfer only the first behavioural session from all subjects
to an analysis PC. 

In the graphical interface, you could fill in the `Custom Transfer` screen
as below and click `Transfer`:

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
A final feature of **datashuttle** is logging—whenever a folder is created or
data transferred, full details are saved in the logs. This ensures
a full history of the project is available at any time

***TODO ADD AN IMAGE OF LOGS IN GRAPHICAL INTERFACE**

## Getting started with **datashuttle**

We have given a brief tour of **datashuttle**'s key features,
but full details on getting started can be found at our 
[website](https://datashuttle.neuroinformatics.dev/) and
[getting started tutorial](https://datashuttle.neuroinformatics.dev/pages/tutorials/getting_started.html).

We are very keen to get feedback on **datashuttle**. 
Standardisation is incredibly useful, but it should not come at the 
expense of convenience. **datashuttle** aims to make managing your project easier than 
it currently is—if it is not, we want to hear how it can be improved. 
You can get in contact with get in contact through our
[GitHub Issues](https://github.com/neuroinformatics-unit/datashuttle/issues)
or
[Zulip Chat.](https://neuroinformatics.zulipchat.com/#narrow/stream/405999-DataShuttle)


