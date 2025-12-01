.. _worker or atools:

How can I run many similar computations conveniently?
=====================================================

It is often necessary to run the same application on many input files,
or with many different parameter values.  You can of course manage such
jobs by hand, or write scripts to do that for you.  However, this is a
very common scenario, so we developed software to do that for you.

Two general purpose software packages are available:

- the `worker framework <https://github.com/gjbex/worker>`_ (:ref:`worker
  quick start <worker framework>` and `worker documentation`_) and
- `atools <https://github.com/gjbex/atools>`_ (`atools documentation`_).

Both are designed to handle this use case, but each has its own strengths
and weaknesses.


What features do atools and worker have?
----------------------------------------

Both software packages will do the bookkeeping for you, i.e.,

- keep track of the computations that were completed;
- monitor the progress of a running job; 
- allow you to resume computations in case you underestimated
  the walltime requirements;
- provide an overview of the computations that succeed, failed,
  or were not completed;
- aggregate output of individual computations;
- analyze the efficiency of a finished job.

Both software packages have been designed with simplicity in mind,
one of the design goals is to make them as easy to use as possible.

For a detailed overview of the features, see the `atools documentation`_
and the `worker documentation`_.


What to use: atools or worker?
------------------------------

That depends on a number of issues, and you have to consider them all
to make the correct choice.

- Is an individual computation
  :ref:`sequential, multi-threaded or even distributed <type_computation>`?
- How much :ref:`walltime is required by an individual computation <walltime_per_work_item>`?
- :ref:`How many individual computations <number_work_items>`
  do you need to perform?
- What are the :ref:`job policies <job_policies>` of the cluster you
  want to run on?

.. _type_computation:

Type of computation
~~~~~~~~~~~~~~~~~~~

In worker and atools terminology, an individual computation is referred to
as a work item.  Depending on the implementation of the work item, worker or
atools may be a better match.  The following table summarizes this.

+----------------+--------+--------+
| work item type | worker | atools |
+================+========+========+
| sequential     | yes    | yes    |
+----------------+--------+--------+
| multi-threaded | yes    | yes    |
+----------------+--------+--------+
| MPI-based      | no     | yes    |
+----------------+--------+--------+

.. warning::

   Although this might seems to suggest that since atools can deal with all types
   of work items, it is the best choice, this is definitely not true.

The table makes it clear that MPI applications can not be used in work items
for worker.  worker itself is implemented using MPI, and hence things would
get terminally confused if it executes work items that contain calls to the
MPI API.

.. _walltime_per_work_item:

Walltime per work item
~~~~~~~~~~~~~~~~~~~~~~

For both atools and worker, we emphasize that the average time to complete
a work item must amount to at least several minutes. If work items take very
little time, there will be a significant overhead from the atools or worker
framework itself. For atools in particular this overhead will be considerable
since it relies on the scheduler to start individual work items.

With both atools and worker, short work items furthermore risk putting a large
pressure on shared file systems (especially if many processes are active at
the same time and if modules need to be loaded as part of the workload).
If small scale tests indicate that many work items take less than 3-4 minutes
to complete, we strongly strongly recommend that you merge multiple work items
together into larger ones.

On the other side of the spectrum, i.e., work items that take a very long time 
complete, atools may be the better choice since work items are executed
independently.  This however depends on the reliability of the infrastructure.

The following table summarizes this.

+---------------------------+--------+--------+
| single work item walltime | worker | atools |
+===========================+========+========+
| < 1 second                | \-     | \-\-   |
+---------------------------+--------+--------+
| < 1 minute                | \+     | \-     |
+---------------------------+--------+--------+
| 1 minute to 24 hours      | \+\+   | \+\+   |
+---------------------------+--------+--------+
| > 24 hours                | \+     | \+\+   |
+---------------------------+--------+--------+

.. _number_work_items:

Number of work items
~~~~~~~~~~~~~~~~~~~~

If you need to do many individual computations (work items), say more than
500, worker is the better choice.  It will be run as a single job, rather
than many individual jobs, hence lightening the load on the scheduler
considerably.

.. _job_policies:

Job policies
~~~~~~~~~~~~

The following job policies are currently in effect on various VSC clusters.

Shared
   Multiple jobs from multiple users are allowed to run concurrently
   on a node.
Single user
   Multiple jobs from a single user are allowed to run concurrently
   on a node.
Single job
   Only a single job can run on a compute node.

On some clusters, credits are required to run jobs, and that policy may
also influence your choice.

The table below provides an overview of the policies in effect on the
various cluster/partitions.

+----------+--------------------+-----------+-------------+------------+
| VSC hub  | cluster            | partition | policy      | accounting |
+==========+====================+===========+=============+============+
| Antwerp  | any                | any       | single user | no         |
+----------+--------------------+-----------+-------------+------------+
| Brussels | any                | any       | shared      | no         |
+----------+--------------------+-----------+-------------+------------+
| Ghent    | any                | any       | shared      | no         |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | default   | shared      | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | bigmem    | shared      | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | gpu       | shared      | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | breniac (Tier-1)   | default   | single job  | yes        |
+----------+--------------------+-----------+-------------+------------+

Clusters with accounting enabled:
   If you use atools on a cluster where accounting is active, make sure a work
   item uses all resources of that node.  If multiple work items run on the same
   node concurrently, you will be charged for each work item individually,
   making that a *very* expensive computation.  In this situation, use worker.
Clusters with single user policy:
   Ensure that the load balance is as good as possible.  If a few work items
   require much more time than others, they may block the nodes they are running
   on from running other jobs.  This is the case for both atools and worker.
   However, since worker is an MPI application, it will keep all nodes involved
   in the job blocked, aggravating the problem.
Clusters with shared policy
   Here atools allows the scheduler the most flexibility, but keep in mind the
   considerations on :ref:`work item walltime <walltime_per_work_item>` and the
   :ref:`number of work items <number_work_items>`.


