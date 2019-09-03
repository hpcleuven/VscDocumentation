.. _standard terms:

What are standard terms used in HPC?
====================================

HPC cluster
   A relatively tightly coupled collection of compute
   nodes, the interconnect typically allows for high bandwidth, low
   latency communication. Access to the cluster is provided through a
   login node. A resource manager and scheduler provide the logic to
   schedule jobs efficiently on the cluster. A detailed description of
   the :ref:`VSC clusters and other
   hardware <hardware>` is available.
Compute node
   An individual computer, part of an HPC cluster.
   Currently most compute nodes have two sockets, each with a single CPU,
   volatile working memory (RAM), a hard drive, typically small, and
   only used to store temporary files, and a network card. The hardware
   specifications for the various :ref:`VSC compute
   nodes <hardware>` is available.
CPU
   Central Processing Unit, the chip that performs the actual
   computation in a compute node. A modern CPU is composed of numerous
   cores, typically 10 to 36. It has also several cache levels that help
   in data reuse.
Core
   Part of a modern CPU, a core is capable of running
   processes, and has its own processing logic and floating point unit.
   Each core has its own level 1 and level 2 cache for data and
   instructions. Cores share last level cache.
Cache
   A relatively small amount of (very) fast volatile memory (when
   compared to regular RAM), on the CPU chip. A modern CPU has three
   cache level, L1 and L2 are specific to each core, while L3 (also
   referred to as Last Level Cache, LLC) is shared among all the cores
   of a CPU.
RAM
   Random Access Memory used as working memory for the CPUs. On
   current hardware, the size of RAM is expressed in gigabytes (GB). The
   RAM is shared between the two CPUs on each of the sockets. This is
   volatile memory in the sense that once the process that creates the
   data ends, the data in the RAM is no longer available. The complete
   RAM can be accessed by each core.
Walltime
   The actual time an application runs (as in clock on the
   wall), or is expected to run. When submitting a job, the walltime
   refers to the maximum time the application can run, i.e.,
   the requested walltime. For accounting purposes, the walltime is the
   time the application actually ran, typically less than the
   requested walltime.
Node-hour
   Unit of work indicating that an application ran for a
   time *t* on *n* nodes, such that *n*\ \*\ *t* = 1 hour. Using 1 node
   for 1 hour is 1 node-hour. This is irrespective of the number of
   cores on the node you actually use.
Node-day
   Unit of work indicating that an application ran for a
   time *t* on *n* nodes such that *n*\ \*\ *t* = 24 hours. Using 3
   nodes for 8 hours results in 1 node day.
Core-hour
   Unit of work indicating that an application ran for a
   time *t* on *p* cores, such that *p*\ \*\ *t* = 1 hour. Using 20
   cores, no matter on how many nodes, for 1 hour results in 20
   core-hours.
Memory requirement
   The amount of RAM required to successfully run
   an application. It can be specified per process for a distributed
   application, expressed in GB.
Storage requirement
   The amount of disk space required to store the
   input and output of an application, expressed in GB or TB.
Temporary storage requirement
   The amount of disk space needed to store temporary files during the run of
   an application, expressed in GB or TB.
Single user per node policy
   Indicates that when a process of
   user *A* runs on a compute node, no process of another user will run
   on that compute node concurrently, i.e., the compute node will be
   exclusive to user *A*. However, if one or more processes of user *A*
   are running on a compute node, and that node's capacity in terms of
   available cores and memory is not exceeded, processes that are part of
   another job submitted by user *A* may start on that compute node.
Single job per node policy
   Indicates that when a process of a job is running on a compute node,
   no other job will concurrently run on that node, regardless of the
   resource that still remain available.
Serial application
   A program that runs a single process, with a
   single thread. All computations are done sequentially, i.e., one
   after the other, no explicit parallelism is used.
Shared memory application
   An application that uses multiple threads for its computations, ideally
   concurrently executed on multiple cores, one per thread.
   Each thread has access to the
   application's global memory space (hence the name), and has some
   thread-private memory. A shared memory application runs on a single
   compute node. Such an application is also referred to as a multi-core
   or a multi-threaded application.
Threads
   A process can concurrently perform multiple computations, i.e., program
   flows.  In scientific applications, threads typically process their own
   subset of data, or a subset of loop iterations.
OpenMP
   A standard for shared memory programming using C/C++/Fortran that makes
   abstraction of explicit threads.  OpenMP is widely used for scientific
   programming.
Distributed application
   An application that uses multiple processes.  The application's
   processes can run on multiple compute nodes.  These processes
   communicate by exchanging messages, typically implemented by calls
   to an MPI library. Messages can be used to exchange data and coordinate
   the execution.
Process
   An independent computation running on a computer. It may
   interact with other processes, and it may run multiple threads. A
   serial and shared memory application run as a single process, while a
   distributed application consists of multiple, coordinated processes.
MPI
   Message Passing Interface, a de-facto standard that defines
   functions for inter-process communication. Many implementations in
   the form of libraries exist for C/C++/Fortran, some vendor specific.
GPU
   A Graphical Processing Unit is a hardware component specifically designed
   to perform graphics related tasks efficiently.  GPUs have been pressed
   into service for scientific computing.  A compute node can be equipped
   with multiple GPUs.  Software has to be designed specifically to use
   GPUs, and for scientific computing, CUDA and OpenACC are the most
   popular programming paradigms.
GPGPU
   General Purpose computing on Graphical Processing Units refers to using
   graphic accelerators for non-graphics related tasks such as scientific
   computing.
CUDA
   Compute Unified Device Architecture, an extension to the C programming
   language to develop software that can use GPU for computations.  CUDA
   application run exclusively on NVIDIA hardware.
OpenACC
   Open ACCelerators is a standard for developing C/C++/Fortran applications
   that can use GPUs for general purpose computing.  OpenACC is mainly
   targeted to scientific computing.
