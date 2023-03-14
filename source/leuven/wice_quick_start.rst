.. _wice_t2_leuven:
========================
wICE quick start guide
========================

:ref:`wICE <wice hardware>` is the most recent KU Leuven/UHasselt Tier-2 cluster.  It can be used for most workloads, and has nodes with a lot of memory, as well as nodes with GPUs.

It does not have separate login nodes and can be accessed from the :ref:`Genius login nodes <genius_login_nodes>`

.. _running jobs on wice:

Running jobs on wICE
----------------------

There are several type of nodes in the wICE cluster: normal compute nodes, GPU nodes, big memory nodes and nodes configured for interactive use. The resources specifications for jobs have to be tuned to use these nodes properly.

In general, the maximum walltime for wICE jobs is 3 days (72 hours). Only jobs submitted to the ``batch_long`` partition are allowed to have walltimes up to 7 days (168 hours), as will be illustrated below.

The wICE cluster uses a different workload manager than Genius: Slurm instead of Torque+Moab. More information about converting pbs scripts and commands into Slurm can be found :ref:`here <Antwerp Slurm_convert_from_PBS>`. A Slurm jobscript for wICE will typically look like this:

::
   
    #!/bin/bash -l
    #SBATCH --cluster=wice
    #SBATCH --partition=...
    #SBATCH --time=...
    #SBATCH --nodes=...
    #SBATCH --ntasks-per-node=...
    #SBATCH --account=...

    module use /apps/leuven/icelake/2021a/modules/all
    module load ...

    ...

For more information on using and installing software on wICE, see the :ref:`advanced guide for wICE<wice_t2_leuven_advanced>`.


.. _submit to wice compute node:

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
In these examples, the submission will be done from login nodes of the Genius cluster, therefore you need to always remember to specify the cluster you want to use.

To submit to a compute node you need to provide the required number of nodes and cores. For example to request 2 nodes with each 72 cores for 2 hours you can submit like this::

   $ sbatch --cluster=wice --nodes=2 --ntasks-per-node=72 --time=2:00:00  -A lp_myproject  myjobscript.slurm
   
More information about accounting used on wice can be found :ref:`here <accounting_leuven>`.

Submit a long job to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To submit to a compute node a job longer than 3 days you need to request a separate partition:

::

   $ sbatch --cluster=wice --nodes=2 --ntasks-per-node=72 --time=6-16:00:00 --partition=batch_long -A lp_myproject  myjobscript.slurm


.. _submit to wice interactive node:

Submit to the interactive partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The interactive nodes are located in a separate partition. The users are allowed to request a maximum of 8 cores for a maximum walltime of 16 hours. These nodes are intended for interactive use. Instead of submitting a job script, you open an interactive session on a compute node as follows:

::

   $ srun -n 1 -t 01:00:00 -A lp_myproject --partition=interactive --cluster=wice --pty bash -l

If a GPU is necessary for the visualization process, it can be requested (max 1 GPU and max 8 cores for at most 16 hours). The available GPU is a single A100 which has been split in 7 GPU instances (one of which will be allocated to your job). Additionally, X11 forwarding should be enabled:

::

   $ srun -N 1 -t 16:00:00 --ntasks-per-node=8 --gpus-per-node=1 -A lp_myproject -p interactive --cluster=wice --x11 --pty bash -l

.. note::

   The interactive partition is intended for relatively lightweight interactive work, such as compiling software, running small preprocessing scripts, small-scale debugging, or visualization. This is the reason why the amount of resources you can get in a job is limited on the interactive partition. In case you must do heavy computational work in an interactive way, it is also possible to submit interactive jobs to the other partitions. For instance suppose you need to debug a program using more than 8 cores. In that case you can use the command above to run an interactive job, changing the partition to ``batch``, ``gpu``, or ``bigmem`` and adapting the resources as needed.  Do note that in general it is recommended to run heavy computational work in a script which you run as a batch job (so without opening an interactive terminal on the compute node).

.. _submit to wice big memory node:

Submit to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The big memory nodes (2048GB of RAM) are also located in a separate partition. In case of the big memory nodes it is also important to add your memory requirements (the maximum of memory per core that can be requested is 28000MB/core), for example:

::

   $ sbatch --cluster=wice --time=01:00:00 --nodes=2 --ntasks-per-node=72 --partition=bigmem --mem-per-cpu=28000M --account=lp_myproject myjobscript.slurm


.. _submit to wice GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~
The GPU nodes are also located in a separate cluster partition so you will need to explicitly specify it when submitting your job. We also configured the GPU nodes as shared resources, meaning that different users can simultaneously use a portion of the same node. However every user will have exclusive access to the number of GPUs requested. If you want to use only 1 GPU of type A100 you can submit for example like this:

::

   $ sbatch --cluster=wice -A lp_myproject -N 1 --ntasks=18 --gpus-per-node=1 --partition=gpu myjobscript.slurm
  
Note that in case of 1 GPU you have to request 18 cores. In case you need more GPUs you have to multiply the 18 cores with the number of GPUs requested, so in case of for example 3 GPUs you will have to specify this:

::

   $ sbatch --cluster=wice -A lp_myproject -N 1 --ntasks=54 --gpus-per-node=3 --partition=gpu myjobscript.slurm
