.. _generating keys linux:

#####################################
:fab:`linux` Generating keys on Linux
#####################################

Requirements:

* Linux operating system
* OpenSSH

On all popular Linux distributions, the OpenSSH software is readily
available, and most often installed by default.

Check the OpenSSH installation
==============================

You can check whether the OpenSSH software is installed by opening
a terminal and typing:

::

   $ ssh -V
   OpenSSH_8.0p1, OpenSSL 1.1.1c FIPS  28 May 2019


Generating a public/private key pair
====================================

A key pair might already be present in the default location inside
your home directory:

::

   $ ls ~/.ssh
   authorized_keys   id_rsa   id_rsa.pub   known_hosts

You can recognize a public/private key pair when a pair of files has the
same name except for the extension ``.pub`` extension of one of them. In
this particular case, the private key is ``id_rsa`` and public key is
``id_rsa.pub``. You may have multiple keys (not necessarily in the
directory ``~/.ssh``) if you or your operating system requires this.

You will need to generate a new key pair, when:

-  you don't have a key pair yet, or
-  you have a key pair, but is not in the correct format (RSA) or
   uses too few bits (at least 4096),
-  you forgot the passphrase protecting your private key, or
-  or your private key was compromised.

To generate a new public/private pair, use the following command:

::

   $ ssh-keygen -t rsa -b 4096
   Generating public/private rsa key pair. 
   Enter file in which to save the key (/home/user/.ssh/id_rsa): 
   Enter passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved in /home/user/.ssh/id_rsa.
   Your public key has been saved in /home/user/.ssh/id_rsa.pub.

This will ask you for a file name to store the private and public key,
and a passphrase to protect your private key.

.. warning::

   It needs to be emphasized that you really should choose the passphrase
   wisely!  A weak passphrase poses a serious security risk.
  
The system will ask you for your passphrase every time you want to use the
private key, that is, every time you want to access the cluster or transfer
your files, unless you use an :ref:`SSH agent<SSH agent>`.


Converting SSH2 keys to OpenSSH format
======================================

*This section is only relevant if you did not use OpenSSH (as described above)
to generate an SSH key.*

If you have a public key ``id_rsa_4096_ssh.pub`` in the SSH2 format,
you can use OpenSSH's ssh-keygen to convert it to the OpenSSH format in
the following way:

::

   $ ssh-keygen -i -f ~/.ssh/id_rsa_4096_ssh.pub > ~/.ssh/id_rsa_4096_openssh.pub

.. include:: links.rst


Additional information
======================

-  `ssh-keygen manual page`_
-  `ssh manual page`_

.. include:: links.rst
