.. _windows_client:

############################################
:fab:`windows` Terminal Interface on Windows
############################################

Getting ready to login
======================

Before you can log in with SSH to a VSC cluster, you need to generate a pair of
SSH keys and upload them to your VSC account. There are multiple ways to create
your keys in Windows, please check our documentation on
:ref:`generating keys windows`.

Connecting to the cluster
=========================

There are multiple solutions on Windows that provide a `Secure Shell`_ (SSH)
client to connect to remote machines. You need to have such a tool to connect
to the login nodes of our HPC clusters. The following are the main options
supported by VSC.

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

Windows PowerShell
    Recent versions of Windows come with OpenSSH installed. This means that you
    can use it from `PowerShell`_ or the Windows Command Prompt as you would in
    the terminal of a Linux system. All information about SSH and data transfer
    on the :ref:`Linux client <linux_client>` pages apply to OpenSSH on
    Windows in the same way.

WSL2
    The `Windows Subsystem for Linux`_ (WSL2) can be an alternative if you are
    using Windows 10 build 1607 or later. This solution allows to install a
    Linux distribution on your Windows computer and use SSH from within it.
    Hence, you can refer to all our documentation about SSH and data transfer
    found in the :ref:`Linux client <linux_client>` section.

    .. toctree::
       :maxdepth: 2

       wsl

