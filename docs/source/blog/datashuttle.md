---
blogpost: true
date: 25 April 2024
author: Joe Ziminski, Niko Sirmpilatze
location: London, UK
category: Blog
language: English
image: 1
---

# Managing systems neuroscience projects with **datashuttle**
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

**datashuttle** performs three key functions during an experimental workflow:

1) Creation and live-validation of folders named to the NeuroBlueprint standard
2)	Transfer of data between acquisition or analysis computers and a central storage machine
3)	Logging of all actions for complete project provenance

**datashuttle** revolves around the concept of multiple *local* machines and one
*central* machine. The central machine is where the project data is collated,
stored and backed up. Local machines are data acquisition or analysis machines
between which data is transferred with the central machine.

**datashuttle** can be run through a graphical
interface or in python code, select the tab to switch between both examples 
below.

## Creating folders with live-validation

Creating and validating NeuroBlueprint project folders
5) 
At the start of an acquisition session when there is a lot to juggle, 
the last thing you want to be thinking about is creating a standardised 
project folder. If setting up your project manually, you would ideally 
enter only the key custom unique information required for the subject and 
session, with everything else created on the fly and live-validation to check 
any possible manual errors. If you are running an automated acquisition, you 
want a simple API to build standardised project folders and get the path for 
downstream applications.

To create folders manually through the graphical interface with **datashuttle**, 
it is as simple as entering the subject and session name in the folder and clicking 'create'.

[IMAGE]

There are a number of convenience shortcuts to ensure you only need to enter 
critical information. Double-clicking will fill the next subject or session 
number while key tags (@DATE@, @TIME@, @DATETIME@) will auto-fill date and time. 

[IMAGE]

Live validation occurs, meaning it is impossible to make a typographical error

```{image} /_static/blog_images/datashuttle/validation-bad-dark.png
:align: center
:class: only-dark
:width: 400px
```
```{image} /_static/blog_images/datashuttle/validation-bad-light.png
:align: center
:class: only-light
:width: 400px
```
<br>

With customisation against defined 'name templates' possible (e.g. if you 
want to specify longer names that might include ids, etc.)

In code, folders can be suggested and created through this simple API:
(example)
Creating standardised project folders should not be something you spend time on. 
Datashuttle aims to make this process as smooth as possible.

## Data transfers

After data is acquired, it can be 'uploaded' to a central storage machine. 
By default, datashuttle will not overwrite existing files, so newly acquired data 
can be quickly transferred by 'uploading entire project'. 
Only the new file will be transferred. Or in code.

However, the real power comes from customisable transfers. This is particularly 
useful when downloading subsets of data from the central storage machine to an 
analysis machine FOR ANALYSIS.
Datashuttle has a rich set of keyword argumetns to allow download of custom 
subsets of data. Say you wanted toget XXX. Then you just run XXX
<code vs. graphical interface>

## Logging
A final feature of datashuttle is logging. Makes it easy. Simple photo

Looking forward 
<last parahraph>
Standardisation is incredibly useful, but it should not come with at the 
expensive of in running day-to-day projects less easily than you currently 
are. Datashuttle aims to make managing your project easier than it currently 
is – if it is not, we want to hear why so it can be improved. 
Please get in contact XXX



OLD 

**estimated reading time: 10 minutes**

Standardised data is important for XXX. Specifications are a way to
handle this. In a previous blogpost, we motivate NeuroBlueprint, XXX.

You are now convinced for the critical importance of standardisation and 
want to get started. Now, to simply follow it for your next experiment 
and problem solved! If only real life was so easy. 

While following any specification is better than no specification, to
get the most out of a standardised project, it needs to be *standardised*.
That means every formatting rule obeyed, structure broken or XXX.  
But real life is full of errors. Typos. Forget what the spec is – no time to look up. 
One error means there is no longer standardisation – the goal is lost!

The solution to this problem is to automate as much as possible the 
creation of standardised project folders. This includes filling in
ann non-critical information and performing live-validation of the 
project as we go.

Datashuttle performs this role. It has two ways of using, a Python API to 
integrate into automated pipelines, or a graphical-interface for use in manual 
acquisition pipelines. 

Affords a lot of benefits e.g. data transfer.

Below we’ll do a whistle-stop tour of datashuttle features 
so you can see how it might fit into your analysis pipelines. For a comprehensive 
overview and guides, please see the datashuttle documentation.
Mention neuroblueprint. 

## Introduction to Datashuttle

[THE IMAGE!]

Datashuttle is to be used in the situation when XXX.


## Creating folders with live validation

The first step when making a project is to create project folders. 
You may automate this as part of an acquisition pipeline before saving 
acquired data (e.g. behavioural XX, ephys XX) there. Alternatively you may 
make these by hand prior to setting the output their through an acquisition 
software's graphical user interface.

They key thing at this stage is to ensure no typographical errors slip in, 
and as much detail on formatting and folder structure can be abstracted away.
Through the datashuttle graphical interface, creating new output folders 
is as easy as:

Live validation

Convenience tags - philosophy any non-custom input should be automated.

When creating through the python API, all features are the same. Can get next 
subject or session. The live validation ensures that no problems can slip 
through the next.


## Data Transfer

Data transfer leverages the power of standardised data format to
make convenient transfers. By default, everything is uploaded
with different overwrite options.

However, true power in custom. Let's say.

Download a subset of the data.


## Other benefits and future additions

Logging. 


What is whistlestop tour. Get in contact XXX.





