.. _linux_client:

##############################
:fab:`linux` Access from Linux
##############################

Since all VSC clusters use Linux as their main operating system, you
will need to get acquainted with Linux using the command-line interface and
using the terminal. To open a terminal in Linux when using KDE, choose
Applications > System > Terminal > Konsole. When using GNOME, choose
Applications > Accessories > Terminal.

If you don't have any experience with using the command-line interface
in Linux, we suggest you to read the :ref:`basic Linux
usage <basic linux>` section first.

Getting ready to login
======================

Before requesting an account, you need to generate a pair of ssh
keys. One popular way to do this on Linux is :ref:`using the freely
available OpenSSH client <generating keys linux>`
which you can then also use to log on to the clusters.

Connecting to the cluster
=========================

Text-mode session
-----------------

The OpenSSH :ref:`ssh command <OpenSSH access>` can be used to open
a connection in a Linux terminal session.

.. toctree::
   :maxdepth: 2

   text_mode_access_using_openssh

.. _linux_gui:

Display graphical programs
==========================

X server
--------

No extra software is needed on a Linux client system, but you need
to use the appropriate options with the ssh command as explained
on :ref:`the page on OpenSSH <OpenSSH access>`.

NX client
---------

|KUL| On the KU Leuven/UHasselt clusters it is also possible to
:ref:`use the NX Client <NX start guide>` to log
on to the machine and run graphical programs. This requires
additional client software that is currently available for
Windows, macOS, Linux, Android and iOS. The advantage over
displaying X programs directly on your Linux screen is that you
can sleep your laptop, disconnect and move to another network
without loosing your X-session. Performance may also be better
with many programs over high-latency networks.

VNC
---

.. include:: vnc_support.rst

Software development
====================

Eclipse
-------

.. include:: eclipse_intro.rst

Version control
---------------

Linux supports all popular version control systems. See :ref:`our
introduction to version control systems <version control systems>`.
