.. _KU Leuven storage:

#################
KU Leuven storage
#################

Storage on the clusters hosted at KU Leuven is organized
:ref:`in a similar way as on other VSC clusters <data location>`.
Currently, we use the NFS filesystem for home and data complemented with
the Lustre and IBM Storage Scale (GPFS) parallel filesystems for scratch storage.

VSC home and data storage
--------------------------

The table below summarizes the VSC home and data storage locations, which are shared
between all VSC clusters. They are intended for long term storage of files that are not
accessed at high frequency by compute jobs. Note that in what follows, the five digits
in the user's VSC IDs are used to construct a unique path pointing at their home
and data storages (as well as scratch storage below).

+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|Variable               | Path                             | Type   | Access        |Backup | Default quota |
+=======================+==================================+========+===============+=======+===============+
|``$VSC_HOME``          | ``/user/leuven/3../vsc3....``    | NFS    | VSC           |Yes    | 3 GiB         |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_DATA``          | ``/data/leuven/3../vsc3....``    | NFS    | VSC           |Yes    | 75 GiB        |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+

Note that for ``$VSC_HOME`` and ``$VSC_DATA``:

- data is protected by snapshots, which means it is possible to
  :ref:`recover data <restoring_snapshot>` that was accidentally deleted
  or modified,

- quota for non-``vsc3*`` users are determined by the policy of the user's
  home institution.

.. note::

   As mentioned in :ref:`data location`,  you should always (try to) use the
   environment variables rather than the paths shown in the table.

Scratch storage
----------------

Scratch storage is provided via the Lustre (Genius, wICE) and GPFS (Mindwell)
parallel file systems. The table below lists all the scratch storage locations
on the Tier-2 clusters.

+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|Variable               | Path                             | Type   | Access        |Backup | Default quota |
+=======================+==================================+========+===============+=======+===============+
|``$VSC_SCRATCH``       | ``/scratch/leuven/3../vsc3....`` | Lustre | Genius & wICE | No    | 500 GiB       |
|                       | ``/gpfs1/scratch/3../vsc3....``  | GPFS   | Mindwell      |       |               |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_SCRATCH_LUSTRE``|``/scratch/leuven/3../vsc3....``  | Lustre | Mindwell      | No    | 500 GiB       |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_SCRATCH_GPFS``  |``/gpfs1/scratch/3../vsc3....``   | GPFS   | Genius & wICE | No    | 500 GiB       |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_SCRATCH_SITE``  | ``$VSC_SCRATCH_LUSTRE``          | Lustre | Genius & wICE | No    | 500 GiB       |
|                       | ``$VSC_SCRATCH_GPFS``            | GPFS   | Mindwell      |       |               |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_SCRATCH_NODE``  | ``/local_scratch``               | ext4   | Genius        | No    | 200 GiB       |
+                       +----------------------------------+--------+---------------+-------+---------------+
|                       | ``/tmp``                         | ext4   | wICE          | No    | 600 GiB       |
+                       +----------------------------------+--------+---------------+-------+---------------+
|                       | ``/tmp``                         | ext4   | Mindwell      | No    | 600 GiB       |
+-----------------------+----------------------------------+--------+---------------+-------+---------------+

.. note::

   Non-``vsc3*`` users need to `contact the servicedesk <mailto:hpcinfo@kuleuven.be>`_
   to receive scratch storage, as it is not set up by default.

Using scratch in compute jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When your workflow interacts with the filesystem at high frequency for read-write operations,
it is recommended to use the scratch storage which is *local* to the cluster you are computing on.
The reason is that both GPFS and Lustre filesystems are designed to handle intensive input/output
(I/O) operations (where NFS can lag significantly behind in performance).
Furthermore, these filesystems handle parallel I/O operations (i.e. when multiple processes/threads
access the same file at the same time) very well.
Therefore, it is a good practice to exploit the parallel filesystem for handling parallel and/or
intensive I/O patterns, specially for intermediate files (which can be garbaged after the job finishes).

To facilitate that, the :ref:`Mindwell <mindwell hardware>` cluster comes with its local GPFS scratch filesystem,
and the :ref:`Genius <genius hardware>` and :ref:`wICE <wice hardware>` clusters come with their local Lustre
scratch filesystem. The ``$VSC_SCRATCH`` environment variable points to the local scratch storage on each cluster.

.. warning::

   The Lustre and GPFS mounts must not be abused. We strongly recommend that compute
   jobs only use the parallel file system associated with the cluster where the job
   is running on. In other words, compute jobs running on Genius and wICE have to use
   Lustre and jobs running on Mindwell have to use GPFS. Compute jobs that do not
   comply can be cancelled by the system administrators without prior notice.

.. tip::

   If your data fit into the local node scratch, that can potentially provide the highest
   throughput, because of avoiding the network overhead for I/O operations.
   But, keep in mind that the ``$VSC_SCRATCH_NODE`` is cleaned up as soon as your job ends.
   Therefore, you have to copy out the results to a more permanent storage location at the
   end of your job should you need to keep them for a longer time.

Transferring data between Lustre and GPFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To facilitate data transfers between the Lustre and GPFS storage,
Lustre is accessible from Mindwell and GPFS is accessible from Genius and
wICE. For instance, to copy a file from your Lustre scratch to your GPFS scratch,
you could go about it as follows:

.. code-block:: bash

   # If initiating the transfer from Genius or wICE:
   cp ${VSC_SCRATCH}/myfile ${VSC_SCRATCH_GPFS}

   # If initiating the transfer from Mindwell:
   cp ${VSC_SCRATCH_LUSTRE}/myfile ${VSC_SCRATCH}

As a best practice, data transfers between Lustre and GPFS should be performed through
'transfer' jobs, where you for example only request a few cores on an ``interactive`` partition.
Short transfers which don't take more than a couple of minutes can also
be performed from a Genius login node.

There are Globus endpoints defined on both Lustre and GPFS filesystems, and you can exploit
the :ref:`globus platform`. for transferring data.

Automatic scratch cleanup
^^^^^^^^^^^^^^^^^^^^^^^^^

``$VSC_SCRATCH`` at KU Leuven is not for long term storage, as files not accessed
for more than 30 days are automatically removed.
The reasoning behind this is that as long as you are actively using a file
(so accessing it), the file will not be removed.

This policy can however cause confusion when files are initially transferred
to a scratch directory. If you use for instance the ``mv`` command, the file
is not actually accessed. As a result, if the last access timestamp of the
original file is a long time in the past, the file on scratch will be considered
to be inactive and automatically removed. A similar thing happens when using
``rsync`` with the option to preserve timestamps. To avoid this problem,
the ``cp`` command (without `-a` argument) should be used for the initial
transfer of files to a scratch directory.