# Use the SLEAP module on the SWC HPC cluster

```{include} ../../_static/howto/swc-wiki-warning.md
```

```{include} ../../_static/howto/code-blocks-note.md
```

## Abbreviations
| Acronym                                                         | Meaning                                      |
| --------------------------------------------------------------- | -------------------------------------------- |
| [SLEAP](https://sleap.ai/)                                      | Social LEAP Estimates Animal Poses           |
| [SWC](https://www.sainsburywellcome.org/web/)                   | Sainsbury Wellcome Centre                    |
| [HPC](https://en.wikipedia.org/wiki/High-performance_computing) | High Performance Computing                   |
| [IT](https://en.wikipedia.org/wiki/Information_technology)      | Information Technology                       |
| [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface)   | Graphical User Interface                     |
| [SLURM](https://slurm.schedmd.com/)                             | Simple Linux Utility for Resource Management |

## Prerequisites

::: {dropdown} Note on managed Linux desktops
:color: info
:icon: info

The SWC's IT team offers managed desktop computers equipped with a Linux image. These machines are already part of SWC's trusted domain and have direct access to SLURM, the HPC modules, and the SWC filesystem.

If you have access to one of these desktops,
you can skip the pre-requisite steps.
You may simply open a terminal, type `module load SLEAP`,
and start using SLEAP directly, as you would on any local
Linux machine. All SLEAP commands should work as expected,
including `sleap-label` for launching the GUI.

That said, you may still want to offload GPU-intensive tasks to an HPC node (e.g. because the desktop's GPU is not powerful enough or because you need to run many jobs in parallel). In that case, you may
still want to read the sections on [model training](sleap-training)
and [inference](sleap-inference).
:::

(access-to-the-hpc-cluster)=
### Access to the HPC cluster
Verify that you can access HPC gateway node (typing your `<SWC-PASSWORD>` both times when prompted):
```{code-block} console
$ ssh <SWC-USERNAME>@ssh.swc.ucl.ac.uk
$ ssh hpc-gw2
```
To learn more about accessing the HPC via SSH, see the [relevant how-to guide](ssh-cluster-target).

### Access to the SLEAP module
Once you are on the HPC gateway node, SLEAP should be listed among the available modules when you run `module avail`:

```{code-block} console
$ module avail
...
SLEAP/2023-03-13
SLEAP/2023-08-01
SLEAP/2024-08-14
SLEAP/2025-09-30
...
```
- `SLEAP/2023-03-13` corresponds to `SLEAP v.1.2.9`
- `SLEAP/2023-08-01` corresponds to `SLEAP v.1.3.1`
- `SLEAP/2024-08-14` corresponds to `SLEAP v.1.3.3`
- `SLEAP/2025-09-30` corresponds to `SLEAP v.1.3.4`

We recommend always using the latest version, which is the one loaded by default
when you run `module load SLEAP`. If you want to load a specific version,
you can do so by typing the full module name,
including the date e.g. `module load SLEAP/2023-08-01`.

::: {warning}
All SLEAP modules currently available on the HPC are from the
legacy SLEAP<=1.4.1 series (TensorFlow backend).
Thus all links to SLEAP documentation in this guide refer to <https://legacy.sleap.ai/>.

Modules for [SLEAP>=1.5.0](https://docs.sleap.ai/latest/) (PyTorch backend)
will be added in the future.
:::

If a module has been successfully loaded, it will be listed when you run `module list`,
along with other modules it may depend on:

```{code-block} console
$ module list
Currently Loaded Modulefiles:
 1) cuda/11.8   2) SLEAP/2023-08-01
```

If you have troubles with loading the SLEAP module,
see this guide's [Troubleshooting section](#problems-with-the-sleap-module).


### Install SLEAP on your local PC/laptop
While you can delegate the GPU-intensive work to the HPC cluster,
you will need to use the SLEAP GUI for some steps, such as labelling frames.
Thus, you also need to install SLEAP on your local PC/laptop.

We recommend following the official [SLEAP installation guide](https://legacy.sleap.ai/installation.html).
To minimise the risk of issues due to incompatibilities between versions, ensure the version of your local installation of SLEAP matches the one you plan to load in the cluster.

### Mount the SWC filesystem on your local PC/laptop
The rest of this guide assumes that you have mounted the SWC filesystem on your local PC/laptop.
If you have not done so, please follow the relevant instructions on the
[SWC internal wiki](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-SWC-Storage-Platform-Overview-198905992.aspx).

We will also assume that the data you are working with are stored in a `ceph`
directory to which you have access to. In the rest of this guide, we will use the path
`/ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data` which contains a SLEAP project
for test purposes. You should replace this with the path to your own data.

:::{dropdown} Data storage location matters
:color: warning
:icon: alert-fill

The cluster has fast access to data stored on the `ceph` filesystem, so if your
data is stored elsewhere, make sure to transfer it to `ceph` before running the job.
You can use tools such as [`rsync`](https://linux.die.net/man/1/rsync)
to copy data from your local machine to `ceph` via an ssh connection. For example:

```{code-block} console
$ rsync -avz <LOCAL-DIR> <SWC-USERNAME>@ssh.swc.ucl.ac.uk:/ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data
```
:::

(sleap-training)=
## Model training
This will consist of two parts: [preparing a training job](prepare-the-training-job)
(on your local SLEAP installation) and [running a training job](run-the-training-job)
(on the HPC cluster's SLEAP module). Some evaluation metrics for the trained models
can be [viewed via the SLEAP GUI](model-evaluation) on your local SLEAP installation.

(prepare-the-training-job)=
### Prepare the training job
Follow the SLEAP instructions for [Creating a Project](https://legacy.sleap.ai/tutorials/new-project.html)
and [Initial Labelling](https://legacy.sleap.ai/tutorials/initial-labeling.html).
Ensure that the project file (e.g. `labels.v001.slp`) is saved in the mounted SWC filesystem
(as opposed to your local filesystem).

Next, follow the instructions in [Remote Training](https://legacy.sleap.ai/guides/remote.html#remote-training),
i.e. *Predict* -> *Run Training…* -> *Export Training Job Package…*.
- For selecting the right configuration parameters, see [Configuring Models](https://legacy.sleap.ai/guides/choosing-models.html#) and [Troubleshooting Workflows](https://legacy.sleap.ai/guides/troubleshooting-workflows.html)
- Set the *Predict On* parameter to *nothing*. Remote training and inference (prediction) are easiest to run separately on the HPC Cluster. Also unselect *Visualize Predictions During Training* in training settings, if it's enabled by default.
- If you are working with camera view from above or below (as opposed to a side view), set the *Rotation Min Angle* and *Rotation Max Angle* to -180 and 180 respectively in the *Augmentation* section.
- Make sure to save the exported training job package (e.g. `labels.v001.slp.training_job.zip`) in the mounted SWC filesystem, for example, in the same directory as the project file.
- Unzip the training job package. This will create a folder with the same name (minus the `.zip` extension). This folder contains everything needed to run the training job on the HPC cluster.

(run-the-training-job)=
### Run the training job
Login to the HPC cluster as described above.
```{code-block} console
$ ssh <SWC-USERNAME>@ssh.swc.ucl.ac.uk
$ ssh hpc-gw2
```
Navigate to the training job folder (replace with your own path) and list its contents:
```{code-block} console
:emphasize-lines: 12
$ cd /ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data
$ cd labels.v001.slp.training_job
$ ls -1
centered_instance.json
centroid.json
inference-script.sh
jobs.yaml
labels.v001.pkg.slp
labels.v001.slp.predictions.slp
train_slurm.sh
swc-hpc-pose-estimation
train-script.sh
```
There should be a `train-script.sh` file created by SLEAP, which already contains the
commands to run the training. You can see the contents of the file by running `cat train-script.sh`:
```{code-block} bash
:caption: labels.v001.slp.training_job/train-script.sh
:name: train-script-sh
:linenos:
#!/bin/bash
sleap-train centroid.json labels.v001.pkg.slp
sleap-train centered_instance.json labels.v001.pkg.slp
```
The precise commands will depend on the model configuration you chose in SLEAP.
Here we see two separate training calls, one for the 'centroid' and another for
the 'centered_instance' model. That's because in this example we have chosen
the ['Top-Down'](https://legacy.sleap.ai/tutorials/initial-training.html#training-options)
configuration, which consists of two neural networks - the first for isolating
the animal instances (by finding their centroids) and the second for predicting
all the body parts per instance.

![Top-Down model configuration](https://legacy.sleap.ai/_images/topdown_approach.jpg)

:::{dropdown} More on 'Top-Down' vs 'Bottom-Up' models
:color: info
:icon: info

Although the 'Top-Down' configuration was designed with multiple animals in mind,
it can also be used for single-animal videos. It makes sense to use it for videos
where the animal occupies a relatively small portion of the frame - see
[Troubleshooting Workflows](https://legacy.sleap.ai/guides/troubleshooting-workflows.html) for more info.
:::

Next you need to create a SLURM batch script, which will schedule the training job
on the HPC cluster. Create a new file called `train_slurm.sh`
(you can do this in the terminal with `nano`/`vim` or in a text editor of
your choice on your local PC/laptop). Here we create the script in the same folder
as the training job, but you can save it anywhere you want, or even keep track of it with `git`.

```{code-block} console
$ nano train_slurm.sh
```

An example is provided below, followed by explanations.
```{code-block} bash
:caption: train_slurm.sh
:name: train-slurm-sh
:linenos:
#!/bin/bash

#SBATCH -J slp_train # job name
#SBATCH -p gpu # partition (queue)
#SBATCH -N 1   # number of nodes
#SBATCH --mem 32G # memory pool for all cores
#SBATCH -n 8 # number of cores
#SBATCH -t 0-06:00 # time (D-HH:MM)
#SBATCH --gres gpu:1 # request 1 GPU (of any kind)
#SBATCH -o slurm.%x.%N.%j.out # STDOUT
#SBATCH -e slurm.%x.%N.%j.err # STDERR
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@domain.com

# Print GPU info
nvidia-smi

# Load the SLEAP module
module load SLEAP

# Define directories for SLEAP project and exported training job
SLP_DIR=/ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data
SLP_JOB_NAME=labels.v001.slp.training_job
SLP_JOB_DIR=$SLP_DIR/$SLP_JOB_NAME

# Go to the job directory
cd $SLP_JOB_DIR

# Run the training script generated by SLEAP
./train-script.sh
```

In `nano`, you can save the file by pressing `Ctrl+O` and exit by pressing `Ctrl+X`.

:::{dropdown} Explanation of the batch script
:color: info
:icon: info
- The `#SBATCH` lines are SLURM directives. They specify the resources needed
for the job, such as the number of nodes, CPUs, memory, etc.
A primer on the most useful SLURM arguments is provided in this [how-to guide](slurm-arguments-target).
For more information  see the [SLURM documentation](https://slurm.schedmd.com/sbatch.html).

- The `#` lines are comments. They are not executed by SLURM, but they are useful
for explaining the script to your future self and others.

- The `nvidia-smi` line prints some information about the GPU(s) available on the node, including their driver version and memory usage. This is useful for debugging purposes.

- The `module load SLEAP` line loads the latest SLEAP module and any other modules
it may depend on.

- The `cd` line changes the working directory to the training job folder.
This is necessary because the `train-script.sh` file contains relative paths
to the  model configuration and the project file.

- The `./train-script.sh` line runs the training job (executes the contained commands).
:::

:::{warning}
Before submitting the job, ensure that you have permissions to execute
both the batch script and the training script generated by SLEAP.
You can make these files executable by running in the terminal:

```{code-block} console
$ chmod +x train-script.sh
$ chmod +x train_slurm.sh
```

If the scripts are not in your working directory, you will need to specify their full paths:

```{code-block} console
$ chmod +x /path/to/train-script.sh
$ chmod +x /path/to/train_slurm.sh
```
:::

Now you can submit the batch script via running the following command
(in the same directory as the script):
```{code-block} console
$ sbatch train_slurm.sh
Submitted batch job 3445652
```

You may monitor the progress of the job in various ways:

::::{tab-set}

:::{tab-item} squeue

View the status of the queued/running jobs with [`squeue`](https://slurm.schedmd.com/squeue.html):

```{code-block} console
$ squeue --me
JOBID    PARTITION  NAME     USER      ST  TIME   NODES  NODELIST(REASON)
3445652  gpu        slp_train sirmpila  R   23:11  1      gpu-sr670-20
```
:::

:::{tab-item} sacct

View status of running/completed jobs with [`sacct`](https://slurm.schedmd.com/sacct.html):

```{code-block} console
$ sacct
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
3445652      slp_train        gpu     swc-ac          2  COMPLETED      0:0
3445652.bat+      batch                swc-ac          2  COMPLETED      0:0
```
Run `sacct` with some more helpful arguments.
For example, you can view jobs from the last 24 hours, displaying the time
elapsed and the peak memory usage in KB (MaxRSS):

```{code-block} console
$ sacct \
  --starttime $(date -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --endtime $(date +%Y-%m-%dT%H:%M:%S) \
  --format=JobID,JobName,Partition,State,Start,Elapsed,MaxRSS

JobID           JobName  Partition      State               Start    Elapsed     MaxRSS
------------ ---------- ---------- ---------- ------------------- ---------- ----------
4043595       slp_infer        gpu     FAILED 2023-10-10T18:14:31   00:00:35
4043595.bat+      batch                FAILED 2023-10-10T18:14:31   00:00:35    271104K
4043603       slp_infer        gpu     FAILED 2023-10-10T18:27:32   00:01:37
4043603.bat+      batch                FAILED 2023-10-10T18:27:32   00:01:37    423476K
4043611       slp_infer        gpu    PENDING             Unknown   00:00:00
```
:::

:::{tab-item} view the logs

View the contents of standard output and error
(the node name and job ID will differ in each case):
```{code-block} console
$ cat slurm.gpu-sr670-20.3445652.out
$ cat slurm.gpu-sr670-20.3445652.err
```
:::

::::

```{dropdown} Out-of-memory (OOM) errors
:color: warning
:icon: alert-fill

If you encounter out-of-memory errors, keep in mind that there two main sources of memory usage:
- CPU memory (RAM), specified via the `--mem` argument in the SLURM batch script. This is the memory used by the Python process running the training job and is shared among all the CPU cores.
- GPU memory, this is the memory used by the GPU card(s) and depends on the GPU card type you requested via the `--gres gpu:1` argument in the SLURM batch script. To increase it, you can request a specific GPU card type with more GPU memory (e.g. `--gres gpu:a4500:1`). The SWC wiki provides a [list of all GPU card types and their specifications](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-CPU-and-GPU-Platform-architecture-165449857.aspx).
- If requesting more memory doesn't help, you can try reducing the size of your SLEAP models. You may tweak the model backbone architecture, or play with *Input scaling*, *Max stride* and *Batch size*. See SLEAP's [documentation](https://legacy.sleap.ai/) and [discussion forum](https://github.com/talmolab/sleap/discussions) for more details.
```

(model-evaluation)=
## Model evaluation
Upon successful completion of the training job, a `models` folder will have
been created in the training job directory. It contains one subfolder per
training run (by default prefixed with the date and time of the run).

```{code-block} console
$ cd /ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data
$ cd labels.v001.slp.training_job
$ cd models
$ ls -1
230509_141357.centered_instance
230509_141357.centroid
```

Each subfolder holds the trained model files (e.g. `best_model.h5`),
their configurations (`training_config.json`) and some evaluation metrics.

```{code-block} console
$ cd 230509_141357.centered_instance
$ ls -1
best_model.h5
initial_config.json
labels_gt.train.slp
labels_gt.val.slp
labels_pr.train.slp
labels_pr.val.slp
metrics.train.npz
metrics.val.npz
training_config.json
training_log.csv
```
The SLEAP GUI on your local machine can be used to quickly evaluate the trained models.

- Select *Predict* -> *Evaluation Metrics for Trained Models...*
- Click on *Add Trained Models(s)* and select the folder containing the model(s) you want to evaluate.
- You can view the basic metrics on the shown table or you can also view a more detailed report (including plots) by clicking *View Metrics*.

For more detailed evaluation metrics, you can refer to [SLEAP's model evaluation notebook](https://legacy.sleap.ai/notebooks/Model_evaluation.html).

(sleap-inference)=
## Model inference
By inference, we mean using a trained model to predict the labels on new frames/videos.
SLEAP provides the [`sleap-track`](https://legacy.sleap.ai/guides/cli.html?#inference-and-tracking) command line utility for running inference
on a single video or a folder of videos.

Below is an example SLURM batch script that contains a `sleap-track` call.
```{code-block} bash
:caption: infer_slurm.sh
:name: infer-slurm-sh
:linenos:
#!/bin/bash

#SBATCH -J slp_infer # job name
#SBATCH -p gpu # partition
#SBATCH -N 1   # number of nodes
#SBATCH --mem 64G # memory pool for all cores
#SBATCH -n 16 # number of cores
#SBATCH -t 0-02:00 # time (D-HH:MM)
#SBATCH --gres gpu:rtx5000:1 # request 1 GPU (of a specific kind)
#SBATCH -o slurm.%x.%N.%j.out # write STDOUT
#SBATCH -e slurm.%x.%N.%j.err # write STDERR
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@domain.com

# Print GPU info
nvidia-smi

# Load the SLEAP module
module load SLEAP

# Define directories for SLEAP project and exported training job
SLP_DIR=/ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data
VIDEO_DIR=$SLP_DIR/videos
SLP_JOB_NAME=labels.v001.slp.training_job
SLP_JOB_DIR=$SLP_DIR/$SLP_JOB_NAME

# Go to the job directory
cd $SLP_JOB_DIR
# Make a directory to store the predictions
mkdir -p predictions

# Run the inference command
sleap-track $VIDEO_DIR/M708149_EPM_20200317_165049331-converted.mp4 \
    -m $SLP_JOB_DIR/models/231010_164307.centroid/training_config.json \
    -m $SLP_JOB_DIR/models/231010_164307.centered_instance/training_config.json \
    --gpu auto \
    --tracking.tracker simple \
    --tracking.similarity centroid \
    --tracking.post_connect_single_breaks 1 \
    -o predictions/labels.v001.slp.predictions.slp \
    --verbosity json \
    --no-empty-frames
```
The script is very similar to the training script, with the following differences:
- The time limit `-t` is set lower, since inference is normally faster than training. This will however depend on the size of the video and the number of models used.
- The requested number of cores `n` and memory `--mem` are higher. This will depend on the requirements of the specific job you are running. It's best practice to try with a scaled-down version of your data first, to get an idea of the resources needed.
- The requested GPU is of a specific kind (RTX 5000). This will again depend on the requirements of your job, as the different GPU kinds vary in GPU memory size and compute capabilities (see [the SWC wiki](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-CPU-and-GPU-Platform-architecture-165449857.aspx)).
- The `./train-script.sh` line is replaced by the `sleap-track` command.
- The `\` character is used to split the long `sleap-track` command into multiple lines for readability. It is not necessary if the command is written on a single line.

::: {dropdown} Explanation of the sleap-track arguments
:color: info
:icon: info

 Some important command line arguments are explained below.
 You can view a full list of the available arguments by running `sleap-track --help`.
- The first argument is the path to the video file to be processed.
- The `-m` option is used to specify the path to the model configuration file(s) to be used for inference. In this example we use the two models that were trained above.
- The `--gpu` option is used to specify the GPU to be used for inference. The `auto` value will automatically select the GPU with the highest percentage of available memory (of the GPUs that are available on the machine/node)
- The options starting with `--tracking` specify parameters used for tracking the detected instances (animals) across frames. See SLEAP's guide on [tracking methods](https://legacy.sleap.ai/guides/proofreading.html#tracking-method-details) for more info.
- The `-o` option is used to specify the path to the output file containing the predictions.
- The above script will predict all the frames in the video. You may select specific frames via the `--frames` option. For example: `--frames 1-50` or `--frames 1,3,5,7,9`.
:::

::: {dropdown} RGB-to-Grayscale conversion errors during inference
:color: warning
:icon: alert-fill

If you encounter errors related to [RGB-to-Grayscale conversion](https://github.com/talmolab/sleap/issues/638), you may circumvent them by adding the `--batch_size 1` option to `sleap-track` or by running inference on a CPU node (change `-p gpu` to `-p cpu` and remove the `--gres gpu:rtx5000:1` option). That said, both workarounds will make inference slower.
:::

You can submit and monitor the inference job in the same way as the training job.
```{code-block} console
$ sbatch infer_slurm.sh
$ squeue --me
```
Upon completion, a `labels.v001.slp.predictions.slp` file will have been created in the job directory.

You can use the SLEAP GUI on your local machine to load and view the predictions:
*File* -> *Open Project...* -> select the `labels.v001.slp.predictions.slp` file.

## The training-inference cycle
Now that you have some predictions, you can keep improving your models by repeating
the training-inference cycle. The basic steps are:
- Manually correct some of the predictions: see [Prediction-assisted labeling](https://legacy.sleap.ai/tutorials/assisted-labeling.html)
- Merge corrected labels into the initial training set: see [Merging guide](https://legacy.sleap.ai/guides/merging.html)
- Save the merged training set as `labels.v002.slp`
- Export a new training job `labels.v002.slp.training_job` (you may reuse the training configurations from `v001`)
- Repeat the training-inference cycle until satisfied

## Troubleshooting

### Problems with the SLEAP module

In this section, we will describe how to test that the SLEAP module is loaded
correctly for you and that it can use the available GPUs.

Login to the HPC cluster as described [above](access-to-the-hpc-cluster).

Start an interactive job on a GPU node. This step is necessary, because we need
to test the module's access to the GPU.
```{code-block} console
$ srun -p gpu --gres=gpu:1 --pty bash -i
```
:::{dropdown} Explain the above command
:color: info
:icon: info

* `-p gpu` requests a node from the 'gpu' partition (queue)
* `--gres=gpu:1` requests 1 GPU of any kind
*  `--pty` is short for 'pseudo-terminal'
*  The `-i` stands for 'interactive'

Taken together, the above command will start an interactive bash terminal session
on a node of the 'gpu' partition, equipped with 1 GPU card.
:::

First, let's verify that you are indeed on a node equipped with a functional
GPU, by typing `nvidia-smi`:
```{code-block} console
$ nvidia-smi
Wed Sep 27 10:34:35 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.125.06   Driver Version: 525.125.06   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:41:00.0 Off |                  N/A |
|  0%   42C    P8    22W / 240W |      1MiB /  8192MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
Your output should look similar to the above. You will be able to see the GPU
name, temperature, memory usage, etc. If you see an error message instead,
(even though you are on a GPU node) please contact the SWC Scientific Computing team.

Next, load the SLEAP module.
```{code-block} console
$ module load SLEAP
Loading SLEAP/2024-08-14
  Loading requirement: cuda/11.8
```

To verify that the module was loaded successfully:
```{code-block} console
$ module list
Currently Loaded Modulefiles:
 1) SLEAP/2024-08-14
```
You can essentially think of the module as a centrally installed conda environment.
When it is loaded, you should be using a particular Python executable.
You can verify this by running:

```{code-block} console
$ which python
/ceph/apps/ubuntu-20/packages/SLEAP/2024-08-14/bin/python
```

Finally we will verify that the `sleap` python package can be imported and can
'see' the GPU. We will mostly just follow the
[relevant SLEAP instructions](https://legacy.sleap.ai/installation.html#testing-that-things-are-working).
First, start a Python interpreter:
```{code-block} console
$ python
```
Next, run the following Python commands:

::: {warning}
The `import sleap` command may take some time to run (more than a minute).
This is normal. Subsequent imports should be faster.
:::

```{code-block} pycon
>>> import sleap

>>> sleap.versions()
SLEAP: 1.3.3
TensorFlow: 2.8.4
Numpy: 1.21.6
Python: 3.7.12
OS: Linux-5.4.0-109-generic-x86_64-with-debian-bullseye-sid

>>> sleap.system_summary()
GPUs: 1/1 available
  Device: /physical_device:GPU:0
         Available: True
        Initialized: False
     Memory growth: None

>>> import tensorflow as tf

>>> print(tf.config.list_physical_devices('GPU'))
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]

>>> tf.constant("Hello world!")
<tf.Tensor: shape=(), dtype=string, numpy=b'Hello world!'>
```

If all is as expected, you can exit the Python interpreter, and then exit the GPU node
```{code-block} pycon
>>> exit()
```
```{code-block} console
$ exit()
```
If you encounter troubles with using the SLEAP module, contact
Niko Sirmpilatze of the SWC [Neuroinformatics Unit](https://neuroinformatics.dev/).

To completely exit the HPC cluster, you will need to type `exit` or
`logout` until you are back to the terminal prompt of your local machine.
See [Set up SSH for the SWC HPC cluster](../programming/SSH-SWC-cluster.md)
for more information.
