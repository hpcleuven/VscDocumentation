Text-mode access using OpenSSH
==============================

Prerequisite: OpenSSH
---------------------

See `the page on generating
keys <\%22/client/linux/keys-openssh\%22>`__.

Connecting to the VSC clusters
------------------------------

Text mode
~~~~~~~~~

In many cases, a text mode connection to one of the VSC clusters is
sufficient. To make such a connection, the ssh command is used:

::

   $ ssh <vsc-account>@<vsc-loginnode>

Here,

-  <vsc-account> is your VSC username that you have received by mail
   after your request was approved,
-  <vsc-loginnode> is the name of the loginnode of the VSC cluster you
   want to connect to.

You can find the names and ip-addresses of the loginnodes in the
sections on the\ `available
hardware <\%22/infrastructure/hardware\%22>`__\ .

The first time you make a connection to the loginnode, you will be asked
to verify the authenticity of the loginnode, e.g.,

::

   $ ssh vsc98765@login.hpc.kuleuven.be
   The authenticity of host 'login.hpc.kuleuven.be (134.58.8.192)' can't be established.
   RSA key fingerprint is b7:66:42:23:5c:d9:43:e8:b8:48:6f:2c:70:de:02:eb.
   Are you sure you want to continue connecting (yes/no)?

Here, user vsc98765 wants to make a connection to the ThinKing cluster
at KU Leuven via the loginnode login.hpc.kuleuven.be.

If your private key is not stored in a default file (~/.ssh/id_rsa) you
need to provide the path to it while making the connection:

::

   $ ssh -i <path-to-your-private-key-file> <vsc-account>@<vsc-loginnode>

Connection with support for graphics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| On most clusters, we support a number of programs that have a GUI mode
  or display graphics otherwise through the X system. To be able to
  display the output of such a program on the screen of your Linux
  machine, you need to tell ssh to forward X traffic from the cluster to
  your Linux desktop/laptop by specifying the -X option. There is also
  an option -x to disable such traffic, depending on the default options
  on your system as specified in /etc/ssh/ssh_config, or ~/.ssh/config.
| Example:

::

   ssh -X vsc123456@login.hpc.kuleuven.be

To test the connection, you can try to start a simple X program on the
login nodes, e.g., ``xterm`` or ``xeyes``. The latter will open a new
window with a pair of eyes. The pupils of these eyes should follow your
mouse pointer around. Close the program by typing \\"ctrl+c\": the
window should disappear.

If you get the error 'DISPLAY is not set', you did not correctly enable
the X-Forwarding.

Links
-----

-  `ssh manual page <\%22http://man.openbsd.org/ssh\%22>`__ (external)

"
