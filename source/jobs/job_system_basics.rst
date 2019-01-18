Job system basics
=================

**This page is outdated. Please check our updated \\"\ \ **\ `Running
jobs <\%22/cluster-doc/running-jobs\%22>`__\ **\ \\" section on the user
portal. If you came to this page following a link on a web page of this
site (and not via a search) you can help us improve the documentation by
mailing the URL of the page that brought you here
to\ **\ `kurt.lust@uantwerpen.be <\%22mailto:kurt.lust@uantwerpen.be\%22>`__\ **\ .**

Purpose
-------

When you connect to a cluster of the VSC, you have access to (one of)
the login nodes of the cluster. There you can prepare the work you want
to get done on the cluster by, e.g., installing or compiling programs,
setting up data sets, etc. The computations however, are *not* performed
on this login node. The actual work is done on the cluster's compute
nodes. These compute nodes are managed by the job scheduling software,
which decides when and on which compute nodes the jobs are run. This
how-to explains how to make use of the job system.

Defining and submitting your job
--------------------------------

Usually, you will want to have your program running in batch mode, as
opposed to interactively as you may be accustomed to. The point is that
the program can be started without without user intervention, i.e., you
having to enter any information or pressing any buttons. All necessary
input or options have to be specified on the command line, or in
input/config files. For the purpose of this how-to, we will assume you
want to run a Matlab calculation that you have programmed in a file
'my_calc.m'. On the command line, you would run this using:

::

   $ matlab -r my_calc

Next, you create a PBS script — a description of the job — and save it
as, e.g., 'my_calc.pbs', it contains:

::

   #!/bin/bash -l
   module load matlab
   cd $PBS_O_WORKDIR
   matlab -r my_calc

Important note: this PBS file has to be in UNIX format, if it is not,
your job will fail and generate rather weird error messages. If
necessary, you can conver it using

::

   $ dos2unix my_calc.pbs

It is this PBS script that can now be submitted to the cluster's job
system for execution, using the qsub command:

::

   $ qsub my_calc.pbs
   20030021.icts-p-svcs-1

The qsub command returns a job ID, i.e., a line similar to the one
above, that can be used to further manage your job, if needed. The
important part is the number, i.e., '10021'. The latter is a unique
identifier for the job, and it can be used to monitor and manage your
job.

**Note**: if you want to use project credits to run a job, you should
specify the project's name (e.g., 'lp_fluid_dynamics') using the
following option:

::

   $ qsub -A lp_fluid_dynamics calc.pbs

For more information on working with credits, see `How to work with job
credits <\%22/cluster-doc/running-jobs/credit-system-basics\%22>`__.

Monitoring and managing your job(s)
-----------------------------------

Using the job ID qsub returned, there are various ways to monitor the
status of you job, e.g.,

::

   $ qstat <jobid>

get the status information on your job

::

   $ showstart <jobid>

show an estimated start time for you job (note that this may be *very*
inaccurate)

::

   $ checkjob <jobid>

shows the status, but also the resources required by the job, with error
messages that may prevent you job from starting

::

   $ qstat -n <jobid>

show on which compute nodes you job is running, at least, when it is
running

::

   $ qdel <jobid>

removes a job from the queue so that it will not run, or stops a job
that is already running.

When you have multiple jobs submitted (or you just forgot about the job
ID), you can retrieve the status of all your jobs that are submitted and
have not finished yet using

::

   $ qstat -u <uid>

lists the status information of all your jobs, including their job IDs;
here, uid is your VSC user name on the system.

Specifying job requirements
---------------------------

Without giving more information about your job upon submitting it with
qsub, default values will be assumed that are almost never appropriate
for real jobs.

It is important to estimate the resources you need to successfully run
your program, e.g., the amount of time the job will require, the amount
of memory it needs, the number of CPUs it will run on, etc. This may
take some work, but it is necessary to ensure your jobs will run
properly.

For the simplest cases, only the amount of time is really important, and
it does not harm too much if you slightly overestimate it.

The qsub command takes several options to specify the requirements:

::

   -l walltime=2:30:00

the job will require 2 hours, 30 minutes to complete

::

   -l mem=4gb

the job requires 4 Gb of memory

::

   -l nodes=5:ppn=2

the job requires 5 compute nodes, and two CPUs (actually cores) on each
(ppn stands for processors per node)

::

   -l nodes=1:ivybridge

The job requires just one node, but it should have an Ivy Bridge
processor. A list with site-specific properties can be found in the next
section.

These options can either be specified on the command line, e.g.,

::

   $ qsub -l nodes=1:ivybridge,mem=16gb my_calc.pbs

or in the PBS script itself, so 'my_calc.pbs' would be modified to:

::

   #!/bin/bash -l
   #PBS -l nodes=1:ivybridge
   #PBS -l mem=4gb
   module load matlab
   cd $PBS_O_WORKDIR
   matlab -r my_calc

Note that the resources requested on the command line will override
those specified in the PBS file.

Available queues
----------------

Apart from specifying the walltime, you can also explicitly define the
queue you're submitting your job to. Queue names and/or properties might
be different on different sites. To specify the queue, add:

::

   -q queuename

where *queuename* is one of the possible queues shown below. A maximum
walltime is associated with each queue. Jobs specifying a walltime which
is larger than the maximal walltime of the requested queue, will not
start. The number of jobs currently running in the queue is shown in the
Run column, whereas the number of jobs waiting to get started, is shown
in the Que column.

We strongly advise against the explicit use of queue names. In almost
all cases it is much better to specify the resources you need with
``walltime`` etc. The system will then determine the optimal queue for
your application.

KU Leuven
~~~~~~~~~

::

   $ qstat -q
   server: icts-p-svcs-1
   Queue            Memory CPU Time Walltime Node  Run Que Lm  State
   ---------------- ------ -------- -------- ----  --- --- --  -----
   q24h               --      --    24:00:00   --   36  17 --   E R
   qreg               --      --    30:00:00   --    0   0 --   D R
   qlong              --      --    168:00:0   --    0   0 --   E S
   q21d               --      --    504:00:0     5   6   5 --   E R
   qicts              --      --       --      --    0   0 --   E R
   q1h                --      --    01:00:00   --    0  22 --   E R
   qdef               --      --       --      --    0  50 --   E R
   q72h               --      --    72:00:00   --   12   1 --   E R
   q7d                --      --    168:00:0    25  38   1 --   E R
                                                  ----- -----
                                                     92    96

The queues q1h, q24h, q72h, q7d and q21d use the new queue naming
scheme, while the other ones are still provided for compatibility with
older job scripts.

Submit to a gpu-node:
^^^^^^^^^^^^^^^^^^^^^

::

   qsub  -l partition=gpu,nodes=1:M2070 <jobscript>

or

::

   qsub  -l partition=gpu,nodes=1:K20Xm <jobscript>

depending which GPU node you would like to use if you don't 'care' on
which type of GPU node your job ends up you can just submit it like
this:

::

   qsub  -l partition=gpu <jobscript>

Submit to a Phi node:
^^^^^^^^^^^^^^^^^^^^^

::

   qsub -l partition=phi <jobscript>

Submit to a debug node:
^^^^^^^^^^^^^^^^^^^^^^^

For very short/small jobs (max 30 minutes, max 2 nodes) you could
request (a) debug node(s). This could be useful if the cluster is very
busy and to avoid long queuetime for a debug job. There is a limit on
the number of jobs that a user can concurrently submit in this quality
of service.

You can submit like this to a debug node (remember to request a walltime
equal or smaller than 30 minutes):

::

   qsub -lqos=debugging,walltime=30:00 <jobscript>

UAntwerpen
~~~~~~~~~~

On hopper:

::

   $ qstat -q
   server: mn.hopper.antwerpen.vsc
   Queue            Memory CPU Time Walltime Node  Run Que Lm  State
   ---------------- ------ -------- -------- ----  --- --- --  -----
   q1h                --      --    01:00:00   --    0  24 --   E R
   batch              --      --       --      --    0   0 --   E R
   q72h               --      --    72:00:00   --   64   0 --   E R
   q7d                --      --    168:00:0   --    9   0 --   E R
   q24h               --      --    24:00:00   --   17   0 --   E R
                                                  ----- -----
                                                     90    24

The maximum job (wall)time on hopper is 7 days (168 hours).

On turing:

::

   $ qstat -q
   server: master1.turing.antwerpen.vsc
   Queue            Memory CPU Time Walltime Node  Run Que Lm  State
   ---------------- ------ -------- -------- ----  --- --- --  -----
   qreg               --      --       --      --    0   0 --   E R
   batch              --      --       --      --    0   0 --   E R
   qshort             --      --       --      --    0   0 --   E R
   qxlong             --      --       --      --    0   0 --   E R
   qxxlong            --      --       --      --    0   0 --   E R
   q21d               --      --    504:00:0   --    4   0 --   E R
   q7d                --      --    168:00:0   --   20   0 --   E R
   qlong              --      --       --      --    0   0 --   E R
   q24h               --      --    24:00:00   --   22   2 --   E R
   q72h               --      --    72:00:00   --   46   0 --   E R
   q1h                --      --    01:00:00   --    0   0 --   E R
                                                  ----- -----
                                                     92     2

The essential queues are q1h, q24h, q72h, q7d and q21d. The other queues
route jobs to one of these queues and exist for compatibility with older
job scripts. The maximum job execution (wall)time on turing is 21 days
or 504 hours.

To obtain more detailed information on the queues, e.g., qxlong, the
following command can be used:

::

   $ qstat -f -Q qxlong

This will list additional restrictions such as the maximum number of
jobs that a user can have in that queue.

Site-specific properties
------------------------

The following table contains the most common site-specific properties.

+-----------------------+-----------------------+-----------------------+
| site                  | property              | explanation           |
+=======================+=======================+=======================+
| UAntwerpen            | harpertown            | only use Intel        |
|                       |                       | processors from the   |
|                       |                       | Harpertown family     |
|                       |                       | (54xx)                |
+-----------------------+-----------------------+-----------------------+
| UAntwerpen            | westmere              | only use Intel        |
|                       |                       | processors from the   |
|                       |                       | Westmere family       |
|                       |                       | (56xx)                |
+-----------------------+-----------------------+-----------------------+
| KU Leuven, UAntwerpen | ivybridge             | only use Intel        |
|                       |                       | processors from the   |
|                       |                       | Ivy Bridge family     |
|                       |                       | (E5-XXXXv2)           |
+-----------------------+-----------------------+-----------------------+
| KU Leuven             | haswell               | only use Intel        |
|                       |                       | processors from the   |
|                       |                       | Haswell family        |
|                       |                       | (E5-XXXXv3)           |
+-----------------------+-----------------------+-----------------------+
| UAntwerpen            | fat                   | only use large-memory |
|                       |                       | nodes                 |
+-----------------------+-----------------------+-----------------------+
| KU Leuven             | M2070                 | only use nodes with   |
|                       |                       | NVIDIA Tesla M2070    |
|                       |                       | cards (combine with   |
|                       |                       | partition=gpu at KU   |
|                       |                       | Leuven)               |
+-----------------------+-----------------------+-----------------------+
| KU Leuven             | K20Xm                 | only use nodes with   |
|                       |                       | NVIDIA Tesla K20Xm    |
|                       |                       | cards (combine with   |
|                       |                       | partition=gpu at KU   |
|                       |                       | Leuven)               |
+-----------------------+-----------------------+-----------------------+
| KU Leuven             | K40c                  | only use nodes with   |
|                       |                       | NVIDIA Tesla K40c     |
|                       |                       | cards (combine with   |
|                       |                       | partition=gpu at KU   |
|                       |                       | Leuven)               |
+-----------------------+-----------------------+-----------------------+
| KU Leuven             | phi                   | only use nodes with   |
|                       |                       | Intel Xeon Phi cards  |
|                       |                       | (combine with         |
|                       |                       | partition=phi at KU   |
|                       |                       | Leuven)               |
+-----------------------+-----------------------+-----------------------+
| UAntwerpen            | ib                    | use Infiniband        |
|                       |                       | interconnect (only    |
|                       |                       | needed on turing)     |
+-----------------------+-----------------------+-----------------------+
| UAntwerpen            | gbe                   | use GigaBit Ethernet  |
|                       |                       | interconnect (only on |
|                       |                       | turing)               |
+-----------------------+-----------------------+-----------------------+

To get a list of all properties defined for all nodes, enter

::

   $ pbsnodes | grep properties

This list will also contain properties referring to, e.g., network
components, rack number, ...

You can check the `page on available hardware <../harware>` to find out how many
nodes of each type a cluster has.

Job output and error files
--------------------------

At some point your job finishes, so you will no longer see the job ID in
the list of jobs when you run qstat. You will find the standard output
and error of your job by default in the directory where you issued the
qsub command. When you navigate to that directory and list its contents,
you should see them:

::

   $ ls
   my_calc.e10021 my_calc.m my_calc.pbs my_calc.o10021

The standard output and error files have the name of the PBS script,
i.e. 'my_calc' as base name, followed by the extension '.o' and '.e'
respectively, and the job number, '10021' for this example. The error
file will be empty, at least if all went well. If not, it may contain
valuable information to determine and remedy the problem that prevented
a succesful run. The standard output file will contain the results of
your calculation.

At KU Leuven, it contains extra information about your job as well.

::

    $ cat my_calc.o20030021
    ... lots of interesting Matlab results ...
    =========================================================== 
    Epilogue args: 
    Date: Tue Mar 17 16:40:36 CET 2009 
    Allocated nodes: r2i2n12 
    Job ID: 20030021.icts-p-svcs-1 
    User ID: vsc98765 Group ID: vsc98765 
    Job Name: my_calc Session ID: 2659 
    Resource List: neednodes=1:ppn=1:nehalem,nodes=1:ppn=1,walltime=02:30:00 
    Resources Used: cput=01:52:17,mem=4160kb,vmem=28112kb,walltime=01:54:31 
    Queue Name: qreg 
    Account String:

As mentioned, there are two parts, separated by the horizontal line
composed of equality signs. The part above the horizontal line is the
output from our script, the part below is some extra information
generated by the scheduling software.

Finally, 'Resources used' shows our wall time is 1 hour, 54 minutes, and
31 seconds. Note that this is the time the job will be charged for, not
the walltime you requested in the resource list.

Regular interactive jobs, without X support
-------------------------------------------

The most basic way to start an interactive job is the following:

::

   vsc30001@login1:~> qsub -I
   qsub: waiting for job 20030021.icts-p-svcs-1 to start
   qsub: job 20030021.icts-p-svcs-1 ready

::

   vsc30001@r2i2n15:~>

Interactive jobs with X support
-------------------------------

Before starting an interactive job with X support, you have to make sure
that you have logged in to the cluster with X support enabled. If that
is not the case, you won't be able to use the X support inside the
cluster either!

The easiest way to start a job with X support is:

::

   vsc30001@login1:~> qsub -X -I
   qsub: waiting for job 20030021.icts-p-svcs-1 to start
   qsub: job 20030021.icts-p-svcs-1 ready
   vsc30001@r2i2n15:~>

"
