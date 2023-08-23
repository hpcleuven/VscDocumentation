.. _wice_t2_leuven_advanced:

===================
wICE advanced guide
===================

.. _wice_compilation:

Compiling software
------------------

The wICE compute nodes feature Intel processors nicknamed IceLake, which are
the successors of the SkyLake and CascadeLake architectures which you can find
on Genius. Although architectural differences are rather small, it is highly
recommended to compile a version of your code specifically for wICE. Since the
operating system (Rocky Linux) differs from the one on Genius (CentOS), a
separate compilation is strictly required in most cases anyway. A good approach
to compile on a wICE node is to launch an interactive job.

Many dependencies you might need are centrally installed. The modules that are
optimized for wICE are available in ``/apps/leuven/icelake/2021a/modules/all``.
This directory has to be in the ``$MODULEPATH`` environment variable in order
to make those modules available. Normally this should happen automatically, but
in case of problems it is a good idea to check this. If for some reason it is
missing, it can be added by executing:

::

    $ module use /apps/leuven/icelake/2021a/modules/all

Note that in the future, newer versions of software will be compiled using
different toolchain versions. In order to use modules from different toolchain
versions, you can use:

::

    $ module use /apps/leuven/icelake/<toolchain-version>/modules/all

where valid choices for ``<toolchain-version`` look like ``2021a``, ``2022b``,
etc. Older versions of the toolchains will however not be provided because they
are not compatible with the new cluster. Please contact
:ref:`support <user support VSC>` if you run into problems arising from using
newer libraries than the ones provided on Genius.

.. note::

   If you are trying to write scripts that work on several VSC clusters, it can
   be handy to make use of environment variables like ``$VSC_ARCH_LOCAL``,
   which is set to the local architecture. As an example, the statement
   ``module use /apps/leuven/${VSC_ARCH_LOCAL}/2021a/modules/all`` will enable
   using skylake modules when you are on a Genius SkyLake node, icelake modules
   when you are on a wICE IceLake node, etc. Another environment variable that
   can be interesting is ``$VSC_INSTITUTE_CLUSTER``, which resolves to
   ``genius`` on Genius nodes and to ``wice`` on wICE nodes.

Similar to other VSC clusters, wICE supports two toolchain flavors:
:ref:`FOSS <FOSS toolchain>` and :ref:`Intel <Intel toolchain>`. For more
general information on software development on the VSC, have a look at this
:ref:`overview <software_development>`.

.. _wice_worker:

Worker
------

The :ref:`Worker framework <worker framework>`, which allows to conveniently
parameterize simulations, is available on wICE. An attention point is that
if you want to lauch Worker jobs from the Genius login nodes, you will need to
use a specific module:

::

    $ module use /apps/leuven/skylake/2021a/modules/all
    $ module load worker/1.6.12-foss-2021a-wice

If instead you want to launch Worker jobs from an interactive job running on
wICE, you can use the ``worker/1.6.12-foss-2021a`` module (but do make sure
this is the version installed in a subdirectory of ``/apps/leuven/icelake``).

Also note that the Worker support for Slurm is not yet complete. Both
the ``-master`` option for ``wsub`` and the ``wresume`` tool currently
only work for PBS/Torque and hence should not be used in the case of Slurm.

All the resources furthermore need to be specified inside the Slurm script
used as input for Worker (passing resources via the command line is not
supported). Various examples can be found in a `development branch
<https://github.com/gjbex/worker/tree/development_slurm/examples/>`__.


.. _wice_monitoring:

Monitoring
----------

For monitoring or debugging jobs on wICE, you can look into tools provided by
Slurm such as:

* `scontrol <https://slurm.schedmd.com/scontrol.html>`__ to view Slurm
  configuration and state
* `squeue <https://slurm.schedmd.com/squeue.html>`__ to get information about
  jobs in the scheduling queue
* `sacct <https://slurm.schedmd.com/sacct.html>`__ to display information about
  finished jobs

