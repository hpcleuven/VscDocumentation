.. _disk usage:

How much disk space am I using?
===============================

.. _quota:

Total disk space used on filesystems with quota
-----------------------------------------------

On filesystems with quota enabled, you can check the amount of disk space that
is available for you, and the amount of disk space that is in use by
you.  Unfortunately, there is not a single command that will give
you that information for all file systems in the VSC.

On most systems, ``quota`` will show you for each file system

``space``
   The disk space taken up by your files.
``quota``
   If the disk space you are using exceeds this value, you may
   get warnings (disabled on most systems).  The reported disk
   usage will be marked with an ``*`` if it exceeds the value
   of ``quota``.
``limit``
   If the limit is reached, nothing can be written to disk, so
   applications and jobs may crash.

Example::

   quota -s
   Disk quotas for user vsc31234 (uid 123456):
     Filesystem  space    quota   limit   grace   files   quota   limit   grace
     nas2-ib1:/mnt/home
                 648M   2919M   3072M            3685       0       0
     nas2-ib1:/mnt/data
               20691M  24320M  25600M            134k       0       0
     nas1-ib1:/mnt/site_scratch
                    0  24320M  25600M               1       0       0

Each line represents a file system you have access to, ``$VSC_HOME``,
``$VSC_DATA``, and, for this particular example, ``$VSC_SCRATCH_SITE``.
When using the ``-s`` flag, ``quota`` will report disk space and limits
in human-readable format, i.e., using MB or GB, rather than blocks.

Some file systems have limits on the number of files that can be
stored, and those are represented by the last four columns. The

``files``
   The number of files on the file system owned by you.
``quota``
   If the number of files exceeds this value, you may
   get warnings (disabled on most systems).  The reported number
   of files will be marked with an ``*`` if it exceeds the value
   of ``quota``.
``limit``
   If the limit is reached, no new files can be written to disk, so
   applications and jobs may crash.

.. note::

   Using these commands on another cluster than the one
   in your home institution, will fail to return information
   about the quota on your ``$VSC_HOME`` and ``$VSC_DATA``
   directories and will show you  the quota for your ``$VSC_SCRATCH``
   directory on that system.


.. _mmlsquota:

Total disk space on GPFS file systems
-------------------------------------

On some parallel file systems, notably ``$VSC_SCRATCH`` on KU Leuven
infrastructure (Tier-1 and Tier-2), ``mmlsquota`` should be used to
display the total disk space you use and the limits you have.

These file system is a parallel file system, i.e., IBM Spectrum Scale (formerly
GPFS)::

      $ mmlsquota  --block-size auto  vol_ddn2:leuven_scratch
                               Block Limits                                                   |     File Limits
      Filesystem Fileset        type             KB      quota      limit   in_doubt    grace |    files   quota    limit in_doubt    grace  Remarks
      vol_ddn2   leuven_scratch  USR        1444864 1970061312 2073755648          0     none |    16494       0        0        0     none

The ``--block-size auto`` option respectively ensure that sizes are
reported in a human-readable format, rather than expressed in blocks.

The optional volume ``vol_ddn2:leuven`` is the fileset you want information
on.  You can leave out the fileset, but in that case ``mmlsquota`` will
display information on all filesets, most of which you don't have access
to.


.. _du command:

Disk space used by individual directories
-----------------------------------------

The command to check the size of  all subdirectories in the current
directory is ``du``::

   $ du -h
   4.0k      ./.ssh
   0         ./somedata/somesubdir
   52.0k     ./somedata
   56.0k     .

This shows you first the aggregated size of all subdirectories, and
finally the total size of the current directory "``.``" (this includes
files stored in the current directory). The ``-h`` option ensures
that sizes are displayed in human-readable form (kB, MB, GB), omitting
it will   show sizes in bytes.

If the directory contains a deep hierarchy of subdirectories,
you may not want to see the information at that depth; you
could just ask for a summary of the current directory::

   $ du -s
   54864 .

If you want to see the size of any file or top level subdirectory in the current
directory, you could use the      following command::

   du -s *
   12      a.out
   3564    core
   4       mpd.hosts
   51200   somedata
   4       start.sh
   4       test

Finally, if you don't want to know the size of the data in your
current directory, but in some other directory (e.g., your data
directory), you just pass this directory as a parameter::

   du -h -s $VSC_DATA/*
   50M     /data/leuven/300/vsc30001/somedata
