.. _UAntwerp hopper nodes:

Using the hopper nodes in leibniz
=================================

The 24 nodes of hopper with 256 GB RAM have been recpvered and integrated into
leibniz. These nodes should be used for:

  * Jobs that need more than 128 GB of RAM to run properly and do not have enough
    parallelism to exploit the large nodes of vaughan, if you feel you have to 
    wait too long before the job runs on leibniz and can do the work with 20
    cores per node.
  * Jobs that use old software that cannot be properly compiled to benefit from the
    extensions in the instruction sets of leibniz and vaughan, or that lack enough
    parallelism to fully exploit the leibniz or vaughan compute nodes (even taking 
    into account that multiple jobs launched nearly simultaneously can still make
    it possible to use the full capacity of a compute node).
  * Jobs that do not fit in a queue length of maximum 3 days and cannot be restarted
    cheaply.
    
The maximum wall time for a job on these nodes is 7 days (168 hours). Note however that
this feature should not be abused as there is only very little software that really
needs this.

Node that these nodes are not covered anymore by a service contract.
We have some spare parts for repairs but it is to be expected that the number
of hopper nodes available will decrease over time.

Getting access
--------------

Every user with an active account on leibniz has access to the hopper nodes.

Most modules available on the leibniz login nodes are also available on the hopper
compute nodes.

Starting jobs
-------------

The hopper nodes are managed through a separate queue in the queueing system
that cannot be accessed through the automatic queue dispatch mechanism in 
Torque and hence cannot be accessed by specifying features in your node
request. Instead, specify that the job should be submitted to the queue
``hopper`` either by adding ``-q hopper`` to the qsub command, e.g.,

.. code:: bash
   
    qsub -q hopper <jobscript>

or by adding the line

.. code:: bash
   
    #PBS -q hopper

to your job script.

History
-------

Hopper was a compute cluster at UAntwerp in operation from late 2014 till the
summer of 2020. The cluster had 168 compute nodes with
2 Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (Ivy Bridge), 10 cores each
(so 20 cores per node). 144 of those compute nodes had 64 GB RAM and 24 had 256 GB of RAM.
All nodes where connected through an InfiniBand FDR10 network.

When the cluster was moved out in the summer of 2020 to make space for the
installation of vaughan, the 24 nodes with 256 GB were recovered for further use.

The cluster hopper is named after `Grace Hopper <https://en.wikipedia.org/wiki/Grace_Hopper>`_.
Grace Hopper was an American mathematician turned computer scientist and United States Navy
rear admiral. She worked as a programmer of some of the first computer systems and devised
hte theory of machine independent programming languages. Her work laid at the base of the 
programming language COBOL. 

