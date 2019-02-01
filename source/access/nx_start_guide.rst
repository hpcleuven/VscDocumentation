.. _NX start guide:

NX start guide
==============

Installing NX NoMachine client
------------------------------

-  Download the enterprise version of the client from
   the `NX Client download`_ page.
-  Continue with Configuration of your NoMachine NX client.

NoMachine NX Client Configuration Guide
---------------------------------------

NoMachine NX requires keys in OpenSSH format, therefore the existing key
needs to be :ref:`converted into OpenSSH format <converting PuTTY keys>` if
you're working on Windows and using PuTTY.

Start the NoMachine client and press twice continue to see the screen
with connection. Press **New** to create a new connection.

Change the Protocol to **SSH**.

Choose the hostname:

-  **for ThinKing (Tier-2): nx.hpc.kuleuven.be** and port **22**.
-  **for BrENIAC (Tier-1): login2-tier1.hpc.kuleuven.be** and port
   **22**.
-  If you experience problems with connection please switch to Protocol
   NX and port 4000.

Choose the authentication **Use the system login.**

Choose the authentication method **Private key.**

Browse your private key. This should be in OpenSSH format (not .ppk).

-  For Android users it is easy to transfer your key and save it in the
   chosen location with the Box (KU Leuven) or Dropbox (UHasselt) apps.
-  For iOS users (iPad running iOS 5 or later) it is possible to
   transfer the key with iTunes. Connect your device through iTunes, go
   to the connected device, choose the \\"apps\" tab, scroll down to
   \\"file sharing\". Select the NoMachine client and add files to
   NoMachine Documents. Remember to Sync your device.
-  Browse your file on a mobile device from the given location.

Choose the option Don’t use proxy for the network connection.

Give the name to your connection, e.g. *Connection to
nx.hpc.kuleuven.be*. You can optionally create the link to that
connection on your desktop. Click the \\"Done\" button to finish
configuration.

Choose the just created connection and press \\"Connect\".

Enter your username (**vsc-account**) and **passphrase** for your
private key and press "ok".

If you are creating for the first time choose **New desktop**. Otherwise
please go to step 16 for instructions how to reconnect to your session.

Choose **Create a new virtual desktop** and continue. Each user is
allowed to have a maximum 5 desktops open.

Read the useful information regarding your session displayed on several
screens. This step is very important in case of mobile devices – once
you miss the instructions it is not so easy to figure out how to operate
NoMachine on your device. You can optionally choose not to show these
messages again.

Once connected you will see the virtual Linux desktop.

When **reconnecting** choose your desktop from all the listed ones. If
there are too many you can use the option **find a user or a desktop**
and type your username (vsc-account). Once you found your desktop press
**connect**.

You will be prompted about the screen resolution (**Change the server
resolution to match the client when I connect**) which can be changed to
match the client when you connect. It is a recommended setup as your
session will correspond to your actual device resolution. While
reconnection from a different device (e.g. mobile device) it is highly
recommended to change the resolution.

For more detailed information about the configuration process please
refer to the `short video <https://www.vscentrum.be/assets/1187>`_ (ThinKing
configuration) showing the installation and configuration procedure
step-by-step or to the :download:`document containing graphical
instructions <nx_start_guide/nx_config_guide.pdf>`.

How to start using NX on ThinKing?
----------------------------------

#. Once your desktop is open, you can use all available GUI designed
   software that is listed within the Applications menu. Software is
   divided into several groups:

   -  Accessories (e.g. Calculator, Character Map, Emacs, Gedit, GVim),
   -  Graphics (e.g. gThumb Image Viewer, Xpdf PDF Viewer),
   -  Internet (e.g. Firefox with pdf support, Filezilla),
   -  **HPC** (modules related to HPC use: **Computation** sub-menu with
      Matlab, RStudio and SAS, **Visualisation** sub-menu with Paraview
      and VisIt),
   -  Programming (e.g. Meld Diff Viewer),
   -  System tools (e.g. File Browser, Terminal).

#. Running the applications in the text mode requires having a terminal
   open. To launch the terminal please go to Applications -> System
   tools -> Terminal. From Terminal all the commands available on
   regular login node can be used.
#. Some more information can be found on :download:`slides from our lunchbox
   session <nx_start_guide/nx_slides.pdf>`. In the slides you can find the
   information how to **connect the local HDD** to the NX session for
   easier transfer of data between the cluster and your local computer.

Attached documents
------------------

-  :download:`Instructions with screenshots <nx_start_guide/nx_config_guide.pdf>`
-  :download:`Slides from the lunchbox session <nx_start_guide/nx_slides.pdf>`

.. include:: links.rst
