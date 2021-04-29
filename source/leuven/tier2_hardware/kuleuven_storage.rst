.. _KU Leuven storage:

KU Leuven storage
=================

The storage is organized according to the :ref:`VSC storage guidelines<data location>`

+--------------------------+--------+----------+--------+----------------+
|Variable                  | Type   |  Access  |Backup  | Default quota  |
+==========================+========+==========+========+================+
|$VSC_HOME                 | NFS    |  VSC     |YES     | 3 GB           |
+--------------------------+--------+----------+--------+----------------+
|$VSC_DATA                 | NFS    |  VSC     |YES     | 75 GB          |
+--------------------------+--------+----------+--------+----------------+
|$VSC_SCRATCH              | GPFS   |  genius  |NO      | 100 GB         |
|$VSC_SCRATCH_SITE         |        |          |        |                |
+--------------------------+--------+----------+--------+----------------+
|$VSC_SCRATCH_NODE         | ext4   | genius,  |NO      | 200 GB         |
|                          |        | job only |        |                |
+--------------------------+--------+----------+--------+----------------+
|$VSC_SCRATCH_JOB          | BeeGFS | genius,  |NO      | variable       |
|                          |        | job only |        |                |
+--------------------------+--------+----------+--------+----------------+

For users from other universities, the quota on ``$VSC_HOME`` and ``$VSC_DATA``
will be determined by the local policy of your home institution as these file
systems are mounted from there. The path names will be similar with trivial
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
|$VSC_SCRATCH_NODE         |/local_scratch                |
+--------------------------+------------------------------+

The ``$VSC_HOME`` and ``$VSC_DATA`` file systems have snapshots, so it is possible to
recover data that was accidentally deleted or modified.  You can retrieve data by
:ref:`restoring a snapshot <Restoring a snapshot>`.

On genius, a BeeGFS file system can be created during the run of a job, for details,
see the page on :ref:`using BeeGFS <using BeeGFS>` for details.
