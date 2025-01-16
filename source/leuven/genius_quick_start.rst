.. _genius_t2_leuven:

Genius quick start guide
========================
:ref:`Genius <Genius hardware>` is one of the two KU Leuven/UHasselt Tier-2 clusters,
besides :ref:`wICE <wice hardware>`.
Given the architectural diversity of compute nodes on Genius, this cluster is suited
for most HPC workloads.

Access to the cluster
---------------------

Genius can be accessed from the :ref:`Genius login nodes <tier2_login_nodes>`, or from your web browser via the :ref:`Open On-Demand <ood_t2>` service.

For example, you can log in to any of the login node using SSH::

   $ ssh vscXXXXX@login.hpc.kuleuven.be

.. _running_jobs_on_genius:

Running jobs on Genius
----------------------
Genius is equipped with regular (thin) compute nodes, two kinds of big memory nodes,
and GPU nodes.  The resource specifications for jobs have to be tuned to use these
nodes properly.

The `Slurm Workload Manager <https://slurm.schedmd.com>`_ is the scheduler,
resource manager and credit accounting manager on Genius (and wICE).

In case you are not yet familiar with Slurm and/or the Genius hardware, you can find
more information on the following pages:

- :ref:`Genius hardware <Genius hardware>`
- :ref:`Slurm jobs (basics) <running jobs>`
- :ref:`Slurm jobs (advanced) <job advanced>`
- :ref:`Site-specific Slurm info <leuven_slurm_specifics>`


.. _submit_genius_batch:

Submitting to a regular compute node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The regular (thin) compute nodes are gathered in the default ``batch`` partition.
This partition allows jobs with maximum 3 days of walltime. Jobs which require a
walltime up to maximum 7 days need to be submitted to the ``batch_long`` partition
instead.

Submitting a regular compute job boils down to specifying the required number of
nodes, cores-per-node, memory and walltime. You may e.g. request two full nodes like
this::

   $ sbatch --account=lp_myproject --clusters=genius --time=2:00:00 --nodes=2 \
            --ntasks-per-node=36 myjobscript.slurm

You may also request only a part of the resources on a node.
For instance, to test a multi-threaded application which performs optimally using 4 cores,
you may submit your job like this::

   $ sbatch --account=lp_myproject --clusters=genius --time=2:00:00 --ntasks=4 myjobscript.slurm
   # or
   $ sbatch --account=lp_myproject --clusters=genius --time=2:00:00 --ntasks=1 \
            --cpus-per-task=4 myjobscript.slurm

.. note::

   Please bear in mind to not exceed the maximum allowed resources on compute
   nodes for the targeted partition. E.g. you can request at most 36 cores per
   node (``--ntasks=36``). In general, we advise you to only request as many
   resources as needed by your application.

.. note::

   If you do not provide a walltime for your job, then a default walltime will
   be applied. This is 1 hour for all partitions, except for the debug partitions
   where it is 30 minutes (see :ref:`submit_genius_debug` below).

.. note::

   If you do not specify the number of tasks and cores per task for your job,
   then it will default to a single task running on a single core.

.. note::

   Each partition also has a default amount of memory that is provided for
   every allocated core. For e.g. the `batch` partition, this is 5000 MB,
   which corresponds to the ``--mem-per-cpu=5000M`` Slurm option.
   You may choose higher values if your application requires more memory
   than what is provided by default. When doing so, keep in mind that e.g.
   specifying ``--mem-per-cpu=10G`` will be interpreted as a request for
   10240 MB and not 10000 MB.


Advanced node usage
^^^^^^^^^^^^^^^^^^^
The ``batch(_long)`` partitions used to contain both Skylake and Cascadelake
nodes, which meant that ``--constraint=skylake|cascadelake``-like options
were needed when you wanted to ensure that your job runs on a specific type
of node. As the Skylake nodes from this partitions have been decommissioned,
only the Cascadelake nodes remain and ``--constraint=skylake`` no longer works.

By default, all nodes are shared among all jobs and users, unless the resource specifications
would imply an exclusive access to a node by a job or user.


.. _submit_genius_interactive:

Submit to the interactive partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is also a small ``interactive`` partition intended for interactive work
(compiling software, post-processing, small-scale debugging, visualization,
...). This is typically done via interactive jobs, for example::

   # A short single-core job:
   $ srun --account=lp_myproject --clusters=genius --partition=interactive \
           --ntasks=1 --time=01:00:00 --pty bash -l

   # A longer job with more cores and X11 forwarding:
   $ srun --account=lp_myproject --clusters=genius --partition=interactive \
          --ntasks-per-node=8 --time=08:00:00 --x11 --pty bash -l

