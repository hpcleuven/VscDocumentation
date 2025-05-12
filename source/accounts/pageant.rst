.. _Pageant:

#######
Pageant
#######

Pageant is an SSH authentication agent that couples seamlessly with
:ref:`Putty<terminal putty>`, :ref:`MobaXterm<terminal mobaxterm>`,
:ref:`NoMachine<NX start guide>` and :ref:`FileZilla<FileZilla>` to make user
authentication an easy task. As of version 0.78, Pageant can also hold SSH
certificates in addition to SSH private keys.

.. warning::

   SSH authentication agents are very handy as you no longer need to
   type your passphrase every time that you try to log in to the cluster.
   It also implies that when someone gains access to your computer, he
   also automatically gains access to your account on the cluster. So be
   very careful and lock your screen when you're not with your computer!
   It is your responsibility to keep your computer safe and prevent easy
   intrusion of your VSC account due to an obviously unprotected PC!

Prerequisites
=============

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      To access KU Leuven clusters, only an approved :ref:`VSC account <access>` is needed
      as a prerequisite.

   .. tab-item:: UAntwerpen
      :sync: ua

      Before you run Pageant, you need to have a private key in PPK format
      (filename ends with ``.ppk``).
      See :ref:`our page on generating keys with PuTTY <generating keys putty>`
      to find out how to generate and use one.
      
   .. tab-item:: UGent
      :sync: ug

      Before you run Pageant, you need to have a private key in PPK format
      (filename ends with ``.ppk``).
      See :ref:`our page on generating keys with PuTTY <generating keys putty>`
      to find out how to generate and use one.
      
   .. tab-item:: VUB
      :sync: vub

      Before you run Pageant, you need to have a private key in PPK format
      (filename ends with ``.ppk``).
      See :ref:`our page on generating keys with PuTTY <generating keys putty>`
      to find out how to generate and use one.

Installation
============

Pageant is part of the :ref:`PuTTY distribution <terminal putty>`. Follow
:ref:`our installation instructions for PuTTY <putty install>` to install
Pageant on your computer.

Running Pageant
===============

Oncer you launch Pageant, it will put an icon of a computer wearing a hat
onto the system tray, which looks like this: 

.. _pageant_logo:
.. figure:: pageant/Pageant_logo.png
   :alt: pageant_logo

Pageant runs silently in the background and does nothing until you load a
private key into it.

Open the main window of Pageant by:

#. Click the Pageant icon with the right mouse button
#. Select "View Keys" from the menu

   .. _pageant_menu:
   .. figure:: pageant/Pageant_add_key.png
      :alt: pageant_menu

You can also bring this window up by double-clicking on the Pageant icon.

Adding keys to Pageant
======================

The Pageant window contains a list box.
This shows the private keys and/or certificates that Pageant is holding.
Initially this list is empty.
After you add one or more keys or certificates, they will show up in the list box.

Steps to add a key to Pageant:

#. Press the "Add Key" button
#. A file dialog opens labelled "Select Private Key File"
#. Find your private key file in this dialog, and press "Open"
#. Pageant will now load the private key. If the key is protected by a
   passphrase, Pageant will ask you to type its passphrase.

   .. _pageant_passphrase:
   .. figure:: pageant/Pageant_passphrase.png
      :alt: pageant_passphrase

#. When the key has been loaded, it will appear in the list in the Pageant window.

Now start PuTTY (or FileZilla) and open an SSH session to a site that
accepts your key or certificate. PuTTY (or Filezilla) will notice that Pageant is
running; they retrieve the key or certificate automatically from Pageant, and use it to
authenticate you as a recognized user.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Follow the steps in :ref:`Connecting with an SSH agent <mfa-with-ssh-agent>`
      to get an SSH certificate into your agent.
      At this point, a new certificate will be stored in Pageant that holds your
      identity for a limited period of time.
      You can verify that the certificate is actually stored by right-clicking on
      Pageant and selecting ‘View Keys’:

      .. figure:: pageant/Pageant_view_keys.png
         :alt: pageant_view_keys

   .. tab-item:: UAntwerpen
      :sync: ua

      You can now open as many PuTTY sessions as you like without having to
      type your passphrase again.

   .. tab-item:: UGent
      :sync: ug

      You can now open as many PuTTY sessions as you like without having to
      type your passphrase again.

   .. tab-item:: VUB
      :sync: vub

      You can now open as many PuTTY sessions as you like without having to
      type your passphrase again.

Pageant provides your credentials to other applications (such as PuTTY, NoMachine,
FileZilla, MobaXterm) whenever you are prompted for your identity.

Stopping Pageant
================

When you want to shut down Pageant, click the right button on the
Pageant icon in the system tray, and select 'Exit' from the menu.
Closing the Pageant main window does *not* shut down Pageant, because
a SSH agent sits silently in the background.

.. seealso::

   You can find more info in the
   `on-line manual <http://the.earth.li/~sgtatham/putty/0.63/htmldoc/Chapter9.html>`_.

