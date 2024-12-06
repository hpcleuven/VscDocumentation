.. _FileZilla:

############################
Data transfer with FileZilla
############################

FileZilla is a free and easy-to-use FTP-style program to
transfer files to and from your VSC account on the clusters.


You can `download FileZilla`_ from the `FileZilla project page`_.

Prerequisites
=============

All users need to setup an :ref:`SSH agent <SSH agent>` before proceeding.

.. tab-set::

   .. tab-item:: KU Leuven
   
      You need to :ref:`get an SSH certificate into your agent <mfa-with-ssh-agent>`,
      if you haven't done so already.

   .. tab-item:: UGent, VUB, UAntwerpen

      You need to load your private SSH key into your :ref:`SSH agent <SSH agent>`.

Configuration of FileZilla to connect to a login node
=====================================================

#. Start FileZilla
#. Open the Site Manager using the 'File' menu
#. Create a new site by clicking the 'New Site' button
#. In the tab marked 'General', enter the following values (all other
   fields remain blank):

   .. tab-set::

      .. tab-item:: KU Leuven

         - Host: ``login.hpc.kuleuven.be``
         - Server Type: 'SFTP - SSH File Transer Protocol'
         - Logon Type: 'Interactive'
         - User: *your own* VSC user ID

           .. figure:: filezilla/site_manager_kul.png
              :alt: FileZilla's site manager for KU Leuven clusters

      .. tab-item:: UGent, VUB, UAntwerpen

         -  Host: fill in the hostname of the VSC login node of your home
            institution. You can find this information in the :ref:`overview
            of available hardware on this site <hardware>`.
         -  Server Type: 'SFTP - SSH File Transfer Protocol'
         -  Logon Type: 'Normal'
         -  User: *your own* VSC user ID, e.g. vsc98765

            .. figure:: filezilla/site_manager_non_kul.png
               :alt: FileZilla's site manager for UGent, VUB, UAntwerpen

#. Optionally, rename this setting to your liking by pressing the
   'Rename' button
#. Press 'Connect' and enter your passphrase when requested


.. tab-set::

   .. tab-item:: KU Leuven

      As long as your SSH agent is running and keeping a valid SSH certificate,
      you stay connected via FileZilla and you do not require additional
      configuration.

   .. tab-item:: UGent, VUB, UAntwerpen

      Recent versions of FileZilla have a screen in the settings to
      manage private keys. The path to the private key must be provided in
      options (Edit Tab -> options -> connection -> SFTP):

      .. figure:: filezilla/prefs_private_key.jpg
         :alt: FileZilla site manager with settings

      After that you should be able to connect after being asked for
      passphrase. As an alternative you can choose to use an :ref:`SSH agent <SSH agent>`.

Under the 'Advanced' tab you can also set the directory you wish to open by
default upon login.
For example, to set your default path to your ``VSC_DATA`` directory, you need to
provide the full path, like ``/data/brussels/1xx/vsc1xxxxx``.
