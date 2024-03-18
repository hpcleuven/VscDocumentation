# Orchestration Using Terraform

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

Terraform
client is available for different Operating Systems like Windows, Linux
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

We've provided two examples of how to use the terraform modules.

navigate to the environment directory first:

```shell
cd ~/openstack-templates/terraform/environment
```

### Single VM(s)
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
| nfs_enabled   | Connects the vfm to the NFS network. Only set true if you requested access. | true, false
| vsc_enabled   | Connects the vfm to the VSC network. Only set true if you requested access. | true, false

More advanced options are described further on.
### Cluster of VMs
You can also deploy a public VM and multiple private VMs (without a public IP) in one go by using the cluster template:
```shell 
cat cluster.tf.example >> main.tf
```
The customization options are similar to the single vm template:
| Variable | Explanation
|--|--|
| private count | How many private instances you want |
| public_flavor | The flavor for the public instances (and private instances by default)|
| public_image | The OS image for the public instances (and private instances by default)|
| cluster_name | The basename for the vms. Public instance will be called `MyCluster-public` and private instances `MyCluster-private-x` |

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
To access your private VMs you need to ssh to your public VM first, then ssh from your main vm to your private VMs.
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
Do not remove or modify the port_something_ssh.json files. These keep track of the external ports used. Deleting them _will_ break Terraform.
:::
## Making changes to module variables
### Adding NFS Or Nginx
:::{tip}
If you enabled these options upon initial creation of the VM, you don't have to do these steps
:::

If you added NFS or Nginx after initial creation, you need to run a script **on your openstack VM** to mount the NFS volume or install nginx, respectively.

First ssh to your instance. You can get the command with
```shell
terraform output
```
Then run the command you got from terraform.
After connecting to your instance, run:
```shell
curl http://169.254.169.254/2009-04-04/user-data | sudo bash
```
### Advanced variables
There's some extra variables you can configure:
| Variable | Explanation | Values
|---|---|---|
| access_key | the name of the ssh key you want to associate with the vm/cluster | (string)
| playbook_url | A url to an ansible playbook that gets applied when nginx_enabled = true | (string) |
| project_name | The name VSC of the project you want to create the resurce in | VSC_XXXX |
| nfs_size | Size of the NFS share if nfs_enabled=true | (number) |

#### Single VM only
| Variable | Explanation | Values |
| --- | --- | --- |
| public | Add a public IP if true | true/false|
#### Cluster only
| Variable | Explanation | Values |
| --- | --- | ---|
| private_image | Sets a different OS name for the private VMs | See `OS_CLOUD=openstack openstack image list |
| private_flavor | Sets a different flavor for the private VMs | see `OS_CLOUD=openstack openstack flavor list` |
| public_nginx_enabled | enables nginx on the public instance | true/false |
| public_vsc_enabled | Connects the public vm to the VSC network. Only set true if you requested access | true/false |


You can also modify and add more resources for the current templates.
This task is out of the scope of this document, please refer to official
Terraform documentation to add you own changes
<https://www.terraform.io/docs> or ask to VSC Cloud admins via email at
<cloud@vscentrum.be>.
