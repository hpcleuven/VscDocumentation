Windows client
==============

The icons
---------

+-----------------------------------+-----------------------------------+
| |Windows|                         | Works on Windows, but may need    |
|                                   | additional pure Windows packages  |
|                                   | (free or commercial)              |
+-----------------------------------+-----------------------------------+
| |Windows+Linux|                   | Works on Windows with a `UNIX     |
|                                   | compatibility                     |
|                                   | layer <\%22#UNIX\%22>`__ added,   |
|                                   | e.g., cygwin or the \\"Windows    |
|                                   | Subsystem for Linux\" in Windows  |
|                                   | 10 build 1607 (anniversary        |
|                                   | edition) or later                 |
+-----------------------------------+-----------------------------------+

Getting ready to request an account
-----------------------------------

-  Before requesting an account, you need to generate a pair of ssh
   keys. One popular way to do this on Windows is\ `using the freely
   available PuTTY client <\%22/client/windows/keys-putty\%22>`__ which
   you can then also use to log on to the clusters.

Connecting to the cluster
-------------------------

-  Open a text-mode session using an ssh client

   -  `PuTTY <\%22/client/windows/console-putty\%22>`__ is a
      simple-to-use and freely available GUI SSH client for Windows.
   -  `pageant <\%22/client/windows/using-pageant\%22>`__ can be used to
      manage active keys for PuTTY, WinSCP and FileZilla so that you
      don't need to enter the passphrase all the time.
   -  `Setting up a SSH proxy with
      PuTTY <\%22/client/windows/putty-proxy\%22>`__ to log on to a node
      protected by a firewall through another login node, e.g., to
      access the tier-1 system muk.
   -  `Creating a SSH tunnel using
      PuTTY <\%22/client/windows/creating-an-ssh-tunnel\%22>`__ to
      establish network communication between your local machine and the
      cluster otherwise blocked by firewalls.

-  Transfer data using Secure FTP (SFTP) clients:

   -  `FileZilla <\%22/client/windows/filezilla\%22>`__
   -  `WinSCP <\%22/client/windows/winscp\%22>`__

-  Display graphical programs:

   -  You can install a so-called X server:
      `Xming <\%22/client/windows/xming\%22>`__. X is the protocol that
      is used by most Linux applications to display graphics on a local
      or remote screen.
   -  On the KU Leuven/UHasselt clusters it is also possible to `use the
      NX Client <\%22/client/multiplatform/nx-start-guide\%22>`__ to log
      on to the machine and run graphical programs. Instead of an
      X-server, another piece of client software is needed. That
      software is currently available for Windows, OS X, Linux, Android
      and iOS.
   -  The KU Leuven/UHasselt and UAntwerp clusters also offer support
      for visualization software through TurboVNC. VNC renders images on
      the cluster and transfers the resulting images to your client
      device. VNC clients are available for Windows, macOS, Linux,
      Android and iOS.

      -  On the KU Leuven/UHasselt clusters, `TurboVNC is supported on
         the visualization
         nodes <\%22/client/multiplatform/turbovnc\%22>`__.
      -  On the UAntwerp clusters, TurboVNC is supported on all regular
         login nodes (without OpenGL support) and on the visualization
         node of Leibniz (with OpenGL support through VirtualGL). See
         the page \\"\ `Remote visualization @
         UAntwerp <\%22/infrastructure/hardware/hardware-ua/visualization\%22>`__\\"
         for instructions.

-  If you install the free `UNIX emulation layer
   Cygwin <\%22http://www.cygwin.com/\%22>`__ with the necessary
   packages, you can use the same OpenSSH client as on Linux systems and
   all pages about ssh and data transfer from `the Linux client
   pages <\%22/client/linux\%22>`__ apply.

Programming tools
-----------------

-  By installing the `UNIX emulation layer
   Cygwin <\%22https://www.cygwin.com/\%22>`__ with the appropriate
   packages you can mimic very well the VSC cluster environment (at
   least with the foss toolchain). Cygwin supports the GNU compilers and
   also contains packages for OpenMPI (`look for
   \\"openmpi\" <\%22https://cygwin.com/cgi-bin2/package-grep.cgi?grep=openmpi&arch=x86_64\%22>`__)
   and some other popular libraries (FFTW, HDF5, ...). As such it can
   turn your Windows PC in a computer that can be used to develop
   software for the cluster if you don't rely on too many external
   libraries (which may be hard to install). This can come in handy if
   you sometimes need to work off-line. If you have a 64-bit Windows
   system (which most recent computers have), it is best to go for the
   64-bit version of Cygwin. After all, the VSC-clusters are also
   running a 64-bit OS.
-  If you're running Windows 10 build 1607 (Anniversary Edition) or
   later, you may consider running the \\"\ `Windows Subsystem for
   Linux <\%22https://www.google.be/webhp?q=windows%20subsystem%20for%20linux\%22>`__\\"
   that will give you a Ubuntu-like environment on Windows and allow you
   to install some Ubuntu packages. *In build 1607 this is still
   considered experimental technology and we offer no support.*
-  `Microsoft Visual
   Studio <\%22/client/windows/microsoft-visual-studio\%22>`__ can also
   be used to develop OpenMP or MPI programs. If you do not use any
   Microsoft-specific libraries but stick to plain C or C++, the
   programs can be recompiled on the VSC clusters. Microsoft is slow in
   implementing new standards though. In Visual Studio 2015, OpenMP
   support is still stuck at version 2.0 of the standard. An alternative
   is to get a license for the Intel compilers which plug into Visual
   Studio and give you the best of both worlds, the power of a
   full-blown IDE and compilers that support the latest technologies in
   the HPC world on Windows.
-  Eclipse is a popular multi-platform Integrated Development
   Environment (IDE) very well suited for code development on clusters.

   -  Read our `Eclipse
      introduction <\%22/client/multiplatform/eclipse-intro\%22>`__ to
      find out why you should consider using Eclipse if you develop code
      and how to get it.
   -  You can use `Eclipse on the desktop as a remote editor for the
      cluster <\%22/client/multiplatform/eclipse-remote-editor\%22>`__.
   -  You can use `Eclipse on the desktop to access files in a
      subversion repository on the
      cluster <\%22/client/multiplatform/eclipse-vsc-subversion\%22>`__.
   -  You can combine the remote editor feature with version control
      from Eclipse, but some care is needed, and `here's how to do
      it <\%22/client/multiplatform/eclipse-ptp-versioncontrol\%22>`__.

   On Windows Eclipse relies by default on the cygwin toolchain for its
   compilers and other utilities, so you need to install that too.
-  Information on tools for version control (git and subversion) is
   available on the `\\"Version control systems\" introduction
   page <\%22/cluster-doc/development/version-control\%22>`__ on this
   web site.

   -  Information about `using the TortoiseSVN Subversion client with
      the VSC systems <\%22/client/windows/tortoisesvn\%22>`__.

"

.. |Windows| image:: windows_client_copy/windows.png
.. |Windows+Linux| image:: windows_client_copy/windows_with_linux.png

