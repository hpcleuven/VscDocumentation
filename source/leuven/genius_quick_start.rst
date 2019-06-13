Genius Quick Start Guide
========================
How to connect to Genius?
-------------------------
Genius does have a 4 dedicated login nodes. All users having an active VSC account can connect to the login node with the same credentials using the command: 

::
  
  $ ssh vscXXXXX@nodename 

Where nodename can be one of the following: 

Normal login nodes: 

- login1-tier2.hpc.kuleuven.be 
- login2-tier2.hpc.kuleuven.be 

With a visualization capabilities (nvidia Quadro P6000 GPU): 

- login3-tier2.hpc.kuleuven.be  
- login4-tier2.hpc.kuleuven.be  

Running jobs
------------
There are several type of nodes in the Genius cluster: normal compute nodes, gpu nodes, big memory nodes.

Submit to a compute node
~~~~~~~~~~~~~~~~~~~~~~~~
To submit to a compute node it all boils down to specifying the required number of nodes and cores. As the nodes have a single user policy we recommend to always request all available cores por node (36 cores in this case). For example to request 2 nodes with each 36 cores you can submit like this:

::

  qsub -lnodes=2:ppn=36 -lwalltime=2:00:00 -A myproject myjobscript
  
Submit to a GPU node
~~~~~~~~~~~~~~~~~~~~
The GPU nodes are located in a separate cluster partition so you will need to explicitly specify it when submitting your job. We also configured the GPU nodes as a shared resource, meaning that different users can simultaneously use the same node. However every user will have exclusive access to the number of GPUs requested. If you want to use only 1 GPU you can submit for example like this:

::

  qsub -lnodes=1:ppn=9:gpus=1 -lpartition=gpu -A myproject myscript
  
Note that in case of 1 GPU you have to request 9 cores. In case you need more GPUs you have to multiply the 9 cores with the number of GPUs requested, so in case of for example 3 GPUS you will have to specify this:
 
::

  qsub -lnodes=1:ppn=27:gpus=3 -lpartition=gpu -A myproject myscript  
   
Submit to a big memory node
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The big memory nodes are also located in a separate partition. In case of the big memory nodes it is alo important to add your memory requirements, for example:

::

  qsub -lnodes=1:ppn=36 -lpmem=20gb -lpartition=bigmem -A myproject myscript
