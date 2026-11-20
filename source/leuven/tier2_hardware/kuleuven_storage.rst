.. _KU Leuven storage:

#################
KU Leuven storage
#################

Storage on the clusters hosted at KU Leuven is organized
:ref:`in a similar way as on other VSC clusters <data location>`.
Currently, we use an NFS filesystem for home and data complemented with
Lustre and IBM Storage Scale (GPFS) parallel filesystems for scratch
and project storage.

.. note::

   There exist environment variables that point at your home, data and parallel 
   scratch storage locations, as shown in the tables below. These 
   paths are constructed based on the 5 digits in your VSC ID, which are 
   represented by ``x`` characters below. As mentioned in :ref:`data location`,
   you should always (try to) use the environment variables rather than the paths
   shown in the tables.

VSC home and data storage
-------------------------

The table below describes the VSC home and data storage locations, which
can be acessed on all VSC clusters. These are intended for long term storage
of files that are not accessed at high frequency by compute jobs.

+-----------------------+----------------------------------+--------+------------------+-------+---------------+
| Variable              | Path                             | Type   | Access           |Backup | Default quota |
+=======================+==================================+========+==================+=======+===============+
| ``$VSC_HOME``         | ``/user/leuven/xxx/vscxxxxx``    | NFS    | All VSC clusters | Yes   | 3 GiB         |
+-----------------------+----------------------------------+--------+------------------+-------+---------------+
| ``$VSC_DATA``         | ``/data/leuven/xxx/vscxxxxx``    | NFS    | All VSC clusters | Yes   | 75 GiB        |
+-----------------------+----------------------------------+--------+------------------+-------+---------------+

Note that for ``$VSC_HOME`` and ``$VSC_DATA``:

- data is protected by snapshots, which means it is possible to
  :ref:`recover data <data_recovery>` that was accidentally deleted
  or modified,

- quota for VSC accounts that do *not* have Leuven / Hasselt as home institute are
  determined by the policy of the user's home institute. Note that you can
  check the institute of your VSC account on the `VSC account page`_.


Parallel storage
----------------

For workflows requiring frequent read or write operations (especially those
involving intermediate files), it is recommended to use one of the parallel file
systems. Compared to NFS, the GPFS and Lustre filesystems are better designed
to handle intensive serial and parallel input/output (IO) operations. If you would like
to understand better when to use the parallel storage or when to use NFS storage, have a
look at the note in :ref:`this section of the KU Leuven parallel file system page <kuluh_pfs_background>`.

Our Tier-2 clusters come with different parallel filesystems:

- :ref:`wICE <wice hardware>`: Lustre-based parallel storage

- :ref:`Mindwell <mindwell hardware>`: GPFS-based parallel storage.

We offer two types of storage solutions on our parallel file systems, catered
to different use-cases:

+----------------+---------------------------------------------------+----------------------------------------------------+
| Characteristic | :ref:`Parallel scratch storage <leuven_scratch>`  | :ref:`Project storage <project_storage>`           |
+================+===================================================+====================================================+
| Scope          | Personal storage                                  | Shared storage for group members                   |
+----------------+---------------------------------------------------+----------------------------------------------------+
| Availability   | By default on wICE and Mindwell                   | Upon request                                       |
+----------------+---------------------------------------------------+----------------------------------------------------+
| Price          | Free default storage + free (temporary) increases | Paid, charged based on monthly peak usage          |
+----------------+---------------------------------------------------+----------------------------------------------------+
| Cleaning       | :ref:`automatically cleaned up <scratch_cleanup>` | End users are responsible for cleaning.            |
|                |                                                   | :ref:`Extended permissions <project_storage_acls>` |
|                |                                                   | for team moderators for easier cleaning            |
+----------------+---------------------------------------------------+----------------------------------------------------+

For both solutions the storage is meant only for **active** data. The automatic cleanup on the parallel scratch
storage takes care of this automatically. For project storage, the responsibility lies with the team members.

