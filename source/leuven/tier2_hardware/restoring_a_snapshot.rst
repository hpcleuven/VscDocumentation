Restoring a snapshot
====================

**Note:** *this only applies to the ``$VSC_HOME`` and ``$VSC_DATA`` directories of KU Leuven/UHasselt users.*

The backup consists of snapshots that are created at regular intervals:

1. for the past 24 hours, 5 snapshots are avialable, created at 4 hours intervals (``sv_hourly.[0-4]``);
2. for the past week, 6 snapshots are available, created once a day (``sv_nightly.[0-5]``);
3. for the past month, 4 snapshots are available, created weekly (``sv_weekly.[0-3]``).

An offsite backup is maintained for older data, but operator intervention is required to restore that. The names in brackets will be explained below.

The snapshots can be found in:

- ``/user/leuven/.snapshot`` for ``$VSC_HOME``
- ``/data/leuven/.snapshot`` for ``$VSC_DATA``

In these ``.snapshot`` directories, a number of directories can be found, their names reflecting the moment the snapshot was taken, as explained above. For example, the directory ``sv_weekly.0`` will contain the most recent weekly backup, while ``sv_weekly.3`` will contain the snapshot that is nearly a month old. Similarly, ``sv_hourly.0`` will be a snapshot that has been taken between now and at most 4 hours ago, ``sv_hourly.1`` was taken between approximately 4 and 8 ago, etc.

The directory structure of all the sv_* directories mirrors that of ``/user/leuven`` and ``/data/leuven`` respectively, so the most recent backup of your home directory can be found in ``/user/leuven/.snapshot/sv_hourly.0/301/vsc30124``

In this directory, you will find all your files in the state they were in when that particular snapshot was made, and you can simply copy them using the familiar bash shell operations.
