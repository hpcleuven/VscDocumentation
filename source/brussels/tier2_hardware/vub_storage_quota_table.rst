+--------------------------+------+---------+--------+----------------+
|Variable                  | Type |  Access |Backup  | Default quota  |
+==========================+======+=========+========+================+
|$VSC_HOME                 | GPFS |  VSC    |YES     | 6 GB           |
+--------------------------+------+---------+--------+----------------+
|$VSC_DATA                 | GPFS |  VSC    |YES     | 50 GB          |
+--------------------------+------+---------+--------+----------------+
| | $VSC_SCRATCH           | GPFS |  Hydra  |NO      | 100 GB         |
| | $VSC_SCRATCH_SITE      |      |         |        |                |
+--------------------------+------+---------+--------+----------------+
|$VSC_SCRATCH_NODE         | ext4 |  Node   |NO      | (no quota)     |
|                          |      |         |        |                |
+--------------------------+------+---------+--------+----------------+
