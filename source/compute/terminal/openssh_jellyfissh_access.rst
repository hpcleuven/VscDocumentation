########################
Remote Terminal on macOS
########################

Prerequisites
=============

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      To access KU Leuven clusters, only an approved
      :ref:`VSC account <access>` is needed as a prerequisite.

   .. tab-item:: UAntwerpen
      :sync: ua

      Before attempting to launch a terminal on UAntwerpen clusters, you need
      to have :ref:`a private key in OpenSSH format <generating keys macos>`
      that is already :ref:`uploaded to your VSC account <upload public key>`.

   .. tab-item:: UGent
      :sync: ug

      Before attempting to launch a terminal on UGent clusters, you need
      to have :ref:`a private key in OpenSSH format <generating keys macos>`
      that is already :ref:`uploaded to your VSC account <upload public key>`.

   .. tab-item:: VUB
      :sync: vub

      Before attempting to launch a terminal on VUB clusters, you need
      to have :ref:`a private key in OpenSSH format <generating keys macos>`
      that is already :ref:`uploaded to your VSC account <upload public key>`.

.. _mac openssh access:

Using OpenSSH on macOS
======================

The Terminal on macOS works in the same way as a Linux terminal. Hence, you can
use the same commands for the :ref:`Linux terminal with OpenSSH <openssh access>`
to access the VSC clusters and transfer files from your Mac:

* use :ref:`ssh <OpenSSH access>` to connect and open a remote terminal on the
  cluster

* use :ref:`scp and sftp <scp and sftp>` for file transfers

.. _mac jellyfissh access:

Managing SSH with JellyfiSSH
============================

|Optional| You can use `JellyfiSSH`_ to store your SSH session settings for the
different VSC clusters and easily connect to them.

Installation
------------

Install `JellyfiSSH`_. The most recent version is available for a small fee
from the Mac App Store, but if you search for *JellyfiSSH 4.5.2*, which is the
version used for the screenshots in this page, you might still find some free
downloads for that version.

Installation is easy: just drag the program's icon to the Application folder in
the Finder, and you're done.

Bookmarking SSH connections
---------------------------

You can use JellyfiSSH to create a user-friendly bookmark for your ssh
connection settings. To do this, follow these steps:

#. Start JellyfiSSH and select 'New'. This will open a window where you
   can specify the connection settings.

#. In the 'Host or IP' field, type in <vsc-loginnode>. In the 'Login
   name' field, type in your <vsc-account>.
   In the screenshot below we have filled in the fields for a connection
   to the Genius cluster at KU Leuven as user vsc98765.

   .. figure:: openssh_jellyfissh_access/text_mode_access_using_openssh_or_jellyfissh_01.png 

#. You might also want to change the Terminal window settings, which can
   be done by clicking on the icon in the lower left corner of the
   JellyfiSSH window.

#. When done, provide a name for the bookmark in the 'Bookmark Title'
   field and press 'Add' to create the bookmark.

Connecting to SSH connections
-----------------------------

To make a connection, select the bookmark in the 'Bookmark' field and
click on 'Connect'. Optionally, you can make the bookmark the default
by selecting it as the 'Startup Bookmark' in the JellyfiSSH >
Preferences menu entry.

