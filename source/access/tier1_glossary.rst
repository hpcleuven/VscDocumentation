.. _Tier-1 application glossary:

Tier-1 application glossary
===========================

HPC cluster
   Relatively tightly coupled collection of compute nodes, the interconnect typically allows for high bandwidth, low latency communication. Access to the cluster is provided through a login node. A resource manager and scheduler provide the logic to schedule jobs efficiently on the cluster. A detailed description of the <a href=\"/infrastructure/hardware\">VSC clusters and other hardware</a> is available.
   
Compute node
   An individual computer, part of an HPC cluster.  Currently most compute node have two sockets, each with a single CPU, volatile working memory (RAM), a hard drive, typically small, and only used to store temporary files, and a network card. The hardware specifications for the various <a href=\"/infrastructure/hardware\">VSC compute nodes</a> is available.

CPU*
   Central Processing Unit, the chip that performs the actual computation in a compute node.  A modern CPU is composed of numerous cores, typically 8 or 10.  It has also several cache levels that help in data reuse.

Core
   Part of a modern CPU.  A core is capable of running processes, and has its own processing logic and floating point unit.  Each core has its own level 1 and level 2 cache for data and instructions. Cores share last level cache.

Cache
    A relatively small amount of (very) fast memory (when compared to regular RAM), on the CPU chip.  A modern CPU has three cache level, L1 and L2 are specific to each core, while L3 (also referred to as Last Level Cache, LLC) is shared among all the cores of a CPU.
    
RAM
   Random Access Memory used as working memory for the CPUs.  On current hardware, the size of RAM is expressed in gigabytes (GB). The RAM is shared between the two CPUs on each of the sockets.  This is volatile memory in the sense that once the process that creates the data ends, the data in the RAM is no longer available. The complete RAM can be accessed by each core.

Walltime
   The actual time an application runs (as in clock on the wall), or is expected to run. When submitting a job, the walltime refers to the maximum amount of time the application can run, i.e., the requested walltime.  For accounting purposes, the walltime is the amount of time the application actually ran, typically less than the requested walltime.

Node-hour
   unit of work indicating that an application ran for a time *t* on *n* nodes, such that *n* x *t* = 1 hour. Using 1 node for 1 hour is 1 node-hour. This is irrespective of the number of cores on the node you actually use.

Core-hour
   unit of work indicating that an application ran for a time *t* on *p* cores, such that *p* x *t* = 1 hour. Using 20 cores, no matter on how many nodes, for 1 hour results in 20 core-hours.

Node-day
   Unit of work indicating that an application ran for a time *t* on *n* nodes such that *n* x *t* = 24 hours. Using 3 nodes for 8 hours results in 1 node day.

Memory requirement
   The amount of RAM needed to successfully run an application.  It can be specified per process for a distributed application, expressed in GB.

Storage requirement
    The amount of disk space needed to store the input and output of an application, expressed in GB or TB.

Temporary storage requirement
   The amount of disk space needed to store temporary files during the run of an application, expressed in GB or TB.

Single user per node policy
    Indicates that when a process of user *A* runs on a compute node, no process of another user will run on that compute node concurrently, i.e., the compute node will be exclusive to user *A*.  However, if one or more processes of user *A* are running on a compute node, and that node's capacity in terms of available cores and memory is not exceeded, processes part of another job submitted by user *A* may start on that compute node.

Shared memory application
    An application that uses multiple cores for its computations, concurrent computations are executed by threads, typically one per core.  Each thread has access to the application's global memory space (hence the name), and has some thread-private memory. A shared memory application runs on a single compute node. See also multi-core application.

Multi-core application
    A multi-core application uses more than one core during its execution by running multiple threads, also called a shared memory application.

Distributed application
    An application that uses multiple compute nodes for its computations, concurrent computations are executed as processes.  These processes communicate by exchanging messages, typically implemented by calls to an MPI library.  Messages can be used to exchange data and coordinate the execution.
    
Serial application
   A program that runs a single process, with a single thread.  All computations are done sequentially, i.e., one after the other, no explicit parallelism is used.

Process
   An independent computation running on a computer.  It may interact with other processes, and it may run multiple threads.  A serial and shared memory application run as a single process, while a distributed application consists of multiple, coordinated processes.

Threads
   A process can perform multiple computations, i.e., program flows, concurrently.  In scientific applications, threads typically process their own subset of data, or a subset of loop iterations.

MPI
   Message passing interface, a de-facto standard that defines functions for inter-process communication. Many implementations in the form of libraries exist for C/C++/Fortran, some vendor specific.

OpenMP
   A standard for shared memory programming that makes abstraction of explicit threads.
