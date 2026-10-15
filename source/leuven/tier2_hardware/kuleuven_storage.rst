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
   in your VSC ID, which are represented by "x" characters below. As mentioned in
   :ref:`data location`, you should always (try to)
   use the environment variables rather than the paths shown in the tables.

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
  :ref:`recover data <restoring_snapshot>` that was accidentally deleted
  or modified,

- quota for VSC accounts that do *not* have Leuven / Hasselt as home institute are
  determined by the policy of the user's home institute. Note that you can
  check the institute of your VSC account on the `VSC account page`_.

.. _leuven_scratch:

Parallel scratch storage
------------------------

For workflows requiring frequent read or write operations (especially those
involving intermediate files), it is recommended to use scratch storage.
Compared to NFS, the GPFS and Lustre filesystems are better designed to handle
intensive serial and parallel input/output (IO) operations.
:ref:`wICE <wice hardware>` uses Lustre-based scratch storage, while
:ref:`Mindwell <mindwell hardware>` comes with GPFS-based scratch
storage.

Types of scratch directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next to having two different types of scratch storage coupled to our clusters,
you can also have two different types of directories on each of the
scratch storages:

- ``$VSC_SCRATCH``: this is your personal scratch storage, available to everyone by default.
  It can be temporarily extended for free, but is subject to 
  :ref:`automatic cleaning <scratch_cleanup>`.

- project storage: this is a shared storage space, but is only available upon request.
  Clean-up is the responsibility of the team members. Moderators of the associated group also
  have :ref:`extended permissions <project_storage_acls>`. Note that project storage 
  is a paid service.

For extensions and new storage requests, please refer to the `KU Leuven service catalogue <https://icts.kuleuven.be/sc/english/research/HPC-storage>`_.

+------------------------+----------------------------------+--------+---------------+-------+---------------+
| Variable               | Path                             | Type   | Access        |Backup | Default quota |
+========================+==================================+========+===============+=======+===============+
|``$VSC_SCRATCH``        | ``/scratch/leuven/xxx/vscxxxxx`` | Lustre | wICE          | No    | 500 GiB       |
|                        |                                  +--------+---------------+-------+---------------+
|                        |                                  | GPFS   | Mindwell      | No    | 500 GiB       |
+------------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_PROJECT_LUSTRE1``| ``/lustre1/project``             | Lustre | wICE          | No    | NA            |
+------------------------+----------------------------------+--------+---------------+-------+---------------+
|``$VSC_PROJECT_GPFS1``  | ``/gpfs1/project``               | GPFS   | Mindwell      | No    | NA            |
+------------------------+----------------------------------+--------+---------------+-------+---------------+

On each node, the ``$VSC_SCRATCH`` environment variable will point to the
scratch storage associated with the node (GPFS scratch on the Mindwell nodes,
Lustre scratch on the wICE nodes).

For both ``$VSC_PROJECT_XXXX`` directories, you will only be able to access the
subdirectories you are part of. Request your team members to add you, or
request a new project if needed.


.. warning::

   It is *crucial* that intensive IO operations in your compute jobs are done
   on the scratch storage associated with the cluster where the job is running.
   In other words, compute jobs running on wICE have to use Lustre
   and jobs running on Mindwell have to use GPFS. Compute jobs that do not
   comply can be cancelled by the system administrators without prior notice.
   If you are looking for more information on this, please read the page on
   :ref:`parallel filesystems <kuluh_parallel_filesystems>`

.. note::

   VSC accounts whose home institute is not Leuven / Hasselt need to
   `contact the servicedesk <mailto:hpcinfo@kuleuven.be>`_
   to receive scratch storage, as it is not set up by default.

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

.. _scratch_cleanup:

Automatic scratch cleanup (``$VSC_SCRATCH``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _project_storage_acls:

Extended permissions for project storage moderators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For project storage on either Lustre or GPFS, access will be controlled
with a Linux group created on the VSC account page. This can be a new group, but you
can use your group's credit account as well.

The moderators of the project storage group will be automatically added to a
``<groupname>_moderators`` group. We automatically apply extended permissions (ACLs) for this
group. These permissions allow them to modify, delete and move all files and directories in
this shared storage space. This way, your team has the tools to manage their project storage
without the need to ask the HPC support team to change permissions and/or ownership of certain
files and directories.

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

- The top directory of the project storage is writeable only by the moderators. They can create
  subdirectories, which can then be used by their team members.

- The ACLs are not 100% foolproof. Users can still modify the permissions on their own files and
  directories. Depending on how they are changed, it could be that the moderators lose their elevated
  access rights on these files or directories. In general, you should not create more restrictive
  permissions.

- The default ACLs are automatically inherited by files and directories that are created or copied
  in the project storage. This also means that files or directories that are moved (``mv``) into the
  project storage will not inherit the ACLs.

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
