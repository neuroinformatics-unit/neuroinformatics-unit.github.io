# Use SLEAP on the SWC HPC cluster

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

SWC's IT team offers managed Linux desktops with direct access to SLURM, the HPC modules, and the SWC filesystem. If you have one, you can skip the prerequisite steps: open a terminal, run `module load SLEAP`, and use SLEAP directly (including `sleap label` for the GUI).

You may still want to offload GPU-intensive work to an HPC node (e.g. for more powerful GPUs or parallel jobs). In that case, read the sections on [model training](sleap-training) and [inference](sleap-inference).
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
Once you are on the HPC gateway node, you can list the available SLEAP modules:

```{code-block} console
$ module avail SLEAP
----------------------- /ceph/apps/ubuntu-24/modulefiles-----------------------
   ...  SLEAP/2025-09-30    SLEAP/2026-05-08 (D)

  Where:
   D:  Default Module
...
```
- `SLEAP/2026-05-08` corresponds to [SLEAP v1.6.3](https://docs.sleap.ai/v1.6.3/) (PyTorch backend) — this is the recommended module for all new projects, and what this guide documents.
- Older modules use the [legacy TensorFlow backend](https://legacy.sleap.ai/). Use these only if you need compatibility with an existing project.
- Modules dated before `2025-09-30` were built for an older Ubuntu base and are no longer recommended.

To load the recommended PyTorch-based version (the default):
```{code-block} console
$ module load SLEAP
```

To load an older TensorFlow-based version (e.g. `SLEAP/2025-09-30`, which is SLEAP v1.3.4), specify its full name:
```{code-block} console
$ module load SLEAP/2025-09-30
```

To view the modules that are currently loaded:

```{code-block} console
$ module list
Currently Loaded Modules:
...   15) SLEAP/2026-05-08
```

If you have troubles with loading the SLEAP module,
see the [](troubleshooting) section.


### Install SLEAP on your local PC/laptop
While you can delegate the GPU-intensive work to the HPC cluster,
you will need to use the SLEAP GUI for some steps, such as labelling frames.
Thus, you also need to install SLEAP on your local PC/laptop.

We recommend following the official [SLEAP installation guide](https://docs.sleap.ai/latest/installation/).
To avoid compatibility issues, make sure your local SLEAP version matches the module you plan to use on the cluster.
The guide also includes a [version compatibility table](https://docs.sleap.ai/latest/installation/#version-compatibility) showing which versions of `sleap`, `sleap-io`, and `sleap-nn` belong together—use this when installing a specific version or updating pinned packages.

For example, to match the current default module (`SLEAP/2026-05-08`, SLEAP v1.6.3), you can install the corresponding versions locally with:

```{code-block} console
uv tool install --python 3.13 "sleap[nn]==1.6.3" --with "sleap-io==0.7.0" --with "sleap-nn==0.2.0" --torch-backend auto
```

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
Follow the [SLEAP tutorial](https://docs.sleap.ai/latest/tutorial/overview/) till
the end of the section on [Initial Labelling](https://docs.sleap.ai/latest/tutorial/initial-labeling/).
Ensure that the project file (e.g. `labels.v002.slp`) is saved in the mounted SWC filesystem
(as opposed to your local filesystem).

Next, read the [Training a model](https://docs.sleap.ai/latest/tutorial/training-a-model/) section
of the tutorial, but **do not hit the `Run` button** in the SLEAP GUI just yet
(that would run the training job on your local machine, which is not what we want).
Instead, follow the instructions in the [Running SLEAP remotely](https://docs.sleap.ai/latest/guides/running-sleap-remotely/) guide,
i.e. *Predict* -> *Run Training…* -> *Export Training Job Package…*.

- For selecting the right configuration parameters, see the [Model Configuration](https://nn.sleap.ai/latest/reference/models/) guide.
- Set the *Inference Target* parameter to *Nothing*. Remote training and inference (prediction) are easiest to run separately on the HPC Cluster.
- Make sure to save the exported training job package (e.g. `labels.v002.slp.training_job.zip`) in the mounted SWC filesystem, for example, in the same directory as the project file.
- Unzip the training job package. This will create a folder with the same name (minus the `.zip` extension). This folder contains everything needed to run the training job on the HPC cluster: YAML configuration files and a packaged labels file (`.pkg.slp`).

(run-the-training-job)=
### Run the training job
Login to the HPC cluster as described above.
```{code-block} console
$ ssh <SWC-USERNAME>@ssh.swc.ucl.ac.uk
$ ssh hpc-gw2
```
Navigate to the training job folder (replace with your own path) and list its contents:
```{code-block} console
$ cd /ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data
$ cd labels.v002.slp.training_job
$ ls -1
centered_instance.yaml
centroid.yaml
inference-script.sh
jobs.yaml
labels.v002.pkg.slp
train-script.sh
```

The YAML configuration files specify the model architecture, training hyperparameters,
and data pipeline settings for each model. You can inspect them with
`cat centroid.yaml` or open them in a text editor.

The precise files will depend on the model configuration you chose in SLEAP.
Here we see two config files, one for the 'centroid' and another for
the 'centered_instance' model. That's because in this example we have chosen
the ['Top-Down](https://nn.sleap.ai/latest/reference/models/#top-down)' configuration, which consists of two neural networks - the first
for isolating the animal instances (by finding their centroids) and the second
for predicting all the body parts per instance.

![Top-Down model configuration](https://nn.sleap.ai/latest/assets/images/topdown_approach.jpg)

:::{dropdown} More on 'Top-Down' vs 'Bottom-Up' models
:color: info
:icon: info

Although the 'Top-Down' configuration was designed with multiple animals in mind,
it can also be used for single-animal videos,
where the animal occupies a relatively small portion of the frame - see
[Model Configuration](https://nn.sleap.ai/latest/reference/models/) for more info.
:::

SLEAP also generates a `train-script.sh` file in the training job folder.
You can inspect it with `cat train-script.sh` to see the training commands it contains.
These are useful as a reference, but be cautious about copying them verbatim.
They may point to folders on the machine that exported the training package,
rather than on the cluster. They may also include a `trainer_config.run_name=...`
setting whose value contains an `=` sign. This makes SLEAP stop with an error like
`mismatched input '=' expecting`. Instead, we'll write the `sleap train` commands from
scratch in the next step, letting SLEAP name each training run automatically.

Next you need to create a SLURM batch script, which will schedule the training job
on the HPC cluster. Create a new file called `train-slurm.sh` inside the training job
folder (the same folder that holds the config files), because the training commands
below use paths relative to that folder. You can create it in the terminal with
`nano`/`vim`, or write it in a text editor on your local machine and copy it in.

```{code-block} console
$ nano train-slurm.sh
```

An example is provided below, followed by explanations.
```{code-block} bash
:linenos:
#!/bin/bash

#SBATCH -J slp_train # job name
#SBATCH -p gpu # partition (queue)
#SBATCH -N 1   # number of nodes
#SBATCH --mem 32G # memory pool for all cores
#SBATCH --ntasks-per-node=1 # one process per node
#SBATCH --cpus-per-task=8   # CPU cores available to the process
#SBATCH -t 0-06:00 # time (D-HH:MM)
#SBATCH --gres gpu:a100:1 # request 1 GPU of a given type (see dropdown below)
#SBATCH -o slurm.%x.%N.%j.out # STDOUT
#SBATCH -e slurm.%x.%N.%j.err # STDERR
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@domain.com

# Print GPU info
nvidia-smi

# Load the SLEAP module
module load SLEAP

# Run the training for each model
sleap train --config-name centroid.yaml --config-dir . trainer_config.ckpt_dir='models'
sleap train --config-name centered_instance.yaml --config-dir . trainer_config.ckpt_dir='models'
```

:::{dropdown} Explanation of the batch script
:color: info
:icon: info
- `#SBATCH` lines are SLURM directives specifying the resources needed for the job.
  See our [SLURM primer](slurm-arguments-target) and the [SLURM documentation](https://slurm.schedmd.com/sbatch.html) for details.

- `--ntasks-per-node=1` tells SLURM to launch one process per node. PyTorch Lightning
  (which SLEAP uses internally) requires this form rather than `--ntasks` or `-n`;
  Lightning then manages GPU parallelism within that single process.
  `--cpus-per-task=8` allocates CPU cores to that process for data loading and preprocessing.

- `--gres gpu:a100:1` requests 1 GPU of type A100. To request any available GPU, use `--gres gpu:1`.
  Inspect available GPU types by listing the nodes in the `gpu` and `gpu_lowp` partitions:
    ```{code-block} console
    $ sinfo -p gpu,gpu_lowp -o "%N %G" --noheader
    ```
    Look for the string between `gpu:` and the next `:` (e.g. `a100`, `l40s`).
    Avoid GPUs with CUDA compute capability below 7.5 (unsupported by PyTorch ≥ 2.5);
    at the time of writing, only `p5000` cards are incompatible.
    See the [SWC wiki](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-CPU-and-GPU-Platform-architecture-165449857.aspx)
    and the [NVIDIA CUDA GPUs page](https://developer.nvidia.com/cuda/gpus) for compute capabilities.

- `module load SLEAP` loads the latest SLEAP module and its dependencies.
  PyTorch bundles its own CUDA runtime, so no separate `cuda` module is needed.

- `--config-dir .` and `trainer_config.ckpt_dir='models'` use paths relative to the
  training job folder, so submit the script from within that folder (see below).

- Each `sleap train` call trains one model: `--config-name` selects the YAML file,
  `--config-dir .` points to the current folder containing it, and
  `trainer_config.ckpt_dir='models'` saves the trained model into a `models/`
  subfolder of the training job folder.
:::

Using a legacy (TensorFlow) module instead? See [Legacy (TensorFlow) modules](legacy-modules) for the equivalent training commands.

Now submit the batch script from within the training job folder, so that the
relative paths in the script resolve correctly:
```{code-block} console
$ cd /ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data/labels.v002.slp.training_job
$ sbatch train-slurm.sh
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

If you encounter out-of-memory errors, keep in mind that there are two main sources of memory usage:
- CPU memory (RAM), specified via the `--mem` argument in the SLURM batch script. This is the memory used by the Python process running the training job and is shared among all the CPU cores.
- GPU memory, this is the memory used by the GPU card(s) and depends on the GPU card type you requested via the `--gres gpu:1` argument in the SLURM batch script. To increase it, you can request a specific GPU card type with more GPU memory (e.g. `--gres gpu:a100:1`). The SWC wiki provides a [list of all GPU card types and their specifications](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-CPU-and-GPU-Platform-architecture-165449857.aspx).
- If requesting more memory doesn't help, you can try reducing the size of your SLEAP models. You may tweak the model backbone architecture, or play with *Input scaling*, *Max stride* and *Batch size*. See SLEAP's [documentation](https://docs.sleap.ai/) and [discussion forum](https://github.com/talmolab/sleap/discussions) for more details.
```

(model-evaluation)=
## Model evaluation
Upon successful completion of the training job, a `models` folder will have
been created inside the training job folder (as set by `trainer_config.ckpt_dir='models'`).
It contains one subfolder per training run.

```{code-block} console
$ cd /ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data/labels.v002.slp.training_job
$ cd models
$ ls -1
'260512_151547.centroid.n=46'
'260512_151547.centered_instance.n=46'
```

Each subfolder holds the trained model files (e.g. `best.ckpt`),
their configurations (`training_config.yaml`) and some evaluation metrics.

```{code-block} console
$ cd '260512_151547.centroid.n=46'
$ ls -1
best.ckpt
initial_config.yaml
labels_gt.train.0.slp
labels_gt.val.0.slp
labels_pr.train.0.slp
labels_pr.val.0.slp
metrics.train.0.npz
metrics.val.0.npz
training_config.yaml
training_log.csv
```
The SLEAP GUI on your local machine can be used to quickly evaluate the trained models.

- Select *Predict* -> *Evaluation Metrics for Trained Models...*
- Click on *Add Trained Models(s)* and select the folder containing the model(s) you want to evaluate.
- You can view the basic metrics on the shown table or you can also view a more detailed report (including plots) by clicking *View Metrics*.

For more detailed evaluation metrics, you can refer to [SLEAP's model evaluation notebook](https://docs.sleap.ai/latest/notebooks/Model_evaluation/).

(sleap-inference)=
## Model inference
By inference, we mean using a trained model to predict the labels on new frames/videos.
SLEAP provides the `sleap track` command line utility for running inference
on a single video or a folder of videos.
See the [remote inference guide](https://docs.sleap.ai/latest/guides/running-sleap-remotely/#remote-inference) for more details.

Create a new file called `infer-slurm.sh`. Because this script uses absolute paths
(see below), you can keep it anywhere you like.

```{code-block} console
$ nano infer-slurm.sh
```

An example is provided below.
```{code-block} bash
:linenos:
#!/bin/bash

#SBATCH -J slp_infer # job name
#SBATCH -p gpu # partition
#SBATCH -N 1   # number of nodes
#SBATCH --mem 64G # memory pool for all cores
#SBATCH --ntasks-per-node=1 # one process per node
#SBATCH --cpus-per-task=16  # CPU cores available to the process
#SBATCH -t 0-02:00 # time (D-HH:MM)
#SBATCH --gres gpu:a100:1 # request 1 GPU of a given type
#SBATCH -o slurm.%x.%N.%j.out # write STDOUT
#SBATCH -e slurm.%x.%N.%j.err # write STDERR
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@domain.com

# Print GPU info
nvidia-smi

# Load the SLEAP module
module load SLEAP

# Define directory for SLEAP project
SLP_DIR=/ceph/scratch/neuroinformatics-dropoff/SLEAP_HPC_test_data

# Make a directory to store the predictions (if it doesn't exist already)
mkdir -p $SLP_DIR/predictions

# Run the inference command
sleap track \
    -i $SLP_DIR/mice.mp4 \
    -m $SLP_DIR/labels.v002.slp.training_job/models/260512_151547.centroid.n=46 \
    -m $SLP_DIR/labels.v002.slp.training_job/models/260512_151547.centered_instance.n=46 \
    -d auto \
    -b 4 \
    --tracking \
    -o $SLP_DIR/predictions/labels.v002.predictions.slp
```
The script mirrors the training one, with a few differences:
- `--cpus-per-task` and `--mem` are higher; tune these to your specific job, ideally after a scaled-down trial run.
- The time limit `-t` is lower, since inference is typically faster than training (depends on video length and number of models).
- `sleap train` is replaced by a single `sleap track` call (split across lines with `\` for readability).
- Paths are absolute (built from `$SLP_DIR`) rather than relative to the training job folder.

In the `sleap track` call, `-i` is the input video to run inference on (replace this
with the path to your own video), each `-m` points to a trained model from the training
step, and `-o` is the output file where the predictions will be saved.

Using a legacy (TensorFlow) module instead? See [Legacy (TensorFlow) modules](legacy-modules) for the equivalent inference commands.

You can submit and monitor the inference job in the same way as the training job.
```{code-block} console
$ sbatch infer-slurm.sh
$ squeue --me
```
Upon completion, a `labels.v002.predictions.slp` file will have been created in the `predictions` directory.

You can use the SLEAP GUI on your local machine to load and view the predictions:
*File* -> *Open Project...* -> select the `labels.v002.predictions.slp` file.

:::{note}
The SLEAP CLI commands `sleap train` and `sleap track` are aliases for
`sleap-nn train` and `sleap-nn track` respectively; the two forms work
interchangeably. For a full list of arguments, run `<command> --help`
(with the SLEAP module loaded) or consult the SLEAP-NN documentation on
[training](https://nn.sleap.ai/latest/guides/training/),
[inference](https://nn.sleap.ai/latest/guides/inference/) and
[tracking](https://nn.sleap.ai/latest/guides/tracking/).
:::


## The training-inference cycle

Now that you have some predictions, you can keep improving your models by repeating
the training-inference cycle.

This predictions file has the same format as a standard SLEAP project file,
and you can use the GUI (on your local machine) to manually correct the predictions
or merge them into an existing SLEAP project.

For example, you can:

- [Manually correct](https://docs.sleap.ai/latest/tutorial/correcting-predictions/) some of the predictions
- Merge corrected labels into the initial training set (*File* -> *Merge into Project...*).
- Save the merged training set under a new name, e.g. `labels.v003.slp`
- Export a new training job `labels.v003.slp.training_job` (you may reuse the training configurations from before)
- Repeat the training-inference cycle until satisfied

(troubleshooting)=
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
* `--gres=gpu:1` requests 1 GPU of any kind. Use `--gres=gpu:<type>:1` to request a specific GPU type (e.g. `--gres=gpu:a100:1`).
*  `--pty` is short for 'pseudo-terminal'
*  The `-i` stands for 'interactive'

Taken together, the above command will start an interactive bash terminal session
on a node of the 'gpu' partition, equipped with 1 GPU card.
:::

First, let's verify that you are indeed on a node equipped with a functional
GPU, by typing `nvidia-smi`:
```{code-block} console
$ nvidia-smi
Tue May 12 17:02:17 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  Quadro RTX 5000                On  |   00000000:37:00.0 Off |                  Off |
| 33%   27C    P8             11W /  230W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```
Your output should look similar to the above. You will be able to see the GPU
name, temperature, memory usage, etc. If you see an error message instead,
(even though you are on a GPU node) please contact the SWC Scientific Computing team.

Next, load the SLEAP module.
```{code-block} console
$ module load SLEAP
```

Verify that SLEAP is correctly installed and can access the GPU by running
the built-in diagnostic command:
```{code-block} console
$ sleap doctor
```
This prints system information, package versions, and confirms whether a GPU
was detected. Look for the `[GPU / CUDA]` section.

:::{dropdown} Verify manually via the Python interpreter
:color: info
:icon: info

If `sleap doctor` fails, you can also verify manually by starting a
Python interpreter and running the following commands:

```{code-block} console
$ python
```

```{code-block} pycon
>>> import sleap
>>> import torch
>>> torch.cuda.is_available()
True
>>> torch.cuda.get_device_name(0)
'Quadro RTX 5000'
>>> exit()
```
:::

When done, exit the GPU node:
```{code-block} console
$ exit
```

To completely exit the HPC cluster, you will need to type `exit` or
`logout` until you are back to the terminal prompt of your local machine.
See [Set up SSH for the SWC HPC cluster](../programming/SSH-SWC-cluster.md)
for more information.

Using a legacy (TensorFlow) module instead?
See [Legacy (TensorFlow) modules](legacy-modules) for the equivalent verification steps.

If you encounter troubles with using the SLEAP module, contact
Niko Sirmpilatze of the SWC [Neuroinformatics Unit](https://neuroinformatics.dev/).


(legacy-modules)=
## Legacy (TensorFlow) modules

If you are using a legacy SLEAP module (≤ 1.4.1, TensorFlow backend), the
CLI uses `sleap-train` and `sleap-track` with JSON config files instead of
the YAML-based `sleap train` / `sleap track` shown above. See the
[legacy SLEAP documentation](https://legacy.sleap.ai/) for full details;
the equivalents for the steps in this guide are below.

### Training

```{code-block} bash
sleap-train centroid.json labels.v002.pkg.slp
sleap-train centered_instance.json labels.v002.pkg.slp
```

The exported training job package from legacy SLEAP also includes a
`train-script.sh` containing these commands, so you can run
`./train-script.sh` from the SLURM script. See the legacy
[remote training guide](https://legacy.sleap.ai/guides/remote.html#remote-training)
and [CLI reference](https://legacy.sleap.ai/guides/cli.html).

### Inference

```{code-block} bash
sleap-track video.mp4 \
    -m models/centroid/training_config.json \
    -m models/centered_instance/training_config.json \
    --gpu auto \
    --tracking.tracker simple \
    --tracking.similarity centroid \
    -o predictions.slp
```

### Verifying the module

The verification steps in the [](troubleshooting) section
use TensorFlow instead of PyTorch:

```{code-block} pycon
>>> import sleap
>>> sleap.versions()
>>> sleap.system_summary()
>>> import tensorflow as tf
>>> print(tf.config.list_physical_devices('GPU'))
>>> tf.constant("Hello world!")
```

For details, see the [legacy SLEAP installation guide](https://legacy.sleap.ai/installation.html#testing-that-things-are-working).
