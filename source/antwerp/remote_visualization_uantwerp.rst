.. _remote visualization UAntwerp:

Remote visualization @ UAntwerp
===============================

The UAntwerp clusters have limited features for remote visualization on
the login nodes of the clusters and the visualization node of Leibniz using a
`VNC-based remote display technology <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`_.
On the regular login nodes of the clusters, there is no acceleration of 3D
graphics. However, the visualization node of Leibniz is equipped with a
NVIDIA P5000 card that, when used properly, will offer accelerated
rendering of OpenGL applications.

.. note::
   Using VNC is a good solution for those who absolutely need a
   GUI tool or a visualization tool on the cluster rather than on your local
   desktop. It is not a good solution for those who don't want to invest in
   learning Linux properly and are only looking for the ease-of-use of a PC.

Prerequisites
-------------

You'll need an ssh client on your desktop that provides port forwarding
functionality on your desktop. We refer to the :ref:`access methods`
section for information about ssh clients for various client operating systems.
PuTTY (Windows) and OpenSSH (macOS, Linux, UNIX-compatibility environment on
Windows) both provide all required functionality.

Furthermore, you'll need a VNC client. In theory, using the TurboVNC client should result
in the least problems, as that is made by the same people as the server we use.

.. tab-set::

   .. tab-item:: Windows

      We have tested the setup with four different clients:

      - The TurboVNC client can be downloaded by following the Downloads link
        on the `TurboVNC`_ web site, which will lead you to `TurboVNC download page`_.
        Binaries are available for both 32-bit and 64-bit Windows systems.

      - `TigerVNC`_ is a client whose development is supported by the Swedish
        company Cendio who makes a remote display server product (ThinLinc) based on
        TigerVNC. Binaries for 32-bit and 64-bit windows (``vncviewer(64)-*.*.*.exe``) can
        be downloaded by following the link on
        `the GitHub Releases page <https://github.com/TigerVNC/tigervnc/releases>`_.
        These binaries are ready-to-run.

      - `TightVNC <http://www.tightvnc.com/>`_ is also a popular free VNC
        implementation. 32-bit and 64-bit Windows installers can be downloaded from
        `the download page on their website <http://www.tightvnc.com/download.php>`_.
        When installing on your PC or laptop, make sure to choose the "custom
        install" and only install the TightVNC Viewer.

      - `MobaXterm`_ also has an integrated VNC viewer. 
        With that viewer it is possible to build the tunnel in the 
        network settings of the VNC connection.

      All four viewers are quite fast and offer good performance, even when
      run from home over a typical broadband internet connection. TigerVNC
      seems to be a bit quicker than the others, while TightVNC and MobaXterm don't
      allow you to resize your window. With the other two implementations,
      when you resize your desktop window, the desktop is also properly
      resized.

   .. tab-item:: macOS

      Here also there are several possible setups:
      
      - The TurboVNC client can be downloaded from the `TurboVNC`_ web
        site. The macOS client is Java-based. It requires Oracle Java 
        (which you will need to install if it is not yet on your system).
      
      - `TigerVNC`_, a client whose development is supported by the Swedish company
        Cendio who makes a remote display server product (ThinLinc) based on
        TigerVNC, is a native macOS client. Some places report that this client is a
        lot slower than the TurboVNC one on macOS.
        Binaries are available by following the link on
        `the GitHub Releases page <https://github.com/TigerVNC/tigervnc/releases>`_.
        Look for the ``tigervnc-*.dmg`` files, which contrary to those for
        Windows and Linux, only contain the viewer software.
      
      - A not-so-good alternative is to use the Apple Screen Sharing feature
        which is available through Finder (Command-K key combination) or
        Safari (URL bar) by specifying the server as a URL starting with
        vnc://. The port number is 5900 + the number of the VNC server if you 
        follow the scheme below to start an application in a VNC session.
        For example, with port tunnelling and a VNC server with number 2, the server
        address will be ``vnc://localhost:5902``.
        This VNC client is considerably slower though than the
        TurboVNC client, partly because it doesn't support some of the
        TurboVNC-specific compression algorithms.

   .. tab-item:: Linux

      RPM and Debian packages for TurboVNC can be downloaded from the
      `TurboVNC`_ web site and are available in some Linux distributions. 
      You can also try another VNC client provided by your Linux distribution, 
      although we cannot guarantee those will work with our TurboVNC server.

How do I run an application with TurboVNC?
------------------------------------------

Running an application with TurboVNC requires 3 steps:

1. Start the VNC server on the cluster
2. Start the VNC client on your desktop/laptop and connect to the server
3. Start your application

Step 1: Starting the VNC server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log on in the regular way to one of the regular login nodes or to
   the visualization node of Leibniz. Note that the latter should only
   be used for running demanding visualizations that benefit from the 3D
   acceleration. The node is not meant for those who just want to run
   some lightweight 2D GUI application, e.g., an editor with GUI.
2. Load the module vsc-vnc:

   .. code:: bash

      module load vsc-vnc
3. Use the wrapper script to start the VNC server
   and the `Xfce <https://xfce.org/>`_ desktop environment:

   .. code:: bash

       vnc-xfce
4. The first time you use VNC, it will ask you to create a password.

   .. note::
     For security reasons, please use a password that you don't use for
     anything else. If you have forgotten your password, it can easily be
     changed with the ``vncpasswd`` command and is stored in the file
     ``~/.vnc/passwd`` in encrypted form. It will also ask you for a
     viewer-only password. If you don't know what this is, you don't need it.
