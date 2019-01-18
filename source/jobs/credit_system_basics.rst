.. _credit system basics:

Credit system basics
====================

Introduction
------------

The accounting system on ThinKing is very similar to a regular bank.
Individual users have accounts that will be charged for the jobs they
run. However, the number of credits on such accounts is fairly small, so
research projects will typically have one or more project accounts
associated with them. Users that are project members can have their
project-related jobs charged to such a project account. In this how-to,
the technical aspects of accounting are explained.

How to request credits on the KU Leuven Tier-2 systems
------------------------------------------------------

You can request 2 types of job credits: introduction credits and project
credits. **Introduction credits** are a limited amount of free credits
for test and development purposes. **Project credits** are job credits
used for research.

How to request introduction credits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find all relevant information in the `HPC section of the Service
Catalog (login required) <\%22https://icts.kuleuven.be/sc/HPC\%22>`__.

How to request project credits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find all relevant information in the `HPC section of the Service
Catalog (login required) <\%22https://icts.kuleuven.be/sc/HPC\%22>`__.

Prices
~~~~~~

All details about prices you can find on `HPC section of the Service
Catalog (login required) <\%22https://icts.kuleuven.be/sc/HPC\%22>`__ .

Checking an account balance
---------------------------

Since no calculations can be done without credits, it is quite useful to
determine the amount of credits at your disposal. This can be done quite
easily:

::

   $ module load accounting
   $ mam-balance

This will provide an overview of the balance on the user's personal
account, as well as on all project accounts the user has access to.

Obtaining a job quote
---------------------

In order to determine the cost of a job, the user can request a quote.
The gquote commands takes those options as the qsub command that are
relevant for resource specification (-l, -q, -C), and/or, the PBS script
that will be used to run the job. The command will calculate the maximum
cost based on the resources that are requested, taking into account
walltime, number of compute nodes and node type.

::

   $ module load accounting
   $ gquote -q qlong -l nodes=3:ppn=20:ivybridge

Details of how to tailor job requirements can be found on the page on
\\"\ `Specifying resources, output files and
notifications <\%22/cluster-doc/running-jobs/specifying-requirements\%22>`__\\".

Note that when a queue is specified and no explicit walltime, the
walltime used to produce the quote is the longest walltime allowed by
that queue. Also note that unless specified by the user, gquote will
assume the most expensive node type. This implies that the cost
calculated by gquote will always be larger than the effective cost that
is charged when the job finishes.

Running jobs: accounting workflow
---------------------------------

When a job is submitted using
`qsub <\%22/cluster-doc/running-jobs/submitting-managing-jobs\%22>`__,
and it has to be charged against a project account, the name of the
project has to be specified as an option.

::

   $ qsub -A l_astrophysics_014 run-job.pbs

If the account to be charged, i.e., l_astrophysics_014, has insufficient
credits for the job, the user receives a warning at this point.

Just prior to job execution, a reservation will be made on the specified
project's account, or the user's personal account if no project was
specified. When the user checks her balance at this point, she will
notice that it has been decreased with an amount equal to, or less than
that provided by gquote. The latter may occur when the node type is
determined when the reservation is made, and the node type is less
expensive than that assumed by gquote. If the relevant account has
insufficient credits at this point, the job will be deleted from the
queue.

When the job finishes, the account will effectively be charged. The
balance of that account will be equal or larger after charging. The
latter can occur when the job has taken less walltime than the
reservation was made for. This implies that although quotes and
reservations may be overestimations, users will only be charged for the
resources their jobs actually consumed.

Obtaining an overview of transactions
-------------------------------------

A bank provides an overview of the financial transactions on your
accounts under the form of statements. Similarly, the job accounting
system provides statements that give the user an overview of the cost of
each individual job. The following command will provide an overview of
all transactions on all accounts the user has access to:

::

   $ module load accounting
   $ mam-statement

However, it is more convenient to filter this information so that only
specific projects are displayed and/or information for a specific period
of time, e.g.,

::

   $ mam-statement -a l_astrophysics_014 -s 2010-09-01 -e 2010-09-30

This will show the transactions on the account for the
l_astrophysics_014 project for the month September 2010.

Note that it takes quite a while to compute such statements, so **please
be patient**.

Very useful can be adding the '--summarize' option to the 'gstatement'
command:

::

   vsc30002@login1:~> mam-statement -a lp_prodproject --summarize -s 2010-09-01 -e 2010-09-30
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

As you can see it will give you a summary of used credits (Amount) and
number of jobs (Count) per user in a given timeframe for a specified
project.

Reviewing job details
---------------------

A statement is an overview of transactions, but provides no details on
the resources the jobs consumed. However, the user may want to examine
the details of a specific job. This can be done using the following
command:

::

   $ module load accounting
   # mam-list-transactions -J 20030021

Where job ID does not have to be complete.

Job cost calculation
--------------------

The cost of a job depends on the resources it consumes. Generally
speaking, one credit buys the user one hour of walltime on one reference
node. The resources that are taken into account to charge for a job are
the walltime it consumed, and the number and type of compute nodes it
ran on. The following formula is used:

(0.000278\**nodes*\ \*\ *walltime*)\*\ *nodetype*

Here,

-  *nodes* is the number of compute nodes the job ran on;
-  *walltime* the effective duration of the job, expressed in seconds;
-  *nodetype* is the factor representing the node type's performance as
   listed in the table below.

Since Tier-2 cluster has several types of compute nodes, none of which
is actually a reference node, the following values for *nodetype* apply:

+------------+-------------+
| node type  | credit/hour |
+============+=============+
| Ivy Bridge | 4.76        |
+------------+-------------+
| Haswell    | 6.68        |
+------------+-------------+
| GPU        | 2.86        |
+------------+-------------+
| Cerebro    | 3.45        |
+------------+-------------+

The difference in cost between different machines/processors reflects
the performance difference between those types of nodes. The total cost
of a job will typically be the same on any compute nodes, but the
walltime will be different nodes. It is considerably more expensive to
work on Cerebro since it has a large amount of memory, as well as local
disk, and hence required a larger investment.

An example of a job running on multiple nodes and cores is given below:

::

   $ qsub -A l_astrophysics_014 -lnodes=2:ppn=20:ivybridge simulation_3415.pbs

If this job finished in 2.5 hours (i.e., walltime is 9000), the user
will be charged:

(0.000278*2*9000)*4.76 = 23.8 credits

For a single node, single core job that also took 2.5 hours and was
submitted as:

::

   $ qsub -A l_astrophysics_014 -lnodes=1:ppn=1:ivybridge simulation_147.pbs

In this case, the user will be charged:

(0.000278*1*9000)*4.76 = 11.9 credits

Note that charging is done for the number of compute nodes used by the
job, not the number of cores. This implies that a single core job on a
single node is as expensive as an 20 core job on the same single node.
The rationale is that the scheduler instates a single user per node
policy. Hence using a single core on a node blocks all other cores for
other users' jobs. If a user needs to run many single core jobs
concurrently, she is advised to use the `Worker
framework <\%22/cluster-doc/running-jobs/worker-framework\%22>`__.

"
