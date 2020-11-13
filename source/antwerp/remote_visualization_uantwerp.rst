.. _remote visualization UAntwerp:

.. role:: bash(code)
    :language: bash

Remote visualization @ UAntwerp
===============================

The UAntwerp clusters have limited features for remote visualization on
the login nodes of the clusters and the visualization node of leibniz using a
`VNC-based remote display
technology <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`_.
On the regular login nodes of the clusters, there is no acceleration of 3D
graphics, but the visualisation node of leibniz is equipped with a
NVIDIA P5000 card that when used properly will offer accelerated
rendering of OpenGL applications. The setup is similar to the setup of
:ref:`the visualization nodes at the KU Leuven <TurboVNC>`.

*Using VNC turns out to be more complicated than one would think and
things sometimes go wrong. It is a good solution for those who
absolutely need a GUI tool or a visualization tool on the cluster rather
than on your local desktop; it is not a good solution for those who
don't want to invest in learning Linux properly and are only looking for
the ease-of-use of a PC.*

The idea behind the setup
-------------------------

2D and 3D graphics on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Graphics (local and remote) on Linux-machines is based on the `X Window
System version
11 <https://en.wikipedia.org/wiki/X_Window_System>`_, shortly
X11. This technology is pretty old (1987) and nor really up to the task
anymore with today's powerful computers yet has so many applications that
support it that it is still the standard in practice (though there are
efforts going on to replace it with Wayland on modern Linux systems).

X11 applications talk to an X server which draws the commands on your
screen. These commands can go over a network so applications on a remote
machine can draw on your local screen. Note also the somewhat confusing
terminology: The server is the program that draws on the screen and thus
runs on your local system (which for other applications will usually be
called the client) while the application is called the client (and in
this scenario runs on a computer which you will usually call the
server). However, partly due to the way the X11 protocol works and
partly also because modern applications are very graphics-heavy, the
network has become a bottleneck and graphics-heavy applications (e.g.,
the MATLAB GUI) will work sluggish on all but the lowest latency network
connections.

X11 is a protocol for 2D-graphics only. However, it is extensible. Enter
`OpenGL <https://en.wikipedia.org/wiki/OpenGL>`_, a standard
cross-platform API for professional 3D-graphics. Even though its
importance on Windows and macOS platforms had decreased as Microsoft and
Apple both promote their own APIs (DirectX and Metal respectively), it
is still very popular for professional applications and in the Linux
world. It is supported by X11 servers through `the
GLX-extension <https://en.wikipedia.org/wiki/GLX>`_ (OpenGL for
the X Window System). When set up properly, OpenGL commands can be
passed to the X server and use any OpenGL graphics accelerator available
on the computer running the X server. In principle, if you have a X
server with GLX extension on your desktop, you should be able to run
OpenGL programs on the cluster and use the graphics accelerator of your
desktop to display the graphics. In practice however this works well
when the application and X server run on the same machine, but the
typical OpenGL command stream is to extensive to work well over a
network connection and performance will be sluggish.

Optimizing remote graphics
~~~~~~~~~~~~~~~~~~~~~~~~~~

The solution offered on the visualization node of leibniz (and in a
reduced setting on the regular login nodes of the clusters) consists 
of two elements to deal with the issues of network bandwidth and, more 
importantly, network latency.

`VirtualGL <https://en.wikipedia.org/wiki/VirtualGL>`_ is a
technology that redirects OpenGL commands to a 3D graphics accelerator
on the computer where the application is running or to a software
rendering library. It then pushes the rendered image to the X server.
Instead of a stream of thousands or millions of OpenGL commands, one
large image is now passed over the network to the X server, reducing the
effect of latency. These images can be large though, but with an
additional piece of software on your client, called the VGL client,
VirtualGL can send the images in compressed form which strongly reduces
the bandwidth requirements. To use VirtualGL, you have to start the
OpenGL application through the vglrun-command. That command will set up
the application to redirect OpenGL calls to the VirtualGL libraries.

VirtualGL does not solve the issue of slow 2D-rendering because of
network latency and also requires the user to set up a VGL client and an
X server on the local desktop, which is cumbersome for less experienced
users. We solve this problem through `VNC (Virtual Network
Computing) <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`_.
VNC consists of three components: a server on the computer where your
application runs, a client on your desktop, and a standardized protocol
for the communication between server and client. The server renders the
graphics on the computer on which it runs and sends compressed images to
the client. The client of course takes care of keyboard and mouse input
and sends this to the server. A VNC server for X applications will in
fact emulate an X server. Since the protocol between client and server is
pretty standard, most clients will work with most servers, though some
combinations of client and server will be more efficient because they
may support a more efficient compression technology. Our choice of
server is `TurboVNC`_ which is
maintained by the same group that also develops VirtualGL and has an
advanced implementation of a compression algorithm very well suited for
3D graphics. TurboVNC has clients for Windows, macOS and Linux. However,
our experience is that it also works with several other VNC clients
(e.g., Apple Remote Desktop), though it may be a bit less efficient as
it may not be able to use the best compression strategies.

