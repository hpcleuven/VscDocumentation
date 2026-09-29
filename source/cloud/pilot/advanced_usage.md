# Advanced usage
We highly recommend using the [OpenTofu](./opentofu.md) module for deploying your infrastructure.
There is limited support for workflows that do not use it.
If there is some functionality you need, feel free to contact the VSC Cloud admins via email at
<cloud@vscentrum.be> or submit a Merge Request on the [Github Repository](https://github.com/hpcugent/terraform-vsc-opennebula).

## Restrictions
### VM Size
In order to facilitate migrations between different hypervisors, VMs have resource limits. 
A VM may not exceed:
* `368640` Mib of RAM
* `20` CPU

VMs that exceed this size **will** be shut down.

### Templates
All VMs must use the provided templates. It is not possible to use custom OpenNebula templates. 

