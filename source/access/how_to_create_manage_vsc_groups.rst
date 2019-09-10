.. _groups:

How to create/manage VSC groups
===============================

What is a group?
----------------

The concept of group as it is used here is that of a POSIX group and is
a user management concept from the Linux OS (and many other OSes, not
just UNIX-like systems). Groups are a useful concept to control access
to data or programs for groups of users at once, using so-called group
permissions. Three important use cases are:

#. Controlling access to licensed software, e.g., when one or only some
   research groups pay for the license
#. Creating a shared subdirectory to collaborate with several VSC-users
   on a single project
#. Controlling access to a project allocation on clusters implementing a
   credit system (basically all clusters at KU Leuven)

VSC groups are managed without any interaction from the system
administrators. This provides a highly flexible way for users to
organise themselves. Each VSC group has members and moderators:

-  A user can become a member of a group after a moderator approves it.
   As a regular user, you can check all groups you belong to on the `VSC
   account page`_.  -  A moderator can add/delete members *and* moderators

   -  When you create a new group, you become both the first member and
      moderator of that group.

**Warning:** You should not exaggerate in creating new groups. Mounting
file systems over NFS doesn't work properly if you belong to more than
32 different groups, and so far we have not found a solution. This
happens when you log on to a VSC cluster at a different site.

Managing groups
---------------

.. _viewing groups:

Viewing the groups you belong to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Go to the `VSC account page`_.
-  Click on "View groups".

You will in fact see that you always belong to at least two groups
depending on the institution from which you have your VSC account.

.. _join groups:

Join an existing group
~~~~~~~~~~~~~~~~~~~~~~

-  Go to the `VSC account page`_.
-  Click on "New group"
-  Fill in the name of the group

   -  The name of the group will automatically begin with the first
      letter of the hosting institute (a for Antwerp, b for Brussels, g
      for Ghent, l for Leuven)
   -  If the name is wrong, it will treat the request as a new group

-  In the message field, describe who you are to motivate the request,
   so the moderator knows who is making the request

   -  Moderators will deny all unclear requests

.. _create groups:

Create new group
~~~~~~~~~~~~~~~~

-  Go to the `VSC account page`_.
-  Click on "New group"
-  Fill in the group name
-  You will receive a confirmation email
-  After the confirmation, you are now member and moderator of the new
   group

.. _permissions groups:

Working with file and directory permissions
-------------------------------------------

-  The ``chgrp`` (from **change group**) command is used by users on
   Unix-like systems to change the group associated with a computer
   file. General syntax:

   ::

      chgrp [options] group target1 [target2 ..]

-  The ``chmod`` command (abbreviated from **ch**\ ange **mod**\ e) can
   change file system modes of files and directories. The modes include
   permissions and special modes. General syntax:

   ::

      chmod [options] mode[,mode] file1 [file2 ...]

-  Hints:

   -  To view what the permissions currently are, type:

      ::

         $ ls -l file

   -  ``-R``: Changes the modes of directories and files recursively.
   -  Setting the setgid permission on a directory (chmod g+s) causes
      new files and subdirectories created within it to inherit its
      groupID, rather than the primary groupID of the user who created
      the file (the ownerID is never affected, only the groupID). Newly
      created subdirectories inherit the setgid bit. Note that setting
      the setgid permission on a directory only affects the groupID of
      new files and subdirectories created after the setgid bit is set,
      and is not applied to existing entities. Setting the setgid bit on
      existing subdirectories must be done manually, with a command such
      as the following:

      ::

         [user@foo]# find /path/to/directory -type d -exec chmod g+s '{}' \\;

.. include:: links.rst
