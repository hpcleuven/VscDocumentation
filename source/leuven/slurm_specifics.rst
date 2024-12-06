.. _leuven_slurm_specifics:

Site-specific Slurm info
========================

While the :ref:`Running jobs in Slurm <running jobs>` pages provide generic
information regarding Slurm, there are additional points to consider when
using Slurm on Tier-2 clusters hosted at KU Leuven.


Compute credits
---------------
When submitting a job, you need to provide a valid Slurm credit account holding
enough compute credits for the job using the ``-A/--account`` option.
For more information, please consult the following pages:

.. toctree::
   :maxdepth: 1

   ./credits
   ./slurm_accounting


.. _leuven_job_shell:

Job shell
---------
For batch jobs we strongly recommend to use ``#!/bin/bash -l`` as the shebang
at the top of your jobscript. The ``-l`` option (hyphen lowercase L) is needed
to make sure that your ``~/.bashrc`` settings get applied and the appropriate
:ref:`cluster module <cluster_modules>` gets loaded at the start of the job.
This is not strictly needed for interactive jobs: ``srun ... --pty bash``
and ``srun ... --pty bash -l`` will give essentially identical environments.

Note that we still discourage loading modules in your ``~/.bashrc`` file and
recommend to do that in your jobscripts instead (see also the
:ref:`Compiling software for wICE<wice_compilation>` paragraph for example).


.. _leuven_cluster_choice:

Cluster choice
--------------
Many Slurm commands (like `sbatch`, `srun`, `scontrol`, `squeue`, `scancel`,
...) accept a ``-M/--clusters`` option which selects one or more clusters.
The default value depends on where the command is executed (Genius for the
Genius compute nodes and login nodes; wICE for the wICE compute nodes).
This means that if you are connected to a (Genius) login node, you will need
to add ``-M wice`` in order to select wICE instead of Genius. Also note that
some of these commands (such as `squeue` and `sacct`) accept ``-M all`` which
selects all available clusters.

In order to avoid potential mistakes we have made the ``-M/--clusters`` option
mandatory when submitting jobs.


.. _leuven_job_monitoring:

Monitoring jobs
---------------

For monitoring or debugging jobs, you can look into the following Slurm tools:

* `scontrol <https://slurm.schedmd.com/scontrol.html>`__ to view Slurm
  configuration and state
* `squeue <https://slurm.schedmd.com/squeue.html>`__ to get information about
  jobs in the scheduling queue
* `sacct <https://slurm.schedmd.com/sacct.html>`__ to display information about
  finished jobs

.. note::

    Don't forget the ``-M/--clusters`` option for these commands, as mentioned
    in the :ref:`Cluster choice <leuven_cluster_choice>` paragraph.

For convenience, we provide the ``slurm_jobinfo`` tool, which runs and parses
output from the Slurm tools mentioned above into a format that is easier to
read. Simply use ``slurm_jobinfo <jobid>`` where ``<jobid>`` has to be replaced
by the 8-digit number that identifies your job.

For getting a compact overview of the current state of the cluster, execute
``slurmtop`` on any KU Leuven Tier-2 node. Use ``slurmtop --help`` to get to
know the functionality.


.. _leuven_environment_propagation:

Environment propagation
-----------------------

Slurm jobs start in a clean environment which corresponds to your login
environment, i.e. with only those additional variables that you defined in your
``~/.bashrc`` file (see also the :ref:`Job shell <leuven_job_shell>` paragraph
above). Environment variables that happen to be set in the session
from which you submit the job are not propagated to the job.

If needed you can modify this default behaviour with the
`--export option <https://slurm.schedmd.com/sbatch.html#OPT_export>`__.
When doing so, keep in mind that you will need to include the default minimal
environment as well. To e.g. pass an additional environment variable ``FOO``
with value ``bar``, use ``--export=HOME,USER,TERM,PATH=/bin:/sbin,FOO=bar``.


.. _leuven_slurm_mpi:

MPI applications
----------------

MPI launchers
^^^^^^^^^^^^^
We recommend to start MPI applications using the launcher that comes with
the MPI implementation (typically called ``mpirun``). The present Slurm
installation has not been configured with PMI support, which may cause
applications to hang when launched via ``srun``. The main use for ``srun``
on our clusters is to request an interactive job.

