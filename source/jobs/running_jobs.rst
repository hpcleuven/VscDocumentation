.. _running jobs:

Running jobs
============

An HPC cluster is a multi-user system.  This implies that your computations
run on a part of the cluster that will be temporarily reserved for you by
the scheduler.

.. warning::

   Do not run computationally intensive tasks on the login nodes! These
   nodes are shared among all active users, so putting a heavy load on those
   nodes will annoy other users.

Although you can :ref:`work interactively <interactive jobs>` on an HPC system,
most computations are performed in batch mode.

The workflow is straightforward:

#. Create a job script.
#. Submit it as a job to the scheduler.
#. Wait for the computation to run and finish.


Job script
----------

A job script is essentially a Bash script, augmented with information for the
scheduler.  As an example, consider a file ``hello_world.pbs`` as below.

.. code-block:: bash
   :linenos:

   #!/usr/bin/env bash

   #PBS -l nodes=1:ppn=1
   #PBS -l walltime=00:05:00
   #PBS -l pmem=1gb

   cd $PBS_O_WORKDIR

   module purge
   module load Python/3.7.2-foss-2018a

   python hello_world.py


We discuss this script line by line.

- Line 1 is a she-bang that indicates that this is a Bash script.
- Lines 3-5 inform the scheduler about the resources required by this job.

  - It requires a single node (``nodes=1``), and a single core (``ppn=1``) on
    that node.
  - It will run for at most 5 minutes (``walltime=00:05:00``).
  - It will use at most 1 GB of RAM (``pmem=1gb``).

- Line 7 changes the working directory to the directory in which the job will
  be submitted (that will be the value of the ``$PBS_O_WORKDIR`` environment
  variable when the job runs).
- Lines 9 and 10 set up the environment by :ref:`loading the appropriate modules 
  <module system basics>`.
- Line 12 performs the actual computation, i.e., running a Python script.

.. warning::

   When running on KU Leuven/UHasselt and Tier-1 infrastructure make sure to specify
   a credit account as part of your job script, if not, your job will not
   run.

   ::

      #PBS -A lp_example

   For more information, see :ref:`credit system basics<credit system basics>`.

Every job script has the same basic structure.

.. note::

   Although you can use any file name extension you want, it is good practice
   to use ``.pbs`` since that allows support staff to easily identify your
   job script.

More information is available on

- :ref:`specifying job resources <resource specification>`,
- :ref:`specifying job names, output files and notifications
  <specifying output files and notifications>`,
- using the :ref:`credit system <credit system basics>` (KU Leuven/UHasselt
  infrastructure and Tier-1 only),
- using the :ref:`module system <module system basics>`.


Submitting and monitoring a job
-------------------------------

Once you have created your job script, and transferred all required input data
if necessary, you can submit your job to the scheduler

::

   $ qsub hello_world.pbs
   205814.leibniz

The ``qsub`` returns a job ID, an unique identifier that you can use to manage
your job.  Only the number, i.e., ``205814`` is significant.

Once submitted, you can monitor the status of your job using the ``qstat`` command.

::

   $ qstat
   Job ID                    Name             User            Time Use S Queue
   ------------------------- ---------------- --------------- -------- - -----
   205814.leibniz            hello_world.pbs  vsc30140               0 Q q1h

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
   :maxdepth: 3
   
   submitting and monitoring your jobs <submitting_and_managing_jobs_with_torque_and_moab>


Job output
----------

By default, the output of your job is saved to two files.

``<job_name>.o<job_id>``
   This file contains all text written to standard output, as well as some
   information about your job.
``<job_name>.e<job_id>``
   This file contains all text written to standard error, if any.  If your job fails,
   or doesn't produce the expected output, this is the first place to look.

For instance, for the running example, the output file would be
``hello_world.pbs.o205814`` and contains

.. code-block::
   :linenos:

   ===== start of prologue =====
   Date : Mon Aug  5 14:50:28 CEST 2019
   Job ID : 205814
   Job Name : hello_world.pbs
   User ID : vsc30140
   Group ID : vsc30140
   Queue Name : q1h
   Resource List : walltime=00:05:00,nodes=1:ppn=1,neednodes=1:ppn=1
   ===== end of prologue =======
   
   hello world!
   
   ===== start of epilogue =====
   Date : Mon Aug  5 14:50:29 CEST 2019
   Session ID : 21768
   Resources Used : cput=00:00:00,vmem=0kb,walltime=00:00:02,mem=0kb,energy_used=0
   Allocated Nodes : r3c08cn1.leibniz 
   Job Exit Code : 0
   ===== end of epilogue =======

Lines 1 through 10 are written by the prologue, i.e., the administrative script that
runs before your job script.  Similarly, lines 12 though 19 are written by the
epilogue, i.e., the administrative script that runs after your job script.

Line 11 is the actual output of your job script.

.. note::

   The format of the output file differs slightly from cluster to cluster, although
   the overall structure is the same.


Troubleshooting
---------------

.. toctree::
   :maxdepth: 2

   Why doesn't my job start immediately? <why_doesn_t_my_job_start>
   Why does my job fail after a successful start? <what_if_jobs_fail_after_starting_successfully>


Advanced topics
---------------

-  :doc:`monitoring_memory_and_cpu_usage_of_programs`, which helps to find the
   right parameters to improve your specification of the job requirements.
-  :doc:`worker_framework`: To manage lots of small jobs on a cluster. The
   cluster scheduler isn't
   meant to deal with tons of small jobs. Those create a lot of
   overhead, so it is better to bundle those jobs in larger sets.
-  The :doc:`checkpointing_framework` can be used to run programs that take
   longer than the maximum time
   allowed by the queue. It can break a long job in shorter jobs, saving
   the state at the end to automatically start the next job from the
   point where the previous job was interrupted.
