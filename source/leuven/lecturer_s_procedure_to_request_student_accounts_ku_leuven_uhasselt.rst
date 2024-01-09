.. _lecturer procedure leuven:

Lecturer's procedure to request student accounts (KU Leuven/UHasselt)
=====================================================================

We support using HPC for educational purposes, and we fully assist the lecturers
with all aspects of using HPC in the classroom, such as creating studing accounts,
granting credits, resource reservation (if needed), and also live technical support
during the trainings.

In order to make this experience as convenient as possible for the students and the
for the lecturer, it is requested that the lecturer (or any course responsible) would
take the following actions:

#. Submit a request to
   `hpcinfo@.kuleuven.be <mailto:hpcinfo@kuleuven.be?subject=Accounts%20requests%20for%20students%20attending%20the%20course>`_
   1-2 weeks before the beginning of the course.
   Please provide a short description of the course, and explain why the HPC
   facilities are necessary for teaching the course. It is mandatory to provide a list
   of students with their full names, KU Leuven/UHasselt email addresses, and their student number.
   For KU Leuven students, you have to convert the students' q-number to their r-/s-number using the export
   tool on Toledo (Administrations -> Convert user-ids (q-numbers))
#. For all students on the list a VSC-account will be created without any further action required by the student. 
   The students will receive a mail when the account is created. 
   This account wil have no associated ssh-key. If needed the students can create and upload one,
   but for most usage this will be no longer needed.
#. We encourage to create a specific project for the course, with the project name starting with
   ``p_edu_``. We will assign compute credits to this project, and add the students to the account. The
   course lecturer will be the moderator of the project. This gives the lecturer an opportunity
   to track the use of the Tier-2 clusters by individual users during the course.
   For more information about the procedure of requesting the project please refer to the page
   :ref:`Slurm accounting <accounting_leuven>`.
#. We advise to use :ref:`Open OnDemand <ood_t2_leuven>` service for the student to get access to the
   login nodes, file browser and the job submission. The student will only need to use a browser and does not need to install any other software.
   Students will login through the KU Leuven :ref:`Multi Factor Authentication (MFA) <mfa_leuven>`, no additional ssh-agent is required.
#. To ensure that students jobs do not wait in the queue during the hands-on sessions, we offer
   to reserve some limited resources during the session. In that case, please submit your exact
   resource requirements one week before the training, by latest.
   We will communicate the ``<reservation_name>`` with you for every exercise session. 
   To submit the job during the class to the reserved resources, the ``--reservation`` argument
   needs to be used, e.g.:

   ::

      $ sbatch --account=<project_name> --reservation=<reservation_name> jobscript.slurm

   where ``project_name`` refers to the project created by the lecturer for
   the purpose of the course, and the ``<reservation_name>`` refers to an 
   existing reservation on the system for the spcific course.
   The reservation name can also be passed as a parameter in the OpenOnDemand form.


#. In case your workflow requires extra access to the cluster with other applications (such as NX,
   FileZilla, etc.) the students need to :ref:`generate private-public key pair <generic access procedure>`,
   and add the public key it to their VSC account via the `VSC account page`_.
#. If you are not using Open OnDemand, make sure that the software to connect to the cluster
   (Putty, MobaXterm, Xming, FileZilla, NX) is available in the PC-class that will be used during the
   course. For KU Leuven courses, please follow the procedure at
   https://icts.kuleuven.be/sc/pcklas/ictspcklassen (1 month before the beginning of the course).

