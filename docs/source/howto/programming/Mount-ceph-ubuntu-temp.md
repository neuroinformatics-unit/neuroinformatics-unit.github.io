(target-mount-ceph-ubuntu-temp)=
# Mount ceph storage on Ubuntu temporarily
In this example, we will **temporarily** mount a partition of `ceph` in an Ubuntu machine. The mounting is temporary because it will only remain until the next reboot. To mount a partition of `ceph` permanently, see [Mount ceph storage on Ubuntu permanently](target-mount-ceph-ubuntu-perm).


## Prerequisites
- Administrator rights (`sudo`) on the local Ubuntu machine
- `cifs-utils` installed via `sudo apt-get install cifs-utils`


## Steps
### 1. Create a mount point
Create a directory to mount the storage to. Sensible places to do this on Ubuntu would be in `/mnt` or `/media`. In the example below, we will use `/mnt/ceph-neuroinformatics`.

```bash
sudo mkdir /mnt/ceph-neuroinformatics
```

### 2. Mount the `ceph` partition
To mount the desired partition on the directory we just created, run the `mount` command with the appropriate options. In our example, this would be:
```bash
sudo mount -t cifs -o user=<SWC-USERNAME>,domain=AD.SWC.UCL.AC.UK //ceph-gw02.hpc.swc.ucl.ac.uk/neuroinformatics /mnt/ceph-neuroinformatics
```
:::{note}
You can check the full set of options for the `mount` command by running `mount --help`
:::

Make sure to replace the following for your particular case:
- `//ceph-gw02.hpc.swc.ucl.ac.uk/neuroinformatics` with the path to your desired partition, e.g. `//ceph-gw02.hpc.swc.ucl.ac.uk/<LAB-NAME>`
- `/media/ceph-neuroinformatics` with the path to the local mount point you created in the previous step.
- `<SWC-USERNAME>` with your SWC username

If the command is executed without errors you will be prompted for your SWC password.

### 3. Check the partition is mounted correctly
It should show up in the list of mounting points when running `df -h`

:::{note}
The command `df` prints out information about the file system
:::

### 4. To unmount the storage
Run the following command
```bash
sudo umount /mnt/ceph-neuroinformatics
```
Remember that because the mounting is temporary, the `ceph` partition will be unmounted upon rebooting our machine.

You can check that the partition is correctly unmounted by running `df -h` and verifying it does not show in the output.

:::{warning}
Do not use `sudo rm -r /media/ceph-neuroinformatics` to unmount, even though it looks like a local folder. This will delete files on `ceph`!
:::

## References
- [Mount network drive under Linux temporarily/permanently](https://www.rz.uni-kiel.de/en/hints-howtos/connecting-a-network-share/Linux/through-temporary-permanent-mounting/mount-network-drive-under-linux-temporarily-permanently)
- [How to Mount a SMB Share in Ubuntu](https://support.zadarastorage.com/hc/en-us/articles/213024986-How-to-Mount-a-SMB-Share-in-Ubuntu)
