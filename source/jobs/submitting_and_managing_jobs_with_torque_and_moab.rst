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


Viewing your jobs in the queue: qstat
-------------------------------------

``qstat`` show the queue from the resource manager's perspective. It
doesn't know about priorities, only about requested resources and the
state of your job: Still idle and waiting for resources, running,
completed, ...

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

A note on queues
~~~~~~~~~~~~~~~~

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

.. _qdel:

Deleting a queued or running job: qdel
--------------------------------------

This is easily done with ``qdel``, e.g., the following command will delete the
job with ID 323323::

   $ qdel 323323

If the job is already running, the processes will be killed and the resources
will be returned to the scheduler for another job.
