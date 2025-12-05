.. _genius_t2_leuven:

Genius quick start guide
========================

:ref:`Genius <genius hardware>` is a KU Leuven/UHasselt Tier-2 cluster
which entered production in 2018. Currently only its login nodes and most of
its GPU nodes remain in production.

Access to the cluster
---------------------

Genius can be accessed from the :ref:`Genius login nodes <tier2_login_nodes>`,
or from your web browser via the :ref:`Open OnDemand <ood>` service.

For example, you can log in to any of the login node using SSH::

   $ ssh vscXXXXX@login.hpc.kuleuven.be

.. _running_jobs_on_genius:

Running jobs on Genius
----------------------
The `Slurm Workload Manager <https://slurm.schedmd.com>`_ is the scheduler,
resource manager and credit accounting manager on Genius (and wICE).

In case you are not yet familiar with Slurm and/or the Genius hardware,
you can find more information on the following pages:

- :ref:`Genius hardware <Genius hardware>`
- :ref:`Slurm jobs (basics) <running jobs>`
- :ref:`Slurm jobs (advanced) <job advanced>`
- :ref:`Site-specific Slurm info <leuven_slurm_specifics>`

.. note::

   The examples given on this page only serve as illustrations.
   We expect that you adapt the number of nodes, cores, memory, walltime, ...
   depending on what your compute task requires.

.. _submit_genius_gpu:

Submitting to a GPU node
~~~~~~~~~~~~~~~~~~~~~~~~
The GPU nodes are accessible via the following partitions:

+---------------+----------+----------------------------------------+-------------+
| Partition     | Walltime | Resources                              | CPU model   |
+===============+==========+========================================+=============+
| gpu_p100      | 3 days   | 14 nodes, 4x Nvidia P100 GPUs per node | Skylake     |
+---------------+----------+                                        |             |
| gpu_p100_long | 7 days   |                                        |             |
+---------------+----------+----------------------------------------+-------------+
| gpu_v100      | 3 days   | 2 nodes, 8x Nvidia V100 GPUs per node  | Cascadelake |
+---------------+----------+                                        |             |
| gpu_v100_long | 7 days   |                                        |             |
+---------------+----------+----------------------------------------+-------------+

As usual, GPU nodes can be shared by different jobs from different users.
However, every user will have exclusive access to its allocated GPUs.

If you e.g. want to get one P100 GPU and two CPU cores::

   $ sbatch --account=lp_myproject --clusters=genius --partition=gpu_p100 \
            --nodes=1 --ntasks=2 --gpus-per-node=1 myjobscript.slurm

For a V100 GPU, select the `gpu_v100` partition instead. Note that these nodes
also offer :ref:`a much larger amount of CPU memory <Genius hardware>`.

You are free to request more GPU devices and/or CPU cores if needed,
but take note of the :ref:`limits on CPU resources per allocated GPU
<cpu_resource_limits_in_gpu_jobs>`).

For easier development and testing, also a ``gpu_p100_debug`` partition is
available which accepts jobs with walltimes up to 1 hour. Note that you can
only have a single debug job in the queue at any time.
