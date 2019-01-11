The job system: What and why?
=============================

A batch system
--------------

There are two important differences between a supercomputer and your
personal laptop or smartphone apart from the amount of compute power it
can deliver if used properly: As it is a large and expensive machine and
as not every program can use all of its processing power, it is a
multi-user machine, and furthermore it is optimised to run large
parallel programs in such a way that they don't interfere too much with
each other. So your compute resources will be as much as possible
isolated from those assigned to another user. The latter is necessary to
ensure fast and predictable execution of large parallel jobs as the
performance of a parallel application will always be limited by the
slowest node, process or thread.

This has some important consequences:

#. As a user, you don't get the whole machine, but a specific part of
   it, and so you'll have to specify which part you need for how long.
#. Often more capacity is requested than available at that time. Hence
   you may have to wait a little before you get the resources that you
   request. To organise this in a proper way, every supercomputer
   provides a queueing system.
#. Moreover, as you often have to wait a bit before you get the
   requested resources, it is not well suited for interactive work.
   Instead, most work on a supercomputer is done in **batch mode**:
   Programs run without user interaction, reading their input from file
   and storing their results in files.

In fact, another reason why interactive work is discouraged on most
clusters is because interactive programs rarely fully utilise the
available processors but waste a lot of time waiting for new user input.
Since that time cannot be used by another user either (remember that
your work is isolated from that from other users), is is a waste of very
expensive compute resources.

A **job** is an entity of work that you want to do on a supercomputer. A
job consists of the execution of one or more programs and needs certain
resources for some time to be able to execute. **Batch jobs** are
described by a **job script**. This is like a regular linux shell script
(usually for the bash shell), but it usually contains some extra
information: a description of the resources that are needed for the job.
A job is then submitted to the cluster and placed in a queue (managed by
a piece of software called the **queue manager**). A **scheduler** will
decide on the priority of the job that you submitted (based on the
resources that you request, your past history and policies determined by
the system managers of the cluster). It will use the **resource
manager** to check which resources are available and to start the job on
the cluster when suitable resources are available and the scheduler
decides it is the job's time to run.

At the VSC we use two software packages to perform these tasks.
**Torque** is an open source package that performs the role of queue and
resource manager. **Moab** is a commercial package that provides way
more scheduling features than its open source alternatives. Though both
packages are developed by the same company and are designed to work well
with each other, they both have their own set of commands with often
confusing command line options.

Anatomy of a job script
-----------------------

A typical job script looks like:

::

   #!/bin/bash
   #PBS –l nodes=1:ppn=20
   #PBS –l walltime=1:00:00
   #PBS -o stdout.$PBS_JOBID
   #PBS -e stderr.$PBS_JOBID

   module load MATLAB
   cd $PBS_O_WORKDIR

   matlab -r fibo

We can distinguish 4 sections in the script:

#. The first line simply tells that this is a shell script.
#. The second block, the lines that start with ``#PBS``, specify the
   resources and tell the resource manager where to store the standard
   output and standard error from the program. To ensure unique file
   names, the author of this script has chosen to put the \\"Job ID\", a
   unique ID for every job, in the name.
#. The next two lines create the proper environment to run the job: it
   loads a module and changes the working directory to the directory
   from which the job was submitted (this is what is stored in the
   environment variable\ ``$PBS_O_WORKDIR``).
#. Finally the script executes the commands that are the core of the
   job. In this simple example, this is just a single command, but it
   could as well be a whole bash script.

In other pages of the documentation in this section, we'll go into more
detail on specifying resource requirements, output redirection and
notifications and on environment variables that are set by the scheduler
and can be used in your job.

Assuming that this script is called myscript.pbs, the job can then be
submitted to the queueing system with the command ``qsub myscript.pbs``.

Note that if you use a system at the KU Leuven, including the Tier-1
system BrENIAC, you need credits. When submitting your job, you also
need to tell ``qsub`` which credits to use. We refer to the page on
\\"\ `Credit system
basics <\%22/cluster-doc/running-jobs/credit-system-basics\%22>`__\\".

Structure of this documentation section
---------------------------------------

-  The page on `specifying job
   requirements <\%22cluster-doc/running-jobs/specifying-requirements\%22>`__
   describes everything that goes in the second block of your job
   script: the specification of the resources, notifications, etc.
-  The page on `starting programs in your
   job <\%22/cluster-doc/running-jobs/starting-programs-in-job\%22>`__
   describes the third and fourth block: Setting up the environment and
   starting a program.
-  The page on `starting and managing
   jobs <\%22/cluster-doc/running-jobs/submitting-managing-jobs\%22>`__
   describes the main Torque and Moab commands to submit and then manage
   your jobs and to follow up how they proceed trough the scheduling
   software.
-  The `worker
   framework <\%22/cluster-doc/running-jobs/worker-framework\%22>`__ is
   a framework developed at the VSC to bundle a lot of small but related
   jobs into a larger parallel job. This makes life a lot easier for the
   scheduler as the scheduler is optimised to run a limited number of
   large long-duration jobs as efficient as possible and not to deal
   with thousands or millions of small short jobs.

Some background information
---------------------------

*For those readers who want some historical background to understand
where the complexity comes from.*

In the ’90s of the previous century, there was a popular resource
manager called Portable Batch System, developed by a contractor for
NASA. This was open-sourced. But that contractor was acquired by another
company that then sold the rights to Altair Engineering that evolved the
product into the closed-source product PBSpro (which was then
open-sourced again in the summer of 2016). The open-source version was
forked by another company that is now known as Adaptive Computing and
renamed to Torque. Torque remained open–source. The name stands for
Terascale Open-source Resource and QUEue manager. Even though the name
was changed, the commands remained which explains why so many commands
still have the abbreviation PBS in their name.

The scheduler Moab evolved from MAUI, an open-source scheduler. Adaptive
Computing, the company behind Torque and Moab, contributed a lot to MAUI
but then decided to start over with a closed source product. They still
offer MAUI on their website though. MAUI used to be widely used in large
USA supercomputer centres, but most now throw their weight behind SLURM
with or without another scheduler.

"
