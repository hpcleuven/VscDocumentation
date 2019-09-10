.. _disk usage:

How much disk space am I using?
===============================

.. _quota:

Total disk space used on file systems with quota
------------------------------------------------

On file systems with quota enabled, you can check the amount of disk space that
is available for you, and the amount of disk space that is in use by
you.

On most systems, ``myquota`` will show you for the ``$VSC_HOME``,
``$VSC_DATA`` and ``$VSC_SCRATCH`` file systems either the
percentage of the available disk space you are using, or the
absolute amount. Users from Ghent university should check their disk usage
using the `web application <https://account.vscentrum.be/>`_.

If quota have been set on the number of files you can create on a file
system, those are listed as well.

Example::

   $ myquota
   file system $VSC_DATA
       using 35G of 75G, 1126k of 10000k files
   file system $VSC_HOME
       using 2401M of 3072M, 40342 of 100k files
   file system $VSC_SCRATCH
       using 5.82G of 100G

.. warning::

   If your file usage approaches the limits, jobs may crash unexpectedly.
   If your usage exceeds the limits, an appropriate message will be shown, 
   including the number of days of grace left before no more bit can be written.  


.. _du command:

Disk space used by individual directories
-----------------------------------------

.. warning::

   The ``du`` command will stress the file system, and all file systems
   are shared, so please use it wisely and sparingly.

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
directory, you could use the following command::

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

   du -h -s $VSC_DATA/input_data/*
   50M     /data/leuven/300/vsc30001/input_data/somedata
