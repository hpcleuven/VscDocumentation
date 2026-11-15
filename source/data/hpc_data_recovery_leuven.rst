The snapshots can be found in two ways.
Either from the top-level folder on ``$VSC_HOME`` and ``$VSC_DATA``:

- ``/user/leuven/.snapshot`` for ``$VSC_HOME``
- ``/data/leuven/.snapshot`` for ``$VSC_DATA``

Or equivalently, from any nested subfolder inside ``$VSC_HOME`` and
``$VSC_DATA``. For instance, if a file is missing from ``projects/simulations``
folder, you may retrieve it from:

- ``$VSC_DATA/projects/simulations/.snapshot``

In these ``.snapshot`` directories, a number of directories can be found with
names of the form ``hourly.<timestamp>``, ``daily.<timestamp>`` or
``weekly.<timestamp>``; where *timestamp* reflects the moment that snapshot was
taken. For example, the directory ``weekly.2019-06-09_0000`` will contain the
snapshot taken at midnight on June 9, 2019.

The directory structure of all the directories mirrors that of ``/user/leuven``
and ``/data/leuven`` respectively, so the most recent backup of your home
directory can be found in  ``/user/leuven/.snapshot/hourly.2019-06-12_0205/301/vsc30124``.

In this directory, you will find all your files in the state they were in when
that particular snapshot was made, and you can simply copy them using the
familiar bash shell operations.

.. note::

    You can indeed retrieve older states of your files using the snapshots, taken
    strictly at fixed time intervals. However, for a full control over the history
    of your critical files, you may consider using version control. Good example of
    that would be using Github or the private Gitlab services offered at KU Leuven.
