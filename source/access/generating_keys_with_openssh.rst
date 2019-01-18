.. _generating keys linux:

Generating keys with OpenSSH
============================

Prerequisite: OpenSSH
---------------------

Linux
~~~~~

On all popular Linux distributions, the OpenSSH software is readily
available, and most often installed by default. You can check whether
the OpenSSH software is installed by opening a terminal and typing:

::

   $ ssh -V
   OpenSSH_4.3p2, OpenSSL 0.9.8e-fips-rhel5 01 Jul 2008

To access the clusters and transfer your files, you will use the
following commands:

-  ssh: to generate the ssh keys and to open a shell on a remote
   machine,
-  sftp: a secure equivalent of ftp,
-  scp: a secure equivalent of the remote copy command rcp.

Windows
~~~~~~~

You can use OpenSSH on Windows also if you install the `free UNIX
emulation layer Cygwin <\%22http://www.cygwin.com/\%22>`__ with the
package \\"openssh\".

macOS/OS X
~~~~~~~~~~

macOS/OS X comes with its own implementation of OpenSSH, so you don't
need to install any third-party software to use it. Just open a Terminal
window and jump in!

Generating a public/private key pair
------------------------------------

Usually you already have the software needed and a key pair might
already be present in the default location inside your home directory:

::

   $ ls ~/.ssh
   authorized_keys2    id_rsa            id_rsa.pub         known_hosts

You can recognize a public/private key pair when a pair of files has the
same name except for the extension \\".pub\" added to one of them. In
this particular case, the private key is \\"id_rsa\" and public key is
\\"id_rsa.pub\". You may have multiple keys (not necessarily in the
directory \\"~/.ssh\") if you or your operating system requires this. A
popular alternative key type, instead of rsa, is dsa. However, we
recommend to use rsa keys.

You will need to generate a new key pair, when:

-  you don't have a key pair yet,
-  you forgot the passphrase protecting your private key,
-  or your private key was compromised.

To generate a new public/private pair, use the following command:

::

   $ ssh-keygen
   Generating public/private rsa key pair. 
   Enter file in which to save the key (/home/user/.ssh/id_rsa): 
   Enter passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved in /home/user/.ssh/id_rsa.
   Your public key has been saved in /home/user/.ssh/id_rsa.pub.

This will ask you for a file name to store the private and public key,
and a passphrase to protect your private key. It needs to be emphasized
that you really should choose the passphrase wisely! The system will ask
you for it every time you want to use the private key, that is every
time you want to access the cluster or transfer your files.

Keys are required in the OpenSSH format.

If you have a public key \\"id_rsa_2048_ssh.pub\" in the SSH2 format,
you can use OpenSSH's ssh-keygen to convert it to the OpenSSH format in
the following way:

::

   $ ssh-keygen -i -f ~/.ssh/id_rsa_2048_ssh.pub > ~/.ssh/id_rsa_2048_openssh.pub

"
