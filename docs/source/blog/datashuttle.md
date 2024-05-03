:blogpost: true
:date: May 02, 2024
:author: Joe Ziminski, Niko Sirmpilatze
:location: London, UK
:category: Blog
:language: English
:image: 1


# Managing neuroscience projects with **datashuttle**
*Create, validate and transfer standardised project folders*

```{image} /_static/blog_images/datashuttle/datashuttle-overview-light.png
:align: center
:width: 650px
```
<br>

**Maintaining a well-organised neuroscience project is hard.**

Everyone can appreciate the benefits of a tidy project
folder, but the practicalities of running an experiment often get 
in the way. Folder organisation 
is low on the priority list during acquisition sessions 
spent managing complex equipment and experimental animals.

However, the cost of small mistakes during data acquisition are high.
One misplaced character can mean sessions are missed by analysis 
scripts or subject identifiers duplicated.
The best protection against such errors is automating the process
through acquisition scripts—resulting in hours spent writing 
data-management code entirely unrelated the central research goal.

In our previous blog post we highlighted the benefits of data standardisation 
for systems neuroscience, introducing the 
[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) 
specification. 
An immediate benefit of a widely-used standard is that the entire community
can share tools for project management.

In this blog post we introduce 
[**datashuttle**](https://datashuttle.neuroinformatics.dev/)—a 
tool for the automated creation, 
validation and transfer of projects organised to 
the **NeuroBlueprint** standard. **datashuttle** aims to
drop into existing acquisition pipelines, reducing errors
associated with manual folder creation and removing the need
to write your down data-management code.

Below we give a whistlestop tour of **datashuttle** and its key
features. 

## How **datashuttle** is used in an experiment

**datashuttle** runs on Windows, macOS or Linux and is
[easy to install](https://datashuttle.neuroinformatics.dev/pages/how_tos/install.html)
through 
[Conda Forge](https://conda-forge.org/)
or 
[PyPi](https://pypi.org/). **datashuttle** can be used
from within Python code (using the 'Python API') or through a graphical 
interface that works in any system terminal.

Imagine you are starting a new experiment, during which you acquire both
behavioural (`behav`) and electrophysiological (`ephys`) data. 

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


The first thing typically done prior to acquiring data is to
create the folders it will be stored in. 
**datashuttle** can be used to quickly create standardised
project folders for this purpose, with live-validation to ensure
no errors creep in.

Then, the important part, acquiring the actual data (hoping the animals and
their brain's do what you want them to!). **datashuttle** plays no role
in the acquisition process, its job so far was to simply create the standardised project folders.

Once the data is collected, it is usually moved to a central storage
machine and collated with other project data. This might typically be 
done by manually dragging and dropping, or a custom transfer script.
**datashuttle** you to transfer project folders after acquisition 
at the click of a button, or with a single function call.

Later on in the experiment, you may want to transfer only a subset
of data from the central machine to separate computer for analysis. For exampe,
you may  want to pilot a behavioural data analysis, grabbing
only the behavioural data for the first 5 subjects. 
**datashuttle** allows flexible custom transfers, 
meaning you don't have to drag and drop these data manually or
write a custom script.

Overall, **datashuttle** aims to drop into your existing acquisition pipelines whether 
they be manual or automated, with two ways to use it:

Below we will give an overview of **datashttle**'s key folder creation
and transfer features.

## Creating folders with live-validation

Creating folders through **datashuttle**'s graphical interface is as simple as
entering the subject and session name in the folder and clicking 'create'.


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

Live-validation of inputs, ensuring 
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

There are a number of shortcuts to ensure you only need to enter 
your custom information. For example, the tags 
(`@DATE@`, `@TIME@`, `@DATETIME@`) will fill the created folder 
with the date / time / datetime. A full list of shortcuts
(e.g. automatic suggestion of next subject / session names)
are available in the 
[documentation](https://datashuttle.neuroinformatics.dev/pages/how_tos/create-folders.html#creating-project-folders)


Folders can be created in an equivalent way through the Python API:

```python
from datashuttle import DataShuttle

project = DataShuttle("my_first_project")

created_folder_paths = project.create_folders(
    "sub-001", "ses-001_@DATE@", ["behav", "funcimg"]
)
```

## Data Transfer

**datashuttle** allows you to transfer all data between machines
at the click of a `Transfer` button.

The real power comes from customisable transfers. Let's say
that you wanted to transfer a subset of your acquired data to a 
workstation for analysis. For example, only the first behavioural 
session from all subjects to pilot an animal-tracking pipeline.

In the graphical interface, you would fill in the `Custom Transfer` screen
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

The keyword `all_sub` will transfer any subject while the `@*@` tag
in the session name acts as a wildcard. There are 
[many more options](https://datashuttle.neuroinformatics.dev/pages/how_tos/transfer-data.html#custom-transfers)
for customised transfer available.

Transfers can be run through the Python API similarly:
```python
from datashuttle import DataShuttle

project = DataShuttle("my_first_project")

project.transfer_custom(
    "rawdata", "all_sub", "ses-001_@*@", "behav"
)
```

## Logging

Whenever a folder is created or data transferred in **datashuttle**, 
full details are saved in the logs. This ensures
a full history of the project is available at any time. Logs are stored
on the local filesystem and can be viewed in a text editor or through
the graphical interface:

```{image} /_static/blog_images/datashuttle/logging-example-dark.png
:align: center
:class: only-dark
:width: 650px
```
```{image} /_static/blog_images/datashuttle/logging-example-light.png
:align: center
:class: only-light
:width: 650px
```
<br>

## Getting started with **datashuttle**

We have given a brief tour of **datashuttle**'s key features,
but full details on getting started can be found on our 
[website](https://datashuttle.neuroinformatics.dev/) and
[Getting Started tutorial](https://datashuttle.neuroinformatics.dev/pages/tutorials/getting_started.html).

Standardisation is incredibly useful, but it should not come at the 
expense of convenience. **datashuttle** should make managing your project easier than 
it currently is—if not, we want to hear how it can be improved.
Please can get in contact anytime through our
[GitHub Issues](https://github.com/neuroinformatics-unit/datashuttle/issues)
or
[Zulip Chat.](https://neuroinformatics.zulipchat.com/#narrow/stream/405999-DataShuttle)


