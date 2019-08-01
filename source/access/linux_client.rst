.. _Linux client:

Linux client
============

Since all VSC clusters use Linux as their main operating system, you
will need to get acquainted with using the command-line interface and
using the terminal. To open a terminal in Linux when using KDE, choose
Applications > System > Terminal > Konsole. When using GNOME, choose
Applications > Accessories > Terminal.

If you don't have any experience with using the command-line interface
in Linux, we suggest you to read the :ref:`basic Linux
usage <basic linux>` section first.


Getting ready to request an account
-----------------------------------

Before requesting an account, you need to generate a pair of ssh
keys. One popular way to do this on Linux is :ref:`using the freely
available OpenSSH client <generating keys linux>`
which you can then also use to log on to the clusters.


Connecting to the cluster
-------------------------

Text-mode session using an SSH client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenSSH :ref:`ssh command <OpenSSH access>` can be used to open
a connection in a Linux terminal session.

It is convenient to use :ref:`an SSH-agent <SSH agent>` to avoid
having to enter your private key's passphrase all the time when
establishing a new connection.

If you need to log in to a node protected by a firewall through another
login node, you need to :ref:`sett up an SSH proxy <proxy>` to log in to
the protected node, e.g., to access the tier-1 system muk.

To establish network communication between your local machine and the
cluster otherwise blocked by firewalls, you have to :ref:`create an
SSH tunnel using OpenSSH <tunnel OpenSSH>`.


Transfer data using Secure FTP (SFTP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data can easily be transferred to and from remote systems using
the :ref:`OpenSSH sftp and scp commands <scp and sftp>`.


Display graphical programs
~~~~~~~~~~~~~~~~~~~~~~~~~~

X server
^^^^^^^^

No extra software is needed on a Linux client system, but you need
to use the appropriate options with the ssh command as explained
on :ref:`the page on OpenSSH <OpenSSH access>`.

NX client
^^^^^^^^^

On the KU Leuven/UHasselt clusters it is also possible to :ref:`use
the NX Client <NX start guide>` to log
on to the machine and run graphical programs. This requires
additional client software that is currently available for
Windows, OS X, Linux, Android and iOS. The advantage over
displaying X programs directly on your Linux screen is that you
can sleep your laptop, disconnect and move to another network
without loosing your X-session. Performance may also be better
with many programs over high-latency networks.

TurboVNC
^^^^^^^^

The KU Leuven/UHasselt and UAntwerp clusters also offer support
for visualization software through TurboVNC. VNC renders images on
the cluster and transfers the resulting images to your client
device. VNC clients are available for Windows, macOS, Linux,
Android and iOS.

-  On the KU Leuven/UHasselt clusters, :ref:`TurboVNC is supported on
   the visualization nodes <TurboVNC start guide>`.
-  On the UAntwerp clusters, TurboVNC is supported on all regular
   login nodes (without OpenGL support) and on the visualization
   node of Leibniz (with OpenGL support through VirtualGL). See
   the page ":ref:`Remote visualization @ UAntwerp <remote visualization
   UAntwerp>`" for instructions.


Software development
--------------------

Eclipse
~~~~~~~

Eclipse is a popular multi-platform Integrated Development
Environment (IDE) very well suited for code development on clusters.

-  Read our :ref:`Eclipse introduction <Eclipse intro>` to
   find out why you should consider using Eclipse if you develop code
   and how to get it.
-  You can use :ref:`Eclipse on the desktop as a remote editor for the
   cluster <Eclipse as remote editor>`.
-  You can use :ref:`Eclipse on the desktop to access files in a
   subversion repository on the cluster <Eclipse VSC subversion>`.
-  You can combine the remote editor feature with version control
   from Eclipse, but some care is needed, and :ref:`here's how to do
   it <Eclipse PTP>`.


Version control
~~~~~~~~~~~~~~~

Linux supports all popular version control systems. See :ref:`our
introduction to version control systems <version control systems>`.

Specific instructions to :ref:`access subversion repositories on the
VSC clusters or other servers from your desktop with UNIX-style
command line tools <desktop access VSC SVN>`.
