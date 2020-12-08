.. _Antwerp advanced Slurm:

Slurm @ UAntwerp: Advanced use
==============================

Requesting resources
--------------------

TODO: Requesting resources by number of nodes instead of tasks and CPUs per task.


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