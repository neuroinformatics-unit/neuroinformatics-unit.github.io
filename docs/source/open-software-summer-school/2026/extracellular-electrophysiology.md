(track-extracellular-ephys)=
# Track: Extracellular Electrophysiology

Alongside the development of high-density recording probes (e.g. [Neuropixels](https://www.neuropixels.org/)), 
the range and  complexity of extracellular electrophysiology preprocessing methods has greatly increased in recent years. 
In this course, we will cover the theory and practical implementation of the full extracellular
processing pipeline, including preprocessing, sorting and quality control. 

We will use [SpikeInterface](https://spikeinterface.readthedocs.io/en/stable/) 
to implement the pipeline, with manual curation in the [SpikeInterface GUI](https://github.com/SpikeInterface/spikeinterface-gui). 
We will explore modern toolkits for sorting quality assessment ([Bombcell](https://github.com/Julie-Fabre/bombcell)), 
unit matching ([UnitMatch](https://github.com/EnnyvanBeest/UnitMatch)) and downstream analysis ([pynapple](https://github.com/pynapple-org/pynapple)).

::: {admonition} Target audience
:class: note

This course is suitable for researchers and students with no experience in extracellular electrophysiology.
However, experienced users interested in using SpikeInterface or exploring the theory of processing steps 
in more detail will also benefit.

This course is focused on analysing high-density recordings (e.g. Neuropixels).
:::

## Course overview

**Monday — Introduction**

_Morning_  

We will begin with a high-level overview of extracellular electrophysiology data, including:
- Probe layouts and channel maps, timeseries sampling and accessing the associated metadata on the probe
- Visualising the probe and acquired data in SpikeInterface
- Implementing a simple pipeline in SpikeInterface, including preprocessing (phase shift, filtering, 
common median referencing), sorting (e.g. `kilosort4`) and computing quality metrics.

**Tuesday — Preprocessing & Sorting**

_Morning: Preprocessing Deep Dive_

We will extend the pipeline developed on Monday by exploring:
- Advanced preprocessing methods ([IBL tools](https://figshare.com/articles/online_resource/Spike_sorting_pipeline_for_the_International_Brain_Laboratory/19705522)
for assessing raw data quality, [DREDGE](https://www.nature.com/articles/s41592-025-02614-5) motion correction)
- Concatenating recordings for multi-session studies

We will also have talks that go through the theory of the applied preprocessing steps.


_Afternoon: Running and Comparing Sorters_

In the afternoon session, we will run multiple sorters
(e.g. `kilosort4`, `spyking circus 2`, `mountainsort`) and compare the outputs
in SpikeInterface. We will also cover unit matching for multiple sessions.

This section will include a talk going through the internal operations of a sorter in detail.

**Wednesday — Quality Assessment & Downstream Analysis**

_Morning: Assessing Sorting Quality_

In this session, we will cover how to assess the quality of the sorting outputs.
This will include a lecture on the different quality metrics as well as:
- Computing quality metrics in [SpikeInterface](https://spikeinterface.readthedocs.io/en/latest/modules/qualitymetrics.html)
and [Bombcell](https://github.com/Julie-Fabre/bombcell)
- Assessing the sorter output in the [SpikeInterface GUI](https://github.com/SpikeInterface/spikeinterface-gui) 
(you are also free to use Phy here if you have it installed).

_Afternoon: Analyzing Outputs_

In the final session, we will focus on combining spike sorting outputs with behavioural events
for analysis. This will include time alignment between electrophysiology and behavioural
events, and using [PyNapple](https://github.com/pynapple-org/pynapple) to generate outputs (e.g. peristimulus time histograms).

## Instructors
- [Joseph Ziminski](https://github.com/JoeZiminski)

## Prerequisites

TODO: python is the only pre-requisite, I guess we will all link in the same
way to the python pre-course

### Hardware

You will need to bring your own laptop with Python installed. We will provide a small
test dataset, so any fairly recent laptop will be sufficient. A GPU is not required.

### Software

TODO: see prerequisites section and python knowledge

For general software requirements, please see the [prerequisites](target-general-prerequisites) on the 
main event page and make sure you have these installed and properly configured.

We will install other software required (e.g. SpikeInterface, Kilosort, or another sorter of
your choice) during the course.


### Python knowledge

TODO: SEE PREREQUISITES

### Data

We will provide a small test dataset for the purposes of the course, that will
run quickly without requiring significant memory or a GPU. 

However, please feel free to bring your own datasets. We are happy to discuss your data and
help you try out the methods covered in the course on it. 

