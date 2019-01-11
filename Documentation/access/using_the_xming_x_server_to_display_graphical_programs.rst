Using the Xming X server to display graphical programs
======================================================

To display graphical applications from a Linux computer (such as the VSC
clusters) on your Windows desktop, you need to install an X Window
server. Here we describe the installation of Xming, one such server and
freely available.

Installing Xming
----------------

#. Download the Xming installer from `the XMing web
   site <\%22http://www.straightrunning.com/XmingNotes/\%22>`__.
#. Either install Xming from the **Public Domain Releases** (free) or
   from the **Website Releases** (after a donation) on the website.
#. Run the Xming setup program on your Windows desktop. Make sure to
   select 'XLaunch wizard' and 'Normal PuTTY Link SSH client'.
   |\\"Xming-Setup.png\"|

Running Xming:
--------------

#. To run Xming, select XLaunch from the Start Menu.
#. Select 'Multiple Windows'. This will open each application in a
   separate window.
   |\\"Xming-Display.png\"|
#. Select 'Start no client' to make XLaunch wait for other programs
   (such as PuTTY).
   |\\"Xming-Start.png\"|
#. Select 'Clipboard' to share the clipboard.
   |\\"Xming-Clipboard.png\"|
#. Finally save the configuration.
   |\\"Xming-Finish.png\"|
#. Now Xming is running ... and you can launch a graphical application
   in your PuTTY terminal. Do not forget to enable X11 forwarding as
   explained on `our PuTTY
   page <\%22/client/windows/console-putty\%22>`__.
   To test the connection, you can try to start a simple X program on
   the login nodes, e.g., xterm or xeyes. The latter will open a new
   window with a pair of eyes. The pupils of these eyes should follow
   your mouse pointer around. Close the program by typing \\"ctrl+c\":
   the window should disappear.
   If you get the error 'DISPLAY is not set', you did not correctly
   enable the X-Forwarding.

"

.. |\\"Xming-Setup.png\"| image:: \%22/assets/153\%22
.. |\\"Xming-Display.png\"| image:: \%22/assets/155\%22
.. |\\"Xming-Start.png\"| image:: \%22/assets/157\%22
.. |\\"Xming-Clipboard.png\"| image:: \%22/assets/159\%22
.. |\\"Xming-Finish.png\"| image:: \%22/assets/161\%22

