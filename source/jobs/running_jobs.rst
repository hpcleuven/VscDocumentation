.. _running jobs:

Running jobs in Slurm
=====================

VSC clusters using the Slurm job scheduler

.. include:: clusters_slurm.rst

.. note:: Other clusters might use the :ref:`Torque job scheduler <running jobs torque>`

This page covers the more basic Slurm use, including starting jobs, basic job management
and some templates for job scripts for various scenarios. It is the minimum a user should
master. A second page describes :ref:`more advanced use of Slurm <job advanced>`.

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
accepts Torque job scripts with some limitations) and will also be the scheduler on Hortense, the
successor of the BrENIAC Tier-1 system.

Historically, Slurm was an acronym of **S**\imple **L**\inux **U**\tility for
**R**\esource **M**\anagement. The development started around 2002 at Lawrence Livermore
National Lab as a resource manager for Linux clusters. Slurm has always had a very modular
architecture. From 2008 on increasingly sophisticated scheduling plugins were added
to Slurm. Nowadays it is used on some of the largest systems in the world. Slurm is
completely open source though commercial support can be obtained from SchedMD, a
spin-off company of the Slurm development.

.. note:: Glossary of concepts and terms related to Slurm

    Nodes
      A node is (commonly) the largest part of the cluster running a single
      operating system image, and hence capable of supporting a shared memory
      program. Nodes are connected with each other through an interconnect, and
      communication between nodes is done via message passing.

    CPU
      The CPU is the Computer Processing Unit. Each node in a cluster can have
      one or multiple CPUs and each CPU has multiple cores capable of executing
      compute instructions.

    Core
      A core is the smallest processor of the CPU. It can execute a single
      *thread* of instructions.

    Partition
      Groups of nodes with limits and access controls, basically the equivalent
      of a queue in Torque. A node can be part of multiple partitions.

    Job
      A resource allocation request.

    Job step
      A set of (possibly parallel) tasks within a job. A job can consist of
      just a single job step or can contain multiple job steps which may use all or just
      a part of the resource allocation of a job and can run sequentially or in parallel
      (or a mix of that). The job script itself is a special job step, called the batch
      job step, but additional job steps can be created (e.g., for running a
      parallel MPI application).

    Task
      A task is executed within a job step and essentially corresponds to a
      Linux process: a single- or multithreaded process, or a single rank within a MPI
      process. Specifying the number of tasks one wants to run simultaneously and the
      number of cores per task is a very convenient way to request resources to Slurm
      as afterwards starting a MPI or hybrid MPI/OpenMP program using the ``srun``
      command is very easy.

.. toctree::
   :maxdepth: 3

   job_submission
   job_management
   job_types
   job_advanced
   slurm_pbs_comparison

