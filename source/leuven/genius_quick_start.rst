Genius quick start guide
========================

:ref:`Genius <Genius hardware>` is the most recent KU Leuven/UHasselt Tier-2 cluster.  It can be used for most workloads, and has nodes with a lot of memory, as well as nodes with GPUs.

.. include:: tier2_hardware/genius_login_nodes.rst
  
For example, to log in to any of the login node using SSH::

   $ ssh vscXXXXX@login.hpc.kuleuven.be


.. _running jobs on genius:

Running jobs on Genius
----------------------

There are several type of nodes in the Genius cluster: normal compute
nodes, GPU nodes, big memory nodes.  The resources specifications for
jobs have to be tuned to use these nodes properly.

In case you are not yet familiar with the system, you read more
information on

- :ref:`running jobs <running jobs>`, and
- :ref:`specifying resources <resource specification>`.

There are several type of nodes in the Genius cluster: normal compute nodes,
GPU nodes, big memory nodes.  For information on systems, see the :ref:`hardware
specification <Genius hardware>`.

The charge rate for the various node types of Genius are listed in the table
below.  Information on :ref:`obtaining credits <KU Leuven credits>` and
:ref:`credit system basics <credit system basics>` is available.

+----------------+--------------+
| node type      | credit/hour  |
+================+==============+
| skylake        | 10.00        |
+----------------+--------------+
| skylake bigmem | 12.00        |
+----------------+--------------+
| GPU            | 5.00 per GPU |
+----------------+--------------+


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
The AMD nodes are in their own partition.  Besides specifying the partition,
it is also important to specify the memory per process (``pmem``) since
the AMD nodes have 256 GB of RAM, which implies that the default value is
too high, and your job will never run.

For example::

   $ qsub -l nodes=2:ppn=64  -l pmem=3800mb  -l partition=amd  -A myproject  myscript.pbs

This resource specification for the memory is a few GB less than 256 GB,
leaving some room for the operating system to function properly.


Running debug jobs
------------------
Debugging on a busy cluster can be taxing due to long queue times.  To mitigate
this, two skylake  CPU nodes and a skylake GPU node has been reserved for debugging
purposes.

A few restrictions apply to a debug job:

- it has to be submitted with ``-l qos=debugging``
- it can only use at most two nodes for CPU jobs, a single node for GPU jobs,
- its walltime is at oust 30 minutes,
- you can only have a single debug node in the queue at any time.

To run a debug job for 20 minutes on two CPU nodes, you would use::

   $ qsub  -A myproject  -l nodes=2:ppn=36  -l walltime=00:20:00  \
           -l qos=debugging  myscript.pbs

To run a debug job for 15 minutes, you would use::

   $ qsub  -A myproject  -l nodes=1:ppn=9:gpus=1  -l partition=gpu \
           -l walltime=00:15:00   -l qos=debugging  myscript.pbs
