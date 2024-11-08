# Orchestration Using Terraform
:::{warning}
In November 2024, the terraform templates have been significantly rewritten. Should you be using an older version of the templates, you can find the old version of the documentation [here](https://github.com/hpcleuven/VscDocumentation/blob/cb0d48a0132677a6a70282bb0bf0444208420f69/source/cloud/terraform.md).
:::
HashiCorp Terraform <https://www.terraform.io/> is an
infrastructure as code tool (IaC). Users can deploy a data center
infrastructure using a declarative configuration language known as
HashiCorp Configuration Language (HCL), or using JSON.
Terraform has
some advantages over OpenStack Heat service. It is has a simple syntax, it
can provision virtual infrastructures across multiple cloud providers
(not only OpenStack) and it provides important features like network port forwarding rules (see
[floating-ip](configure_instances.md#floating-ip-addresses)).
Terraform is
currently one of the most popular infrastructure automation tools
available. VSC Cloud also provides some template examples that could be
used to deploy virtual infrastructures within VSC Tier-1 Cloud in an
automated way
(<https://github.com/hpcugent/openstack-templates/tree/master/terraform>).

**Terraform**
The client is available for different Operating Systems like Windows, Linux
or macOS (<https://www.terraform.io/downloads>) but it is also available
from UGent login node _login.hpc.ugent.be_.

## Create application credentials for Terraform

Terraform
uses OpenStack application credentials to authenticate to VSC Cloud
Tier-1 public API. It is a good practice to generate a new application
credential just to be used with Terraformframework. The process is the same
described in section
[application credentials](access.md#application-credentials).

:::{note}
Make sure you download the new application credential as yaml file
instead of openRC.
:::

At this point you should have a _clouds.yaml_ text file with these lines:

```bash
# This is a clouds.yaml file, which can be used by OpenStack tools as a source
# of configuration on how to connect to a cloud. If this is your only cloud,
# just put this file in ~/.config/openstack/clouds.yaml and tools like
# python-openstackclient will just work with no further config. (You will need
# to add your password to the auth section)
# If you have more than one cloud account, add the cloud entry to the clouds
# section of your existing file and you can refer to them by name with
# OS_CLOUD=openstack or --os-cloud=openstack
clouds:
  openstack:
    
    auth:
      
      auth_url: https://cloud.vscentrum.be:13000
      
      application_credential_id: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      application_credential_secret: "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
    
      
        
    region_name: "regionOne"
        
      
    interface: "public"
    identity_api_version: 3
    auth_type: "v3applicationcredential"

```

As the file comments state, you should copy the current clouds.yaml to
your VSC login node **$HOME** _login.hpc.ugent.be:
~/.config/openstack/clouds.yaml_, or locally if you have installed
Terraform in
your own laptop or computer. Terraform will use this file to authenticate to
OpenStack API automatically.

## Getting Terraform examples

You can connect to UGent login node `login.hpc.ugent.be` to use
terraform. Login to the login node with your VSC account first:

```shell
ssh -A vscxxxxx@login.hpc.ugent.be
```

If this is the first time using Terraform, download the VSC Terraform
examples from github from
<https://github.com/hpcugent/openstack-templates>:

```shell
git clone https://github.com/hpcugent/openstack-templates
```

Make sure you have *`~/.config/openstack/clouds.yaml`* available from
the login node (see previous [section](#create-application-credentials-for-terraform)).

:::{warning}
Do not share your application's credential file `clouds.yaml` or put this
file in a public place.
:::

```shell
chmod 600 ~/.config/openstack/clouds.yaml
```

## Terraform modules
:::{tip}
If you are **not** using the VSC login node, you need to make sure to:
1) [Install Terraform](https://developer.hashicorp.com/terraform/install)
2) Install openstack client:
    * Ubuntu: `sudo apt install python3-openstackclient`
    * [RHEL/CentOS](https://docs.openstack.org/install-guide/environment-packages-rdo.html)
    * [Others](https://docs.openstack.org/ocata/user-guide/common/cli-install-openstack-command-line-clients.html)
:::
We've provided two examples of how to use the terraform modules.

Navigate to the environment directory first:

```shell
cd ~/openstack-templates/terraform/environment
```

### Basic VM configuration
This module deploys one VM with a public IP address and can be configured with extra options
Copy the `single.tf.example` code to the `main.tf` file like so:
```shell
cat single.tf.example >> main.tf
```

The file now contains the definition for one VM with several options you can customize:
| variable      | explanation | Possible values
----------------|-------------|----
| vm_name       | Sets the name of the virtual machine. | (string)
| image_name    | Sets the operating system image for the machine. | See [Image list](https://cloud.vscentrum.be/dashboard/project/images)
| flavor_name   | Sets the machine flavor. | see [Flavors list](flavors.md).
| nginx_enabled | Installs nginx and exposes port 80. | true, false
| nfs_network   | Connects the vm to the NFS network. See [NFS_Share](#terraform_share) Only set true if you requested access  | true, false |
| vsc_enabled   | Connects the vm to the VSC network. Only set true if you requested access. | true, false |
| is_windows | Configures windows-specific behavior if `true` | true/false |

More advanced options are described further on. 

## Deploy Terraform templates

If you have followed the previous steps now you can init and deploy your
infrastucture to Tier-1 VSC cloud.

If you haven't deployed any template yet, you need to initiate terraform:

Move to environment directory first:

```shell
cd ~/openstack-templates/terraform/environment
```

This command performs several different initialization steps in order to
prepare the current working directory for use with Terraform:

```shell
terraform init
```

Now you can check and review your Terraform plan, from the same
directory:

```shell
terraform plan
```

You will see a list of the resources required to deploy your
infrastructure, Terraform also checks if there is any systax error in
your templates. Your infrastructure is not deployed yet, review the plan
and then just deploy it to VSC Tier-1 Cloud running:

```shell
terraform apply
```

Terraform will show your plan again and you will see this message:

```console
..
..
Do you want to perform these actions?
Terraform will perform the actions described above.
Only ’yes’ will be accepted to approve.
Enter a value:
```

Type **yes** and press enter and wait a few seconds or minutes. If
everything is correct and if you have enough quota Terraform will show
you a message after creating all the required resources.

```console
..
..
Apply complete! Resources: 6 added, 0 changed, 0 destroyed.

Outputs:

MyVM = "SSH: ssh -A -p 56315 rocky@193.190.80.3"
```

:::{tip}
Usually the username (rocky/ubuntu/...) will be provided by `terraform output`. If you forget or are not sure what username to use, just connect with `root` and a message will appear telling you the correct user.
:::
For a cluster it might look like this:
```
..
..

Outputs:

cluster = <<EOT
Main:
SSH: ssh -A -p 59619 rocky@193.190.80.3

Private:
Note: SSH to main server first
MyCluster-private-0:
 SSH: ssh -A rocky@10.113.1.135
MyCluster-private-1:
 SSH: ssh -A rocky@10.113.1.229
MyCluster-private-2:
 SSH: ssh -A rocky@10.113.1.213

EOT
```
:::{tip}
To access your private VMs you need to ssh to your public VM first, then ssh from your public vm to your private VMs.
:::
Your cloud infrastructure is ready to be used.

:::{tip}
If you forgot your VM's details, just run `terraform output`
If you make any changes to the template, just run `terraform apply` again.
:::

:::{tip}
It is important to keep a backup of your terraform directory, specially
all the files within the environment directory:
`~/openstack-templates/terraform/environment`
:::



Terraform generates several files in this directory to keep track of any
change in your infrastructure. If for some reason you lost or remove
these files you will not able to modify or change the current Terraform
plan (only directly from OpenStack).


:::{warning}
Do not remove or modify the `port_something_ssh.json` files. These keep track of the external ports used. Deleting them _will_ break Terraform.
:::
## Automated variables
The terraform templates include the ability to automatically adapt your VM based on certain variables.
This is accomplished by installing scripts on the VM when it is first created.
It requires ssh access to the VM.

These features can be disabled by setting `scripts_enabled=false`.

:::{tip}
Automated variables will not work if you started using the templates before November 2024
Set `scripts_enabled=false` or contact us for assistance.
They also do not work if `public=false`.
:::
### Nginx
`nginx_enabled` will automatically install nginx and start the service.
It will also expose ports `80` and `443`, or two random ports if `alt_http = true`.
### Volumes
If you set `automount = true` on a volume (see [Volumes](#volumes)), volumes will automatically be mounted at `/mnt/volname` and will have a filesystem created. Size changes will result in the filesystem being automatically resized.

### Private VMs
You can also deploy a public VM and multiple private VMs (without a public IP) by defining multiple instance modules and setting `public = false` on the private VMs.
You can then reach those VMs through your public VMs with ssh-agent forwarding (`ssh -A`). See `frontend_backend_nfs.example` for a complete example.

### Advanced variables
There's some extra variables you can configure:
| Variable | Explanation | Values
|---|---|---|
| access_key | the name of the ssh key you want to associate with the vm/cluster | (string)
| userscript | A shell script that is executed when the VM is first created. | (string) |
| project_name | The name VSC of the project you want to create the resurce in | VSC_XXXX |
| alt_http | Use randomly generated ports for http instead of port 80/443 | true/false (default false)|
| public | Add a public IP if true | true/false (default true) |
| custom_secgroup_rules | A list of security group rules | map of objects (see [Firewall](#firewall) ) |
| volumes | A list of extra volumes | map of objects (see [Volumes](#volumes)) |
| cloud_init | Cloud-init "part" to execute when the VM is first created |[cloud-init terraform part](https://registry.terraform.io/providers/hashicorp/cloudinit/latest/docs/data-sources/config#nested-schema-for-part) |
| nfs_size | DEPRECATED, use nfs_share module | (Gigabytes) |
| scripts_enabled | Enables/disables optional ansible scripts | true/false (default true)|
| vsc_ip | Manually set a VSC floating ip | ip address (default null)|
| rootdisk_size | Manually sets the size of the rootdisk, overriding the flavor settings | (Gigabytes)

(volumes)=
#### Volumes
if you need large amounts of storage and don't want to use an NFS share, you can instead attach an additional block-storage volume with the `volumes` variable (see `volume.example`).
The `size` represents the volume size in gigabytes.
:::{tip}
This variable will create and attach the volume as a regular disk, but it will **not** create a filesystem or mount it. New versions of the template support `automount = true`, see [automount](#automount).
:::
```hcl
volumes = {
  vol1 = {
    size = 100
  }
}
```
(automount)=
##### Automount
The module supports automatically creating a filesystem, mounting it and resizing it as necessary.
It adds these arguments to `volumes`:
| Variable | Explanation | Values |
| --- | --- | --- |
| automount | Automatically create a filesystem and mount it | true/false|
| filesystem | Sets the filesystem to be created | see [here](https://docs.ansible.com/ansible/latest/collections/community/general/filesystem_module.html#parameter-fstype) (default: "ext4") |
(firewall)=
#### Firewall
With the single VM module you can add open ports to the VM. 
These wont export ports to the internet by default. but it will allow other VMs to connect to that port. 
See the `custom_secgroup.example` file for an example.
You can set `expose = true` for a particular port and terraform will select a random external port to forward to your chosen local port:
```hcl
  custom_secgroup_rules = { 
    node_exporter = {
      port = 9100
      protocol = "tcp"
      remote_ip_prefix = "0.0.0.0/0"
      expose   = true
    }
  }
```
Will output something like:
```text
MyVM = <<EOT
SSH: ssh -A -p 51274 rocky@193.190.80.3

node_exporter 9100 -> 193.190.80.3:51273
EOT
```
:::{tip}
Be sure to add the subnet to the `remote_ip_prefix`, and note that this rule does not support individual IPs.
:::
:::{warning}
Exposing ports to the internet is potentially dangerous. Make sure that the application you're exporting is properly secured.
:::
(terraform_share)=
## NFS Share
:::{tip}
In order to use NFS shares, you need to request access.
Your VM(s) must also be connected to the NFS network with `nfs_network=true`
:::
The latest templates include a module to easily configure an NFS share.
```hcl
module "nfs-share" {
  source = "../modules/nfs_share"
  name = "MyShare"
  size = 30 #Size in gigabytes
}
```
By default the NFS share only allows access from your project's NFS subnet.
You can add additional access rules with the `access_rules` variable:
```hcl
  access_rules = [
    { 
      access_level = "rw", #optional
      access_to = "0.0.0.0/0"
      access_type = "ip" #optional
    },
    {
      access_to = "10.122.148.0/24"
      access_level = "ro"
    }
  ]
```
Terraform will then output the path to the share:
```
nfs-share = "10.131.35.194:/volumes/_nogroup/12b329db-b301-4d15-qbwd-9439e545210a"
```
:::{warning}
Setting custom rules disables the default rule.
:::
You can also modify and add more resources for the current templates.
This task is out of the scope of this document, please refer to official
Terraform documentation to add you own changes
<https://www.terraform.io/docs> or ask to VSC Cloud admins via email at
<cloud@vscentrum.be>.
