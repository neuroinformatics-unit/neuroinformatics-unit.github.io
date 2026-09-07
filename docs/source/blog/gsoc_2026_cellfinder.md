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

The `build_model()` function creates the neural network used to classify candidate cells. The input shape passed to it now reflects the number of channels in the data, allowing the network to accept a signal channel alone. With no background given, `cellfinder` switches to a single-channel model automatically, and a channel mismatch raises a clear error. Every pre-trained model `cellfinder` shipped expected two channels, so this path also needed retraining.

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

I then compared our results against the two-channel model to understand the trade-offs it would have.

- Early use on data from a different microscope threw up more false-positive cells than expected.
- So: cross-validation of single- versus two-channel over three stratified folds, against one frozen test set of 10,756 cubes, 5066 cells and 5690 non-cells.
- Plus a sweep skewing the class balance of the training data, to separate "not enough data" from "weaker input".
- At a fixed threshold the two models look nearly identical, but that is an artefact: they sit at different points on their curves.
- The comparison that shows the difference is at a matched operating point, here a recall of 0.99.

| Training set | Threshold 1-ch | Threshold 2-ch | FP rate 1-ch (%) | FP rate 2-ch (%) |
|---|---|---|---|---|
| Balanced (47% cell) | 0.406 ± 0.018 | 0.495 ± 0.069 | 4.46 ± 0.23 | 3.58 ± 0.04 |
| Skew 60% cell | 0.270 ± 0.046 | 0.599 ± 0.075 | 5.09 ± 0.32 | 3.83 ± 0.06 |
| Skew 70% cell | 0.298 ± 0.082 | 0.663 ± 0.053 | 5.65 ± 0.39 | 4.18 ± 0.09 |
| Skew 80% cell | 0.222 ± 0.044 | 0.760 ± 0.093 | 5.08 ± 0.21 | 4.05 ± 0.16 |

Fixing recall pins both models to the same 5016 cells found and 50 missed, so the whole difference lands in false positives: 254 against 204 on balanced data, 321 against 238 at 70% skew. Those 50 to 80 extra spurious cells never show up in an accuracy score. The thresholds diverge too, and more so with skew, so tune the threshold per model rather than leaving it at the default.

### Closing the gap

There is more work to be done here. Warm-start fine-tuning recovers roughly 40% of the gap and a top-hat variant around 28%, while distillation does nothing and hard-negative mining hurts. Substituting a blurred copy of the signal for the missing background also proved unsuccessful, since a real background channel is anti-correlated with the signal at a cell, with a mean background-to-signal intensity ratio of 0.05 at a true cell against 2.00 at a true non-cell, whereas a blurred copy is positively correlated by construction.

A performance drop from two channels was always expected. However, now, if you only have one channel, `cellfinder` runs. We have an explicit offering for it.

---

## Reflections

A big reason I applied for this project is how closely it sits to my PhD work, and it was genuinely interesting to take the techniques I use there and apply them over here, on a different problem and a different kind of data.

Working with a larger group was the other half of it. Seeing how research gets translated into software people can rely on, through review, tests and carefully chosen defaults, was the most useful thing I took from the summer.

Single-channel support was one of three deliverables, and I am carrying on with the other two: extending the classifier to two-dimensional and 2.5D input so that brain slices are as well supported as whole volumes, and standardising the axis conventions underneath that make any change to dimensionality error-prone. Both are already under way, and I am looking forward to seeing them land.

---

## Repositories

- [`cellfinder`](https://github.com/brainglobe/cellfinder)
- [`brainglobe.github.io`](https://github.com/brainglobe/brainglobe.github.io/)

---

*Thank you to my mentors and the whole team at NIU and BrainGlobe for their patience, their reviews, and their guidance throughout the summer!*
