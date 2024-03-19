.. _UAntwerp storage:

################
UAntwerp storage
################

The storage is organised according to the :ref:`VSC storage guidelines<data location>`.

File systems
============

.. include:: uantwerp_storage_quota_table.rst

* VSC_HOME
   The **home** file system uses two mirrored SSD drives. It should only be used
   for all **configuration files** that Linux programs use. It should not be used
   to install software or to run jobs from. It is also not meant to be 
   heavily written to, but offers excellent read performance. 
   (Incremental) backups are made on a daily basis.
* VSC_DATA
   The **data** file system uses 4TB hard drives in a RAID6 configuration for
   redundancy in case of a disk failure. It uses the XFS file system
   exported to the nodes of the cluster over NFS. We make backups of data
   on this file system for as long as the daily volume remains small enough.
   
   The data file system should be used for:
 
   * Data that should be stored for a **longer time**, since it is often reused on the cluster.
   * It is the best place to install **software you prefer to install yourself**. For performance reasons we do advice users though to build on
     existing centrally installed software and not do a complete install of,
     e.g., Python or R if it can be build on the existing installation.
   * The data file system should not be used to store temporary data or 
     run jobs on.
     We may however ask users who tend to generate **many small files** to use
     this file system instead of the scratch file system. Their directories
     might not go on backup though.
* VSC_SCRATCH
   The central **scratch** file system is a parallel file system using BeeGFS.
   That implies that it is optimized for **large I/O transfers** to **large files**.
   It has the largest capacity of all file systems at UAntwerpen and
   also provides much higher bandwidth then the data and home file systems. 
   
.. note::
  The VSC storage is not meant for backup purposes. You should not 
  rely on it to store all data of your PhD or postdoc.
  
  It is the individual
  user's responsibility to store that data on reliable storage managed by
  your research group or the ICT service of the university.

Environment variables
=====================

+-------------------+---------------------------------+
| Variable          | Name                            |
+===================+=================================+
| $VSC_HOME         | /user/antwerpen/2WX/vsc2WXYZ    |
+-------------------+---------------------------------+
| $VSC_DATA         | /data/antwerpen/2WX/vsc2WXYZ    |
+-------------------+---------------------------------+
| $VSC_SCRATCH      | /scratch/antwerpen/2WX/vsc2WXYZ |
| $VSC_SCRATCH_SITE |                                 |
+-------------------+---------------------------------+
| $VSC_SCRATCH_NODE | /tmp                            |
+-------------------+---------------------------------+

.. note::

  |VUB| |UG| |KUL| For users with a different home institution: 
  the path names will be
  similar to those above for UAntwerpen users with trivial modifications
  based on your home institution and VSC account number.

Requesting quota
================

Additional quota can be requested via the UAntwerp support team 
at hpc@uantwerpen.be.

When requesting additional quota, please state clearly what you 
would like the new quota to be and provide a motivation on why 
you would need that increase.

.. note::

  |VUB| |UG| |KUL| For users with a different home institution: your **scratch** 
  directory is not automatically created on the 
  UAntwerp clusters. Please contact the UAntwerp support team at hpc@uantwerpen.be
  to get a scratch directory on our systems, or to request additional quota.
  
  Your **user** and **data** directories are exported from your home institution
  which implies that you have to ask for additional quota on those file
  systems at your home institution.
