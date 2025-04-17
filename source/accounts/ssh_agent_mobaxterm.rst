.. _mobaxterm ssh agent:

######################
SSH agent on MobaXterm
######################

Once you've successfully setup the connection to your cluster, you will notice
that you are prompted for the passphrase at each connection you make to a
cluster. To avoid the need to re-type it each time, you can setup an internal
SSH agent in :ref:`MobaXterm <terminal mobaxterm>` that will take care of
unlocking your SSH private key or SSH certificate for
:ref:`Multi-Factor Authentication <mfa_leuven>` when you open the application.
The SSH agent will save the passphrase after you have introduced it once.

Prerequisites
=============

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven
      :sync: kuluh

      To access KU Leuven clusters, only an approved
      :ref:`VSC account <access>` is needed as a prerequisite.

   .. tab-item:: UAntwerpen
      :sync: ua

      Before you run an SSH agent on MobaXterm, you need to have a private key
      in OpenSSH format, which can be created with MobaXterm itself. See
      :ref:`generating keys mobaxterm` to find out how to generate and use one.
      
   .. tab-item:: UGent
      :sync: ug

      Before you run an SSH agent on MobaXterm, you need to have a private key
      in OpenSSH format, which can be created with MobaXterm itself. See
      :ref:`generating keys mobaxterm` to find out how to generate and use one.
      
   .. tab-item:: VUB
      :sync: vub

      Before you run an SSH agent on MobaXterm, you need to have a private key
      in OpenSSH format, which can be created with MobaXterm itself. See
      :ref:`generating keys mobaxterm` to find out how to generate and use one.

Enable SSH Agent
================

The following steps explain how to enable the SSH Agent on the MobaXterm
application. You can install MobaXterm on your computer following
:ref:`our installation instructions <mobaxterm install>`.

#. Open the MobaXterm program and go to the menu 'Settings ->
   Configuration'

#. You should see the `MobaXterm Configuration` panel. In the 'General' tab
   choose the 'MobaXterm passwords management' option; a new panel will be
   opened; make sure that 'Save sessions passwords' has the options
   'Always' and 'Save SSH keys passphrases as well' selected (as shown below)
   and click 'OK'.

   .. figure:: ssh_agent_mobaxterm/mobaxterm_save_passwords.png
      :alt: mobaxterm save passwords option

#. Open  the 'SSH' tab in the same `MobaXterm Configuration` panel.
   Make sure that all the boxes below the 'SSH agents' section are
   ticked.

#. Press the '+' button in the 'Load following keys at MobAgent startup'
   field, look for your private key file and select it. At the end of the
   process, the panel should look like this (the location of your private SSH
   key may be different):

   .. figure:: ssh_agent_mobaxterm/mobaxterm_ssh_agent.png
      :alt: mobaxterm ssh agent setup

   Please, keep in mind that these settings will have to be updated if the
   location of private key ever changes.
   
#. Press OK and when prompted for restarting MobaXterm, choose to do so.

#. Once MobaXterm restarts you will be asked for the private key passphrase at
   launch. This will occur only once and after you introduce it correctly it
   will stay saved for all following sessions. Double clicking on a shortcuts
   for a cluster should open the corresponding connection directly.

