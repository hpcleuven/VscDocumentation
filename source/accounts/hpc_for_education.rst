##########################################
:fas:`person-chalkboard` HPC for education
##########################################

HPC as an educational asset
---------------------------

|KUL| We support using HPC for educational purposes, such as in the classroom or
for hackathons. We assist the lecturers with all aspects of using HPC in the classroom,
such as creating student accounts, granting credits, providing storage, resource reservation 
(if needed), and also in-situ technical support during the trainings, where applicable.

Practical steps
===============

In order to make this experience as convenient as possible for the students and the
for the lecturer, it is requested that the lecturer (or any course responsible) would
take the following actions:

#. Submit a request to
   `hpcinfo@.kuleuven.be <mailto:hpcinfo@kuleuven.be?subject=Accounts%20requests%20for%20students%20attending%20the%20course>`_
   at least 2 weeks before the course needs to make use of the HPC resources.
   Please provide a short description of the course, and explain why the HPC
   facilities are necessary for teaching the course. It is mandatory to provide a list
   of students with their full names, KU Leuven/UHasselt email addresses, and their student number.
   For KU Leuven an export from the participants in Toledo is sufficient.
#. For all students on the list a VSC-account will be created without any further action required by the student. 
   The students will receive a mail when the account is created. 
#. We encourage to create a :ref:`specific VSC group <groups>` for the course, with the name starting 
   with ``p_edu_``. We will assign compute credits to this project, and add the students to the account.
   The course lecturer will be the moderator of the project. This gives the lecturer an opportunity
   to track the use of the Tier-2 clusters by individual users during the course, and add/remove students
   as needed.
   For more information about the procedure of requesting the project please refer to the
   :ref:`Slurm accounting <accounting_leuven>` page.
#. Throughout your course, we recommend to use the :ref:`Open OnDemand portal <ood>`. The students will only
   need to use a web browser and do not need to install any other software.
#. To ensure that students jobs do not wait in the queue during the hands-on sessions, we offer
   to reserve some limited resources during the session. In that case, please submit your exact
   resource requirements one week before the training, by latest.
   We will communicate the ``<reservation_name>`` with you for every exercise session.
   To start and OnDemand session on a reserved node, please specify the ``<reservation_name>`` in the 
   'Reservation' text field of the desired app.
   To submit batch jobs using reserved resources, the ``--reservation`` argument needs to be used, e.g.:

   ::

      $ sbatch --account=<project_name> --reservation=<reservation_name> jobscript.slurm

   where ``project_name`` refers to the project credit assigned to your training.

#. If you are not using Open OnDemand, make sure that the software to connect to the cluster
   (Putty, MobaXterm, Xming, FileZilla) is available in the PC-class that will be used during the
   course. For KU Leuven courses, please follow the procedure at
   https://icts.kuleuven.be/sc/pcklas/ictspcklassen (1 month before the beginning of the course).