Users are allowed to request a maximum of 8 cores for walltimes up to 16 hours.
Note that the nodes in this partition do not contain GPUs. The ``ìnteractive``
partition on wICE is therefore better suited if you need GPU acceleration for
e.g. data visualization.

.. note::

   It is also possible to submit interactive jobs to the other partitions
   (``batch``, ``gpu_v100``, ``bigmem``, ...) in case you need more resources.
   For large amounts of compute resources, however, we recommend to use
   batch jobs since these will result in fewer idling resources
   compared to interactive jobs.


.. _submit_genius_gpu:

Submitting to a GPU node
~~~~~~~~~~~~~~~~~~~~~~~~
The GPU nodes are accessible via the following partitions:

+---------------+----------+----------------------------------------+-------------+
| Partition     | Walltime | Resources                              | CPU model   |
+===============+==========+========================================+=============+
| gpu_p100      | 3 days   | 20 nodes, 4x Nvidia P100 GPUs per node | Skylake     |
+---------------+----------+                                        |             |
| gpu_p100_long | 7 days   |                                        |             |
+---------------+----------+----------------------------------------+-------------+
| gpu_v100      | 3 days   | 2 nodes, 8x Nvidia V100 GPUs per node  | Cascadelake |
+---------------+----------+                                        |             |
| gpu_v100_long | 7 days   |                                        |             |
+---------------+----------+----------------------------------------+-------------+

Similar to the other nodes, the GPU nodes can be shared by different jobs from
different users.
However, every user will have exclusive access to the number of GPUs requested.
If you want to use only 1 GPU of type P100 you can submit for example like this::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=1 --ntasks=9 \
            --gpus-per-node=1 --partition=gpu_p100 myjobscript.slurm

Note that in case of 1 GPU you have to request 9 cores.
In case you need more GPUs you have to multiply the 9 cores with the number of GPUs
requested, so in case of for example 3 GPUs you will have to specify this::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=1 --ntasks=27 \
            --gpus-per-node=3 -p gpu_p100 myjobscript.slurm

To specifically request V100 GPUs, you can submit for example like this::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=1 --ntasks=4 \
            --gpus-per-node=1 --mem-per-cpu=20000M --partition=gpu_v100 myjobscript.slurm

For the V100 type of GPU, it is required that you request 4 cores for each GPU.
Also notice that these nodes offer a much larger amount of CPU memory.


.. _submit_genius_bigmem:

Submitting to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The big memory nodes are located in the ``bigmem`` and ``bigmem_long`` partitions.
In case of the big memory nodes it is also important to add your memory requirements,
for example::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=1 --ntasks=36 \
            --mem-per-cpu=20000M --partition=bigmem myjobscript.slurm


.. _submit_genius_amd:

Submitting to an AMD node
~~~~~~~~~~~~~~~~~~~~~~~~~
The AMD nodes are accessible via the ``amd`` and ``amd_long`` partitions.
Besides specifying the partition, it is also important to note that the default memory
per core in this partition is 3800 MB, and each node contains 64 cores.
For example, to request two full nodes::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=2 --ntasks-per-node=64 \
            --partition=amd myjobscript.slurm


.. _submit_genius_debug:

Running debug jobs
------------------
Debugging on a busy cluster can be taxing due to long queue times.
To mitigate this, two Cascadelake CPU nodes and a Skylake GPU node have been
reserved for debugging purposes. To use these debug nodes, you have to select
the ``batch_debug`` or ``gpu_p100_debug`` partition, respectively.

A few restrictions apply to a debug job:

- it can only use at most two nodes for CPU jobs, a single node for GPU jobs
- its walltime is at most 1 hour
- you can only have a single debug job in the queue at any time.

To run a debug job for 20 minutes on two CPU nodes, you would use::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=2 --ntasks-per-node=36 \
            --partition=batch_debug --time=20:00 myjobscript.slurm

To run a debug job for 15 minutes on a GPU node, you would use::

   $ sbatch --account=lp_my_project --clusters=genius --nodes=1 --ntasks=9 \
            --gpus-per-node=1 --partition=gpu_p100_debug --time=15:00 myjobscript.slurm
