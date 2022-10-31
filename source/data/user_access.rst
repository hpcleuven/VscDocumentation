.. _user_access:

User Access to iRODS
====================

The Tier-1 Data Service at KU Leuven is currently in a pilot phase, so access to the system is strictly by invitation. If you have a use case that combines data and computing workflows and you are interested on testing the Tier-1 Data service you can contact us to discuss a possible collaboration by e-mail at the address: data@vscentrum.be

To be able to log on and to use the Tier-1 Data platform, you need to have an active vsc-account and an approved Tier-1 Data project. During the pilot phase Tier-1 Data projects are granted by invitation only. 

Users can connect to the iRODS platform by using different clients (command line, WebDAV interface or web application) both from the VSC HPC systems (login and compute nodes) and from external systems (i.e: user's laptops).

Before you can interact with iRODS, as a VSC user you will need to activate the service executing one of the following commands;

- If you are logged in to the login nodes of Tier-1 or Tier-2 clusters of KU Leuven, you should use:

::

    $ irods-setup | bash

- If you want to connect from any login nodes of other universities' HPC cluster, you should execute:

::

    $ ssh login.hpc.kuleuven.be irods-setup | bash

In any case, any attempt to login to the Tier-1 or Tier-2 HPC clusters at KU Leuven will invite you to open the HPC Firewall url, which in turn forwards to your institutional login page. Therefore, please note that you can't login to iRODS in an automated fashion. More information can be found on the `HPC Firewall page <https://firewall.vscentrum.be/>`__.

These commands will activate a temporary token for a period of 7 days. After the 7 days have passed you will need to reactivate your access by re-executing one of these commands again.

The Tier-1 Data service has the following landing page: https://irods.hpc.kuleuven.be/. This provides the entrypoint to start working with iCommands, the Python iRODS client and the WebDAV client.

It is also possible to launch iCommands directly from your local Linux (either native or via a VM or the Windows Subsystem for Linux) computer against the Tier-1 iRODS zone. For this you need to install iCommands and execute the snippet under 'iCommands Client on Linux' from the landing page.

Once logged in iRODS users will have access to the following iRODS collections:

- Your personal area: /kuleuven_tier1_pilot/home/vscXXXXX (where XXXXX is the number of your vsc-account). This area is by default only visible by your user account.

- Your group area: /kuleuven_tier1_pilot/home/lt1_projectcode. The area is shared and visible by all the members of your group.

- The public area: /kuleuven_tier1_pilot/home/public. This is an area accessible by everyone in the system. It could be even accessed by anonymous users from external sources if this is configured. Usage of this area is discouraged, and your group directory under home should be used for shared storage.