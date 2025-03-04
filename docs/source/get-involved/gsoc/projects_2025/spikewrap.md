# GSoC NIU Projects 2025: `spikewrap`

If you are interested in any of these [spikewrap](https://github.com/neuroinformatics-unit/spikewrap) projects, 
[get in touch](https://spikewrap.neuroinformatics.dev/community/index.html)! 
Feel free to open a new topic on our [Zulip GSoC channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-GSoC) and ask the community.

Our working language is English.


<!-- ------------------------------ -->
:::{dropdown} {fas}`database;sd-text-primary` Add motion correction preprocessing

Extracellular electrophysiology is a technique used to record the activity of thousands of neurons in the brain simultaneously. 
Understanding how this neural activity drives behavior requires reliably identifying and distinguishing individual neurons 
based on their electrophysiological signatures—a process known as spike sorting.

[spikewrap](https://spikewrap.neuroinformatics.dev/)  is a Python package designed to streamline electrophysiology 
preprocessing and spike sorting across experimental projects. It leverages
[SpikeInterface](https://spikeinterface.readthedocs.io/en/latest/index.html), a popular package that exposes many electrophysiology processing tools.
The aim of spikewrap is to abstract away implementation details and make running electrophysiological analysis as simple as possible.

This project involves adding 'motion correction' preprocessing to spikewrap.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- Add SpikeInterface [motion correction](https://spikeinterface.readthedocs.io/en/latest/modules/motion_correction.html) functionality to spikewrap
- Test motion correction functions.
- Document the new functionality

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours)


**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
In terms of coding requirements, a beginner or intermediate developer would be well suited.
However, the project will require working closely with extracellular electrophysiological data,
which can be quite complex. Therefore, domain knowledge of extracellular electrophysiology would be an advantage.


**Required skills**
Experience with Python and running neuroscience (preferably electrophysiology) experiments.

**Nice-to-haves**
Experience with extracellular electrophysiology.

**Potential mentors**
- [@JoeZiminski](https://github.com/JoeZiminski)

**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->

[spikewrap](https://spikewrap.neuroinformatics.dev/) and [SpikeInterface](https://spikeinterface.readthedocs.io/en/latest/index.html) documentation.

:::


<!-- ------------------------------ -->
:::{dropdown} {fas}`database;sd-text-primary` Extend spikewrap test functionality

[spikewrap](https://spikewrap.neuroinformatics.dev/) is a young project in the prototyping phase.
Testing the package is not straightforward and requires access to GPU hardware and SLURM scheduling software
on a high-performance compute (HPC) cluster. Currently, test suite is currently lagging development.

This project will involve developing a comprehensive test suite for running experimental pipelines in spikewrap.
This will involve running all possible options the software supports on an HPC system, leveraging GPU, SLURM and 
singularity image functionality.

- **Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a beginner to intermediate level developer, in particular with an interest
in testing infrastructure. Less domain knowledge is required for this project compared to `Add motion correction preprocessing`.


**Required skills**
Experience with Python

**Potential mentors**
- [@JoeZiminski](https://github.com/JoeZiminski)

**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->

[spikewrap](https://spikewrap.neuroinformatics.dev/) and [SpikeInterface](https://spikeinterface.readthedocs.io/en/latest/index.html) documentation.

:::
