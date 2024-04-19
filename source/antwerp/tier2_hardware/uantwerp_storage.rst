.. _UAntwerp storage:

################
UAntwerp storage
################

The storage is organised according to the :ref:`VSC storage guidelines<data location>`.

File systems
============

.. include:: uantwerp_storage_quota_table.rst

UAntwerp storage guidelines
---------------------------

* ``$VSC_HOME`` should only be used
  for all **configuration files** that Linux programs use.

  * It should not be used to install software or to run jobs from.
  * It is also not meant to be heavily written to, but offers excellent read performance. 
  * Backups are made on a daily basis.

* ``$VSC_DATA`` should be used for data that should be stored for a **longer time**,
  because it will be reused on the cluster.

  * It is the best place to install **software you prefer to install yourself**.
    For performance reasons we do advice users though to build on
    existing centrally installed software, and not do a complete install of
    (e.g.) Python or R if it can be build upon the central installation.
  * It should not be used to store temporary data or run jobs on.
    We may however ask users who tend to generate **many small files** to use
    this file system instead of the scratch file system.
  * Backups are made on a daily basis, but directories with large installations
    or many small files may be excluded.

* ``$VSC_SCRATCH`` is stored on a parallel file system,
  which is optimized for **large I/O transfers** to **large files**.

  * It should be used to temporary or transient data (unless told otherwise).
  * There is no backup.

.. warning::
  The VSC storage is not meant for backup purposes.
  You should not rely on it to store all data of your PhD or postdoc.
  It is the individual user's responsibility to store that data on reliable
  storage managed by your research group or the ICT service of the university.

Environment variables
=====================

The environment variables point to your directories on the different
storage locations.

+----------------------+---------------------------------+
| Environment variable | Path                            |
+======================+=================================+
| $VSC_HOME            | /user/antwerpen/2../vsc2....    |
+----------------------+---------------------------------+
| $VSC_DATA            | /data/antwerpen/2../vsc2....    |
+----------------------+---------------------------------+
| | $VSC_SCRATCH       | /scratch/antwerpen/2../vsc2.... |
| | $VSC_SCRATCH_SITE  |                                 |
+----------------------+---------------------------------+
| $VSC_SCRATCH_NODE    | /tmp                            |
+----------------------+---------------------------------+

The dots are wildcards that match single digits.

For users with a different home institution, the path names
will be similar to those above with trivial modifications
based on your home institution and VSC account number.

About quota
================

Additional quota can be requested via the UAntwerp support team 
at hpc@uantwerpen.be.

When requesting additional quota, please state clearly what you 
would like the new quota to be and provide a motivation on why 
you would need that increase.

For users with a different home institution, the quota on
``$VSC_HOME`` and ``$VSC_DATA`` directories are determined
by the local policy of your home institution, as these file
systems are mounted from there. This implies that you have
to ask for additional quota at your home institution.
