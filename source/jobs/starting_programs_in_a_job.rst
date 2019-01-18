Starting programs in a job
==========================

This page describes the part of the job script that actually does the
useful work and runs the programs you want to run.

When your job is started by the scheduler and the resource manager, your
job script will run as a regular script on the first core of the first
node assigned to the job. **The script runs in your home directory**,
which is not the directory where you will do your work, and with the
standard user environment. So before you can actually start your
program(s), you need to set up a proper environment. On a cluster, this
is a bit more involved than on your PC, partly also because multiple
versions of the same program may be present on the cluster, or there may
be conflicting programs that make it impossible to offer a single set-up
that suits all users.

Setting up the environment
--------------------------

Changing the working directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As explained above, the job script will start in your home directory,
which is not the place where you should run programs. So the first step
will almost always be to switch to the actual working directory (the
bash ``cd`` command).

-  In most cases, you simply want to start your job in the directory
   from which you submitted your job. Torque offers the environment
   variable ``PBS_O_WORKDIR`` for that purpose. So for most users, all
   you need is simply ``cd $PBS_O_WORKDIR`` as the first actual command
   in your job script.
-  On all VSC clusters we also define a number of environment variables
   that point to different file systems that you have access to. They
   may also be useful in job scripts, and may help to make your job
   script more portable to other VSC clusters. An overview of
   environment variables that point to various file systems is given on
   the page on :doc:`where which data should be
   stored<../access/where_can_i_store_what_kind_of_data>`.

Loading modules
~~~~~~~~~~~~~~~

The next step consists of loading the appropriate modules. This is no
different from loading the modules on the login nodes to prepare for
your job or when running programs on interactive nodes, so we refer to
the :ref:`modules system<module-system-basics>` page.

Useful Torque environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Torque defines a lot of environment variables on the compute nodes on
which your job runs, They can be very useful in your job scripts. Some
of the more important ones are:

-  ``PBS_O_WORKDIR`` : The directory from which your job was submitted.
-  ``PBS_JOBNAME`` : The name of the job
-  ``PBS_JOBID`` : The unique jobid. This is very useful when
   constructing, e.g., unique file names.
-  ``PBS_NUM_NODES`` : The number of nodes you requested.
-  ``PBS_NUM_PPN`` : The number of cores per node requested.
-  ``PBS_NP`` : The total number of cores requested.
-  ``PBS_NODEFILE`` : This variable is used by several MPI
   implementation to get the node list from the resource manager when
   starting an MPI program. It will contain ``$PBS_NP`` lines.

There are also some variables that are useful if you use the Torque
command ``pbsdsh`` to execute a command on another node/core of your
allocation. We mention them here for completeness, but they will also be
elaborated on in the paragraph on ":ref:`Starting a single-core program on each assigned core`" further down this page.

-  ``PBS_NODENUM`` : The number of the node in your allocation. E.g.,
   when starting a job with ``-l nodes=3:ppn=5``, ``$PBS_NODENUM`` will
   be 0, 1 or 2 if the job script has actually been scheduled on three
   physically distinct nodes. As the job script executes on the first
   core of the allocation, its value will always be 0 in your job
   script.
-  ``PBS_VNODENUM`` : The number of the physical core or hyperthread in
   your allocation. The numbering continues across the nodes in the
   allocation, so in case of a job started with ``-l nodes=3:ppn=5``,
   ``$PBS_VNODENUM`` will be a number between 0 and 14 (0 and 14
   included). In your job script, its value will be 0.
-  ``PBS_TASKNUM`` : Number of the task. The numbering starts from 1 but
   continues across calls of ``pbsdsh``. The login script runs with
   ``PBS_TASKNUM`` set to 1. The first call to ``pbsdsh`` will start its
   numbering from 2, and so on.

Starting programs
-----------------

We show some very common start scenarios for programs on a cluster:

-  Shared memory programs with OpenMP as an example
-  Distributed memory programs with MPI programs as an example
-  An embarrassingly parallel job consisting of independent single-core
   runs combined in a single job script

Starting a single multithreaded program (e.g., an OpenMP program)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting a multithreaded program is easy. In principle, all you need to
do is call its executable as you would do with any program at the
command line.

However, often the program needs to be told how many threads to use. The
default behaviour depends on the program. Most programs will either use
only one thread unless told otherwise, or use one thread per core it can
detect. The problem with programs that do the latter is that if you have
requested only a subset of the cores on the node, the program will still
detect the total number of cores or hyperthreads on the node and start
that number of threads. Depending on the cluster you are using, these
threads will swarm out over the whole node and sit in the way of other
programs (often the case on older clusters) or will be contained in the
set of cores/hyperthreads allocated to the job and sit in each others
way (e.g., because they compete for the same limited cache space). In
both cases, the program will run way slower than it could.

You will also need to experiment a bit with the number of cores that can
actually be used in a useful way. This depends on the code and the size
of the problem you are trying to solve. The same code may scale to only
4 threads for a small problem yet be able to use all cores on a node
well when solving a much larger problem.

How to tell the program the number of threads to use, also differs
between programs. Typical ways are through an environment variable or a
command line option, though for some programs this is actually a
parameter in the input file. Many scientific shared memory programs are
developed using OpenMP directives. For these programs, the number of
threads can be set through the environment variable OMP_NUM_THREADS. The
line

