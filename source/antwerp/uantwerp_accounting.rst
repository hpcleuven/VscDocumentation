.. _UAntwerp accounting:

###################
UAntwerp Accounting
###################

Since 1 March 2024, there is accounting for both compute (jobs) and storage (files).
You will need to select a project account when submitting jobs to the CalcUA clusters.
If you do not have access to any project account, please ask your supervisor to give you access.

.. seealso::
  the infosession `Accounting @ CalcUA <https://www.uantwerpen.be/en/research-facilities/calcua/support/accounting/>`__

Project accounts
================

Project accounts are mandatory when submitting jobs. You may have access to different project accounts, 
so it is important to use the appropriate account for every job you submit. You can get a list of 
valid project accounts you are a member of using the ``myprojectaccounts`` command.

To get access to an existing project account, the account moderator (typically your supervisor) has to invite you.
They have to:

*  Log in to the `VSC account page`_
*  Select "Edit Groups"
*  Enter the name of the ``ap_`` group, and click "Edit"
*  Invite users by adding them in the "Invited members" area 
*  Click "Update" for the changes to take effect 

Creating a new project account
------------------------------

If you would like to create a new project account, you need to request it via hpc@uantwerpen.be.
No budget code is needed for creating the project account, only a name for you to identify the project. 
Every project account starts with ``ap_`` and includes the name of the research group, followed by the 
project/supervisor/course name code, for example: ``ap_medchem``, ``ap_tsm2_wh``, ``ap_course_2400wetcmp``, ... .
Invoices will be sent yearly.

Shared group folders
--------------------

To facilitate collaboration between VSC users, there is the possibility of shared group directories.
If you would like to use a shared group folder, the moderator of the project account can request one
via hpc@uantwerpen.be. This can be both in scratch: ``/scratch/antwerpen/grp`` or data: ``/data/antwerpen/grp``.

Please make your own arrangements with the group members regarding the structure and organisation of 
the directory. Note that it is not possible to check the usage of individual members in the shared folder, 
due to limitaitions in user/group ownership of files and directories.

Associated costs
================

.. seealso::
  Only a tiny fraction of the operational costs (hardware, support contracts, infrastructure, ...) are 
  billed to the users. 

  Pricing details can be found in the `slides of the Accounting @ CalcUA infosession 
  (requires UAntwerp login) <https://pintra.uantwerpen.be/bbcswebdav/xid-1120010_1>`_.

Jobs
----

The cost associated to jobs will be based on the resources *used*, not those requested for the job. 
So the actual runtime is taken into account, not the requested wall time. The costs are calculated by 
core-hour. Jobs that use a lot of memory (or GPU's or other options that make the cores unavailable 
to other users) will be assigned more cores accordingly. You can monitor your usage with the ``myaccounting`` 
command (option ``-A`` for the entire project account):

.. code-block :: bash

   $ myaccounting -S YYYY-MM-DD [-A <ap_project>]

Storage
-------

The default storage quota are free. You can request extra quota, and similarly to jobs, the cost is calculated 
by your actual use. Quota requests are still reviewed, despite being paid for, as tons of small files on the 
shared scratch system impact the performance for all users. 

Your storage usage is calculated each month (by the maximum daily use during that month) at 1/12th of the yearly price.
You can monitor your current storage usage with the ``myquota`` command (option ``-g`` for the shared group folders):

.. code-block :: bash

   $ myquota [-g <ap_project>]

Exceptions
----------

Some exceptions are applied:

-  Ba/Ma students get a limited free budget, with usage restricted to the Ba/Ma thesis of this student.
-  Course participants are allowed free usage during the course, though restrictions can apply.
-  Failed jobs due to hardware failure will not be accounted for. 
-  Software testing *in coordination with the support team* will not be accounted for.

