.. _OpenSSH access:

Text-mode access using OpenSSH
==============================

Prerequisite: OpenSSH
---------------------

You will need a public/private key pair to request and account, this key pair
has to be used to authenticate when making a connection.  For information
on how to create a key pair, see :ref:`the page on generating keys <generating keys linux>`.

How to connect?
---------------

In many cases, a text mode connection to one of the VSC clusters is
sufficient. To make such a connection, the ssh command is used:

::

   $ ssh <vsc-account>@<vsc-loginnode>

Here,

-  ``<vsc-account>`` is your VSC username that you have received by mail
   after your request was approved, e.g., ``vsc98765``, and
-  ``<vsc-loginnode>`` is the name of the login node of the VSC cluster you
   want to connect to, e.g., ``login.hpc.kuleuven.be``.

You can find the names of the login nodes for the various clusters
in the sections on the :ref:`available hardware <hardware>`.

.. note::

   The first time you make a connection to a login node, you will be prompted
   to verify the authenticity of the login node, e.g.,
   
   ::
   
      $ ssh vsc98765@login.hpc.kuleuven.be
      The authenticity of host 'login.hpc.kuleuven.be (134.58.8.192)' can't be established.
      RSA key fingerprint is b7:66:42:23:5c:d9:43:e8:b8:48:6f:2c:70:de:02:eb.
      Are you sure you want to continue connecting (yes/no)?


How to connect with support for graphics?
-----------------------------------------

On most clusters, we support a number of programs that have a GUI mode
or display graphics otherwise through the X system. To be able to
display the output of such a program on the screen of your Linux
machine, you need to tell ssh to forward X traffic from the cluster to
your Linux desktop/laptop by specifying the ``-X`` option. There is also
an option ``-x`` to disable such traffic, depending on the default options
on your system as specified in ``/etc/ssh/ssh_config``, or ``~/.ssh/config``.

Example:

::

   $ ssh -X vsc98765@login.hpc.kuleuven.be

To test the connection, you can try to start a simple X program on the
login nodes, e.g., ``xeyes``. The latter will open a new
window with a pair of eyes. The pupils of these eyes should follow your
mouse pointer around. Close the program by typing \\"ctrl+c\": the
window should disappear.

If you get the error 'DISPLAY is not set', you did not correctly enable
the X-Forwarding.


How to configure the OpenSSH client?
------------------------------------

The SSH configuration file ``~/.ssh/config`` can be used to configure your SSH
connections. For instance, to automatically define your username, or the
location of your key, or add X forwarding. We provide :ref:`some useful
tips<SSH config>` to help you save time when working on a terminal-based
session.

Managing keys with an SSH agent
-------------------------------

It is convenient to use :ref:`an SSH-agent <SSH agent>` to avoid
having to enter your private key's passphrase all the time when
establishing a new connection.

Network tunnel to compute node
------------------------------

To establish network communication between your local machine and the cluster
otherwise blocked by firewalls, you have to create an
:ref:`SSH tunnel using OpenSSH <tunnel OpenSSH>`.

.. toctree::

   creating_a_ssh_tunnel_using_openssh

Troubleshooting OpenSSH connection issues
-----------------------------------------

When contacting support regarding connection issues, it saves time if you
provide the verbose output of the ``ssh`` command.  This can be obtained by
adding the ``-vvv`` option for maximal verbosity.

If you get a ``Permission denied`` error message, one of the things to verify
is that your private key is in the default location, i.e., the output of
``ls ~/.ssh`` should show a file named ``id_rsa_vsc``.

The second thing to check is that your :ref:`private key is linked to your
VSC-id <linking key with vsc-id linux>` in your :ref:`SSH configuration file <SSH
config>` at ``~/.ssh/config``.

If your private key is not stored in ``~/.ssh/id_rsa_vsc``, you need to adapt
the path to it in your ``~/.ssh/config`` file.

Alternatively, you can provide the path as an option to the ``ssh`` command when
making the connection:

::

   $ ssh -i <path-to-your-private-key-file> <vsc-account>@<vsc-loginnode>

SSH Manual
----------

-  `ssh manual page`_

