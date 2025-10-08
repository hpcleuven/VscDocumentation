.. _UAntwerp accounting:

###################
UAntwerp accounting
###################

Since 1 March 2024, there is accounting for both compute (jobs) and storage (files).
You will need to select a project account when submitting jobs to the CalcUA clusters.
If you do not have access to any project account, please ask your supervisor to give you access.

.. seealso::
 TODO calcUA (login)

Project accounts
================
Project accounts are mandatory when submitting jobs. You may belong to different project accounts, 
so it is important to use the appropriote account for every job you submit. You can get a list of 
valid project accounts you are a member of using the ``myprojectaccounts`` command.

To get access to an existing project account, the account moderator (typically your supervisor) has to invite you.
They have to:

*  Log in to the VSC account page TODO
*  Select 'Edit Groups'
*  Enter the name of the ``ap_`` group, and click 'Edit'
*  Invite users by adding them in the “Invited members” area 
*  Click 'Update' for the changes to take effect 

If you would like to create a new project account, you need to request it via hpc@uantwerpen.be.
No budget code is needed for creating the project account, only a name for you to identify the project. 
Every project account starts with ``ap_`` and includes the name of the research group, followed by the 
project/supervisor/course name code, for example: ``ap_medchem``, ``ap_tsm2_wh``, ``ap_course_2400wetcmp``, ... 

TODO invoices will be sent yearly?
? moderators add users? or users request access?


shared group folders -> vreate VSC group (account page) then request us to create shared group folder in: /data/antwerpen/grp or /scratch/antwerpen/grp
-> make own arrangements regarding structure and organisation of dirs
?-> all files in group folder are owned by group? cant check individual users usage

Cost
====

.. seealso::
  pricing details link CalcUA (login) TODO 
  fraction of the cost

The cost associated to **jobs** will be based on the resources *used*, not those requested for the job. 
So the actual runtime is taken into account, not the requested wall time. The costs are calculated by 
core-hour. Jobs that use a lot of memory (or GPU's or other options that make the cores unavailable 
to other users) will be assigned more cores accordingly. You can monitor your usage with the ``myaccounting`` command:

.. code-block :: bash

   $ myaccounting -S YYYY-MM-DD -A <ap_project>

The default **storage** quota are free. You can request extra quota, and similarly to jobs, the cost is calculated 
by your actual use. Quota requests are still reviewed, despite being paid for, as tons of small files on the 
shared scratch system impact the performance for all users. 

TODO
?per month
?monitoring

Some exceptions are applied:

-  Ba/Ma students get a limited free budget, with usage restricted to the Ba/Ma thesis of this student.
-  Course participants are allowed free usage during the course, though restrictions can apply.
-  Failed jobs due to hardware failure will not be accounted for. 
-  Software testing *in coordination with the support team* will not be accounted for.