5. Among other information, the VNC server will show a line similar to::

    Desktop 'TurboVNC: viz1.leibniz:2 (vsc20XXX)' started on display viz1.leibniz:2
   
   Note the number after `TurboVNC: viz1.leibniz`, in this case 2. This is
   the number of your VNC server, and it will in general be the same as
   the X display number which is the last number on the line. You'll
   need that number to connect to the VNC server.
6. |Optional| It is now safe to log out from your SSH
   session. The VNC server will continue running in the background.

Step 2: Connecting to the server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In most cases, you will not be able to connect directly to the TurboVNC
server. Instead, you will need to create an SSH tunnel to forward
traffic to the VNC server. The exact procedure is explained at length
in the pages ":ref:`ssh tunnel using PuTTY`" (for Windows) 
and ":ref:`tunnel OpenSSH`" (for Linux and macOS).

In the following example, we assume the VNC server was started with number 2, 
running on port 5902 (VNC's default port 5900 + your server number).

1. First, setup an SSH tunnel. 

   In theory, you can create an SSH tunnel 
   from any port number on your local machine to the port number on the node 
   running the VNC server. However, it is easier to use the same port number 
   on both ends of the tunnel.
   
   .. warning:: 
     Avoid using the generic login names here, as that may result in an SSH tunnel 
     to a different login node as the one running your VNC server. 
     Instead, use the full names for the specific nodes, e.g.,
     viz1-leibniz.hpc.uantwerpen.be, login2-leibniz.hpc.uantwerpen.be or
     login1-vaughan.hpc.uantwerpen.be.

   .. tab-set::

      .. tab-item:: OpenSSH 
         
         For a VNC server started with number 2 on the visualization node,
         your command will look like

         .. code:: bash

            ssh -L 5902:localhost:5902 -N vsc20XXX@viz1-leibniz.hpc.uantwerpen.be

         The above line assumes that you log on to the node where the VNC
         server is running, which is why we can use ``localhost`` in the 
         ``-L``-line (as this is the name under which the node running the 
         VNC server is known on that node).

      .. tab-item:: PuTTY

         Select \"Connections - SSH - Tunnel\" in the left pane.
         As \"Source port\", use 5900 + the server number (5902 in our
         example).
         As destination, use the full name of the node on which the
         VNC server is running, e.g., viz1-leibniz.hpc.uantwerpen.be,
         or localhost if you will log on to the node running the VNC server.


2. Start your VNC client once your tunnel is up-and-running. The 
   procedure depends on the precise client you are using. 
   
   In general, the client will ask for the VNC server address. 
   The server address is ``localhost:x`` where ``x`` is the number of your VNC server 
   (2 in the example above). Some clients also allow you to use the port number instead
   (``localhost:5902`` for the example above), and will automatically assume that 
   bigger numbers are port numbers.
  
   The client will then ask you for the password that you have assigned
   when you first started a VNC server.
3. You should now get a window with the desktop
   environment that you have chosen when starting the VNC server

   .. note::
      The first time that you start a Xfce session with TurboVNC,
      you'll see a panel "Welcome to the first start of the panel". 
      You may want to select "Use default config", as otherwise you 
      get a very empty desktop.

Step 3: Starting an application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open a terminal window in the VNC session.
   In the default Xfce-environment, you can open a terminal window by selecting
   \"Terminal Emulator\" in the \"Applications\" menu in the top left.
   The first time it will let you choose between selected terminal
   applications.
2. Load the modules that are required to start your application of
   choice.
3. 2D applications or applications that use a software renderer for 3D
   start as usual. However, to start an application using the
   hardware-accelerated OpenGL, you'll need to start it through
   ``vglrun``. This will use `VirtualGL`_ to redirect the OpenGL calls
   to your VNC server's display. 

   Adding ``vglrun`` at the start of the command line is usually sufficient.

   .. note:: For a quick test of your setup, enter

      .. code:: bash

         vglrun glxinfo
         vglrun glxgears

      The first command will print some information about the OpenGL
      functionality that is supported. The second command will display a set
      of rotating gears. Don't be fooled if they appear to stand still but
      look at the \"frames per second\" printed in the terminal window.

   However, this doesn't work with all applications. Some applications, like MATLAB,
   might require a special setup.

   |Example| Start MATLAB with hardware-accelerated OpenGL with ``-nosoftwareopengl`` as follows:

    .. code:: bash
 
       vglrun matlab -nosoftwareopengl
    
    The MATLAB command ``opengl info`` will then show that you are
    indeed using the GPU.

4. When you've finished, don't forget to log out in the Xfce desktop 
   (right mouse click in the desktop, then select \"Application\"
   and then select \"Log Out\") when you use one of
   our wrapper scripts or kill the VNC server otherwise using

   .. code:: bash

      vncserver -kill :x
       
   with ``x`` the number of the server.

.. warning::
   Do not forget to close your tunnel when you log out from the VNC
   server. Otherwise the next user might not be able to connect.

Common problems
~~~~~~~~~~~~~~~

- Authentication fails when connecting to the server
   This happens
   occasionally when switching between different versions of TurboVNC.
   The easiest solution is to simply kill the VNC server using
   ``vncserver -kill :x`` (with x the display number), set a new VNC
   password using ``vncpasswd`` and start over again.
- Xfce doesn't show the task bar at the top of the screen
   This sometimes happens when switching between versions of Xfce4, or you
   may have screwed up your configuration in another way. Remove the
   ``.config/xfce-centos7`` directory (``rm -r .config/xfce-centos7``),
   kill the VNC server and start again.
