.. _macos_client:

########################################
:fab:`apple` Terminal Interface on macOS
########################################

If you are using a macOS system on your own computer, then you already have all
the tools to start a terminal interface on the VSC clusters. You just need to
launch the Terminal app and the ``ssh`` command, which is available by default.

To open a Terminal window in macOS (formerly OS X), go to *Applications* >
*Utilities* > *Terminal* in *Finder*. If you don't have any experience using
the Terminal, we suggest you to first read our :ref:`basic linux` guide, which
also applies to macOS as it based on the same `GNU`_ operating system as Linux.

Getting ready to login
======================

Before you can log in with SSH to a VSC cluster, you need to generate a pair of
SSH keys and upload them to your VSC account. You can create your keys in macOS
with `OpenSSH`_, please check our documentation on :ref:`generating keys macos`.

Connecting to the cluster
=========================

OpenSSH
    `OpenSSH`_ is a reputable suite of secure networking utilities based on the
    `Secure Shell`_ (SSH) protocol. OpenSSH is open-source software and is readily
    available on all macOS versions.

JellyfiSSH
    `JellyfiSSH`_ is a bookmark manager specifically built for storing SSH
    connections. Sitting in the dock or accessible via menulet, JellyfiSSH
    allows you to easily store SSH connections and launch new terminal windows
    using customisable saved settings.

.. toctree::
   :maxdepth: 2

   openssh_jellyfissh_access

