.. _why_not_job_start:

Why doesn't my job start?
=========================

Jobs are submitted to a queue system, which is monitored by a scheduler
that determines when a job can be executed.

The latter depends on two factors:

#. the priority assigned to the job by the scheduler, and the priorities
   of the other jobs already in the queue, and
#. the availability of the resources required to run the job.

The priority of a job is calculated using a formula that takes into
account a number of criteria.

#. the user's credentials (at the moment, all users are equal).
#. Fair share: this takes into account the walltime the
   user has used over the last seven days. The more used, the lower the
   resulting priority.
#. Time queued: the longer a job spends in the queue, the higher its
   priority becomes, so that it will run eventually.
#. Requested resources: larger jobs get a higher priority.

These factors are used to compute a weighted sum at each iteration of
the scheduler to determine a job's priority. Due to the time queued and
fair share, this is not static, but evolves over time while the job is
in the queue.

Different clusters use different policies as some clusters are optimized
for a particular type of job.

Also, don't try to outsmart the scheduler by explicitly specifying nodes
that seem empty when you submit your job. The scheduler may be reserving
these nodes for a job that requires multiple nodes, so your job will likely spend
even more time in the queue, since the scheduler will not launch your job
on another node which may be available sooner.

Remember that the cluster is not intended as a replacement for a decent
desktop PC. Short, sequential jobs may spend quite some time in the
queue, but this type of calculation is atypical from an HPC perspective.
If you have large batches of (even relatively short) sequential jobs,
you can still pack them as longer sequential or even parallel jobs and
get to run them sooner. User support can help you with that, or see
the page :ref:`worker or atools`.
