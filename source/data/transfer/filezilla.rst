.. _FileZilla:

############################
Data transfer with FileZilla
############################

FileZilla is an easy-to-use freely available ftp-style program to
transfer files to and from your account on the clusters.

You can also put FileZilla with your private key on a USB stick to
access your files from any internet-connected PC.

You can `download FileZilla`_ from the `FileZilla project page`_.

Configuration of FileZilla to connect to a login node
=====================================================

.. note::

   The UGent, VUB, and UAntwerpen users need to start Pageant first and load their private key to Pageant (more info in our ":ref:`using Pageant`" page). The KU Leuven/UHasselt users do not necessarily require SSH key pairs.

#. Start FileZilla;
#. Open the Site Manager using the 'File' menu;
#. Create a new site by clicking the New Site button;
#. In the tab marked General, enter the following values (all other
   fields remain blank):

   .. tab-set::

      .. tab-item:: KU Leuven/UHasselt

         - Host: ``login.hpc.kuleuven.be``
         - Server Type: SFTP - SSH File Transer Protocol
         - Logon Type: Interactive
         - User: *your own* VSC user ID, starting as ``vsc3``

           .. figure:: filezilla/site_manager_kul.png
              :alt: FileZilla's site manager for KU Leuven/UHasselt site 

      .. tab-item:: UGent, VUB, UAntwerpen

         -  Host: fill in the hostname of the VSC login node of your home
            institution. You can find this information in the :ref:`overview
            of available hardware on this site <hardware>`.
         -  Server Type: SFTP - SSH File Transfer Protocol
         -  Logon Type: Normal
         -  User: *your own* VSC user ID, e.g., vsc98765;

            .. figure:: filezilla/site_manager_non_kul.png
               :alt: FileZilla's site manager for UGent, VUB, UAntwerpen

#. Optionally, rename this setting to your liking by pressing the
   'Rename' button;
#. Press 'Connect' and enter your passphrase when requested.


.. tab-set::

   .. tab-item:: KU Leuven

      As long as your SSH agent is running and keeping a valid SSH certificate,
      you stay connected via FileZilla and you do not require additional
      configuration.

   .. tab-item:: UHasselt, UGent, VUB, UAntwerpen

      Recent versions of FileZilla have a screen in the settings to
      manage private keys. The path to the private key must be provided in
      options (Edit Tab -> options -> connection -> SFTP):

      .. figure:: filezilla/prefs_private_key.jpg
         :alt: FileZilla site manager with settings

      After that you should be able to connect after being asked for
      passphrase. As an alternative you can choose to use putty pageant.

Under the 'Advanced' tab you can also set the directory you wish to open by
default upon login.
For example, to set your default path to your ``VSC_DATA`` directory, you need to
provide the full path, like ``/data/brussels/1xx/vsc1xxxxx``.
