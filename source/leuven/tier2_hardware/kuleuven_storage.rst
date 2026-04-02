.. _KU Leuven storage:

#################
KU Leuven storage
#################

Storage on the clusters hosted at KU Leuven is organized
:ref:`in a similar way as on other VSC clusters <data location>`.

File systems
============

The table below provides an overview of the different storage locations
that are available to all VSC users.

The path examples and default quota are given for the case of KU Leuven /
UHasselt VSC accounts, which start with the digit ``3`` (subsequent digits
are marked with dots ``.``). For non-``vsc3*`` users the paths will be similar,
with modifications based on the user's home institution and VSC ID.

TODO: update (and possibly restructure) the table once mount points are confirmed

.. include:: kuleuven_storage_quota_table.rst

.. note::

   As mentioned in :ref:`data location`,  you should always (try to) use the
   environment variables rather than the paths shown in the table.

VSC home and data storage
--------------------------

Note that for ``$VSC_HOME`` and ``$VSC_DATA``:

- data is protected by snapshots, which means it is possible to
  :ref:`recover data <restoring_snapshot>` that was accidentally deleted
  or modified,

- quota for non-``vsc3*`` users are determined by the policy of the user's
  home institution.

Scratch storage
----------------

Scratch storage is provided via the Lustre (Genius, wICE) and GPFS (Mindwell)
parallel file systems. The following paragraphs provide more information
on how they are intended to be used.

.. note::

   Non-``vsc3*`` users need to `contact the servicedesk
   <mailto:hpcinfo@kuleuven.be>`_ to receive scratch storage,
   as it is not set up by default.

Automatic scratch cleanup
^^^^^^^^^^^^^^^^^^^^^^^^^

``$VSC_SCRATCH`` at KU Leuven is not for long term storage, as files older
than 30 days are cleaned up regularly. To be more specific, the automatic file
removal is based on the moment a file was accessed for the last time.
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

Transferring data between Lustre and GPFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To facilitate data transfers between the Lustre and GPFS storage,
Lustre is accessible from Mindwell and GFPS is accessible from Genius and
wICE. To for example copy a file from your Lustre scratch to your GFPS scratch,
you could go about it as follows:

.. code-block:: bash

   # If initiating the transfer from Genius or wICE:
   cp ${VSC_SCRATCH}/myfile ${VSC_SCRATCH_GPFS}

   # If initiating the transfer from Mindwell:
   cp ${VSC_SCRATCH_LUSTRE}/myfile ${VSC_SCRATCH}

These connections must however not be abused. We strongly recommend that compute
jobs only use the parallel file system associated with the cluster where the job
is running. In other words, compute jobs running on Genius and wICE have to use
Lustre and jobs running on Mindwell have to use GPFS. Compute jobs that do not
comply can be cancelled by the system administrators without prior notice.

It is of course OK to carry out transfers through 'transfer' jobs
where you for example only request a few cores on an ``interactive`` partition.
Short transfers which don't take more than a couple of minutes can also
be performed from a Genius login node. You may also use the
:ref:`globus platform` for transferring data.
