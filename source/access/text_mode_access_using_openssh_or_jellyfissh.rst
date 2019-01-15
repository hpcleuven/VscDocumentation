Text-mode access using OpenSSH or JellyfiSSH
============================================

Prerequisites
-------------

-  macOS comes with its own implementation of OpenSSH, so you don't need
   to install any third-party software to use it. Just open a Terminal
   window and jump in! Because of this, you can use the same commands as
   specified in the `Linux client section <\%22/client/linux\%22>`__ to
   access the cluster and transfer files
   (`ssh-keygen <\%22/client/linux/keys-openssh\%22>`__ to generate the
   keys, `ssh <\%22/client/linux/login-openssh\%22>`__ to log on to the
   cluster and `scp and sftp <\%22/client/linux/data-openssh\%22>`__ for
   file transfer).
-  Optional: You can use
   `JellyfiSSH <\%22http://www.m-works.co.nz/jellyfissh.php\%22>`__ to
   store your ssh session settings. The most recent version is available
   for a small fee from the Mac App Store, but if you `google for
   JellyfiSSH
   4.5.2 <\%22https://www.google.be/webhp?ion=1&ie=UTF-8#q=JellyfiSSH+4.5.2\%22>`__,
   the version used for the screenshots in this page, you can still find
   some free downloads for that version. Installation is easy: just drag
   the program's icon to the Application folder in the Finder, and
   you're done.

Connecting using OpenSSH
------------------------

Like in the Linux client section, the ssh command is used to make a
connection to (one of) the VSC clusters. In a Terminal window, execute:

::

   $ ssh <vsc-account>@<vsc-loginnode>

where

-  <vsc-account> is your VSC username that you have received by mail
   after your request was approved,
-  <vsc-loginnode> is the name of the loginnode of the VSC cluster you
   want to connect to.

You can find the names and ip-addresses of the loginnodes in the
`sections of the local VSC
clusters <\%22/infrastructure/hardware\%22>`__.

SSH will ask you to enter your passphrase.

On sufficiently recent macOS/OS X versions (Leopard and newer) you can
use the Keychain Access service to automatically provide your passphrase
to ssh. All you need to do is to add the key using

::

   $ ssh-add ~/.ssh/id_rsa

(assuming that your private key that `you generated
before <\%22/client/macosx/keys-openssh\%22>`__ is called id_rsa).

Using JellyfiSSH for bookmarking ssh connection settings
--------------------------------------------------------

You can use JellyfiSSH to create a user-friendly bookmark for your ssh
connection settings. To do this, follow these steps:

#. Start JellyfiSSH and select 'New'. This will open a window where you
   can specify the connection settings.
#. In the 'Host or IP' field, type in <vsc-loginnode>. In the 'Login
   name' field, type in your <vsc-account>.
   In the screenshot below we have filled in the fields for a connection
   to ThinKing cluster at KU Leuven as user vsc98765.
   |JellyfiSSH|
#. You might also want to change the Terminal window settings, which can
   be done by clicking on the icon in the lower left corner of the
   JellyfiSSH window.
#. When done, provide a name for the bookmark in the 'Bookmark Title'
   field and press 'Add' to create the bookmark.
#. To make a connection, select the bookmark in the 'Bookmark' field and
   click on 'Connect'. Optionally, you can make the bookmark the default
   by selecting it as the 'Startup Bookmark' in the JellyfiSSH >
   Preferences menu entry.

"

.. |JellyfiSSH| image:: text_mode_access_using_openssh_or_jellyfissh/text_mode_access_using_openssh_or_jellyfissh_01.png 