Intel MPI pinning
^^^^^^^^^^^^^^^^^
The Intel MPI library does not always play well with the Slurm scheduler.
Specifically, when launching a job from a compute node (for instance from
inside an interactive job), processes are not pinned correctly. This issue can
be overcome by setting the environment variable ``I_MPI_PIN_RESPECT_CPUSET=off``
or equivalently adding the option ``-env I_MPI_PIN_RESPECT_CPUSET=off`` to your
``mpirun`` command. To check that processes are pinned correctly to physical
cores, set the environment variable ``I_MPI_DEBUG=5`` to get more verbose
output. Note that this issue does not occur with the Open MPI library.


.. _gpu_compute_mode:

Setting the GPU compute mode
----------------------------

NVIDIA GPUs support multiple `compute modes
<https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-modes>`_.
By default, the compute mode is set to `Exclusive-process` on our clusters
(which is the best setting in the majority of cases), but you can choose
another compute mode at job submission time. This is done by making use of a
plugin for our Slurm job scheduler:

.. code-block:: shell

   $ sbatch --help
   ...
   Options provided by plugins:
   
         --gpu_cmode=<shared|exclusive|prohibited>
                                 Set the GPU compute mode on the allocated GPUs to
                                 shared, exclusive or prohibited. Default is
                                 exclusive

Submitting a batch job where you want to set the compute mode of your NVIDIA
GPU(s) to be `shared` can be done with:

.. code-block:: shell

   sbatch --export=ALL --gpu_cmode=shared jobscript.slurm

An interactive job can be launched as follows:

.. code-block:: shell

   srun --ntasks-per-node=9 --nodes=1 --gpus-per-node=1 --account=<YOUR_ACCOUNT> \
        --clusters=wice --time=01:00:00 --partition=gpu_a100 --gpu_cmode=shared \
        --pty /bin/bash -l

A few notes on this feature:

* To check the behaviour is as expected, execute ``nvidia-smi`` in your job.
* Runs with GPUs on multiple nodes are not supported. Contact the helpdesk if
  you think you have a use case where this would be necessary.
* The GPU compute mode does not apply when multi-instance GPU partitioning
  (MIG) is used. This is for instance the case on the wICE Slurm partition
  called ``interactive``. For jobs on that partition this feature is
  irrelevant.

.. _cpu_resource_limits_in_gpu_jobs:

CPU resource limits in GPU jobs
-------------------------------

Jobs sent to the ``gpu_*`` partitions are expected to only request a proportionate
amount of CPU resources. For example, a single-GPU job submitted to a partition
with 4 GPUs per node should only request up to 1/4th of the available
CPU cores and CPU memory. An overview of the maximal CPU resources
per GPU is provided in the table below.

.. list-table:: Available CPU cores and CPU memory per GPU
   :widths: 20 20 20 20
   :header-rows: 2

   * - Cluster
     - Partition(s)
     - Max Cores
     - Max Memory
   * -
     -
     -
     - (MiB)
   * - Genius
     - ``gpu_p100*``
     - 9
     - 45000
   * - Genius
     - ``gpu_v100*``
     - 4
     - 84000
   * - wICE
     - ``interactive``
     - 8
     - 60000
   * - wICE
     - ``gpu|gpu_a100``
     - 18
     - 126000
   * - wICE
     - ``gpu_h100``
     - 16
     - 187200

If a job requests more cores or memory per GPU than listed above, you will receive a
warining message.
In this case, please adjust the Slurm options accordingly for your future jobs.

As an example, suppose that you need two A100 GPUs for your calculation, with just
one core per GPU but with as much CPU memory as you can get.
Such a job can be submitted as follows:

.. code-block:: bash

   sbatch --account=lp_myproject --clusters=wice --partition=gpu_a100 \
          --nodes=1 --ntasks-per-node=2 --gpus-per-node=2 --mem=252000m \
          myjobscript.slurm

In practice, 18 CPU cores and 126000 MiB CPU memory will be allocated per GPU,
and no warning will be raised.

For more examples of valid GPU jobs, have a look at the
:ref:`Genius <genius_t2_leuven>` and :ref:`wICE <wice_t2_leuven>`
quickstart guides.

Aside from options such as ``--ntasks-per-node`` and ``--cpus-per-task``
(for CPU cores) and ``--mem`` and ``--mem-per-cpu`` (for CPU memory),
Slurm also offers options like ``--cpus-per-gpu`` and ``--mem-per-gpu``.
When using these options, make sure that the requested CPU cores
and CPU memory per GPU does not exceed the limits mentioned in the table above.
