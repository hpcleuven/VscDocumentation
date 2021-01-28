.. _user_access:

User Access to iRODS
====================

The Tier-1 Data Service is currently on the pilot phase, so access to the system is strictly by invitation. If you have a use case that combines data and computing workflows and you are interested on testing the Tier-1 Data service you can contact us to discuss a possible collaboration by e-mail at the address: data@vscentrum.be

To be able to log on and to use Tier-1 Data platform, you need to have an active vsc-account and an approved Tier-1 Data project. During the pilot phase Tier-1 Data projects are granted by invitation only. 

Users can connect to the iRODS platform by using different clients (command line, WebDAV interface or a portal) both from the VSC HPC systems (login and compute nodes) and from external systems (i.e: their laptops).

Before you can interact with iRODS, as a VSC user you will need to activate the service executing one of the following commands;

- After you have reached the Tier-1 to work on, you should use:

::

    $ irods-setup | bash

or,

::

    $ ssh irods.hpc.kuleuven.be | bash 

- If you are connecting from a Tier-2 login node, you should then execute:

::

    $ irods-setup | bash

or,

::

    $ ssh irods.tier1.leuven.vsc | bash

**Note**: As you have seen, `irods-setup | bash` command can work both in Tier-1 and Tier-2 login nodes. Besides, to avaoid pseudo-terminal warnings it is recommended to use the same command in compute nodes, meaning in batch scripts once required.

These commands will activate a temporary token for a period of 7 days. After the 7 days have passed you will need to reactivate your access by re-executing one of these commands again.

Once logged in iRODS users will have access to the following iRODS collections:

- Your personal area: /kuleuven_tier1_pilot/home/vscXXXXX (where XXXXX is the number of your vsc-account). This are is by default only visible by your user.

- Your group area: /kuleuven_tier1_pilot/home/lt1_projectcode. The area is shared and visible by all the members of your group.

- The public area: /kuleuven_tier1_pilot/home/public. This is an area accessible by everyone in the system.  I could be even accessed by anonymous users from external sources if this is configured. You should not copy on this area any confidential or private data.
