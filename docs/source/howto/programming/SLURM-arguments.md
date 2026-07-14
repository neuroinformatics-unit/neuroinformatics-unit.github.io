(slurm-arguments-target)=
# SLURM arguments primer

```{include} ../../_static/howto/swc-wiki-warning.md
```

## Abbreviations
| Acronym                                                         | Meaning                                      |
| --------------------------------------------------------------- | -------------------------------------------- |
| [SLURM](https://slurm.schedmd.com/)                             | Simple Linux Utility for Resource Management |
| [SWC](https://www.sainsburywellcome.org/web/)                   | Sainsbury Wellcome Centre                    |
| [HPC](https://en.wikipedia.org/wiki/High-performance_computing) | High Performance Computing                   |
| [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)  | Message Passing Interface                    |


## Overview
SLURM is a job scheduler and resource manager used on the SWC HPC cluster.
It is responsible for allocating resources (e.g. CPU cores, GPUs, memory) to jobs submitted by users.
When submitting a job to SLURM, you can specify various arguments to request the resources you need.
These are called SLURM directives, and they are passed to SLURM via the `sbatch` or `srun` commands.

These are often specified at the top of a SLURM job script,
e.g. the lines that start with `#SBATCH` in the following example:

```{code-block} bash
#!/bin/bash

#SBATCH -J my_job # job name
#SBATCH -p gpu # partition (queue)
#SBATCH -N 1   # number of nodes
#SBATCH --mem 16G # memory pool for all cores
#SBATCH -n 4 # number of cores
#SBATCH -t 0-06:00 # time (D-HH:MM)
#SBATCH --gres gpu:1 # request 1 GPU (of any kind)
#SBATCH -o slurm.%x.%N.%j.out # STDOUT
#SBATCH -e slurm.%x.%N.%j.err # STDERR
#SBATCH --mail-type=ALL
#SBATCH --mail-user=user@domain.com
#SBATCH --array=1-12%4 # job array index values

# load modules
...

# execute commands
...
```
This guide provides only a brief overview of the most important SLURM arguments,
to demysify the above directives and help you get started with SLURM.
For a more detailed description see the [SLURM documentation](https://slurm.schedmd.com/sbatch.html).

##  Commonly used arguments

### Partition (Queue)
- *Name:* `--partition`
- *Alias:* `-p`
- *Description:* Specifies the partition (or queue) to submit the job to. To see a list of all partitions/queues, the nodes they contain and their respective time limits, type `sinfo` when logged in to the HPC cluster.
- *Example values:* `gpu`, `cpu`

### Job Name
- *Name:* `--job-name`
- *Alias:* `-J`
- *Description:* Specifies a name for the job, which will appear in various SLURM commands and logs, making it easier to identify the job (especially when you have multiple jobs queued up)
- *Example values:* `training_run_24`

### Number of Nodes
- *Name:* `--nodes`
- *Alias:* `-N`
- *Description:* Defines the number of nodes required for the job.
- *Example values:* `1`

:::{warning}
This is usually `1` unless you're parallelising your code across multiple nodes with technologies such as MPI.
:::

### Number of Cores
- *Name:* `--ntasks`
- *Alias:* `-n`
- *Description:* Defines the number of cores (or tasks) required for the job.
- *Example values:* `1`, `5`, `20`

### Memory Pool for All Cores
- *Name:* `--mem`
- *Description:* Specifies the total amount of memory (RAM) required for the job across all cores (per node)
- *Example values:* `4G`, `32G`, `64G`

### Time Limit
- *Name:* `--time`
- *Alias:* `-t`
- *Description:* Sets the maximum time the job is allowed to run. The format is D-HH:MM, where D is days, HH is hours, and MM is minutes.
- *Example values:* `0-01:00` (1 hour), `0-04:00` (4 hours), `1-00:00` (1 day).

:::{warning}
If the job exceeds the time limit, it will be terminated by SLURM.
On the other hand, avoid requesting way more time than what your job needs,
as this may delay its scheduling (depending on resource availability).

If needed, the systems administrator can extend long-running jobs.
:::

### Generic Resources (GPUs)
- *Name:* `--gres`
- *Description:* Requests generic resources, such as GPUs.
- *Example values:* `gpu:1`, `gpu:rtx2080:1`, `gpu:rtx5000:1`, `gpu:a100_2g.10gb:1`

:::{warning}
No GPU will be allocated to you unless you specify it via the `--gres` argument (even if you are on the 'gpu' partition).
To request 1 GPU of any kind, use `--gres gpu:1`. To request a specific GPU type, you have to include its name, e.g. `--gres gpu:rtx2080:1`.
You can view the available GPU types on the [SWC internal wiki](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-CPU-and-GPU-Platform-architecture-165449857.aspx).
:::

### Standard Output File
- *Name:* `--output`
- *Alias:* `-o`
- *Description:* Defines the file where the standard output (STDOUT) will be written. In the example script above, it's set to slurm.%x.%N.%j.out, where %x is the job name, %N is the node name and %j is the job ID.
- *Example values:* `slurm.%x.%N.%j.out`, `slurm.MyAwesomeJob.out`

:::{note}
This file contains the output of the commands executed by the job (i.e. the messages that normally gets printed on the terminal).
:::

### Standard Error File
- *Name:* `--error`
- *Alias:* `-e`
- *Description:* Specifies the file where the standard error (STDERR) will be written. In the example script above, it's set to slurm.%x.%N.%j.out, where %x is the job name, %N is the node name and %j is the job ID.
- *Example values:* `slurm.%N.%j.err`, `slurm.MyAwesomeJob.err`

:::{note}
This file is very useful for debugging, as it contains all the error messages produced by the commands executed by the job.
:::

### Email Notifications
- *Name:* `--mail-type`
- *Description:* Defines the conditions under which the user will be notified by email.
- *Example values:* `ALL`, `BEGIN`, `END`, `FAIL`

### Email Address
- *Name:* `--mail-user`
- *Description:* Specifies the email address to which notifications will be sent.
- *Example values:* `user@domain.com`

### Array jobs
- *Name:* `--array`
- *Description:* Job array index values (a list of integers in increasing order). The task index can be accessed via the `SLURM_ARRAY_TASK_ID` environment variable.
- *Example values:* `--array=1-10` (10 jobs), `--array=1-100%5` (100 jobs, but only 5 of them will be allowed to run in parallel at any given time).

:::{warning}
If an array consists of many jobs, using the `%` syntax to limit the maximum number of parallel jobs is recommended to prevent overloading the cluster.
:::
