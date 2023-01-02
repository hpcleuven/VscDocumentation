.. _Antwerp Slurm:

Slurm @ UAntwerp
================

This page covers the more basic Slurm use, including starting jobs, basic job management
and some templates for job scripts for various scenarios. It is the minimum a user should
master. A second page describes :ref:`more advanced use of Slurm <Antwerp advanced Slurm>`.

What and why?
-------------

Since the start of the VSC, Torque and Moab were used as the resource manager and scheduler
respectively. The resource manager is responsible for keeping track of resources and making
sure jobs use the resources allocated to them. The scheduler is the piece of software that
prioritises jobs that are waiting in the queue and decides which job can start with which
resources. It is clear that both have to work together very closely. Torque and Moab were
developed and supported by Adaptive Computing. This company was acquired by ALA Services
Technology Companies. Since then the software isn't well supported anymore, resulting in
problems to keep it running on our systems.

Therefore, the decision was taken to transfer to a different resource manager and scheduler
software. Slurm Workload Manager was chosen due to its wide use in academic supercomputer
centres. We've been preparing for this switch for over two years now by stressing in the
introductory courses those features of Torque and Moab that resemble Slurm features
the most.

Slurm Workload Manager is also used on the clusters at UGent (but with a wrapper that still
accepts Torque job scripts with some limitations) and is also the scheduler on Hortense.

Historically, Slurm was an acronym of **S**\imple **L**\inux **U**\tility for
**R**\esource **M**\anagement. The development started around 2002 at Lawrence Livermore
National Lab as a resource manager for Linux clusters. Slurm has always had a very modular
architecture. From 2008 on increasingly sophisticated scheduling plugins were added
to Slurm. Nowadays it is used on some of the largest systems in the world. Slurm is
completely open source though commercial support can be obtained from SchedMD, a
spin-off company of the Slurm development.


Slurm concepts
--------------

* **Nodes**: On the UAntwerp clusters (and most other clusters) a node is the largest
  part of the cluster running a single operating system image, and hence capable of
  supporting a shared memory program. Nodes are connected with each other through an
  interconnect, and communication between nodes is done via message passing.
* **Core**: A core is a physical core in a system.
* **CPU**: A CPU is a virtual core in a system, in other words, a hardware thread
  in a system with hyperthreading/SMT enabled. On a system with hyperthreading/SMT
  disabled, virtual cores are just physical cores.
* **Partition**: Groups of nodes with limits and access controls, basically the equivalent
  of a queue in Torque. A node can be part of multiple partitions.
* **Job**: A resource allocation request.
* **Job step**: A set of (possibly parallel) tasks within a job. A job can consist of
  just a single job step or can contain multiple job steps which may use all or just
  a part of the resource allocation of a job and can run sequentially or in parallel
  (or a mix of that). The job script itself is a special job step, called the batch
  job step, but additional job
  steps can be created (e.g., for running a parallel MPI application).
* **Task**: A task is executed within a job step and essentially corresponds to a
  Linux process: a single- or multithreaded process, or a single rank within a MPI
  process. Specifying the number of tasks one wants to run simultaneously and the
  number of cores per task is a very convenient way to request resources to Slurm
  as afterwards starting a MPI or hybrid MPI/OpenMP program using the ``srun``
  command is very easy.


Slurm commands
--------------


Submitting a job script: sbatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Slurm sbatch manual page on the web <https://slurm.schedmd.com/sbatch.html>`_

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
  variables instead. A list of those can be found in the
  `sbatch manual page <https://slurm.schedmd.com/sbatch.html>`_. The name of those
  variables starts with ``SBATCH_`` and the remaining part is derived from the
  matching command line option. However, be careful when using those and hiding them
  in ``.bashrc`` or ``.bash_profile`` as they are easily forgotten yet have a higher
  priority than those on ``SBATCH`` lines which is the most used mechanism to specify
  resources etc.
