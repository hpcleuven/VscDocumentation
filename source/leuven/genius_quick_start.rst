.. _genius_t2_leuven:

Genius quick start guide
========================

:ref:`Genius <Genius hardware>` is one of the two KU Leuven/UHasselt Tier-2 clusters,
besides :ref:`wICE <wice hardware>`. 
Given the architectural diversity of compute nodes on Genius, this cluster is suited  
for most HPC workloads.

Access to the cluster
---------------------

Access to Genius follows the common :ref:`access guidelines for KU Leuven/UHasselt Tier-2 clusters <tier2_login_nodes>`. 
  
For example, you can log in to any of the login node using SSH::

   $ ssh vscXXXXX@login.hpc.kuleuven.be

.. _running jobs on genius:

Running jobs on Genius
----------------------

Genius is equipped with normal (thin) compute nodes, two kinds of large memory nodes,
and GPU nodes.  The resources specifications for jobs have to be tuned to use these 
nodes properly.

In case you are not yet familiar with the system, you can find more
information on

- :ref:`hardware specification <Genius hardware>`
- :ref:`submitting jobs using Slurm <running jobs>` and the :ref:`advanced topics <job advanced>`
- :ref:`obtaining credits <KU Leuven credits>` and :ref:`Slurm accounting <accounting_leuven>`

The default ``batch`` partition allows jobs with maximum 3 days of walltime.
Jobs which require a walltime up to maximum 7 days must be submitted to the 
``batch_long`` partition explicitly.

The `Slurm Workload Manager <https://slurm.schedmd.com>`_ is the scheduler, resource manager and 
accounting manager on Genius (and wICE).
To get started with Slurm, you may refer to our documentation on  
:ref:`running jobs` and :ref:`job advanced` usage.

.. _submit to genius compute node:

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
Submitting a compute job boils down to specifying the required number of nodes, cores-per-node, memory and walltime.
You may e.g. request two full nodes like this::

   $ sbatch -A lp_myproject -M genius -t 2:00:00 --nodes=2 --ntasks-per-node=36 myjobscript.slurm

You may also request only a part of the resources on a node.
For instance, to test a multi-threaded application which performs optimally using 4 cores, you may submit your job like this::

   $ sbatch -A lp_myproject -M genius -t 2:00:00 --ntasks=4 myjobscript.slurm
   # or
   $ sbatch -A lp_myproject -M genius -t 2:00:00 --ntasks=1 --cpus-per-task=4 myjobscript.slurm

.. note::

   Please bear in mind to not exceed the maximum allowed resources on compute nodes for the targeted partition.
   E.g. you can request at most 36 cores per node (``--ntasks=36``). 
   In general, we advise you to only request as much resources as needed by your application.

.. note::

   By default, each job will use a single core on a single node for a duration of 1 hour.
   In other words, these default values are implicitly applied 
   ``--nodes=1 --ntasks=1 --mem-per-cpu=5000M --time=1:00:00``.

Advanced node usage
^^^^^^^^^^^^^^^^^^^
In certain cases (such as performance tests) you may want to be sure that your job runs 
on a specific type of node (i.e. only Skylake nodes or only Cascadelake nodes). 
You can do this by additionally specifying ``--constraint=skylake|cascadelake``.
Otherwise, your job will land on the first available node(s) as decided by Slurm.

By default, all nodes are shared among all jobs and users, unless the resource specifications
would imply an exclusive access to a node by a job or user.

.. _submit to genius GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~
The GPU nodes are accessible via different partitions.
The table below summarizes all the possibilities:

+---------------+----------+----------------------------------------+-------------+
| Partition     | Walltime | Resources                              | CPU model   |
+===============+==========+========================================+=============+
| gpu_p100      | 3 days   | 20 nodes, 4x Nvidia P100 GPUs per node | Skylake     |
| gpu_p100_long | 7 days   |                                        |             |
+---------------+----------+----------------------------------------+-------------+
| gpu_v100      | 3 days   | 2 nodes, 8x Nvidia V100 GPUs per node  | Cascadelake |
| gpu_v100_long | 7 days   |                                        |             |
+---------------+----------+----------------------------------------+-------------+


Similar to the other nodes, the GPU nodes can be shared by different jobs from 
different users.
However every user will have exclusive access to the number of GPUs requested. 
If you want to use only 1 GPU of type P100 you can submit for example like this::

   $ sbatch -A lp_my_project -M genius -N 1 -n 9 --gpus-per-node=1 -p gpu_p100 myjobscript.slurm
  
Note that in case of 1 GPU you have to request 9 cores. 
In case you need more GPUs you have to multiply the 9 cores with the number of GPUs 
requested, so in case of for example 3 GPUs you will have to specify this::

   $ sbatch -A lp_my_project -M genius -N 1 -n 27 --gpus-per-node=3 -p gpu_p100 myjobscript.slurm

To specifically request V100 GPUs, you can submit for example like this::

   $ sbatch -A lp_my_project -M genius -N 1 -n 4 --gpus-per-node=1 --mem-per-cpu=20G -p gpu_v100 myjobscript.slurm
  
For the V100 type of GPU, it is required that you request 4 cores for each GPU. 
Also notice that these nodes offer a much larger memory bank.


.. _submit to genius big memory node:

Submit to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The big memory nodes are hosted by the ``bigmem`` and ``bigmem_long`` partitions. 
In case of the big memory nodes it is also important to add your memory requirements, 
for example::

   $ sbatch -A lp_my_project -M genius -N 1 -n 36 --mem-per-cpu=20G -p bigmem myjobscript.slurm

.. _submit to genius AMD node:

Submit to an AMD node
~~~~~~~~~~~~~~~~~~~~~

The AMD nodes are accessible via the ``amd`` and ``amd_long`` partitions.
Besides specifying the partition, it is also important to note that the default memory
per core in this partition is 3800 MB, and each node offers maximum 64 cores. 
For example, to request two full nodes::

   $ sbatch -A lp_my_project -M genius -N 2 --ntasks-per-node=64 -p amd myjobscript.slurm 


Running debug jobs
------------------
Debugging on a busy cluster can be taxing due to long queue times.
To mitigate this, two Skylake CPU nodes and a Skylake GPU node have been reserved 
for debugging purposes.
To use these debug nodes, you have to select the ``batch_debug`` or ``gpu_p100_debug`` 
partition, respectively.

A few restrictions apply to a debug job:

- it can only use at most two nodes for CPU jobs, a single node for GPU jobs
- its walltime is at most 30 minutes
- you can only have a single debug job in the queue at any time.

To run a debug job for 20 minutes on two CPU nodes, you would use::

   $ sbatch -A lp_my_project -M genius -N 2 --ntasks-per-node=36 -p batch_debug -t 20:00 myjobscript.slurm

To run a debug job for 15 minutes on a GPU node, you would use::

   $ sbatch -A lp_my_project -M genius -N 1 -n 9 --gpus-per-node=1 -p gpu_p100_debug -t 15:00 myjobscript.slurm
