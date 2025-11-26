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

**Introduction**

We will begin with a high-level overview of extracellular electrophysiology data, including:
- Probe layouts and channel maps, timeseries sampling and accessing the associated metadata on the probe
- Visualising the probe and acquired data in SpikeInterface
- Implementing a simple pipeline in SpikeInterface, including preprocessing (phase shift, filtering, 
common median referencing), sorting (e.g. `kilosort4`) and computing quality metrics.

**Preprocessing**

We will extend the pipeline developed on Monday by exploring:
- Advanced preprocessing methods ([IBL tools](https://figshare.com/articles/online_resource/Spike_sorting_pipeline_for_the_International_Brain_Laboratory/19705522)
for assessing raw data quality, [DREDGE](https://www.nature.com/articles/s41592-025-02614-5) motion correction)
- The theory behind the applied preprocessing steps.
- Concatenating recordings for multi-session studies

**Sorting**

In the afternoon session, we will run multiple sorters
(e.g. `kilosort4`, `spyking circus 2`, `mountainsort`) and compare the outputs
in SpikeInterface. We will discuss the inner workings of a sorter in detail.
We will also cover unit matching for multiple sessions.

**Assessing Sorting Quality**

In this session, we will cover how to assess the quality of the sorting outputs:
- Introduction to the different types of quality metrics
- Computing quality metrics in [SpikeInterface](https://spikeinterface.readthedocs.io/en/latest/modules/qualitymetrics.html)
and [Bombcell](https://github.com/Julie-Fabre/bombcell)
- Assessing the sorter output in the [SpikeInterface GUI](https://github.com/SpikeInterface/spikeinterface-gui)

**Afternoon: Analysing Outputs**

In the final session, we will focus on combining spike sorting outputs with behavioural events
for analysis. This will include time alignment between electrophysiology and behavioural
events, and using [pynapple](https://github.com/pynapple-org/pynapple) to generate outputs (e.g. peristimulus time histograms).

## Instructors
- [Joseph Ziminski](https://github.com/JoeZiminski)

## Prerequisites

The only prerequisite is a basic knowledge of programming in Python, and the scientific Python ecosystem. 
For those without this background, the [preparatory month](https://neuroinformatics.dev/open-software-summer-school/index.html#preparatory-month) 
will equip you with all the skills needed to make the most of this course. 

### Hardware

You will need to bring your own laptop with Python installed. We will provide a small
test dataset, so any fairly recent laptop will be sufficient. A GPU is not required.

### Data
Sample data will be provided, but if you have any of your own extracellular electrophysiology data, please bring it with you.

