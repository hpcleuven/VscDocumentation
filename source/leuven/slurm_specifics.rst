.. _leuven_slurm_specifics:

Site-specific Slurm info
========================

While the :ref:`Running jobs in Slurm <running jobs>` pages provide generic
information regarding Slurm, there are additional points to consider when
when using Slurm on Tier-2 clusters hosted at KU Leuven.


Compute credits
---------------
When submitting a job, you need to provide a valid Slurm credit account holding
enough compute credits for the job using the ``-A/--account`` option.
For more information, please consult the following pages:

.. toctree::
   :maxdepth: 1

   ./credits
   ./slurm_accounting


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

    Our Slurm scheduler is aware of multiple clusters and ``wice`` is not the
    default one. As a consequence, any Slurm command (such as `scontrol`,
    `squeue`, `sacct`) needs to be executed with the option ``--clusters=wice``
    (or ``-M wice`` in short) in order to get information for the wICE cluster.

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
``~/.bashrc`` file. Environment variables that happen to be set in the session
from which you submit the job are no longer propagated to the job.

If needed you can modify this default behaviour with the
`--export option <https://slurm.schedmd.com/sbatch.html#OPT_export>`__.
When doing so, keep in mind that you will need to include the default minimal
environment as well. To e.g. pass an additional environment variable ``FOO``
with value ``bar``, use ``--export=HOME,USER,TERM,PATH=/bin:/sbin,FOO=bar``.

Note that we still discourage loading modules in your ``~/.bashrc`` file and
recommend to do that in your jobscripts instead (see also the
:ref:`Compiling software for wICE<wice_compilation>` paragraph).


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
        --clusters=wice --time=01:00:00 --partition=gpu --gpu_cmode=shared \
        --pty /bin/bash -l

A few notes on this features:

* To check the behaviour is as expected, execute ``nvidia-smi`` in your job.
* Runs with GPUs on multiple nodes are not supported. Contact the helpdesk if
  you think you have a use case where this would be necessary.
* The GPU compute mode does not apply when multi-instance GPU partitioning
  (MIG) is used. This is for instance the case on the wICE Slurm partition
  called ``interactive``. For jobs on that partition this feature is
  irrelevant.


.. _known_issues:

Known issues
------------

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
