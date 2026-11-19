.. _windows_client:

############################################
:fab:`windows` Terminal Interface on Windows
############################################

Getting ready to login
======================

Before you can log in to a VSC cluster using SSH, you need to
check which authentication method the cluster supports.

For clusters that support :ref:`mfa_login`, SSH keys are not required.

For clusters that do not support MFA, you need to generate an SSH key pair and
upload the public key to your VSC account on your your `VSC Account - Edit
Account`_ page before logging in.  There are multiple ways to generate SSH keys
in Windows. See :ref:`generating keys windows` for instructions.

Connecting to the cluster
=========================

There are multiple solutions on Windows that provide a `Secure Shell`_ (SSH)
client to connect to remote machines. You need to have such a tool to connect
to the login nodes of our HPC clusters. The following are the main options
supported by VSC.

Windows PowerShell
    Recent versions of Windows come with OpenSSH installed. This means that you
    can use it from `PowerShell`_ or the Windows Command Prompt as you would in
    the terminal of a Linux system. All information about SSH and data transfer
    on the :ref:`Linux client <linux_client>` pages apply to OpenSSH on
    Windows in the same way, though you may need to adjust the file paths so 
    they work correctly on Windows.

PuTTY
    PuTTY  is a simple-to-use and freely available GUI SSH client for Windows that
    is :ref:`easy to set up <terminal PuTTY>`.

    .. toctree::
       :maxdepth: 2

       putty_access

MobaXterm
    MobaXterm is a free and easy to use SSH client for Windows that has
    text-mode, a graphical file browser, an X server, an SSH agent, and more,
    all in one. Installation is very simple when using its *Portable edition*.

    .. toctree::
       :maxdepth: 2

       mobaxterm_access

WSL2
    The `Windows Subsystem for Linux`_ (WSL2) can be an alternative if you are
    using Windows 10 build 1607 or later. This solution allows to install a
    Linux distribution on your Windows computer and use SSH from within it.
    Hence, you can refer to all our documentation about SSH and data transfer
    found in the :ref:`Linux client <linux_client>` section.

    .. toctree::
       :maxdepth: 2

       wsl

