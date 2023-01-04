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
operating system (Rocky Linux 8.6) differs significantly from Genius, a
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

Note that in the future, newer versions of software will be added to
directories called for instance ``/apps/leuven/icelake/2022b/modules/all``.
Older versions will however not be provided because they are not compatible
with the new cluster. Please contact support if you run into problems arising
from using newer libraries than the ones provided on Genius.

.. note::

   If you are trying to write scripts that work on several VSC clusters, it can
   be handy to make use of environment variables like ``$VSC_ARCH_LOCAL``,
   which is set to the local architecture. As an example, the statement
   ``module use /apps/leuven/${VSC_ARCH_LOCAL}/2021a/modules/all`` will enable
   using skylake modules when you are on a Genius SkyLake node, icelake modules
   when you are on a wICE IceLake node, etc. Another environment variable that
   can be interesting is ``$VSC_INSTITUTE_CLUSTER``.

Similar to other VSC clusters, wICE supports two toolchain flavors:
:ref:`FOSS <FOSS toolchain>` and :ref:`Intel <Intel toolchain>`. For more
general information on software development on the VSC, have a look at this
:ref:`overview <software_development>`.

.. _wice_worker:

Worker
------

The :ref:`worker framework <worker framework>`, which allows to conveniently
parameterize simulations, is available on wICE. An attention point is that
if you want to lauch worker jobs from the Genius login nodes, you will need to
use a specific module:

::

    $ module use /apps/leuven/skylake/2021a/modules/all
    $ module load worker/1.6.12-foss-2021a-wice

If instead you want to launch Worker jobs from an interactive job running on
wICE, you can use the ``worker/1.6.12-foss-2021a`` module (but do make sure
this is the version installed in a subdirectory of ``/apps/leuven/icelake``).

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

For convenience, we provide the ``slurm_jobinfo`` tool, which runs and parses
output from the Slurm tools mentioned above into a format that is easier to
read. Simply use ``slurm_jobinfo <jobid>`` where ``<jobid>`` has to be replaced
by the 8-digit number that identifies your job.

For getting a compact overview of the current state of the cluster, execute
``slurmtop`` on any KU Leuven Tier-2 node. Use ``slurmtop --help`` to get to
know the functionality.

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
mpirun command. To check that processes are pinned correctly to physical cores,
set the environment variable ``I_MPI_DEBUG=5`` to get more verbose output. Note
that this issue does not occur with the Open MPI library.

Environment propagation
=======================

Jobs on wICE do not start with a clean slate. Some information from the session
in which the job was submitted is propagated. For instance modules that were
loaded at job submission time, will also be loaded inside the job. This can
create problems when you submit a job to wICE from a Genius login node, because
modules installed for genius are generally not suited to be used on wICE nodes.
You can make sure this does not happen by executing ``module --force purge`` at
the start of your job script, which will unload any currently loaded module.
