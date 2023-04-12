Hybrid MPI/OpenMP programs
==========================

MPI and OpenMP both have their advantages and disadvantages.

MPI can be used on distributed memory clusters and can scale to
thousands of nodes. However, it was designed in the days that clusters
had nodes with only one or two cores. Nowadays CPUs often have more than
ten cores and sometimes support multiple hardware threads (or logical
cores) per physical core (and in fact may need multiple threads to run
at full performance). At the same time, the amount of memory per
hardware thread is not increasing and is in fact quite low on several
architectures that rely on a large number of slower cores or hardware
threads to obtain a high performance within a reasonable power budget.
Starting one MPI process per hardware thread is then a waste of
resources as each process needs its communication buffers, OS resources,
etc. Managing the hundreds of thousands of MPI processes that we are
nowadays seeing on the biggest clusters, is very hard.

OpenMP on the other hand is limited to shared memory parallelism,
typically within a node of a cluster. Moreover, many OpenMP programs
don't scale past some tens of threads partly because of thread overhead
in the OS implementation and partly because of overhead in the OpenMP
run-time.

Hybrid programs try to combine the advantages of both to deal with the
disadvantages. Hybrid programs use a limited number of MPI processes
(\"MPI ranks\") per node and use OpenMP threads to further exploit the
parallelism within the node. An increasing number of applications is
designed or re-engineered in this way. The optimum number of MPI
processes (and hence OpenMP threads per process) depends on the code,
the cluster architecture and the problem that is being solved, but often
one or, on newer CPUs such as the Intel Haswell, two MPI processes per
socket (so two to four for a typical two-socket node) is close to
optimal. Compiling and starting such applications requires some care as
we explain on this page.

Preparing your hybrid application to run
----------------------------------------

To compile and link your hybrid application, you basically have to
combine the instructions for MPI and OpenMP programs: use
``mpicc -fopenmp`` for the GNU compilers and ``mpiicc -qopenmp`` for the
Intel compilers ( ``mpiicc -openmp`` for older versions) or the
corresponding MPI Fortran compiler wrappers for Fortran programs.

Running hybrid programs on the VSC clusters
-------------------------------------------

When running a hybrid MPI/OpenMP program, fewer MPI processes have to be
started than there are logoical cores available to the application as
every process uses multiple cores in OpenMP parallelism. Yet when
requesting logical cores per node to the scheduler, one still has to
request the total number of cores needed per node. Hence the PBS
property \\"ppn\" should not be read as \\"processes per node\" but
rather as \\"logical cores per node\" or \\" processing units per
node\". Instead we have to tell the MPI launcher ( ``mpirun`` for most
applications) to launch fewer processes than there are logical cores on
a node and tell each MPI process to use the correct number of OpenMP
threads.

For optimal performance, the threads of one MPI process should be put
together as close as possible in the logical core hierarchy implied by
the cache and core topology of a given node. E.g., on a dual socket node
it may make a lot of sense to run 2 MPI processes with each MPI process
using all cores on a single socket. In other applications, it might be
better to run only one MPI process per node, or multiple MPI processes
per socket. In more technical words, each MPI process runs in its MPI
domain consisting of a number of logical cores, and we want these
domains to be non-overlapping and fixed in time during the life of the
MPI job and the logical cores in the domain to be \\"close\" to each
other. This optimises the use the memory hierarchy (cache and RAM).

OpenMP has several environment variables that can then control the
number of OpenMP threads and the placement of the threads in the MPI
domain. All of these may also be overwritten by the application, so it
is not a bullet-proof way to control the behaviour of OpenMP
applications. Moreover, some of these environment variables are
implementation-specific and hence are different between the Intel and
GNU OpenMP runtimes. The most important variable is ``OMP_NUM_THREADS``.
It sets the number of threads to be used in parallel regions. As
parallel constructs can be nested, a process may still start more
threads than indicated by ``OMP_NUM_THREADS``. However, the total number
of threads can be limited by the variable ``OMP_THREAD_LIMIT``.

Script mympirun (VSC)
---------------------

The mympirunn script is developed by the UGent VSC-team to cope with
differences between different MPI implementations automatically. It
offers support for hybrid programs through the ``--hybrid`` command line
switch to specify the number of processes per node. The number of
threads per process can then be computed by dividing the number of
logical cores per node by the number of processes per node.

E.g., to run a hybrid MPI/OpenMP program on 2 nodes using 20 cores on
each node and running 4 MPI ranks per node (hence 5 OpenMP threads per
MPI rank), your script would contain

::

   #PBS -l nodes=2:ppn20

near the top to request the resources from the scheduler. It would then
load the appropriate module with the mympirun command:

::

   module load vsc-mympirun

(besides other modules that are needed to run your application) and
finally start your application:

::

   mympirun --hybrid=4 ./hybrid_mpi

assuming your executable is called hybrid_mpi and resides in the working
directory. The mympirun launcher will automatically determine the
correct number of MPI processes to start based on the resource
specifications and the given number of processes per node (the
``--hybrid`` switch).

Intel toolchain (Intel compilers and Intel MPI)
-----------------------------------------------

On Intel MPI defining the MPI domains is done through the environment
variable ``I_MPI_PIN_DOMAIN``. Note however that the Linux scheduler is
still free to move all threads of a MPI process to any core within its
MPI domain at any time, so there may be a point in further pinning the
OpenMP threads through the OpenMP environment variables also. This is
definitely the case if there are more logical cores available in the
process partition than there are OpenMP threads. Some environment
variables to influence the thread placement are the Intel-specific
variable ``KMP_AFFINITY`` and the OpenMP 3.1 standard environment
variable ``OMP_PROC_BIND``.

