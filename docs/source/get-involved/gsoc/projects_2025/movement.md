# GSoC NIU Projects 2025: `movement`

If you are interested in any of these [movement](https://github.com/neuroinformatics-unit/movement) projects, [get in touch](https://movement.neuroinformatics.dev/community/index.html)! Feel free to open a new topic on [Zulip GSoC channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-GSoC) and ask the community.

Our working language is English, but our mentors for these projects also speak Spanish.

<!-- ------------------------------ -->
:::{dropdown} {fas}`video;sd-text-primary` Support for Kalman filters in `movement`
One of `movement`'s [priority features](https://movement.neuroinformatics.dev/community/roadmaps.html#long-term-vision) is to support versatile and efficient methods for data cleaning and filtering. To this aim, we would like to add support for applying Kalman filter in `movement`.

In its simplest implementation, we would like to be able to use Kalman filters to smooth position, velocity and acceleration timeseries. However, the same functionality could be expanded to other use cases, for example to fix identity switches between animals in multi-animal tracking data, or to improve point trajectory estimations by aggregating information from multiple sources. We are open to either implementing from scratch or wrapping an existing Python implementation. We would like to work with the GSoC contributor to design the best possible solution.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A Python implementation of a Kalman filter for smoothing position, velocity and acceleration timeseries.
- A Python implementation of a Kalman filter for fixing identity switches in multi-animal tracking data (stretch goal).
- Tests to cover any added functionality.
- Documentation for the new functionality.
- An example use case in the `movement` [gallery](https://movement.neuroinformatics.dev/examples/index.html).

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours).

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a student or a beginner contributor to open source.

**Required skills**

Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).


