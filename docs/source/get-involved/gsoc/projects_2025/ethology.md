# GSoC NIU Projects 2025: `ethology`

If you are interested in any of these [ethology](https://github.com/neuroinformatics-unit/ethology) projects, get in touch! Feel free to open a new topic on our [Zulip GSoC channel](https://neuroinformatics.zulipchat.com/#narrow/channel/487898-GSoC) and ask the community.

Our working language is English, but our mentors for these projects also speak Spanish.

:::{dropdown} {fas}`video;sd-text-primary` Support for any-point trackers in `ethology`

The main goal of [`ethology`](https://github.com/neuroinformatics-unit/ethology) is to facilitate the application of a wide range of computer vision tasks to animal behaviour research, by providing a unified data analysis interface across these tasks. 

Any-point tracking is a good example of a computer vision task that is maturing within the field of computer vision, but it still relatively inaccessible to animal behaviour researchers. The task consists on the following: given a video and a set of query points on a frame of that video, predict the location of those points on every other frame of the video. This is a more general problem than the pose estimation one, which typically focuses on predicting the location of a fixed set of keypoints on an animal's body. As a result, any-point tracking tools could prove to be a very valuable tool for studying animal behaviour, with potential to supplement or potentially even replace pose estimation.


Depending on the quality of the trajectories generated by any-point trackers, these could be useful to study the movement patterns of animals directly, or they may be more helpful as a semi-automatic way to quickly generate labelled data. In recent years, there has been an increase in the development of any-point trackers, such as [cotracker3](https://cotracker3.github.io/) and [TAPIR](https://deepmind-tapir.github.io/blogpost.html). The goal of this project is to add support for any-point trackers to `ethology`, so that users can easily apply these tools to their data and analyse the trajectories generated.


**Deliverables**

<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
The expected deliverables include:
- A prototype [napari](https://napari.org/stable/) widget, that allows the user to load a video and select the query points to track. 
- Back-end functionality to read the query points from the napari widget, and run inference on a pre-trained any-point tracker model, such as those provided by [cotracker3](https://cotracker3.github.io/) or [TAPIR](https://deepmind-tapir.github.io/blogpost.html).
- Ability to read the generated trajectories as a `movement` [dataset](https://movement.neuroinformatics.dev/user_guide/movement_dataset.html).
- Front-end support on the napari widget to overlay the trajectories generated by the any-point tracker on the video.
- As a stretch goal, the widget could be extended to allow the user to run inference directly from the napari GUI.

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate or advanced contributor to open source.

**Required skills**

Experience with Python and [PyTorch](https://pytorch.org/).

**Nice-to-haves**
- Experience developing or using [napari](https://napari.org/) plugins.
- Experience with computer vision applications, particularly pose estimation and any-point tracking approaches.


**Potential mentors**

- [@sfmig](https://github.com/sfmig)
- [@niksirbi](https://github.com/niksirbi)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [cotracker3 paper and code](https://cotracker3.github.io/)
- [TAPIR paper and code](https://deepmind-tapir.github.io/blogpost.html)
- [napari usage tutorials](https://napari.org/stable/tutorials/index.html) and [contributing guide](https://napari.org/stable/developers/contributing/index.html).
- [napari Plugin documentation](https://napari.org/stable/plugins/index.html), particularly the section on [Building a plugin](https://napari.org/stable/plugins/building_a_plugin/index.html).
:::

:::{dropdown} {fas}`video;sd-text-primary` Support for low-shot detectors in `ethology`

Low-shot detection is a computer vision task that aims to detect objects in images with very few labelled examples (between 0 and 5). This task can be very useful to researchers in animal behaviour, but it is still somewhat inaccessible to them. For example, it could be particularly useful for collective animal behaviour research, where it may be tedious to obtain large labelled datasets for training accurate detection models. It could also be useful for labelling large datasets collected in the lab, where the collected frames are relatively similar in appearance, as it is common to record videos of animals with static cameras and relatively uniform backgrounds. 

The goal of this project is to support few-shot detection in `ethology`, initially as a semi-automatic approach to labelling bounding boxes. The workflow could look something like this: given a set of frames extracted from a video, the user would load these files into a GUI (likely a [napari](https://napari.org/stable/) widget) and use the GUI annotation tools to manually draw bounding boxes around the object they want to detect. These annotations define the visual prompts, and could be drawn on a single or multiple frames. Then the user would select a low-shot detector model to label the rest of identical instances in the dataset. After the model has labelled the dataset, the user should be able to review the results and correct any mistakes. The final output would be a bounding boxes annotation object, which could then be used to create a detection dataset for training a supervised learning model.



**Deliverables**

<!-- Goals, or expected status after Community Bonding Period, Start of Coding, End of Coding. Stretch goals? -->
The expected deliverables include:
- Back-end functionality with a user friendly API, to read a set of manually labelled bounding boxes and run inference on a pre-trained low-shot detection model, such as those provided by [GeCo](https://github.com/jerpelhan/GeCo) or [CountGD](https://github.com/niki-amini-naieni/CountGD). The detections should be formatted as an `ethology` annotation dataframe. Ideally we would support a couple of models with a similar API.
- A front-end [napari](https://napari.org/stable/) widget, that allows the user to load a set of extracted frames, manually draw bounding boxes around the objects they want to detect, and run inference on the rest of the data using a low-shot detection model. The widget should also allow the user to review and correct the labels generated by the model.
- As a stretch goal, we could explore the possibility of specifying the target with a text prompt, as is done in [CountGD](https://arxiv.org/pdf/2407.04619)

**Duration**
<!-- Small (~90 hours), Medium (~175 hours) or Large (~350 hours)  -->
Large (~350 hours)

**Difficulty**
<!-- Is this project geared more toward a student level or a more advanced developer level? -->
This project is well-suited for an intermediate or advanced contributor to open source.

**Required skills**

Experience with Python and [PyTorch](https://pytorch.org/).

**Nice-to-haves**
- Experience developing or using [napari](https://napari.org/) plugins.
- Experience with computer vision applications, particularly vision transformers and detection.


**Potential mentors**

- [@sfmig](https://github.com/sfmig)
- [@niksirbi](https://github.com/niksirbi)


**Further reading**
<!-- The best pages include links to more detailed descriptions and related materials for each project. They might even include actual use cases! -->
- [GeCo code](https://github.com/jerpelhan/GeCo)
- [GeCo paper](https://arxiv.org/pdf/2409.18686)
- [CountGD code](https://github.com/niki-amini-naieni/CountGD)
- [CountGD paper](https://arxiv.org/pdf/2407.04619)
- [napari usage tutorials](https://napari.org/stable/tutorials/index.html) and [contributing guide](https://napari.org/stable/developers/contributing/index.html).
- [napari Plugin documentation](https://napari.org/stable/plugins/index.html), particularly the section on [Building a plugin](https://napari.org/stable/plugins/building_a_plugin/index.html).
:::


