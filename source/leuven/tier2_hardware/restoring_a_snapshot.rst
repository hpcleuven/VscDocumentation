Restoring a snapshot
====================

**Note:** *this only applies to the ``$VSC_HOME`` and ``$VSC_DATA`` directories of KU Leuven/UHasselt users.*

The backup consists of snapshots that are created at regular intervals:

1. for the past 24 hours, one snapshot per hour is avialable (``hourly.<timestamp>``);
2. for the past week, 6 snapshots are available, created once a day (``daily.<timestamp>``);
3. for the past month, 4 snapshots are available, created weekly (``weekly.<timestamp>``).

An offsite backup is maintained for older data, but operator intervention is required to restore that. The names in brackets will be explained below.

The snapshots can be found in:

- ``/user/leuven/.snapshot`` for ``$VSC_HOME``
- ``/data/leuven/.snapshot`` for ``$VSC_DATA``

In these ``.snapshot`` directories, a number of directories can be found, their names reflecting the moment the snapshot was taken, as explained above. For example, the directory ``weekly.2019-06-09_0000`` will contain the snapshot taken at midnight on June 9, 2019.

The directory structure of all the directories mirrors that of ``/user/leuven`` and ``/data/leuven`` respectively, so the most recent backup of your home directory can be found in ``/user/leuven/.snapshot/hourly.2019-06-12_0205/301/vsc30124``.

In this directory, you will find all your files in the state they were in when that particular snapshot was made, and you can simply copy them using the familiar bash shell operations.
