.. _running jobs torque:

Running jobs in Torque
======================

VSC clusters using the Torque job scheduler:

.. include:: clusters_torque.rst

.. note:: Other clusters might use the :ref:`Slurm job scheduler <running jobs>`

The workflow in the HPC is straightforward:

#. Create a job script
#. Submit it as a job to the scheduler
#. Wait for the computation to run and finish

Job script
----------

A job script is essentially a Bash script, augmented with information for the
scheduler.  As an example, consider a file ``hello_world.pbs`` as below.

.. code-block:: bash
   :linenos:

   #!/usr/bin/env bash

   #PBS -l nodes=1:ppn=1
   #PBS -l walltime=00:05:00
   #PBS -l mem=1gb

   cd $PBS_O_WORKDIR

   module purge
   module load Python/3.12.3-GCCcore-13.3.0

   python hello_world.py


We discuss this script line by line.

- Line 1 is a she-bang that indicates that this is a Bash script.
- Lines 3-5 inform the scheduler about the resources required by this job.

  - It requires a single node (``nodes=1``), and a single core (``ppn=1``) on
    that node.
  - It will run for at most 5 minutes (``walltime=00:05:00``).
  - It will use at most 1 GB of RAM (``mem=1gb``).

- Line 7 changes the working directory to the directory in which the job will
  be submitted (that will be the value of the ``$PBS_O_WORKDIR`` environment
  variable when the job runs).
- Lines 9 and 10 set up the environment by
  :ref:`loading the appropriate modules <module_system_basics>`.
- Line 12 performs the actual computation, i.e., running a Python script.

Every job script has the same basic structure.

.. note::

   Although you can use any file name extension you want, it is good practice
   to use ``.pbs`` since that allows support staff to easily identify your
   job script.

More information is available on:

.. toctree::
   :maxdepth: 2

   Job resources <specifying_resources>
   Job names, output files and notifications <specifying_output_files_and_notifications>
   Starting programs <starting_programs_in_a_job>

.. seealso::

   Using the :ref:`module system <module_system_basics>`

Submitting and monitoring a job
-------------------------------

Once you have created your job script, and transferred all required input data
if necessary, you can submit your job to the scheduler

::

   $ qsub hello_world.pbs
   11549090

The ``qsub`` returns a job ID, an unique identifier that you can use to manage
your job.

Once submitted, you can monitor the status of your job using the ``qstat`` command.

::

   $ qstat
   Job ID     Name             User            Time Use S Queue
   ---------- ---------------- --------------- -------- - -------
   11549090   hello_world.pbs  vsc30140        0:00:10  C cpu... 

The status of your job is given in the ``S`` column.  The most common values are
given below.

+--------+------------------------------------------------------+
| status | meaning                                              |
+========+======================================================+
| Q      | job is *queued*, i.e., waiting to be executed        |
+--------+------------------------------------------------------+
| R      | job is *running*                                     |
+--------+------------------------------------------------------+
| C      | job is *completed*, i.e., finished.                  |
+--------+------------------------------------------------------+

More information is available on

.. toctree::
   :maxdepth: 2

   Submitting and monitoring your jobs <submitting_and_managing_jobs_with_torque_and_moab>

Job output
----------

By default, the output of your job is saved to two files.

``<job_name>.o<jobid>``
   This file contains all text written to standard output, as well as some
   information about your job.
``<job_name>.e<jobid>``
   This file contains all text written to standard error, if any.  If your job fails,
   or doesn't produce the expected output, this is the first place to look.


Troubleshooting
---------------

* :ref:`why_not_job_start`
* :ref:`job failure`


Advanced topics
---------------

.. toctree::
   :maxdepth: 2
   :hidden:

   monitoring_memory_and_cpu_usage_of_programs
   worker_framework
   checkpointing_framework

-  :ref:`monitoring memory and cpu`, which helps to find the
   right parameters to improve your specification of the job requirements.
-  :ref:`worker framework`: To manage lots of small jobs on a cluster. The
   cluster scheduler isn't
   meant to deal with tons of small jobs. Those create a lot of
   overhead, so it is better to bundle those jobs in larger sets.
-  The :ref:`checkpointing framework` can be used to run programs that take
   longer than the maximum time
   allowed by the queue. It can break a long job in shorter jobs, saving
   the state at the end to automatically start the next job from the
   point where the previous job was interrupted.
