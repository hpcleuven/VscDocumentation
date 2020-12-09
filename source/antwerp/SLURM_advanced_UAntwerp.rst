.. _Antwerp advanced Slurm:

Slurm @ UAntwerp: Advanced use
==============================

Requesting resources
--------------------

Requesting nodes
~~~~~~~~~~~~~~~~

It is possible to specify the number of nodes, or a range of number of nodes, for a job. However,
those options should always be used in combination with other options.

Two possibilities are currently relevant for the clusters at UAntwerpen:

In combination with --ntasks and --cpus-per-task
""""""""""""""""""""""""""""""""""""""""""""""""

In addition to specifying the number of tasks and CPUs per task for a job, it is also
possible to specify the number of nodes that should be used. This is very useful on clusters
that may spread out your tasks over more nodes than the minimum needed, which can happen
if you would run your job on clusters (or partitions) that allow multiple users per node
or even multiple jobs of a single user per node. Parallel jobs that get spread out over
more nodes than really needed may show decreased performance due to more communication
over the cluster interconnect (rather than through shared memory within the node) or 
interference with other jobs on the node (that, e.g., might cause cache trashing if they
have a bad memory access pattern).

Specifying the number of nodes that will be used can be done with either 
``-N <number of nodes>`` or ``--nodes=<number of nodes``. If it is specified, then this
is the exact number of nodes that will be allocated.

It is in fact also possible to specify both a minimum and a maximum number of nodes
using either ``-N <minimum number>-<maximum number>`` or
``--nodes=< minimum number>-<maximum number>``. However, we ask you not to use this option
without consulting us first and discussing why it would make sense for your job.

Note that you should be very careful when specifying the number of nodes:
  * Requesting more nodes than really needed is very asocial behaviour as it will decrease
    the efficiency of cluster use and lengthen the waiting time for other users.
  * If you request less nodes than is required to accomodate the tasks (if also specifying 
    the number of tasks and of CPUs per task), your job will be refused by the system.
  * If you only request nodes and forget to further specify the number of tasks and 
    CPUs per task, you will get 1 core per node on most Slurm clusters.

    
In combination with --ntasks-per-node and --cpus-per-task
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In this scenario, a user specifies:
  * The number of nodes needed for a job using either ``-N <number of nodes>`` or
    ``--nodes=<number of nodes> ``. Just as above, it is possible to specify a minimum
    and maximum value. The system will allocate the maximum value if possible, but given
    the high load on a typical cluster, you're more likely to get the minimum number.
    Note also that you may then need to detect the number of tasks etc. that you can actually
    run if your code does not automatically adapt but requires parameters on the command
    line or in the input file to specify the node configuration.
  * The number of tasks per node using ``--ntasks-per-node=<number of tasks per node>``.
    The default is one task per node.
  * The number of CPUs per task using ``-c <CPUs per task>`` or 
    ``--cpus-per-task=<CPUs per task>``. Failing to specify this value results in 
    getting one CPU per task.

In this case also one should be very careful when specifying the parameters:
  * Not filling up the nodes optimally is very asocial behaviour as it will decrease
    the efficiency of the cluster use and lengthen the waiting time for others.
  * Requesting a number of tasks per node in combination with a number of CPUs per task
    that cannot be accomodated on the cluster, will lead to the job being refused by
    Slurm.


Advanced Slurm commands
-----------------------

The scontrol command
~~~~~~~~~~~~~~~~~~~~

The ``scontrol`` command is mostly meant for system administrators. In fact, most of the
actions that `scontrol` can perform, cannot be performed by regular users. 

One good use for regular users though is to get more information about one of your jobs:

.. code:: bash

    scontrol -d show job <jobID>

will show extensive information for the job with job id ``<jobID>``. 

The ``scontrol``-command is discussed in length on the 
`Slurm manual page for scontrol<https://slurm.schedmd.com/scontrol.html>`_. 
Most of the subcommands and options however are not accessible to regular users.


The sinfo command
~~~~~~~~~~~~~~~~~

The ``sinfo`` command can return a lot of information about a Slurm cluster. Understanding
its output does require a good understanding of the Slurm concepts.

The command

.. code:: bash

    sinfo
    
will print a list of partitions with their availability, nodes that will be used to run
jobs within that partition, number of nodes in that partition, and the state. The default
partition will be marked with an asteriks behind the partition name.

The command

.. code:: bash
    
    sinfo -N -1
    
will return a more node-oriented output. You'll see node groups, the partition they
belong to, and the amount of CPUs, memory (in MB), and temporary disk space available
on that node group. On Vaughan the output is rather boring as all nodes are identical.

By specifying additional command line arguments it is possible to further customize the 
output format. See the `Slurm manual page for sinfo <https://slurm.schedmd.com/sinfo.html>`_.