The concept of a Window Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When working with Windows or macOS, we're used to seeing a title bar for
most windows with buttons to maximize or hide the window, and borders
that allow to resize a window. You'd think this functionality is
provided by the X server, but in true UNIX-spirit of having separate
components for every bit of functionality, this is not the case. On X11,
this functionality is provided by the Window Manager, a separate
software package that you start after starting the X server (or may be
started for you automatically by the start-up script that is run when
starting the X server). The basic window managers from the early days of
X11 have evolved into feature-rich desktop environments that do not only
offer a window manager, but also a task bar etc. Gnome and KDE are
currently the most popular desktop environments. However, these require
a lot of resources and are difficult to install on top of TurboVNC.
Examples of very basic old-style window managers are the `Tab Window
Manager <https://en.wikipedia.org/wiki/Twm>`_ (command ``twm``)
and the `Motif Window
Manager <https://en.wikipedia.org/wiki/Motif_Window_Manager>`_
(command ``mwm``).

For the remote visualization setup on the UAntwerp clusters, we have
chosen to use the Xfce Desktop Environment which is definitely more
user-friendly than the rather primitive Tab Window Manager and Motif
Window Manager yet requires less system resources and is easier to set
up than the more advanced Gnome and KDE desktops.

Prerequisites
-------------

You'll need an ssh client on your desktop that provides port forwarding
functionality on your desktop. We refer to the :ref:`access and data transfer`
section for information about ssh clients for various client operating systems.
PuTTY (Windows) and OpenSSH (macOS, Linux, UNIX-compatibility environment on
Windows) both provide all required functionality.

Furthermore, you'll need a VNC client, preferably the TurboVNC client.

Windows
~~~~~~~

We have tested the setup with four different clients:

-  The TurboVNC client can be downloaded by following the Download link
   on the `TurboVNC`_ web site (which at the moment of
   writing this documentation takes you to a Sourceforge
   `TurboVNC download page`_).
   Binaries are available for both 32-bit and 64-bit windows systems.
   This client is made by the same people as the server we use so in
   theory one should expect the least problems with this setup.
-  `TigerVNC <http://tigervnc.org/>`_ is a client whose
   development is supported by the Swedish company Cendio who makes a
   remote display server product (ThinLinc) based on TigerVNC. Binaries
   for 32-bit and 64-bit windows (``vncviewr-*.*.*.exe``) can be downloaded
   by following the link on `the GitHub Releases
   page <https://github.com/TigerVNC/tigervnc/releases>`_.
   These binaries are ready-to-run.
-  `TightVNC <http://www.tightvnc.com/>`_ is also a popular
   free VNC implementation. 32-bit and 64-bit Windows installers can be
   downloaded from `the download page on their
   website <http://www.tightvnc.com/download.php>`_. When
   installing on your PC or laptop, make sure to chose the "custom
   install" and only install the TightVNC Viewer.
-  `MobaXterm <https://mobaxterm.mobatek.net/>`_ also has an integrated VNC viewer. 
   With that viewer it is possible to build the tunnel in the 
   network settings of the VNC connection.

All four viewers are quite fast and offer good performance, even when
run from home over a typical broadband internet connection. TigerVNC
seems to be a bit quicker than the others, while TightVNC and MobaXterm don't
allow you to resize your window. With the other two implementations,
when you resize your desktop window, the desktop is also properly
resized.

macOS
~~~~~

Here also there are several possible setups:

-  The TurboVNC client can be downloaded from the `TurboVNC`_ web
   site. The macOS client is
   Java-based. It requires Oracle Java (which you will need to install if
   it is not yet on your system).
-  `TigerVNC <https://tigervnc.org/>`_, a client whose
   development is supported by the Swedish company Cendio who makes a
   remote display server product (ThinLinc) based on TigerVNC, is a
   native macOS client. Some places report that this client is a lot
   slower than the TurboVNC one on macOS.
   `Binaries are available <https://bintray.com/tigervnc/stable/tigervnc/>`_.
   Look for the ``tigervnc-*.dmg`` files, which contrary to those for
   Windows and Linux, only contain the viewer software.
