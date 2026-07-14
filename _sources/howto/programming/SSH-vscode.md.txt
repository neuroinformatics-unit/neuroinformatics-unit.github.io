# SSH into an unmanaged machine using VSCode
> **_Example Usecase:_**  When working from home, connect from you local Mac to the SWC office Linux machine

In your local machine `cd` and ` open .ssh/config` and append the following configurations:
```
Host *
    ServerAliveInterval 60

Host jump-host
    User swcUserID
    HostName ssh.swc.ucl.ac.uk

Host remote-host
    User remoteMachineUsername
    HostName 172.24.243.000
    ProxyJump jump-host
```

Make sure to replace `172.24.243.000` with the IP address of your remote machine.
On Ubuntu, you can find the IP address in this way:
* Got to `Settings` then `Network`
* Click on the cogwheel next to your connections (usually `Wired`)
* The `IPv4` is the address you are looking for

If you do not have a config file in your .ssh folder, create one:
```bash
cd .ssh/
touch config
```

Connect to VPN, then use the `Open a remote window` (Remote - SSH extension) tool of vscode and connect to `remote-host`. You will be asked for your SWC and Linux passwords.
