.. _accounting_leuven:
========================
Slurm Accounting
========================

The :ref:`wICE <wice_t2_leuven>` cluster uses the Slurm Account Manager (SAM) 
for credit accounting.
The reason is that having a valid Slurm account with sufficient credits in it
is mandatory for running jobs on KU Leuven Tier-2 machines. 
We developed so called SAM-commands to mimic the behavior of previously used 
MAM-commands (from the MOAB account manager). 
From the user point of view it should mostly be enough to change the prefix ``mam`` 
in the accounting command into ``sam``.

The accounting system is very similar to a regular bank. 
Individual users have accounts that will be charged for the jobs they run. 
However, the number of credits on such accounts is fairly small, so research projects 
will typically have one or more project accounts associated with them. 
Users that are project members can have their project-related jobs charged to such a 
project account. 
In this how-to, the technical aspects of accounting are explained.

Checking an account balance
---------------------------

Since no calculations can be done without credits, it is quite useful to determine the 
amount of credits at your disposal. 
This can be done by executing the following command on any KU Leuven Tier-2 node::

   $ sam-balance

This will provide an overview of the balance on the user's personal account, as well as 
on all project accounts the user has access to.


Running jobs: accounting workflow
---------------------------------

When a job is submitted using ``sbatch`` or ``srun``, it has to be charged against a 
project account.
The name of the project has to be specified as an option. 
If a user requests introductory credits, the assigned project name carries the VSC-id
of the user, e.g. ``intro_vsc3....``, where the dots ``.`` signify the user's uniqe VSC-id.

   $ sbatch -A lp_my_project run-job.slurm
   or
   $ sbatch -A intro_39999 run-job.slurm

If the account to be charged, i.e., ``lp_my_project``, has insufficient credits for the 
job, the user receives a warning at this point, and the job will never enter the queue.

Obtaining an overview of transactions
-------------------------------------

A bank provides an overview of the financial transactions on your accounts under the 
form of statements. 
Similarly, the job accounting system provides statements that give the user an overview 
of the cost of each individual job. 
The following command will provide an overview of all transactions on all accounts the 
user has access to, as well as a summary of the credit usage at the top::

     $ sam-statement

It is more convenient to filter this information so that only specific projects are 
displayed and/or information for a specific period of time, e.g.::

   $ sam-statement -A lp_my_project -s 2023-01-01 -e 2023-01-31

This will show the transactions on the account for the ``lp_my_project`` project for 
the month January 2023.

If you are only interested in the overview of user's transactions, and don't require 
the actual balance information, ``sam-list-usagerecords`` provides a much faster 
alternative for a summarized statement::

   $ sam-list-usagerecords -A lp_my_project -s 2023-01-01 -e 2023-01-31

.. note::

   - It takes quite a while to compute such statements, so **please be patient**
   - The full statements are only visible to the project leaders. 
     Individual users can only see their usage, but not the whole project usage
   - All ``sam``-commands provide help with ``-h`` option
