Genius quick start guide
========================

:ref:`Genius <Genius hardware>` is the most recent KU Leuven/UHasselt Tier-2 cluster.  It can be used for most workloads, and has nodes with a lot of memory, as well as nodes with GPUs.


How to connect to Genius?
-------------------------
Genius does have a 4 dedicated login nodes. All users having an active VSC account can connect to the login node with the same credentials using the command::
  
   $ ssh vscXXXXX@nodename 

Where ``nodename`` is one of the following: 

Normal login nodes: 

- ``login1-tier2.hpc.kuleuven.be``
- ``login2-tier2.hpc.kuleuven.be``

With a visualization capabilities (NVIDIA Quadro P6000 GPU): 

- ``login3-tier2.hpc.kuleuven.be``
- ``login4-tier2.hpc.kuleuven.be``


Running jobs
------------
There are several type of nodes in the Genius cluster: normal compute nodes, GPU nodes, big memory nodes.


.. _submit to genius compute node:

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
To submit to a compute node it all boils down to specifying the required number of nodes and cores. As the nodes have a single user policy we recommend to always request all available cores per node (36 cores in this case). For example to request 2 nodes with each 36 cores you can submit like this::

   $ qsub -l nodes=2:ppn=36  -l walltime=2:00:00  -A myproject  myjobscript.pbs
  

.. _submit to genius GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~
The GPU nodes are located in a separate cluster partition so you will need to explicitly specify it when submitting your job. We also configured the GPU nodes as a shared resource, meaning that different users can simultaneously use the same node. However every user will have exclusive access to the number of GPUs requested. If you want to use only 1 GPU you can submit for example like this::

   $ qsub -l nodes=1:ppn=9:gpus=1  -l partition=gpu  -A myproject  myscript.pbs
  
Note that in case of 1 GPU you have to request 9 cores. In case you need more GPUs you have to multiply the 9 cores with the number of GPUs requested, so in case of for example 3 GPUS you will have to specify this::

   $ qsub -l nodes=1:ppn=27:gpus=3  -l partition=gpu  -A myproject  myscript.pbs
   

.. _submit to genius big memory node:

Submit to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The big memory nodes are also located in a separate partition. In case of the big memory nodes it is also important to add your memory requirements, for example:

::

   $ qsub -l nodes=1:ppn=36  -l pmem=20gb  -l partition=bigmem  -A myproject  myscript.pbs

.. _submit to genius AMD node:

Submit to an AMD node
~~~~~~~~~~~~~~~~~~~~~
The AMD nodes are in their own parition.  Besides specifying the partition,
it is also important to specify the memory per process (``pmem``) since
the AMD nodes have 256 GB of RAM, which implies that the default value is
too high, and your job will never run.

For example::

   $ qsub -l nodes=2:ppn=64  -l pmem=3800mb  -l parition=amd  -A myproject  myscript.pbs

This resource specification for the memory is a few GB less than 256 GB,
leaving some room for the operating system to function properly.


Running debug jobs
------------------
Debugging on a busy cluster can be taxing due to long queue times.  To mitigate
this, two ndoes have been reserved for debuggign purposes, an ordinary compute
ndoe and a GPU node.

A few restrictions apply to a debug job:

- it has to be submitted with ``-l qos=debugging``
- it can only use a single node,
- its walltime is at ost 30 mintues,
- you can only have a single debug node in the queue at any time.

For instance, to run a debug job for 15 mintues, you would use::

   $ qsub  -A my_project  -l nodes=1:ppn=36  -l walltime=00:15:00  \
           -l qos=debugging  my_job.pbs

To use the GPU debug node, use::

   $ qsub  -A my_project  -l nodes=1:ppn=9:gpus=1  -l partition=gpu \
           -l walltime=00:15:00   -l qos=debugging  my_job.pbs
