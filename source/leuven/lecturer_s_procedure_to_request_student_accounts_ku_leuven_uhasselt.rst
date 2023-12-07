.. _lecturer procedure leuven:

Lecturer's procedure to request student accounts (KU Leuven/UHasselt)
=====================================================================

In order to smoothly go through account creation for students process
several actions from the lecturer are required.

#. Submit the request to
   `hpcinfo@.kuleuven.be <mailto:hpcinfo@kuleuven.be?subject=Accounts%20requests%20for%20students%20attending%20the%20course>`_
   providing a short description of the course and explanation why HPC
   facilities are necessary for teaching the course. Please also add the
   attachment with the list of students (including student number, provided by the toledo export)
   1-2 weeks before the beginning of the course.
#. We advise to use :ref:`Open OnDemand <ood_t2_leuven>` service for the student to get access to the login nodes,
   file browser and the job submission. For working with Open OnDemand only, the accounts are provisioned without students being involved in the procedure
   and they login  to the cluster only using KU Leuven MFA.
#. Since introductory credits are supposed to be used for private
   projects (e.g. master thesis computations) we encourage to create
   a specific project, starting with ``p_edu_``, which will be used for computations related to the course.
   We will assign compute credits to this project. It also gives a lecturer an opportunity of tracing the use of
   the cluster during the course. After provisioning the student accounts, we will also add these to the given project.
   For more information about the procedure of creating the project please refer to the page
   :ref:`Slurm accounting <accounting_leuven>`.
   Once the project is accepted, the students from the course list will be added to it.
#. If the reservation of few nodes is necessary during the exercise
   classes please let us know at the latest 1 week before the exercise class, so that
   it can be scheduled. To submit the job during the class the following
   command should be used:

   ::

      $ sbatch --account=<project_name> --reservation=<reservation_name> jobscript.slurm

   where ``project_name`` refers to the project created by the lecturer for
   the purpose of the course, and the ``<reservation_name>`` refers to an 
   existing reservation on the system for the spcific course.


#. In case workflow requires extra access to the cluster with other applications,
   the students will have to :ref:`generate private-public key pair <generic access procedure>`, and add the public key it to their account
   via the `VSC account page`_.
#. If you are not using Open OnDemand, make sure that the software to connect to the cluster (Putty, Xming,
   FileZilla, NX) is available in the PC-class that will be used during the
   course. For KU Leuven courses: please follow the procedure at
   https://icts.kuleuven.be/sc/pcklas/ictspcklassen
   (1 month before the beginning of the course).

