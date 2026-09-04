# Accessing VMs
## SSH key pairs
OpenNebula will automatically add SSH Keys to your VMs.
These keys will be synced to your OpenNebula user from the accountpage.
For general instructions on SSH keys, see: [Security Keys](/accounts/generating_keys.rst).

If you have generated a key pair with an external tool, you can import
it into OpenStack. The key pair can be used for multiple instances that
belong to a project. For more information, see section
[import a key pair](#import-a-key-pair).

You can of course add more keys to individual VMs via the appropriate method for your OS.

## Windows
:::{note}
WIP: Need RDP client recommendations with tunneling support
:::
UGent Firewall blocks RDP connections for security reasons. 
You can however, connect to our Windows image with SSH. The [Tofu module](./opentofu.md) will give you the credentials.

Many RDP clients (excluding Windows' own RPD client) support SSH tunneling. This way you can securely access your VM with RDP.