.. _submitting jobs:

Submitting and managing jobs with Torque and Moab
=================================================


.. _qsub:

Submitting your job: qsub
-------------------------

Once your job script is finished, you submit it to the scheduling system
using the ``qsub`` command to place your job in the queue::

   $ qsub <jobscript>
   205814.leibniz

When ``qsub`` successfully queues your job, it responds with a job ID, ``205814.leibniz``
in the example above.  This is a unique identifier for your job, and can be used
to manage it.  In general, the number will suffice for this purpose.

As explained on the pages on :ref:`resource specification` and 
:ref:`specifying output files and notifications`,
there are several options to inform the scheduler about the
resources your jobs requires, or whether you want to be notified on events
related to your job.

These options can be specified

- at the top of your job script, or/and
- as additional command line options for ``qsub``.
  
In case both are used, options given on the command line take precedence
over those in the job script. For example, suppose the job
script has the following directive::

   #PBS -l walltime=2:00:00

However, when submitting it with ``qsub``, you specify ``-l walltime=1:30:00``,
the maximum walltime for your job will be 1 hour, 30 minutes.


.. _interactive jobs:

Starting interactive jobs
~~~~~~~~~~~~~~~~~~~~~~~~~

Though our clusters are mainly meant to be used for batch jobs, there
are some facilities for interactive work:

-  The login nodes can be used for light interactive work. They can
   typically run the same software as the compute nodes. Some sites also
   have special interactive nodes for special tasks, e.g., scientific
   data visualization. See the ":ref:`hardware`" section
   where each site documents what is available.
   Examples of work that can be done on the login nodes :

   - running a GUI program that generates the input files for your
     simulation,
   - a not too long compile,
   - a quick and not very resource intensive visualization.

   We have set limits on the compute time a program can use on the
   login nodes.

-  It is also possible to request one or more compute nodes for
   interactive work. This is also done through the ``qsub`` command.
   Interactive use of nodes is mostly meant for

   - debugging,
   - for large compiles, or
   - larger visualizations on clusters that don't have dedicated nodes for
     visualization.

To start an interactive job, use ``qsub``'s ``-I`` option.  You would
typically also add several ``-l`` options to specify for how long
you need the node and the amount of resources that you need. For instance,
to use a node with 20 cores interactively for 2 hours, you can use the
following command::

   qsub -I -l walltime=2:00:00 -l nodes=1:ppn=20

``qsub`` will block until it gets a node and then you get the command
prompt for that node. If the wait is too long however, ``qsub`` will
return with an error message and you'll need to repeat the command.

If you want to run **graphical user interface programs** (using X) in your
interactive job, you have to add the ``-X`` option to the above command.
This will set up the forwarding of X traffic to the login node, and
ultimately to your terminal if you have set up the connection to the login
node properly for X support.

.. note::

   - Please be reasonable when requesting interactive resources. On
     some clusters, a short walltime will give you a higher priority, and on
     most clusters a request for a multi-day interactive session will fail
     simply because the cluster cannot give you such a node before the
     time-out of ``qsub`` kicks in.

   - Please act responsibly, interactive jobs are by definition inefficient:
     the systems are mostly idling while you type.


Viewing your jobs in the queue
------------------------------

Two commands can be used to show your jobs in the queue:

-  ``qstat`` show the queue from the resource manager's perspective. It
   doesn't know about priorities, only about requested resources and the
   state of your job: Still idle and waiting for resources, running,
   completed, ...
-  ``showq`` shows the queue from the scheduler's perspective, taking
   priorities and policies into account.



.. _qstat:

qstat
~~~~~

On the VSC clusters, users will only receive a part of the information
that ``qstat`` offers. To protect the users' privacy, output is always
restricted to the user's own jobs.

To see your jobs in the queue, enter::

   $ qstat

This will give you an overview of all jobs including their status, possible
values are listed in the table below.

+--------+------------------------------------------------------+
| status | meaning                                              |
+========+======================================================+
| Q      | job is *queued*, i.e., waiting to be executed        |
+--------+------------------------------------------------------+
| S      | job is *starting*, i.e., its prologue is executed    |
+--------+------------------------------------------------------+
| R      | job is *running*                                     |
+--------+------------------------------------------------------+
| E      | job is *exiting*, i.e., its epilogue is executed     |
+--------+------------------------------------------------------+
| C      | job is *completed*, i.e., finished.                  |
+--------+------------------------------------------------------+
| H      | job has a *hold* in place                            |
+--------+------------------------------------------------------+

Several command line options can be specified to modify the output of
``qstat``:

-  ``-i`` will show you the resources the jobs require.
-  ``-n`` or ``-n1`` will also show you the nodes allocated to each running job.


.. _showq:

showq
~~~~~

The ``showq`` command will show you information about the queue from the
scheduler's perspective. Jobs are subdivided in three categories:

-  Active jobs are actually running, started or terminated.
-  Eligible jobs are queued and considered eligible for scheduling.
-  Blocked jobs are ineligible to run or to be queued for scheduling.
 
