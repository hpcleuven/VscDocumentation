.. _wice_t2_leuven:

wICE quick start guide
======================

:ref:`wICE <wice hardware>` is a KU Leuven/UHasselt Tier-2 cluster
which entered production in 2022. Aside from regular CPU nodes, wICE also
contains large memory nodes and GPU nodes.

wICE does not have separate login nodes and can be accessed either from the
:ref:`Genius login nodes <tier2_login_nodes>`, or from your web browser via the
:ref:`Open OnDemand <ood>` service.

.. _running jobs on wice:

Running jobs on wICE
--------------------

There are several type of nodes in the wICE cluster: normal compute nodes, GPU nodes,
big memory nodes and nodes configured for interactive use.
The resource specifications for jobs have to be tuned to use these nodes properly.

In general, the maximum walltime for wICE jobs is 3 days (72 hours).
Only jobs submitted to the ``*_long`` partitions are allowed to have
walltimes up to  7 days (168 hours), as will be illustrated below.

Similar to Genius, wICE uses Slurm as the workload manager.
A Slurm jobscript for wICE will typically look like this:

::

    #!/bin/bash -l
    #SBATCH --clusters=wice
    #SBATCH --partition=...
    #SBATCH --time=...
    #SBATCH --nodes=...
    #SBATCH --ntasks-per-node=...
    #SBATCH --account=...

    module load ...

    ...

In case you are not yet familiar with Slurm and/or the wICE hardware, you can find
more information on the following pages:

- :ref:`wICE hardware <wice hardware>`
- :ref:`Slurm jobs (basics) <running jobs>`
- :ref:`Slurm jobs (advanced) <job advanced>`
- :ref:`Site-specific Slurm info <leuven_slurm_specifics>`

For information about using and installing software on wICE (including Conda
environments), see the :ref:`advanced guide for wICE<wice_t2_leuven_advanced>`.

For information about compute credit accounts, see
:ref:`Leuven accounting <accounting_leuven>` and
:ref:`KU Leuven credits <KU Leuven credits>` pages.

.. note::

   The examples given on this page only serve as illustrations.
   We expect that you adapt the number of nodes, cores, memory, walltime, ...
   depending on what your compute task requires.

.. note::

   If you do not provide a walltime for your job, then a default walltime will
   be applied. This is 1 hour for all partitions, except for the ``*_debug``
   partitions where it is 30 minutes.

.. note::

   If you do not specify the number of tasks and cores per task for your job,
   then it will default to a single task running on a single core.


.. _submit to wice compute node:

Submit to a regular compute node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submitting a 2-node job on the regular IceLake compute nodes (with 72 cores
each) can be done like this::

   $ sbatch --account=lp_myproject --clusters=wice \
            --nodes=2 --ntasks-per-node=72 --time=2:00:00 myjobscript.slurm

This will select the default partition (called ``batch``) which is the
one containing these IceLake nodes. The ``batch_icelake`` partition is
equivalent to the ``batch`` one.

To use Sapphire Rapids nodes instead (mind the higher core count)::

   $ sbatch --account=lp_myproject --clusters=wice --partition=batch_sapphirerapids \
            --nodes=2 --ntasks-per-node=96 --time=2:00:00 myjobscript.slurm

For jobs which need more than 3 days of walltime (up to maximum 7 days),
you need to submit to the respective ``batch_long``/``batch_icelake_long``
or ``batch_sapphirerapids_long`` partitions instead.


.. _submit to wice interactive node:

Submit to the interactive partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is also a small ``interactive`` partition intended for interactive work
(compiling software, post-processing, small-scale debugging, visualization,
...). This is typically done via interactive jobs, for example::

   # A short single-core job:
   $ srun --account=lp_myproject --clusters=wice --partition=interactive \
           --ntasks=1 --time=01:00:00 --pty bash -l

   # A longer job with more cores, a GPU instance and X11 forwarding:
   $ srun --account=lp_myproject --clusters=wice --partition=interactive \
          --ntasks-per-node=8 --gpus-per-node=1 --time=08:00:00 --x11 --pty bash -l

Users are allowed to request a maximum of 8 cores, one A100 GPU instance
(equal to 1/7th of the physical device), for walltimes up to 16 hours.

.. note::

   It is also possible to submit interactive jobs to the other partitions
   (e.g. ``batch``, ``gpu`` or ``bigmem``) in case you need more resources.
   For large amounts of compute resources, however, we recommend to use
   batch jobs since these will result in fewer idling resources
   compared to interactive jobs.


.. _submit to wice big memory node:

Submit to nodes with more memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IceLake nodes with 2 TiB of RAM are placed in the ``bigmem`` partition.
To select the maximum amount of memory per core (28 000 MB, which is also the
default), you can submit a job as follows::

   $ sbatch --account=lp_myproject --clusters=wice --partition=bigmem \
            --nodes=2 --ntasks-per-node=72 --mem-per-cpu=28000M myjobscript.slurm

There is also one IceLake node with even more memory (8 TiB RAM) in the
``hugemem`` partition (defaulting to ``--mem-per-cpu=111900M``).


.. _submit to wice GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~

The nodes with A100 GPUs are located in the ``gpu_a100`` partition (the
``gpu`` partition also covers the same nodes). As for the other
node types, the GPU nodes can be shared by different jobs from different users
but each job has exclusive access to its allocated cores and GPU(s).

If you e.g. need one A100 GPU and two CPU cores::

   $ sbatch --account=lp_myproject --clusters=wice --partition=gpu_a100 \
            --nodes=1 --ntasks=2 --gpus-per-node=1 myjobscript.slurm

You are free to request more GPU devices and/or CPU cores if needed,
but take note of the :ref:`limits on CPU resources per allocated GPU
<cpu_resource_limits_in_gpu_jobs>`).

There are also nodes with H100 GPUs and AMD Genoa CPUs (4 GPUs and 64 cores
per node) which you can select via the ``gpu_h100`` partition, e.g.::

   $ sbatch --account=lp_myproject --clusters=wice --partition=gpu_h100 \
            --nodes=1 --gpus-per-node=1 myjobscript.slurm

For easier development and testing with a full GPU, also a ``gpu_a100_debug``
partition is available which accepts jobs with walltimes up to 1 hour,
e.g.::

   $ sbatch --account=lp_myproject --clusters=wice --partition=gpu_a100_debug \
            --nodes=1 --gpus-per-node=1 --time=00:10:00 \
            myjobscript.slurm

The node in this partition is of the same type as those in the ``interactive``
partition except that its A100 GPU is not divided into smaller instances. Note
that you can only have a single ``gpu_a100_debug`` job in the queue at any
time.
