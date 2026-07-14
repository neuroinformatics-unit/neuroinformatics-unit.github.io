# Using VSCode with interactive SLURM jobs on the SWC HPC cluster

This guide explains how to set up and use VSCode in a SLURM interactive job on the SWC HPC cluster, offering a solution for users who require fast access to shared storage or substantial computational resources.

This solution is easy to set up and constrained by the SLURM job's resource limits, as long as those limits are applied. This ensures that users can work efficiently within the allocated resources, preventing system overload. While the constraints depend on SLURM's enforcement (e.g., memory or time limits), users should remain mindful of their resource requests to avoid program terminations.

Furthermore, VSCode's code tunnel automatically forwards any HTTP servers launched from the compute node, such as Dash-Plotly apps or Jupyter Notebook servers, offering seamless integration.


## Instructions

First, open a terminal (not the VSCode terminal) and connect to the gateway node by running:

```{code-block} console
$ ssh <SWC-USERNAME>@ssh.swc.ucl.ac.uk
$ ssh hpc-gw2
```

Once connected, request an interactive job via SLURM to access a compute node. For example:

```{code-block} console
$ srun -p cpu -n 4 --mem 8G --pty bash -i
```

In this example, `-p cpu` requests the "cpu" partition, with default time settings, though you may adjust this according to your needs.
You can also try other partitions depending on your needs and node availability.
For more information, see the [SLURM arguments primer](slurm-arguments-target).

After connecting to a compute node, initiate [VSCode Remote Tunnel](https://code.visualstudio.com/docs/remote/tunnels) by typing:

```{code-block} console
$ code tunnel
```

A URL (`https://github.com/login/device`) and a PIN code will appear in the terminal.
Follow this link, log in with your GitHub credentials, and enter the provided PIN to authorize access.

You have two options to run VSCode:

-  **Run VSCode in the browser:**
    After completing the above step, a second link will appear in the terminal (e.g., `https://vscode.dev/tunnel/<node-name>`), which you can follow to launch a VSCode browser-based session running directly on the HPC compute node. If you sign in to your VSCode account and have account syncing enabled, you will have your extensions and settings available.

- **Run VSCode on your local machine:**
    If you want instead to use your local VSCode, install the "Remote - Tunnels" extension, click on "Open remote window" in the bottom left corner of the VSCode window, and select "Connect to Tunnel". You should see the node name in the list of available tunnels. Click on it to connect to the VSCode session running on the HPC compute node.

:::{note}
The name associated with the tunnel may not match the node name assigned by SLURM. E.g., the assigned compute node may appear as `gpu-380-11` in SLURM, but the corresponding tunnel may be named `gpu-350-02` in VSCode. When using VSCode via the browser, the tunnel name is shown at the end of the URL (e.g., `https://vscode.dev/tunnel/<node-name>`).
:::

If by mistake you close your terminal window, the tunnel will continue to run until you reach the time limit. To rejoin the SLURM job, you can use the following command if you know the job ID:

```{code-block} console
$ sattach <JOBID>.0
```

When you’re finished, simply exit the SLURM session to close the VSCode tunnel and release the assigned resources.

::: {dropdown} Why do I have to authenticate via GitHub?
:color: info
:icon: info

As explained in [VSCode docs](https://code.visualstudio.com/docs/remote/tunnels) it serves as a secure way to authenticate the user and ensure that only the user who initiated the tunnel can access it:
> Tunneling securely transmits data from one network to another via [Microsoft dev tunnels](https://learn.microsoft.com/azure/developer/dev-tunnels/overview).
>
> Both hosting and connecting to a tunnel requires authentication with the same Github or Microsoft account on each end. In both cases, VS Code will make outbound connections to a service hosted in Azure; no firewall changes are generally necessary, and VS Code doesn't set up any network listeners.
>
>Once you connect from a remote VS Code instance, an SSH connection is created over the tunnel in order to provide end-to-end encryption.
:::

## Port forwarding

One advantage of using VSCode's code tunnel is that it automatically detects any HTTP servers you launch from the same node (such as Dash-Plotly apps or Jupyter Notebook servers) and shows them in the "Ports" view. Make sure to launch your server inside your compute node, for example by running:

```{code-block} console
$ jupyter notebook
```

You can then open the forwarded address from the Ports view in your browser or copy it. By default, forwarded ports are private and require GitHub authentication; to make a port public (no sign-in required), right-click the port and select "Port Visibility > Public." For more details, see the [VSCode port forwarding documentation](https://code.visualstudio.com/docs/debugtest/port-forwarding).
