.. _using Pageant:

Using Pageant
=============

Getting started with Pageant
----------------------------

Pageant is an SSH authentication agent that couples seamlessly with Putty, MobaXterm,
NoMachine and FileZilla to make user authentication an easy task.
Pageant is part of the `PuTTY`_ distribution.
As of version 0.78, Pageant can hold certificates in addition to SSH private keys.

Prerequisites
=============

.. tab-set::

   .. tab-item:: KU Leuven

      To access KU Leuven clusters, only an approved :ref:`VSC account <access>` is needed
      as a prerequisite.

   .. tab-item:: UGent, VUB, UAntwerpen

      Before you run Pageant, you need to have a private key in PPK format
      (filename ends with ``.ppk``). See :ref:`our page on generating keys with
      PuTTY <generating keys putty>` to find out how to
      generate and use one.
      
When you run Pageant, it will put an icon (of a computer wearing a hat)
into the System tray, which looks like this: 

   .. _pageant_logo:
   .. figure:: using_pageant/Pageant_logo.PNG
      :alt: pageant_logo


Pageant runs silently in the background and does nothing until you load a private key into it.
If you click the Pageant icon with the right mouse button, you will see a menu.
Select ‘View Keys’ from this menu. The Pageant main window will appear.
You can also bring this window up by double-clicking on the Pageant icon.

   .. _pageant_add_key:
   .. figure:: using_pageant/Pageant_add_key.PNG
      :alt: pageant_add_key


The Pageant window contains a list box.
This shows the private keys and/or certificates that Pageant is holding.
Initially this list is empty.
After you add one or more keys or certificates, they will show up in the list box.

To add a key to Pageant, press the ‘Add Key’ button. Pageant will bring
up a file dialog, labelled ‘Select Private Key File’. Find your private
key file in this dialog, and press ‘Open’. Pageant will now load the
private key. If the key is protected by a passphrase, Pageant will ask
you to type the passphrase. When the key has been loaded, it will appear
in the list in the Pageant window.
For adding an SSH key, the window dialog looks like this:

   .. _pageant_passphrase:
   .. figure:: using_pageant/Pageant_passphrase.PNG
      :alt: pageant_passphrase

Now start PuTTY (or FileZilla) and open an SSH session to a site that
accepts your key or certificate. PuTTY (or Filezilla) will notice that Pageant is
running; they retrieve the key or certificate automatically from Pageant, and use it to
authenticate you as a recognized user.

.. tab-set::

   .. tab-item :: KU Leuven

      Try to connect to one of :ref:`Tier2 login nodes <tier2_login_nodes>`.
      It is mandatory to allow agent forwarding in your ssh client.
      While connecting, you will be given a URL to validate your identity.
      Copy that URL in your browser and login to your KU Leuven/UHasselt account.
      Upon a successful login to your KU Leuven/UHasselt account, the login with 
      your VSC account will also succeed.
      At this point, a new certificate will be stored in Pageant that holds your
      identity for a limited period of time.
      You can verify that the certificate is actually stored by right-clicking on
      Pageant and selecting ‘View Keys’:

      .. _pageant_view_keys:
      .. figure:: using_pageant/Pageant_view_keys.PNG
         :alt: pageant_view_keys

   .. tab-item:: UGent, VUB, UAntwerpern

      You can now open as many PuTTY sessions as you like without having to type your passphrase again.

Pageant provides your credentials to other applications (such as PuTTY, NoMachine,
FileZilla, MobaXterm) whenever you are prompted for your identity.

When you want to shut down Pageant, click the right button on the
Pageant icon in the system tray, and select 'Exit' from the menu.
Closing the Pageant main window does *not* shut down Pageant, because
a SSH agent sits silently in the background.

You can find more info `in the on-line
manual <http://the.earth.li/~sgtatham/putty/0.63/htmldoc/Chapter9.html>`_.

.. warning::

   SSH authentication agents are very handy as you no longer need to
   type your passphrase every time that you try to log in to the cluster.
   It also implies that when someone gains access to your computer, he
   also automatically gains access to your account on the cluster. So be
   very careful and lock your screen when you're not with your computer!
   It is your responsibility to keep your computer safe and prevent easy
   intrusion of your VSC-account due to an obviously unprotected PC!

