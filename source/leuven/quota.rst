.. _disk quota:

How do you get your disk quota?
===============================

You have :ref:`three directories where you can store data <data location>`.  For
KU Leuven/UHasselt accounts, you have to check the quota for your directories in
one of two ways:

`$VSC_HOME`/`$VSC_DATA`
   These file systems are mounted via NFS, and the standard `quota` command
   will provide the relevant information::

      $ quota  -s
      Disk quotas for user vsc30140 (uid 2530140): 
           Filesystem   space   quota   limit   grace   files   quota   limit   grace
           10.118.240.67:/user
                        3029M*  2765M   3072M           41169   90000    100k        
           10.118.240.67:/data
                         75G     50G     60G           1120k   9000k  10000k        

`$VSC_SCRATCH`
   This file system is a parallel file system, i.e., IBM Spectrum Scale (formerly
   GPFS)::

      $ mmlsquota  --block-size auto  vol_ddn2:leuven_scratch
                               Block Limits                                               |     File Limits
      Filesystem Fileset    type             KB      quota      limit   in_doubt    grace |    files   quota    limit in_doubt    grace  Remarks                                                                  
      vol_ddn2   leuven_scratch USR         1444864 1970061312 2073755648          0     none |    16494       0        0        0     none                                                                       

The `-s` and `--block-size auto` options respectively ensure that sizes are
reported in a human-readable format, rather than expressed in blocks.