For more details, take a look at the sections below. For extensions and new storage requests,
KU Leuven users can refer to the `KU Leuven service catalogue <https://icts.kuleuven.be/sc/english/research/HPC-storage>`_.
Other VSC users should contact the `KU Leuven HPC servicedesk <https://www.vscentrum.be/getintouch>`_ directly.

.. warning::

   It is *crucial* that intensive IO operations in your compute jobs are done
   on the parallel storage associated with the cluster where the job is running.
   In other words, compute jobs running on wICE have to use Lustre
   and jobs running on Mindwell have to use GPFS. Compute jobs that do not
   comply can be cancelled by the system administrators without prior notice.
   If you are looking for more information on this, please read the page on
   :ref:`parallel filesystems <kuluh_parallel_filesystems>`. If you need to transfer
   files between the two parallel filesystems, refer to the section about
   :ref:`transferring data between Lustre and GPFS <leuven_lustre_gpfs_transfer>`.


.. _leuven_scratch:

Parallel scratch storage
^^^^^^^^^^^^^^^^^^^^^^^^

Every user working on either of the KU Leuven Tier 2 clusters has two personal
scratch directories, one on wICE and one on Mindwell. For VSC accounts associated with
KU Leuven or UHasselt, these are created automatically upon the account creation.
Other VSC users should request this explicitly.

Using scratch storage is free of charge for all VSC users, and the storage quota can
be temporarily increased upon user's request. Note that this might be subject to
availability of free storage on either of the filesystems. Beware that your scratch storage
is subject to our :ref:`automatic clean up policy <scratch_cleanup>`. Hence, we propose
to move out your critical result files from your scratch storage to other permanent storage solutions.

The environment variable ``$VSC_SCRATCH`` points at your local scratch storage which depends on your
choice of cluster. On the login nodes and on the wICE compute nodes, ``$VSC_SCRATCH`` points to the
Lustre filesystem and on the Mindwell compute nodes it points to the GPFS filesystem. In the 
following table, you find an overview of some important features:

+------------------------+----------------------------------+--------+----------+----------------------------+--------+---------------+
| Variable               | Path                             | Type   | Access   | Storage-specific variable* | Backup | Default quota |
+========================+==================================+========+==========+============================+========+===============+
|``$VSC_SCRATCH``        | ``/scratch/leuven/xxx/vscxxxxx`` | Lustre | wICE     | ``$VSC_SCRATCH_LUSTRE1``   | No     | 500 GiB       |
|                        |                                  +--------+----------+----------------------------+--------+---------------+
|                        |                                  | GPFS   | Mindwell | ``$VSC_SCRATCH_GPFS1``     | No     | 500 GiB       |
+------------------------+----------------------------------+--------+----------+----------------------------+--------+---------------+

\* Use these variables in case you need to :ref:`transfer data between Lustre and GPFS <leuven_lustre_gpfs_transfer>`.

.. _scratch_cleanup:

**Automatic scratch cleanup**

``$VSC_SCRATCH`` at KU Leuven is not for long term storage, as files not accessed
for more than 30 days are automatically removed.
The reasoning behind this is that as long as you are actively using a file
(so accessing it), the file will not be removed. This means that you should
actively move or copy important files to an :ref:`external storage <external_storage>`.

The data removal policy can however cause confusion when files are initially transferred
to a scratch directory.  The ``mv`` command preserves the last access timestamp of a
file after moving it to a new destination. As a result, if the last access timestamp of the
original file is a long time in the past, the file on scratch will be considered
to be inactive and will be automatically removed. A similar thing happens when using
``rsync`` with the option to preserve timestamps. To avoid this problem,
the ``cp`` command (without ``-a`` argument) should be used to copy files to the
scratch directory, followed by removing the sources (if needed) using the ``rm``
command upon a successful transfer.

.. _project_storage:

Project storage
^^^^^^^^^^^^^^^

