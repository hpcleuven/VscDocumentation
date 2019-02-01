.. _desktop access VSC SVN:

Desktop access to a VSC subversion repository
=============================================

Prerequisites
-------------

-  You should be familiar with subversion, either by reading the online
   subversion book, or, for the impatient, the :ref:`documentation page on
   creating and using a subversion repository on the VSC
   clusters <Subversion>`.
-  You should have (access to) a subversion repository on a VSC cluster,
   or any other repository (you should however be able to commit
   changes).
-  A command line client for subversion, which is available all
   operating systems. For Windows, you can use the `Cygwin`_ unix
   emulation layer and the subversion packages included in it.

Environment & general use
-------------------------

All operations introduced in the :ref:`documentation page on using subversion
repositories on the VSC clusters <Subversion>` work as
illustrated therein. The repository's URI can be conveniently assigned
to an environment variable

::

   $ export SVN=\"svn+ssh://userid@vsc.login.node/data/leuven/300/vsc30000/svn-repo\"

where userid should be replaced by your own VSC user ID, and
vsc.login.node to the appropriate login node for the cluster the
repository is on. In the above, it is assumed that the SVN repository
you are going to use is in your VSC data directory (here shown for user
vsc30000) and is called svn-repo. This should be changed appropriately.

Checking out a project from a VSC cluster repository
----------------------------------------------------

To check out the simulation project to a directory 'simulation' on your
desktop, simply type:

::

   $ svn checkout  ${SVN}/simulation/trunk  simulation

The passphrase for your private key used to authenticate on the VSC
cluster will be requested.

Once the project is checked out, you can start editing or adding files
and directories, committing your changes when done.

Importing a local project into the VSC cluster repository
---------------------------------------------------------

Importing a project directory that is currently on your desktop and not
on the VSC cluster is also possible, again by simply modifying the URLs
in the previous section appropriately. Suppose the directory on your
desktop is 'calculation', the steps to take are the following:

::

   $ svn mkdir -m 'calculation: creating dirs' --parents   \\
               $SVN/calculation/trunk    \\
               $SVN/calculation/branches \\
               $SVN/calculation/tags
   $ svn import -m 'calculation: import' \\
                calculation              \\
                $SVN/calculation/trunk

Note that each time you access the repository, you need to authenticate,
which gets tedious pretty soon. Using ssh-agent may be considered to
simplify life, see, e.g., a `short
tutorial <http://novosial.org/openssh/publickey-auth/index.html>`_
on a possible setup.

Links
-----

-  `Apache Subversion <https://subversion.apache.org>`_, with
   documentation, source and binary packages for various operating
   systems.
-  `Cygwin`_ , a UNIX emulation layer
   for Windows. Search for subversion in the list of packages when
   running the setup program.

.. include:: links.rst
