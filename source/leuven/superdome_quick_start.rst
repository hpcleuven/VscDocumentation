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
