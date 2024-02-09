# NIU behavioural dev meetings

- scheduled for evey 2nd Friday 11:00-12:00
- [movement project board](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2)

## 2024-02-09
- In attendance:
  - x 
- Discuss:
    - Sofia: thoughts about a 'computer-vision utils package'? Initially mainly focusing on detection. To include utils such as frame extraction (probs this would be the place to start), video cropping, clipping, reencoding. A similar role of what movement is to WAZP dashboard, but going towards a [Spike Interface](https://github.com/SpikeInterface/spikeinterface) model --> moved to next meeting
    - conference senses in motion, Brandon may present a pitch / concept / roadmap on movement: can we recycle Niko's material from previous conference?
    - Sofía: poses clustering in movement (something like [this](https://deeplabcut.github.io/DeepLabCut/docs/recipes/ClusteringNapari.html#clustering-in-the-napari-deeplabcut-gui))?
    - Niko: possible chance to hack togother with NWB folks for integration with ndx-pose
    - Niko: some feedback on napari widget
    - Niko: positive response from the [napari-video](https://github.com/janclemenslab/napari-video) developer
        - they're willing to maintain it and welcome external contributions
        - they'd like to chat next week
        - they also have [xarray-behave](https://github.com/janclemenslab/xarray-behave) which has some similarities to movement
    - Niko: Meet with Timothy Dunn ([DANNCE](https://github.com/spoonsso/dannce) developer)
    - CH: [PR #106](https://github.com/neuroinformatics-unit/movement/pull/106) `compute_norm`, `compute_theta`

## 2024-01-26

- In attendance:
    - CH
    - Niko
    - Brandon
    - Sofia
- discuss:
    - proposed [feature](https://github.com/neuroinformatics-unit/movement/issues/102): pose to bounding boxes annotations
    - implementing the 3 unsupervised losses from [LightningPose](https://github.com/danbider/lightning-pose) - temporal smoothness, multi-view consistency, and pose plausibility - as outlier detection methods during pose filtering. See details on [Zulip](https://neuroinformatics.zulipchat.com/#narrow/stream/406001-Movement/topic/LightningPoses.20losses.20for.20outlier.20detection).
    - Niko: report on movement packaging progresss (pip and conda-forge)
    - Niko: demo of reading pose tracks into napari
    - Sofia: thoughts about a 'computer-vision utils package'? Initially mainly focusing on detection. To include utils such as frame extraction (probs this would be the place to start). A similar role of what movement is to WAZP dashboard. **--> moved to next meeting**
    - Kinematic features: 
        - updates
        - output shapes np.diff (e.g. displacement,distance) vs. np.gradient (e.g. velocity, acceleration)
    - Dunn seminar ([DANNCE](https://www.nature.com/articles/s41592-021-01106-6))

- Deriving bounding boxes annotations from keypoint labels
    - [sleap](https://github.com/talmolab/sleap/blob/60a441fc1d4fc60533ddb0296cab56165cd3e664/sleap/instance.py#L878) has a function like this (computing min/max)
    - start with rectangle (easy to derive ellipse or others from there)
    - why would this be interesting?
        - defining the ROI around an animal can be useful for analysis (in the future we can explore deriving segmentation masks with [SAM](https://segment-anything.com/) or equivalent from the crops?)
        - derive detection datasets from pose estimation ones
    - we suggest dealing with it next term, just after v0.1
    - Converting between DLC and SLEAP formats
        - DLC to SLEAP somewhat flaky (the first frame is identified as the input video?)? Check sleap discussions maybe for help.
- Brandon's update on outlier detection based on confidence
    - checking how xarray works 
        - Niko says learning about xarray is time well spent!
        - good material online
    - what are reasonable default values for confidence outliers?
        - DLC uses 0.4 default for viz, papers usually 0.8 to 0.9
        - decision for default being 0.6 seems alright as starting point (users will be able to define it anyways)
        - neither LP (Lightning pose) nor SLEAP have a recommended threshold
            - SLEAP is not bounded between 0 and 1 and also has a few confidence metrics
        - we chat about the issue of confidence not really being comparable across pose estim packages
            - maybe this is interesting to explore as a blogpost? E.g., how the distribution of confidence values varies for different packages trained on the same data 
    - plan for detecting outliers 
        - start of with confidence values and printout how many % of the points have been removed (we think this would be very useful for users)
        - next based on percentiles, next based on temporal smoothness, next use multiview consistency and pose consistency metrics from Lightning pose
        - after movement v0.1 we can think of a nicer object-oriented structure and an `outlier` class that has different methods for detection
        - going forward: we can implement more outlier detection methods, and find a way to combine them (chatting with Matt Whiteway would be useful for this)
- Niko's update on visualising predictions in napari
    - we can now import movement/csv/sleap files to napari (drag and drop :star:)
    - 2 layers: 
        - points layer: keypoints
        - tracks: adds a tail to each keypoint
    - many options for customising visualisation (color based on different variables, length of tails...)
    - current blockers:
        - napari's handling of nans in tracks layer
        - we have 3 functions for reading files depending on pose estimation package --> we want to have one function that then calls the correct one under the hood
    - next steps
        - display video rather than a static frame (probably for v1)
        - there is a plugin for playing videos, not actively maintained but Niko knows the main developer -- Niko can chat to him and ask him if he'd be happy for us to take over. The plugin reads from opencv into a 3D napari array. In the future: potentially use dask?
- Niko's update on movement package
    - before we had to install pytables from conda-forge, then install movement
    - Will G (ARC) came to the rescue and using `pandas[hdf5]` version did the trick, now it's completely pip-installable
    - working towards getting it in conda-forge: we only need `sleap-io` to be in conda-forge, which only needs one more dependency (`ndxpose`) in conda-forge --- seems feasible and people are keen to collaborate
    - CH: there is another config for `pandas` which references `xarray` - maybe worth checking? Yes, we can explore this.
- CH's update on kinematics
    - added vectorised functions to compute derivatives (veloc and accel) and a separate function for displacement
    - they all output an xarray Dataset with magnitude and direction DataArrays
        - e.g. vel = kinematics.velocity(pos) --> vel.magnitude gives speed; vel.direction gives direction
    - Question: what is the difference between xarray, dataset and data array?
        - data array: a numpy array with strings along axes that we can use for indexing (panda-like)
        - dataset: collection of data arrays, if they share axes (even some of them) xarray aligns them. E.g.: confidence and trajectories are data arrays of the same dataset. So we can use conditionals across them to access the relevant data
    - Is it better to have derivatives in the same dataset along with the trajectories, or to have them in a separate one?
        - for now go for the easiest for the developer 
    - Velocity (or accel) as polar (magnitude and angle) or as cartesian (vx, vy components)?
        - maybe some preference to save vx, vy, and magnitude and angle as an extra data that probably users want (understanding magnitude and angle as somewhat derived from cartesian format)
    - Displacement
        - diff(pos) is defined for n-1 frames, ideally for consistency with vel and other metrics we have n frames
        - we suggest setting the first frame to displacement = 0, rather than nan, since it makes more intuitive sense (at t=0, we have no displacement relative to the initial position).
        
- Conference [senses in motion](https://sensesinmotion.org/)
    - Brandon may present a pitch / concept / roadmap on movement
    - we will continue chatting about it next meeting
    
## 2024-01-24: Chat with Matt Whiteway
- what we do
	- RSEs for SWC
	- subgroup specialised in behaviour
- projects we are working on/have lined up
	- movement
		- thoughts on error correction methods?
		- we could implement some of their spatiotemporal losses (the ones that correlate with error more strongly) for post-hoc anomaly/outliers detection, or for comparing the quality of predictions from various pose estimation networks.
		- maybe the spatiotemporal losses are also interesting for active learning? shameless promo [here](https://deeplabcut.medium.com/exploring-active-learning-with-deeplabcut-an-ai-residents-journey-e441bbd5a71c)
	- a similar package with detection tools
	    - detecting and tracking crabs in the field
    - data management and viz with dashboards
	- video encoding
- questions
    - what is next for him?
    - about lightning pose
        - thoughts about using video streams of compressed videos?
        - anything we can beta-test?
        - anything we could contribute to?
        - thoughts for multi-animal approach? ID tracking? ([roadmap](https://github.com/danbider/lightning-pose/blob/main/docs/roadmap.md))
        - thoughts about unsupervised kpt discovery? (in the paper they mention potentially using unsupervised predicted kpts as labels in the future - cool)
        - thoughts for 3D approach?
        - online inference?
        - thoughts about integrating models of pose dynamics?
        - thoughts on using [FiftyOne](https://docs.voxel51.com/) as a GUI for reviewing predictions?

## 2024-01-12
- In attendance:
    - Niko
    - CH
    - Adam
    - Sofia
    - Brandon
- PR #86, which overhauled the datasets.py module, has now been merged.
- CH briefly updated us on current work towards adding velocity and acceleration to movement (Issue #3).
    - We discussed whether to add movement magnitude and direction to the Dataset as new variables, or to map these to the existing x and y coordinates. We ultimately decided (if I followed correctly) to start by storing these (and other derivatives more broadly) as separate variables for now, and to make a more definitive decision at a later point. Niko proposed that we add an additional variable, "dataset.speed", and to implement a heading direction method in a later PR.
    - After a brief aside about memory constraints, Adam also proposed that we ultimately implement a method that computes derivates such as velocity under the hood when the user calls on e.g. the dataset.velocity variable for the first time.
    - We also agreed to rename the pose_tracks variable to position for clarity.
    - (I'm not sure if I managed to follow everything during this discussion so please feel free to comment here if I've missed something)
- We also discussed ongoing progress on Issue #97, which proposes that we implement functions for dropping position values based on their confidence scores and interpolating over them
    - We agreed to keep functions for dropping/filtering values and interpolation separated.
    - We debated whether to use separate, hard-coded threshold values for different pose estimation tools, or whether to use a single approach that generalizes to all (e.g. one that detects outliers based on percentile). No real conclusion was reached before the end of the meeting, and it was suggested that we continue this discussion in writing (either here on Zulip or under the issue itself on github).
    - Later down the line we may consider implementing a helper function to help users decide on what threshold makes sense.


## 2023-12-15

- In attendance:
    - Niko
    - CH
    - Adam
    - Sofia
    - Brandon
- Welcome Sofia + introductions
- Movement: [abstract for Measuring Behavior conference](https://docs.google.com/document/d/1-joTcRZL-ubyaUbxow3MF609w_KP5yy1zpRNI-4sLX4/edit?usp=sharing)
    - Feedback for figure:
        - separate individuals as 3D blocks with some distance
        - assing small xarray dataset icons to kinematic variables
    - Authorship: poster authorship will include everyone who has contributed by the time of the conference
    - Acknowledge ChatGPT for editing
- Movement: progress on currently open PRs:
    - Hosting and fetching of sample data (Brandon)
        - rename functions to contain "sample"
        - use `source_software` yaml field to choose the appropriate function
    - Importing data from LightningPose
    - Any blockers?
- Movement: next priorities
    - Threshold data based on confidence values (Brandon)
    - Kinematics: motion derivatives (CH implementes, Sofia will provide references)
    - Write a "metaloader" function that can load any pose tracks, by having `source_software` as keyword argument.
- Aeon:
    - Sofia and CH discussed how sparse RFID ground truth data can be used to retro-actively correct for identity switches
    - Future ideas for movement: assist with stitching tracks (Sofia may tackle it after a few months)
- How to structure future behavioural meetings
    - assign a scribe per meeting

## 2023-11-17

- In attendance:
    - Niko
    - Brandon
    - Chang Huan
- Hosting and fetching of [test data from GIN](https://gin.g-node.org/neuroinformatics/movement-test-data)
    - We decided to keep hosting the metadata.yaml file on GIN
    - This can be fetched by pooch and based the file's contained info, we can create the data registry containing video file names and hashes
    - The hash of the metadata file itself will not be checked
    - The goal is to avoid updating the code repo every time we update the data repo
    - Brandon will work on this, making sure to test the behaviour of pooch when either the metadata or the data itself updates on GIN
    - Niko will add Lightning pose data to GIN
    - Niko will also [add sample video frames to GIN](https://github.com/neuroinformatics-unit/movement/issues/38) (one frame per poses dataset for now)
- We discussed the recently merged-PRs, so that we're all up-to-date with the changes
    - [SLEAP read user labels](https://github.com/neuroinformatics-unit/movement/pull/79)
        - user-labeled instances have a NaN point confidence score, keep this in mind for filtering
        - confidences reported by vairous pose estimation packages [are not the same](https://github.com/talmolab/sleap/discussions/1268)
    - [Ability to save multi-animal pose tracks to single-animal files](https://github.com/neuroinformatics-unit/movement/pull/83)
- Next issues to tackle?
    - [Import data from Lightning Pose](https://github.com/neuroinformatics-unit/movement/issues/74), Niko will ask Dhruv if he's happy to take this on
    - Chang Huan will look at [exporting data to SLEAP analysis files](https://github.com/neuroinformatics-unit/movement/issues/46)
- [Measuring behaviour](https://www.measuringbehavior.org/call-for-papers/) conference?
    - We will discuss during the next meeting
- Long term working directions
    - Brandon is happy to work on pose data cleaning/filtering problems, [this issue](https://github.com/neuroinformatics-unit/movement/issues/55) could be a good starting point
    - Niko will focus on the napari frontend in December
    - Chang Huan may tackle converting SLEAP labels into a DeepLabCut project

## 2023-11-03

### Agenda
- Welcome Brandon!
- Niko/Adam - [scivision](https://sci.vision/) meeting update
- Niko - update on collaboration with [AIND](https://alleninstitute.org/division/neural-dynamics/)
- Discuss ongoing PRs
- Next issues to tackle - see [movement project board](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2)
- Discuss Brandon's onboarding and first tasks.

### Meeting minutes
- In attendance:
    - Niko
    - Brandon
    - Adam
    - Chang Huan (CH)
- Welcomed Brandon to the project, made introductions
- Showed [Community](https://movement.neuroinformatics.dev/) section of website to Brandon
- [Scivision](https://sci.vision/) - cool idea and nice people to work with, but not immediately relevant to movement. We may consider it for future behaviour-related projects that involve computer vision models.
- Make [projects board](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2) public :tada:
- Adam suggedted we should publicly share the meeting minutes on our Zulip, Niko will do it.
- Niko gave an update on the ongoing collaboration with the AIND. They have shared some [LightningPose](https://github.com/danbider/lightning-pose) prediction results with us, and we think loading them into movement should be [easy](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2?query=is%3Aopen+sort%3Aupdated-desc&pane=issue&itemId=42799886)
- Ongoing PRs:
    - [Docs Link check](https://github.com/neuroinformatics-unit/movement/pull/80) by CH. This has been reviewed by Niko and we will merge it soon. CH to add some note to the conteributing guide
    - [SLEAP read user labels](https://github.com/neuroinformatics-unit/movement/pull/79) by CH, who gave as a short intro into what it does. Niko to review it next week.
    - [(DRAFT) Save multi-animal data to single-animal DLC files](https://github.com/neuroinformatics-unit/movement/pull/71) by Dhruv. This is a useful feature to have, we will go through some more rounds of review before it's ready to merge.
- Next issues to tackle
    - [Load data from Lightning Pose](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2?query=is%3Aopen+sort%3Aupdated-desc&pane=issue&itemId=42799886) - Niko within November
    - [Start procedure for first conda release?](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2?query=is%3Aopen+sort%3Aupdated-desc&pane=issue&itemId=41677709) - Niko within November
- First things for Brandon TODO:
    - Go through the docs and try to follow tutorials + examples
    - Identify bugs from the user's perspective (stress testing)
    - Read CONTRIBUTING guide and identify unclear sections
    - Maybe tackle [this issue](https://github.com/neuroinformatics-unit/movement/issues/67) if there is time (there is no time constraint on it)


## 2023-10-16

### Agenda
- Review [document](https://hackmd.io/@niksirbi/HJuQgOcWa/edit) movement mission, scope, and roadmap
- Celebrate merging of [PR #63](https://github.com/neuroinformatics-unit/movement/pull/63)
- Discuss [draft PR](https://github.com/neuroinformatics-unit/movement/pull/68) opened by Dhruv
- Next features for Niko and Chang Huan

### Meeting minutes
- Niko and Chang Huan in attendance
- movement Mission Statement: make shorter?
- CH fine with the rest of the document, we did some minor rewordings.
- Maybe define a glossary of terms to link to (with schematics)
- Niko will have a pair-programming session with Drhuv to clarify the PR
- Will movement docs adopt [diataxis](https://diataxis.fr/)?
    - probably yes, but gradually

### Action items
- [ ] Niko plays with mission statement 
- [ ] Niko should update the docs with the mission/scope/roadmap
- [x] Niko opens issue re Glossary 
    - opened [issue #69](https://github.com/neuroinformatics-unit/movement/issues/69)
- [ ] CH takes on [issue #44](https://github.com/orgs/neuroinformatics-unit/projects/5/views/2?query=is%3Aopen+sort%3Aupdated-desc&pane=issue&itemId=39040657)
- [ ] Niko helps Dhruv with [PR](https://github.com/neuroinformatics-unit/movement/pull/68)