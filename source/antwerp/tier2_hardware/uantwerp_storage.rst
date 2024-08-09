.. _UAntwerp storage:

################
UAntwerp storage
################

The storage is organised according to the :ref:`VSC storage guidelines<data location>`.

File systems
============

.. include:: uantwerp_storage_quota_table.rst

* The **home file system** uses two mirrored SSD drives. It should only be used
  for all configuration files that Linux programs use. It should not be used
  to install software or to run jobs from. It is also not meant to be 
  heavily written to, but offers excellent read performance. 
  (Incremental) backups are made on a daily basis.

* The **data file system** uses 4TB hard drives in a RAID6 configuration for
  redundancy in case of a disk failure. It uses the XFS file system
  exported to the nodes of the cluster over NFS. We make backups of data
  on this file system for as long as the daily volume remains small enough.
  The data file system should be used for:

  * Data that should be stored for a longer time since it is often reused on 
    the cluster.
  * It is the best place to install software you prefer to install 
    yourself. For performance reasons we do advice users though to build on
    existing centrally installed software and not do a complete install of,
    e.g., Python or R if it can be build on the existing installation.
  * The data file system should not be used to store temporary data or 
    run jobs on.
    We may however ask users who tend to generate many small files to use
    this file system instead of the scratch file system. Their directories
    might not go on backup though.
  
* The **central scratch file system** is a parallel file system using BeeGFS.
  It has by far the largest capacity of all file systems at UAntwerpen and
  also provides much higher bandwidth then the data and home file systems. 
  BeeGFS is a parallel supercomputer file system. 
  This implies that it is optimized for large I/O transfers to large files.
  *Note that BeeGFS does not support hard links. Hard links are not used
  a lot. Conda however uses them internally so installing software using
  conda on the scratch file system will not work.*
  
Note that the VSC storage is not meant for backup purposes. You should not 
rely on it to store all data of your PhD or postdoc. It is the individual
user's responsibility to store that data on reliable storage managed by
your research group or the ICT service of the university.

Environment variables
=====================

.. include:: uantwerp_storage_paths_table.rst

For users with non-vsc2XXXX-accounts, the path names will be
similar to those above for UAntwerpen users with trivial modifications
based on your home institution and VSC account number.

Requesting quota
================

* Users with a vsc2XXXX account: Additional quota can be requested via the
  UAntwerp support team at hpc@uantwerpen.be. 
* Users with another VSC account:

  * Your scratch directory is not automatically created on the UAntwerp
    clusters. Please contact the UAntwerp support team at hpc@uantwerpen.be
    to get a scratch directory on our systems if you plan to use them. You 
    can use the same mail address to request additional quota on the
    scratch file system.
  * Your user and data directories are exported from your home institution
    which implies that you have to ask for additional quota on those file
    systems at your home institution.

Note
====

On the previous storage system, UAntwerpen had an additions volume /small
that was slightly better optimized for storing lots of small files. 
There is no full equivalent in the current storage system. If the small
files are the result of installing software yourself, ``$VSC_DATA`` is the 
ideal place to store those files. If they are the result of your jobs, we 
encourage you consider switching to better software or reworking your code
to have a more supercomputer-friendly output pattern (or use databases such
as SQLite3) and if that is impossible, to contact UAntwerpen user support
at hpc!uantwerpen to discuss a possible solution and the best place to put
your data.

