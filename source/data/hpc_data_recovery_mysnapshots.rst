The command tool **mysnapshots** provides a simple interface to restore a file
or directory from a snapshots.

First of all you have to change directory ``cd`` to the directory that
contained (or still contains) the file/directory to be restored. If that parent
directory does not exist anymore, you can jump up to the last parent directory that still
exists. In the worse case where a lot of data is lost, this location might be
the top directory of ``$VSC_DATA`` or ``$VSC_SCRATCH`` for instance.

.. code-block:: bash

   $ cd $VSC_SCRATCH/labo
   $ ls -l
   total 8
   -rw-rw-r-- 1 vsc10930 vsc10930 2261  5 nov  2024 job.sh
   -rw-rw-r-- 1 vsc10930 vsc10930  907  5 nov  2024 results_dir

The command **mysnapshots** always works on the snapshots of the current
working directory. You can use it without arguments to list the available
snapshots for that directory ordered by date/time.

.. code-block:: bash

   $ mysnapshots
   Snapshots of $VSC_SCRATCH/labo:
   2025-05-08T17:02:44  2025-05-08T22:02:08  2025-05-09T08:01:56  2025-05-09T13:02:02

The output of the previous command shows the timestamps of the four snapshots
with data for the working directory. Now if we want to know which
files/directories are available in a specific snapshot, we can execute
**mysnapshots** with the timestamp of that snapshot in the given
``YYYY-MM-DDTHH:mm:ss`` format as argument:

.. code-block:: bash

   $ mysnapshots 2025-05-09T13:02:02
   Inventory of $VSC_SCRATCH/labo at 2025-05-09T13:02:02:
   job.sh      results_dir   old_data

In this case **mysnapshots** shows that for the snapshot *2025-05-09T13:02:02*
there are three entries available. The entries *job.sh* and *results_dir* are
already present in the current directory, while the entry *old_data* is not.

You can restore any of these entries to their previous state at
*2025-05-09T13:02:02* by calling **mysnapshots** with the timestamps of the
snapshot and the path to this item as argument. For instance, we can recover
the missing entry *old_data* from this snapshot:

.. code-block:: bash

   $ mysnapshots 2025-05-09T13:02:02 old_data
   Restoring file '$VSC_SCRATCH/labo/old_data' from snapshot at 2025-05-09T13:02:02
   Restoration complete
   $ ls -l
   total 12
   -rw-rw-r-- 1 vsc10930 vsc10930 2261  5 nov  2024 job.sh
   -rw-rw-r-- 1 vsc10930 vsc10930  907  5 nov  2024 results_dir
   -rw-rw-r-- 1 vsc10930 vsc10930   97  9 mei  2025 old_data

.. warning::

   By default, **mysnapshots** will refuse to overwrite existing
   files/directories in your working directory. Use the ``-f`` option to force
   the restoration of existing items. Beware that restoring an already existing
   directory with the ``-f`` option will also restore all files and folders
   within it as they were at that point in time. More recent files will be
   removed and all updates since then will be lost.
