.. _submitting jobs:

Submitting and managing jobs with Torque and Moab
=================================================

Submitting your job: the qsub command
-------------------------------------

Once your job script is finished, you submit it to the scheduling system
using the ``qsub`` command:

::

   qsub <jobscript>

places your job script in the queue. As explained on the page on
":ref:`Specifying resources, output files and notifications`",
there are several options to tell the scheduler which resources you need
or how you want to be notified of events surrounding your job. The can
be given at the top of your job script or as additional command line
options to ``qsub``. In case both are used, options given on the command
line take precedence over the specifications in the job script. E.g., if
a different number of nodes and cores is requested through a command
line option then specified in the job script, the specification on the
command line will be used.

Starting interactive jobs
~~~~~~~~~~~~~~~~~~~~~~~~~

Though our clusters are mainly meant to be used for batch jobs, there
are some facilities for interactive work:

-  The login nodes can be used for light interactive work. They can
   typically run the same software as the compute nodes. Some sites also
   have special interactive nodes for special tasks, e.g., scientific
   data visualisation. See the ":ref:`hardware`" section
   where each site documents what is available.
   Examples of work that can be done on the login nodes is running a GUI
   program that generates the input files for your simulation, a not too
   long compile, a quick and not very resource intensive visualisation.
   We have set limits on the amount of time a program can use on the
   login nodes.
-  It is also possible to request one or more compute nodes for
   interactive work. This is also done through the ``qsub`` command. In
   this case, you can still use a job script to specify the resources,
   but the most common case is to specify them at the command line.

In the latter scenario, two options of ``qsub`` are particularly useful:
``-I`` to request an node for interactive use, and ``-X`` to add support
for X to the request. You would typically also add several ``-l``
options to specify for how long you need the node and the amount of
resources that you need. E.g.,

::

   qsub -I -l walltime=2:00:00 -l nodes=1:ppn=20

to use 20 cores on a single node for 2 hours. ``qsub`` will block until
it gets a node and then you get the command prompt for that node. If the
wait is too long however, ``qsub`` will return with an error message and
you'll need to repeat the call.

If you want to run programs that use X in your interactive job, you have
to add the -X option to the above command. This will set up the
forwarding of X traffic to the login node, and ultimately to your
terminal if you have set up the connection to the login node properly
for X support.

Please remain reasonable in your request for interactive resources. On
some clusters, a short waltime will give you a higher priority, and on
most clusters a request for a multi-day interactive session will fail
simply because the cluster cannot give you such a node before the
time-out of ``qsub`` kicks in. Interactive use of nodes is mostly meant
for debugging, for large compiles or larger visualisations on clusters
that don't have dedicated nodes for visualisation.

Viewing your jobs in the queue: qstat and showq
-----------------------------------------------

Two commands can be used to show your jobs in the queue:

-  ``qstat`` show the queue from the resource manager's perspective. It
   doesn't know about priorities, only about requested resources and the
   state of your job: Still idle and waiting for resources, running,
   finishing, ...
-  ``showq`` shows the queue from the scheduler's perspective, taking
   priorities and policies into account.

| Both commands will also show you the name of the queue (``qstat``) or
  class (``showq``) which in most cases is actually the same as the
  queue. All VSC clusters have multiple queues. Queues are used to
  define policies for each cluster. E.g., users may be allowed to have a
  lot of short jobs running simultaneously as they will finish soon
  anyway, but may be limited to a few multi-day jobs to avoid long-time
  monopolisation of a cluster by a single user, and this would typically
  be implemented by having separate queues with separate policies for
  short and long jobs. When you submit a job, ``qsub`` will put the job
  in a particular queue based on the resources requested. The ``qsub``
  command does allow to specify the queue to use, but unless instructed
  to do so by user support, we strongly advise against using this
  option. Putting the job in the wrong queue may actually result in your
  job being refused by the queue manager, and we may also chose to
  change the available queues on a system to implement new policies.

qstat
~~~~~

On the VSC clusters, users will only receive a subset of the options
that ``qsub`` offers. The output is always restricted to the user's jobs
only.

To see your jobs in the queue, enter

::

   qstat

This will give you an overview of all jobs including their status, which
includes queues but not yet running (Q), running (R) or finishing (C).

::

   qstat <jobid>

where <jobid> is the number of the job, will show you the information
about this job only.

