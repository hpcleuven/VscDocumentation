.. _Windows client:

Windows client
==============

Getting ready to request an account
-----------------------------------

-  Before requesting an account, you need to generate a pair of ssh
   keys. One popular way to do this on Windows is using the freely
   available `PuTTY`_ client which you can then also use to log on to
   the clusters.

Connecting to the cluster
-------------------------

-  Open a text-mode session using an ssh client

   -  :ref:`PuTTY <text mode access using PuTTY>` is a
      simple-to-use and freely available GUI SSH client for Windows.
   -  :ref:`Pageant <using Pageant>` can be used to
      manage active keys for PuTTY, WinSCP and FileZilla so that you
      don't need to enter the passphrase all the time.
   -  :ref:`Setting up a SSH proxy with PuTTY <ssh proxy with PuTTY>`
      to log on to a node
      protected by a firewall through another login node, e.g., to
      access the tier-1 system muk.
   -  :ref:`Creating a SSH tunnel using PuTTY <ssh tunnel using PuTTY>` to
      establish network communication between your local machine and the
      cluster otherwise blocked by firewalls.

-  Transfer data using Secure FTP (SFTP) clients:

   -  :ref:`FileZilla <FileZilla>`
   -  :ref:`WinSCP <winSCP>`

-  Display graphical programs:

   -  You can install a so-called X server: :ref:`Xming<Xming>`.
      X is the protocol that is used by most Linux applications to display
      graphics on a local or remote screen.
   -  On the KU Leuven/UHasselt clusters it is also possible to use the
      :ref:`NX Client<NX start guide>` to log
      on to the machine and run graphical programs. Instead of an
      X server, another piece of client software is needed. That
      software is currently available for Windows, macOS, Linux, Android
      and iOS.
   -  The KU Leuven/UHasselt and UAntwerp clusters also offer support
      for visualization software through TurboVNC. VNC renders images on
      the cluster and transfers the resulting images to your client
      device. VNC clients are available for Windows, macOS, Linux,
      Android and iOS.

      -  On the KU Leuven/UHasselt clusters, :ref:`TurboVNC<TurboVNC start guide>`
         is supported on the visualization nodes.
      -  On the UAntwerp clusters, TurboVNC is supported on all regular
         login nodes (without OpenGL support) and on the visualization
         node of Leibniz (with OpenGL support through VirtualGL). See
         the page ":ref:`Remote visualization UAntwerp`"
         for instructions.

-  If you install the free `UNIX emulation layer Cygwin <Cygwin>`_
   with the necessary
   packages, you can use the same OpenSSH client as on Linux systems and
   all pages about ssh and data transfer from :ref:`the Linux client
   pages <Linux client>` apply.

Programming tools
-----------------

-  By installing the `UNIX emulation layer Cygwin <Cygwin>`_
   with the appropriate
   packages you can mimic very well the VSC cluster environment (at
   least with the foss toolchain). Cygwin supports the GNU compilers and
   also contains packages for OpenMPI (`look for
   "openmpi" <https://cygwin.com/cgi-bin2/package-grep.cgi?grep=openmpi&arch=x86_64>`_)
   and some other popular libraries (FFTW, HDF5, ...). As such it can
   turn your Windows PC in a computer that can be used to develop
   software for the cluster if you don't rely on too many external
   libraries (which may be hard to install). This can come in handy if
   you sometimes need to work off-line. If you have a 64-bit Windows
   system (which most recent computers have), it is best to go for the
   64-bit version of Cygwin. After all, the VSC-clusters are also
   running a 64-bit OS.
-  If you're running Windows 10 build 1607 (Anniversary Edition) or
   later, you may consider running the "`Windows Subsystem for
   Linux <https://www.google.be/webhp?q=windows%20subsystem%20for%20linux>`_"
   that will give you a Ubuntu-like environment on Windows and allow you
   to install some Ubuntu packages. *In build 1607 this is still
   considered experimental technology and we offer no support.*
-  :ref:`Microsoft Visual Studio <MS Visual Studio>` can also
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

   On Windows Eclipse relies by default on the `Cygwin`_ toolchain for its
   compilers and other utilities, so you need to install that too.
-  Information on tools for version control (git and subversion) is
   available on the :ref:`version control systems` introduction page.

   -  Information about :ref:`using the TortoiseSVN Subversion client with
      the VSC systems <TortoiseSVN>`.

.. |Windows| image:: windows_client/windows.png
.. |Windows+Linux| image:: windows_client/windows_with_linux.png

.. include:: links.rst
