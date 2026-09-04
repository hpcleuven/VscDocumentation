# Networking
Test
Each project will get a private network that connects your virtual machines together.
The gateway for this network will be a Virtual Router, which has a public IP address that is randomly assigned.
A project with VSC access enabled will also have a private network to connect the virtual machines to the VSC Virtual Router.

Each project will need **exactly one** public router to access the internet.
This router will be created for you if you use the [OpenTofu module](opentofu.md).
Through this router you can set up port-forwarding rules to your VMs.

:::{danger}
If your router is deleted (via `tofu destroy`, for example) your **public IP address** might change.
Avoid deleting your router(s), as we cannot manually assign/restore a specific IP to your project.
:::

:::{note}
By default, the UGent firewall blocks most IP addresses and ports on the public router.
Only the port (TCP) range **50000-60000** and ports **80** and **443** 
are open by default for the public floating IP addresses. Contact <cloud@vscentrum.be> if you need to access other ports from
the outside world.
:::

## Firewall
In the previous cloud, OpenStack offered security groups. These are not supported with our new networking model in Opennebula.
Your VMs will thus not be firewalled from each other, and you may have to configure a firewall on OS level.
Of course, your VM is isolated from other projects and the internet, except for any port-forwarding you configure.
