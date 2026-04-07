##########################################
:fas:`person-chalkboard` HPC for education
##########################################

.. _hpc for education:

|KUL| We support using HPC for educational purposes, such as in the classroom or
for hackathons. We assist the lecturers with all aspects of using HPC in the classroom,
such as:
* creating student accounts
* granting compute credits
* providing storage
* reserving compute resources
* technical support during the trainings (either on-site or remote)

Practical steps
===============

In order to make this experience as convenient as possible for the students and the
for the lecturer, we ask that the lecturer (or any of the course coordinators)
takes the following actions:

#. Submit a request to
   `hpcinfo@.kuleuven.be <mailto:hpcinfo@kuleuven.be?subject=Accounts%20requests%20for%20students%20attending%20the%20course>`_
   at least 2 weeks before the course needs the HPC resources.
   Please provide a short description of the course, and explain why the HPC
   facilities are necessary for teaching the course. It is mandatory to provide a list
   of students with their full names, KU Leuven/UHasselt email addresses, and their student number.
   For KU Leuven an export from the participants in Toledo is sufficient.
#. For all students on the list a VSC account will be created.
   No further action will be required by the students. 
   The students will receive a mail when the account is created. 
#. We encourage to create a :ref:`specific VSC group <groups>` for the course, with a name starting 
   with ``p_edu_``. We call it the ``project_name`` and assign compute credits to this project.
   The students will be added to this project, allowing them to submit compute jobs. 
   The course lecturer will be the moderator of the project. This gives the lecturer an opportunity
   to track the use of the Tier-2 clusters by individual users during the course, and add/remove students
   as needed.
   For more information about the procedure of requesting the project please refer to the
   :ref:`Slurm accounting <accounting_leuven>` page.
#. Throughout your course, we recommend to use the :ref:`Open OnDemand portal <ood>`. The students will only
   need a web browser and will normally not need to install any other software.
#. To ensure that students jobs do not wait in the queue during the hands-on sessions, we offer
   to reserve some limited resources during the session. In that case, please submit your exact
   resource requirements one week before the training, at the latest.
   We will communicate the ``<reservation_name>`` with you for every exercise session.
   To start and OnDemand session on a reserved node, please specify the ``<reservation_name>`` in the 
   'Reservation' text field of the desired app.
   To let batch jobs use the reserved resources, the ``--reservation`` argument needs to be applied, e.g.:

   ::

      $ sbatch --account=<project_name> --reservation=<reservation_name> jobscript.slurm

   where ``project_name`` refers to the project credit assigned to your training.

#. If you are not using Open OnDemand, make sure that the software to connect to the cluster
   (Putty, MobaXterm, Xming, FileZilla) is available in the PC class that will be used during the
   course. For KU Leuven courses, please follow the procedure at
   https://icts.kuleuven.be/sc/pcklas/ictspcklassen (1 month before the beginning of the course).