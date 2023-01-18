Genius quick start guide
========================

:ref:`Genius <Genius hardware>` is the default KU Leuven/UHasselt Tier-2 cluster.  It can be used for most workloads, and has nodes with a lot of memory, as well as nodes with GPUs.

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

The maximum walltime for any job on Genius is 7 days (168 hours). Job requests
with walltimes between 3 and 7 days are furthermore only allowed to request up
to 10 compute nodes per job. No such limitation is imposed on jobs with
walltimes of 3 days or less.

.. note::

   There is a limit on the number of jobs you can have in a queue. This number
   includes idle, running, and blocked jobs. If you try to submit more jobs
   than the maximum number, these jobs will be deferred and will not start.
   Therefore you should always respect the following limits on how many jobs
   you have in a queue at the same time:

   - q1h: max_user_queueable = 200
   - q24h: max_user_queueable = 250
   - q72h: max_user_queueable = 150
   - q7d: max_user_queueable = 20
   - qsuperdome: max_user_queueable = 20

   These limits can be checked on the cluster by executing::

      $ qstat -f -Q


.. _submit to genius compute node:

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
Submitting a compute job boils down to specifying the required number of nodes, cores-per-node, memory and walltime.
You may e.g. request two full nodes like this::

   $ qsub -l nodes=2:ppn=36  -l walltime=2:00:00  -A myproject  myjobscript.pbs

You may also request only a part of the resources on a node.
For instance, to test a multi-threaded application which performs optimally using 4 cores, you may submit your job like this::

   $ qsub -l nodes=1:ppn=4  -l walltime=2:00:00  -A myproject  myjobscript.pbs
   
In the two above examples, the jobs may start on Skylake or Cascadelake nodes.
Please bear in mind to not exceed the maximum allowed resources on compute nodes for the targeted partition.
E.g. you can request at most 36 cores per node (``ppn=36``).

Advanced node usage
^^^^^^^^^^^^^^^^^^^
The node access policy on Skylake nodes is ``SINGLEUSER``.
This means that once a job lands on a Skylake node(s), no job from other users can land on the same node(s).
If you insist on using a full node (to exclude jobs from other users), you may enforce getting a Skylake node in one of the following ways::

   $ qsub -l nodes=1:ppn=8:skylake -l walltime=30:00 -A myproject myjobscript.pbs             # or
   $ qsub -l nodes=1:ppn=8 -l feature=skylake -l walltime=30:00 -A myproject myjobscript.pbs

The node access policy on Cascadelake nodes is ``SHARED``.
This means the CPU and memory resources per nodes are exploited as much as possible by packing more and more jobs into a single node.
Similarly, you may enforce getting a Cascadelake node by specifying either ``nodes=1:ppn=8:cascadelake`` or ``-l feature=cascadelake``
when only needing 8 cores.
The ``SHARED`` node access policy leaves room for smaller jobs to start executing earlier than initially scheduled.
Therefore, users are adviced to request only as much resources as needed by their applications.

.. _submit to genius GPU node:

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~
The GPU nodes are located in a separate cluster partition so you will need to explicitly specify it when submitting your job. We also configured the GPU nodes as shared resources, meaning that different users can simultaneously use a portion of the same node. However every user will have exclusive access to the number of GPUs requested. If you want to use only 1 GPU of type P100 (which are on nodes with SkyLake architecture) you can submit for example like this::

   $ qsub -l nodes=1:ppn=9:gpus=1:skylake -l partition=gpu -l pmem=5gb -A myproject  myscript.pbs
  
Note that in case of 1 GPU you have to request 9 cores. In case you need more GPUs you have to multiply the 9 cores with the number of GPUs requested, so in case of for example 3 GPUs you will have to specify this::

   $ qsub -l nodes=1:ppn=27:gpus=3:skylake -l partition=gpu -l pmem=5gb -A myproject  myscript.pbs

To specifically request V100 GPUs (which are on nodes with CascadeLake architecture), you can submit for example like this::

   $ qsub -l nodes=1:ppn=4:gpus=1:cascadelake -l partition=gpu -l pmem=20gb  -A myproject  myscript.pbs
  
For the V100 type of GPU, it is required that you request 4 cores for each GPU. Also notice that these nodes offer much larger memory bank.

Advanced GPU usage
^^^^^^^^^^^^^^^^^^
There are different GPU compute modes available, which are explained on this `documentation page <http://docs.adaptivecomputing.com/9-1-0/MWM/help.htm#topics/moabWorkloadManager/topics/accelerators/nvidiaGpus.htm>`_.

- exclusive_process: only one compute process is allowed to run on the GPU
- default: shared mode available for multiple processes
- exclusive_thread: only one compute thread is allowed to run on the GPU

To select the mode of your choice, you can for example submit like this::

   $ qsub -l nodes=1:ppn=9:gpus=1:skylake:exclusive_process -l partition=gpu  -A myproject  myscript.pbs
   $ qsub -l nodes=1:ppn=9:gpus=1:skylake:default -l partition=gpu  -A myproject  myscript.pbs
   $ qsub -l nodes=1:ppn=9:gpus=1:skylake:exclusive_thread -l partition=gpu  -A myproject  myscript.pbs

If no mode is specified, the ``exclusive_process`` mode is selected by default.
  

.. _submit to genius big memory node:

Submit to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The big memory nodes are also located in a separate partition. In case of the big memory nodes it is also important to add your memory requirements, for example:

::

   $ qsub -l nodes=1:ppn=36  -l pmem=20gb  -l partition=bigmem  -A myproject  myscript.pbs

.. _submit to genius AMD node:

Submit to an AMD node
~~~~~~~~~~~~~~~~~~~~~
The AMD nodes are in their own partition, with `SINGLEUSER` node access policy.
Besides specifying the partition, it is also important to specify the memory 
per process (``pmem``) since the AMD nodes have 256 GB of RAM, which implies 
that the default value is too high, and your job will never run.

For example::

   $ qsub -l nodes=2:ppn=64  -l pmem=3800mb  -l partition=amd  -A myproject  myscript.pbs

This resource specification for the memory is a few GB less than 256 GB,
leaving some room for the operating system to function properly.


Running debug jobs
------------------
Debugging on a busy cluster can be taxing due to long queue times.  To mitigate
this, two skylake  CPU nodes and a skylake GPU node has been reserved for debugging purposes.

A few restrictions apply to a debug job:

- it has to be submitted with ``-l qos=debugging``
- it can only use at most two nodes for CPU jobs, a single node for GPU jobs,
- its walltime is at most 30 minutes,
- you can only have a single debug job in the queue at any time.

To run a debug job for 20 minutes on two CPU nodes, you would use::

   $ qsub  -A myproject  -l nodes=2:ppn=36  -l walltime=00:20:00  \
           -l qos=debugging  myscript.pbs

To run a debug job for 15 minutes on a GPU node, you would use::

   $ qsub  -A myproject  -l nodes=1:ppn=9:gpus=1  -l partition=gpu \
           -l walltime=00:15:00   -l qos=debugging  myscript.pbs
