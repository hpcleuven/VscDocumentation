.. _UAntwerpen storage:

UAntwerpen storage
==================

The storage is organised according to the :ref:`VSC storage guidelines<data location>`

+--------------------------+------+---------+--------+----------------+
|Variable                  | Type |  Access |Backup  | Default quota  |
+==========================+======+=========+========+================+
|$VSC_HOME                 | GPFS |  VSC    |YES     | 3 GB           |
+--------------------------+------+---------+--------+----------------+
|$VSC_DATA                 | GPFS |  VSC    |YES     | 25 GB          |
+--------------------------+------+---------+--------+----------------+
|$VSC_SCRATCH              | GPFS |  Hopper,|NO      | 25 GB          |
|$VSC_SCRATCH_SITE         |      |  Leibniz|        |                |
+--------------------------+------+---------+--------+----------------+
|$VSC_SCRATCH_NODE         | ext4 |  Node   |NO      | 250 GB Hopper, |
|                          |      |         |        | 100 GB Leibniz |
+--------------------------+------+---------+--------+----------------+

For users from other universities, the quota on $VSC_HOME and $VSC_DATA will be
determined by the local policy of your home institution as these file systems
are mounted from there. The pathnames will be similar with trivial
modifications based on your home institution and VSC account number.

+--------------------------+--------------------------------+
|Variable                  |Name                            |
+==========================+================================+
|$VSC_HOME                 |/user/antwerpen/20X/vsc20XYZ    |
+--------------------------+--------------------------------+
|$VSC_DATA                 |/data/antwerpen/20X/vsc20XYZ    |
+--------------------------+--------------------------------+
|$VSC_SCRATCH              |/scratch/antwerpen/20X/vsc20XYZ |
|$VSC_SCRATCH_SITE         |                                |
+--------------------------+--------------------------------+
|(no variable)             |/small/antwerpen/20X/vsc20XYZ   |
+--------------------------+--------------------------------+
|$VSC_SCRATCH_NODE         |/tmp                            |
+--------------------------+--------------------------------+

Next to the default file systems, UAntwerpen storage also has a file system
/small.  /small is a file system optimised for the storage of small files of
types that do not belong in $VSC_HOME. The file systems pointed at by $VSC_DATA
and $VSC_SCRATCH have a large fragment size (128 kB) for optimal performance on
larger files and since each file occupies at least one fragment, small files
waste a lot of space on those file systems. The file system /small is available
on request and accessible from both Hopper and Leibniz.

