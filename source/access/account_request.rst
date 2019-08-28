Account request
===============

What is a VSC account?
----------------------

To log on to and use the VSC infrastructure, you need a so-called VSC
account. There is only one exception: Users of the Brussels University
Association who only need access to the VUB/ULB cluster Hydra can use
their institute account.

All VSC-accounts start with the letters \\"vsc\" followed by a
five-digit number. The first digit gives information about your home
institution. There is no relationship with your name, nor is the
information about the link between VSC-accounts and your name publicly
accessible.

Unlike your institute account, VSC accounts don't use regular fixed
passwords but a key pair consisting of a public an private key because
that is a more secure technique for authentication.

Your VSC account is currently managed through your institute account.

Public/private key pairs
------------------------

A key pair consists of a private and a public key. The private key is
stored on the computer(s) from which you want to access the VSC and
always stays there. The public key is stored on a the systems you want
to access, granting access to the anyone who can prove to have access to
the corresponding private key. Therefore it is very important to protect
your private key, as anybody who has access to it can access your VSC
account. For extra security, the private key itself should be encrypted
using a 'passphrase', to prevent anyone from using your private key even
when they manage to copy it. You have to 'unlock' the private key by
typing the passphrase when you use it.

How to generate such a key pair, depends on your operating system. We
describe the generation of key pairs in the client sections for

- :ref:`Linux<generating keys linux>`,
- :ref:`Windows <generating keys windows>` and
- :ref:`macOS<generating keys macos>` (formerly OS X).

Without your key pair, you won't be able to apply for a VSC account.

It is clear from the above that it is very important to protect your
private key well. Therefore:

-  You should not share your key pair with other users.
-  If you have accounts at multiple supercomputer centers (or on other
   systems that use SSH), you should seriously consider using a
   different key pair for each of those accounts. In that way, if a key
   would get compromised, the damage can be controlled.
-  For added security, you may also consider to use a different key pair
   for each computer you use to access your VSC account. If your
   computer is stolen, it is then easy to disable access from that
   computer while you can still access your VSC account from all your
   other computers. The procedure is explained on a separate web
   page ":ref:`access from multiple machines`".

Applying for the account
------------------------

Depending on restrictions imposed by the institution, not all users
might get a VSC account. We describe who can apply for an account in the
sections of the local VSC clusters.

.. _generic access procedure:

Generic procedure for academic researchers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UHasselt has an agreement with KU Leuven to run a shared infrastructure.
Therefore the procedure is the same for both institutions.

Who?

-  Access is available for faculty, students (under faculty
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
-  If there is no course announced please register to our `training
   waiting list`_ and we will organize a new session as soon as we get a few
   people interested in it.

Users of Ghent University Association
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All information about the access policy is available `in
English <https://www.ugent.be/hpc/en/policy>`_ at the `UGent
HPC web pages <https://www.ugent.be/hpc>`_.

-  Researchers can use the :ref:`generic procedure <generic access procedure>`.
-  Master students can also use the infrastructure for their master
   thesis work. The supervisor of the thesis should first send a
   motivation to hpc@ugent.be and then the :ref:`generic
   procedure <generic access procedure>` should be followed (using your
   student UGent id) to request the account.

Users of the Antwerp University Association (AUHA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Who?

-  Access is available for faculty, students (master's projects under
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If you only need access to the VUB cluster Hydra, you don't
   necessarily need a full VSC account but can use your regular
   institute account. More information can be found on `this VUB Web
   Notes
   page <http://www.ulb.ac.be/wserv2_oratio/oratio?f_type=view&f_context=fiches&language=nl&noteid=227>`_.

Troubleshooting
---------------

-  If you can't connect to the `VSC account page`_, some browser
   extensions have caused problems (and in particular some
   security-related extensions), so you might try with browser
   extensions disabled.

.. include:: links.rst
