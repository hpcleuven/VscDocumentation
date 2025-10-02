.. _generating keys windows:

#########################################
:fab:`windows` Generating keys on Windows
#########################################

Modern Windows installations (10, 11) include OpenSSH client tools as optional features.
(If you use WSL on Windows, treat it as a Linux machine and follow the Linux documentation)
This documentation covers the use of OpenSSH on Windows, which will be similar to Linux. Alternatively, if you cannot install OpenSSH, or you want to use a different SSH client, we provide documentation for
two SSH legacy clients, :ref:`PuTTY <terminal putty>` and :ref:`MobaXterm <terminal mobaxterm>`,
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
by opening a terminal (PowerShell or cmd) and typing:

.. code-block:: bash

   $ ssh -V
    OpenSSH_for_Windows_9.5p1, LibreSSL 3.8.2

If it is not installed, you may need to add it via "Manage optional features" -> Add a feature -> OpenSSH Client
TODO link

Create a public/private key pair
===============================

Open a terminal (this can be PowerShell or cmd). To generate a new public/private pair, use the following command (make sure to generate a 4096-bit key):

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -f $HOME\.ssh\id_rsa_vsc
   TODO

This will ask you for a file name to store the private and public key, and a passphrase to protect your private key.


(optional) Add the key to the SSH agent
=======================================

The system will ask you for your passphrase every time you want to use the private key, that is, every time you want to access the cluster or transfer your files, unless you use an SSH agent.
TODO You may need to run PowerShell as Administrator

.. code-block:: bash
   
   $ Set-Service -Name ssh-agent -StartupType Automatic
     # Start the ssh-agent service (if not already running)
   $ Start-Service ssh-agent  

     # Add your private key
   $ ssh-add $HOME\.ssh\id_rsa_vsc



