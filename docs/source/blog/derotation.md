:blogpost: true
:date: July 1, 2025
:author: Laura Porta
:location: London, UK
:category: Blog
:language: English
:image: 1

# `derotation`: a Python package for correcting motion artifacts in rotating multiphoton movies

The `derotation` package provides a robust solution for reconstructing multiphoton movies of rotating samples acquired with a line-scanning microscope at high speeds and low frame rates. When imaging a rotating sample, the line-by-line nature of acquisition introduces significant geometric distortions. This package corrects these artifacts to produce clear, stable movies suitable for standard analysis pipelines like Suite2p.

![](https://raw.githubusercontent.com/neuroinformatics-unit/derotation/main/docs/source/_static/mean_images_with_incremental.png)
> **Left**: The mean image from a raw 3-photon movie of a rotating sample. **Center**: The mean image after processing with `derotation`. **Right**: The mean image after further registration with Suite2p. The improvement in cell definition is evident after derotation.

---

## Core Functionality: Line-by-Line Correction

The fundamental principle of the package is **derotation-by-line**. Because a line-scanning microscope acquires an image one horizontal line at a time, a rotating sample causes each line to be captured at a slightly different angle. If the angle of rotation is recorded simultaneously, the `derotation` package can computationally rotate each line back to a common frame of reference, incrementally building a corrected, distortion-free image.

![](https://raw.githubusercontent.com/neuroinformatics-unit/derotation/main/docs/source/_static/derotation_by_line.gif)
> This animation demonstrates the line-by-line reconstruction. The distorted frame (left) is corrected one line at a time based on its specific rotation angle to generate the final, stabilized frame (right).

---

## How to Use `derotation`

The package can be used in two primary ways, offering a trade-off between granular control and automation.

### 1. Low-Level Core Function
For direct control, users can call the `derotate_an_image_array_line_by_line` function. This requires two main inputs:
* The raw multiphoton movie (as a NumPy array).
* The corresponding rotation angle for each captured line.

This approach is ideal for users who have already processed their rotation signals and need to apply the core correction algorithm.

### 2. High-Level Pipelines
For an end-to-end workflow, `derotation` provides two pre-built pipeline classes that automate the entire process from raw data to a corrected movie file.

* **`FullPipeline`**: Designed for experiments with randomized  rotations. It automatically parses analog signals, interpolates angles, uses Bayesian optimization to find the center of rotation, and performs the derotation.
* **`IncrementalPipeline`**: Tailored for continuous, slow rotations.

Both pipelines generate a corrected TIFF stack, metadata files, and debugging plots.

---

## Finding the Center of Rotation

Accurately identifying the **center of rotation** is critical. An incorrect center will result in residual motion, where stationary objects appear to trace circles in the final movie.

![](https://raw.githubusercontent.com/neuroinformatics-unit/derotation/main/docs/source/_static/wrong_center.png)
> When the center of rotation is miscalculated, a stationary cell's center (red crosses) will appear to move in a circular path across different rotation angles.

The package implements two methods to find this center:

1.  **Bayesian Optimization**: Used by the `FullPipeline`, this method is computationally intensive but robust. It iteratively tests potential center coordinates to find the one that minimizes motion in the corrected movie.
2.  **Ellipse Fitting**: The `IncrementalPipeline` tracks the path of a bright, stable object (like a cell) across frames. In a physical rotating system, this path would likely form an ellipse. The center of the fitted ellipse is an accurate estimate of the true center of rotation.

---

## Verification and Synthetic Data

To ensure the quality of the correction and validate the algorithms, `derotation` includes tools for generating and processing synthetic data.

* **`Rotator` Class**: This class can take a static image and apply a virtual line-by-line rotation, simulating the distortion from a real microscope.
* **`SyntheticData` Class**: This builds on `Rotator` to create complete, simulated datasets, including fake cell images and corresponding rotation signals.

![](https://raw.githubusercontent.com/neuroinformatics-unit/derotation/main/docs/source/_static/rotator.gif)
> An animation showing a synthetic dataset of two "cells" being rotated with line-scanning artifacts.

These tools are invaluable for testing and can even simulate complex cases like **out-of-plane rotations**, where the axis of rotation is tilted relative to the imaging plane. In such cases, the package can fit an ellipse to the object's trajectory to calculate the 3D rotation geometry and apply a more sophisticated correction.

---

## Get Involved

`derotation` is an open-source project in active development. Community contributions are welcome.

* **Report Bugs or Request Features**: [Open an issue on GitHub](https://github.com/neuroinformatics-unit/derotation/issues)
* **Discuss Development**: [Join the Zulip chat](https://neuroinformatics.zulipchat.com/#narrow/channel/495735-Derotation)

This project is sponsored by the Margrie Lab at the Sainsbury Wellcome Centre.