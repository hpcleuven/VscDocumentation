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
:::{note}
WIP: Need RDP client recommendations with tunneling support
:::
UGent Firewall blocks RDP connections for security reasons. 
You can however, connect to our Windows image with SSH. The [Tofu module](./opentofu.md) will give you the credentials.

Many RDP clients (excluding Windows' own RDP client) support SSH tunneling. This way you can securely access your VM with RDP.