**Nice-to-haves**
- Experience with [xarray](https://docs.xarray.dev/en/stable/index.html) and [pytest](https://docs.pytest.org/en/stable/).
- Familiarity with pose estimation frameworks and their usual workflow ([DeepLabCut](https://www.mackenziemathislab.org/deeplabcut), [SLEAP](https://sleap.ai/), [idtracker](https://idtracker.ai/latest/)...)
- Experience or interest in digital signal processing methods, linear dynamical systems or state space modelling.

**Potential mentors**
- [@niksirbi](https://github.com/niksirbi)
- [@sfmig](https://github.com/sfmig)

**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- `movement` [mission and scope](https://movement.neuroinformatics.dev/community/mission-scope.html#target-mission), [roadmap](https://movement.neuroinformatics.dev/community/roadmaps.html#target-roadmaps) and [contributing guide](https://movement.neuroinformatics.dev/community/contributing.html#target-contributing).
- [KalmanFilter.NET tutorial](https://www.kalmanfilter.net/default.aspx).
- An [example implementation](https://github.com/joacorapela/lds_python) in Python using linear dynamical systems for tracking.
- Python implementations of Kalman filters, such as [pykalman](https://github.com/pykalman/pykalman)
- State-space models packages with support for Kalman filters, such as [dynamax](https://movement.neuroinformatics.dev/examples/index.html), or time series analysis packages such as [darts](https://unit8co.github.io/darts/index.html).
:::


<!-- ------------------------------ -->
:::{dropdown} {fas}`video;sd-text-primary` Implementing outlier detection algorithms in `movement`

A common issue with most popular pose estimation frameworks used in animal behaviour research is that often they produce inaccurate results that are difficult to detect without manual inspection. For example, for a few frames, the bodypart of an animal may be incorrectly located in a position far from the rest of the bodyparts, leading to a "jerky" and unrealistic trajectory.

The goal of this project is to add functionality to easily detect such outlier keypoints, so that users can perform quality control on the predicted keypoints and remove or correct erroneous or implausible ones. Following the ideas implemented in the [LightningPose](https://github.com/paninski-lab/lightning-pose) framework, we would like to implement outlier detection methods based on the heuristics below:
- *temporal smoothness*: often we can assume that the changes in position from frame `f` to frame `f+1` should be smooth. For example, if the animal is moving in a straight line, the position of the mean keypoint should not change abruptly. This is not always the case, for example eye or head movements, may be saccadic, but it does cover a large number of cases.
- *pose plausibility*: the position of the keypoints should be plausible given they represent bodyparts in an animal. For example, if the animal is walking, the position of the keypoints should be consistent with the animal's body shape and the expected range of motion of the joints. One way to implement this constraint could be following LigthningPose's approach, which derives "plausibility" using principal component analysis - i.e. a pose is flagged as implausible if it lies outside a certain low-dimensional subspace.
- *multi-view consistency*: given two or more views of the same animal (e.g. using two cameras, or a camera and a mirror showing a different view), the two views of the same keypoint must be consistent in 3D. This means they should be "projectable" to some 3D subspace (computed for example with principal components analysis), because the true position of that keypoint is a single point in 3D.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- Implementing an outlier detection module, with methods for temporal smoothness, pose plausibility and multi-view consistency.
- Tests to cover any added functionality.
- Documentation for the new functionality.
- An example use case in the `movement` [gallery](https://movement.neuroinformatics.dev/examples/index.html).

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well suited for an intermediate contributor to open source.

**Required skills**

Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).


**Nice-to-haves**
- Experience with [xarray](https://docs.xarray.dev/en/stable/index.html) and [pytest](https://docs.pytest.org/en/stable/).
- Familiarity with pose estimation frameworks and their usual workflow (see for example [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut), [SLEAP](https://sleap.ai/) or [idtracker](https://idtracker.ai/latest/)).
- Experience or interest in digital signal processing methods, linear dynamical systems or state space modelling.


**Potential mentors**
- [@niksirbi](https://github.com/niksirbi)
- [@sfmig](https://github.com/sfmig)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- `movement` [mission and scope](https://movement.neuroinformatics.dev/community/mission-scope.html#target-mission), [roadmap](https://movement.neuroinformatics.dev/community/roadmaps.html#target-roadmaps) and [contributing guide](https://movement.neuroinformatics.dev/community/contributing.html#target-contributing).
- LightningPose [paper](https://www.nature.com/articles/s41592-024-02319-1) and [codebase](https://github.com/paninski-lab/lightning-pose/blob/main/lightning_pose/losses/losses.py)
:::

<!-- ------------------------------ -->
:::{dropdown} {fas}`video;sd-text-primary` Calibrating confidence scores in `movement`

Most pose estimation frameworks provide a confidence score for each predicted keypoint, but these scores are often not well-calibrated, i.e. they do not reflect the true probability of that keypoint being correctly detected. It would be very useful to be able to produce calibrated confidence scores of the keypoint predictions. This would allow us to more fairly compare results across pose estimation frameworks, better filter high/low confidence values, and better interpret model performance.

The goal of this project would be to implement a method to calibrate the confidence scores provided by the pose estimation frameworks supported in `movement`.

One approach to implement this could be similar to the one presented in [keypoint-moseq](https://github.com/dattalab/keypoint-moseq), where the confidence scores are calibrated using an interactive widget that fits a regression line to the log(confidence), log(error) pairs obtained through annotation. 

Another option could be to calibrate the confidence scores using a logistic regression model. The model is trained on a dataset of ground truth keypoints and the corresponding confidence scores, and then used to predict the true probability of the keypoint being correctly detected.

We are open to other suggestions and would like to work with the GSoC contributor to design together a good working solution.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A Python implementation of a method to calibrate the confidence scores provided by at least one of the pose estimation frameworks supported in `movement` (DeepLabCut, SLEAP, LightningPose, anipose).
- Tests to cover any added functionality.
- Documentation for the new functionality.
- An example use case in the `movement` [gallery](https://movement.neuroinformatics.dev/examples/index.html).


**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for a beginner or intermediate contributor to open source.

**Required skills**

Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**
- Experience with [xarray](https://docs.xarray.dev/en/stable/index.html), [pytest](https://docs.pytest.org/en/stable/) or [napari](https://napari.org/stable/).
- Familiarity with pose estimation frameworks and their usual workflow (see for example [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut), [SLEAP](https://sleap.ai/) or [idtracker](https://idtracker.ai/latest/)).
- Experience with supervised machine learning methods and probability calibration.

**Potential mentors**
- [@niksirbi](https://github.com/niksirbi)
- [@sfmig](https://github.com/sfmig)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
There are nice explanations of the calibration issue for the case of classification (but note that in pose estimation we solve a regression problem, not a classification one):
- [Calibrating Neural Networks](https://geoffpleiss.com/blog/nn_calibration.html)
- [Scikit-learn: probability calibration](https://scikit-learn.org/stable/modules/calibration.html)
:::

<!-- ------------------------------ -->
:::{dropdown} {fas}`video;sd-text-primary` Web-based graphical user interface for `movement`

As stated in its [design principles](https://movement.neuroinformatics.dev/community/mission-scope.html#design-principles), `movement` is committed to ensuring ease of use and broad accessibility, to support scientist and researchers of all coding levels. This involves developing an intuitive graphical user interface (GUI), which the team has implemented using [napari](https://napari.org/stable/), a popular Python library for n-dimensional image visualisation, annotation, and analysis.

However, there would be additional value in providing a web-based GUI for `movement`. Specifically one that would allow for interactive data visualisations within Jupyter Notebooks, a tool very popular among data scientists and researchers particularly during data exploration stages. A web-based GUI may also allow for easier sharing of results and analyses with collaborators, and may facilitate cloud-based workflows

The goal of this project is to develop a prototype for a web-based GUI for `movement`. At this early stage, we think it makes sense to explore both options (napari-based and web-based) and evaluate their respective strengths and limitations. They should be independently developed but strive to present a consistent interface to the user.

**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
A good prototype for a web-based GUI for `movement` would include the following features:
- Data loading functionality: ability to load a file containing keypoint or bounding boxes trajectories in the formats supported by `movement`.
- Video visualisation: ability to overlay the imported trajectories on top of the associated video, and go through them frame by frame.
- Data exploration: ability to filter, sort and visualise the trajectories in different ways. For example, the user may want to only visualise the trajectories of a single animal, or only the trajectories of a subset of keypoints.
- Exporting functionality: ability to export the data visualisation as a video or as a set of images.


**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate contributor to open source.

**Required skills**

Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**
- Experience with [xarray](https://docs.xarray.dev/en/stable/index.html) and [pytest](https://docs.pytest.org/en/stable/).
- Familiarity with pose estimation frameworks and their manual annotation workflow (see for example [DeepLabCut](https://www.mackenziemathislab.org/deeplabcut)or [SLEAP](https://sleap.ai/)).
- Experience developing data web apps in Python, with tools such as [Dash Plotly](https://dash.plotly.com/) or [fastplotlib](https://github.com/fastplotlib/fastplotlib).
- Interest in data visualisation.


**Potential mentors**
- [@niksirbi](https://github.com/niksirbi)
- [@sfmig](https://github.com/sfmig)


**Further reading**
- [dash-plotly tutorials](https://dash.plotly.com/tutorial) and documentation, especially the sections "Dash fundamentals" and "Dash callbacks".
- [fastplotlib examples](https://www.fastplotlib.org/_gallery/index.html) and documentation.

:::

<!-- ------------------------------ -->
:::{dropdown} {fas}`video;sd-text-primary` Front-end support for filtering module in `movement`

One of the key features of `movement` is its filtering module, which allows users to clean and process their data before further analysis. However, the current implementation of the filtering module is only accessible via Python scripting, which can be inconvenient for users who are less familiar with programming. To make `movement` more accessible to a wider audience, we would like to add a filtering widget to our [napari](https://napari.org/stable/) graphical user interface.

The goal of this project is to develop this user-friendly interface for the filtering module that allows users to interactively apply filters to their data. This will involve designing and implementing a widget (or set of widgets) that allow users to select the filters they want to apply, adjust their parameters, and preview the results. The interface should be intuitive and easy to use, with clear visual feedback to help users understand the effects of each filter.


**Deliverables**
<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
- A user-friendly [napari](https://napari.org/stable/) widget that acts as a front-end to `movement`'s filtering module. We would like to support at least the following methods: filter by confidence, median filter and the SavGol filter. The user should be able to adjust the parameters of each filter and preview the results in real-time.
- A set of widgets that allow users to select filters, adjust their parameters, and preview the results.
- Tests to cover any added functionality.
- Documentation for the new functionality.
- A short video tutorial demoing the widget's use (stretch goal).

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Medium (~175 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate contributor to open source.

**Required skills**

Experience with Python, [NumPy](https://numpy.org/doc/stable/index.html) and/or [pandas](https://pandas.pydata.org/docs/index.html).

**Nice-to-haves**
- Experience developing or using [napari](https://napari.org/) plugins.
- Interest in data visualisation.
- Experience with digital signal processing methods or time series analysis.
- Familiarity with pose estimation frameworks and their usual workflow ([DeepLabCut](https://www.mackenziemathislab.org/deeplabcut), [SLEAP](https://sleap.ai/), [idtracker](https://idtracker.ai/latest/)).

**Potential mentors**
- [@niksirbi](https://github.com/niksirbi)
- [@sfmig](https://github.com/sfmig)

**Further reading**
- [napari usage tutorials](https://napari.org/stable/tutorials/index.html) and [contributing guide](https://napari.org/stable/developers/contributing/index.html).
- [napari Plugin documentation](https://napari.org/stable/plugins/index.html), particularly the section on [Building a plugin](https://napari.org/stable/plugins/building_a_plugin/index.html).
:::

