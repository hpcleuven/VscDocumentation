+-------------------+---------+----------+--------+---------------------+-------------------+
| Variable          | Type    | Access   | Backup | Default quota       | Total capacity    |
+===================+=========+==========+========+=====================+===================+
| $VSC_HOME         | NFS/XFS | VSC      | YES    | 3 GB, 20000 files   | 3.5 TB            |
+-------------------+---------+----------+--------+---------------------+-------------------+
| $VSC_DATA         | NFS/XFS | VSC      | YES    | 25 GB, 100000 files | 60 TB             |
+-------------------+---------+----------+--------+---------------------+-------------------+
| $VSC_SCRATCH      | BeeGFS  | leibniz, | NO     | 50 GB               | 0.6 PB            |
| $VSC_SCRATCH_SITE |         | vaughan  |        |                     |                   |
+-------------------+---------+----------+--------+---------------------+-------------------+
| $VSC_SCRATCH_NODE | ext4    | Node     | NO     |                     | node-specific (*) |
+-------------------+---------+----------+--------+---------------------+-------------------+

(*) For more details, see the hardware information for 
:ref:`Vaughan <Vaughan hardware>`, :ref:`Leibniz <Leibniz hardware>` and :ref:`Breniac <Breniac hardware UAntwerp>`.