::

   export OMP_NUM_THREADS=$PBS_NUM_PPN

will set the number of threads to the value of ``ppn`` used in your job
script.

Starting a distributed memory program (e.g., an MPI program)
------------------------------------------------------------

Starting a distributed memory program is a bit more involved as they
always involve more than one Linux proces. Most distributed memory
programs in scientific computing are written using the the Single
Program Multiple Data paradigm: A single executable is ran on each core,
but each cores works on a different part of the data. And the most
popular technique for developing such programs is by using the MPI
(Message Passing Interface) library.

Distributed memory programs are usually started through a starter
command. For MPI programs, this is ``mpirun`` or ``mpiexec`` (often one
is an alias for the other). The command line arguments for mpirun differ
between MPI implementations. We refer to the documentation on
:doc:`toolchains<../software/toolchains>` for more information on the
implementations supported at the VSC. As most MPI implementations in use
at the VSC recognise our resource manager software and get their
information about the number of nodes and cores directly from the resource
manager, it is usually sufficient to start your MPI program using

::

   mpirun <mpi-program>

where ``<mpi-program>`` is your MPI program and its command line
arguments. This will start one instance of your MPI program on each core
or hyperthread assigned to the job.

Programs using different distributed memory libraries may use a
different starter program, and some programs come with a script that
will call mpirun for you, so you can start those as a regular program.

Some programs use a mix of MPI and OpenMP (or a combination of another
distributed and shared memory programming technique). Examples are some
programs in Gromacs and QuantumESPRESSO. The rationale is that a single
node on a cluster may not be enough, so you need distributed memory,
while a shared memory paradigm is often more efficient in exploiting
parallelism in the node. You'll need additional implementation-dependent
options to mpirun to start such programs and also to define how many
threads each instance can use. There is some information specifically
for :doc:`hybrid MPI/OpenMP programs<../software/hybrid_mpi_openmp_programs>`.
We advise you to contact user
support to help you figuring out the right options and values for those
options if you are not sure which options and values to use.

Starting a single-core program on each assigned core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A rather common use case on a cluster is running many copies of the same
program independently on a different data set. It is not uncommon that
those programs are not or very poorly parallelised and run on only a
single core. Rather than submitting a lot of single core jobs, it is
easier for the scheduler if those jobs are bundled in a single job that
fills a whole node. Our job scheduler will try to fill a whole node
using multiple of your jobs, but this doesn't always work right. E.g.,
assume a cluster with 20-core nodes where some nodes have 3 GB per core
available for user jobs and some nodes have 6 GB available. If your job
needs 5 GB per core (and you specify that using the ``mem`` or ``pmem``
parameters), but you don\\t explicitly tell that you want to use the
nodes with 6 GB per core, the scheduler may still schedule the first job
on a node with only 3 GB per core, then try to fill up that node further
with jobs from you, but once half the node is filled discover that there
is not enough memory left to start more jobs, leaving half of the CPU
capacity unused.

To ease combining jobs in a single larger job, we advise to have a look
at the :doc:`Worker framework <worker_frameworklllx>`. It
helps you to organise the input to the various instances of your program
for many common scenarios.

Should you decide to start the instances of your program yourself, we
advise to have a look at the Torque ``pbsdsh`` command rather than ssh.
This assures that all programs will execute under the full control of
the resource manager on the cores allocated to your job. The variables
``PBS_NODENUM``, ``PBS_VNODENUM`` and ``PBS_TASKNUM`` can be used to
determine on which core you are running and to select the appropriate
input files. Note that in most cases, it will actually be necessary to
write a second script besides your job script. That second script then
uses these variables to compute the names of the input and the output
files and start the actual program you want to run on that core.

To further explore the meaning of ``PBS_NODENUM``, ``PBS_VNODENUM`` and
``PBS_TASKNUM`` and to illustrate the use of ``pbsdsh,`` consider the
job script

::

   #! /bin/bash
   cd $PBS_O_WORKDIR
   echo \"Started with nodes=$PBS_NUM_NODES:ppn=$PBS_NUM_PPN\"
   echo \"First call of pbsdsh\"
   pbsdsh bash -c 'echo \"Hello from node $PBS_NODENUM ($HOSTNAME) vnode $PBS_VNODENUM task $PBS_TASKNUM\"'
   echo \"Second call of pbsdsh\"
   pbsdsh bash -c 'echo \"Hello from node $PBS_NODENUM ($HOSTNAME) vnode $PBS_VNODENUM task $PBS_TASKNUM\"'

Save this script as \\"testscript.pbs\" and execute it for different
numbers of nodes and cores-per-node using

::

   qsub -l nodes=4:ppn=5 testscript.pbs

(so using 4 nodes and 5 cores per node in this example). When calling
``qsub``, it will return a job number, and when the job ends you will
find a file testscript.pbs.o<number_of_the_job> in the directory where
you executed ``qsub``.

For more information on the pbsdsh command, check the manual page
(``man pbsdsh``), or refer to the the Torque
manual on the `Adaptive Computing documentation`_ web site.

-  `Torque 6.0.1 documentation`_ (Antwerp clusters, Hydra and BrENIAC)
-  `Torque 5.1.x documentation`_ (Thinking, muk).

.. include:: links.rst
