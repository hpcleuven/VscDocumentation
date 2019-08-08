.. _KU Leuven storage:

KU Leuven storage
=================

The storage is organised according to the :ref:`VSC storage guidelines<data location>`

+--------------------------+------+----------+--------+----------------+
|Variable                  | Type |  Access  |Backup  | Default quota  |
+==========================+======+==========+========+================+
|$VSC_HOME                 | NFS  |  VSC     |YES     | 3 GB           |
+--------------------------+------+----------+--------+----------------+
|$VSC_DATA                 | NFS  |  VSC     |YES     | 75 GB          |
+--------------------------+------+----------+--------+----------------+
|$VSC_SCRATCH              | GPFS |  genius, |NO      | 100 GB         |
|$VSC_SCRATCH_SITE         |      |  thinking|        |                |
+--------------------------+------+----------+--------+----------------+
|$VSC_SCRATCH_NODE         | ext4 |  Node    |NO      | 200 GB genius  |
+--------------------------+------+----------+--------+----------------+

For users from other universities, the quota on $VSC_HOME and $VSC_DATA will be
determined by the local policy of your home institution as these file systems
are mounted from there. The pathnames will be similar with trivial
modifications based on your home institution and VSC account number.

+--------------------------+------------------------------+
|Variable                  |Name                          |
+==========================+==============================+
|$VSC_HOME                 |/user/leuven/30X/vsc30XYZ     |
+--------------------------+------------------------------+
|$VSC_DATA                 |/data/leuven/30X/vsc30XYZ     |
+--------------------------+------------------------------+
|$VSC_SCRATCH              |/scratch/leuven/30X/vsc30XYZ  |
|$VSC_SCRATCH_SITE         |                              |
+--------------------------+------------------------------+
|$VSC_SCRATCH_NODE         |/localscratch                 |
+--------------------------+------------------------------+

The ``$VSC_HOME`` and ``$VSC_DATA`` file systems have snapshots, so it is possible to
recover data that was accidentally deleted or modified.  You can retrieve data by
:ref:`restoring a snapshot <Restoring a snapshot>`.
