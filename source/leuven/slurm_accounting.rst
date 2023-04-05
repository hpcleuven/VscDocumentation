.. _accounting_leuven:
========================
Slurm Accounting
========================

To run jobs on :ref:`Genius <genius_t2_leuven>` and :ref:`wICE <wice_t2_leuven>` 
clusters, you will need a valid Slurm credit account with sufficient credits. 
To make it easier to e.g. see your current credit balance and past credit usage,
we have developed a set of ``sam-*`` tools (``sam-balance``, ``sam-list-usagerecords``,
``sam-list-allocations`` and ``sam-statement``).

The accounting system is somewhat similar to a regular bank.
A research group typically has one or more credit accounts, for instance a separate 
credit account for each project.
When credits are purchased, they are depositied in a credit account.
All users that are a member of such a credit account can withdraw credits from it 
by running jobs.
A users can also request introduction credits, in that case a credit account will 
be opened specifically for this user with a limited amount of free credits.
Hence, it is possible for users to have access to multiple credit accounts.

In this page, the technical aspects of accounting and some relevant commands are explained.


Checking an account balance
---------------------------

It is a good practice to check the balance of your credit project(s) from time to time.
This can be done by executing the following command on any KU Leuven Tier-2 node::

   $ sam-balance

This will show the balance of each credit account the user has access to.


Running jobs: accounting workflow
---------------------------------

For every job that gets submitted, the name of a credit account needs to be specified.
If you for example have been granted introduction credits, the corresponding credit
account will be named ``intro_vscxxxxx`` (with ``vscxxxxx`` referring to your VSC username).
Submitting a batch job can then look as follows::

   $ sbatch -A lp_my_project run-job.slurm
   or
   $ sbatch -A intro_vsc3xxxx run-job.slurm

If the account to be charged, i.e., ``lp_my_project``, has insufficient credits for the 
job, the user receives a warning at this point, and the job will not start until the account
is topped up with sufficient credits.

Obtaining an overview of transactions
-------------------------------------

A bank provides an overview of the financial transactions on your accounts under the 
form of statements. 
Similarly, the job accounting system provides statements that give the user an overview 
of the cost of each individual job. 
The following command will provide an overview of all transactions on all accounts
that the user has access to, as well as a summary of the credit usage at the top::

     $ sam-statement -u <vsc-account>

It is more convenient to filter this information so that only specific projects are 
displayed and/or information for a specific period of time, e.g.::

   $ sam-statement -A lp_my_project -s 2023-01-01 -e 2023-01-31

This will show the transactions on the account for the ``lp_my_project`` project for 
the month January 2023.

If you are only interested in the overview of your past credit usage, and don't require 
the actual balance information, ``sam-list-usagerecords`` provides a much faster 
alternative for a summarized statement::

   $ sam-list-usagerecords -A lp_my_project -s 2023-01-01 -e 2023-01-31

.. note::

   - It takes quite a while to compute such statements, so **please be patient**
   - The full statements are only visible to the project leaders. 
     Individual users can only see their own usage and not that of other users of 
     the same credit account.
     The latter is only available to users who have been given a Coordinator role.
   - All ``sam``-commands provide help by running them with ``-h`` option
