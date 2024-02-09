# NeuroBlueprint DataShuttle blogpost

Deadline for first draft: 2024-01-29

reading time: 5 minutes (we could edit it down until readable in 5 minutes? I think actually it is close to 5 minutes now)

## The problem of unstandardized neuroscience data

Every year an overwhelming array of valuable neuroscience data is published in scientific journals, expanding our understanding of the brain.  As co-publication of experimental data becomes increasingly common, it is an exciting time for researchers to leverage the powerful resource of open-access data on an unprecedented scale for both replication and discovery.

However the seemingly simple problem of non-standard data organisation between researchers creates significant barriers to collaboration, blunting the effectiveness of the open-access revolution.

On the ground, research within and between labs is often frustrated by the lack of a widely-adopted data organisation scheme in systems neuroscience. This wastes researchers time, prohibits effective collaboration and at worst  leads to mistakes in analysis and reporting.

To address these problems, the [Neuroinformatics Unit](https://neuroinformatics.dev/) at the SWC have developed an easy-to-use data standardisation framework, [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/). This blog post provides an introduction to [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/), motivating the need for a standardised data framework at the SWC and highlighting the place of [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) within the current data-standardisation landscape.

In a companion post, we introduce [DataShuttle](datashuttle.neuroinformatics.dev), a tool to seamlessly automate the implementation of the [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) standard during data collection and onward.


## Organising data is hard

If you've ever received data to analyse from a colleague or downloaded an open-access dataset, you probably know the pain of navigating an unfamiliar territory.

I distinctly remember the first time I received a dataset from collaborators—I was eager to dive in and analyse the rare recordings we had been sent. However my enthusiasm soon gave way to perplexion, followed by frustration and despair. Was "subject1" the same as "Subject01"? Why were some sessions labelled as "EXCLUDED"? What was this never-seen-before file format and which software should I open it with?  It took several weeks of back and forth emails between me and my collaborators to arrive at a coherent consensus on how this dataset was organised. 

This problem is not restricted to sharing data across labs but also manifests within a research group. People sitting in the same room often find each others' folders uninformative, and group leaders may struggle to find that plot they need for tomorrow's presentation amidst the chaos.

![credit: ErrantScience.com](https://hackmd.io/_uploads/r1-kjrTtT.jpg)

Such stories are by no means unique and illustrate that *effective data management is hard*. Often, the problem is not that one researchers organisation system is better than another, but meerly the fact that they are *different* causes problems and confusion.

Standardisation between researchers takes time and capacity away from major project goals in a already busy working enviorment. Scientists are often highly conscientious and make an effort to organise data according to a *system* that makes sense, especially at the start of a project. However as the demands of the project increase, timelines become tighter and without a clear specification to follow, the system mutates over time and eventually entropy wins over. Things are lost in translation and memories fade, despite our best hopes and efforts. 

![credit: ErrantScience.com](https://hackmd.io/_uploads/ryreaP6Ya.jpg)

Nonetheless, the benefits of good data management are enourmous, and not only for the obvious utility in facilitating collaboration.  The person who uses a dataset most heavily is our future self—who is desperate to get that paper submitted. The confusion generaterated by suboptimal data organisation is not only frustrating and time-consuming, but also threatens the validity and reproducibility of our results. 

:::info
### Why should you care about standardizing your data?
It will save **YOU** significant amounts of **PAIN!**.
:::


## Data specifications as a solution

A data specification provides a well-defined file-system organisation schema as a solution to the problem of effective data management. Consisting of a clear set of rules on how data should be organised, it reduces overhead for researchers and facilitates collaboration by ensuring standardised data organisation across projects. 

:::info
### Data Specification: 
A system that describes how a dataset is organised (**spec** for short) and consists of a set of rules that directly *specify* how a dataset should be organised.
:::

So what makes for a good specification?

- **On the record**. Specs must be written down and made available to the relevant data producers and consumers.
- **Explicit**. The rules included in the spec should be clear and leave little room for ambiguity. 
- **Widely accepted**. Ideally, you should not come up with your own system, but adopt an already existing one used by your group, department, institute or even field. 


Let's look at two concrete specifications that have been most successful in neuroscience—[Brain Imaging Data Structure (BIDS)](https://bids.neuroimaging.io/) and [NeuroData Without Borders (NWB)](https://www.nwb.org/)—and explore the role of [NeuroBlueprint]() within the current data-specification landscape.

### Brain Imaging Data Structure (BIDS)

BIDS is a data specification widely used in human neuroimaging, with recent extensions to systems neuroscience (e.g. [electrophysiology](https://github.com/bids-standard/bep021)). It has intutive and considered design, developed by hundreds of researchers to ensure consensus. BIDS is comprehensive and detailed specification, albiet with some strict requirements (e.g. use of certain file formats, metadata requirements).

However, BIDS has a level of detail that can be intimidating and complex to new users and make full complaince difficult, especially during data collection. BIDS is considered the gold-standard of standardisation for data-sharing, but widespread adoption is hampered by it's complexity.

### NeuroData Without Borders (NWB)

In contrast to BIDS, NWB has a focus not on folder-system organisation but on providing unified open-access file format that can, in theory, contain an entire project and metadata within it. This is a welcome introduction in the land of neuroscience populated by an unweidly array of complex, often closed file formats pose a significant hurdle to data-sharing.

NWB is the primary open-access file format for data-sharing in systems neuroscience. However, it can be difficult to adopt, especially for users with lack of programming experience and if the format of your raw data is not yet supported for conversion to NWB. Additionally during the data-collection stage, storage of all data in a single file can be prohibitively inflexible. 

## The [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specification

[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) has been developed for use in the SWC as an easy-to-use specification with a low barrier for entry (you should be able to read the [full specification](https://neuroblueprint.neuroinformatics.dev/specification.html) in less than 5-10 mins?? CHECK minutes). Acutely aware of profilerating yet another standard, [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) aims to couple as tightly as possible to BIDS, allowing it to act as a stepping stone to more comprehensive data-organisation schemes following data collection.

[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specifies that data should be organised in a particular folder structure, with nested subject, session and datatype (e.g. electrophysiology, behaviour) levels. The naming of these folders should adhere to a certain style, as exemplified below:

![NeuroBlueprint_project_tree_light](https://hackmd.io/_uploads/Sys4pvpF6.png)

While the full specification is available to read [here](https://neuroblueprint.neuroinformatics.dev/specification.html), we provide a breif summary of it's main features below:

- A top-level distinction splitting raw data, ("rawdata"), and any data derived from processing the raw data ("derivatives").
- Heirchical subject-session-datatype organisation, capturing a model where individual subjects may undergo repeated experimental sessions.
- Requirement for unique subject and session IDs with filenames structures as key-value pairs.
- No hard specification on filenames, but recommended structure provided.


#### Limitations 

Currently, [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) is not designed for multi-animal or group experiments where sessions may include interactions between multiple subjects. However, such an extension is in development.

### Getting Started

Getting started with [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) is as easy as reading the [specification](https://neuroblueprint.neuroinformatics.dev/specification.html), and organising your experimental folders according to the standard. You can also read more about it [here]. 

It's recommended to get started by using [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) with your next experiment, rather than trying to re-organisise existing folders and analysis code, which is always tricky. However, it may be a useful template for anyone struggling with re-organising their data for open-access publicaiton.

We are very keen for feedback on the [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specification and happy to make adjustments where required. Please don't hesitate to get in contact with us XXXX.


### Why not just promote an existing standard?
[This is a super important section, but I wonder if this is motivated enough by the above secetion and could be removed, to keep focus on the benefits of [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) at this stage in the post. That been said this is very important to address so if it is not sufficiently covered by the above we should keep.]

We are acutely aware of the dangers of creating a new standard:

![source: xkcd.com/927](https://imgs.xkcd.com/comics/standards.png)


The aim of [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) is to fill a gap in the specification scheme, for a low-barrier to entry and easy-to-use specification, that researchers can get started with immediately. While BIDS and Neurodata without borders are gold-standard sceheme for data publlication, their emphasis is on consumers of open-access data sharing which can be difficult to maintainduring data acquisition.

[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specification is closely tied to the BIDS specification whevever possible, and further extends to systems neuroscience. This means for researchers wanting to convert their data to full BIDS compliance, the [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specification will be an excellent starting step. 

To incentivise data producers to get started, the entry requirements should be minimal. Introduce tha idea of an on-ramp and a virtuous cycle. Some standard is better than none.

We still (partly) follow the BIDS logic [wherever possible] and file formats can still be NWB.

Talk about the specific need systems neuro and justify our departures from BIDS.


<br><br><br><br><br><br><br><br>










### What's next for NeuroBlueprint?
[Maybe remove this section and put something on the website?]
- easy-to-use graphical interface (almost there)
- multi-subject session support?
- metadata specs
- recommendations for good file formats per datatype
- NB will keep evolving, tell us what you think!

## Problem 2: implementing a spec by hand is hard
- illustrate with examples (error-prone, laborious)
- motivate need for automated tools
- specific for systems neuro: acquiring multi-modal data from multiple computers

## Solution 2: datashuttle
- show show what is it capable of
- automation of folder naming
- syncing from multiple remotes to central

## Outlook and Call-to-Action
- Both NeuroBlueprint adn DataShuttle living projects
- TUI coming!
- We will keep updating based on feedback
- Test it and let us know what you need
