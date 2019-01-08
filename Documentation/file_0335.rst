Linux client
============

Since all VSC clusters use Linux as their main operating system, you
will need to get acquainted with using the command-line interface and
using the terminal. To open a terminal in Linux when using KDE, choose
Applications > System > Terminal > Konsole. When using GNOME, choose
Applications > Accessories > Terminal.

If you don't have any experience with using the command-line interface
in Linux, we suggest you to read the `basic Linux
usage <\%22/cluster-doc/using-linux/basic-linux-usage\%22>`__ section
first.

Getting ready to request an account
-----------------------------------

-  Before requesting an account, you need to generate a pair of ssh
   keys. One popular way to do this on Linux is\ `using the freely
   available OpenSSH client <\%22/client/linux/keys-openssh\%22>`__
   which you can then also use to log on to the clusters.

Connecting to the cluster
-------------------------

-  Open a text-mode session using an SSH client:

   -  `OpenSSH ssh command <\%22/client/linux/login-openssh\%22>`__
   -  `Using ssh-agent <\%22/client/linux/ssh-agent\%22>`__ to avoid
      having to enter the passphrase all the time
   -  `Setting up a SSH proxy <\%22/client/linux/openssh-proxy\%22>`__
      to long on to a node by a firewall through another login node,
      e.g., to access the tier-1 system muk
   -  `Creating an SSH tunnel using
      OpenSSH <\%22/client/linux/creating-an-ssh-tunnel\%22>`__ to
      establish network communication between your local machine and the
      cluster otherwise blocked by firewalls.

-  Transfer data using Secure FTP (SFTP) with the `OpenSSH sftp and scp
   commands <\%22/client/linux/data-openssh\%22>`__.
-  Display programs that use graphics or have a GUI

   -  No extra software is needed on a Linux client system, but you need
      to use the appropriate options with the ssh command as explained
      on `the page on OpenSSH <\%22/client/linux/login-openssh\%22>`__.
   -  On the KU Leuven/UHasselt clusters it is also possible to `use the
      NX Client <\%22/client/multiplatform/nx-start-guide\%22>`__ to log
      on to the machine and run graphical programs. This requires
      additional client software that is currently available for
      Windows, OS X, Linux, Android and iOS. The advantage over
      displaying X programs directly on your Linux screen is that you
      can sleep your laptop, disconnect and move to another network
      without loosing your X-session. Performance may also be better
      with many programs over high-latency networks.
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

Software development
--------------------

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

-  Linux supports all popular version control systems. See `our
   introduction to version control
   systems <\%22https://www.vscentrum.be/cluster-doc/development/version-control\%22>`__.

   -  Specific instructions to `access subversion repositories on the
      VSC clusters or other servers from your desktop with UNIX-style
      command line
      tools <\%22https://www.vscentrum.be/client/multiplatform/desktop-access-vsc-subversion\%22>`__.

"