If you need to share data among team members on the KU Leuven clusters, you can
request a project storage. This project storage is always linked to a 
:ref:`VSC user group <groups>`. A request is always cluster-specific, meaning you
will have to submit two separate requests if you want project storage on both
wICE and Mindwell. Approval of a request for new or additional project storage
may depend on available space on the requested filesystem.

Since there is no automatic clean-up in place for project storage, but usage is reserved
for active data, conditions may apply based on the amount of inactive data present in your
project storage:

- We monitor inactive data in project storage, and might contact you to clean up your
  inactive data (or motivate its presence).

- Approval of a request for additional project storage space might also depend on the
  amount of inactive data present in your project storage.

In order to keep your project storage free from these inactive data, we strongly recommend
that you :ref:`keep track of the data in your project storage <data_tracking>`. To assist in
maintaining your project storage, we have implemented
:ref:`extended permissions for team moderators <project_storage_acls>` on all Mindwell project storage
directories, as well as all new wICE project storage directories. If you still have a wICE project
storage directory without these extra permissions, you can request them through our servicedesk.

As a team, you are free to organize this storage as you see fit, but we do
have some :ref:`recommendations regarding storage structure <storage_structure>`.

While this type of shared storage is now called 'project storage' on both file systems,
you might still be used to the old name for the project storage on wICE, namely 'staging storage'.
This is still reflected in the name and the paths of the directories:

+----------+--------------------------------+--------------------------------+--------+--------+-----------------------+
| Cluster  | Canonical path                 | User-facing path               | Type   | Backup | Default quota         |
+==========+================================+================================+========+========+=======================+
| wICE     | ``/lustre1/project/stg_xxxxx`` | ``/staging/leuven/stg_xxxxx``  | Lustre | No     | NA, only upon request |
+----------+--------------------------------+--------------------------------+--------+--------+-----------------------+
| Mindwell | ``/gpfs1/project/prj_xxxxx``   | ``/project1/leuven/prj_xxxxx`` | GPFS   | No     | NA, only upon request |
+----------+--------------------------------+--------------------------------+--------+--------+-----------------------+

With ``xxxxx`` being a number ranging from ``00001`` to ``99999``. This will automatically be assigned to your storage after
your request has been granted.

Two VSC environment variables are also available for the project storage paths, namely ``$VSC_PROJECT_LUSTRE1`` and
``$VSC_PROJECT_GPFS1``. These point to ``/lustre1/project`` and ``/gpfs1/project`` respectively.

Since there is no automatic cleanup for project storage, you might have to worry less 
about files disappearing, but note that this storage does not have a backup!
Be sure to always back up important files to an :ref:`external storage <external_storage>`.

.. _project_storage_acls:

**Access management and permissions**

A project storage top-directory requires an owner and a VSC group for exclusive access
to the storage content. By default, the owner of the project storage is the VSC user
who has requested the storage, and the group owner is set to an existing :ref:`VSC group <groups>` that
the owner is member of. We apply the POSIX permissions and grant read, write and execute permissions
to the owner, as well as to the group.

On top of that, we also add extended permissions ACLs for the moderator group of the VSC group
associated with the project storage. These permissions allow them to modify, delete and
move all files and directories in this shared storage space. This way, your group moderators have the
tools to manage their project storage without the need to ask the HPC support team to change
permissions and/or ownership of certain files and directories.

The moderator group is automatically created whenever a new project storage is created, and is
always named ``<groupname>_moderators``, with ``<groupname>`` being the name of the VSC group
associated with the project storage. The moderator group always contains all moderators of the
``<groupname>`` group. You can add or remove moderators through the 'Edit Group' page on the VSC
account page (reserved for current moderators of the group however). 

If you are interested in the technical details, we implement the following ACLs:

.. code:: bash

   # default ACLs
   setfacl -m d:g:<moderator_group>:rwx <project_dir>

   # ACLs on the top directory
   setfacl -m g:<moderator_group>:rwx <project_dir>


