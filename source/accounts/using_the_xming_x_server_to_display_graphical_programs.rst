.. _Xming:

Using the Xming X server to display graphical programs
======================================================

To display graphical applications from a Linux computer (such as the VSC
clusters) on your Windows desktop, you need to install an X Window
server. Here we describe the installation of Xming, one such server and
freely available.

Installing Xming
----------------

#. Download the Xming installer from the `Xming website`_.

#. Either install Xming from the **Public Domain Releases** (free) or
   from the **Website Releases** (after a donation) on the website.

#. Run the Xming setup program on your Windows desktop. Make sure to
   select 'XLaunch wizard' and 'Normal PuTTY Link SSH client'.

.. figure:: using_the_xming_x_server_to_display_graphical_programs/xming_installation.png

Running Xming:
--------------

#. To run Xming, select XLaunch from the Start Menu.

#. Select 'Multiple Windows'. This will open each application in a
   separate window.

   .. figure:: using_the_xming_x_server_to_display_graphical_programs/xming_display_settings.png

#. Select 'Start no client' to make XLaunch wait for other programs
   (such as PuTTY).

   .. figure:: using_the_xming_x_server_to_display_graphical_programs/xming_session_type.png

#. Select 'Clipboard' to share the clipboard.

   .. figure:: using_the_xming_x_server_to_display_graphical_programs/xming_clipboard.png

#. Finally save the configuration.

   .. figure:: using_the_xming_x_server_to_display_graphical_programs/xming_save.png

#. Now Xming is running ... and you can launch a graphical application
   in your PuTTY terminal. Do not forget to enable X11 forwarding as
   explained on :ref:`our PuTTY page <text mode access using PuTTY>`.
   To test the connection, you can try to start a simple X program on
   the login nodes, e.g., xterm or xeyes. The latter will open a new
   window with a pair of eyes. The pupils of these eyes should follow
   your mouse pointer around. Close the program by typing \\"ctrl+c\":
   the window should disappear.
   If you get the error 'DISPLAY is not set', you did not correctly
   enable the X-Forwarding.