.. note::

    Our Slurm scheduler is aware of multiple clusters and ``wice`` is not the
    default one. As a consequence, any Slurm command (such as `scontrol`,
    `squeue`, `sacct`) needs to be executed with the option ``--cluster=wice``
    (or ``-M wice`` in short) in order to get information for the wICE cluster.

For convenience, we provide the ``slurm_jobinfo`` tool, which runs and parses
output from the Slurm tools mentioned above into a format that is easier to
read. Simply use ``slurm_jobinfo <jobid>`` where ``<jobid>`` has to be replaced
by the 8-digit number that identifies your job.

For getting a compact overview of the current state of the cluster, execute
``slurmtop`` on any KU Leuven Tier-2 node. Use ``slurmtop --help`` to get to
know the functionality.

.. _wice_environment_propagation:

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
:ref:`Compiling software <wice_compilation>` paragraph above).

.. _wice_conda:

Conda on wICE
-------------

As the operating system and hardware are different on Genius and wICE, we advise
to have two separate :ref:`Conda installations <conda for Python>` (one for each
cluster). To select the correct Conda installation when you log in and at the
start of your jobs, you can set up your ``~/.bashrc`` file in the following way:

::
   
   case ${VSC_INSTITUTE_CLUSTER} in
       genius)
           export PATH="${VSC_DATA}/miniconda3/bin:${PATH}"
           ;;
        wice)
           export PATH="${VSC_DATA}/miniconda3-wice/bin:${PATH}"
           ;;
   esac

Also keep in mind that applying your ``~/.bashrc`` settings in your Slurm jobs
requires placing ``#!/bin/bash -l`` at the top of your Slurm jobscript, as
shown in the :ref:`wICE quickstart guide <running jobs on wice>`.

.. _gpu_compute_mode:

Setting the GPU compute mode
----------------------------

NVIDIA GPUs support multiple `compute modes
<https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-modes>`_.
By default, the compute mode is set to `Exclusive-process` on our clusters
(which is the best setting in the majority of cases), but you can choose
another compute mode at job submission time. This is done by making use of a
plugin for our Slurm job scheduler:

::

   $ sbatch --help
   ...
   Options provided by plugins:
   
         --gpu_cmode=<shared|exclusive|prohibited>
                                 Set the GPU compute mode on the allocated GPUs to
                                 shared, exclusive or prohibited. Default is
                                 exclusive

Submitting a batch job where you want to set the compute mode of your NVIDIA
GPU(s) to `shared` can be done with:

::

   sbatch --export=ALL --gpu_cmode=shared jobscript.slurm

An interactive job can be launched as follows:

::

   srun --ntasks-per-node=9 --nodes=1 --gpus-per-node=1 --account=<YOUR_ACCOUNT> \
        --cluster=wice --time=01:00:00 --partition=gpu --gpu_cmode=shared \
        --pty /bin/bash -l

A few notes on this features:

* To check the behaviour is as expected, execute ``nvidia-smi`` in your job
* Runs with GPUs on multiple nodes are not supported. Contact the helpdesk if
  you think you have a use case where this would be necessary.
* The GPU compute mode does not apply when multi-instance GPU partitioning
  (MIG) is used. This is for instance the case on the wICE Slurm partition
  called ``interactive``. For jobs on that partition this feature is
  irrelevant.
* The GPU computed mode can be also set on the ``gpu_p100`` and ``gpu_v100``
  Slurm partitions of our Genius cluster, in the same way as described above.

.. _wice_known_issues:

Known issues
------------

Intel MPI pinning
=================

The Intel MPI library does not always play well with the Slurm scheduler on
wICE. Specifically, when launching a job from a compute node (for instance from
inside an interactive job), processes are not pinned correctly. This issue can
be overcome by setting the environment variable ``I_MPI_PIN_RESPECT_CPUSET=off``
or equivalently adding the option ``-env I_MPI_PIN_RESPECT_CPUSET=off`` to your
``mpirun`` command. To check that processes are pinned correctly to physical
cores, set the environment variable ``I_MPI_DEBUG=5`` to get more verbose
output. Note that this issue does not occur with the Open MPI library.
