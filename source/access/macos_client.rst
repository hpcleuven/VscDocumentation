.. _macos_client:

##############################
:fab:`apple` Access from macOS
##############################

Since all VSC clusters use Linux as their main operating system, you
will need to get acquainted with using the command-line interface and
using the Terminal. To open a Terminal window in macOS (formerly OS X),
choose Applications > Utilities > Terminal in the Finder.

If you don't have any experience with using the Terminal, we suggest you
to read the :ref:`basic Linux usage <basic linux>` section
first (which also applies to macOS).

Getting ready to login
======================

Before requesting an account, you need to generate a pair of ssh
keys. One popular way to do this on macOS is :ref:`using the OpenSSH
client <generating keys macos>` included with macOS
which you can then also use to log on to the clusters.

Connecting to the cluster
=========================

.. toctree::
   :maxdepth: 2

   text_mode_access_using_openssh_or_jellyfissh

.. _macos_gui:

Display graphical programs
==========================

X server
--------

Linux programs use the X protocol to display graphics on local or
remote screens. To use your Mac as a remote screen, you need to
install a X server. `XQuartz <https://www.xquartz.org/>`_
is one that is freely available. Once the X server is up and
running, you can simply open a terminal window and connect to the
cluster using the command line SSH client in the same way as you
would on Linux.

NX client
---------

|KUL| On the KU Leuven/UHasselt clusters it is possible to :ref:`use the NX
Client <NX start guide>` to log on to the machine and run graphical
programs. Instead of an X-server, another piece of client software is
required.


VNC
---

.. include:: vnc_support.rst

Software development
====================

Eclipse
-------

.. include:: eclipse_intro.rst

.. note::
   To get the full functionality of the Parallel Tools Platform and Fortran
   support on macOS, you need :ref:`to install some additional software and
   start Eclipse in a special way as we explain here <Eclipse macOS>`.

Version control
---------------

Most popular version control systems, including Subversion and git,
are supported on macOS. See :ref:`our introduction to version control
systems <version control systems>`.