The ``showq`` command will split its output according to the three major
categories. Active jobs are sorted according to their expected end time
while eligible jobs are sorted according to their current priority.

There are multiple reasons why a job might be blocked, indicated by the state
value below:

Idle
   Job violates a fairness policy, i.e., you have used too many resources lately.
   Use diagnose ``-q`` for more information.
UserHold
   A user hold is in place.  This may be caused by job dependencies.
SystemHold
   An administrative or system hold is in place.  The job will not start until
   that hold is released.
BatchHold
   A scheduler batch hold is in place, used when the job cannot be run because

   - the requested resources are not available in the system, or
   - because the resource manager has repeatedly failed in attempts to start the
     job.  This typically indicates a problem with some nodes of the cluster,
     so you may want to contact user support.
Deferred
   A scheduler defer hold is in place (a temporary hold used when a job has been
   unable to start after a specified number of attempts. This hold is automatically
   removed after a short period of time).  
NotQueued
   Job is in the resource manager state NQ (indicating the job's controlling
   scheduling daemon in unavailable).

If your job is blocked, you may want to run the :ref:`checkjob <checkjob>` command
to find out why.

There are some useful options for ``showq``:

- ``-r`` will show you the running jobs only, but will also give
   more information about these jobs, including an estimate about how
   efficiently they are using the CPU.
- ``-i`` will give you more information about your eligible jobs.
- ``-p <partition>`` will only show jobs running in the specified partition.


.. _queues:

A note on queues
~~~~~~~~~~~~~~~~

Both ``qstat`` and ``showq`` can show you the name of the queue (``qstat``) or
class (``showq``) which in most cases is actually the same as the
queue.

All VSC clusters have multiple queues that are used to define policies.
E.g., users may be allowed to have many short jobs running simultaneously,
but may be limited to a few multi-day jobs to avoid long-time
monopolization of a cluster by a single user.

This would typically be implemented by having separate queues with specific policies for
short and long jobs. When you submit a job, ``qsub`` will put the job
in a particular queue based on the resources requested automatically.

.. warning::

   The ``qsub`` command does allow to specify the queue to use, but unless
   explicitly instructed to do so by user support, we  advise strongly against the use of this
   option.
  
   Putting the job in the wrong queue may actually result in your
   job being refused by the resource manager, and we may also chose to
   change the available queues on a system to implement new policies.


.. _detailed job info:

Getting detailed information about a job
----------------------------------------

qstat
~~~~~

To get detailed information on a single job, add the job ID as argument and
use the ``-f`` or ``-f1`` option::

   $ qstat -f <jobid>

The ``-n`` or ``-n1`` will just show you the nodes allocated to each running job in
addition to regular output.


.. _checkjob:

checkjob
~~~~~~~~

The ``checkjob`` command also provides details about a job, but from
the perspective of the scheduler, so  that you get different information.

The command below will produce information about the job with jobid 323323::

   $ checkjob 323323

Adding the ``-v`` option (for verbose) gives you even more information::

   $ checkjob -v 323323

For a running job, checkjob will give you an overview of the allocated
resources and the wall time consumed so far. For blocked jobs, the end
of the output typically contains clues about why a job is blocked.


.. _qdel:

Deleting a queued or running job: qdel
--------------------------------------

This is easily done with ``qdel``, e.g., the following command will delete the
job with ID 323323::

   $ qdel 323323

If the job is already running, the processes will be killed and the resources
will be returned to the scheduler for another job.


.. _showstart:

Getting a start time estimate for your job: showstart
-----------------------------------------------------

This is a very simple tool that will tell you, based on the current
status of the cluster, when your job is scheduled to start::

   $ showstart 20030021
   job 20030021 requires 896 procs for 1:00:00
   Earliest start in       5:20:52:52 on Tue Mar 24 07:36:36
   Earliest completion in  5:21:52:52 on Tue Mar 24 08:36:36
   Best Partition: DEFAULT

.. note::

   This is only an estimate, based on the jobs that are currently running or
   queued and the walltime that users gave for these jobs.

   - Jobs may always end sooner than requested, so your job may start sooner.
   - On the other hand, jobs with a higher priority may also enter the queue and
     delay the start of your job.


   .. _showbf:

Checking free resources for a short job: showbf
-----------------------------------------------

When the scheduler performs its task, there is bound to be
some gaps between jobs on a node. These gaps can be back filled with
small jobs. To get an overview of these gaps, you can execute the
command ``showbf``::

   $ showbf
   backfill window (user: 'vsc30001' group: 'vsc30001' partition: ALL) Wed Mar 18 10:31:02
   323 procs available for      21:04:59
   136 procs available for   13:19:28:58

To check whether a job can run in a specific partition, add the ``-p <partition>`` option.

.. note::

   There is however no guarantee that if you submit a job that would fit in
   the available resources, it will also run immediately. Another user
   might be doing the same thing at the same time, or you may simply be
   blocked from running more jobs because you already have too many jobs
   running or have made heavy use of the cluster recently.
