.. _groups:

How to create/manage VSC groups
===============================


.. _vsc_groups:

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
      the moderator of that group.

.. warning::

   You should not exaggerate in creating new groups. Mounting
   file systems over NFS doesn't work properly if you belong to more than
   32 different groups, and so far we have not found a solution. This
   happens when you log on to a VSC cluster at a different site.

Managing groups
---------------

.. _viewing groups:

Viewing the groups you belong to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Go to the `VSC account page`_.
-  Click on the 'View Groups' tab.

You will in fact see that you always belong to at least two groups
depending on the institution from which you have your VSC account.

.. _join groups:

Join an existing group
~~~~~~~~~~~~~~~~~~~~~~

-  Go to the `VSC account page`_.
-  Click on the 'New/Join Group' tab.
-  Under the 'Join group' section, fill in the name of the group.
   The name of the group will automatically begin with the first
   letter of the hosting institute (a for Antwerp, b for Brussels, g
   for Ghent, l for Leuven).
-  In the message field, describe who you are to motivate the request,
   so the moderator knows who is making the request. Moderators will
   deny all unclear requests.

.. _create groups:

Create new group
~~~~~~~~~~~~~~~~

-  Go to the `VSC account page`_.
-  Click on the 'New/Join Group' tab.
-  Fill in the group name.
-  You will automatically become a member and moderator of the new group within an hour.
-  Once you are a group moderator, you can manage your group by accepting
   requests from users that would like to join the group or inviting
   users to join your group through the `VSC account page`_.

.. _permissions groups:

Working with file and directory permissions
-------------------------------------------

-  The ``chgrp`` (from **change group**) command is used by users on
   Unix-like systems to change the group associated with a computer
   file. General syntax:

   ::

      chgrp [options] group target1 [target2 ...]

-  The ``chmod`` command (abbreviated from **ch**\ ange **mod**\ e) can
   change file system modes of files and directories. The modes include
   permissions and special modes. General syntax:

   ::

      chmod [options] mode[,mode] file1 [file2 ...]

-  Hints:

   -  To view what the permissions currently are, type:

      ::

         ls -l file

   -  ``-R``: Changes the modes of directories and files recursively.
   -  Setting the setgid permission on a directory (``chmod g+s``) causes
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

         find /path/to/directory -type d -exec chmod g+s '{}' \\;


.. _sharing_via_vsc_groups:

Sharing files and folders with other VSC users
----------------------------------------------

VSC users can share files/folders with other VSC users via `VSC groups <vsc_groups>`.
This applies to any file and folder stored in the `VSC storage locations <data location>`.
However, we discourage using your home directory for such purposes.

Imagine a VSC user who wants to share his post-processed data stored below the
``$VSC_DATA/collab/post-processed`` folder with another VSC user(s).
Then, these are the steps to take:

- Create a `new VSC group <create groups>` (if existing groups do not serve your purpose).
  Let's call this new group ``lp_shared_data``.
- Invite your VSC collaborators to join the group ``lp_shared_data``.
- Change the group name of the folders in the hierarchy one by one to ``lp_shared_data``:

  ::

     chgrp lp_shared_data $VSC_DATA
     chgrp lp_shared_data $VSC_DATA/collab
     # change group name recursively below the top hierarchy you want to share
     chgrp -R lp_shared_data $VSC_DATA/collab/post-processed

- Make sure that the shared directories in this hirarchy have read ``r`` and execute ``x`` 
  access bits recursively, and at least read access for all files:

  ::

     chmod -R g+r $VSC_DATA/collab/post-processed
     chmod g+x $VSC_DATA
     chmod g+x $VSC_DATA/collab
     find $VSC_DATA/collab/post-processed -type d -exec chmod g+x {} +

- Depending on the internal agreement within the collaborating team, you may choose to additionally
  allow the group members to add/remove files to/from the shared hierarchy. If so, the group
  members are expected to be careful specifically in removing files. In that case:

  ::

     chmod -R g+w $VSC_DATA/collab/post-processed

- If the collaborators are expected to overwrite the existing files and/or add new files/folders
  inside the shared hierarchy, you can also set the setgid bit mentioned above on the ``post-processed``
  folder:

  ::

     chmod -R g+s $VSC_DATA/collab/post-processed

  This has the added value that your new files and folders will also inherit the group name from
  the parent directory.

- When communicating the path to the shared data with your collaborators, make sure you provide the
  full path where environment variables such as ``$VSC_DATA`` are expanded to their values, such as
  ``/data/leuven/3xx/vsc3xxxx``.
