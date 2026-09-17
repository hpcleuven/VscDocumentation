.. _generating keys linux:

#####################################
:fab:`linux` Generating keys on Linux
#####################################

`OpenSSH`_ is a reputable suite of secure networking utilities based on the
`Secure Shell`_ (SSH) protocol. OpenSSH is open-source software and is readily
available on all popular Linux distributions, and most often installed by
default as well.

Requirements
============

* Linux operating system
* `OpenSSH`_

You can check whether the OpenSSH software is installed on your Linux computer
by opening a terminal and typing:

.. code-block:: bash

   $ ssh -V
   OpenSSH_8.0p1, OpenSSL 1.1.1c FIPS  28 May 2019

If it is not installed, check our
:ref:`installation instructions for OpenSSH <openssh install>`.

Create a public/private key pair
================================

A key pair might already be present in the default location inside
your home directory:

.. code-block:: bash

   $ ls ~/.ssh
   authorized_keys   id_rsa   id_rsa.pub   known_hosts

You can recognize a public/private key pair when a pair of files has the
same name except for the extension ``.pub`` extension of one of them. In
this particular case, the private key is ``id_rsa`` and public key is
``id_rsa.pub``. You may have multiple keys (not necessarily in the
directory ``~/.ssh``) if you or your operating system requires this.

.. warning::

   For security reasons, users should always generate a new key pair for use in
   the VSC clusters, and only use it for the VSC clusters.

You will need to generate a new key pair, when:

-  you don’t yet have a dedicated key pair for the VSC clusters, or
-  you forgot the passphrase protecting your private key, or
-  or your private key was compromised.

To generate a new public/private pair, use the following command (make sure to
generate a 4096-bit key):

.. code-block:: text

   $ ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_vsc
   Generating public/private rsa key pair. 
   Enter passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved in /home/user/.ssh/id_rsa_vsc
   Your public key has been saved in /home/user/.ssh/id_rsa_vsc.pub

This will ask you for a file name to store the private and public key,
and a passphrase to protect your private key.

.. warning::

   It needs to be emphasized that you really should choose the passphrase
   wisely!  A weak passphrase poses a serious security risk.
  
The system will ask you for your passphrase every time you want to use the
private key, that is, every time you want to access the cluster or transfer
your files, unless you use an :ref:`SSH agent<SSH agent>`.

Next, make sure to configure your OpenSSH client to automatically
:ref:`link your key with your VSC ID <ssh config link key vsc>`.

Converting SSH2 keys to OpenSSH format
======================================

*This section is only relevant if you did not use OpenSSH (as described above)
to generate an SSH key.*

If you have an existing public key ``id_rsa_vsc_ssh2.pub`` in the SSH2 format,
you can use OpenSSH's ``ssh-keygen`` command to convert it to the OpenSSH
format in the following way:

.. code-block:: bash

   $ ssh-keygen -i -f ~/.ssh/id_rsa_vsc_ssh2.pub > ~/.ssh/id_rsa_vsc_openssh.pub

Additional information
======================

-  `ssh-keygen manual page`_
-  `ssh manual page`_

