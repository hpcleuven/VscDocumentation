.. _JellyfiSSH access:

Text-mode access using OpenSSH
==============================

Prerequisites
-------------

- macOS comes with its own implementation of OpenSSH, so you don't need
  to install any third-party software to use it. Just open a Terminal
  window and jump in!

Using OpenSSH on macOS
----------------------

You can use the same commands as specified in the
:ref:`Linux client section <linux client>` to access the cluster and transfer
files:

* :ref:`ssh-keygen <generating keys linux>` to generate the keys
* :ref:`ssh <OpenSSH access>` to log on to the cluster
* :ref:`scp and sftp <scp and sftp>` for file transfer


Text-mode access using JellyfiSSH
=================================

|Optional| You can use `JellyfiSSH`_ to store your ssh session settings.

Prerequisites
-------------

* Install JellyfiSSH. The most recent version is available
  for a small fee from the Mac App Store, but if you `google for
  JellyfiSSH 4.5.2 <https://www.google.be/webhp?#q=JellyfiSSH+4.5.2>`_,
  the version used for the screenshots in this page, you can still find
  some free downloads for that version. Installation is easy: just drag
  the program's icon to the Application folder in the Finder, and
  you're done.

Using JellyfiSSH for bookmarking ssh connection settings
--------------------------------------------------------

You can use JellyfiSSH to create a user-friendly bookmark for your ssh
connection settings. To do this, follow these steps:

#. Start JellyfiSSH and select 'New'. This will open a window where you
   can specify the connection settings.
#. In the 'Host or IP' field, type in <vsc-loginnode>. In the 'Login
   name' field, type in your <vsc-account>.
   In the screenshot below we have filled in the fields for a connection
   to the Genius cluster at KU Leuven as user vsc98765.

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

