###################################
:fas:`user-gear` Account management
###################################

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

Group management
----------------

Once your VSC account is active and you can log on to your home cluster,
you can also manage groups through the account management web interface.
Groups (a Linux/UNIX concept) are used to control access to licensed
software (e.g., software licenses paid for by one or more research
groups), to create subdirectories where researchers working on the same
project can collaborate and control access to those files, and to
control access to project credits on clusters that use these (all
clusters at KU Leuven).

.. toctree::
   :maxdepth: 2

   how_to_create_manage_vsc_groups

.. _virtual_organization:

Virtual Organization management
-------------------------------

For UGent and VUB users only: You can create or join a so-called Virtual
Organization or VO, which gives access to extra storage in the HPC cluster that
is shared between the members of the VO. VUB users may consult the VUB-HPC docs
on `Virtual Organization <https://hpc.vub.be/docs/vo/>`_ for more info.

Managing disk space
-------------------

The amount of disk space that a user can use on the various file systems
on the system is limited by quota on the amount of disk space and number
of files. UGent and VUB users can see and request upgrades for their quota on
the Account management site (Users need to be in a VO (Virtual
Organization) to request additional quota. Creating and joining a VO is
also done through the Account Management website). On other sites
checking your disk space use is still :ref:`mostly done from the command
line <disk usage>` and requesting more quota is done via email.

