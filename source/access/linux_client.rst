.. _Linux client:

############
Linux client
############

Since all VSC clusters use Linux as their main operating system, you
will need to get acquainted with Linux using the command-line interface and
using the terminal. To open a terminal in Linux when using KDE, choose
Applications > System > Terminal > Konsole. When using GNOME, choose
Applications > Accessories > Terminal.

If you don't have any experience with using the command-line interface
in Linux, we suggest you to read the :ref:`basic Linux
usage <basic linux>` section first.

Getting ready to request an account
===================================

Before requesting an account, you need to generate a pair of ssh
keys. One popular way to do this on Linux is :ref:`using the freely
available OpenSSH client <generating keys linux>`
which you can then also use to log on to the clusters.


Connecting to the cluster
=========================

Text-mode session using OpenSSH
-------------------------------

The OpenSSH :ref:`ssh command <OpenSSH access>` can be used to open
a connection in a Linux terminal session.

.. toctree::
   :maxdepth: 2

   text_mode_access_using_openssh

Transfer data using Secure FTP (SFTP)
=====================================

Data can easily be transferred to and from remote systems using
the :ref:`OpenSSH sftp and scp commands <scp and sftp>`.

.. _Linux gui:

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

The KU Leuven/UHasselt, UAntwerp, and VUB clusters also offer support for
visualization software through Virtual Network Computing (VNC). VNC renders
images on the cluster and transfers the resulting images to your client device.
VNC clients are available for Windows, macOS, Linux, Android and iOS.

-  On the UAntwerp clusters, TurboVNC is supported on all regular login nodes
   (without OpenGL support) and on the visualization node of Leibniz (with
   OpenGL support through VirtualGL). See the page ":ref:`Remote visualization
   UAntwerp`" for instructions.
-  On the VUB clusters, TigerVNC is supported on all nodes. See our
   documentation on `running graphical applications
   <https://hpc.vub.be/docs/software/modules/#how-can-i-run-graphical-applications>`_
   for instructions.

Software development
====================

Eclipse
-------

.. include:: eclipse_intro.rst

Version control
---------------

Linux supports all popular version control systems. See :ref:`our
introduction to version control systems <version control systems>`.
