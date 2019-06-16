.. _UAntwerpen storage:

UAntwerpen storage
==================

The storage is organised according to the :ref:`VSC storage guidelines<data location>`

+--------------------------------+--------------------------+------+---------+--------+----------------+
|Name                            |Variable                  | Type |  Access |Backup  |   Quota        |
+================================+==========================+======+=========+========+================+
|/user/antwerpen/20X/vsc20XYZ    |$VSC_HOME                 | GPFS |  VSC    |YES     |   3 GB         |
+--------------------------------+--------------------------+------+---------+--------+----------------+
|/data/antwerpen/20X/vsc20XYZ    |$VSC_DATA                 | GPFS |  VSC    |YES     |   25 GB        |
+--------------------------------+--------------------------+------+---------+--------+----------------+
|/scratch/antwerpen/20X/vsc20XYZ |$VSC_SCRATCH /            | GPFS |  Hopper |NO      |   25 GB        |
|                                |$VSC_SCRATCH_SITE         |      |  Leibniz|        |                |
+--------------------------------+--------------------------+------+---------+--------+----------------+
|/small/antwerpen/20X/vsc20XYZ   |                          | GPFS |  Hopper |NO      |   0 GB         |
|                                |                          |      |  Leibniz|        |                |
+--------------------------------+--------------------------+------+---------+--------+----------------+
|/tmp                            |$VSC_SCRATCH_NODE         | ext4 |  Node   |NO      |  250 GB Hopper |
|                                |                          |      |         |        |  100 GB Leibniz|
+--------------------------------+--------------------------+------+---------+--------+----------------+

/small is a file system optimised for the storage of small files of types
that do not belong in $VSC_HOME. The file systems pointed at by $VSC_DATA and
$VSC_SCRATCH have a large fragment size (128 kB) for optimal performance on
larger files and since each file occupies at least one fragment, small files
waste a lot of space on those file systems. The file system is available on
request.

For users from other universities, the quota on $VSC_HOME and $VSC_DATA will be
determined by the local policy of your home institution as these file systems
are mounted from there. The pathnames will be similar with trivial
modifications based on your home institution and VSC account number.