* All command line options can also be passed in ``#SBATCH`` lines in the job script.
  These lines should follow immediately below the shebang in the first block of
  comment lines (lines that start with ``#``) as otherwise they will
  be ignored by Slurm.

Note that all ``sbatch`` command line options should be specified
*before* the name of the job script. All command line parameters specified
*after* the name of the job script will be passed as command line arguments
to the job script when it executes.

Requesting compute resources
""""""""""""""""""""""""""""

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
"""""""""""""""""

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
""""""""""""""""""""

The requested compute time is specified using ``--time=<time>`` or ``-t <time>``.
``<time>`` is specified in mm (minutes), mm\:ss (minutes and seconds), hh\:mm\:ss
(hours, minutes and seconds), d-hh (days and hours), d-hh\:mm (days, hours and minutes)
or d-hh\:mm\:ss (days, hours, minutes and seconds) format. The ``-`` is not a typo!

If not set, a default wall time of 1 hour will be assigned.

Specifying a partition
""""""""""""""""""""""

Slurm jobs can be submitted to a certain partition of compute nodes. Indicating
the kind of job in this manner imposes some additional restrictions on resources
and time, but may let the job start sooner. The partition can be specified
using ``--partition=<partition>`` or ``-p <partition>``.

If not set, the default partition will be used.

The name of partition is available in the variable ``SLURM_JOB_PARTITION``
in the environment of the running job.

Specifying a job name
"""""""""""""""""""""

The default name of a job is the name of the job script. The name can however be changed
using ``--job-name=<name>`` or ``-J <name>``.

The name of the job is available in the variable ``SLURM_JOB_NAME``
in the environment of the running job.

Redirecting stdout and stderr
"""""""""""""""""""""""""""""

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
A full list of replacement symbols can be found in
`the sbatch manual page <https://slurm.schedmd.com/sbatch.html>`_.

Sending mail at specific events
"""""""""""""""""""""""""""""""

Slurm can send mail when a job starts, fails or ends normally, and on a number of other occasions.
Two flags influence this behaviour:

* ``--mail-type=<type>`` specifies when mail should be sent. ``<type>`` is a comma-separated list
  of type values. Type values include BEGIN, END and FAIL to denote respectively the start of a
  job, end of a job and failure of a job, but there are many other options that can be found in
  `the sbatch manual page <https://slurm.schedmd.com/sbatch.html>`_.
* ``--mail-user=<mail address>`` specifies to which mail address the mails should be sent. The
  default value is the mail address associated with the VSC-account of the submitting user.

If not set, no mail will be sent.

Specifying dependencies
"""""""""""""""""""""""

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
"""""""""""""""""""

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
`sbatch manual page <https://slurm.schedmd.com/srun.html>`_ (in the section on
"OUTPUT ENVIRONMENT VARIABLES").


Starting multiple copies of a process in a job script: srun
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Commands for managing jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Checking the queue: squeue
""""""""""""""""""""""""""

`Slurm squeue manual page on the web <https://slurm.schedmd.com/squeue.html>`_

The Slurm command to list jobs in the queue is ``squeue``.

The basic command without options will show basic information about all your jobs in the queue.
There are a number of useful command line options though:

* The ``--long`` or ``-l`` flag adds some additional information.
* ``--format=<output format>`` or ``-o <output format>`` allows you to specify
  your custom output format that can show a lot more information. Likewise,
  ``--Format=<output format>`` or ``-O <output format>`` (with a capital first letter)
  can show even more
  information but with a longer syntax for the output format. See the
  `squeue manual page <https://slurm.schedmd.com/squeue.html>`_ for information
  on all format options.
* It is possible to show that information for only one or a selection of your
  jobs by using ``--jobs=<job_id_list>`` or ``-j <job_id_list>``, where ``<job_id_list>``
  is a comma-separated list of job IDs.

The column "REASON" lists why a job is waiting for execution. It distinguishes between
30+ different reasons, way to much to discuss here, but some of the codes speak for
themselves. The full list of reason codes can be found in the
`squeue manual page <https://slurm.schedmd.com/squeue.html>`_.


Kill/delete a job: scancel
""""""""""""""""""""""""""

`Slurm scancel manual page on the web <https://slurm.schedmd.com/scancel.html>`_

The Slurm command to cancel a job is ``scancel``. In most cases, it takes only a
single argument, the unique identifier of the job to cancel.

For a job array (see below) it is also possible to cancel only some of the jobs in
the array by specifying the array elements as follows:

.. code:: bash

   scancel 20_[1-3]
   scancel 20_4 20_6

The first command would kill jobs 1, 2 and 3 in the job array with job ID 20,
the second command would kill jobs 4 and 6 of that job array.

As shown in the example above, a space separated list of multiple job IDs can also
be specified, as well as a selection based on multiple filters, e.g., in which partition
the job is running. Consult the `scancel manual page <https://slurm.schedmd.com/scancel.html>`_
for more information.

Getting more information on a running job: sstat
""""""""""""""""""""""""""""""""""""""""""""""""

`Slurm sstat manual page on the web <https://slurm.schedmd.com/sstat.html>`_

The ``sstat`` command displays information on running jobs pertaining to CPU, Task,
Node, Resident Set Size (RSS) and Virtual Memory (VM) for all your running jobs.
The jobs need to be explicitly mentioned using ``--jobs=<job_id_list>`` or
``-j <job_id_list>`` (where ``<job_id_list>`` is a comma-separated list of job IDs).

By default, it will only show information about the lowest job step running in
a particular job unless ``--allsteps`` or ``-a`` is also specified.
It is also possible to request information on a specific job step of a job
by using ``<jobid.jobstep>``, i.e., add the number of the job step to the
job ID, separated by a dot.

To show additional information not shown by the default format, one can
specify a specific format using the ``--format`` or identical ``--fields``
and ``-o`` flags.  Check the `sstat manual page <https://slurm.schedmd.com/sstat.html>`_
for further information.


Getting information about a job after it finishes: sacct
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

`Slurm sacct manual page on the web <https://slurm.schedmd.com/sacct.html>`_

Whereas ``sstat`` is used to show near real-time information for running jobs,
``sacct`` shows the information as it is kept by Slurm in the job accounting
log/database. Hence it is particularly useful to show information about jobs
that have finished already. It allows you to see how much CPU time, wall time,
memory, etc. were used by the application.

By default, ``sacct`` shows the job ID, job name, partition name, account name,
number of CPUs allocated to the job, the state of the job and the exit code
of completed jobs. Several options can be used to modify the format:

* ``--brief`` or ``-b`` shows only the job ID, state and exit ode.
* ``--long`` or ``-l`` shows an overwhelming amount of information, probably more than you
  want to know as a regular user.
* ``--format`` or ``-o`` can be used to specify your own output format. We refer
  to the `sacct manual page <https://slurm.schedmd.com/sacct.html>`_ for an overview of
  possible fields and how to construct the format string.

By default, ``sacct`` will show information about jobs that have been running
since midnight. There are however a number of options to specify for which jobs
you want to see information:

* ``--jobs=<job_id_list>`` or ``-j <job_id_list>`` with a comma-separated list of job IDs
  (in the same format as for ``sstat``) will only show information on those jobs
  (or job steps).
* ``--starttime=<time>`` or ``-S <time>`` will show information about all jobs that
  have been running since the indicated start time. There are four possible
  formats for ``<time>``: HH:MM[:SS] [AM|PM], MMDD[YY] or MM/DD[/YY] or MM.DD[.YY],
  MM/DD[/YY]-HH:MM[:SS] and YYYY-MM-DD[THH:MM[:SS]] (where [] denotes an optional
  part).
* ``--endtime=<time>`` or ``-E <time>`` will show information about all jobs that
  have been running before the indicated end time. By combining a start time and
  end time it is possible to specify a window for the jobs.

For now, there is no reason to be concerned about the account name as we do not use
accounting to control the amount of compute time a user can use.


Job types: Examples
-------------------

Shared memory job
~~~~~~~~~~~~~~~~~

A shared memory program consists of a single task. The number of CPUs you would
request for the task corresponds to the number of computational threads
you want to use for the application. Keep in mind that a single task cannot
span multiple nodes in the cluster.

Shared memory programs often need to be told how many threads they should use.
Unfortunately, there is no standard way that works for all programs. Some programs
require an environment variable to be set, others have a parameter in the input file
and some interpreters (e.g., Matlab) require it to be set in the code being interpreted.

OpenMP is a popular technology for creating shared memory programs. Some OpenMP programs
will read the number of threads from the input file and then set it using OpenMP library functions.
But most OpenMP programs simply use the environment variable ``OMP_NUM_THREADS`` to
determine the number of threads that should be used.

The following job script is an
example of this. It assumes there is a program ``omp`` in the current directory
compiled with the intel/2020a toolchain. It will be run on 10 cores.

.. code:: bash

   #! /bin/bash
   #
   #SBATCH --job-name=OpenMP-demo
   #SBATCH --ntasks=1 --cpus-per-task=10 --mem=2g
   #SBATCH --time=05:00

   # Build the environment
   module --force purge
   module load calcua/2020a
   module load vsc-tutorial

   # Set the number of threads
   export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

   # Run the program
   omp_hello

In this example, ``omp_hello`` is a demo program contained in the ``vsc-tutorial``
module that will simply print a message from each thread. the ``vsc-tutorial``
module also loads the ``intel/2020a`` module as that compiler was used to compile
the programs in the module.

When using Intel OpenMP, not setting the variable ``OMP_NUM_THREADS``
works fine in most or even all cases as the runtime seems to recognize Slurm and pick up
the right number of threads.

In many cases it may be beneficial to also set

.. code:: bash

   export OMP_PROC_BIND=true

before calling the OpenMP program. It will spread the OpenMP threads over the cores and
keep them bound to the core, which is beneficial for reuse of data in caches. Except for
really short running threads (as is the case in this example) the Linux scheduler will
usually rather quickly distribute the threads across the cores and keep them pinned. Yet
there are cases where ``OMP_PROC_BIND=true`` turns out to be beneficial for performance.


MPI program
~~~~~~~~~~~

Running distributed memory programs usually requires a program starter.
In the case of MPI programs, the usual way to start a program is through
the ``mpirun`` or ``mpiexec`` command. The major MPI implementations will
recognize Slurm (sometimes with the help of some environment variables)
and work with Slurm to start the MPI processes on the correct cores
and under the control of the resource manager (so that they are cleaned
up properly if things go wrong).

However, with several implementations (and all MPI implementations supported
on our cluster), it is also possible to use the
Slurm ``srun`` command to start the MPI processes. This is the case
for programs compiled with Intel MPI as the example below shows. The
example assumes there is a MPI program called ``mpi_hello`` provided by the
``vsc-tutorial`` module. The ``vsc-tutorial`` module will also load the
``intel/2020a`` module for the libraries used by the compiler and the
MPI library.

.. code:: bash

   #! /bin/bash
   #
   #SBATCH --job-name=mpihello
   #SBATCH --ntasks=56 --cpus-per-task=1 --mem-per-cpu=512m
   #SBATCH --time=5:00

   # Build the environment
   module --force purge
   module load calcua/2020a
   module load vsc-tutorial

   # Run the MPI program
   srun mpi_hello

In the above case, 56 MPI ranks will be spawned, corresponding to two
nodes on a cluster with 28 cores per node.

Note that if the executable called by ``srun`` is not in the path, you do need
to specify the path to the executable just as you would have to do on the command
line. E.g., if ``mpi_hello`` would be in the current directory in the above example,
it would be started using

.. code:: bash

   srun ./mpi_hello

and of course you'd have to load a module with MPI support.


Hybrid MPI/OpenMP program
~~~~~~~~~~~~~~~~~~~~~~~~~

Some programs are hybrids combining a distributed memory technology with a shared
memory technology. The idea is that shared memory doesn't scale beyond a single
node (and often not even to the level of a single node), while distributed
memory programs that spawn a process per core may also suffer from too much memory
and communication overhead. Combining both can sometimes give better performance
for a given number of cores.

Especially the combination of MPI and OpenMP is
popular. Such programs require a program starter and need the number of threads
to be set in one way or another. With many MPI implementations (including the ones
we use at the VSC), ``srun`` is an ideal program starter and will start the
hybrid MPI/OpenMP processes on the right sets of cores.

The example below assumes ``mpi_omp_hello`` is a program compiled with
the Intel toolchain that uses both MPI and OpenMP. It starts 8 processes
with 7 threads each, so it would occupy two nodes on a cluster with 28 cores
per node.

.. code:: bash

   #! /bin/bash
   #SBATCH --ntasks=8 --cpus-per-task=7 --mem-per-cpu=512m
   #SBATCH --time=5:00
   #SBATCH --job-name=hybrid-hello-test

   module --force purge
   module load calcua/supported
   module load vsc-tutorial

   # Set the number of threads per MPI rank
   export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
   export OMP_PROC_BIND=true

   # Start the application
   srun mpi_omp_hello

As with shared memory programs, it turns out that setting OMP_NUM_THREADS is
not needed most of the time when the Intel compilers were used for the application
as they pick up the correct number of threads from Slurm. We did set
``OMP_PROC_BIND`` to ``true`` as binding threads to core is as essential as it is
for regular shared memory programs.


Job arrays and parameter exploration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Slurm manual page on job array <https://slurm.schedmd.com/job_array.html>`_

Slurm also supports job arrays. This is a mechanism to submit and manage a collection of
similar jobs simultaneously much more efficiently then when they are submitted as
many regular jobs. When submitting a job array, a range of index values is given.
The job script is then started for each of the index values and that value is
passed to the job through the ``SLURM_ARRAY_TASK_ID`` variable.

E.g., assume that there is a program called ``test_set`` in the current directory
that reads from an input file and writes to an output file, and assume that we want
run this for a set of input files named ``input_1.dat`` to ``input_100.dat``, writing
the output to ``output_1.dat`` till ``output_100.dat``. The job script would look like:

.. code:: bash

   #! /bin/bash -l

   #SBATCH --ntasks=1 --cpus-per-task=1
   #SBATCH --mem-per-cpu=512M
   #SBATCH --time 15:00

   INPUT_FILE="input_${SLURM_ARRAY_TASK_ID}.dat"
   OUTPUT_FILE="output_${SLURM_ARRAY_TASK_ID}.dat"

   ./test_set ${SLURM_ARRAY_TASK_ID} -input ${INPUT_FILE}  -output ${OUTPUT_FILE}

Assume the filename of the script is ``job_array.slurm``, then it would be
submitted using

.. code:: bash

   sbatch --array=1-100 job_array.slurm

Within the VSC, the package ``atools`` was developed to ease management of job arrays
and to start programs using parameter values stored in a CSV file that can be generated
easily using a spreadsheet program. On the UAntwerp clusters, the most recent version of
the package is available as the module ``atools/slurm``.
For information on how to use atools, we refer to the
`atools documentation on ReadTheDocs <https://atools.readthedocs.io/en/latest/>`_ and
`course material from a course at KU Leuven <https://gjbex.github.io/worker-and-atools/>`_.
Note however that the Worker package which is also mentioned in that course does not work
on Slurm and can no longer be used.


Workflow through job dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the following example

* We run a simulation to compute a first solution.
* After the simulation, we add two different sized perturbations to the solution and
  run again from these perturbed states.

Of course, one could try to do all three simulations in a single job script, but that is
not a good idea for various reasons.

* Longer-running jobs may have a lower priority in the scheduler
* When there is a failure halfway the job, it may take some puzzling to figure out which
  parts have to run again and to adapt the job script to that.
* As the simulations from the perturbed state are independent of each other, it is possible
  to run them in parallel rather then sequentially.

On the other hand, first launching the simulation that computes the first solution, then
waiting until that job has finished and only then launching two jobs, one for each perturbation,
isn't a very handy solution either.

Two elements can be combined to do this in a handier way, submitting all jobs simultaneously:

* As environment variables are passed to the job script, they can be used to influence the
  behaviour of a job script. In our example, they could be used to specify the size of the
  perturbation to apply so that both jobs that run from a perturbed state can be submitted using
  the same job script.

  An alternative is to pass command line arguments to the job script which is possible in Slurm
  by adding them to the ``sbatch`` command line after the job script.
* Dependency specifications can then be used to ensure that the jobs that run from a perturbed
  state do not start before the first simulation has successfully completed.

For example, assume that we have two job scripts:

* ``job_first.slurm`` is a job script that computes the first solution.
* ``job_depend.slurm`` is a job script to compute a solution from a perturbed initial state.
  It uses the environment variable ``perturbation_size`` to determine the perturbation to
  apply.

To make ``sbatch`` print simply the job ID after submitting, use the ``--parsable`` option.
The following lines automate the launch of the three jobs:

.. code:: bash

    first=$(sbatch --parsable --job-name job_leader job_first.slurm)
    perturbation_size='0.05' sbatch --job-name job_pert_0_05 --dependency=afterok:$first job_depend.slurm
    perturbation_size='0.1'  sbatch --job-name job_pert_0_1  --dependency=afterok:$first job_depend.slurm

Interactive job
~~~~~~~~~~~~~~~

Method 1: with srun
"""""""""""""""""""

Interactively running shared memory programs
''''''''''''''''''''''''''''''''''''''''''''

Starting a single task interactive job can be done easily by using ``srun --pty bash``
on the command line of one of the login nodes. For example:

.. code:: bash

   login$ srun --ntasks=1 --cpus-per-task=10 --time=10:00 --mem-per-cpu=3G --pty bash

(with ``login$`` denoting the command prompt on the login node) or briefly

.. code:: bash

   login$ srun -n1 -c10 -t10 --mem-per-cpu=3G --pty bash

will start a bash shell on a compute node and allocate 10 cores and 30 GB of memory
to that session. The maximum wall time of the job is set to 10 minutes.

Specifying the ``--pty`` option redirects the standard and error outputs of the
first (and, in this case, only) task to the attached terminal. This effectively results
in an interactive bash session on the requested compute node.


Interactively running MPI programs
''''''''''''''''''''''''''''''''''

Interactively running MPI programs or hybrid MPI/OpenMP programs is very similar to
the way you run shared memory programs interactively, but just as in batch scripts you
now need to request one task per MPI rank and use a process starter to start the program,
which usually amounts to running ``srun`` in an ``srun``-session. E.g.,

.. code:: bash

   login$ srun -n 64 -c 1 -t 1:00:00 --pty bash

will create an allocation for 64 single-core tasks and start a bash shell in the first task
that takes its input from the keyboard and sends its output to the terminal. You can then
run a MPI program in the same way as you would in a batch script (with ``r0c00cn0$``
denoting the command prompt of the compute node):

.. code:: bash

   r0c00cn0$ module --force purge
   r0c00cn0$ module load calcua/2020a vsc-tutorial
   r0c00cn0$ srun mpi_hello
   r0c00cn0$ exit

The ``exit`` command at the end ends the shell and hence the interactive job.


Running X11 programs
''''''''''''''''''''

You can also use ``srun`` to start an interactive session with X11 support. However, before
starting a session you should ensure that you can start X11 programs from the session from
you will be starting ``sriun``. So either

1. ensure you are running an X11 server on the machine from which you log on to the cluster
   and then log on using ``ssh -X`` to forward X11 traffic from the cluster to your
   local machine,

2. or use a VNC session on the cluster. VNC without 3D acceleration is supported on all
   login nodes of the UAntwerp infrastructure and 3D acceleration is supported on the
   visualisation node. Follow the instructions on the
   :ref:`Remote visualisation@UAntwerp<remote visualization UAntwerp>` page to start
   a VNC session.

X11 programs rarely use distributed memory parallelism, so in most case you will be requesting
just a single task. To add support for X11, use the ``--x11`` option before ``--pty``:

.. code:: bash

   login$ srun -n 1 -c 64 -t 1:00:00 --x11 --pty bash
   r0c00cn0$ xclock
   r0c00cn0$ exit

would allocate 64 (virtual) cores, and the second line starts a simple X11 program, ``x11``,
which is only good to test if X11 programs work but should not be used for other purposes
than this on the clusters.


Method 2: With salloc
"""""""""""""""""""""

Non-X11 programs
''''''''''''''''

You can use ``salloc`` to create a resource allocation. ``salloc`` will wait until the
resources are available and then return a shell prompt. Note however that that shell
is running on the node where you ran ``salloc`` (likely a login node). Contrary to
the method just before this one based on ``srun``, the shell is **not** running on the
allocated resources. You can however run commands on the allocated resources via
``srun``.

**Note that in particular on clusters with multiple CPU architectures, you need to
understand Linux environments and the way they interact with Slurm very well as you
are now executing commands in two potentially incompatible sections of the cluster that
require different settings in the environment. So if you execute a command in the wrong
environment it may run inefficiently, or it may simply fail.**

There is no problem with Vaughan though as on that cluster all CPUs are of the same
generation.

E.g., to run a shared memory program on 16 (virtual) cores, the following commands
can be used:

.. code:: bash

   login$ salloc --ntasks=1 --cpus-per-task=16 --time=1:00:00 --mem-per-cpu=3g

executed on a login node will return a shell on the login node. To then execute commands.
it is still better to rebuild the environment just as for a batch script as some modules
will use different settings when they load in a Slurm environment. So let's use this shell
to start the demo program ``omp_hello`` on the allocated resources:

.. code:: bash

   login$ module --force purge
   login$ module load calcua/2020a vsc-tutorial
   login$ srun omp_hello
   login$ exit

It is essential in this example that ``omp_hello`` is started through ``srun`` as otherwise
it would be running on the login node rather than on the allocated resources. Also do not forget
to leave the shell when you have finished your interactive work!

For an MPI or hybrid MPI/OpenMP program you would proceed in exactly the same way, except that the
resource request is different to allocate all MPI tasks. E.g., to run the demo program
``mpi_omp_hello`` in an interactive shell and using 16 MPI processes and 8 threads per MPI
rank, you'd allocate the resources through

.. code:: bash

   login$ salloc --ntasks=16 --cpus-per-task=8 --time=1:00:00 --mem-per-cpu=3g

and then run the program with

.. code:: bash

   login$ module --force purge
   login$ module load calcua/2020a vsc-tutorial
   login$ srun mpi_omp_hello
   login$ exit

Note that since we are using all allocated resources, we don't need to specify the number of tasks
or virtual CPUs to ``srun``. It will take care of of properly distributing the job according to the
options specified when calling ``salloc``.


Running a shared memory X11 program with salloc
'''''''''''''''''''''''''''''''''''''''''''''''

As you can log on to a compute node while you have resources allocated on that node, you can also
use ``salloc`` to create an allocation and then use ``ssh`` to log on to the node that has been
allocated. This only makes sense if you allocate one node or less, as when you log on via ``ssh``,
you leave the Slurm environment and hence cannot rely on Slurm anymore to start tasks. Moreover,
if you have multiple jobs running on the node, you may inadvertently influence those jobs as
any work that you're doing in that ssh session is not fully under the control of Slurm anymore.

As when using ``srun``, the first step is to ensure that X11 access from the login node to your
local screen is properly set up.

Next, starting a session that uses a full node on Vaughan can be done as

.. code:: bash

   login$ salloc -n 1 -c 64 -t 1:00:00
   login$ ssh -X $SLURM_JOB_NODELIST
   r0c00cn0$ xclock
   r0c00cn0$ exit
   login$ exit

What this does is:

1. The first command, executed on the login node, creates an allocation for 64 cores. It returns with
   a shell prompt on the login node as soon as the allocation is ready.

2. Next we log on to the allocated compute node using ``ssh``.  The ``-X`` option is used to forwarded
   X11 traffic. As we allocate only a single node, ``$SLURM_JOB_NODELIST`` is just a single node and can be
   used as argument to ``ssh``.

3. It is important to note that now we are in our **home directory** on the compute node as ``ssh`` starts
   with a clean login shell. We can now execute X11 commands or anything we want to do and is supported on
   a compute node.

4. The first ``exit`` command leaves the compute node and returns to the login shell, **but still within the
   salloc command**.

5. Hence we need a second ``exit`` command to leave the shell created by ``salloc`` and free the resources for
   other users.

**So do not forget that you need to exit two shells to free the resources!**


