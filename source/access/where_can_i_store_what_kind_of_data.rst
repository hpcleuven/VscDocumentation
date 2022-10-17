.. _data location:

Where can I store what kind of data?
====================================

Data on the VSC clusters can be stored in several locations, depending
on the size and usage of these data. Following locations are available:

:ref:`Home directory <VSC home directory>`

   -  Location available as $VSC_HOME
   -  The data stored here should be relatively small, and not
      generating very intense I/O during jobs.
      Its main purpose is to store all kinds of configuration files,
      e.g., .bashrc, or MATLAB, and Eclipse configuration, ...
   -  Performance is tuned for the intended load: reading configuration
      files etc.
   -  Readable and writable on all VSC sites.
   -  As best practice, the permissions on your home directory should be
      only for yourself, i.e., 700. To share data with others, use the
      data directory.

:ref:`Data directory <VSC data directory>`

   -  Location available as $VSC_DATA
   -  A bigger 'workspace', for program code, datasets or results that
      must be stored for a longer period of time.
   -  There is no performance guarantee; depending on the cluster,
      performance may not be very high.
   -  Readable and writable on all VSC sites.

:ref:`Scratch directories <VSC scratch space>`

   -  Several types exist, available in $VSC_SCRATCH_XXX variables
   -  For temporary or transient data; there is typically no backup for
      these filesystems, and 'old' data may be removed automatically.
   -  Currently, $VSC_SCRATCH_NODE and $VSC_SCRATCH_SITE
      are defined for space that is available per
      node or per site on all nodes of the VSC.
   -  These file systems are not exported to other VSC sites.

Since these directories are not necessarily mounted on the same
locations over all sites, you should always (try to) use the environment
variables that have been created.

Quota is enabled on the three directories, which means the amount of
data you can store here is limited by the operating system, and not just
by the capacity of the disk system, to prevent that the disk system
fills up accidentally. You can see your current usage and the current
limits with the appropriate quota command as explained on the :ref:`page on
managing disk space <disk usage>`.
The actual disk capacity, shared by *all* users, can be found on the
:ref:`Available hardware <hardware>` page.

You will only receive a warning when you reach the soft limit of either
quota. You will only start losing data when you reach the hard limit.
Data loss occurs when you try to save new files: this will not work
because you have no space left, and thus you will lose these new files.
You will however not be warned when data loss occurs, so keep an eye
open for the general quota warnings! The same holds for running jobs
that need to write files: when you reach your hard quota, jobs will
crash.

A few additional site-specific remarks concerning data storage can be found
on the following pages:

   - :ref:`UAntwerpen<UAntwerp storage>`
   - :ref:`VUB<VUB storage>`
   - :ref:`HPC-UGent Tier-2<UGent storage>`
   - :ref:`KU Leuven/UHasselt<KU Leuven storage>`

.. _VSC home directory:

Home directory
--------------

This directory is where you arrive by default when you login to the
cluster. Your shell refers to it as \\"~\" (tilde), or via the
environment variable $VSC_HOME.

The data stored here should be relatively small (e.g., no files or
directories larger than a gigabyte, although this is not imposed
automatically), and usually used frequently. The typical use is storing
configuration files, e.g., by MATLAB, Eclipse, ...

The operating system also creates a few files and folders here to manage
your account. Examples are:

+-----------------------------------+-----------------------------------+
| .ssh/                             | This directory contains some      |
|                                   | files necessary for you to login  |
|                                   | to the cluster and to submit jobs |
|                                   | on the cluster. Do not remove     |
|                                   | them, and do not alter anything   |
|                                   | if you don't know what you're     |
|                                   | doing!                            |
+-----------------------------------+-----------------------------------+
| .profile                          | This script defines some general  |
| .bash_profile                     | settings about your sessions,     |
+-----------------------------------+-----------------------------------+
| .bashrc                           | This script is executed every     |
|                                   | time you start a session on the   |
|                                   | cluster: when you login to the    |
|                                   | cluster and when a job starts.    |
|                                   | You could edit this file to       |
|                                   | define variables and aliases.     |
|                                   | However, note that loading        |
|                                   | modules is strongly discouraged.  |
+-----------------------------------+-----------------------------------+
| .bash_history                     | This file contains the commands   |
|                                   | you typed at your shell prompt,   |
|                                   | in case you need them again.      |
+-----------------------------------+-----------------------------------+

.. _VSC data directory:

Data directory
--------------

In this directory you can store all other data that you need for longer
terms. The environment variable pointing to it is $VSC_DATA. There are
no guarantees about the speed you'll achieve on this volume.
I/O-intensive programs should not run directly from this volume (and if
you're not sure, whether your program is I/O-intensive, don't run from
this volume).

This directory is also a good location to share subdirectories with
other users working on the same research projects.

.. _VSC scratch space:

Scratch space
-------------

To enable quick writing from your job, a few extra file systems are
available on the work nodes. These extra file systems are called scratch
folders, and can be used for storage of temporary and/or transient data
(temporary results, anything you just need during your job, or your
batch of jobs).

You should remove any data from these systems after your processing them
has finished. There are no guarantees about the time your data will be
stored on this system, and we plan to clean these automatically on a
regular base. The maximum allowed age of files on these scratch file
systems depends on the type of scratch, and can be anywhere between a
day and a few weeks. We don't guarantee that these policies remain
forever, and may change them if this seems necessary for the healthy
operation of the cluster.

Each type of scratch has his own use:

**Shared scratch ($VSC_SCRATCH)**
   To allow a job running on multiple nodes (or multiple jobs running on
   separate nodes) to share data as files, every node of the cluster
   (including the login nodes) has access to this shared scratch
   directory. Just like the home and data directories, every user has
   its own scratch directory. Because this scratch is also available
   from the login nodes, you could manually copy results to your data
   directory after your job has ended. Different clusters on the same
   site may or may not share the scratch space pointed to by
   $VSC_SCRATCH.
   This scratch space is provided by a central file server that contains
   tens or hundreds of disks. Even though it is shared, it is usually
   very fast as it is very rare that all nodes would do I/O
   simultaneously. It also implements a parallel file system that allows
   a job to do parallel file I/O from multiple processes to the same
   file simultaneously, e.g., through MPI parallel I/O.
   For most jobs, this is the best scratch system to use.
**Site scratch ($VSC_SITE_SCRATCH)**
   A variant of the previous one, may or may not be the same. On
   clusters that have access to both a cluster-local scratch and
   site-wide scratch file system, this variable will point to the
   site-wide available scratch volume. On other sites it will just point
   to the same volume as $VSC_SCRATCH.
**Node scratch ($VSC_SCRATCH_NODE)**
   Every node has its own scratch space, which is completely separated
   from the other nodes. On many cluster nodes, this space is provided
   by a local hard drive or SSD. Every job automatically gets its own
   temporary directory on this node scratch, available through the
   environment variable $TMPDIR. $TMPDIR is guaranteed to be unique for
   each job.
   Note however that when your job requests multiple cores and these
   cores happen to be in the same node, this $TMPDIR is shared among the
   cores! Also, you cannot access this space once your job has ended.
   And on a supercomputer, a local hard disk may not be faster than a
   remote file system which often has tens or hundreds of drives working
   together to provide disk capacity.
**Global scratch ($VSC_SCRATCH_GLOBAL)**
   We may or may not implement a VSC-wide scratch volume in the
   future, and the environment variable VSC_SCRATCH_GLOBAL is reserved
   to point to that scratch volume. Currently is just points to the same
   volume as $VSC_SCRATCH or $VSC_SITE_SCRATCH.
