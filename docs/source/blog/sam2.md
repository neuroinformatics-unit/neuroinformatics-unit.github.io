:blogpost: true
:date: August 15, 2025
:author: Pille Wetterauer, Jyoti Bhogal
:location: London, UK
:category: Blog
:language: English
:image: 1

(target-sam2)=

# Exploring automatic ways of extracting a pose estimation skeleton for *C. elegans*
*Segmenting C. elegans using SAM-2 and extracting skeletons.*

```{image} /_static/blog_images/sam2/worm-to-skeleton.png
:align: center
:width: 50%
```
<br>

Manually defining the pose skeletons in each video frame can be very tedious. 
Automating this process would make movement analysis a lot faster and easier. Therefore, 
our project at [OSW](https://neuroinformatics.dev/open-software-week/index.html) 
hackday aimed to explore ways of doing exactly that.

## Why worms?
When studying animal behaviour, _Caenorhabditis elegans_ is not the first model 
organism most people think of. However, they are used frequently as a model for 
drug discovery, developmental biology, genetics, and other areas. Changes in the 
behaviour are thereby an important readout, indicating the effectiveness of a drug, 
a developmental defect, or the contribution of a specific gene. The main advantage 
of using _C. elegans_ over mammalian models like mice is the simpleness. This is also 
true for the OSW hackday project described here: what could be easier to skeletonize 
than a worm!

## Segmenting worms with SAM-2
In order to extract pose skeletons, we first need to create segmentation masks, and 
of course this should be automated as well. There are lots of deep learning algorithms 
available for segmentation. Here, we try out 
[Segment Anything Model 2 (SAM-2)](https://github.com/facebookresearch/sam2). This model
can be applied both to images and videos and is designed to segment any object with 
minimal input from the user.

### Installation
Installing SAM-2 was one of the more challenging steps of this project. The installation 
instructions recommend using WSL on Windows. However, since I already had Python on my 
Windows system, I decided to ignore that. SAM-2 requires:
* Python >= 3.10
* Pytorch and TorchVision
* SAM-2 package, that can be cloned from GitHub
* `ffmpeg` for video manipulation

Setting up Pytorch with GPU support on a Windows system can be tricky. Fortunately, 
I had done this before, so the Nvidia drivers and CUDA were already set up and only the 
correct wheel for Pytorch hat to be downloaded. Still, it didn't all work out the first time. 
After some troubleshooting we found the culprit: Pytorch and SAM-2 are both installed 
using `pip`, so you need to make sure `pip` is installed in the respective environment. 
Otherwise, it can come to version conflicts between packages from different environments, 
where `pip` is installed. 

`ffmpeg` is a commandline video manipulation tool, that is recommended in the example 
notebook for SAM-2 for extracting frames. It is integrated in Linux distributions, but 
on Windows it has to be installed separately, outside the python environment. Of course, 
any other video manipulation tool can be used as well.

In the end everything got installed correctly and I could run the notebook on my laptop, 
even thou I kept getting some non-fatal error messages. The bigger problem, however, was the 
performance of my laptop. Despite the GPU, the prediction took several hours, 
so we decided to use Google Colab instead.

### Running the notebook on Google Colab
The SAM-2 repository contains sample notebooks for different use-cases, including video 
segmentation. The notebooks contain a link to Google Colab and code for setting up the 
Colab environment. You just need to choose a runtime with GPU (T4 for a free runtime), 
connect to it and mount Google Drive. The data has to be uploaded to Google Drive.

Google Colab is good for trying out things, however there are usage limits. The 
connection is determined after being inactive for a while and there is a limited number 
of sessions with GPU usage. Google does not publish these limits, apparently they vary. 
There are paid options for longer runtimes and more GPU types.

### SAM-2 workflow for video segmentation

SAM-2 repository provides an example notebook for segmenting videos, which is a good 
starting point for exploring this model. The video predictor is built with pretrained 
weights (need to be downloaded separately when using SAM-2 on a local machine!). The 
video data has to be saved as single frames, the example notebook uses JPEG files. These 
images are loaded into a variable called `ìnference_state`. Then the user should provide 
prompts for the objects that should be segmented. There can be one or more objects and 
the prompts can be either point coordinates or boxes. Furthermore, the prompts have a label,
showing whether the prompt is positive (i.e. marking the desired object) or negative (
marking the background). With this input the first masks for a given frame are predicted, 
as shown below. Here, point prompts are used, 2 positive and one negative for each worm.

```{image} /_static/blog_images/sam2/sam2-workflow.png
:align: center
:width: 100%
```
<br>
The resulting masks are visualized, so the user can decide whether to move on or add more 
prompts for a better result. Due to limited time, the masks here were not refined further.
The next step is to propagate the masks to whole video. Masks for each frame are predicted 
and each object is tracked throughout the video. This is the time-consuming step. A good 
innings to grab a cup of coffee (or a piece of pizza) and have a chat with fellow coders.

```{image} /_static/blog_images/sam2/sam2-propagation.tiff
:align: center
:width: 100%
```
<br>
As a result of the prediction you get masks for every frame in the video. The notebook 
displays some of them, so you can check the quality. All the predicted masks are stored 
is a variable called `video_segments`. Since the masks are numpy arrays, they are not 
serializable and cannot be stored in a JSON file. But you can use `pickle` to store them 
for later use.

The example notebook contains all these steps with different options and extra code cells 
for e.g. adding additional prompts, different kinds of prompts, only one object, etc. 
A more concise notebook, tailored for segmenting _C. elegans_, can be found 
[here](https://github.com/pwetterauer/WormNotebooks.git).

### Limitations
While the results look reasonably good, there are some limitations. First, even in this 
simple example the masks overlap not only the worm, but also some neighbouring pixels. 
Using more points to prompt the model might solve this issue. However, the point coordinates 
have to be entered manually. Finding out the coordinates and typing them into an array is 
not very convenient. There are plugins for FIJI (SAMJ-IJ, only works for images not for 
videos) or napari (e.g. microSAM for microscopic images, supports 2D, 3D and videos), 
that make this step of the workflow easier.
<br>
Second, on a more crowded plate, where the worms touch each other, the model tends to lose 
track of single worms. This is, however a general problem not only for SAM-2 but also other 
segmentation models. This kind of mistakes can be manually corrected or one can avoid them 
by using less crowded videos.
<br><br>
In summary, SAM-2 did a good job segmenting the worms in a short time. The resulting masks 
can now be further analysed, e.g. by creating a skeleton and selecting some markers to create 
a pose track.
