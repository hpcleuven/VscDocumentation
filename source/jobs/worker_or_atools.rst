How can I run many similar computations?
========================================

It is often necessary to run the same application on many input files,
or with many different parameter values.  You can of course manage such
jobs by hand, or write scripts to do that for you.  However, this is a
very common scenario, so we developed software to do that for you.

Two general purpose software packages are available:

- the `worker framework <https://github.com/gjbex/worker>`_ (:ref:`worker quickstart <worker framework>` and `worker documentation`_) and
- `atools <https://github.com/gjbex/atools>`_ (`atools documentation`_).

Both are designed to handle this use case, but with distinct twists.


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

- Is an individual computation :ref:`sequential, multi-threaded or
  even distributed <Type of computation>`?
- How much :ref:`walltime is required by an individual computation
  <Walltime per work item>`?
- :ref:`How many individual computations <Number of work items>`
  do you need to perform?
- What are the :ref:`job policies <Job policies>` of the cluster you
  want to run on?


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
| MPI- based     | no     | yes    |
+----------------+--------+--------+

.. warning::

   Although this might seems to suggest that since atools can deal with all types
   of work items, it is the best choice, this is definitely not true.

The table makes it clear that MPI application can not be used in work items
for worker.  worker itself is implemented using MPI, and hence things would
get terminally confused if it executes work items that contain calls to the
MPI API.


Walltime per work item
~~~~~~~~~~~~~~~~~~~~~~

When work items take only a short time to complete, the overhead for starting
new work items will be considerable for atools since it relies on the scheduler
to start individual work items.  This is much more efficient for worker since
all work items are executed by a single job, so the scheduler is not involved.

On the other side of the spectrum, i.e., work items that take a very long time 
complete, atools may be the better choice since work items are executed
independently.  This however depends on the reliability of the infrastructure.

The following table summarizes this.

+------------+--------+--------+
| walltime   | worker | atools |
+============+========+========+
| < 1 second | \-     | \-\-   |
+------------+--------+--------+
| < 1 minute | \+     | \-     |
+------------+--------+--------+
|            | \+\+   | \+\+   |
+------------+--------+--------+
| > 24 hours | \+     | \+\+   |
+------------+--------+--------+


Number of work items
~~~~~~~~~~~~~~~~~~~~

If you need to do many individual computations (work items), say more than
500, worker is the better choice.  It will be run as a single job, rather
than many individual jobs, hence lightening the load on the scheduler
considerably.


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
| Leuven   | thinking           | default   | single user | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | default   | single user | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | bigmem    | single user | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | gpu       | shared      | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | superdome | shared      | yes        |
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
Cluster with shared policy
   Here atools allows the scheduler the most flexibility, unless the number of
   job items is too high.


.. include:: links.rst
