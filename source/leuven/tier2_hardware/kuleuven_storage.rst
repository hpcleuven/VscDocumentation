.. _KU Leuven storage:

#################
KU Leuven storage
#################

Storage on the clusters hosted at KU Leuven is organized
:ref:`in a similar way as on other VSC clusters <data location>`.
Currently, we use an NFS filesystem for home and data complemented with
Lustre and IBM Storage Scale (GPFS) parallel filesystems for scratch storage.

.. note::

   We use environment variables to point at your different storage locations, as
   demonstrated in the tables below. These paths are constructed based on the 5 digits
   in your VSC ID. As mentioned in :ref:`data location`, you should always (try to)
   use the environment variables rather than the paths shown in the tables.

VSC home and data storage
-------------------------

The table below describes the VSC home and data storage locations, which
can be acessed on all VSC clusters. These are intended for long term storage
of files that are not accessed at high frequency by compute jobs.

+-----------------------+----------------------------------+--------+------------------+-------+---------------+
| Variable              | Path                             | Type   | Access           |Backup | Default quota |
+=======================+==================================+========+==================+=======+===============+
| ``$VSC_HOME``         | ``/user/leuven/3../vsc3....``    | NFS    | All VSC clusters | Yes   | 3 GiB         |
+-----------------------+----------------------------------+--------+------------------+-------+---------------+
| ``$VSC_DATA``         | ``/data/leuven/3../vsc3....``    | NFS    | All VSC clusters | Yes   | 75 GiB        |
+-----------------------+----------------------------------+--------+------------------+-------+---------------+

Note that for ``$VSC_HOME`` and ``$VSC_DATA``:

- data is protected by snapshots, which means it is possible to
  :ref:`recover data <restoring_snapshot>` that was accidentally deleted
  or modified,

- quota for non-``vsc3*`` users are determined by the policy of the user's
  home institution.

Scratch storage
---------------

Scratch storage is provided via the Lustre (Genius, wICE) and GPFS (Mindwell)
parallel file systems. The table below lists all the scratch storage locations
on the Tier-2 clusters.

+-----------------------+----------------------------------+--------+---------------+-------+---------------+
| Variable              | Path                             | Type   | Access        |Backup | Default quota |
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

For workflows requiring frequent read or write operations, it is recommended
to use scratch storage (specially for intermediate files). Compared to NFS,
the GPFS and Lustre filesystems are better designed to handle intensive serial
and parallel input/output (IO) operations. :ref:`Genius <genius hardware>`
and :ref:`wICE <wice hardware>` share the same (Lustre based) scratch storage,
while Mindwell comes with its own (GPFS based) scratch storage.

On each node, the ``$VSC_SCRATCH`` environment variable will point to the
scratch storage associated with the node (GPFS scratch on the Mindwell nodes,
Lustre scratch on the nodes of Genius and wICE).

.. warning::

   It is *crucial* that intensive IO operations in your compute jobs are done
   on the scratch storage associated with the cluster where the job is running.
   In other words, compute jobs running on Genius and wICE have to use Lustre
   and jobs running on Mindwell have to use GPFS. Compute jobs that do not
   comply can be cancelled by the system administrators without prior notice.

.. tip::

   If you need temporary scratch that does not need to be shared across
   compute nodes, you may also consider using the local node disks
   (``$VSC_SCRATCH_NODE``), which has the advantage that no network traffic
   is involved. The content of ``$VSC_SCRATCH_NODE`` is always removed when
   the job ends and therefore results need to be copied elsewhere if needed.

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

Globus endpoints have been defined on both Lustre and GPFS filesystems,
so you can use the :ref:`globus platform` for these data transfers.

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
the ``cp`` command (without ``-a`` argument) should be used to copy files to the
scratch directory, followed by removing the sources (if needed) using  the ``rm``
command upon a successful transfer.