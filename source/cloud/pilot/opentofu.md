# Creating VMs Using OpenTofu
OpenTofu <https://opentofu.org/> is an
infrastructure as code tool (IaC). It is a fork of [Terraform](https://developer.hashicorp.com/terraform).
Opentofu is currently one of the most popular infrastructure automation tools
available. VSC Cloud provides an OpenTofu module to simplify VM provisioning: https://search.opentofu.org/module/hpcugent/opennebula/vsc/latest.

**OpenTofu**
The client is available for different Operating Systems like Windows, Linux
or macOS (<https://opentofu.org/docs/intro/install/>) but it is also available
from UGent login node _login.hpc.ugent.be_.

## Create credentials for OpenTofu

Tofu requires a username and a login token to authenticate to the Opennebula API. Obtaining a login token is explained in: [application credentials](access.md#login-token).
After obtaining the token, place it in `~/.one/one_auth` on your VSC login node (login.hpc.ugent.be) or on your local machine if you have installed OpenTofu and the One CLI.
The file should be in this format (replace `vscxxx` with your username and `token` with your login token):
```
vscxxx:token
```
:::{tip}
You can easily access and edit the files on the login node by going to the [HPC UGent dashboard](https://login.hpc.ugent.be/pun/sys/dashboard/files/). 
**Enable "Show Dotfiles"** to see the `.one` directory. If it is not there, you may have to create it.

You can also access the commandline of the login node there (under `Clusters` dropdown).
:::
## Using the OpenTofu module

You can connect to UGent login node `login.hpc.ugent.be` to use
OpenTofu. Login to the login node with your VSC account first:

```shell
ssh -A vscxxxxx@login.hpc.ugent.be
```
:::{important}
It is important to forward your ssh agent with `-A` when SSH-ing to the login node.
:::
If this is the first time. you can download the examples with this snippet:
```shell
export MODULE_VERSION="0.0.6"
mkdir -p cloud-examples/
curl -L https://github.com/hpcugent/terraform-vsc-opennebula/archive/refs/tags/$MODULE_VERSION.tar.gz   | tar -xz --strip-components=2 -C cloud-examples terraform-vsc-opennebula-$MODULE_VERSION/examples
```
You can also browse them on [Github](https://github.com/hpcugent/terraform-vsc-opennebula/tree/0.0.5/examples)

Make sure you have *`~/.one/one_auth`* on the login node (see previous [section](#create-credentials-for-opentofu)).

:::{danger}
Do not share your credential file (`~/.one/one_auth`) or put this
file in a public place.
:::


## Basic VM configuration
:::{tip}
If you are **not** using the VSC login node, you need to make sure to:
1) [Install OpenTofu](https://opentofu.org/docs/intro/install/)
2) Install Opennebula client (**optional**):
    1) Add the repository for your linux distro: https://docs.opennebula.io/7.2/software/installation_process/frontend_installation/opennebula_repository_configuration_ce/
    2) Install `opennebula-tools` with your package manager
:::

In the previous [section](#using-the-opentofu-module) we created a `cloud-examples/` directory.
You can copy one of the examples to your new project:
```
mkdir -p MyProject
cp cloud-examples/simple-server/* MyProject/
rm -f MyProject/*.tofutest
```
Let's take a look at the [Simple Server](https://github.com/hpcugent/terraform-vsc-opennebula/tree/0.0.5/examples/simple-server) example's `main.tf`.

This file contains the most basic configuration for a virtual machine.
It consists of two **modules**. A module is convenient grouping of opentofu resources. 
A module has a **source** and a **version**. The source points to our [Module on the OpenTofu Registry](https://search.opentofu.org/module/hpcugent/opennebula/vsc/latest).
The version determines the version of the module you are using. You can view the documentation specific to the version you're using on the OpenTofu registry.


We need three things for our basic setup:
### The Router
```{tip}
Full router module documentation can be found [here](https://search.opentofu.org/module/hpcugent/opennebula/vsc/latest/submodule/router)
```
```
module "router" {
  source  = "hpcugent/opennebula/vsc//modules/router"
  version = "0.0.6"
  # VM Which we can ssh to by default
  access_vm = module.SimpleVM.router_access
}
```
This will provide network connectivity for all the VMs in your project.
With the router, you can specify the **access VM**, being the VM exposed to the internet through ssh. It will also be the default target for [port forwarding rules](https://search.opentofu.org/module/hpcugent/opennebula/vsc/latest/submodule/router/inputs#port_forwards)

```{note}
There can only be **one** regular router per Opennebula group, except an optional VSC router.
```
:::{danger}
If your router is deleted (via `tofu destroy`, for example) your **public IP address** might change.
Avoid deleting your router(s), as we cannot manually assign/restore a specific IP to your project.
:::
#### Port Forwarding
You can open ports with the port-forwards block:
```
  port_forwards = {
    "http" = {
      external_port = 80
    }
    "https" = {
      external_port = 443
    }
  }
```
By default these will target the `access_vm`, but you can override `internal_ip`. For example, to add an ssh port for a second VM:
```
    "http_secondary" = { # Define a port forward rule for the second VM
      external_port = 51001
      internal_port = 22
      internal_ip   = module.Secondary.ip # For a VM module named "Secondary".
    }
```
```{tip}
`external_port` must be between 51001 and 59999 (Except for the vsc router)
```
```{warning}
Changing the port-forward rules will re-create the router VMs, so there may be a network interruption when the changes are applied.
```
### The VM
```{tip}
Full module documentation can be found [here](https://search.opentofu.org/module/hpcugent/opennebula/vsc/latest/)
```
```
module "SimpleVM" {
  source     = "hpcugent/opennebula/vsc"
  version    = "0.0.6"
  vm_name    = "SimpleExample"
  image_name = "Rocky 10"
  is_windows = false
}
```
This code will create a virtual machine with the `Rocky 10` OS image provided by us. You can see which other images are available either with the `oneimage list` command or at https://cloudpr4.ugent.be/fireedge/sunstone/image/.



## Advanced configuration
### Windows
```{tip}
We strongly encourage you to consider linux-based alternatives. Our support for Windows is more limited.
```
Setting `is_windows = true` will configure the VM slightly differently for Windows images.

### Full documentation
```{warning}
Be sure to match the version of the documentation/examples to the version of the module that you are using
```
The module has some examples which can be found on [Github](https://github.com/hpcugent/terraform-vsc-opennebula/tree/0.0.5/examples) 

You can also find documentation on all of the variables on the [OpenTofu Registry](https://search.opentofu.org/module/hpcugent/opennebula/vsc/latest)


## Deploying your VM

If you have followed the previous steps now you can init and deploy your
infrastucture to Tier-1 VSC cloud.

If you haven't deployed anything yet, you must first initialize the modules.

Move to your project directory first:

```shell
cd ~/MyProject
```
Edit the file as necessary (change the VM name to something descriptive, for example.):
```shell
nano main.tf
```
```{tip}
You can also edit the files through [HPC UGent dashboard](https://login.hpc.ugent.be/pun/sys/dashboard/files/)
```



Now you can run
```shell
tofu init
```
This command performs several different initialization steps in order to
prepare the current working directory for use with the module.

Next, we can inspect which changes tofu will apply:
```shell
tofu plan
```

You will see a list of the resources required to deploy your
infrastructure, tofu also checks if there is any systax error in
your code. Your infrastructure is not deployed yet, review the plan
and then just deploy it to VSC Tier-1 Cloud running:

```shell
tofu apply
```

OpenTofu will show your plan again and you will see this message:

```console
..
..
Do you want to perform these actions?
OpenTofu will perform the actions described above.
Only ’yes’ will be accepted to approve.
Enter a value:
```

Type **yes** and press enter and wait a few minutes. If
everything is correct and if you have enough quota OpenTofu will show
you a message after creating all the required resources.

```console
..
..
Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

Outputs:

services = {
  "Primary VM" = [
    "ssh root@193.190.80.2",
  ]
}
```

Your cloud infrastructure is ready to be used.

:::{tip}
If you forgot your VM's details, just run `tofu output`
If you make any changes to the template, just run `tofu apply` again.
If you add any new VMs, tofu will ask you to run `tofu init` again.
:::

:::{important}
It is important to keep a backup of opentofu files.

Opentofu generates several files in this directory to keep track of any
change in your infrastructure. If for some reason you lose these files, it will be very difficult to import them into a new OpenTofu configuration.
:::


## Special considerations for multi-user workflows
If multiple people need to interact with the project independently, there are some additional things to consider.
Because only one (or two, with VSC access) router can exist per project, the management of the router instance needs to be centralized in some way.

### Tofu state
OpenTofu uses a [statefile](https://opentofu.org/docs/v1.12/language/state/) to keep track of which resources have been created and their properties. This way, if you add another port forwarding to your router, OpenTofu knows which router to change and what changes to apply. This has the downside that anyone that needs to change the port forwarding rules, needs to have access to the statefile. The statefile may also contain sensitive information (like a password, in the case of a Windows VM), so it is important to keep this file secret. 

### Suggested workflows
#### One tofu project for all users
In this workflow, you share the tofu code and the statefile. You could do this on a shared filesystem, for example, if you are careful to avoid collosions (working on the files at the same time).
A safer way to do this is with a [Remote Backend](https://opentofu.org/docs/v1.12/language/settings/backends/configuration/) or [Cloud provider](https://opentofu.org/docs/v1.12/language/settings/tf-cloud/), that stores your backend remotely in a way that ensures no conflicts occur. This is often paired with git, to track changes to the code. There is a list of Remote state providers further down this article.
:::{note}
We recommend keeping your OpenTofu code in Git, but **do not put the statefile in a public repository**.
:::
#### One "router manager"
Alternatively, if you do not wish to use a remote state, you could have one person responsible for managing the router and the port-forwarding.
So you would create an OpenTofu project with just the router defintion, and than the other users in your team can create VMs in their own local OpenTofu projects. You would then have to add any port-forwardings to the router project, using the private ip address of the VM. 

### Remote State Providers
These online services offer [Remote state](https://opentofu.org/docs/v1.12/language/state/remote/) storage.
At the time of writing they offer free tiers. This list is non-exhaustive.
You can also use self-hosted options, s3, a postgres db etc. See the [OpenTofu Docs](https://opentofu.org/docs/v1.12/language/settings/backends/configuration/) for more information.

Some of these should be configured with the [Cloud block](https://opentofu.org/docs/v1.12/language/settings/tf-cloud/) and others the [Backend](https://opentofu.org/docs/v1.12/language/settings/backends/configuration/) block.
:::{Note}
(WIP) Of these I've only tested Gitlab so far.
:::

#### [Gitlab](https://docs.gitlab.com/user/infrastructure/iac/terraform_state/)
Gitlab offers free tofu state management with their repositories. There are also [CI/CD Components](https://gitlab.com/components/opentofu) if you want to integrate CI/CD into your workflow.
#### [HCP Terraform / Terraform Cloud](https://app.terraform.io/)
Hashicorp offers a free tier up to 500 managed resources, which should be enough for an average usecase. You can find the documentation on their pricing/limits [Here](https://developer.hashicorp.com/terraform/cloud-docs/overview).
:::{warning}
Terraform Cloud does not officially support OpenTofu, so we recommend only using it as a state provider and to not use any of their automation features (set execution mode to `remote`).
:::
#### [Scalr](https://scalr.com/)
Scalr also offers a free tier, limited to 50 runs per month (which can be avoided by setting the run mode to local).
Scalr is also compatible with OpenTofu, so their additional features can be used.

## Further customization
You can also use your own opentofu code to deploy your infrastructure.
This task is out of the scope of this document, please refer to official
OpenTofu documentation to add you own changes
<https://opentofu.org/docs/> or ask to VSC Cloud admins via email at
<cloud@vscentrum.be>.

