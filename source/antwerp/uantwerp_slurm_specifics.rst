.. _uantwerp_slurm_specifics:

########################
Site-specific Slurm info
########################

.. seealso::
  For basic and advanced Slurm instructions, please see :ref:`Running jobs in Slurm <running jobs>` and :ref:`job advanced`.

  For more specific information on Slurm use on the UAntwerp clusters, 
  please see our :ref:`site-specific Slurm info<uantwerp_slurm_specifics>`.

While the :ref:`Running jobs in Slurm <running jobs>` and :ref:`job advanced`
pages provide basic and advanced information regarding Slurm, there are
additional points to consider when using Slurm on Tier-2 clusters hosted
at UAntwerpen.

.. _uantwerp_accounts:

**************
Using accounts
**************

Since the introduction of the project account system in March 2024, 
users need to specify a valid project account for each job.
This can be set using Slurm's  `-A/--account 
option <https://slurm.schedmd.com/sbatch.html#OPT_account>`__.

You can get a list of valid project accounts you are a member of using the 
``myprojectaccounts`` command.

.. _uantwerp_requesting_memory:

*****************
Requesting memory
*****************

When requesting memory, keep in mind that no swap space is available in
case your application runs out of memory. Swapping is disabled because the nodes
don't have drives suitable for the load caused by swapping and because swapping
is extremely detrimental to performance.


.. _uantwerp_requesting_nodes:

****************
Requesting nodes
****************

On UAntwerp clusters we ask to only use the ``-N/--nodes`` option to request
(and use) full nodes.

We furthermore ask to abstain
from the ``--nodes=<minimum number>-<maximum number>`` option without
consulting us first and discussing why it would make sense for your job.

.. _GPU computing UAntwerp:

***************
Requesting GPUs
***************

Users of the GPU compute nodes are expected to report back on their
experiences. We are most interested in users who can also compare with
running on regular nodes as we will use this information for future
purchase decisions.

Given that modern clusters tend to be built with nodes with 
even 4 or 8 GPUs, we would also like to learn from those users who can use only
a single GPU in a node what is restricting them to use multiple GPUs.

Starting jobs
=============

The GPU compute nodes are managed through a separate partition, so you will need
to explicitly specify it when submitting your job. We also configured the GPU
nodes as shared resources, so that two users could each get exclusive 
access to a single, dedicated GPU at the same time.

In total, three GPU partitions are available:

+----------------------------------+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| Cluster                          | Partition    |  Available nodes                                                                                                              |
+==================================+==============+===============================================================================================================================+
| :ref:`Vaughan<Vaughan hardware>` | ampere_gpu   | 2 nodes with 4 NVIDIA Tesla `A100 (Ampere) <https://www.nvidia.com/en-us/data-center/a100/>`_ 40 GB SXM4                      |
+                                  +--------------+-------------------------------------------------------------------------------------------------------------------------------+
|                                  | arcturus_gpu | 2 nodes with 2 AMD Instinct `MI100 (Arcturus) <https://www.amd.com/en/products/accelerators/instinct/mi100.html>`_  32 GB HBM2|
+----------------------------------+--------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Leibniz<Leibniz hardware>` | pascal_gpu   | 2 nodes with 2 NVIDIA Tesla `P100 (Pascal) <https://www.nvidia.com/en-us/data-center/tesla-p100/>`_ 16 GB HBM2                |
+----------------------------------+--------------+-------------------------------------------------------------------------------------------------------------------------------+

To submit a job on a GPU compute node belonging to a certain partition and get a single GPU, use the  ``sbatch`` command

.. code:: bash
   
    sbatch -p <partition> --gpus-per-node=1 <jobscript>

or add the lines

.. code:: bash
   
    #SBATCH -p <partition>
    #SBATCH --gpus-per-node=1

to your job script.

Using ``--gpus-per-node=2`` would give you access to 2 GPU cards on a GPU compute node.

The defaults for the pascal_gpu nodes are set to ``--cpus-per-gpu=14`` and ``walltime=1:00:00``, so
that with using only ``-p pascal_gpu --gpus=1`` you would get a single GPU for 1 hour and all
cores belonging to the CPU that is closest to that GPU. The Vaughan GPU nodes use a similar setup.

Note that the maximum wall time for GPU jobs is limited to **24 hours**, without exception.

Monitoring GPU nodes
====================

Monitoring of CPU use by jobs running on the GPU nodes can be done in
the same way as for regular compute nodes.

One useful command to monitor the use of the NVIDIA GPUs is ``nvidia-smi``. It
will show information on both GPUs in the GPU node, and among others
lets you easily verify if the GPUs are used by the job.
The AMD GPUs can be monitored similarly using the ``rocm-smi`` command.

.. _uantwerp_environment_propagation:

***********************
Environment propagation
***********************

Slurm jobs start in a clean environment which corresponds to your login
environment, i.e. with only those additional variables that you defined in your
``~/.bashrc`` file. Environment variables that happen to be set in the session
from which you submit the job are not propagated to the job.

If needed you can modify this default behaviour with the
`--export option <https://slurm.schedmd.com/sbatch.html#OPT_export>`__.

|Example| To pass an additional environment variable ``FOO``
with value ``bar``, use ``--export=FOO=bar``.

.. note::
  The default minimal environment for a job is ``HOME,USER,TERM,PATH=/bin:/sbin``.
  
  These variables are added to the export options automatically.

