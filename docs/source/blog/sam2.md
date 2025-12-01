:blogpost: true
:date: December 1, 2025
:author: Pille Wetterauer, Jyoti Bhogal
:location: London, UK
:category: Blog
:language: English
:image: 1

(target-sam2)=

# Exploring automatic ways of extracting a pose estimation skeleton for *C. elegans*
*Segmenting C. elegans using SAM-2 and extracting skeletons.*

Manually defining the pose skeletons in each video frame can be very tedious. 
Automating this process would make movement analysis a lot faster and easier. Therefore, 
our project at [OSW](https://neuroinformatics.dev/open-software-week/index.html) 
hackday aimed to explore ways of doing exactly that.

```{figure} /_static/blog_images/sam2/worm-to-skeleton.png
:align: center
:width: 60%

**How to automatically define a pose estimation skeleton on a worm?** We explored this as part of the OSW hackday.
```

## Why worms?
When studying animal behaviour, [_Caenorhabditis elegans_](https://en.wikipedia.org/wiki/Caenorhabditis_elegans) is not the first model 
organism most people think of. However, they are used frequently as a model for 
drug discovery, developmental biology, genetics, and other areas. Changes in their 
behaviour are thereby an important readout, indicating the effectiveness of a drug, 
a developmental defect, or the contribution of a specific gene. The main advantage 
of using _C. elegans_ over mammalian models like mice is their simplicity. This is also 
true for the OSW hackday project described here: what could be easier to skeletonize 
than a worm!

## Segmenting worms with SAM-2
In order to automatically extract pose skeletons, we first need to create segmentation masks, and 
of course this should be automated as well. There are lots of deep learning algorithms 
available for segmentation. Here, we try out 
[Segment Anything Model 2 (SAM-2)](https://github.com/facebookresearch/sam2). This model
can be applied both to images and videos and is designed to segment any object with 
minimal input from the user.

### Installation
Installing SAM-2 was one of the more challenging steps of this project. The installation 
instructions recommend using [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) on Windows. However, since I already had Python on my 
Windows system, I decided to ignore that. SAM-2 requires:
* Python >= 3.10
* Pytorch and TorchVision
* SAM-2 package, that can be cloned from GitHub
* `ffmpeg` for video manipulation

Setting up Pytorch with GPU support on a Windows system can be tricky. Fortunately, 
I had done this before, so the NVIDIA drivers and CUDA were already set up and only the 
correct wheel for Pytorch had to be downloaded. Still, it didn't all work out the first time. 
After some troubleshooting we found the culprit: Pytorch and SAM-2 are both installed 
using `pip`, so you need to make sure `pip` is installed in the respective environment. 
Otherwise, it can come to version conflicts between packages from different environments, 
where `pip` is installed. 

`ffmpeg` is a command line tool for video manipulation, that is recommended in the example 
notebook for SAM-2 for extracting frames. It is integrated in Linux distributions, but 
on Windows it has to be installed separately, outside the Python environment. Of course, 
any other video manipulation tool can be used as well.

In the end everything got installed correctly and I could run the notebook on my laptop, 
even though I kept getting some non-fatal error messages. The bigger problem, however, was the 
performance of my laptop. Despite the GPU, the prediction took several hours, 
so we decided to use Google Colab instead.

### Running the notebook on Google Colab
The SAM-2 repository contains sample notebooks for different use-cases, including video 
segmentation. The notebooks contain a link to Google Colab and code for setting up the 
Colab environment. You just need to choose a runtime with GPU (T4 for a free runtime), 
connect to it and mount Google Drive. The data has to be uploaded to Google Drive.

Google Colab is good for trying out things, however there are usage limits. The 
connection is terminated after being inactive for a while and there is a limited number 
of sessions with GPU usage. Google does not publish these limits, apparently they vary. 
There are paid options for longer runtimes and more GPU types.

### SAM-2 workflow for video segmentation

The SAM-2 repository provides an example notebook for segmenting videos, which is a good 
starting point for exploring this model. The video predictor is provided with pretrained 
weights (which need to be downloaded separately when using SAM-2 on a local machine!). The 
video data has to be saved as single frames, the example notebook uses JPEG files. These 
images are loaded into a variable called `inference_state` during initialization. Then the user should provide 
prompts for the objects that should be segmented. There can be one or more objects and 
the prompts can be either point coordinates or boxes. Furthermore, the prompts have a label,
showing whether the prompt is positive (i.e. marking the desired object) or negative (
marking the background). In this way, the first masks for a given frame are predicted, 
as shown below. We used two positive and one negative point prompt for each worm.

```{figure} /_static/blog_images/sam2/sam2-workflow.png
:align: center
:width: 70%

**Masks definition on the first frame.** The SAM-2 workflow showing the provided prompts for three worms (positive points shown in green, negative points in red) and the initial mask predictions. A selected worm (highlighted with a red bounding box) is shown as a zoomed-in view in the panels on the right.
```

The resulting masks are visualized, so the user can decide whether to move on or add more 
prompts for a better result. Due to limited time, the masks here were not refined further.

The next step is to propagate the masks to the whole video. Masks for each frame are predicted 
and each object labelled in the first frame is tracked throughout the video. This is the time-consuming step. A good 
opportunity to grab a cup of coffee (or a piece of pizza) and have a chat with fellow coders.


```{figure} /_static/blog_images/sam2/sam2-propagation.png
:align: center
:width: 100%

**Propagation of masks to subsequent frames.** Once the masks are defined for the first frame, we can propagate the prompts to get the trajectories of the masks across the full video.
```

As a result of the prediction you get masks for every frame in the video. The notebook 
displays some of them, so you can check the quality. All the predicted masks are stored 
in a variable called `video_segments`. Since the masks are numpy arrays, they are not 
serializable and cannot be stored in a JSON file. But you can use `pickle` to export them 
for later use.

The example notebook in the SAM-2 repository contains all these steps with different options and extra code cells 
for e.g. adding additional prompts, different kinds of prompts, only one object, etc. 
A more concise notebook, tailored for segmenting _C. elegans_, can be found 
[here](https://github.com/pwetterauer/WormNotebooks.git).

### Limitations
While the results look reasonably good, there are some limitations. First, even in this 
simple example the masks overlap not only the worm, but also some neighbouring pixels. 
Using more points to prompt the model might solve this issue. However, the point coordinates 
have to be entered manually. Finding out the coordinates and typing them into an array is 
not very convenient. There are some SAM plugins for FIJI (SAMJ-IJ, only works for images not for 
videos) and napari (e.g. microSAM for microscopic images, supports 2D, 3D and videos), 
that could make this step of the workflow easier.

Second, on a more crowded plate, where the worms touch each other, the model tends to lose 
track of single worms. This is, however a general problem not only for SAM-2 but also other 
segmentation models. This kind of mistakes can be manually corrected or one can avoid them 
by using less crowded videos.

In summary, SAM-2 did a good job segmenting the worms in a short time. The resulting masks 
can now be further analysed, e.g. by creating a skeleton and selecting some markers to create 
a pose track.

## Skeletonisation of the masks

The next step after obtaining segmentation masks is to extract a skeleton from them. For this, we used the 
[`skeletonize` function from the `skimage` library](https://scikit-image.org/docs/stable/auto_examples/edges/plot_skeleton.html). This function takes a masked image as input in the format of a two-dimensional array and returns a skeletonised version of the image.

The process of skeletionsation by using the `skimage` library is an iterative one, with several cycles of removing the outermost pixels of the object until only a one-pixel wide representation of the object remains. The function works by iteratively removing pixels from the boundaries of the object while preserving its connectivity and overall structure. The algorithm continues this process until no more pixels can be removed without breaking the connectivity of the object.

As an example, let's look at the following image of a worm mask and its skeletonised version:

```{figure} /_static/blog_images/sam2/output_skeleton_and_node_images/EGCG5_40_2018_10_19_Mask_masked_and_skeletonised.png
:align: center
:width: 70%

**Masked worm image and its skeletonised version.** The input masked worm image (left) and its one-pixel wide skeletonised version (right).
```

Once we have the skeletonised image, we can define keypoints or nodes along the skeleton to represent the pose of the worm. This can be done by sampling points at regular intervals along the skeleton or by identifying specific features such as bends or junctions in the skeleton. These keypoints could then be used to create a pose track for the worm, which can be further analysed for movement patterns and behaviours. They could also be used to quickly create annotations for a pose estimation model (as long as the keypoints are consistent across the frames).

```{figure} /_static/blog_images/sam2/output_skeleton_and_node_images/EGCG5_40_2018_10_19_Mask_skeleton_and_nodes.png
:align: center
:width: 70%

**Skeletonised worm image with sampled nodes.** Five pixels were randomly sampled along the skeleton to define the nodes.
```

A Python notebook to perform the skeletonisation of the worm masks, extract the nodes from the masks, and visualise the process can be found in this [GitHub repository](https://github.com/jyoti-bhogal/neuroinformatics_osw/tree/main/python_code_skeletonisation_and_node_selection). 

In conclusion, the combination of SAM-2 for segmentation and `skimage` for skeletonisation provides an effective workflow for extracting pose estimation skeletons for _C. elegans_. This automated approach can significantly speed up the analysis of worm behaviour and facilitate further research in this area.
