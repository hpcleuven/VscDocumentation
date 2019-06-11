Superdome Quick Start Guide
===========================

How to connect to Superdome?
----------------------------
Superdome does not have a dedicated login node, so in order to work with the system users must 
connect to the same login node used for Genius (login{1,2,3,4}-tier2.hpc.kuleuven.be).
All users having an active VSC account can connect to the login node with the same credentials using the command:

::

  ssh vscXXXXX@login1-tier2.hpc.kuleuven.be

Running Jobs
------------
Jobs can be submitted from the login node but it must be noted that in order to submit jobs to Superdome you need to specify the partition superdome and the queue qnodef:

::
  
  qsub -I -lpartition=superdome –q qnodef -L tasks=1:lprocs=14:place=numanode -A lp_myproject
  
Without specifying this partition (and queue) your jobs will be submitted to Genius, and will probably not be able to start, due to lack of specified resources.

How to request more memory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~
When submitting to superdome no explicit memory request should be added. Memory will scale together with the number of numanodes. You will have exclusive access to the memory of the requested numanode(s). There are 8 numanodes available in superdome. So if you want 1/8 of superdome memory you have to request 1 numanode, if you want ¼ you request 2 numanodes, etc .. For example for 2 numanodes you request:

::

  qsub -I -lpartition=superdome -q qnodef -L tasks=1:lprocs=28:place=numanode=2 -A lp_myproject
  
**Note**: that you have to scale also the number of lprocs and that the number of tasks stays always 1.
