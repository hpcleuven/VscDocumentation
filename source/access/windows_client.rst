.. _windows_client:

##################################
:fab:`windows` Access from Windows
##################################

Getting ready to login
======================

Before you can log in with SSH to a VSC cluster, you need to generate a pair of
SSH keys and upload them to your VSC account. There multiple ways to create
yours keys in Windows, please check our documentation on
:ref:`generating keys windows`.

Connecting to the cluster
=========================

Text-mode session using PuTTY
------------------------------

PuTTY  is a simple-to-use and freely available GUI SSH client for Windows that
is :ref:`easy to set up <text mode access using PuTTY>`.

.. toctree::
   :maxdepth: 2

   text_mode_access_using_putty

Text-mode and graphical browser using MobaXterm
-----------------------------------------------

MobaXterm is a free and easy to use SSH client for Windows that has text-mode,
a graphical file browser, an X server, an SSH agent, and more, all in one.
No installation is required when using the *Portable edition*. See
:ref:`detailed instructions on how to setup MobaXterm <access using mobaxterm>`.

.. toctree::
   :maxdepth: 2

   access_using_mobaxterm

Alternatives
------------

Recent versions of Windows come with an OpenSSH installed, and you can use
it from PowerShell or the Command Prompt as you would in the termial on Linux
systems and all pages about SSH and data transfer from :ref:`the Linux client
pages <linux_client>` apply.

The Windows Subsystem for Linux can be an alternative if you are using
Windows 10 build 1607 or later.  The available Linux distributions have
SSH clients, so you can refer to all pages about SSH and data transfer
from :ref:`the Linux client pages <linux_client>` as well.

.. _windows_gui:

Display graphical programs
==========================

X server
--------

X11 is the protocol that is used by most Linux applications to display
graphics on a local or remote screen. It is necessary to run an X server on
your Windows system to display graphical applications running on the Linux
system of the cluster.

|Recommended| Use the X server included in :ref:`MobaXterm <access using mobaxterm>`.

Alternatively, you can install an X server such as `Xming`_ on Windows as well.

.. toctree::

   using_the_xming_x_server_to_display_graphical_programs

NX client
---------

|KUL| On the KU Leuven/UHasselt clusters it is also possible to use the
:ref:`NX Client<NX start guide>` to log on to the machine and run graphical
programs. Instead of an X server, another piece of client software is required.

VNC
---

.. include:: vnc_support.rst

Programming tools
=================

.. warning::
   Although it is convenient to develop software on your local machine,
   you should bear in mind that the hardware architecture is likely to
   differ substantially from the VSC HPC hardware.  Therefore it is
   recommended that performance optimizations are done on the target
   system.

Windows Subsystem for Linux (WSL/WSL2)
--------------------------------------
If you're running Windows 10 build 1607 (Anniversary Edition) or
later, you may consider running the "`Windows Subsystem for
Linux <https://www.google.be/webhp?q=windows%20subsystem%20for%20linux>`_"
that will give you a Ubuntu-like environment on Windows and allow you
to install some Ubuntu packages. *In build 1607 this is still
considered experimental technology and we offer no support.*

Microsoft Visual Studio
-----------------------
:ref:`Microsoft Visual Studio <MS Visual Studio>` can also
be used to develop OpenMP or MPI programs. If you do not use any
Microsoft-specific libraries but stick to plain C or C++, the
programs can be recompiled on the VSC clusters. Microsoft is slow in
implementing new standards though. In Visual Studio 2015, OpenMP
support is still stuck at version 2.0 of the standard. An alternative
is to get a license for the Intel compilers which plug into Visual
Studio and give you the best of both worlds, the power of a
full-blown IDE and compilers that support the latest technologies in
the HPC world on Windows.

Eclipse
-------

.. include:: eclipse_intro.rst

.. note::
   On Windows Eclipse relies by default on the `Cygwin`_ toolchain for its
   compilers and other utilities, so you need to install that too.

Version control
---------------
Information on tools for version control (git and subversion) is
available on the :ref:`version control systems` introduction page.