-  A not-so-good alternative is to use the Apple Screen Sharing feature
   which is available through the Finder (command-K key combination) or
   Safari (URL bar) by specifying the server as a URL starting with
   vnc://. You also have to use the port number on the local host
   to access the screen rather than the screen number.
   The port number is 5900 + the number of the VNC server if you 
   follow the scheme below to
   start an application in a VNC session. So the full URL will be
   ``vnc://localhost:5901`` for VNC server 1.
   This VNC client is considerably slower though than the
   TurboVNC client, partly because it doesn't support some of the
   TurboVNC-specific compression algorithms.

Linux
~~~~~

RPM and Debian packages for TurboVNC can be downloaded from the
`TurboVNC`_ web site and are
available in some Linux distributions. You can also try another VNC
client provided by your Linux distribution at your own risk as we cannot
guarantee that all VNC viewers (even recent ones) work efficiently with
TurboVNC.

How do I run an application with TurboVNC?
------------------------------------------

Running an application with TurboVNC requires 3 steps:

#. Start the VNC server on the cluster
#. Start the VNC client on your desktop/laptop and connect to the server
#. Start your application

Step 1: Starting the VNC server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Log on in the regular way to one of the regular login nodes or to
   the visualization node of Leibniz. Note that the latter should only
   be used for running demanding visualizations that benefit from the 3D
   acceleration. The node is not meant for those who just want to run
   some lightweight 2D GUI application, e.g., an editor with GUI.
#. Load the module vsc-vnc:

       :bash:`module load vsc-vnc`
       
   This module does not only put the TurboVNC server in the path, but
   also provides wrapper scripts to start the VNC server with a
   supported window manager / desktop environment. Try
   
       :bash:`module help vsc-vnc` 
       
   for more info about the specific wrappers.
#. Use your wrapper of choice to start the VNC server. We encourage to
   use the one for the Xfce desktop environment:
   
       :bash:`vnc-xfce`

   Other wrapper scripts may or may not be available on the system.       
#. The first time you use VNC, it will ask you to create a password. For
   security reasons, please use a password that you don't use for
   anything else. If you have forgotten your password, it can easily be
   changed with the ``vncpasswd`` command and is stored in the file
   ``~/.vnc/passwd`` in encrypted form. It will also ask you for a
   viewer-only password. If you don't know what this is, you don't need
   it.
#. Among other information, the VNC server will show a line similar to:

       ``Desktop 'TurboVNC: viz1.leibniz:2 (vsc20XXX)' started on display viz1.leibniz:2``
   
   Note the number after TurboVNC:viz1.leibniz, in this case 2. This is
   the number of your VNC server, and it will in general be the same as
   the X display number which is the last number on the line. You'll
   need that number to connect to the VNC server.
#. It is in fact safe though not mandatory to log out now from your SSH
   session as the VNC server will continue running in the background.

The standard way of starting a VNC server as described in the TurboVNC
documentation is by using the ``vncserver`` command. However, you should
only use this command if you fully understand how it works and what it
does. Also, please don't forget to kill the VNC server when you have
finished using it as it will not be killed automatically when started
through this command (or use the ``-autokill`` command line option at
start-up). The default start-up script (``xstart-up.turbovnc``) which will
be put in the ``~/.vnc`` directory on first use does not function
properly on our systems. We know this and we have no intent to repair
this as we prefer to install the vncserver command unmodified from the
distribution and provide wrapper scripts instead that use working
start-up files.

Step 2: Connecting to the server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In most cases, you'll not be able to connect directly to the TurboVNC
   server (which runs on port 5900 + the server number, 5902 in the
   above example) but you will need to create a SSH tunnel to forward
   traffic to the VNC server. The exact procedure is explained in length
   in the pages ":ref:`ssh tunnel using PuTTY`" (for
   Windows) and ":ref:`tunnel OpenSSH`" (for or Linux and macOS) .
   The easiest thing to do is to tunnel port number (5900 + server number) (5902 in the
   example above) on your local machine to the same port number on the
   node on which the VNC server is running, but you can use another port 
   number on your local machine. You cannot use the generic
   login names (such as login.hpc.uantwerpen.be) for that as you may be
   assigned a different login node as you were assigned just minutes
   ago. Instead, use the full names for the specific nodes, e.g.,
   viz1-leibniz.hpc.uantwerpen.be, login2-leibniz.hpc.uantwerpen.be or
   login1-vaughan.hpc.uantwerpen.be.

   #. In brief: With OpenSSH, your command will look like
   
          :bash:`ssh -L 5902:localhost:5902 -N vsc20XXX@viz1-leibniz.hpc.uantwerpen.be`

      The above line assumes that you log on to the node where the VNC
      server is running, which is why we can use ``localhost`` in the 
      ``-L``-line (as this is the name under which the node running the 
      VNC server is known on that node).      
   #. In PuTTY, select \"Connections - SSH - Tunnel\" in the left pane.
      As \"Source port\", use 5900 + the server number (5902 in our
      example) and as destination the full name of the node on which the
      VNC server is running, e.g., viz1-leibniz.hpc.uantwerpen.be,
      or localhost if you will log on to the node running the VNC server.

