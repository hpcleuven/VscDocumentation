.. _wsl:

##########################
Installing WSL2 on windows
##########################

As a Windows user, if you don't already use any virtualisation system to
operate Linux you can install Windows Subsystem for Linux (WSL2).

You must be running Windows 10 version 2004 and higher (Build 19041 and higher)
or Windows 11 to be able to use WSL2.
The requirements can be checked by typing ``winver`` on your search bar, a
informative popup appears showing your Windows version.

|KUL| Users who are using a system managed by KU Leuven should fulfill these
requirements. 

The installation of WSL2 will consist of the following steps:

1. Enable WSL 2
2. Enable *Virtual Machine Platform*
3. Set WSL 2 as default
4. Install a Linux distro

We will complete all steps by using Power Shell of Windows. However you can do
some of the steps by graphical screens as an option. Here you can find all
steps.

Run Windows PowerShell as administrator and type the following to enable WSL:

.. code-block::

   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

To enable Virtual Machine Platform on Windows 10 (2004), execute the following command:

.. code-block::

   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

To set WSL 2 as default execute the command below (You might need to restart your PC):

.. code-block::

   wsl --set-default-version 2

To install your Linux distribution of choice on Windows 10, open the Microsoft
Store app, search for it, and click the “Get” button.
The first time you launch a newly installed Linux distribution, a console
window will open and you'll be asked to wait for a minute or two.
You will then need to create a user account and password for your new Linux
distribution. This password will give you ‘sudo' rights when asked.
If you see ‘WSLRegisterDistribution Failed with Error:' or you may find that
things don't work as intended you should restart your system at this point.
After all these steps when you type ‘wsl' to your Windows PowerShell, you will
be directed to your Ubuntu machine mounted on your Windows' C drive. From now
on, you can execute all Linux commands. It is advised to use the home directory
instead of your Windows drives. So if you type ‘cd‘ you will be forwarded to
your Ubuntu home.

You can also install (optional) the Windows Terminal app, which enables
multiple tabs operation, search feature, and custom themes etc.
