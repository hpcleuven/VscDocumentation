.. _tunnel OpenSSH:

SSH tunnel using OpenSSH
========================

Prerequisites
-------------

-  An SSH key pair (optional for KU Leuven clusters), see :ref:`page
   on generating keys <create key pair>`.
-  Additionally, you should be able to :ref:`connect to the cluster's login
   node <OpenSSH access>` using SSH.

Background
----------

Because of one or more firewalls between your desktop and the HPC
clusters, it is generally impossible to communicate directly with a
process on the cluster from your desktop except when the network
managers have given you explicit permission (which for security reasons
is not often done). One way to work around this limitation is SSH
tuneling. There are serveral cases where this is usefull:

-  Running X applications on the cluster: The X program cannot directly
   communicate with the X server on your local system. In this case, the
   tunneling is easy to set up as OpenSSH will do it for you if you
   specify the -X-option on the command line when you log on to the
   cluster in text mode:

   ::

      $ ssh -X <vsc-account>@<vsc-loginnode>
          

   where <vsc-account> is your VSC-number and <vsc-loginnode> is the
   hostname of the cluster's login node you are using.

-  Running a server application on the cluster that a client on the
   desktop connects to. One example of this scenario is :ref:`ParaView in
   remote visualization mode <Paraview>`,
   with the interactive client on the desktop and the data processing
   and image rendering on the cluster. Setting up a tunnel for this
   scenario is also :ref:`explained on that page <Paraview>`.
-  Running clients on the cluster and a server on your desktop. In this
   case, the source port is a port on the cluster and the destination
   port is on the desktop.

Procedure
---------

In a terminal window on your client machine, issue the following
command:

::

   ssh -L 11111:r1i3n5:44444 -N <vsc-account>@<vsc-loginnode>

where <vsc-account> is your VSC-number and <vsc-loginnode> is the
hostname of the cluster's login node you are using. The local port is
given first (e.g., 11111, followed by the remote host (e.g., 'r1i3n5')
and the server port (e.g., 44444).

#. Log in on the login node
#. Start the server job, note the compute node's name the job is running
   on (e.g., 'r1i3n5'), as well as the port the server is listening on
   (e.g., '44444').
