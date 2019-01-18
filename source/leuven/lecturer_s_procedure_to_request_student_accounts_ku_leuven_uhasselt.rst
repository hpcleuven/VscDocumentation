.. _lecturer procedure leuven:

Lecturer's procedure to request student accounts (KU Leuven/UHasselt)
=====================================================================

In order to smoothly go through account creation for students process
several actions from the lecturer are required.

#. Submit the request to
   `hpcinfo@.kuleuven.be <mailto:hpcinfo@kuleuven.be?subject=Accounts%20requests%20for%20students%20attending%20the%20course>`_
   providing a short description of the course and explanation why HPC
   facilities are necessary for teaching the course. Please also add the
   attachment with the list of students attending the course (2 weeks
   before the beginning of the course).
#. Send the information to students that they have 1 week time windowto
   apply for the account (the last day when account creating can be
   processed is the day before the course starts). Students should
   follow the :ref:`generic procedure <generic access procedure>`, that
   starts with
   generating private-public key pair and ends with submitting the
   public key via the `VSC account page`_. After 1 week the
   lists of students that already submitted the request for the account
   and corresponding vsc-account numbers will be send to the lecturer.
#. The students should be informed to bring the private key with them to
   be able to connect and attend the course.
#. Since introductory credits are supposed to be used for private
   projects (e.g. master thesis computations) we encourage to create the
   project which will be used for computations related to the course.
   This will also give a lecturer an opportunity of tracing the use of
   the cluster during the course. For more information about the
   procedure of creating the project please refer to the page
   ":ref:`credit system basics`".
   Once the project is accepted, the students that already applied for
   the account will be automatically added to the project (1 week before
   the beginning of the course).
#. Students that failed to submit request in a given time will have to
   follow regular procedure of applying for the account involving
   communication with the HPC support staff and delaying the account
   creation process (these students will have to motivate the reason of
   applying for the account and send a request for using the project
   credits). Students that submit the requests later than 2 days before
   the beginning of the courseare not guaranteed to get the account in
   time.
#. Both the accounts and the generated key-pairs are strictly PRIVATE
   and students are not supposed to share the accounts, not even for the
   purpose of the course.
#. Please remember to instruct your students to bring the private key to
   the class. Students may forget it and without the key they will not
   be able to login to the cluster even if they have the accounts.
#. If the reservation of few nodes is necessary during the exercise
   classes please let us know 1 week before the exercise class, so that
   it can be scheduled. To submit the job during the class the following
   command should be used:

   ::

      $ qsub -A project-name -W group_list=project-name script-file

   where project-name refers to the project created by the lecturer for
   the purpose of the course.

#. Make sure that the software to connect to the cluster (Putty, Xming,
   FileZilla, NX) is available in pc-class that will be used during the
   course. For KU Leuven courses: please follow the procedure at
   https://icts.kuleuven.be/sc/pcklas/ictspcklassen
   (1 month before the beginning of the course).

.. include:: ../access/links.rst
