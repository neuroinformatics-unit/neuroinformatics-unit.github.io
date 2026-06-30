(target-mount-ceph-ubuntu-perm)=
# Mount ceph storage on Ubuntu permanently
In this example, we will **permanently** mount the `neuroinformatics` partition of `ceph`. The same procedure can be used to mount other partitions, such as those belonging to particular labs or projects.

To mount a partition of `ceph` only temporarily, see [Mount ceph storage on Ubuntu temporarily](target-mount-ceph-ubuntu-temp).


The following instructions have been tested on **Ubuntu 20.04 LTS**.

## Prerequisites
- Administrator rights (`sudo`) on the local Ubuntu machine
- `cifs-utils` installed via `sudo apt-get install cifs-utils`

## Steps
### 1. Store your SWC credentials
First, create a file to store your SWC login credentials and save it in your home directory.
You can do that on the terminal via `nano ~/.smb_swc`.

The ``.smb_swc`` file contents should look like this:
```bash
user=<SWC-USERNAME>
password=<SWC-PASSWORD>
domain=AD.SWC.UCL.AC.UK
```
Save the file and exit.

:::{warning}
Storing the password in plain-text format as done above constitutes a security risk.
If someone gets access to your machine, they will be able to see your SWC password.

You can harden the security a bit by changing the permissions of the file. Run the following command:

```bash
chmod 600 ~/.smb_swc
```
This will ensure the file is readable and writable only by the owner (you).
However, if someone gets access to your machine with your user logged in, they will still be able to read the SWC password.
:::

### 2. Create a mount point
Create a directory to mount the storage to. Sensible places to do this on Ubuntu would be in `/mnt` or `/media`. In the example below, we will use `/media/ceph-neuroinformatics`.

```bash
sudo mkdir /media/ceph-neuroinformatics
```

### 3. Edit the fstab file
This will allow you to mount the storage automatically on boot. Before editing the file, make a backup of it, just in case.
```bash
sudo cp /etc/fstab /etc/fstab.bak
```
Now, open the file with your favourite editor (e.g. `sudo nano /etc/fstab`) and add new lines at the end of the file.

For example:
```bash
# Mount ceph/neuroinformatics
//ceph-gw02.hpc.swc.ucl.ac.uk/neuroinformatics /media/ceph-neuroinformatics cifs uid=1002,gid=1002,credentials=/home/<LOCAL-USERNAME>/.smb_swc 0 0
```
Make sure to replace the following:
- `//ceph-gw02.hpc.swc.ucl.ac.uk/neuroinformatics` with the path to your desired partition, e.g. `//ceph-gw02.hpc.swc.ucl.ac.uk/<LAB-NAME>`
- `/media/ceph-neuroinformatics` with the path to the local mount point you created in the previous step.
- `uid=1002,gid=1002` with your local user ID and group ID. You can find these out by running `id` on the terminal.
- `<LOCAL-USERNAME>` with your username on the local Ubuntu machine on which you are mounting the storage

Save the file and exit.

### 4. Mount the storage
You can now mount the storage by running `sudo mount -a`. If you get an error, check the `fstab` file for typos. If you get no error, you should be able to see the mounted storage by running `df -h`.

The next time you reboot your machine, the storage should be mounted automatically.

### 5. Unmount the storage
To unmount the storage, run `sudo umount /media/ceph-neuroinformatics` (or whatever your mount point is).

To permanently unmount the storage, remove the lines you added to the `fstab` file and run `sudo mount -a` again.

:::{warning}
Do not trust your instincts and use `sudo rm -r /media/ceph-neuroinformatics` to permanently unmount, even though it looks like a local folder. This will delete files on `ceph`!
:::
