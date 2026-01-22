.. _generating keys windows:

#########################################
:fab:`windows` Generating keys on Windows
#########################################

Recent versions of Windows come with `OpenSSH`_ installed, so you do not 
need to install other software.

.. seealso::
   This documentation covers the use of OpenSSH on Windows to generate keys, 
   which will be similar to the Linux documentation. 
   If you use WSL on Windows, please refer to the :ref:`Linux documentation 
   <generating keys linux>`.

.. seealso::
   Alternatively, if your installation does not come with OpenSSH, or you want 
   to use a different SSH client, we provide documentation for two SSH legacy 
   clients, :ref:`PuTTY <terminal putty>` and :ref:`MobaXterm <terminal mobaxterm>`,
   both of which require a public/private key pair in a different format:

   .. toctree::
      :maxdepth: 1

      generating_keys_putty
      generating_keys_mobaxterm


Requirements
============

* Windows operating system
* `OpenSSH`_

You can check whether the OpenSSH software is installed on your computer
by opening `PowerShell`_ (or command prompt) and typing:

.. code-block:: bash

   $ ssh -V
   OpenSSH_for_Windows_9.5p1, LibreSSL 3.8.2

You want the ``ssh -V`` command to return a version string without errors. 
This assures that the OpenSSH client is correctly installed and available. 
Often the SSL library version is printed, like the example, but not necessarily.

If OpenSSH is not installed, `you need to add it in you settings 
<https://learn.microsoft.com/en-us/windows-server/administration/openssh/
openssh_install_firstuse?tabs=gui&pivots=windows-11#install-openssh-server--client>`__ : 
System > Optional features > Add an optional feature > OpenSSH Client

Create a public/private key pair
================================

Open PowerShell (or command prompt). To generate a new public/private pair, 
use the following command (make sure to generate a 4096-bit key):

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -f $HOME\.ssh\id_rsa_vsc
   Generating public/private rsa key pair.
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   Your identification has been saved in C:\Users\<user>\.ssh\id_rsa_vsc
   Your public key has been saved in C:\Users\<user>\.ssh\id_rsa_vsc.pub

This will ask you for a file name to store the private and public key, 
and a passphrase to protect your private key.

.. _ssh agent windows:

Add the key to the SSH agent
============================

|Optional| The system will ask you for your passphrase every time you want to 
use the private key, that is, every time you want to access the cluster or 
transfer your files, unless you use an :ref:`SSH agent<SSH agent>`.

.. code-block:: bash
  
    # By default, the ssh-agent service is disabled. Configure it to start automatically. 
   $ Set-Service -Name ssh-agent -StartupType Automatic
    # Start the ssh-agent service
   $ Start-Service ssh-agent  

    # Add your private key
   $ ssh-add $HOME\.ssh\id_rsa_vsc

.. note::
   Note: You may need to run PowerShell as Administrator.

Create or edit SSH config
=========================

|Optional| Next, make sure to configure your OpenSSH client to automatically 
:ref:`link your key with your VSC ID <ssh config link key vsc>`. You can apply 
all the information about SSH on the Linux pages to OpenSSH on Windows, though 
you will need to replace the paths, as ``~`` does not expand in PowerShell.


