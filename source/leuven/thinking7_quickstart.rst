ThinKing7 quick start guide
===========================

:ref:`ThinKing7 <thinking7 hardware>` is the old ThinKing cluster that got an upgrade to CentOS 7.6. The cluster is at the end of its lifetime. The Ivybridge nodes will be removed by the end of 2019. The Hasswell nodes have a little longer to go. ThinKing can be used for most workloads, but have a look at :ref:`Genius <Genius hardware>` for the most recent hardware.

How to connect to ThinKing?
---------------------------

All users having an active VSC account can connect to the login node(s).You can login through 1 general login node which will loadbalance your connection to one of the available login nodes using the command::

   $ ssh vscXXXXX@login-thinking.hpc.kuleuven.be

ThinKing has 4 dedicated login nodes. You can directly login to these nodes with the same credentials, by using their hostname

Normal login nodes:

- ``login5-tier2.hpc.kuleuven.be``
- ``login6-tier2.hpc.kuleuven.be``

With a visualization capabilities (2 nvidia Quadro K5200 GPUs):

- ``login7-tier2.hpc.kuleuven.be``
- ``login8-tier2.hpc.kuleuven.be``
    
For visualization nodes please refer to the :ref:`TurboVNC documentation <TurboVNC start guide>`.

Running jobs
------------

Remind that with migration to CentOS 7.6 toolchain starting from 2018a are available for Ivybride nodes and Haswell nodes. Older toolchains are no longer available. By default toolchain 2018a is loaded, for the CPU type of the specific node. If you want to load the toolchains explicitly you find then at

- for ivybridge::

     module use /apps/leuven/ivybridge/2018a/modules/all

- for haswell::
 
     module use /apps/leuven/haswell/2018a/modules/all
 
ThinKing is now also using Lmod as module system. Have a look at  :ref:`Software stack <Software stack>` for more information.

There are several type of nodes in the ThinKing cluster: compute nodes with ivybridge or haswell processors and some gpu nodes. Have a look at the hardware pages for more information.

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a compute node it all boils down to specifying the required number of nodes and cores. As the nodes have a single user policy we recommend to always request all available cores por node (20 in case of ivybridge nodes and 24 in case of haswell nodes). For example to request 2 nodes with each 24 cores for 1 hour you can submit like this::

   $ qsub -l nodes=2:ppn=24  -l walltime=1:00:00  -A myproject  myjob.pbs

and the request of 2 nodes with each 20 cores with the specific ivybridge architecture you can submit like that::

   $ qsub -l nodes=2:ppn=20:ivybridge  -l walltime=1:00:00  -A myproject  myjob.pbs

You always need to submit with a project account (-A). To find out which projects you have, run::

   $ mam-balance

Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~

The GPU nodes are located in a separate cluster partition so you will need to explicitly specify it when submitting your job. On ThinKing the GPU nodes are not a shared resources, so you are the only user of the node. However you need to request the number of GPU's you want to use. 

For the K20::

   $ qsub -A myproject  -l walltime=1:00:00  -l nodes=1:ppn=12:gpus=2:K20Xm  -l partition=gpu  myjob.pbs

For the K40::

   $ qsub -A myproject -l walltime=1:00:00  -l nodes=1:ppn=20:gpus=2:K40c  -l partition=gpu  myjob.pbs
