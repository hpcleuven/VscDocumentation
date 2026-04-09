.. _generating keys windows:

#########################################
:fab:`windows` Generating keys on Windows
#########################################

Recent versions of Windows come with `OpenSSH`_ installed, so you do not need
to install any other software to connect to the terminal interface of VSC
clusters. It is therefore the **recommended** method to generate SSH keys on
Windows.

There are multiple options to generate keys on Windows though, and depending on
your case you might need to check some of the alternative methods:

Windows OpenSSH
    |Recommended| Default option for all users using the terminal interface on recent
    Windows computers. Instructions found below in this document.

Windows Subsystem for Linux (WSL)
    Users of :ref:`WSL<wsl>` should instead refer to
    the :ref:`Linux documentation <generating keys linux>`.

Alternative SSH clients
    Older Windows systems without OpenSSH, or users needing to use SSH keys on
    third-party graphical applications should instead consider using
    :ref:`PuTTY <generating keys putty>` or
    :ref:`MobaXterm <generating keys mobaxterm>`, both of which require a
    public/private key pair in a different format.

.. toctree::
   :maxdepth: 1
   :hidden:

   generating_keys_putty
   generating_keys_mobaxterm


Requirements
============

*  Windows 11 or Windows 10 (build 1809 or newer)  
* `OpenSSH`_

You can check whether the OpenSSH software is installed on your computer
by opening `PowerShell`_ and typing:

.. code-block:: PowerShell

   $ ssh -V
   OpenSSH_for_Windows_9.5p1, LibreSSL 3.8.2

The ``ssh -V`` command should return a version string without errors. 
This assures that the OpenSSH client is correctly installed and available. 
Often the SSL library version is printed, like the example, but not necessarily.

.. note::

   If OpenSSH is not enabled but you have the minimum required version of
   Windows, you need to add it in you settings by going to your system
   settings: System > Optional features > Add an optional feature > OpenSSH
   Client. More information in the `Microsoft documentation page about
   OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-11#install-openssh-server--client>`__

Create a public/private key pair
================================

Open PowerShell and use the following command to generate a new public/private
pair (make sure to generate a 4096-bit key):

.. code-block:: PowerShell

   $ ssh-keygen -t rsa -b 4096 -f $HOME/.ssh/id_rsa_vsc
   Generating public/private rsa key pair.
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   Your identification has been saved in C:\Users\<user>/.ssh/id_rsa_vsc
   Your public key has been saved in C:\Users\<user>/.ssh/id_rsa_vsc.pub

This will ask you for a file name to store the private and public key, 
and a passphrase to protect your private key.

.. _ssh agent windows:

Add key to SSH agent
====================

|Optional| The system will ask you for your passphrase every time you want to 
use the private key, that is, every time you want to access the cluster or 
transfer your files. You can use an :ref:`SSH agent<SSH agent>` to hold your
unlocked keys and avoid being asked for the passphrase on each connection.

The following commands will enable and automatically start the SSH Agent
service on your system. You only need to do this once:

.. code-block:: PowerShell

    # The ssh-agent service is disabled by default. Configure it to start automatically. 
    # Run the following command as an administrator.
   $ Set-Service -Name ssh-agent -StartupType Automatic

    # Start the ssh-agent service
   $ Start-Service ssh-agent  
    # The following command should return a status of Running
   $ Get-Service ssh-agent

    # Add your private key. Fill in the path to your private key correctly.
   $ ssh-add C:\Users\<user>/.ssh/id_rsa_vsc

.. note::
   You need to run PowerShell as Administrator to be able to use
   the ``Set-Service`` command.

Create or edit SSH config
=========================

|Optional| You can configure your OpenSSH client to automatically 
:ref:`link your key with your VSC ID <ssh config link key vsc>`. You can follow 
all the same instructions about SSH configuration on Linux on your Windows system.
Just keep in mind to replace any paths with the corresponding format in Windows,
as ``~`` does not expand in PowerShell.

The following is an example of how to create and edit the SSH config file on
Windows:

.. code-block:: PowerShell

   $ New-Item $HOME\.ssh\config
   $ notepad $HOME\.ssh\config

.. code-block:: PowerShell
   :caption: Example SSH configuration file in Windows format

   Match final User <vscXXXXX>
     IdentityFile C:\Users\<user>\.ssh\id_rsa_vsc

   Host hortense
     User <vscXXXXX>
     HostName tier1.hpc.ugent.be
     ForwardAgent yes
     ForwardX11 yes
