# GPUs

For GPU workloads, VSC Cloud provides NVIDIA L40S GPUs.

## Attaching a GPU to your instance

In order to deploy a VM with a GPU, you must use a different template from the default.
With the OpenTofu Module, this can be accomplished by setting `template = "UserL40"`.

## Restrictions and limitations

* A VM may only have 1 GPU at a time
* If we have to migrate your VM due to regular maintenance of the platform, it will have to be shut down and restarted
