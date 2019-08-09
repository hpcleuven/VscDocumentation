ThinKing7 quick start guide

:ref:`ThinKing7 <thinking centos7 hardware>` is the old Thinking cluster that got an upgrade to CentOS 7.6. The cluster is at the end of its lifetime. The Ivybridge nodes will be removed by the end of 2019. The Hasswell nodes have a little longer to go. Thinking can be used for most workloads, but have a look at :ref:`Genius <Genius hardware>` for the most recent hardware.

How to connect to ThinKing?

All users having an active VSC account can connect to the login node(s).You can login through 1 general login node which will loadbalance your connection to one of the available login nodes using the command: 

$ ssh vscXXXXX@login-thinking.hpc.kuleuven.be

ThinKing does have a 4 dedicated login nodes. You can directly login to these nodes with the same credentials, by using their hostname

Normal login nodes:

    login5-tier2.hpc.kuleuven.be
    login6-tier2.hpc.kuleuven.be

With a visualization capabilities (2 nvidia Quadro K5200 GPUs):

    login7-tier2.hpc.kuleuven.be
    login8-tier2.hpc.kuleuven.be
    
For visualization nodes please refer to the :ref:`TurboVNC documentation <access/turbovnc_start_guide>`

Running jobs

Remind that with migration to CentOS 7.6 toolchain starting from 2018a are available. Older toolchains are no longer available. Thinking is now also using LMOD as module system. Have a look at  :ref:`Software stack <software/software_stack>` for more information.

There are several type of nodes in the ThinKing cluster: normal compute nodes with ivybridge or haswell processors and gpu nodes.

Submit to a compute node

To submit to a compute node it all boils down to specifying the required number of nodes and cores. As the nodes have a single user policy we recommend to always request all available cores por node (20 in case of ivybridge nodes and 24 in case of haswell nodes). For example to request 2 nodes with each 24 cores you can submit like this:

::
qsub -lnodes=2:ppn=24 -lwalltime=2:00:00 -A myproject myjobscript

You always need to submit with a project account (-A). To find out which projects you have, run:

::
mam-balance

to have 

Submit to a GPU node

The GPU nodes are located in a separate cluster partition so you will need to explicitly specify it when submitting your job. On Thinking the GPU nodes are not a shared resources, so you are the only user of the node. However you need to request the number of GPU's you want to use. 

For the K20:

::
qsub -A myproject -lnodes=1:ppn=12:gpus=2:K20Xm -lpartition=gpu

For the K40:

::
qsub -A myproject -lnodes=1:ppn=20:gpus=2:K40c -lpartition=gpu

