.. _job types:

Example job types
=================

Shared memory job
-----------------

A shared memory program consists of a single task. The number of cores you would
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

The following job script provides an example. It assumes there is a program
``omp_hello`` in the current directory compiled with the intel/2020a toolchain.
It will be run on 10 cores.

.. code:: bash

   #! /bin/bash
   #
   #SBATCH --job-name=OpenMP-demo
   #SBATCH --ntasks=1 --cpus-per-task=10 --mem=2g
   #SBATCH --time=05:00

   # Build the environment (UAntwerp example)
   module --force purge
   module load calcua/2020a
   module load vsc-tutorial

   # Set the number of threads
   export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

   # Run the program
   omp_hello

In this example, ``omp_hello`` is a demo program contained in the (UAntwerp)
``vsc-tutorial`` module that will simply print a message from each thread. The
``vsc-tutorial`` module also loads the ``intel/2020a`` module as that compiler
was used to compile the programs in the module.

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
(UAntwerp) ``vsc-tutorial`` module. The ``vsc-tutorial`` module will also load
the ``intel/2020a`` module for the libraries used by the compiler and the
MPI library.

.. code:: bash

   #! /bin/bash
   #
   #SBATCH --job-name=mpihello
   #SBATCH --ntasks=56 --cpus-per-task=1 --mem-per-cpu=512m
   #SBATCH --time=5:00

   # Build the environment (UAntwerp example)
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

   # Build the environment (UAntwerp example)
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
easily using a spreadsheet program. For information on how to use atools, we refer to the
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

   r0c00cn0$ # Build the environment (UAntwerp example)
   r0c00cn0$ module --force purge
   r0c00cn0$ module load calcua/2020a vsc-tutorial
   r0c00cn0$ # Start the application
   r0c00cn0$ srun mpi_hello
   r0c00cn0$ exit

The ``exit`` command at the end ends the shell and hence the interactive job.


Running X11 programs
""""""""""""""""""""

You can also use ``srun`` to start an interactive session with X11 support. However, before
starting a session you should ensure that you can start X11 programs from the session from
you will be starting ``srun``. Check the corresponding guide for your operating system:

- :ref:`Windows <windows_gui>`
- :ref:`Linux <linux_gui>`
- :ref:`macOS <macos_gui>`

X11 programs rarely use distributed memory parallelism, so in most case you will be requesting
just a single task. To add support for X11, use the ``--x11`` option before ``--pty``:

.. code:: bash

   login$ srun -n 1 -c 64 -t 1:00:00 --x11 --pty bash
   r0c00cn0$ xclock
   r0c00cn0$ exit

would allocate 64 cores, and the second line starts a simple X11 program, ``xclock``,
to test if X11 programs work.
