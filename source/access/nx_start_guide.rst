.. _NX start guide:

NX start guide
==============

Installing NX NoMachine client
------------------------------

Download the enterprise version of the client from the `NX Client download`_ page.

NoMachine NX Client Configuration
---------------------------------

NoMachine works smoothly with SSH agents, such as :ref:`Pageant <using Pageant>` 
for Windows users, and :ref:`Built-in SSH agent <SSH agent>` for Linux/Mac users.
As a result of that, users first need to authenticate themselves, using 
:ref:`Multi-Factor Authentication (MFA) <mfa_leuven>` before being able to start a new 
NX session.
You may also refer to :ref:`MFA Quick Start Guide <mfa for nx>` for additional information.


1. Start the NoMachine client and press **Continue** till you see the screen
   listing your connections, titled **Machines**.

#. Press **Add** to create a new connection

#. In the **Addres** pane,

   #. choose a name for the connection, e.g., "genius"
   #. change the Protocol to **SSH**
   #. choose the hostname **nx.hpc.kuleuven.be** for Genius and port **22**

            .. note::

                This login node cannot be used to access the cluster from the terminal.   

#. In the **Configuration** pane

   #. choose **Use key-based authentication with a SSH agent**
   #. press **Modify** and select **Forward authentication**

#. Press **Connect**

#. Your VSC username and passphrase will be automatically fetched from your SSH agent

#. If you are creating for the first time choose **Create a new virtual desktop**.
   Otherwise please refer to the :ref:`section on how to reconnec to an NX session
   <Reconnecting to an NX session>` for instructions.

#. Read the useful information regarding your session displayed on several
   screens. This step is very important in case of mobile devices – once
   you miss the instructions it is not so easy to figure out how to operate
   NoMachine on your device. You can optionally choose not to show these
   messages again.

Once connected you will see the virtual Linux desktop.

Reconnecting to an NX session
-----------------------------

When you leave a session without logging out, you can reconnect to
that session.  This is of course a great feature if your network
connection is not very stable.  It also helps you to work more
efficiently since you can simply resume your work where you left off.

When reconnecting choose your desktop from all the listed ones. If
there are too many you can use the option **find a user or a desktop**
and type your username (vsc-account). Once you found your desktop press
**connect**.

Note that when you don't want your session to persist, you should select
**Log out** from the **System** menu.

How to start using NX on Genius?
----------------------------------

#. Once your desktop is open, you can use all available GUI designed
   software that is listed within the Applications menu. Software is
   divided into several groups:

   -  Accessories (e.g. Calculator, Character Map, Emacs, Gedit, GVim),
   -  Graphics (e.g. gThumb Image Viewer, Xpdf PDF Viewer),
   -  Internet (e.g. Firefox with pdf support, Filezilla),
   -  **HPC** (modules related to HPC use: **Computation** sub-menu with
      MATLAB, RStudio and SAS, **Visualisation** sub-menu with Paraview
      and VisIt),
   -  Programming (e.g. Meld Diff Viewer, Microsoft Visual Studio Code),
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
