:blogpost: true
:date: August 7, 2026
:author: Soumya Snigdha Kundu
:location: London, UK
:category: Blog
:language: English
:image: 0

# GSoC 2026: single-channel support in cellfinder

## Introduction

Hi, I'm [Soumya](https://github.com/aymuos15). I was one of the [Neuroinformatics Unit](https://github.com/neuroinformatics-unit) [Google Summer of Code](https://summerofcode.withgoogle.com/) (GSoC) interns for the 2026 summer term, and I worked on broadening the range of inputs [`cellfinder`](https://github.com/brainglobe/cellfinder) accepts, in both channel count and dimensionality.

**Project**: BrainGlobe: expand `cellfinder` input support to 2.5D and single-channel data <br>
**Mentors**: [Igor Tatarnikov](https://github.com/IgorTatarnikov), [Alessandro Felder](https://github.com/alessandrofelder), [Adam Tyson](https://github.com/adamltyson)

---

## Project Overview

`cellfinder` is BrainGlobe's tool for detecting and classifying cells in whole-brain microscopy volumes. By default, two channels are expected by `cellfinder`. This stems from a finding in the original `cellfinder` paper ([Tyson et al., 2021](https://doi.org/10.1371/journal.pcbi.1009074)), where the second channel lets the network learn the difference between neuron-based signals, only present in the primary signal channel, and other non-neuronal sources of fluorescence, potentially present in both channels.

However, collecting a second channel doubles the data volume, and for some fluorophores it is difficult to obtain a channel containing only autofluorescence. These limitations are what originally motivated the [request for single-channel support](https://github.com/brainglobe/cellfinder/issues/352). Making this background channel optional was a major part of my project.

### What changed

The `build_model()` function creates the neural network used to classify candidate cells. The input shape passed to it now reflects the number of channels in the data, allowing the network to accept a signal channel alone. With no background given, `cellfinder` switches to a newly trained single-channel default model automatically, and a channel mismatch raises a clear error. Previously, every pre-trained model `cellfinder` shipped expected two channels.

The same support runs through the napari plugin, so detection, curation and training all work from a signal channel alone. Curation writes only the signal cubes and notes the missing background in the training YAML, so training your own single-channel model needs no extra configuration.

From Python, it is one argument:

```python
from cellfinder.core.main import main

cells = main(
    signal_array=signal,
    background_array=None,
    voxel_sizes=(5, 2, 2),
)
```

In napari, you leave the background image unselected.

### How well does it work

I used the same ResNet-50 architecture and training dataset as the standard two-channel model, but dropped the background channel during training to create our first single-channel model. I then uploaded it to the [Hugging Face Hub](https://huggingface.co/brainglobe/cellfinder_single_channel_default), marking the start of our transition to hosting models there. It downloads automatically on first use, just like the existing models.

I then compared our results against the two-channel model to understand the trade-offs it would have. Early tests on data from a different microscope produced more false positives: objects incorrectly identified as cells. I tested both models on the same set of 10,756 image cubes, containing 5,066 cells and 5,690 non-cell objects, and varied the proportion of cells in the training data to see how it affected the models' performance.

Each model assigns a score to a candidate cell, and a threshold determines whether it is counted as a cell. Using the same threshold for both models does not necessarily give a fair comparison. Instead, I adjusted their thresholds so that both found 99% of the real cells, then measured how often they incorrectly counted non-cell objects as cells.

The single-channel model made more false-positive errors in every training setup. With the original training balance, it incorrectly classified around 4.5% of non-cell objects, compared with 3.6% for the two-channel model. Increasing the proportion of cells in the training data did not close this gap.

| Cells in the training data | Non-cell objects counted as cells: single-channel | Two-channel |
|---|---:|---:|
| 47% (original balance) | 4.46% | 3.58% |
| 60% | 5.09% | 3.83% |
| 70% | 5.65% | 4.18% |
| 80% | 5.08% | 4.05% |

*Values are averages across three training runs.*

### Closing the gap

There is more work to be done here. Warm-start fine-tuning recovers roughly 40% of the gap and a top-hat variant around 28%, while distillation does nothing and hard-negative mining hurts. Substituting a blurred copy of the signal for the missing background also proved unsuccessful, since a real background channel is anti-correlated with the signal at a cell, with a mean background-to-signal intensity ratio of 0.05 at a true cell against 2.00 at a true non-cell, whereas a blurred copy is positively correlated by construction.

A performance drop from two channels was always expected. However, now, if you only have one channel, `cellfinder` runs. We have an explicit offering for it.

---

## Reflections

A big reason I applied for this project is how closely it sits to my PhD work, and it was genuinely interesting to take the techniques I use there and apply them over here, on a different problem and a different kind of data.

Working with a larger group was the other half of it. Seeing how research gets translated into software people can rely on, through review, tests and carefully chosen defaults, was the most useful thing I took from the summer.

I also really enjoyed the opportunity to present this work at the [NIU Open Software Summer School](https://neuroinformatics.dev/slides-osss-intro/#/friday-approximate) and hear some very interesting feedback from the participants.

Single-channel support was one of three deliverables, and I am carrying on with the other two: extending the classifier to two-dimensional and 2.5D input so that brain slices are as well supported as whole volumes, and standardising the axis conventions underneath that make any change to dimensionality error-prone. Both are already under way, incorporating the additional feedback gathered at the summer school, and I am looking forward to seeing them land.

---

## Repositories

- [`cellfinder`](https://github.com/brainglobe/cellfinder)
- [`brainglobe.github.io`](https://github.com/brainglobe/brainglobe.github.io/)

---

*Thank you to my mentors and the whole team at NIU and BrainGlobe for their patience, their reviews, and their guidance throughout the summer!*
