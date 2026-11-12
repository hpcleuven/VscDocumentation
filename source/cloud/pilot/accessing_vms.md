# Accessing VMs

## SSH key pairs

When a VM is instantiated, OpenNebula will inject any SSH keys associated with your user.
These keys will be synced to your OpenNebula user from the [VSC account page](https://account.vscentrum.be).
You may also add keys to OpenNebula manually in the [user settings](https://cloudpr4.ugent.be/fireedge/sunstone/settings) of the VSC Cloud Dashboard.
For general instructions on SSH keys, see: [Security Keys](/accounts/generating_keys.rst).

You can of course add more keys to individual VMs via the appropriate method for your OS.
:::{note}
The SSH keys are injected **only** when the VM is created. Adding or removing a key in VSC account page or in OpenNebula will not change the authorized keys in existing VMs.
:::

## Windows

UGent Firewall blocks RDP connections for security reasons. 
You can however, connect to our Windows image with SSH. The [Tofu module](./opentofu.md) will give you the credentials.

Many RDP clients (excluding Windows' own RDP client) support SSH tunneling. This way you can securely access your VM with RDP.
To obtain the password for RDP, add an output block:
```
output "Password" {
  value     = module.WindowsExample.windows_password
  sensitive = true
}
```
Tofu will automatically hide the password in the output. To show the password, use `tofu output --show-sensitive`.
:::{warning}
The password **will** be in the statefile in cleartext, so keep this file safe. 
:::
### Tested RDP Clients
This is an overview of RDP clients that were tested with SSH tunnelling.
#### [MobaXTerm](https://mobaxterm.mobatek.net/)
This Windows-only freemium client supports SSH tunneling.
To enable SSH tunnelling:
1) Create a new RDP session
2) Remote host: `localhost`, Username: `Admin`
3) Network settings -> SSH gateway
    1) Gateway host: your public ip
    2) Username: Admin, port 22
    3) Enable "Use SSH key" and select your private key. 

#### [Remmina](https://remmina.org/)
This Linux-only client supports SSH tunneling
To enable SSH tunnelling:
1) Create a connection profile for RDP
2) Configure Username (Admin) and password for the RDP connection
3) Click "SSH Tunnel"
    1) Enable SSH Tunnel
    2) Enable "Tunnel via loopback address"
    3) Authentication type: "Public key (automatic)
    4) Username: Admin
4) Save.