In our case, we want to use all logical cores of a node but make sure
that all cores for a domain are as close together as possible. The
easiest way to accomplish this is to set ``OMP_NUM_THREADS`` to the
desired number of OpenMP threads per MPI process and then set
``I_MPI_PIN_DOMAIN`` to the value omp:

::

   export I_MPI_PIN_DOMAIN=omp

The longer version is

::

   export I_MPI_PIN_DOMAIN=omp,compact

where compact tells the launcher explicitly to pack threads for a single
MPI process as close together as possible. This layout is the default on
current versions of Intel MPI so it is not really needed to set this. An
alternative, when running 1 MPI process per socket, is to set

::

   export I_MPI_PIN_DOMAIN=socket

To enforce binding of each OpenMP thread to a particular logical core,
one can set

::

   export OMP_PROC_BIND=true

As an example, assume again we want to run the program ``hybridmpi`` on
2 nodes containing 20 cores each, running 4 MPI processes per node, so 5
OpenMP threads per process.

The following are then essential components of the job script:

-  Specify the resource requirements:
   ``#PBS -lnodes=2:ppn=20``
-  Load the modules, including one which contains Intel MPI, e.g.,
   ``module load intel``
-  Create a list of unique hosts assigned to the job
   ``export HOSTS=$(sort -u $PBS_NODEFILE | paste -s -d,)`` This
   step is very important; the program will not start with the correct
   number of MPI ranks if it is not provided with a list of unique host
   names.
-  Set the number of OpenMP threads per MPI process:
   ``export OMP_NUM_THREADS=5``
-  Pin the MPI processes:
   ``export I_MPI_PIN_DOMAIN=omp``
-  And launch hybrid_mpi using the Intel MPI launcher and specifying 4
   MPI processes per host:
   ``mpirun -hosts $HOSTS -perhost 4 ./hybrid_mpi``

| In this case we do need to specify both the total number of MPI ranks
  and the number of MPI ranks per host as we want the same number of MPI
  ranks on each host.
| In case you need a more automatic script that is easy to adapt to a
  different node configuration or different number of processes per
  node, you can do some of the computations in Bash. The number of
  processes per node is set in the shell variable
  ``MPI_RANKS_PER_NODE``. The above commands become:

::

   #! /bin/bash -l
   # Adapt nodes and ppn on the next line according to the cluster your're using!#PBS -lnodes=2:ppn=20
   ...
   MPI_RANKS_PER_NODE=4
   #
   module load intel
   #
   export HOSTS=`sort -u $PBS_NODEFILE | paste -s -d,`
   #
   export OMP_NUM_THREADS=$(($PBS_NUM_PPN / $MPI_RANKS_PER_NODE))
   #
   export OMP_PROC_BIND=true
   #
   export I_MPI_PIN_DOMAIN=omp
   #
   mpirun -hosts $HOSTS -perhost $MPIPROCS_PER_NODE ./hybrid_mpi

Intel documentation on hybrid programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some documents on the Intel web site that contain more information on
developing and running hybrid programs:

-  `Interoperability with OpenMP API`_ in the `MPI Reference Manual`_
   explains the concept of MPI domains and how they should be used/set
   for hybrid programs.
-  `Beginning Hybrid MPI/OpenMP Development`_,
   useful if you develop your own code.

FOSS toolchain (GCC and Open MPI)
---------------------------------

Open MPI has very flexible options for process and thread placement, but
they are not always easy to use. There is however also a simple option
to indicate the number of logical cores you want to assign to each MPI
rank (MPI process): ``-cpus-per-proc <num>`` with <num> the number of
logical cores assigned to each MPI rank.

You may want to further control the thread placement one can using the
standard OpenMP mechanism, e.g. the GNU-specific variable
``GOMP_CPU_AFFINITY`` or the OpenMP 3.1 standard environment variable
``OMP_PROC_BIND``. As long as we want to use all cores, it won't matter
whether ``OMP_PROC_BIND`` is set to true, close or spread. However,
setting ``OMP_PROC_BIND`` to true is generally a safe choice to assure
that all threads remain on the same core as they were started on to
improve cache performance.

Essential elements of your job script are:

::

   #! /bin/bash -l
   # Adapt nodes and ppn on the next line according to the cluster your're using!
   #PBS -lnodes=2:ppn=20
   ...
   #
   module load foss
   #
   export OMP_NUM_THREADS=5
   #
   export MPI_NUM_PROCS=$(( ${PBS_NP}/${OMP_NUM_THREADS} ))
   #
   mpirun --np ${MPI_NUM_PROCS} \
          --map-by socket:PE=${OMP_NUM_THREADS} \
          --bind-to core \
          ./hybrid_mpi
                  

Open MPI allows a lot of control over process placement and rank
assignment. The Open MPI mpirun command has several options that
influence this process:

-  ``--map-by`` influences the mapping of processes on the available
   processing resources
-  ``--rank-by`` influences the rank assignment
-  ``--bind-to`` influences the binding of processes to sets of
   processing resources
-  ``--report-bindings`` can then be used to report on the process
   binding.

More information can be found in the manual pages for ``mpirun`` which
can be found on the Open MPI webpages `Open MPI Documentation`_ and in the following
presentations:

-  Poster paper \\"`Locality-Aware Parallel Process Mapping for Multi-Core HPC Systems`_\" 
-  Slides from the presentation \\"`Open MPI Explorations in Process Affinity`_\" from EuroMPI'13 

