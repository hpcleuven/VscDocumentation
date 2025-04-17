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
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven
      :sync: kuluh
   
      You need to :ref:`get an SSH certificate into your agent <mfa-with-ssh-agent>`,
      if you haven't done so already.

   .. tab-item:: UAntwerpen
      :sync: ua

      You need to load your private SSH key into your :ref:`SSH agent <SSH agent>`.

   .. tab-item:: UGent
      :sync: ug

      You need to load your private SSH key into your :ref:`SSH agent <SSH agent>`.

   .. tab-item:: VUB
      :sync: vub

      You need to load your private SSH key into your :ref:`SSH agent <SSH agent>`.


Configuration of FileZilla to connect to a login node
=====================================================

#. Start FileZilla
#. Open the Site Manager using the 'File' menu
#. Create a new site by clicking the 'New Site' button
#. In the tab marked 'General', enter the following values (all other
   fields remain blank):

   .. tab-set::
      :sync-group: vsc-sites

      .. tab-item:: KU Leuven
         :sync: kuluh

         * Host: ``login.hpc.kuleuven.be``
         * Server Type: 'SFTP - SSH File Transfer Protocol'
         * Logon Type: 'Interactive'
         * User: *your own* VSC user ID

         .. figure:: filezilla/site_manager_kul.png
            :alt: FileZilla's site manager for KU Leuven clusters

      .. tab-item:: UAntwerpen
         :sync: ua

         * Host: ``login.hpc.uantwerpen.be``
         * Server Type: 'SFTP - SSH File Transfer Protocol'
         * Logon Type: 'Normal'
         * User: *your own* VSC user ID

         .. figure:: filezilla/site_manager_non_kul.png
            :alt: FileZilla's site manager for UGent, VUB, UAntwerpen

      .. tab-item:: UGent
         :sync: ug

         * Host: ``login.hpc.ugent.be``
         * Server Type: 'SFTP - SSH File Transfer Protocol'
         * Logon Type: 'Normal'
         * User: *your own* VSC user ID

         .. figure:: filezilla/site_manager_non_kul.png
            :alt: FileZilla's site manager for UGent, VUB, UAntwerpen

      .. tab-item:: VUB
         :sync: vub

         * Host: ``login.hpc.vub.be``
         * Server Type: 'SFTP - SSH File Transfer Protocol'
         * Logon Type: 'Normal'
         * User: *your own* VSC user ID

         .. figure:: filezilla/site_manager_non_kul.png
            :alt: FileZilla's site manager for UGent, VUB, UAntwerpen

#. Optionally, rename this setting to your liking by pressing the
   'Rename' button

#. Press 'Connect' and enter your passphrase when requested

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven
      :sync: kuluh

      As long as your SSH agent is running and keeping a valid SSH certificate,
      you stay connected via FileZilla and you do not require additional
      configuration.

   .. tab-item:: UAntwerpen
      :sync: ua

      .. include:: filezilla-key-management.rst

   .. tab-item:: UGent
      :sync: ug

      .. include:: filezilla-key-management.rst

   .. tab-item:: VUB
      :sync: vub

      .. include:: filezilla-key-management.rst

Under the *'Advanced'* tab you can also set the directory you wish to open by
default upon login.
For example, setting your default path to your ``VSC_DATA`` directory can be done by
providing its full path, like ``/data/brussels/100/vsc10000``.
