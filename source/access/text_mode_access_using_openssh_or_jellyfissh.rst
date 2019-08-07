.. _OpenSSH JellyfiSSH access:

Text-mode access using OpenSSH or JellyfiSSH
============================================

Prerequisites
-------------

-  macOS comes with its own implementation of OpenSSH, so you don't need
   to install any third-party software to use it. Just open a Terminal
   window and jump in! Because of this, you can use the same commands as
   specified in the :ref:`Linux client section <linux client>` to
   access the cluster and transfer files
   (:ref:`ssh-keygen <generating keys linux>` to generate the
   keys, :ref:`ssh <OpenSSH access>` to log on to the
   cluster and :ref:`scp and sftp <scp and sftp>` for file transfer).
-  Optional: You can use `JellyfiSSH`_ to
   store your ssh session settings. The most recent version is available
   for a small fee from the Mac App Store, but if you `google for
   JellyfiSSH 4.5.2 <https://www.google.be/webhp?ion=1&ie=UTF-8#q=JellyfiSSH+4.5.2>`_,
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

You can find the names of the loginnodes in the
:ref:`sections of the local VSC clusters <hardware>`.

SSH will ask you to enter your passphrase.

On sufficiently recent macOS versions (Leopard and newer) you can
use the Keychain Access service to automatically provide your passphrase
to ssh. All you need to do is to add the key using

::

   $ ssh-add ~/.ssh/id_rsa

(assuming that your private key that :ref:`you generated
before <generating keys linux>` is called ``id_rsa``).

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

.. |JellyfiSSH| image:: text_mode_access_using_openssh_or_jellyfissh/text_mode_access_using_openssh_or_jellyfissh_01.png 

.. include:: links.rst
