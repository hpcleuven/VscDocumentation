.. _job management:

Managing and monitoring jobs
============================

Checking the queue: squeue
--------------------------

`Slurm squeue manual page on the web <https://slurm.schedmd.com/squeue.html>`_

The Slurm command to list jobs in the queue is ``squeue``.

The basic command without options will show basic information about all your jobs in the queue.
There are a number of useful command line options though:

* The ``--long`` or ``-l`` flag adds some additional information.
* ``--format=<output format>`` or ``-o <output format>`` allows you to specify
  your custom output format that can show a lot more information. Likewise,
  ``--Format=<output format>`` or ``-O <output format>`` (with a capital first letter)
  can show even more
  information but with a longer syntax for the output format. See the
  `squeue manual page <https://slurm.schedmd.com/squeue.html>`_ for information
  on all format options.
* It is possible to show that information for only one or a selection of your
  jobs by using ``--jobs=<job_id_list>`` or ``-j <job_id_list>``, where ``<job_id_list>``
  is a comma-separated list of job IDs.

The column "REASON" lists why a job is waiting for execution. It distinguishes between
30+ different reasons, way to much to discuss here, but some of the codes speak for
themselves. The full list of reason codes can be found in the
`squeue manual page <https://slurm.schedmd.com/squeue.html>`_.


Kill/delete a job: scancel
--------------------------

`Slurm scancel manual page on the web <https://slurm.schedmd.com/scancel.html>`_

The Slurm command to cancel a job is ``scancel``. In most cases, it takes only a
single argument, the unique identifier of the job to cancel.

For a job array (see below) it is also possible to cancel only some of the jobs in
the array by specifying the array elements as follows:

.. code:: bash

   scancel 20_[1-3]
   scancel 20_4 20_6

The first command would kill jobs 1, 2 and 3 in the job array with job ID 20,
the second command would kill jobs 4 and 6 of that job array.

As shown in the example above, a space separated list of multiple job IDs can also
be specified, as well as a selection based on multiple filters, e.g., in which partition
the job is running. Consult the `scancel manual page <https://slurm.schedmd.com/scancel.html>`_
for more information.

Getting more information on a running job: sstat
------------------------------------------------

`Slurm sstat manual page on the web <https://slurm.schedmd.com/sstat.html>`_

The ``sstat`` command displays information on running jobs pertaining to CPU, Task,
Node, Resident Set Size (RSS) and Virtual Memory (VM) for all your running jobs.
The jobs need to be explicitly mentioned using ``--jobs=<job_id_list>`` or
``-j <job_id_list>`` (where ``<job_id_list>`` is a comma-separated list of job IDs).

By default, it will only show information about the lowest job step running in
a particular job unless ``--allsteps`` or ``-a`` is also specified.
It is also possible to request information on a specific job step of a job
by using ``<jobid.jobstep>``, i.e., add the number of the job step to the
job ID, separated by a dot.

To show additional information not shown by the default format, one can
specify a specific format using the ``--format`` or identical ``--fields``
and ``-o`` flags.  Check the `sstat manual page <https://slurm.schedmd.com/sstat.html>`_
for further information.


Getting information about a job after it finishes: sacct
--------------------------------------------------------

`Slurm sacct manual page on the web <https://slurm.schedmd.com/sacct.html>`_

Whereas ``sstat`` is used to show near real-time information for running jobs,
``sacct`` shows the information as it is kept by Slurm in the job accounting
log/database. Hence it is particularly useful to show information about jobs
that have finished already. It allows you to see how much CPU time, wall time,
memory, etc. were used by the application.

By default, ``sacct`` shows the job ID, job name, partition name, account name,
number of CPUs allocated to the job, the state of the job and the exit code
of completed jobs. Several options can be used to modify the format:

* ``--brief`` or ``-b`` shows only the job ID, state and exit ode.
* ``--long`` or ``-l`` shows an overwhelming amount of information, probably more than you
  want to know as a regular user.
* ``--format`` or ``-o`` can be used to specify your own output format. We refer
  to the `sacct manual page <https://slurm.schedmd.com/sacct.html>`_ for an overview of
  possible fields and how to construct the format string.

By default, ``sacct`` will show information about jobs that have been running
since midnight. There are however a number of options to specify for which jobs
you want to see information:

* ``--jobs=<job_id_list>`` or ``-j <job_id_list>`` with a comma-separated list of job IDs
  (in the same format as for ``sstat``) will only show information on those jobs
  (or job steps).
* ``--starttime=<time>`` or ``-S <time>`` will show information about all jobs that
  have been running since the indicated start time. There are four possible
  formats for ``<time>``: HH:MM[:SS] [AM|PM], MMDD[YY] or MM/DD[/YY] or MM.DD[.YY],
  MM/DD[/YY]-HH:MM[:SS] and YYYY-MM-DD[THH:MM[:SS]] (where [] denotes an optional
  part).
* ``--endtime=<time>`` or ``-E <time>`` will show information about all jobs that
  have been running before the indicated end time. By combining a start time and
  end time it is possible to specify a window for the jobs.

For now, there is no reason to be concerned about the account name as we do not use
accounting to control the amount of compute time a user can use.

