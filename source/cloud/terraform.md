# Orchestration Using Terraform
HashiCorp Terraform <https://www.terraform.io/> is an
infrastructure as code tool (IaC). Users can deploy a data center
infrastructure using a declarative configuration language known as
HashiCorp Configuration Language (HCL)..
Terraform is currently one of the most popular infrastructure automation tools
available. VSC Cloud also provides some template examples that could be
used to deploy virtual infrastructures within VSC Tier-1 Cloud in an
automated way
(<https://github.com/hpcugent/openstack-templates/tree/master/terraform>).

**Terraform**
The client is available for different Operating Systems like Windows, Linux
or macOS (<https://www.terraform.io/downloads>) but it is also available
from UGent login node _login.hpc.ugent.be_.

## Create application credentials for Terraform

Terraform uses OpenStack application credentials to authenticate to VSC Cloud
Tier-1 public API. It is a good practice to generate a new application
credential just to be used with Terraformframework. The process is the same
described in section
[application credentials](access.md#application-credentials).

:::{important}
Make sure you download the new application credential as yaml file
instead of openRC.
:::

At this point you should have a _clouds.yaml_ text file with these lines:

```yaml
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

```{important}
You should copy the current clouds.yaml to
your VSC login node (login.hpc.ugent.be) `$HOME/.config/openstack/clouds.yaml`, or locally if you have installed
Terraform on your own computer. Terraform will use this file to authenticate to OpenStack API automatically.
```
:::{tip}
You can easily access and edit the files on the login node by going to the [HPC UGent dashboard](https://login.hpc.ugent.be/pun/sys/dashboard/files/). 
**Enable "Show Dotfiles"** to see the `.config` directory.

You can also access the commandline of the login node there (under `Clusters` dropdown).
:::
## Getting Terraform examples

You can connect to UGent login node `login.hpc.ugent.be` to use
terraform. Login to the login node with your VSC account first:

```shell
ssh -A vscxxxxx@login.hpc.ugent.be
```
:::{important}
It is important to forward your ssh agent with `-A` when SSH-ing to the login node.
:::
If this is the first time using the templates, download the VSC Terraform
examples from github from
<https://github.com/hpcugent/openstack-templates>:

```shell
git clone https://github.com/hpcugent/openstack-templates
```

Make sure you have *`~/.config/openstack/clouds.yaml`* available from
the login node (see previous [section](#create-application-credentials-for-terraform)).

:::{danger}
Do not share your application credential file (`clouds.yaml`) or put this
file in a public place.
:::

```shell
chmod 600 ~/.config/openstack/clouds.yaml
```

:::{tip}
If you want to use the `openstack` CLI, you need to set the `OS_CLOUD` environment variable.
This command will ensure that it will be set automatically the next time you open a terminal:
```shell
export OS_CLOUD=openstack
echo "export OS_CLOUD=openstack" >> ~/.bashrc
```
**You only need to run this command once**.
This is only required for the CLI, not for terraform.
:::

## Basic VM configuration
:::{tip}
If you are **not** using the VSC login node, you need to make sure to:
1) [Install Terraform](https://developer.hashicorp.com/terraform/install)
2) Install openstack client:
    * Ubuntu: `sudo apt install python3-openstackclient`
    * [RHEL/CentOS](https://docs.openstack.org/install-guide/environment-packages-rdo.html)
    * [Others](https://docs.openstack.org/ocata/user-guide/common/cli-install-openstack-command-line-clients.html)
:::
We've provided examples of how to use the terraform modules in the `examples/` directory.

Navigate to the environment directory first:

```shell
cd ~/openstack-templates/terraform/environment
```

The `single.tf.example` deploys one VM with a public IP address and can be configured with extra options
Copy the `single.tf.example` code to the `main.tf` file like so:
```shell
cat examples/single.tf.example >> main.tf
```

The file now contains the definition for one VM with several options you can customize:
| variable      | explanation | Possible values
----------------|-------------|----
| vm_name       | Sets the name of the virtual machine. | string |
| image_name    | Sets the operating system image for the machine. | See [Image list](https://cloud.vscentrum.be/dashboard/project/images) |
| flavor_name   | Sets the machine flavor. | see [Flavors list](flavors.md). |
| nginx_enabled | Installs nginx and exposes ports 80 and 443 (See {ref}`tf_automated`)  | true/false |
| nfs_network   | Connects the vm to the NFS network (Does not create a share). (See [NFS_Share](#terraform_share))Only set true if you requested access  | true/false |
| vsc_enabled   | Connects the vm to the VSC network. Only set true if you requested access. | true/false |
| is_windows | Configures windows-specific behavior if `true` | true/false |

More advanced options are described further on. 
(tf_automated)=
## Automated variables
The terraform templates include the ability to automatically adapt your VM based on certain variables.
This is accomplished by installing scripts on the VM when it is first created.
It requires ssh access to the VM.

These features can be disabled by setting `scripts_enabled=false`.
### Nginx
`nginx_enabled` will automatically install nginx and start the service.
It will also expose ports `80` and `443`, or two random ports if `alt_http = true`.
### Volumes
If you set `automount = true` on a volume (see [Volumes](#volumes)), volumes will automatically be mounted at `/mnt/volname` and will have a filesystem created. Size changes will result in the filesystem being automatically resized.

(volumes)=
## Volumes
if you need large amounts of storage and don't want to use an NFS share, you can instead attach an additional block-storage volume with the `volumes` variable (see `examples/vm_with_volumes.tf.example`).
The `size` represents the volume size in gigabytes.
:::{note}
This variable will create and attach the volume as a regular disk, but it will **not** create a filesystem or mount it unless you set `automount = true`.
:::
```hcl
volumes = {
  vol1 = {
    size = 100
  }
}
```
(automount)=
### Automount
The module supports automatically creating a filesystem, mounting it and resizing it as necessary.
It adds these arguments to `volumes`:
| Variable | Explanation | Values |
| --- | --- | --- |
| automount | Automatically create a filesystem and mount it | true/false|
| filesystem | Sets the filesystem to be created | see [here](https://docs.ansible.com/ansible/latest/collections/community/general/filesystem_module.html#parameter-fstype) (default: "ext4") |
(terraform_share)=
## NFS Share
The templates include a module to easily configure an NFS share.
You can find an example of this in `examples/vm_with_share.tf.example`
:::{tip}
In order to use NFS shares, you need to request access.
Your VM(s) must also be connected to the NFS network with `nfs_network=true`
:::
```hcl
module "nfs-share" {
  source = "../modules/nfs_share"
  name = "MyShare"
  size = 30 #Size in gigabytes
}
```
Terraform will then output the path to the share:
```
nfs-share = "10.131.35.194:/volumes/_nogroup/12b329db-b301-4d15-qbwd-9439e545210a"
```
### Advanced NFS settings
:::{dropdown} Access rules
By default the NFS share only allows access from your project's NFS subnet, which will work for most usecases.
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
```{warning}
Setting custom rules disables the default rule.
```
:::

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

Type **yes** and press enter and wait a few minutes. If
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
Depending on the options you've added/enabled, the output may contain additional info
```
..
..

Outputs:

MyVM = <<EOT
SSH: ssh -A -p 53594 rocky@193.190.80.3
HTTP: http://193.190.80.3:52159 (HTTPS :57773)
VSC: 172.24.49.6
EOT
```

Your cloud infrastructure is ready to be used.

:::{tip}
If you forgot your VM's details, just run `terraform output`
If you make any changes to the template, just run `terraform apply` again.
:::

:::{important}
It is important to keep a backup of your terraform directory, specially
all the files within the environment directory:
`~/openstack-templates/terraform/environment`

Terraform generates several files in this directory to keep track of any
change in your infrastructure. If for some reason you lost or remove
these files you will not able to modify or change the current Terraform
plan (only directly from OpenStack).
:::



:::{warning}
Do not remove or modify the `port_something_ssh.json` files. These keep track of the external ports used. Deleting them _will_ break Terraform.
:::

## Private VMs
If you don't need/want a VM to be exposed to the internet, you can set the `public` variable to `false`.
You can then reach those VMs through your public VM(s) with ssh-agent forwarding (`ssh -A`). See `examples/frontend_backend.tf.example` for a complete example.
:::{note}
Private VMs do not support {ref}`tf_automated`
:::
## Advanced variables
There's some extra variables you can configure:
| Variable | Explanation | Values
|---|---|---|
| access_key | the name of the ssh key you want to associate with the vm/cluster | string |
| userscript | A shell script that is executed when the VM is first created. | string |
| rootdisk_size | Manually sets the size of the rootdisk, overriding the flavor settings | Gigabytes |
| ssh_user | Override default ssh user (necessary for custom images) | (string) (default "root") |
| persistent_root | Makes the rootdisk persistent (will not be destroyed when the VM resource is destroyed) | true/false (default false) |
| public | Add a public IP if true | true/false (default true) |
| floatingip_address | Manually define the public floating IP, in case the project has more than one | ip address (default null) |
| custom_secgroup_rules | A list of security group rules | map of objects (see [Firewall](#firewall) ) |
| volumes | A list of extra volumes | map of objects (see [Volumes](#volumes)) |
| cloud_init | Cloud-init "part" to execute when the VM is first created |[cloud-init terraform part](https://registry.terraform.io/providers/hashicorp/cloudinit/latest/docs/data-sources/config#nested-schema-for-part) |
| alt_http | Use randomly generated ports for http instead of port 80/443 | true/false (default false)|
| nfs_size | DEPRECATED, use nfs_share module | Gigabytes |
| scripts_enabled | Enables/disables optional ansible scripts | true/false (default true) See {ref}`tf_automated`|
| vsc_ip | Manually set a VSC floating ip | ip address (default null)|
| project_name | The name VSC of the project you want to create the resource in | VSC_XXXX |

(firewall)=
### Firewall
On a public VM, these ports will be open and exposed to the internet by default:
* A random ssh port
* If `nginx_enabled=true`:
  * Port 80/443
  * 2 random ports if `http_enabled=true`

You may need to open more ports, either within the vm network or exposed to the internet.
You can add extra port forwarding rules through the `custom_secgroup_rules` variable.
See the `/examples/custom_secgroup.tf.example` file for an example.

:::{dropdown} Opening ports
```{note}
Ports will not be exposed to the internet by default, but it will allow other VMs to connect to that port.
```
```hcl
  custom_secgroup_rules = { 
    node_exporter = {
      port = 9100
      protocol = "tcp"
      remote_ip_prefix = "0.0.0.0/0"
    }
  }
```
```{important}
Be sure to add the subnet to the `remote_ip_prefix`, and note that this rule does not support individual IPs.
```
:::

:::{dropdown} Exposing ports to the internet
You can set `expose = true` for a particular port and terraform will select a random external port to forward to your chosen local port.
It is also possible to choose an external port manually, between the range of 51001-59999, by setting `external_port = portnumber`.
This port must also be unique for your public floating IP. 
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
```{important}
Be sure to add the subnet to the `remote_ip_prefix`, and note that this rule does not support individual IPs.
```

```{warning}
Exposing ports to the internet is potentially dangerous. Make sure that the application you're exporting is properly secured.
```

:::
## Further customization
You can also modify and add more resources for the current templates.
This task is out of the scope of this document, please refer to official
Terraform documentation to add you own changes
<https://www.terraform.io/docs> or ask to VSC Cloud admins via email at
<cloud@vscentrum.be>.

## Troubleshooting
This section describes some common errors you may encounter.
If this section does not help you, don't hesitate to contact <cloud@vscentrum.be> for help.

:::{dropdown} A duplicate port forwarding entry with same attributes already exists
If you get the error:
```
│ Error: Error creating openstack_networking_portforwarding_v2: Bad request with: [POST https://cloud.vscentrum.be:13696/v2.0/floatingips/64f2705c-43ec-4bdf-864e-d18fee013e3f/port_forwardings], error message: {"NeutronError": {"type": "BadRequest", "message": "Bad port_forwarding request: A duplicate port forwarding entry with same attributes already exists, conflicting values are {'floatingip_id': '64f2705c-43ec-4bdf-864e-d18fee013e3f', 'external_port': 80, 'protocol': 'tcp'}.", "detail": ""}}
```
This means that a different VM in your project is already using port 80 and/or 443.
You can have multiple VMs with `nginx_enabled=true` by setting `alt_http=true` for that particular VM.
:::
:::{dropdown} remote-exec provisioner error
If you get the error:
```
│ Error: remote-exec provisioner error
│ 
│   with module.MyVMExample.null_resource.testconnection[0],
│   on ../modules/single_instance/ansible.tf line 17, in resource "null_resource" "testconnection":
│   17:   provisioner "remote-exec" {
│ 
│ interrupted - last error: SSH authentication failed (rocky@193.190.80.3:51307): ssh: handshake failed: ssh: unable to authenticate, attempted methods [none], no
│ supported methods remain
```
Then terraform is unable to SSH to your instance. There are a couple of possible reasons:
* You are on a login node but have not forwarded your ssh-agent with `ssh -A`
  * If you have, check if your ssh-agent is configured correctly
* You do not have ssh access to this VM/it was created with the wrong keypair
  * Ask whoever does have access to add your ssh public key to the VM
  * If this is a new VM and it is using the wrong keypair, use the [Advanced Variable](#advanced-variables) `access_key` to set the correct one.

```{tip}
You can also set `scripts_enabled=false` if you do not want any [convenience scripts](#automated-variables) or if there is no better solution
```

Feel free to contact us <cloud@vscentrum.be> for help.
:::

:::{dropdown} Failed to upload script: please login as the user...
If you get the error:
```
│ Error: remote-exec provisioner error
│
│   with module.RS-GPU[0].null_resource.testconnection[0],
│   on ../modules/single_instance/ansible.tf line 17, in resource
"null_resource" "testconnection":
│   17:   provisioner "remote-exec" {
│
│ Failed to upload script: please login as the user "ubuntu" rather than
the user "root".
```
Terraform is using the wrong user to connect to your VM. This can happen if you're using your own OS image.
You can set the correct user with the `ssh_user` variable.
:::

:::{dropdown} (Web UI) "You are not allowed to start instance..."
If you powered off a VM it is possible that it was automatically _shelved_ to conserve resources (see [Difference between suspend, pause...](launch_instance.md#difference-between-suspend-pause-shelve-shut-off-delete)).

If you try and start a `shelved, offloaded` VM in the web dashboard, you will get the error `You are not allowed to start instance....`.

You must first use the dropdown menu to unshelve the vm. Then it will be started automatically. Alternatively, you can run `terraform apply` again, which will set the vm to `active`.

:::
