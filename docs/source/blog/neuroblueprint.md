# NeuroBlueprint DataShuttle blogpost

reading time: 5 minutes (we could edit it down until readable in 5 minutes? I think actually it is close to 5 minutes now)

## The problem of unstandardized neuroscience data

Every year an overwhelming array of valuable neuroscience data is published in scientific journals, expanding our understanding of the brain. As co-publication of experimental data becomes increasingly common, it is an exciting time for researchers to leverage the powerful resource of open-access data on an unprecedented scale for both replication and discovery.

However the seemingly simple problem of non-standard data organisation between researchers creates significant barriers to collaboration, blunting the effectiveness of the open-access revolution. On the ground, research within and between labs is often frustrated by the lack of a widely-adopted data organisation scheme in systems neuroscience. This wastes researchers' time, prohibits effective collaboration and at worst  leads to mistakes in analysis and reporting.

To address these problems, the [Neuroinformatics Unit](https://neuroinformatics.dev/) at the SWC have developed an easy-to-use data standardisation framework, [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/). This blog post provides an introduction to [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/), motivating the need for a standardised data framework at the SWC and highlighting [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/)'s place within the current data standardisation landscape.

In a companion post, we introduce [DataShuttle](datashuttle.neuroinformatics.dev), a tool to seamlessly automate the implementation of the [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) standard during data collection and onward.


## Why should you care?

Making sense of someone else's data can often feel like navigating a maze. The initial excitement for analysing a fresh dataset can quickly turn into confusion and frustration. Questions about inconsistent naming conventions ("Is `subject1` the same as `Subject01`?"), unclear labels ("Why are some sessions marked as `EXCLUDED`?"), and unfamiliar file formats may trigger weeks of back-and-forth emails and sap all enthusiasm.

This issue doesn't just concern collaborations with external partners; it's prevalent within research teams too. It's common to find colleagues puzzled by each other's filing systems or a group leader scrambling to locate a crucial graph for an upcoming presentation. The main issue isn't that one person's system is superior to another's; rather, it's their differences that lead to confusion.

![credit: ErrantScience.com](https://hackmd.io/_uploads/r1-kjrTtT.jpg)

In general, **good data management is hard**.  Trying to get everyone on the same page takes time and effort away from the big-picture goals, especially in the non-stop world of research. Scientists tend to be diligent folks and usually kick off a project with a neat system for keeping their data in order. But as the project picks up speed, deadlines get tighter, and without a clear plan to stick to, that neat system begins to fray at the edges. Before you know it, things get messy, stuff gets misplaced, and what was once clear is now a fog.

![credit: ErrantScience.com](https://hackmd.io/_uploads/ryreaP6Ya.jpg)

However, the **payoff for good data management is huge**, not just for teamwork but also for your future self who's racing to submit a paper. The headaches and time lost to disorganised data aren't just frustrating; they can undermine the integrity and reproducibility of your work. In other words:

:::info
### Standardising your data will save *YOU* significant amounts of *PAIN*!
:::


## Data specifications as a solution

**Data specifications**, or **specs** for short, tackle the aforementioned challenges by establishing explicit rules for the naming and organisation of files and folders. They simplify the process for researchers and enhance collaboration through standardised data organization practices across projects.

In other words, specs serve as a way for people (and machines) to agree on using the same data organisation scheme.

Key elements of an effective data spec include:

- **Documentation:** Specs should be thoroughly documented and accessible to all relevant parties involved in data handling.
- **Clarity:** The guidelines within the spec need to be precise, minimising any chance for confusion.
- **Adoption:** Rather than creating a bespoke system, it's preferable to use a widely recognised spec already in use by your group, department, institute, or research field.


Let's look at two concrete specifications that have been most successful in neuroscience—[Brain Imaging Data Structure (BIDS)](https://bids.neuroimaging.io/) and [NeuroData Without Borders (NWB)](https://www.nwb.org/)—and explore the role of [NeuroBlueprint]() within the current data specification landscape.

### Brain Imaging Data Structure (BIDS)

The [Brain Imaging Data Structure (BIDS)](https://bids.neuroimaging.io/) is a widely adopted data specification in the field of human neuroimaging. Developed through the collaborative efforts of hundreds of researchers, BIDS is known for its intuitive design and comprehensive guidelines. It offers explicit rules for folder and file naming, file formats, and metadata, and is supported by a broad [ecosystem of software tools and data repositories](https://bids.neuroimaging.io/benefits.html).

However, BIDS has a level of detail that can be intimidating to new users and make full compliance difficult, especially during data collection. Originally built for human neuroimaging (MRI), BIDS has been expanded to include other modalities but it currently falls short of fully accommodating the varied experimental techniques and data prevalent in systems neuroscience. Efforts are underway to bridge this gap, such as the extension proposal for [animal electrophysiology](https://bids.neuroimaging.io/bep032). Yet, the need for legacy support, backward compatibility, and broad consensus slows down these extensions, understandably so for maintaining the integrity and broad utility of the specification.

### NeuroData Without Borders (NWB)

[NeuroData Without Borders (NWB)](https://www.nwb.org/) takes a different approach compared to BIDS. Rather than focusing on how folders and files are organized, NWB provides a unified, open-access file format able to encapsulate an entire project and its metadata in one file. This approach is particularly valuable in neuroscience, where diverse and often proprietary file formats pose a significant hurdle to data sharing.

NWB has established itself as the primary open-access file format for data-sharing in systems neuroscience. However, it can be difficult to adopt, especially for those without programming experience or when the raw data format is not yet supported for conversion to NWB. Moreover, consolidating all data into a single file might not always be practical, especially during the data collection phase where flexibility is crucial.

## The [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specification

[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) has been developed for use in the SWC as an easy-to-use specification with a low barrier for entry (you should be able to read the [full specification](https://neuroblueprint.neuroinformatics.dev/specification.html) in less than 5-10 mins?? CHECK minutes). Acutely aware of profilerating yet another standard, [NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) aims to couple as tightly as possible to BIDS, allowing it to act as a stepping stone to more comprehensive data-organisation schemes following data collection.

[NeuroBlueprint](https://neuroblueprint.neuroinformatics.dev/) specifies that data should be organised in a particular folder structure, with nested subject, session and datatype (e.g. electrophysiology, behaviour) levels. The naming of these folders should adhere to a certain style, as exemplified below:

![NeuroBlueprint_project_tree_light](https://hackmd.io/_uploads/Sys4pvpF6.png)

While the full specification is available to read [here](https://neuroblueprint.neuroinformatics.dev/specification.html), we provide a brief summary of its main features below:

- A top-level distinction splitting raw data, ("rawdata"), and any data derived from processing the raw data ("derivatives").
- Heirchical subject-session-datatype organisation, capturing a model where individual subjects may undergo repeated experimental sessions.
- Requirement for su
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
