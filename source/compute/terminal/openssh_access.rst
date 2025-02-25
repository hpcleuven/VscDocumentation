.. _OpenSSH access:

############################
Remote Terminal with OpenSSH
############################

Prerequisites
=============

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven
      :sync: kuluh

      To access KU Leuven clusters, only an approved
      :ref:`VSC account <access>` is needed as a prerequisite.

   .. tab-item:: UAntwerpen
      :sync: ua

      Before attempting to launch a terminal on UAntwerpen clusters, you need
      to have :ref:`a private key in OpenSSH format <generating keys linux>`
      that is already :ref:`uploaded to your VSC account <upload public key>`.

   .. tab-item:: UGent
      :sync: ug

      Before attempting to launch a terminal on UGent clusters, you need
      to have :ref:`a private key in OpenSSH format <generating keys linux>`
      that is already :ref:`uploaded to your VSC account <upload public key>`.

   .. tab-item:: VUB
      :sync: vub

      Before attempting to launch a terminal on VUB clusters, you need
      to have :ref:`a private key in OpenSSH format <generating keys linux>`
      that is already :ref:`uploaded to your VSC account <upload public key>`.

.. _openssh install:

Installation
============

You can check whether the OpenSSH software is installed on your Linux computer
by opening a terminal and typing:

.. code-block:: bash

   $ ssh -V
   OpenSSH_8.0p1, OpenSSL 1.1.1c FIPS  28 May 2019

If it is not installed, you need to know the Linux distribution on your
computer and use the corresponding command to install it with its package
manager. The following are the installation commands for some popular Linux
distributions:

* Distros with APT package manager (Debian, Ubuntu)

  .. code-block:: bash

     $ sudo apt install openssh-client

* Distros with RPM package manager (Red Hat, Fedora, SuSE)

  .. code-block:: bash

     $ sudo dnf install openssh

* Distros with Pacman package manager (Arch)

  .. code-block:: bash

     $ sudo pacman -S openssh

Connecting to VSC clusters
==========================

Start an SSH connection to the VSC cluster of your choice with the ``ssh``
command. Once the secure connection is established, a terminal shell will open
ready to accept your commands.

.. code-block:: bash

   $ ssh -i ~/.ssh/id_rsa_vsc <vsc-account>@<vsc-loginnode>

You have to adapth the following placeholder elements on this command:

* ``<vsc-account>`` is your VSC username, which you get after completing the
  :ref:`application of a VSC account <apply for account>`. It is of the form
  ``vsc00000`` and you can check it on the `VSC account page`_

* ``<vsc-loginnode>`` is the name of the login node of the VSC cluster you
  want to connect to. It is of the form ``login.hpc.<institute>.be`` and you
  can find the exact name of the login node of any VSC cluster in
  :ref:`tier1 hardware` or :ref:`tier2 hardware`.

* ``~/.ssh/id_rsa_vsc`` is the path to your private SSH key. This value is the
  default used in our guide about :ref:`generating keys linux`. But the file of
  the private can have any arbitrary name of your choice.

.. note::

   The first time you make a connection to a login node, you will be prompted
   to verify the authenticity of the login node, e.g.,
   
   .. code-block:: text
   
      $ ssh vsc98765@login.hpc.kuleuven.be
      The authenticity of host 'login.hpc.kuleuven.be (134.58.8.192)' can't be established.
      RSA key fingerprint is b7:66:42:23:5c:d9:43:e8:b8:48:6f:2c:70:de:02:eb.
      Are you sure you want to continue connecting (yes/no)?

Configuration of OpenSSH client
===============================

The SSH configuration file ``~/.ssh/config`` can be used to configure your SSH
connections. For instance, to automatically define your username, or the
location of your key, or add X forwarding. See below for some useful tips to
help you save time when working on a terminal-based session.

.. toctree::

   openssh_ssh_config

Managing keys with SSH agent
============================

Once you've successfully connected to a VSC cluster, you will notice that you
are prompted for the passphrase of your SSH key every time you connect
to it. You can avoid the need to re-type it by using an SSH agent.

Check the documentation in: :ref:`OpenSSH agent`

.. _openssh x11 forwarding:

Connecting with support for graphics
====================================

On most clusters, we support a number of programs that can display graphics or
provide a graphical interface (GUI). Those programs can be displayed over the
SSH terminal interface on your computer by enabling *X11-Forwarding*. This
options allows graphical applications to use the X Window System protocol to
send their graphical data over the network.

You can enable *X11-Forwarding* on your SSH connections with the ``-X`` option.

.. code-block:: bash

   $ ssh -X vsc98765@login.hpc.kuleuven.be

To test the connection, you can try to start a simple X program on the login
nodes, e.g., ``xeyes``. The latter will open a new window with a pair of eyes.
The pupils of these eyes should follow your mouse pointer around. Close the
program by typing *CTRL+C* and the window should disappear.

If you get the error 'DISPLAY is not set', you did not correctly enable
the *X11-Forwarding*.

.. note::

   There is also the oposite option ``-x`` which disables X traffic. This might
   be useful depending on the default options on your system as specified in
   ``/etc/ssh/ssh_config``, or ``~/.ssh/config``.

Proxies and network tunnels to compute nodes
--------------------------------------------

Network communications between your local machine and some node in the cluster
other than the login nodes will be blocked by the cluster firewall. In such a
case, you can directly open a shell in the compute node with an SSH connection
using the login node as a proxy or, alternatively, you can also open a network
tunnel to the compute node which will allow direct communication from software
in your computer to certain ports in the remote system.

.. toctree::

   openssh_ssh_proxy
   openssh_ssh_tunnel

.. _troubleshoot_openssh:

Troubleshooting OpenSSH connection issues
-----------------------------------------

When contacting support regarding connection issues, it saves time if you
provide the verbose output of the ``ssh`` command.  This can be obtained by
adding the ``-vvv`` option for maximal verbosity.

If you get a ``Permission denied`` error message, one of the things to verify
is that your private key is in the default location, i.e., the output of
``ls ~/.ssh`` should show a file named ``id_rsa_vsc``.

The second thing to check is that your
:ref:`private key is linked to your VSC ID <ssh config link key vsc>`
in your :ref:`SSH configuration file <ssh_config>` at ``~/.ssh/config``.

If your private key is not stored in ``~/.ssh/id_rsa_vsc``, you need to adapt
the path to it in your ``~/.ssh/config`` file.

Alternatively, you can provide the path as an option to the ``ssh`` command when
making the connection:

.. code-block:: bash

   $ ssh -i <path-to-your-private-key-file> <vsc-account>@<vsc-loginnode>

SSH Manual
----------

* `ssh manual page`_

