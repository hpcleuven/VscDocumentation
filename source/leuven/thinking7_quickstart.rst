ThinKing7 quick start guide
===========================

:ref:`ThinKing7 <thinking7 hardware>` is the old ThinKing cluster that got an upgrade to CentOS 7.6.
The cluster is at the end of its lifetime. The ivybridge nodes have been removed.
The haswell nodes have a little longer to go. ThinKing can be used for most workloads,
but have a look at :ref:`Genius <Genius hardware>` for the most recent hardware.

How to connect to ThinKing?
---------------------------

All users having an active VSC account can connect to the login node(s).You can login through 1 general login node which will load balance your connection to one of the available login nodes using the command::

   $ ssh vscXXXXX@login-thinking.hpc.kuleuven.be

ThinKing has 4 dedicated login nodes. You can directly login to these nodes with the same credentials, by using their host name

Normal login nodes:

- ``login5-tier2.hpc.kuleuven.be``
- ``login6-tier2.hpc.kuleuven.be``

With a visualization capabilities (2 NVIDIA Quadro K5200 GPUs):

- ``login7-tier2.hpc.kuleuven.be``
- ``login8-tier2.hpc.kuleuven.be``
    
For information on how to use the visualization capabilities of these
login nodes, please refer to the :ref:`TurboVNC documentation
<TurboVNC start guide>`.


.. _running jobs on thinking:

Running jobs on Thinking
------------------------

In case you are not yet familiar with the system, you read more
information on

- :ref:`running jobs <running jobs>`, and
- :ref:`specifying resources <resource specification>`.

.. note::

   Remember that due to the migration to CentOS 7.6 toolchains
   starting from 2018a are available for haswell
   nodes. Older toolchains are no longer available. By default toolchain
   2018a is loaded, for the CPU type of the specific node. If you want
   to load the toolchains explicitly you find then at 
   
   ::
 
        $ module use /apps/leuven/haswell/2018a/modules/all

ThinKing is now also using Lmod as module system. Have a look at
:ref:`Software stack <Software stack>` for more information.

There are several type of nodes in the ThinKing cluster: compute nodes
haswell CPUs, and some GPU nodes with two NVIDIA K40c GPUs. Have a look at
the :ref:`hardware pages <Thinking hardware>` for more information.

The charge rate for the various node types of Thinking are listed in the table
below.  Information on :ref:`obtaining credits <KU Leuven credits>` and
:ref:`credit system basics <credit system basics>` is available.

+----------------+--------------+
| node type      | credit/hour  |
+================+==============+
| haswell        | 6.68         |
+----------------+--------------+
| K40c GPU nodes | 2.86         |
+----------------+--------------+


Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a compute node it all boils down to specifying the required number of nodes and cores. As the nodes have a single user policy we recommend to always request all available cores per node (24 in case of haswell CPU nodes, 20 for the haswell GPU nodes). For example to request 2 nodes with each 24 cores for 1 hour you can submit like this::

   $ qsub -l nodes=2:ppn=24  -l walltime=1:00:00  -A myproject  myjob.pbs

You always need to submit with a project account (-A). To find out which projects you have, run::

   $ mam-balance

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~

The GPU nodes are located in a separate cluster partition so you will need to
explicitly specify it when submitting your job. On ThinKing the GPU nodes are
not a shared resources, so you are the only user of the node. However you need
to request the number of GPUs you want to use:: 

   $ qsub -A myproject -l walltime=1:00:00  -l nodes=1:ppn=20:gpus=2:K40c  -l partition=gpu  myjob.pbs
