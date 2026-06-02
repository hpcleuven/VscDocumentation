.. _mindwell_quick_start:

Mindwell quick start guide
==========================

The KU Leuven / UHasselt Tier-2 cluster *Mindwell* is planned to enter
production around mid 2026. Mindwell contains thin nodes, large memory
nodes and GPU nodes.

.. note::

   All vsc3 users can now try out Mindwell for free by submitting
   jobs using the "lp_mindwell_pilot" credit account.

   Mindwell is planned to enter production on Monday June 15.
   From that point onwards, you will need to use your regular
   credit accounts to run on Mindwell.

Mindwell does not have separate login nodes and can be accessed from the
:ref:`Genius login nodes <tier2_login_nodes>`. Access through
:ref:`Open OnDemand <ood>` will be provided in the near future.

.. _running jobs on mindwell:

Running jobs on Mindwell
------------------------

There are several type of nodes in Mindwell: normal compute nodes, GPU nodes,
big memory nodes and nodes configured for interactive use.
The resource specifications for jobs have to be tuned to use these nodes properly.

In general, the maximum walltime for Mindwell jobs is 3 days (72 hours).
Only jobs submitted to the ``*_long`` partitions are allowed to have
walltimes up to 7 days (168 hours), as will be illustrated below.

Similar to Genius and wICE, Mindwell uses Slurm as the workload manager.
A Slurm jobscript for Mindwell will typically look like this:

::

    #!/bin/bash -l
    #SBATCH --clusters=mindwell
    #SBATCH --partition=...
    #SBATCH --time=...
    #SBATCH --nodes=...
    #SBATCH --ntasks-per-node=...
    #SBATCH --account=...

    module load ...

    ...

In case you are not yet familiar with Slurm and/or the Mindwell hardware
(including the new GPFS storage), you can find more information on the
following pages:

- :ref:`Mindwell hardware <mindwell hardware>`
- :ref:`Scratch storage (including GPFS) <leuven_scratch>`
- :ref:`Transferring data between Lustre and GPFS <leuven_lustre_gpfs_transfer>`
- Slurm jobs (basics): :ref:`running jobs` and :ref:`job_types`
- :ref:`Slurm jobs (advanced) <job advanced>`
- :ref:`Site-specific Slurm info <leuven_slurm_specifics>`

For information about compute credit accounts, see the
:ref:`Leuven accounting <accounting_leuven>` and
:ref:`KU Leuven credits <KU Leuven credits>` pages.

.. note::

   The examples given on this page only serve as illustrations.
   We expect that you adapt the number of nodes, tasks, cores, memory,
   walltime, ... depending on what your compute task requires.


.. _submit to mindwell compute node:

Submit to a regular compute node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submitting a 2-node job on the regular Granite Rapids compute nodes
(with 192 cores each) can be done like this::

   $ sbatch --account=lp_mindwell_pilot --clusters=mindwell \
            --nodes=2 --ntasks-per-node=192 --time=2:00:00 myjobscript.slurm

This will select the default partition (called ``batch_graniterapids``)
which is the one of interest here.

For jobs which need more than 3 days of walltime (up to maximum 7 days),
you need to submit to the ``batch_graniterapids_long`` partition instead.


.. _submit to mindwell interactive node:

Submit to the interactive partition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is also a small ``interactive`` partition intended for interactive work
(compiling software, post-processing, small-scale debugging, visualization,
...). This is typically done via interactive jobs, for example::

   # A short single-core job:
   $ srun --account=lp_mindwell_pilot --clusters=mindwell --partition=interactive \
           --ntasks=1 --time=01:00:00 --pty bash -l

   # A longer job with more cores, one GPU and X11 forwarding:
   $ srun --account=lp_mindwell_pilot --clusters=mindwell --partition=interactive \
          --ntasks-per-node=8 --gpus-per-node=1 --time=08:00:00 --x11 --pty bash -l

Users are allowed to request a maximum of 8 cores and one RTX 5000 'Ada' GPU,
for walltimes up to 16 hours.

.. note::

   It is also possible to submit interactive jobs to the other partitions
   (e.g. ``batch_graniterapids``, ``gpu_b200`` or ``bigmem``) in case
   you need more resources. For large amounts of compute resources, however,
   we recommend to use batch jobs since these will result in fewer idling
   resources compared to interactive jobs.

.. note::

   Jobs on the ``interactive`` partition do not consume any credits.

.. _submit to mindwell big memory node:

Submit to nodes with more memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mindwell nodes with 1.5 TiB of RAM are placed in the ``bigmem`` partition.
To select the maximum amount of memory per core (8 000 MB, which is also the
default), you can submit a job as follows::

   $ sbatch --account=lp_mindwell_pilot --clusters=mindwell --partition=bigmem \
            --nodes=2 --ntasks-per-node=192 --mem-per-cpu=8000M myjobscript.slurm


.. _submit to mindwell GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~

The nodes with B200 GPUs are located in the ``gpu_b200`` partition.
As for the other node types, the GPU nodes can be shared by different jobs
from different users but each job has exclusive access to its allocated cores
and GPU(s).

If you e.g. need one B200 GPU and two CPU cores::

   $ sbatch --account=lp_mindwell_pilot --clusters=mindwell --partition=gpu_b200 \
            --nodes=1 --ntasks=2 --gpus-per-node=1 myjobscript.slurm

You are free to request more GPU devices and/or CPU cores if needed,
but take note of the :ref:`limits on CPU resources per allocated GPU
<cpu_resource_limits_in_gpu_jobs>`).
