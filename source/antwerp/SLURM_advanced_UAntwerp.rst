.. _Antwerp advanced Slurm:

Slurm @ UAntwerp: Advanced use
==============================

This page contains some more advanced commands and additional ways to request resources.
Make sure to first read our :ref:`basic Slurm use <Antwerp Slurm>` page.

Requesting resources
--------------------

Requesting nodes
~~~~~~~~~~~~~~~~

It is possible to specify the number of nodes, or a range of number of nodes, for a job. However,
those options should always be used in combination with other options.

In combination with ``--ntasks`` and ``--cpus-per-task``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In addition to specifying the number of tasks and CPUs per task for a job, it is also
possible to specify the number of nodes that should be used. This is very useful on clusters
that may spread out your tasks over more nodes than the minimum needed, which can happen
if you would run your job on clusters (or partitions) that allow multiple users per node
or even multiple jobs of a single user per node. Parallel jobs that get spread out over
more nodes than really needed may show decreased performance due to more communication
over the cluster interconnect (rather than through shared memory within the node) or
interference with other jobs on the node (that, e.g., might cause cache thrashing if they
have a bad memory access pattern).

Specifying the number of nodes that will be used can be done with either
``--nodes=<number of nodes>`` or ``-N <number of nodes>``. If it is specified, then this
is the exact number of nodes that will be allocated.

It is also possible to specify both a minimum and a maximum number of nodes
using either ``--nodes=<minimum number>-<maximum number>`` or
``-N <minimum number>-<maximum number>``. However, we ask you not to use this option
without consulting us first and discussing why it would make sense for your job.

Note that you should be very careful when specifying the number of nodes:

* Requesting more nodes than really needed is very asocial behaviour as it will decrease
  the efficiency of cluster use and lengthen the waiting time for other users.
* If you request less nodes than is required to accommodate the tasks (if also specifying
  the number of tasks and of CPUs per task), your job will be refused by the system.
* If you only request nodes and forget to further specify the number of tasks and
  CPUs per task, you will get the default of 1 CPU per node.

**Never use this option on the clusters at UAntwerp except to request (and use) full
nodes as in the current Slurm configuration the empty cores cannot be used by other jobs.**

In combination with ``--ntasks-per-node`` and ``--cpus-per-task``
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In this scenario, a user specifies:

* The number of nodes needed for a job using either ``--nodes=<number of nodes>`` or
  ``-N <number of nodes>``. Just as above, it is possible to specify a minimum
  and maximum value. The system will allocate the maximum value if possible, but given
  the high load on a typical cluster, you're more likely to get the minimum number.
  Note also that you may then need to detect the number of tasks etc. that you can actually
  run if your code does not automatically adapt but requires parameters on the command
  line or in the input file to specify the node configuration.
* The number of tasks per node using ``--ntasks-per-node=<number of tasks per node>``.
  The default is one task per node.
* The number of CPUs per task using ``--cpus-per-task=<CPUs per task>`` or
  ``-c <CPUs per task>``. Failing to specify this value results in
  getting one CPU per task.

In this case also one should be very careful when specifying the parameters:

* Not filling up the nodes optimally is very asocial behaviour as it will decrease
  the efficiency of the cluster use and lengthen the waiting time for others.
* Requesting a number of tasks per node in combination with a number of CPUs per task
  that cannot be accommodated on the cluster, will lead to the job being refused by
  Slurm.

**This option should only be used on the UAntwerp cluster if you can fill nodes completely
or have a very good reason to leave some cores empty.**

Minimizing distance on the network for faster communications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The nodes in a cluster are connected with each other through a number of switches that
form a hierarchical network tree (also called a topology). On the UAntwerp clusters,
the topology is a variant of the tree. All nodes are connected to an edge switch and
hence split up naturally in groups corresponding to the edge switch they are connected
with. These edge switches are then connected through a number of top level switches
so that all nodes can communicate with each other.

This means that traffic between two nodes either passes through just a single switch
(if the nodes are connected to the same edge switch) or through a series of three switches
(edge - top - edge). Obviously, traffic that passes through multiple switches will incur
a higher latency. Slurm tries to minimize network contention by identifying the lowest
level switch in the hierarchy that can satisfy a job's request and then allocates the
requested resources, based on a best-fit algorithm and the currently available resources.
This may result in an allocation with more than the optimum number of switches when the
cluster is under a heavy load (as is usually the case on the UAntwerp clusters).

A user can request a maximum number of switches for a job using the ``--switches=<count>``
option. Usually, one would specify ``--switches=1`` here to make sure the job runs on
nodes which are all connected to the same edge switch.
Note that this may increase the wait time of the job (because the scheduler has
less nodes to choose from).

Optionally, a maximum time delay can be specified as well using
``--switches=<count>@<max-time>`` to tell the scheduler that it can delay the job until
it either finds an allocation with the desired switch count, or to ignore the switches
request when the time limit expires.


Advanced Slurm commands
-----------------------

The scontrol command
~~~~~~~~~~~~~~~~~~~~

`Slurm scontrol manual page on the web <https://slurm.schedmd.com/scontrol.html>`_

The ``scontrol`` command is mostly meant for system administrators. In fact, most of the
actions that `scontrol` can perform, cannot be performed by regular users.

One good use for regular users though is to get more information about one of your jobs:

.. code:: bash

    scontrol -d show job <jobid>

will show extensive information for the job with job ID ``<jobid>``.

Some software might require a list of hostnames:

.. code:: bash

   scontrol show hostnames

in the context of a job, returns a list of (unqualified) hostnames of the allocated nodes.
This can be used, e.g. with bash scripting, to generate a nodelist file in the format required by the software.

The sinfo command
~~~~~~~~~~~~~~~~~

`Slurm sinfo manual page on the web <https://slurm.schedmd.com/sinfo.html>`_

The ``sinfo`` command can return a lot of information about a Slurm cluster. Understanding
its output does require a good understanding of the Slurm concepts
(see our :ref:`basic Slurm use <Antwerp Slurm>` page).

The command

.. code:: bash

    sinfo

will print a list of partitions with their availability, nodes that will be used to run
jobs within that partition, number of nodes in that partition, and the state. The default
partition will be marked with an asterisk behind the partition name.

The command

.. code:: bash

    sinfo -N -l

will return a more node-oriented output. You'll see node groups, the partition they
belong to, and the amount of CPUs, memory (in MB), and temporary disk space available
on that node group. On Vaughan the output is rather boring as all nodes are identical.

By specifying additional command line arguments it is possible to further customize the
output format. See the `sinfo manual page <https://slurm.schedmd.com/sinfo.html>`_.
