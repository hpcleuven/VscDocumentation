Getting access
==============

The VSC account
---------------

In order to use the infrastructure of the VSC, you need a VSC-userid,
also called a VSC account.

All VSC-accounts start with the letters \\"vsc\" followed by a
five-digit number. The first digit gives information about your home
institution. There is no relationship with your name, nor is the
information about the link between VSC-accounts and your name publicly
accessible.


What can you access?
--------------------

Your VSC account gives you access to the VSC Tier-2 infrastructure, though
for some more specialised hardware you have to ask access separately, typically
to the coordinator of your institution, because we want to be sure that that
(usually rather expensive) hardware is used efficiently for the type of
applications it was purchased for.

You have disk space on the storage infrastructure that is accessible from
all VSC infrastructure.

For the main Tier-1 compute cluster you need to submit a project application
(or you should be covered by a project application within your research group).


Who can get a VSC account?
--------------------------

Researchers at the Flemish university associations
   In many cases, this is done through a fully automated application process,
   but in some cases you must submit a request to your local support
   team.
Master students in the framework of their master thesis
   If supercomputing is needed for the thesis. For this, you will first
   need the approval of your supervisor. The details about the procedure
   can again be found below.
Use in courses at the University of Leuven and Hasselt University
   Lecturers can also use the local Tier-2 infrastructure in the
   context of some courses (when the software cannot run in the PC
   classes or the computers in those classes are not powerful enough).
   It is important that the application is submitted on
   time, at least two weeks before the start of the computer sessions.
Researchers from iMinds and VIB
   The application is made through
   your host university. The same applies to researchers at the
   university hospitals and research institutes under the direction or
   supervision of a university or a university college, such as the
   special university institutes mentioned in Article 169quater of the
   Decree of 12 June 1991 concerning universities in the Flemish
   Community.
Researchers at other Flemish public research institutions
   You can get compute on the Tier-1 infrastructure through a project
   application or access the Tier-2 infrastructure through contact with
   one of the coordinators.
Businesses, non-Flemish public knowledge institutions and not-for-profit organisations
   These entities can buy compute time on the
   infrastructure. The procedures are explained on the page
   ":ref`buying compute time`".


.. _account request
How to request access?
----------------------

Unlike your institute account, VSC accounts don't use regular fixed
passwords but a key pair consisting of a public an private key because
that is a more secure authentication technique.  To apply for a VSC
account, you need a public/private key pair.

Public/private key pairs
~~~~~~~~~~~~~~~~~~~~~~~~

A key pair consists of a private and a public key.

#. The private key is stored on the computer(s) you use to access the VSC
   infrastructure and always stays there.
#. The public key is stored on the  VSC systems you want to access, allowing
   to prove your identity through the corresponding private key.
  
How to generate such a key pair depends on your operating system. We
describe the generation of key pairs in the client sections for

- :ref:`Linux<generating keys linux>`,
- :ref:`Windows <generating keys windows>` and
- :ref:`macOS<generating keys macos>` (formerly OS X).

Without a key pair, you won't be able to apply for a VSC account.

.. warning::

   It is clear from the above that it is very important to protect your
   private key well. Therefore:
   
   - You should choose a strong passphrase to protect your private key.
   - You should not share your key pair with other users.
   - If you have accounts at multiple supercomputer centres (or on other
     systems that use SSH), you should seriously consider using a
     different key pair for each of those accounts. In that way, if a key
     would get compromised, the damage can be controlled.
   - For added security, you may also consider to use a different key pair
     for each computer you use to access your VSC account. If your
     computer is stolen, it is then easy to disable access from that
     computer while you can still access your VSC account from all your
     other computers. The procedure is explained on a separate web
     page ":ref:`access from multiple machines`".

Your VSC account is currently managed through your institute account.


Applying for the account
~~~~~~~~~~~~~~~~~~~~~~~~

Once you have a valid public/private key pair, you can submit an account
request.

For staff memebers and students of the universities and their
associations, this can be d

.. _generic access procedure:
Generic procedure for academic researchers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For most researchers from the Flemish universities, the procedure has
been fully automated and works by using your institute account to
request a VSC account. Check below for exceptions or if the generic
procedure does not work.

Open the `VSC account page`_ and select your "home" institution. After
you log in using your institution login and password, you will be asked
to upload your public key. You will get an e-mail to confirm your application.
After the account has been approved by the VSC, your account will be created
and you will get a confirmation e-mail.

Users from the KU Leuven and UHasselt association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

