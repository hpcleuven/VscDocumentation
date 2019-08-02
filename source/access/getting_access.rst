Getting access
==============

VSC accounts
------------

In order to use the infrastructure of the VSC, you need a VSC-userid,
also called a VSC account.  Check the `VSC website <eligible users_>`_
for conditions.

All VSC-accounts start with the letters \\"vsc\" followed by a
five-digit number. The first digit gives information about your home
institution. There is no relationship with your name, nor is the
information about the link between VSC-accounts and your name publicly
accessible.

Your VSC account gives you access to most the VSC Tier-2 infrastructure, though
for some more specialised hardware you have to ask access separately.
The rationale is that  we want to ensure that that (usually rather expensive)
hardware is used efficiently for the type of applications it was purchased for.
Contact your :ref:`local VSC coordinator<get in touch_>`_ to arrange access
when required.

For the main Tier-1 compute cluster you need to submit a
`project application <tier-1 project application_>`_ (or you should be
covered by a project application within your research group).


.. _account request:

How to request an accout?
-------------------------

Unlike your institute account, VSC accounts don't use regular fixed
passwords but a key pair consisting of a public an private key because
that is a more secure authentication technique.  To apply for a VSC
account, you need a public/private key pair.

Create a public/private key pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
request.  The following algorithm guides you to the appropriate approach.

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

Everyone else
^^^^^^^^^^^^^

Ask your VSC contact for help.  If you don't have a VSC contact yet, and
`you are eligible to use VSC infrastructure <eligible users_>`_,
please `get in touch`_ with us.


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

.. note::

   If you can't connect to the `VSC account page`_ , some browser
   extensions have caused problems (and in particular some
   security-related extensions), so you might try with browser
   extensions disabled.



Next steps
----------

Register for an HPC Introduction course. These are organized at all universities
on a regular basis.
.. note:

   For KU Leuven users: if there is no course announced please register to our `training
   waiting list`_ and we will organize a new session as soon as we get a few
   people interested in it.

Information on our training program and the schedule is available on the
`VSC website <VSC training_>`_.


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

.. include:: links.rst
