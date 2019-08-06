.. _resource specification:

Specifying job resources
========================

Resources are specified using the ``-l`` option.  Typically, three resources will
be specified:

- walltime,
- number of nodes and cores, and
- memory.

Additional specifications may be required for specialized hardware.


.. _walltime:

Walltime
--------

Walltime is specified through the option ``-l walltime=HH:MM:SS`` with
``HH:MM:SS`` the walltime that you expect to need for the job. (The
format ``DD:HH:MM:SS`` can also be used when the waltime exceeds 1 day,
and ``MM:SS`` or simply ``SS`` are also viable options for very short
jobs).

To specify a run time of 30 hours, 25 minutes and 5 seconds, you'd use the
following ``qsub`` command::

   $ qsub -l walltime=30:25:05 myjob.pbs

Equivalently, you can specify the following PBS directive in your job script::

   #PBS -l walltime=30:25:05

If you omit this option, the resource manager use a default value (one hour
on most clusters).

Walltime estimation
~~~~~~~~~~~~~~~~~~~

.. warning::

   It is important that you try to estimate the walltime for your job properly.

If your job exceeds the specified walltime, it will be killed, so the walltime
should not be underestimated.

On the other hand, the walltime should not be wildly overestimated either since this
has several disadvantages.

- It will make your job harder to schedule, so it will spend more time in the queue.
- Shorts jobs may benefit from back fill, i.e., if the scheduler finds a gap
  (based on the estimated end time of the running jobs) that is long enough to run
  that job before it has enough resources to start a large higher-priority parallel job
  (cfr. `showbf`_).
- To make sure that the cluster cannot be monopolized by one or
  a few users, many of our clusters have a stricter limit on the number of
  long-running jobs than on the number of jobs with a shorter walltime.

The maximum allowed walltime for a job is cluster-dependent. Since
these policies can change over time (as do other properties from
clusters), we bundle these on one page per cluster in the
":ref:`hardware`" section.


.. _nodes and ppn:

Number of nodes and cores
-------------------------

The following options can be used to specify the number of nodes and cores
needed for the job::

   -l nodes=<nodenum>:ppn=<cores per node>
   
This indicates that the job needs ``<nodenum>`` nodes with ``<cores per node>``
cores per node. Depending on the settings for the particular system, this will
be physical cores or hyperthreads on a physical core.

.. note::

   Specifying ``-l nodes=<nodenum>:ppn=<cores per node>`` does
   not guarantee you that you actually get ``<nodenum>`` physical nodes.
   You may actually get multiple groups of ``<cores per node>`` cores on a
   single node instead.
  
For example, ``-l nodes=4:ppn=5`` may result in an allocation of 20 cores
on a single node.

.. note::

   The job script will only run once on the first node of
   your allocation. To start processes on the other nodes, you'll need to
   use tools like ``pbsdsh`` or ``mpirun``/``mpiexec``.


.. _pmem:

Memory
------

The following option specifies the RAM requirements of your job::

   -l pmem=<memory>

The job needs ``<memory>`` RAM memory per core or hyperthread (the unit used
by ppn).  The units are ``kb``, ``mb``, ''gb`` or ``tb``.

.. warning::

   Users are strongly advised to use this option. If not specified, the system
   will use a default value, and that may be too small for your job and cause
   trouble if the scheduler puts multiple jobs on a single node.

   Moreover, the resource manager software can check for the actual
   use of resources, so when this is enabled, they
   may just terminate your job if it uses more memory than requested.

Example::

   -l nodes=2:ppn=8  -l pmem=10gb

In total, each of the 16 processes can use 10 GB RAM.

.. _pvmem:

Virtual memory
~~~~~~~~~~~~~~

A second option is to specify virtual memory::

   -l pvmem=<memory>

The job needs ``<memory>`` virtual memory per core or hyperthread (the unit
used by ppn). This determines the total amount of RAM memory + swap space that
can be used on any node.

.. note::

   On many clusters, there is not much swap space available.
   Moreover, swapping should be avoided as it causes a dramatic
   performance loss. Hence this option is not very useful in most cases.


Specifying further node properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several clusters at the VSC have nodes with different properties. E.g.,
a cluster may have nodes of two different CPU generations and your
program may be compiled to take advantage of new instructions on the
newer generation and hence not run on the older generation. Or some
nodes may have more physical memory or a larger hard disk and support
more virtual memory. Or not all nodes may be connected to the same high
speed interconnect (which is mostly an issue on the older clusters). You
can then specify which node type you want by adding further properties
to the ``-l nodes=`` specification. E.g., assume a cluster with both Ivy
Bridge and Haswell generation nodes. The Haswell CPU supports new and
useful floating point instructions, but programs that use these will not
run on the older Ivy Bridge nodes. The cluster will then specify the
property ivybridge for the Ivy Bridge nodes and haswell for the Haswell
nodes. Specifying ``-l nodes=8:ppn=6:haswell`` then tells the scheduler
that you want to use nodes with the haswell property only (and in this
case, since Haswell nodes often have 24 cores, you will likely get 2
physical nodes).

The exact list of properties depend on the cluster and is given in the
page for your cluster in the ":ref:`hardware`" section
of this manual. Note that even for a given cluster, this list may evolve over
time, e.g., when new nodes are added to the cluster, so check these
pages again from time to time!

Combining resource specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to combine multiple ``-l`` options in a single one by
separating the arguments with a colon (,). E.g., the block

::

   #PBS -l walltime=2:30:00
   #PBS -l nodes=2:ppn=16:sandybridge
   #PBS -l pmem=2gb

is equivalent with the line

::

   #PBS -l walltime=2:30:00,nodes=2:ppn=16:sandybridge,pmem=2gb

The same holds when using ``-l`` at the command line of ``qsub``.

Enforcing the node specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*These are very asocial options as they typically result in lots of
resources remaining unused, so use them with care and talk to user
support to see if you really need them. But there are some rare
scenarios in which they are actually useful.*

If you don't use all cores of a node in your job, the scheduler may
decide to bundle the tasks of several nodes in your resource request on
a single node, may put other jobs you have in the queue on the same
node(s) or may - depending on how the system manager has configured the
scheduler - put jobs of other users on the same node. In fact, most VSC
clusters have a single user per node policy as misbehaving jobs of one
user may cause a crash or performance degradation of another user's job.

-  Using ``-W x=nmatchpolicy:exactnode`` will result in the scheduler
   giving you resourced on the exact number of nodes you request.
   However, other jobs may still be scheduled on the same nodes if not
   all cores are used.
-  Using ``-l naccesspolicy=singlejob`` will make sure that no other job
   can use the nodes allocated to your job. In most cases it is very
   asocial to claim a whole node for a job that cannot fully utilise the
   resources on the node, but there are some rare cases when your
   program actually runs so much faster by leaving some resources unused
   that it actually improves the performance of the cluster. But these
   cases are very rare, so you shouldn't use this option unless, e.g.,
   you are running the final benchmarks for a paper and want to exclude
   as much factors that can influence the results as possible.
