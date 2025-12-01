.. _leuven_slurm_specifics:

Site-specific Slurm info
========================

While the :ref:`Running jobs in Slurm <running jobs>` pages provide generic
information regarding Slurm, there are additional points to consider when
using Slurm on Tier-2 clusters hosted at KU Leuven.


.. _leuven_compute_credits:

Compute credits
---------------
When submitting a job, you need to provide a valid Slurm credit account holding
enough compute credits for the job using the ``-A/--account`` option.
For more information, please consult the following pages:

* :ref:`KU Leuven credits`
* :ref:`accounting_leuven`


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


.. _leuven_job_memory:

CPU memory requirements
-----------------------
Each partition also defines a default amount of CPU memory that is provided
per allocated core. For e.g. the wICE `batch_sapphirerapids` partition
this amounts to 2500 MB (equivalent to the ``--mem-per-cpu=2500M`` Slurm
option). For all partitions except the `interactive` ones, this default amount
per core is furthermore equal to the *maximum* amount per core. You may
therefore request more memory per core if needed, but it will cause additional
cores to be allocated to your job. This is to ensure that memory is not
oversubscribed.

On the wICE `batch_sapphirerapids` partition, for example, you can get twice
as much memory per core by specifying ``--mem-per-cpu=5000M`` but the job will
then also require twice as many cores and cost twice as many credits.
Note that in this example the same also applies if you would only specify
``--mem-per-cpu=4000M`` because Slurm takes ``ceil(4000/2500) = 2``.

Also be careful with multipliers such as ``G``. If in the above example
you would specify ``--mem-per-cpu=5G``, you will be tripling the number of
cores (because ``ceil(5*1024/2500) = 3``).

Note that similar considerations apply for other CPU memory options such
as `--mem <https://slurm.schedmd.com/srun.html#OPT_mem>`__.

Finally, in case of doubt, see the :ref:`leuven_job_monitoring` paragraph for
tips on how to check your past jobs, as well as the
:ref:`sam-quote tool<leuven_job_cost_calculation>`.


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


.. _leuven_job_limits:

Job limits
----------
We set limits to the number of concurrent jobs that a user can have
(in any active state, i.e. pending plus running). If you reach this limit,
you will not be able to submit additional jobs. There may also be limits to the
total sum of resources that your running jobs can occupy. Slurm will not let
any of your pending jobs start if that would cause this limit to be exceeded.

These two limits have different values depending on which partitions are
involved, through so-called partition QoSs:

.. list-table:: Partitions and their QoS
   :widths: 10 10

   * - Partitions
     - Partition QoS
   * - ``*_debug``
     - ``debug``
   * - ``interactive``
     - ``interactive``
   * - ``*_long``
     - ``long``
   * - other partitions (e.g. ``batch``)
     - ``normal``

With the following command you can find out what those limits are::

   $ sacctmgr show qos debug,interactive,long,normal format=Name%20,MaxSubmitJobsPerUser%15,MaxTRESPerUser%30


.. _leuven_batch_job_header:

Batch job header
----------------
We have configured Slurm to print the values of important Slurm environment
variables at the start of the standard output of each batch job (such as
``SLURM_JOB_ID: ...``). These lines will not be present, however, if the batch
job was itself submitted from within another Slurm job.

For GPU jobs this output includes the
`SLURM_JOB_GPUS <https://slurm.schedmd.com/sbatch.html#OPT_SLURM_JOB_GPUS>`__
variable. Keep in mind that this value refers to the index (or indices)
of the GPU(s) that were allocated on the job's master node.
A value of ``0`` therefore means that the GPU device with index 0 got
allocated (not that the job did not get any GPUs).


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

Multi-node jobs with Intel MPI and SSH bootstrapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some packages such as Fluent will hang at startup when using multiple nodes.
In that case, try adding ``export -n I_MPI_HYDRA_BOOTSTRAP_EXEC_EXTRA_ARGS``
in your jobscript before the application gets launched.


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


.. _leuven_join_job:

Joining a job
-------------
For debugging purposes it can sometimes be useful to connect to one of the
compute nodes allocated to your job (for example to inspect its processes
using GDB). In such cases we recommend to 'join' the job as follows::

   $ srun -M <cluster> --jobid=<jobid> --overlap --pty bash -l