Several command line options can be specified to modify the output of
``qstat``:

-  ``qstat -i`` will show you a bit more information.
-  ``qstat -n`` will also show you the nodes allocated to each running
   job.
-  ``qstat -f`` or ``qstat -f1`` produces even more output. In fact, it
   produces so much output that it is better only used with the job ID
   as an argument to request information about a specific job.

showq
~~~~~

The ``showq`` command will show you information about the queue from the
scheduler's perspective. Jobs are subdivided in three categories:

-  The active jobs are the jobs that are actually running, or are being
   started or terminated.
-  Eligible jobs are jobs that are queued and considered eligible for
   scheduling.
-  Blocked jobs are jobs that are ineligible to run or to be queued for
   scheduling. There are multiple reasons why a job might be in the
   blocked state.

   -  If the status is marked as idle, your job most likely violates a
      fairness policy, i.e., you've used too many resources recently.
   -  BatchHold: Either the cluster has repeatedly failed to start the
      job (which typically is a problem with the cluster, so contact
      user support if you see this happen) or your resource request
      cannot be granted on the cluster. This is also the case if you try
      to put more jobs in a queue than you are allowed to have queued or
      running at any particular moment.

   -  deferred: a temporary hold after a failed start attempt, but the
      system will have another try at starting the job.

   -  UserHold or SystemHold: The user or the system administrator has
      put a hold on the job (and it is is up to him/her to also release
      that hold again).

   -  NotQueued: The job has not been queued for some other reason.

The ``showq`` command will split its output according to the three major
categories. Active jobs are sorted according to their expected end time
while eligible jobs are sorted according to their current priority.

There are also some useful options:

-  ``showq -r`` will show you the running jobs only, but will also give
   more information about these jobs, including an estimate about how
   efficiently they are using the CPU.
-  ``showq -i``\ will give you more information about your eligible
   jobs.

Getting detailed information about a job: qstat -f and checkjob
---------------------------------------------------------------

We've discussed the Torque ``qstat -f`` command already in the previous
section. It gives detailed information about a job from the resource
manager's perspective.

The ``checkjob`` command does the same, but from the perspective of the
scheduler, so the information that you get is different.

::

   checkjob 323323

will produce information about the job with jobid 323323.

::

   checkjob -v 323323

where -v stands for verbose produces even more information.

For a running job, checkjob will give you an overview of the allocated
resources and the wall time consumed so far. For blocked jobs, the end
of the output typically contains clues about why a job is blocked.

Deleting a job that is queued or running
----------------------------------------

This is easily done with ``qdel``:

::

   qdel 323323

will delete the job with job ID 323323. If the job is already running,
the processes will be killed and the resources will be returned to the
scheduler for another job.

Getting an estimate for the start time of your job: showstart
-------------------------------------------------------------

This is a very simple tool that will tell you, based on the current
status of the cluster, when your job is scheduled to start. Note however
that this is merely an estimate, and should not be relied upon: jobs can
start sooner if other jobs finish early, get removed, etc., but jobs can
also be delayed when other jobs with higher priority are submitted.

::

   $ showstart 20030021
   job 20030021 requires 896 procs for 1:00:00
   Earliest start in       5:20:52:52 on Tue Mar 24 07:36:36
   Earliest completion in  5:21:52:52 on Tue Mar 24 08:36:36
   Best Partition: DEFAULT

Note however that this is only an estimate, starting from the jobs that
are currently running or in the queue and the wall time that users gave
for these jobs. Jobs may always end earlier than predicted based on the
requested wall time, so your job may start earlier. But other jobs with
a higher priority may also enter the queue and delay the start from your
job.

See if there is are free resources that you might use for a short job: showbf
-----------------------------------------------------------------------------

When the scheduler performs its scheduling task, there is bound to be
some gaps between jobs on a node. These gaps can be back filled with
small jobs. To get an overview of these gaps, you can execute the
command ``showbf``:

::

   $ showbf
   backfill window (user: 'vsc30001' group: 'vsc30001' partition: ALL) Wed Mar 18 10:31:02
   323 procs available for      21:04:59
   136 procs available for   13:19:28:58

There is however no guarantee that if you submit a job that would fit in
the available resources, it will also run immediately. Another user
might be doing the same thing at the same time, or you may simply be
blocked from running more jobs because you already have too many jobs
running or have made heavy use of the cluster recently.
