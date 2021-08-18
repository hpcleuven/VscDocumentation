Account management
==================

Account management at the VSC is mostly done through the `VSC account page`_
using your institute account rather than your VSC account.

Managing user credentials
-------------------------

-  You use the VSC account page to request your account as explained on
   the ":ref:`account request`" page. You'll also need to
   create an SSH-key which is also explained on those pages.
-  Once your account is active and you can log on to your home cluster,
   you can use the account management pages for many other operations:

   -  If you want to :ref:`access the VSC clusters from more than one
      computer <access from multiple machines>`,
      it is good practice to use a different key for each computer. You
      can upload additional keys via the account management page. In
      that way, if your computer is stolen, all you need to do is remove
      the key for that computer and your account is safe again.
   -  If you've :ref:`messed up your keys <messed up keys>`,
      you can restore the keys on the cluster or upload a new key and
      then delete the old one.

Group and Virtual Organization management
-----------------------------------------

Once your VSC account is active and you can log on to your home cluster,
you can also manage groups through the account management web interface.
Groups (a Linux/UNIX concept) are used to control access to licensed
software (e.g., software licenses paid for by one or more research
groups), to create subdirectories where researchers working on the same
project can collaborate and control access to those files, and to
control access to project credits on clusters that use these (all
clusters at KU Leuven).

-  All details are on the page ":ref:`groups`".
   In particular, you'll find how to

   -  :ref:`view the groups you belong to <viewing groups>`.
   -  :ref:`request membership to a group <join groups>`
      you feel you should belong to. It is then up to the moderator of
      that group to grant you membership.
   -  :ref:`create a new group <create groups>`
   -  use group permissions to :ref:`control access to files and
      directories <permissions groups>`

-  If you are a group moderator, you can manage your group by accepting
   requests from users that would like to join the group or inviting
   users to join your group through the `VSC account page`_.
-  For UGent users only: You can create or join a so-called Virtual
   Organization or VO.

Managing disk space
-------------------

The amount of disk space that a user can use on the various file systems
on the system is limited by quota on the amount of disk space and number
of files. UGent users can see and request upgrades for their quota on
the Account management site (Users need to be in a VO (Virtual
Organization) to request additional quota. Creating and joining a VO is
also done through the Account Management website). On other sites
checking your disk space use is still :ref:`mostly done from the command
line <disk usage>` and requesting more quote is done via email.

.. include:: links.rst