UHasselt has an agreement with KU Leuven to run a shared infrastructure.
Therefore the procedure is the same for both institutions.

Who?

   Access is available for faculty, students (under faculty
   supervision), and researchers of the KU Leuven, UHasselt and their
   associations.

How?

   -  Researchers with a regular personnel account (u-number) can use
      the :ref:`generic procedure <generic access procedure>`.
   -  If you are in one of the higher education institutions associated
      with KU Leuven, the :ref:`generic procedure <generic access procedure>`
      may not work. In that case, please e-mail hpcinfo@kuleuven.be
      to get an account. You will have to provide a public ssh key generated
      as described above.
   -  Lecturers of KU Leuven and UHasselt that need HPC access for giving
      their courses: The procedure requires action both from the lecturers
      and from the students. Lecturers should follow the :ref:`specific
      procedure for lecturers <lecturer procedure leuven>`,
      while the students should simply apply for the account through the
      :ref:`generic procedure <generic access procedure>`.

How to start?

   -  Please follow the information on the documentation site,
   -  or register for the HPC Introduction course.
   -  If there is no course announced please register to ojjjjur `training
      waiting list`_ and we will organize a new session as soon as we get a few
      people interested in it.

Users of Ghent University Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All information about the access policy is available `in
English <https://www.ugent.be/hpc/en/policy>`_ at the `UGent
HPC web pages <https://www.ugent.be/hpc>`_.

-  Researchers can use the :ref:`generic procedure <generic access procedure>`.
-  Master students can also use the infrastructure for their master
   thesis work. The promotor of the thesis should first send a
   motivation to hpc@ugent.be and then the :ref:`generic
   procedure <generic access procedure>` should be followed (using your
   student UGent id) to request the account.

Users of the Antwerp University Association (AUHA)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Who?

   Access ia available for faculty, students (master's projects under
   faculty supervision), and researchers of the AUHA.

How?

-  Researchers of the University of Antwerp with a regular UAntwerpen
   account can use the :ref:`generic procedure <generic access procedure>`.
-  Users from higher education institutions associated with UAntwerpen
   can get a VSC account via UAntwerpen. However, we have not yet set up
   an automated form. Please contact the user support at
   `hpc@uantwerpen.be <mailto:hpc@uantwerpen.be?subject=Account%20request>`_
   to get an account. You will have to provide a public ssh key
   generated as described above.

Users of Brussels University Association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you only need access to the VUB cluster Hydra, you don't
necessarily need a full VSC account but can use your regular
institute account. More information can be found on `this VUB Web
Notes
page <http://www.ulb.ac.be/wserv2_oratio/oratio?f_type=view&f_context=fiches&language=nl&noteid=227>`_.

Troubleshooting
~~~~~~~~~~~~~~~

If you can't connect to the `VSC account page`_, some browser
extensions have caused problems (and in particular some
security-related extensions), so you might try with browser
extensions disabled.


Additional information
----------------------

Before you apply for VSC account, it is useful to first check whether
the infrastructure is suitable for your application. Windows or OS X
programs for instance cannot run on our infrastructure as we use the
Linux operating system on the clusters. The infrastructure also should
not be used to run applications for which the compute power of a good
laptop is sufficient. The pages on the :ref:`tier1 hardware` and
:ref:`tier2 hardware`
in this part of the website give a high-level description of our
infrastructure. You can find more detailed information in the user
documentation on the user portal. When in doubt, you can also contact
your local support team. This does not require a VSC account.

Furthermore, it can also be useful to take one of the introductory
courses that we organise periodically at all universities. However, it
is best to apply for your VSC account before the course since you also
can then also do the exercises during the course. We strongly urge
people who are not familiar with the use of a Linux supercomputer to
take such a course. After all, we do not have enough staff to help
everyone individually for all those generic issues.

There is an exception to the rule that you need a VSC account to access
the VSC systems: Users with a valid VUB account can access the Tier-2
systems at the VUB.

Your account also includes two “blocks” of disk space: your home
directory and data directory. Both are accessible from all VSC clusters.
When you log in to a particular cluster, you will also be assigned one
or more blocks of temporary disk space, called scratch directories.
Which directory should be used for which type of data, is explained in
the page ":ref:`data location`".

Your VSC account does not give you access to all available software. You
can use all free software and a number of compilers and other
development tools. For most commercial software, you must first prove
that you have a valid license or the person who has paid the license on
the cluster must allow you to use the license. For this you can contact
your local support team.