Note that the actual permissions of a file (or directory) may not be reflected by
``ls -l <file>``. Use ``getfacl <file>`` to get a detailed overview of all permissions.

Some remarks:

- Choose your moderators carefully! Since they can remove files and directories that do
  not belong to them, it is best to choose people with at least some Linux experience.

- The ACLs are not 100% foolproof. Users can still modify the permissions on their own files and
  directories. Depending on how they are changed, it could be that the moderators lose their elevated
  access rights on these files or directories. In general, users should avoid commands that remove group
  permissions, e.g. ``chmod g-rwx <file>``.

- The default ACLs are automatically inherited by files and directories that are created or copied
  in the project storage. This also means that files or directories that are moved (``mv``) into the
  project storage will not inherit the ACLs.

- To support your team in maintaining your project storage, we also developed the
  `duduckdb tool <https://github.com/hpcleuven/duduckdb>`_. This tool allows you to retrieve
  overviews of storage and inode usage within your project storage.


.. _leuven_lustre_gpfs_transfer:

Transferring data between Lustre and GPFS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   You can use the methods below to transfer between GPFS and Lustre project
   storage as well. Use the ``$VSC_PROJECT_XXXX`` variables instead.

To facilitate data transfers between the Lustre and GPFS storage,
Lustre is accessible from Mindwell and GPFS is accessible from wICE
and from the (wICE) login nodes. Note that GPFS is not reachable
from the wICE P100 and V100 nodes.

Two more environment variables (``$VSC_SCRATCH_LUSTRE1`` and
``$VSC_SCRATCH_GPFS1``) have been defined for this purpose, so that you can
easily find the mount location of your scratch directory on the "other"
parallel file system.

For instance, to copy a file from your Lustre scratch to your GPFS scratch,
you could go about it as follows:

.. code-block:: bash

   # If initiating the transfer from wICE:
   cp ${VSC_SCRATCH}/myfile ${VSC_SCRATCH_GPFS1}

   # If initiating the transfer from Mindwell:
   cp ${VSC_SCRATCH_LUSTRE1}/myfile ${VSC_SCRATCH}

As a best practice, data transfers between Lustre and GPFS should be performed
through 'transfer' jobs submitted to, for example, the ``interactive``
partition of :ref:`wICE <submit to wice interactive node>` or
:ref:`Mindwell <submit to mindwell interactive node>`.
Short transfers which don't take more than a couple of minutes can also
be performed from a wICE login node. For more advanced examples, please read
the :ref:`recommendations for managing data on multiple filesystems <kuluh_pfs_practical>`.

Globus endpoints have been defined on both Lustre and GPFS filesystems,
so you can use the :ref:`globus platform` for these data transfers.
For transferring large volumes of data (> 1 TB), however, we recommend using
'transfer' jobs instead of Globus for performance reasons.

Node scratch
------------

If your jobs require temporary storage that does not need to be shared across
compute nodes, you may also consider using the local node disks:

+-----------------------+----------------------------------+--------+------------------+-------+---------------+
|Variable               | Path                             | Type   | Access           |Backup | Default quota |
+=======================+==================================+========+==================+=======+===============+
|``$VSC_SCRATCH_NODE``  | ``/tmp``                         | ext4   | wICE P100 & V100 | No    | 200 GiB       |
|                       |                                  |        +------------------+       +---------------+
|                       |                                  |        | wICE             |       | 600 GiB       |
|                       |                                  |        +------------------+       +---------------+
|                       |                                  |        | Mindwell         |       | 600 GiB       |
+-----------------------+----------------------------------+--------+------------------+-------+---------------+

Though limited in storage capacity, ``$VSC_SCRATCH_NODE`` has the advantage
that no network traffic is involved. The contents of this temporary storage
location are always removed when the job ends. Therefore, results need to be
copied elsewhere if needed.
