.. _job types:

Example job types
=================

Shared memory job
-----------------

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
-----------

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
-------------------------

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
------------------------------------

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
---------------------------------

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
---------------

Method 1: with srun
~~~~~~~~~~~~~~~~~~~

Interactively running shared memory programs
""""""""""""""""""""""""""""""""""""""""""""

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
""""""""""""""""""""""""""""""""""

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
""""""""""""""""""""

You can also use ``srun`` to start an interactive session with X11 support. However, before
starting a session you should ensure that you can start X11 programs from the session from
you will be starting ``srun``. Check the corresponding guide for your operating system:

- :ref:`Windows <Windows gui>`
- :ref:`Linux <Linux gui>`
- :ref:`macOS <macOS gui>`

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
~~~~~~~~~~~~~~~~~~~~~

Non-X11 programs
""""""""""""""""

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
"""""""""""""""""""""""""""""""""""""""""""""""

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


