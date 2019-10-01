.. _credit system basics:

Credit system basics
====================

VSC infrastructure hosted by KU Leuven uses a credit system, so if you want
to use this infrastructure, you will need :ref:`access to a credit account
<Credits to use KU Leuven infrastructure>`.


Introduction
------------

The accounting system is very similar to a regular bank.
Individual users have accounts that will be charged for the jobs they
run. However, the number of credits on such accounts is fairly small, so
research projects will typically have one or more project accounts
associated with them. Users that are project members can have their
project-related jobs charged to such a project account. In this how-to,
the technical aspects of accounting are explained.

Checking an account balance
---------------------------

Since no calculations can be done without credits, it is quite useful to
determine the amount of credits at your disposal. This can be done quite
easily::

   $ mam-balance

This will provide an overview of the balance on the user's personal
account, as well as on all project accounts the user has access to.

Obtaining a job quote
---------------------

In order to determine the cost of a job, the user can request a quote.
The ``gquote`` commands takes those options as the ``qsub`` command that are
relevant for resource specification (-l, -q, -C), and/or, the PBS script
that will be used to run the job. The command will calculate the maximum
cost based on the resources that are requested, taking into account
walltime, number of compute nodes and node type::

   $ module load accounting
   $ gquote  -l walltime=5:00:00  -l nodes=3:ppn=36

The resources can be specified either on the command line as in the example
above, in the job script, or in both.  Just like for ``qsub``, the
specifications on the command line take priority over those in the
job script::

   $ module load accounting
   $ gquote  -l walltime=5:00:00  myjob.pbs

In this case, the number of nodes and the node type will be derived from
the specification in ``myjob.pbs``.

Details of how to tailor job requirements can be found on the page on
":ref:`resource specification`".

.. note::

   ``gquote`` will always show the maximum amount of credits your job
   can be charged.  For instance, if no node type is specified, ``gquote``
   assumes your job will run on the most expensive one.

   Obviously, ``gquote`` only provides a quote, you will be charged for
   the actual resource usage, not the requested resources.


Running jobs: accounting workflow
---------------------------------

When a job is submitted using ``qsub``
and it has to be charged against a project account, the name of the
project has to be specified as an option. In case of the introduction
credits the project account should be specified as  ``default_project``::

   $ qsub  -A lp_astrophysics_014  run-job.pbs

If the account to be charged, i.e., ``lp_astrophysics_014``, has insufficient
credits for the job, the user receives a warning at this point.

Just prior to job execution, a reservation will be made on the specified
project's account, or the user's personal account if no project was
specified. When the user checks her balance at this point, she will
notice that it has been decreased with an amount equal to, or less than
that provided by ``gquote``. The latter may occur when the node type is
determined when the reservation is made, and the node type is less
expensive than that assumed by ``gquote``. If the relevant account has
insufficient credits at this point, the job will be deleted from the
queue.

When the job finishes, the account will effectively be charged. The
balance of that account will be equal or larger after charging. The
latter can occur when the job has taken less walltime than the
reservation was made for. This implies that although quotes and
reservations may be overestimated, users will only be charged for the
resources their jobs actually consumed.


Obtaining an overview of transactions
-------------------------------------

A bank provides an overview of the financial transactions on your
accounts under the form of statements. Similarly, the job accounting
system provides statements that give the user an overview of the cost of
each individual job. The following command will provide an overview of
all transactions on all accounts the user has access to::

   $ module load accounting
   $ mam-statement

.. note::

   It takes quite a while to compute such statements, so **please
   be patient**.  If you simply want a list of the transaction,
   consider using ``mam-list-transactions``, this is typically
   much faster.

However, it is more convenient to filter this information so that only
specific projects are displayed and/or information for a specific period
of time, e.g.,

::

   $ mam-statement  -a lp_astrophysics_014  -s 2010-09-01  -e 2010-09-30

This will show the transactions on the account for the
``lp_astrophysics_014`` project for the month September 2010.

If you are only interested in the individual transaction, and don't require
balance information, ``mam-list-transactions`` provides a much faster
alternative::

   $ mam-list-transactions  -a lp_astrophysics_014  -s 2010-09-01  -e 2010-09-30

It can be Very useful to add the ``--summarize`` option to the ``mam-statement``
command::

   $ mam-statement  -a lp_prodproject  --summarize  -s 2010-09-01  -e 2010-09-30
   ################################################################################
   #
   # Statement for project lp_prodproject
   # Statement for user vsc30002
   # Includes account 536 (lp_prodproject)
   # Generated on Thu Nov 17 11:49:55 2010.
   # Reporting account activity from 2010-09-01 to 2010-09-30.
   #
   ################################################################################
   Beginning Balance:                 0.00
   ------------------ --------------------
   Total Credits:                 10000.00
   Total Debits:                     -4.48
   ------------------ --------------------
   Ending Balance:                 9995.52
   ############################### Credit Summary #################################
   Object     Action   Amount
   ---------- -------- --------
   Allocation Activate 10000.00
   ############################### Debit Summary ##################################
   Object Action Project             User     Machine Amount Count
   ------ ------ ------------------- -------- ------- ------ -----
   Job    Charge lp_prodproject      vsc30002 SVCS1    -4.26 13
   Job    Charge lp_prodproject      vsc30140 SVCS1    -0.22 1
   ############################### End of Report ##################################

As you can see it will give you a summary of credits used (Amount) and
number of jobs (Count) per user in a given time frame for a specified
project.


Reviewing job details
---------------------

A statement is an overview of transactions, but provides no details on
the resources the jobs consumed. However, the user may want to examine
the details of a specific job. This can be done using the following
command::

   $ module load accounting
   $ mam-list-transactions  -J 20030021

Where job ID does not have to be complete.

.. note:

   Charging is done for the number of compute nodes used by the
   job, not the number of cores. This implies that a single core job on a
   single node is as expensive as an 36 core job on the same single node.
   The rationale is that the scheduler instates a single user per node
   policy. Hence using a single core on a node blocks all other cores for
   other users' jobs. If a user needs to run many single core jobs
   concurrently, she is advised to use the :ref:`worker framework`.


.. include:: links.rst
