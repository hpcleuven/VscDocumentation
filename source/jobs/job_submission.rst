.. _job submission:

Submission of job scripts: sbatch
=================================

Slurm `sbatch manual page`_

The ``sbatch`` is the command in Slurm to submit a job script.
A job script first contains a list of resources and other instructions to
Slurm, and this is followed by a set of commands that will be executed on the
first node of the job. When the submission succeeds, ``sbatch`` will print a
message containing the unique job ID for the job.

Resource specifications and other instructions can be specified in three
different ways: command line options, environment variables, and ``#SBATCH``
lines in the job script.

* Slurm ``sbatch`` has a lot of command line options. We will only list the
  most important command line options below. Command line options of Slurm
  take precedence over environment variables and ``#SBATCH`` lines in the
  job script.
* Some command line options can also be passed to ``sbatch`` through environment
  variables instead. A list of those can be found in the `sbatch manual page`_.
  The name of those variables starts with ``SBATCH_`` and the remaining part is
  derived from the matching command line option. However, be careful when using
  those and hiding them in ``.bashrc`` or ``.bash_profile`` as they are easily
  forgotten yet have a higher priority than those on ``SBATCH`` lines which is
  the most used mechanism to specify resources etc.
* All command line options can also be passed in ``#SBATCH`` lines in the job script.
  These lines should follow immediately below the shebang in the first block of
  comment lines (lines that start with ``#``) as otherwise they will
  be ignored by Slurm.

Note that all ``sbatch`` command line options should be specified
*before* the name of the job script. All command line parameters specified
*after* the name of the job script will be passed as command line arguments
to the job script when it executes.

Requesting compute resources
----------------------------

Slurm supports several ways to request CPU cores and/or GPUs for a job.

The easiest way to request CPU cores is by following the "task"-idea
of Slurm and specifying the number of parallel tasks and cores per task
that you need. By specifying resources this way, it is very easy afterwards
to start OpenMP, MPI and hybrid MPI/OpenMP programs in the right configuration.

* The number of tasks is specified by ``--ntasks=<number of tasks>`` or
  ``-n <number of tasks>``. The ``=``-sign in the long option format can
  be replaced by a space, and in the short form (``-n``) the space between
  the flag and the value form can also be omitted (in effect, this holds
  for all options).
* The number of CPUs (hardware threads) per task is specified by
  ``--cpus-per-task=<value>`` or ``-c <value>``.  On the UAntwerp clusters,
  CPUs are physical cores (since hyperthreading is disabled). For each task,
  all of the CPUs for that task are allocated on a single node. When using
  multiple nodes, the allocated CPUs for all tasks are distributed equally
  over all the nodes (except possibly for the last node).

Make sure to request a valid combination of tasks and/or CPUs per task.
Otherwise, your job can be rejected or it could end up in the partition
queue but it will never start (in that case, check the reason code, as
explained later in this document in the section on checking the queue).

If set, the Slurm controller will set the corresponding variables,
respectively ``SLURM_NTASKS`` and ``SLURM_CPUS_PER_TASK`` in the
environment of the running job.

If not set, the default values of 1 task and 1 CPU are used.

Requesting memory
-----------------

Slurm jobs can also request an amount of RAM space (resident memory).
In case of the UAntwerp clusters, swapping for jobs is
disabled since the nodes don't have drives suitable for the load caused by
swapping and since swapping is extremely detrimental to the performance of
the cluster. Therefore, swap space cannot be requested.

Slurm has various ways to request memory. Unfortunately, there is currently no
way to request memory per task. The preferred method for requesting memory in
Slurm on the UAntwerp clusters is to specify the amount of memory per CPU
(per core on the UAntwerp clusters):
``--mem-per-cpu=<amount><unit>`` (e.g., ``--mem-per-cpu=1g``). The amount is an
integer, ``<unit>`` can be either ``k`` for kilobytes, ``m`` for megabyte or
``g`` for gigabyte.

The job will be rejected if the final amount of memory requested cannot be satisfied.
This could happen if ``--mem-per-cpu`` times the number of CPUs on a node is greater
than the memory on that node that is available for job allocations. Note that on the
UAntwerp clusters, the memory available for job allocations is somewhat less than the
total memory installed on a node (to keep some amount of memory for the OS and file
system buffers).

If not set, a default value will be used, equal to the total memory available for job
allocations of that node divided by the number of CPUs.

The amount of available memory per CPU is available via the variable
``SLURM_MEM_PER_CPU`` as an integer with megabytes as unit in the
environment of the running job.

Requesting wall time
--------------------

The requested compute time is specified using ``--time=<time>`` or ``-t <time>``.
``<time>`` is specified in mm (minutes), mm\:ss (minutes and seconds), hh\:mm\:ss
(hours, minutes and seconds), d-hh (days and hours), d-hh\:mm (days, hours and minutes)
or d-hh\:mm\:ss (days, hours, minutes and seconds) format. The ``-`` is not a typo!

If not set, a default wall time of 1 hour will be assigned.

Specifying a partition
----------------------

Slurm jobs can be submitted to a certain partition of compute nodes. Indicating
the kind of job in this manner imposes some additional restrictions on resources
and time, but may let the job start sooner. The partition can be specified
using ``--partition=<partition>`` or ``-p <partition>``.

If not set, the default partition will be used.

The name of partition is available in the variable ``SLURM_JOB_PARTITION``
in the environment of the running job.

Specifying a job name
---------------------

The default name of a job is the name of the job script. The name can however be changed
using ``--job-name=<name>`` or ``-J <name>``.

The name of the job is available in the variable ``SLURM_JOB_NAME``
in the environment of the running job.

Redirecting stdout and stderr
-----------------------------

By default, Slurm redirects both stdout and stderr to the same file, named ``slurm-<jobid>.out``.
There are two flags to ``sbatch`` to change this behaviour:

* ``--output=<output file>`` or ``-o <output file>`` will redirect all output to the file
  specified by ``<output file>`` rather than the default.
* ``--error=<error file>`` or ``-e <error file>`` will redirect output sent to stderr to
  the file specified by ``<error file>``. Output sent to stdout is still sent to the default
  file, unless ``--output`` is also used.

Hence:

* No ``--output`` and no ``--error``: stdout and stderr are both sent to the default output
  file ``slurm-<jobid>.out``.
* ``--output`` specified but no ``--error``: stdout and stderr are both sent to the file
  pointed to by ``--output``.
* No ``--output``, but ``--error`` specified: stdout is redirected to the default output file
  ``slurm-<jobid>.out`` while stderr is redirected to the file pointed to by ``--error``.
* Both ``--output`` and ``--error`` are specified: stdout is redirected to the file pointed to
  by ``--output`` and stderr is redirected to the file pointed to by ``--error``.

The file name can (and usually will) be a template. It can contain replacement symbols preceded
by a % that allow to use the job ID etc. in the name of the file to ensure unique file names.
The most useful of such symbols is ``%j`` which will be replaced by the unique job ID.
A full list of replacement symbols can be found in the `sbatch manual page`_.

Sending mail at specific events
-------------------------------

Slurm can send mail when a job starts, fails or ends normally, and on a number of other occasions.
Two flags influence this behaviour:

* ``--mail-type=<type>`` specifies when mail should be sent. ``<type>`` is a comma-separated list
  of type values. Type values include BEGIN, END and FAIL to denote respectively the start of a
  job, end of a job and failure of a job, but there are many other options that can be found in
  the `sbatch manual page`_.
* ``--mail-user=<mail address>`` specifies to which mail address the mails should be sent. The
  default value is the mail address associated with the VSC-account of the submitting user.

If not set, no mail will be sent.

Specifying dependencies
-----------------------

Job dependencies can be used to defer the start of a job until the specified dependencies have been
satisfied. They are very helpful when implementing a workflow consisting of steps with different
requirements for each job in the workflow.

The basic way of specifying a job dependency is through
``--dependency=<type>:jobid:jobid,<type>:jobid:jobid``
etc. For (almost) each type one can specify one or more job IDs, and it is also possible
to specify multiple types of dependencies.

============================  =====================
Dependency type               What it does
============================  =====================
**after**:jobid[:jobid]       Job can begin after all specified jobs have started (or are cancelled)
**afterany**:jobid[:jobid]    Job can begin after all specified jobs have terminated
**afterok**:jobid[:jobid]     Job can begin after the specified jobs has successfully completed
**afternotok**:jobid[:jobid]  Job can begin after the specified jobs have failed
**singleton**                 Job can start after all previously launched jobs with the same name and same user have ended.
                              This can be useful to collate results after running a batch of related jobs.
============================  =====================

The job environment
-------------------

The Slurm ``sbatch`` command by default copies the environment in which the job script was submitted
(at least, the environment seen by the ``sbatch`` command, so all exported variables and functions).
This implies that, e.g., all modules that were loaded when you submitted the job script, will
be loaded in your job environment. This poses a number of risks:

* Some modules adapt their behaviour to the environment in which they were loaded.
  One important example are the modules that provide MPI on the cluster. When
  launched in a Slurm job environment, some environment variables are set to
  ensure maximal integration with Slurm. However, when loaded on the login nodes
  these variables are not set as otherwise running a MPI program as a regular
  program without ``mpirun`` (and launching just a single process) would fail.
  The latter is a problem for, e.g., Python when some module loads the Python
  MPI package.
* You may be working in a different environment than the one you used the previous
  time you ran the job script, and as a consequence of this your job script that
  previously functioned well may now function differently.
* Paths may be different on the login nodes and compute nodes. This can happen during
  OS upgrades of the cluster. These can often be done without downtime or interrupting
  work on the cluster, but that implies that some nodes will be running one version while
  other nodes will be running another version of the OS setup.

To alleviate these issues,  we set a minimal environment for jobs by default. This means that, along
with the SLURM_* variables, only the HOME, USER and TERM environment variables are exported to the job.
The PATH environment variable is set to a minimum in the job environment. This implies that the desired
software modules must be loaded in your job scripts for use during the execution of the job.

In case you would attempt to use the ``--export`` sbatch option to override this behaviour, 
we advise you to apply one of the following solutions to avoid accidental mistakes:

* Clear the environment in your job script by reloading all modules that are needed and
  ensuring that all environment variables that you need are set.
  Cleaning the module environment can be done by calling

  ``module --force purge``

  and then reloading the right ``calcua`` software stack module and application modules. This should
  be a common practice in all your job scripts.
* Use one of the options ``--get-user-env`` or ``--export=NONE`` (either with the ``sbatch``
  command or, preferably, as a ``#SBATCH`` line in the job script).

  The option ``--get-user-env`` will tell ``sbatch`` not to propagate the environment in which
  it executes, but to reconstruct the environment that you would get when you log on to the
  cluster. Though be aware that any environment variables already set in the environment will
  still take precedence over any environment variables in the user's login environment.
  And there is also a difference with what you get when executing your
  ``.bash_profile`` script: The environment only contains exported variables and functions and
  no aliases or variables or functions that are not exported by ``.bash_profile``.

  The option ``--export=NONE`` will only define SLURM_* variables from the user environment.
  When using this option, one must use an absolute path to the binary to be executed (which
  could then be used to further define the environment). When using this option, it is not
  possible to pass environment variables to the job script.

The Slurm controller also sets several SLURM_* variables in the environment of the running job.
Some of these variables are only available if the corresponding option has been explicitly set,
while other variables are always set (with default values filled in, if appropriate).
Several of these variables are mentioned on our
:ref:`PBS-to-Slurm conversion tables <Antwerp Slurm_convert_from_PBS>` page.
A full list of all SLURM_* environments can be found in the
`sbatch manual page`_ (in the section on "OUTPUT ENVIRONMENT VARIABLES").


Starting multiple copies of a process in a job script: srun
-----------------------------------------------------------

`Slurm srun manual page on the web <https://slurm.schedmd.com/srun.html>`_

The ``srun`` command is used to start a new job step in a job script. The most common case is
to start a parallel application. ``srun`` integrates well with major MPI implementations and
can be used instead of ``mpirun`` or ``mpiexec`` to start a parallel MPI application. It then
takes your resource requests and allocated resources into account and does a very good job
of starting each MPI rank on the right set of cores even without having to use additional
command line options. Further down this section/page there are a couple of examples that
demonstrate the power of the ``srun`` command. The advantage of this way of working is that
all processes run under the strict control of Slurm, ensuring that if something goes wrong,
they are also cleaned up properly.

The ``srun`` command can also be used outside of a resource allocation, i.e., at the command
line of the login nodes, outside a job script or an allocation obtained with ``salloc`` (see
further in the text). It will then first create the resource allocation before executing the
command given as an argument to ``srun``. One useful case which we discuss further down in this
text is to start an interactive session. Most of the command line options of
``sbatch`` to specify the properties of the allocation can also be used with ``srun``.

Just as ``sbatch``, ``srun`` will propagate the environment. When ``srun`` is used in
a job script to start a parallel application, this is also very sensible and desired
behaviour as it ensures the processes started with Slurm run in the right environment
created by the job script.

