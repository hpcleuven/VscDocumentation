Moab commands
=============

**This page is outdated. Please check our updated \\"\ \ **\ `Running
jobs <\%22/cluster-doc/running-jobs\%22>`__\ **\ \\" section on the user
portal. If you came to this page following a link on a web page of this
site (and not via a search) you can help us improve the documentation by
mailing the URL of the page that brought you here
to\ **\ `kurt.lust@uantwerpen.be <\%22mailto:kurt.lust@uantwerpen.be\%22>`__\ **\ .**

Job scheduling: Moab
--------------------

To map jobs to available resources, and to make sure the necessary
resources are available when a job is started, the cluster is equiped
with a job scheduler. The scheduler will accept new jobs from the users,
and will schedule them according to walltime, number of processors
needed, number of jobs the user already has scheduled, the number of
jobs the user executed recently, etc.

For this task we currently use Moab:

*Moab Cluster Suite is a policy-based intelligence engine that
integrates scheduling, managing, monitoring and reporting of cluster
workloads. It guarantees service levels are met while maximizing job
throughput. Moab integrates with existing middleware for consolidated
administrative control and holistic cluster reporting. Its graphical
management interfaces and flexible policy capabilities result in
decreased costs and increased ROI. (Adaptive Computing/Cluster
Resources)*

Most commands used so far were PBS/Torque commands. Moab also provides a
few interesting commands, which are more related to the scheduling
aspect of the system. For a full overview of all commands, please refer
to the `Moab user
manual <\%22http://docs.adaptivecomputing.com/suite/8-0/basic/help.htm#topics/moabWorkloadManager/topics/intro/productOverview.htm\%22>`__
on their site.

Moab commands
-------------

checkjob
~~~~~~~~

This is arguably the most useful Moab command since it provides detailed
information on your job from the scheduler's point of view. It can give
you important information about why your job fails to start. If a
scheduling error occurs or your job is delayed, the reason will be shown
here:

::

   $ checkjob 20030021
   checking job 20030021
   State: Idle
   Creds:  user:vsc30001  group:vsc30001  account:vsc30001  class:qreg  qos:basic
   WallTime: 00:00:00 of 1:00:00
   SubmitTime: Wed Mar 18 10:37:11
     (Time Queued  Total: 00:00:01  Eligible: 00:00:01)
   Total Tasks: 896
   Req[0]  TaskCount: 896  Partition: ALL
   Network: [NONE]  Memory >= 0  Disk >= 0  Swap >= 0
   Opsys: [NONE]  Arch: [NONE]  Features: [NONE]
   IWD: [NONE]  Executable:  [NONE]
   Bypass: 0  StartCount: 0
   PartitionMask: [ALL]
   Flags:       RESTARTABLE PREEMPTOR
   PE:  896.00  StartPriority:  5000
   job cannot run in partition DEFAULT (insufficient idle procs available: 752 < 896)

In this particular case, the job is delayed because the user asked a
total of 896 processors, and only 752 are available. The user will have
to wait, or adapt his program to run on less processors.

showq
~~~~~

This command will show you a list of running jobs, like qstat, but with
somewhat different information per job.

showbf
~~~~~~

When the scheduler performs its scheduling task, there is bound to be
some gaps between jobs on a node. These gaps can be back filled with
small jobs. To get an overview of these gaps, you can execute the
command \\"showbf\":

::

   $ showbf
   backfill window (user: 'vsc30001' group: 'vsc30001' partition: ALL) Wed Mar 18 10:31:02
   323 procs available for      21:04:59
   136 procs available for   13:19:28:58

showstart
~~~~~~~~~

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

"
