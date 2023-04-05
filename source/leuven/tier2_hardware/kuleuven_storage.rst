.. _KU Leuven storage:

KU Leuven storage
=================

The storage is organized according to the :ref:`VSC storage guidelines<data location>`

+------------------+--------+---------+-------+----------------+
|Variable          | Type   | Access  |Backup | Default quota  |
+==================+========+=========+=======+================+
|$VSC_HOME         | NFS    | VSC     |YES    | 3 GB           |
+------------------+--------+---------+-------+----------------+
|$VSC_DATA         | NFS    | VSC     |YES    | 75 GB          |
+------------------+--------+---------+-------+----------------+
|$VSC_SCRATCH      | Lustre | Genius  | NO    | 500 GB         |
+------------------+--------+---------+-------+----------------+
|$VSC_SCRATCH      | Lustre | wICE    | NO    | 500 GB         |
+------------------+--------+---------+-------+----------------+
|$VSC_SCRATCH_SITE | Lustre | Genius  | NO    |                |
+------------------+--------+---------+-------+----------------+
|$VSC_SCRATCH_SITE | Lustre | wICE    | NO    |                |
+------------------+--------+---------+-------+----------------+
|$VSC_SCRATCH_NODE | ext4   | Genius  | NO    | 200 GB         |
+------------------+--------+---------+-------+----------------+
|$VSC_SCRATCH_NODE | ext4   | wICE    | NO    | 600 GB         |
+------------------+--------+---------+-------+----------------+

$VSC_SCRATCH at KU Leuven is not a permanent storage. The files older than 30
days are cleaned up regularly. To be more specific, the automatic file removal is
based on the moment a file was accessed for the last time. The reasoning
behind this is that as long as you are actively using a file (so accessing it)
, the file will not be removed. This policy can however cause confusion when
files are initially transferred to a scratch directory. If you use for
instance the `mv` command, the file is not actually accessed. As a result, if
the last access timestamp of the original file is a long time in the past,
the file on scratch will be considered to be inactive and automatically
removed. A similar thing happens when using `rsync` with the option to
preserve timestamps. Also `Midnight Commander` will always preserve
timestamps when copying or moving data. To avoid this problem, the
`cp` command (without `-a` argument) should be used for the
initial transfer of files to a scratch directory.

For users from other universities, the quota on ``$VSC_HOME`` and ``$VSC_DATA``
will be determined by the local policy of your home institution as these file
systems are mounted from there. The path names will be similar with trivial
modifications based on your home institution and VSC account number.

The table below lists the path to different storages that KU Leuven users can
by default access.
Note that all KU Leuven VSC accounts start with the digit ``3``.
Also the dots ``.`` are wildcards that match single digits.

+--------------------+-------------------------------+
| Variable           | Path                          |
+====================+===============================+
| $VSC_HOME          | /user/leuven/3../vsc3....     |
+--------------------+-------------------------------+
| $VSC_DATA          | /data/leuven/3../vsc3....     |
+--------------------+-------------------------------+
| $VSC_SCRATCH       | /scratch/leuven/3../vsc3....  |
+--------------------+-------------------------------+
| $VSC_SCRATCH_NODE  | /local_scratch (Genius)       |
+--------------------+-------------------------------+
| $VSC_SCRATCH_NODE  | /tmp (wIce)                   |
+--------------------+-------------------------------+
| $VSC_SCRATCH_SITE  | $VSC_SCRATCH                  |
+--------------------+-------------------------------+

The ``$VSC_HOME`` and ``$VSC_DATA`` file systems have snapshots, so it is possible to
recover data that was accidentally deleted or modified.  You can retrieve data by
referring to :ref:`restoring a snapshot <Restoring a snapshot>`.
