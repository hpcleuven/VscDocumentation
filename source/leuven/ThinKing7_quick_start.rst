ThinKing7 quick start guide

:ref:`ThinKing7 <thinking centos7 hardware>` is the most recent KU Leuven/UHasselt Tier-2 cluster. It can be used for most workloads, and has nodes with a lot of memory, as well as nodes with GPUs.
How to connect to ThinKing?

ThinKing does have a 4 dedicated login nodes. All users having an active VSC account can connect to the login node with the same credentials using the command:

$ ssh vscXXXXX@nodename

Where nodename can be one of the following:

Normal login nodes:

    login5-tier2.hpc.kuleuven.be
    login6-tier2.hpc.kuleuven.be

With a visualization capabilities (2 nvidia Quadro K5200 GPUs):

    login7-tier2.hpc.kuleuven.be
    login8-tier2.hpc.kuleuven.be
    
For visualization nodes please refer to the :ref:`TurboVNC documentation <access/turbovnc_start_guide>`

Running jobs

There are several type of nodes in the ThinKing cluster: normal compute nodes with ivybridge or haswell processors and gpu nodes.

Submit to a compute node

To submit to a compute node it all boils down to specifying the required number of nodes and cores. As the nodes have a single user policy we recommend to always request all available cores por node (20 in case of ivybridge nodes and 24 in case of haswell nodes). For example to request 2 nodes with each 24 cores you can submit like this:

qsub -lnodes=2:ppn=24 -lwalltime=2:00:00 -A myproject myjobscript

Submit to a GPU node

The GPU nodes are located in a separate cluster partition so you will need to explicitly specify it when submitting your job. We also configured the GPU nodes as a shared resource, meaning that different users can simultaneously use the same node. However every user will have exclusive access to the number of GPUs requested. If you want to use only 1 GPU you can submit for example like this:

qsub -lnodes=1:ppn=20:gpus=1 -lpartition=gpu -A myproject myscript


