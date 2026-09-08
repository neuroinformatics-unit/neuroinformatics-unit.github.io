(ssh-cluster-target)=
# Set up SSH for the SWC HPC cluster

This guide explains how to connect to the SWC's HPC cluster via SSH from
any personal computer.

```{include} ../../_static/howto/swc-wiki-warning.md
```

```{include} ../../_static/howto/code-blocks-note.md
```

## Abbreviations
| Acronym                                                                 | Meaning                                      |
| ----------------------------------------------------------------------- | -------------------------------------------- |
| [SSH](https://en.wikipedia.org/wiki/Secure_Shell)                       | Secure (Socket) Shell protocol               |
| [SWC](https://www.sainsburywellcome.org/web/)                           | Sainsbury Wellcome Centre                    |
| [HPC](https://en.wikipedia.org/wiki/High-performance_computing)         | High Performance Computing                   |
| [IT](https://en.wikipedia.org/wiki/Information_technology)              | Information Technology                       |
| [SLURM](https://slurm.schedmd.com/)                                     | Simple Linux Utility for Resource Management |
| [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) | Integrated Development Environment           |
| [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface)           | Graphical User Interface                     |

## Prerequisites
- You have an SWC account and know your username and password.
- You have read the [SWC wiki's section on High Performance Computing (HPC)](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-High-Performance-Computing-147954090.aspx), especially the [Logging into the Cluster page](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-Logging-into-the-Cluster-194972967.aspx).
- You know the basics of using the command line, i.e. using the terminal to navigate the file system and run commands.
- You have an SSH client installed on your computer. This is usually pre-installed on Linux and macOS. SSH is also available on Windows (since Windows 10), however some steps will differ. If you are a Windows user, read the note below before proceeding.

::: {dropdown} Note for Windows users
:color: info
:icon: info

You have two options on how to proceed:

1. Install [Git Bash](https://gitforwindows.org/), which emulates a Linux terminal on Windows and includes tools that are not available on Windows by default, such as `nano`, and `ssh-copy-id`. This is the recommended option, as it will allow you to follow along with all commands in this guide, as they are presented. Just assume that all commands are run in Git Bash.

2. If you are using Windows 10 or newer, you can follow this guide (except for the section on [SSH keys](#ssh-keys)) using native Windows functionalities as described here.

    To [Log into the cluster](#log-into-the-cluster), you can use the same commands as in the guide below, but typed in the Windows `cmd` or PowerShell.

    The [SSH config file](#ssh-config-file) section can be followed using the file browser and Notepad, instead of the terminal and `nano`.
    Create the `.ssh` folder in you home directory, i.e. `C:\Users\<USERNAME>\.ssh`,
    if it does not already exist (don't forget the `.` at the start of `.ssh`).

    You may create and edit the `config` file with Notepad but beware that the file must not have an extension.
    To create a file without an extension in Windows, you need to make the file extensions visible
    (click 'View' in the file browser and check the box 'File name extensions').
    The `config` file contents should be the same as in the guide below.

    In day-to-day use, you can use the `ssh swc-gateway` command natively in Windows `cmd`,
    provided that you have defined the alias in your `config` file, as this guide describes.
:::

## Log into the cluster

Run the following commands on the terminal, typing your `<SWC-PASSWORD>` when prompted.
Note that the password will not be displayed on the screen as you type.

If you are physically **at SWC** using a **wired network connection** (i.e., not eduroam)—or
connected using the **SWC VPN**, you can directly connect to the cluster's *gateway* node (`hpc-gw2`).

```{code-block} console
$ ssh <SWC-USERNAME>@hpc-gw2
```

In any other scenario, you are **not within the SWC network**; you must first connect to a secure access point (called the *bastion* node) before you can reach the cluster's *gateway* node (`hpc-gw2`).

```{code-block} console
$ ssh <SWC-USERNAME>@ssh.swc.ucl.ac.uk
$ ssh hpc-gw2
```

To return to the computer you came from, simply type `logout`. You can think of `logout` as undoing the last `ssh` command you ran.

:::{admonition} You may stop reading here, but...

If you want to learn more about the various types of HPC nodes (*bastion / gateway / compute*), read the [next section](#types-of-hpc-nodes).

If you want to make you life easier, you can set yourself up with an [SSH config file](#ssh-config-file)
and some [SSH keys](#ssh-keys).
:::


## Types of HPC nodes

A *node* is simply a computer that is part of the cluster.
Let's distinguish the different types of nodes on the SWC HPC system.

| Node Type | Hostname | Analogy / Role | Use cases |
| :--- | :--- | :--- | :--- |
| *Bastion* | `ssh.swc.ucl.ac.uk` | Secure entry point | **Strictly pass-through.** Do not run any computations or file operations. If you find yourself here, just type `ssh hpc-gw2` to reach the *gateway* node. |
| *Gateway* | `hpc-gw2` | Staging Area | **Light-weight tasks only** (script editing, file management, job submission). Do not run computations. |
| *Compute* | `enc1-node10`, `gpu-sr670-21`, etc. | Workhorses | **Run the actual computations** submitted via `srun` or `sbatch`. |

![](../../_static/howto/ssh_flowchart_unmanaged.png)

Your home directory, as well as the locations where filesystems like `ceph` are mounted, are shared across all of the nodes.

The *compute* nodes should only be accessed via the SLURM `srun` or `sbatch` commands from the *gateway* node.

:::{dropdown} Be mindful of using shared nodes
:color: warning
:icon: alert

Avoid running heavy computations on the *bastion* or *gateway* nodes, as these are shared across all users of the HPC cluster.

It's always safer to request dedicated *compute* resources, which will be yours for the duration of your job.

For example, this is how you can request an an interactive session on a *compute* node to create a new conda environment:

```{code-block} console
$ srun -p cpu -n 4 --mem 8G --pty bash -i
$ module load miniconda
$ conda create -n myenv python=3.10
```

The first command requests 4 cores and 8GB of memory on a node of the `cpu`
partition, meant for jobs that do not require GPUs.
Depending on your needs and node availability, you may need to request
a different partition. See the [SLURM arguments primer](slurm-arguments-target)
for more information.

The `--pty bash -i` part specifies an interactive bash shell.
The following two commands are run in this shell, on the assigned *compute* node.

Type `exit` to leave the interactive session when finished.
Avoid keeping sessions open when not in use.
:::

(target-managed-desktops)=
## Note on managed desktops

The SWC's IT team offers managed desktop computers equipped with either
a Windows or a Linux image. These machines are already part of the SWC's
trusted network domain, meaning you can easily access the HPC cluster.

- If you are using a [managed Windows desktop](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-SWC-Desktops-147956857.aspx),
you can SSH directly into the *gateway* node with `ssh hpc-gw2` from the
Windows `cmd` or PowerShell. You may use that node to prepare your scripts and submit SLURM jobs.
- If you are using a [managed Linux desktop](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-Managed-Linux-Desktop-69502751.aspx),
you can even bypass the *gateway* node. In fact, you may directly submit SLURM jobs
from your terminal, without having to SSH at all. That's because managed Linux desktops
use the same platform as the HPC nodes
and are already equipped with the SLURM job scheduler.

A modified version of the flowchart found above, including managed desktops:

![](../../_static/howto/ssh_flowchart_full.png)


## SSH config file
If you are frequently accessing the cluster from outside the SWC network,
you may find yourself typing the same SSH commands over and over again.
You can make your life easier by editing the SSH config file.
This is a text file that lives in your home directory and contains
a list of aliases for SSH connections.

On your local PC/Laptop, navigate to the `.ssh` folder in your user's home `~` directory:
```{code-block} console
$ cd ~/.ssh
```

List the files in this directory:
```{code-block} console
$ ls -1
authorized_keys
config
known_hosts
```
Some of these files may not exist yet. Next we will open the `config` file
using the terminal text editor `nano`:
```{code-block} console
$ nano config
```
If the file doesn't exist yet, it will be created.
Add the following lines to the file:

```{code-block} bash
:caption: config
:name: config-content

# Specify our intermediate jump host, aka the bastion node
Host swc-bastion
    HostName ssh.swc.ucl.ac.uk
    User <SWC-USERNAME>

# Specify how to get to the gateway node by jumping through the bastion node
# The gateway hostname is specified as the jump-host would see it
Host swc-gateway
    HostName hpc-gw2
    User <SWC-USERNAME>
    ProxyJump swc-bastion
```

Save the file by pressing `Ctrl+O`, then `Enter`.
Exit the `nano` editor by pressing `Ctrl+X`.

From now on, you can directly SSH into the *gateway* node by typing:
```{code-block} console
$ ssh swc-gateway
```
You can also use the same syntax to SSH into the *bastion* node:
```{code-block} console
$ ssh swc-bastion
```
In both cases, typing the `logout` command once will return you to your local machine.

## SSH keys
If you are bored of typing your password every time you SSH into the cluster,
you can set up authentication via SSH keys. You will have to do some work
upfront, but it will save you tons of time in the long run. Plus, it's more secure.

::: {dropdown} How does SSH key authentication work?
:color: info
:icon: info
You generate a pair of keys locally—a public and a private one—
and then copy the public key to the remote machine.
When you try to SSH into the remote machine, the SSH client on your local machine
will use the private key to generate a signature, which the SSH server on the
remote machine will verify using the public key. If the signature is valid,
you will be granted access.

There are several cryptographic algorithms that can be used to generate the keys.
They can be selected using the `-t` argument of the `ssh-keygen` command.
In the following example, we use `ed25519`, as it strikes a good balance between
security and speed for most use cases.
:::

To generate a pair of SSH keys, run the following command on your local machine:
```{code-block} console
$ ssh-keygen -t ed25519
```

You will be prompted to enter a file path for the key. You may accept the
default - `~/.ssh/id_ed25519` - or choose another path/name.

Next, you will be prompted to enter a passphrase.
This is an extra layer of security, but you can leave it blank if you want.

There are now two new files in the `.ssh` directory:
```{code-block} console
:emphasize-lines: 5,6
$ cd ~/.ssh
$ ls -1
authorized_keys
config
id_ed25519
id_ed25519.pub
known_hosts
```
The `id_ed25519` file is your private key and **it should never be shared with anyone**.

The `id_ed25519.pub` file is your public key.

:::{dropdown} When to specify private key location in the SSH config
:color: warning
:icon: alert
In most cases, you don't need to explicitly specify the location of the private key
in your `~/.ssh/config` file because SSH will automatically look for the default key names
(like `id_rsa`, `id_ed25519`, etc.) in the `~/.ssh` directory.

However, if you're using a non-default name or location for your private key,
or if you have multiple keys and want to specify which one to use for a particular host,
then you can add the `IdentityFile` directive in your `~/.ssh/config` to
point to the private key.

For example, if you have a private key with a custom name `<MY-SPECIAL-KEY>`
in the `~/.ssh` directory, you can add the following lines to your `~/.ssh/config` file:


```{code-block} bash
:caption: config
:emphasize-lines: 5,13

# Specify our intermediate jump host, aka the bastion node
Host swc-bastion
    HostName ssh.swc.ucl.ac.uk
    User <SWC-USERNAME>
    IdentityFile ~/.ssh/<MY-SPECIAL-KEY>

# Specify how to get to the gateway node by jumping through the bastion node
# The gateway hostname is specified as the jump-host would see it
Host swc-gateway
    HostName hpc-gw2
    User <SWC-USERNAME>
    ProxyJump swc-bastion
    IdentityFile ~/.ssh/<MY-SPECIAL-KEY>
```
:::

Next, let's copy the public key you just generated to the remote machines.

```{code-block} console
$ ssh-copy-id -i id_ed25519.pub swc-gateway
```

::: {dropdown} Explain the above command
:color: info
:icon: info
The `ssh-copy-id` command uses the configuration we previously set up
in the `config` file to figure out how to reach the remote machine.

It copies the specified public key to your home directory on the target machine (in this case `swc-gateway`) and adds it to the `.ssh/authorized_keys` file there.

Since your SWC home directory is shared across all HPC nodes, the public
key will be available on all of them. That's why you only need to run the above command once.
:::


🎉 Congrats! You can now directly SSH into the *gateway* node without typing your password:
```{code-block} console
$ ssh swc-gateway
```
