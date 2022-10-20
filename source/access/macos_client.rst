.. _macOS client:

macOS client
============

Since all VSC clusters use Linux as their main operating system, you
will need to get acquainted with using the command-line interface and
using the Terminal. To open a Terminal window in macOS (formerly OS X),
choose Applications > Utilities > Terminal in the Finder.

If you don't have any experience with using the Terminal, we suggest you
to read the :ref:`basic Linux usage <basic linux>` section
first (which also applies to macOS).

Getting ready to request an account
-----------------------------------

Before requesting an account, you need to generate a pair of ssh
keys. One popular way to do this on macOS is :ref:`using the OpenSSH
client <generating keys macos>` included with macOS
which you can then also use to log on to the clusters.

Connecting to the machine
-------------------------

Text-mode session using an SSH client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get terminal-based access to a remote system, you can use

-  the :ref:`OpenSSH ssh command<OpenSSH access>`, or
-  the :ref:`JellyfiSSH<JellyfiSSH access>` GUI client.


Transfer data using Secure FTP (SFTP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data can be transferred using

- Secure FTP (SFTP) with the :ref:`OpenSSH sftp and scp commands <scp and sftp>`, or
- GUI clients such as :ref:`Cyberduck or FileZilla <data transfer>`.

.. _macOS gui:

Display graphical programs
~~~~~~~~~~~~~~~~~~~~~~~~~~

X server
^^^^^^^^

Linux programs use the X protocol to display graphics on local or
remote screens. To use your Mac as a remote screen, you need to
install a X server. `XQuartz <https://www.xquartz.org/>`_
is one that is freely available. Once the X server is up and
running, you can simply open a terminal window and connect to the
cluster using the command line SSH client in the same way as you
would on Linux.

NX client
^^^^^^^^^

On the KU Leuven/UHasselt clusters it is possible to :ref:`use the NX
Client <NX start guide>` to log on to the machine and run graphical
programs. Instead of an X-server, another piece of client software is
required.


VNC
^^^
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
--------------------

Eclipse
~~~~~~~

Eclipse is a popular multi-platform Integrated Development
Environment (IDE) very well suited for code development on clusters.

-  Read our :ref:`Eclipse introduction <Eclipse intro>` to
   find out why you should consider using Eclipse if you develop code
   and how to get it. To get the full functionality of the Parallel
   Tools Platform and Fortran support on macOS, you need :ref:`to install
   some additional software and start Eclipse in a special way as we
   explain here <Eclipse macOS>`.
-  You can use :ref:`Eclipse on the desktop as a remote editor for the
   cluster <Eclipse as remote editor>`.
-  You can combine the remote editor feature with version control
   from Eclipse, but some care is needed, and :ref:`here's how to do
   it <Eclipse PTP>`.


Version control
~~~~~~~~~~~~~~~

Most popular version control systems, including Subversion and git,
are supported on macOS. See :ref:`our introduction to version control
systems <version control systems>`.