#. Once your tunnel is up-and-running, start your VNC client. The
   procedure depends on the precise client you are using. However, in
   general, the client will ask for the VNC server. That server is
   localhost:x where x is the number of your VNC server, 2 in the above
   example. It will then ask you for the password that you have assigned
   when you first started VNC. (Instead of using the screen number
   most VNC clients will also allow you to use the port number instead.)
   Some clients also allow you to use the port number instead of the
   server number and will automatically assume that bigger numbers
   are port numbers.
#. If all went well, you will now get a window with the desktop
   environment that you have chosen when starting the VNC server
#. Do not forget to close your tunnel when you log out from the VNC
   server. Otherwise the next user might not be able to connect.

*Note that the first time that you start a Xfce session with TurboVNC,
you'll see a panel "Welcome to the first start of the panel". Please
select "Use default config" as otherwise you get a very empty
desktop.*

Step 3: Starting an application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open a terminal window (if one was not already created when you
   started your session).
   In the default Xfce-environment, you can open a terminal by selecting
   \"Terminal Emulator\" in the \"Applications\" menu in the top left.
   The first time it will let you choose between selected terminal
   applications.
#. Load the modules that are required to start your application of
   choice.
#. 2D applications or applications that use a software renderer for 3D
   start as usual. However, to start an application using the
   hardware-accelerated OpenGL, you'll need to start it through
   ``vglrun``. Usually adding ``vglrun`` at the start of the command
   line is sufficient.
   This however doesn't work with all applications. Some applications
   require a special setup.

   #. MATLAB: start MATLAB with the ``-nosoftwareopengl`` option to
      enable accelerated OpenGL:
      
          :bash:`vglrun matlab -nosoftwareopengl`
      
      The MATLAB command ``opengl info`` will then show that you are
      indeed using the GPU.

#. When you've finished, don't forget to log out in the Xfce desktop 
   (right mouse click in the desktop, then select `"Application\"
   and then select \"Log Out\") when you use one of
   our wrapper scripts or kill the VNC server otherwise (using
   
       :bash:`vncserver -kill :x` 
       
   with ``x`` the number of the server).

Note: For a quick test of your setup, enter

.. code:: bash

   vglrun glxinfo
   vglrun glxgears

The first command will print some information about the OpenGL
functionality that is supported. The second command will display a set
of rotating gears. Don't be fooled if they appear to stand still but
look at the \"frames per second\" printed in the terminal window.

Common problems
~~~~~~~~~~~~~~~

-  Authentication fails when connecting to the server: This happens
   occasionally when switching between different versions of TurboVNC.
   The easiest solution is to simply kill the VNC server using
   ``vncserver -kill :x`` (with x the display number), set a new VNC
   password using ``vncpasswd`` and start over again.
-  Xfce doesn't show the task bar at the top of the screen: This too
   happens sometimes when switching between versions of Xfce4, or you
   may have screwed up your configuration in another way. Remove the
   ``.config/xfce-centos7`` directory (``rm -r .config/xfce-centos7``),
   kill the VNC server and start again.

Links
-----

Components used in the UAntwerp setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The `TurboVNC`_ web site, where you'll find downloads for Linux,
   Windows and macOS
-  The `VirtualGL <https://www.turbovnc.org/>`_ web site 
-  The `Xfce <https://xfce.org/>`_  web site and some
   `background material in Wikipedia <https://en.wikipedia.org/wiki/Xfce>`_

Related technologies
~~~~~~~~~~~~~~~~~~~~

-  `The Gnome web site <https://www.gnome.org/>`_ and `some
   background in Wikipedia <https://en.wikipedia.org/wiki/GNOME>`_
-  `The KDE web site <https://www.kde.org/>`_ and `some
   background in Wikipedia <https://en.wikipedia.org/wiki/KDE>`_
-  `The Tab Window Manager (sometimes called Tom's Window Manager) on
   Wikipedia <https://en.wikipedia.org/wiki/Twm>`_.
-  `The Motif Window Manager on Wikipedia
   <https://en.wikipedia.org/wiki/Motif_Window_Manager>`_.

.. include:: ../access/links.rst
