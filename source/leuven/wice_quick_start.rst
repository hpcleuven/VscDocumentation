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

The maximum walltime for any job on wICE regular nodes is 7 days (168 hours). Job requests with walltimes between 3 and 7 days are not allowed to run on big memory, interactive, GPU nodes.

wICE cluster uses different workload manager than Genius: Slurm instead of Torque+Moab. More information about converting pbs scripts and commands into Slurm can be found :ref:`here <Antwerp Slurm_convert_from_PBS>`

.. _submit to wice compute node:

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
The submission will occur from login nodes of Genius cluster, therefore you need to always remember to specify the cluster you need to use. 

To submit to a compute node you need to provide the required number of nodes and cores. For example to request 2 nodes with each 72 cores for 2 hours you can submit like this::

   $ sbatch --cluster=wice --nodes=2 --ntasks-per-node=72 --time=2:00:00  -A lp_myproject  myjobscript.slurm
  

Submit a long job to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
To submit to a compute node a job longer than 3 days you need to request a separate partition:

::

   $ sbatch --cluster=wice --nodes=2 --ntasks-per-node=72 --time=6-16:00:00 –-partition=batch_long -A lp_myproject  myjobscript.slurm


.. _submit to wice interactive node:

Submit to an interactive partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The interactive nodes are located in a separate partition. The users are allowed to request maximum of 8 cores for maximum walltime of 16 hours. In case of these nodes it is important to use then in interactive way (so not submittiong the script) and specyfying the requirements, for example:

::

   $ srun -n 1 -t 01:00:00 -A lp_myproject --partition=interactive --cluster=wice --pty bash –l

If a GPU is necessary for the visualization process - it can be requested (max 1 GPU per max 8 cores and max 16 hours). The available GPU is a single A100, but split in 7 'virtual' GPU's. Additionaly, X11 forwarding should be on:

::

   $ srun -N 1 -t 16:00:00 --ntasks-per-node=8 --gpus-per-node=1 -A lp_myproject -p interactive --cluster=wice --x11 --pty bash -l


.. _submit to wice big memory node:

Submit to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The big memory nodes are also located in a separate partition. In case of the big memory nodes it is also important to add your memory requirements (the maximum of memory per core that can be requested is 28GB/core), for example:

::

   $ sbatch –-cluster=wice --time=01:00:00 --nodes=2 --ntasks-per-node=72 --partition=bigmem --mem-per-cpu=20G --account=lp_myproject myjobscript.slurm


.. _submit to wice GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~
The GPU nodes are also located in a separate cluster partition so you will need to explicitly specify it when submitting your job. We also configured the GPU nodes as shared resources, meaning that different users can simultaneously use a portion of the same node. However every user will have exclusive access to the number of GPUs requested. If you want to use only 1 GPU of type A100 you can submit for example like this:

::

   $ sbatch --cluster=wice -A lp_myproject -N 1 --ntasks=18 --gpus-per-node=1 --partition=gpu myjobscript.slurm
  
Note that in case of 1 GPU you have to request 18 cores. In case you need more GPUs you have to multiply the 18 cores with the number of GPUs requested, so in case of for example 3 GPUs you will have to specify this:

::

   $ sbatch --cluster=wice -A lp_myproject -N 1 --ntasks=54 --gpus-per-node=3 --partition=gpu myjobscript.slurm

