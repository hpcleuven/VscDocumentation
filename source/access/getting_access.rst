################################
:fas:`user-check` Getting Access
################################

Once you have a valid :ref:`public/private key pair<create key pair>`, you can
submit an account request.  The following algorithm guides you to the
appropriate approach for each institution.

.. _apply for account:

Applying for your VSC account
=============================

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      UHasselt has an agreement with KU Leuven to run a shared infrastructure.
      Therefore the procedure is the same for both institutions.

      Who?
         Access is available for faculty students (under faculty
         supervision), and researchers of the KU Leuven, UHasselt and their
         associations.

      How?
         Researchers with a regular personnel account (u-number) can use
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

   .. tab-item:: UGent

      All information about the access policy is available `in
      English <https://www.ugent.be/hpc/en/access>`_ at the `UGent
      HPC web pages <https://www.ugent.be/hpc>`_.

      Who?
         Access is available for faculty students (master's projects under
         faculty supervision), and researchers of UGent.

      How?
         Researchers and students can use the :ref:`generic procedure <generic access procedure>`.

   .. tab-item:: UAntwerp (AUHA)

      Who?
         Access is available for faculty students (master's projects under
         faculty supervision), and researchers of the AUHA.

      How?
         Researchers can use the :ref:`generic procedure <generic access procedure>`.

      -  Master students can also use the infrastructure for their master
         thesis work. The promotor of the thesis should first send a
         motivation to hpc@uantwerpen.be and then the :ref:`generic
         procedure <generic access procedure>` should be followed (using your
         student UAntwerpen id) to request the account.

   .. tab-item:: VUB

      All information about the access policy is available on the `VUB
      HPC documentation website <https://hpc.vub.be/docs/access/>`_.

      Who?
         Access is available for faculty students (under faculty
         supervision), and researchers of VUB and their associations.

      How?
         Researchers with a regular VUB account (`@vub.be`) can use
         the :ref:`generic procedure <generic access procedure>`.

      -  Master students can also use the infrastructure for their master
         thesis work. The promotor of the thesis should first send a
         motivation to hpc@vub.be and then the :ref:`generic
         procedure <generic access procedure>` should be followed to request the account.

   .. tab-item:: Others

      Who?
         Check that `you are eligible to use VSC infrastructure <eligible users_>`_.

      How?
         Ask your VSC contact for help.  If you don't have a VSC contact yet, and please
         `get in touch`_ with us.


.. _generic access procedure:

Generic procedure for academic researchers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For most researchers from the Flemish universities, the procedure has
been fully automated and works by using your institute account to
request a VSC account. Check below for exceptions or if the generic
procedure does not work.

#. Open the `VSC account page`_
#. Select your "home" institution from the drop-down menu and click the
   "confirm" button
#. Log in using your institution login and password
#. You will be asked to upload the public key you
   :ref:`created earlier <create key pair>`
#. You will be asked for your scientific domain, please pick one from the
   :ref:`NWO classification <list of scienfic domains>`
#. You will get an e-mail to confirm your application, click the included link
   to do so
#. After the account has been approved by the VSC, your account will be created
   and you will get a confirmation e-mail

.. warning::

   Allow for at least half an hour for your account to be properly created
   after receiving the confirmation email!

.. note::

   If you can't connect to the `VSC account page`_ , some browser
   extensions have caused problems (and in particular some
   security-related extensions), so you might try with browser
   extensions disabled.

.. toctree::
   :hidden:

   scientific_domains
   ../leuven/lecturer_s_procedure_to_request_student_accounts_ku_leuven_uhasselt

Next steps
----------

Register for an HPC Introduction course. These are organized at all universities
on a regular basis.

Information on our training program and the schedule is available on the
`VSC website <VSC training_>`_.

.. note::

   |KUL| If there is no course announced, users of KU Leuven can register to
   the `training waiting list`_ and we will organize a new session as soon as
   we get a few people interested in it.

Additional information
----------------------

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

