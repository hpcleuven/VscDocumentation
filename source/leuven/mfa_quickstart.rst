Quickstart guide for using MFA on the KU Leuven cluster
=======================================================
General
-------
Multi factor authentication (MFA) has been activated for all users that try to log in to the KU Leuven cluster. This guide will take you
through the steps of correctly using and setting up MFA. For more detailed information, visit the
official VSC documentation page: https://docs.vscentrum.be/en/latest/leuven/tier2_hardware/mfa_login.html.

Getting started
---------------
#. When you try to connect to the cluster through an ssh-client or a terminal, you will be prompted with a URL:

   .. _firewall_link_mfa:
   .. figure:: mfa_quickstart/firewall_link_mfa.PNG
      :align: left
      :alt: firewall_link_mfa
#. Copy-paste the provided link in a browser and follow it. You should end up on a login page of your university or association. For KU Leuven this will be the idp page:

   .. _idp_page:
   .. figure:: mfa_quickstart/idp_page.PNG
      :align: left
      :alt: idp_page
#. Log in as usual. You should now end up on a page that tells you that your vsc identity is confirmed. If you already performed the previous login in that browser session, you will immediately end up on this page.

   .. _firewall_confirmed:
   .. figure:: mfa_quickstart/firewall_confirmed.PNG
      :align: left
      :alt: firewall_confirmed
#. Go back to your SSH client or terminal. You should now be connected to a login node on the cluster.    

   .. _login_node:
   .. figure:: mfa_quickstart/login_node.PNG
      :align: left
      :alt: login_node
#. That’s it! You can continue doing your HPC work as usual.

Using apps that use SSH connections in the background
-----------------------------------------------------
Not all apps that can connect to the cluster with an SSH connection can prompt you the firewall link. For some apps it is possible to first connect
to the cluster as described above, keep that connection open and if you then launch the app, it will start normally. Another method
is going straight to https://firewall.vscentrum.be/ while the connection is pending. Look for: "Are you trying to log in from <IP address>? YES / NO".
Click YES. This works for FileZilla, and some versions of NX. If that does not allow you to connect, you should set up an agent. 

Setting up an agent
-------------------
The standard login method will prompt you the URL every time you try to connect to the cluster. By setting up an SSH agent, you can create a
certificate that will avoid this. Depending on your OS, there are different solutions. Select the correct one for your machine and follow the
subsequent steps to set it up. The different set-ups are:
-	Windows machines
-	Linux machines and Mac machines 

Windows machines
~~~~~~~~~~~~~~~~
#. For the Windows machines, download the vscagent.exe from https://firewall.vscentrum.be/vscagent/latest/. You will be asked to log in with the credentials of your university or institution. Then you will to be able to download it.

   .. _vscagent_download:
   .. figure:: mfa_quickstart/vscagent_download.PNG
      :align: left
      :alt: vscagent_download
#. This exe file can be run directly. If you have a KU Leuven central managed laptop, place it in C:\temp (running it from other locations won’t work). If you have another machine, place it on a location of your choice. Run the application.

   .. _vscagent_app:
   .. figure:: mfa_quickstart/vscagent_app.PNG
      :align: left
      :alt: vscagent_app
#. Select the ‘Configuration’ tab. Check the ‘Enable HPC user certificates’ and the ‘tier2-leuven’ boxes. Add your vsc number under ‘Username’. Save the configuration file. **KU Leuven server certificates and the tier1-leuven are only for very specific users. Have a read through our documentation if you think you would belong to them.**

   .. _vscagent_config:
   .. figure:: mfa_quickstart/vscagent_config.PNG
      :align: left
      :alt: vscagent_config
#. Now, Go to the ‘SSH Key Files’ tab. Click the ‘+’ and navigate to your private file. Then, click ‘Open’. You will be asked to provide your key passphrase. **If this is not the case, you don’t have a passphrase protected key, which is a security threat! Consider creating a new key-pair.** Your private key should then appear in the list here.

   .. _vscagent_keys:
   .. figure:: mfa_quickstart/vscagent_keys.PNG
      :align: left
      :alt: vscagent_keys
#. You can now load your certificate. Go to the ‘SSH Identities’ tab. You will already see your key listed there. Now, click the ‘Renew certificate’ button and then the ‘HPC Tier 2 Leuven certificate’. Your browser opens and you will now follow step 2 and 3 under ‘Getting started’.

   .. _vscagent_renewcert:
   .. figure:: mfa_quickstart/vscagent_renewcert.PNG
      :align: left
      :alt: vscagent_renewcert 
#. You will get a message that the certificate was renewed.

   .. _vscagent_success:
   .. figure:: mfa_quickstart/vscagent_success.PNG
      :align: left
      :alt: vscagent_success    
#. The agent is now configured. From now on, when you start the agent, you will be asked the passphrase of your key first, followed by step 5 and 6.

Linux and Mac machines
~~~~~~~~~~~~~~~~~~~~~~
If you want to use a UI as an agent, you can also use the vscagent, as explained under ‘Windows machines’.
The steps are the same, just download ‘vscagent’ instead of ‘vscagent.exe’. Start it with `vscagent gui`.

***!!! The vscagent does not work for Mac PCs with a M1 processor!!!***

Linux and MacOS come with a built-in SSH agent, so there is no real need to download an extra program. Before using it,
it is best to verify whether or not it is configured correctly:

#. Open a terminal
#. Verify if your agent is running with `ssh-add -l`. If it is not running you will get following error: `Could not open a connection to your authentication agent`
#. If this is the case, start your agent with `eval $(ssh-agent)`
#. You now need to create or adapt a profile for the cluster in your ~/.shh/config file. If you notice you do not have this file yet, create it with the following command, you should adapt the permissions as well:

      touch ~/.ssh/config
      chmod 600 ~/.ssh/config
#. Your profile should look like this

      Host login.hpc.kuleuven.be
        ForwardAgent yes
        PubkeyAuthentication yes
        ChallengeResponseAuthentication yes
        PreferredAuthentications publickey,keyboard-interactive
#. You can now ssh to the cluster. The agent will automatically store your certificate. The certificate will be stored as long as your agent stays alive.

Configuration of SSH clients and UI apps for use with an agent
--------------------------------------------------------------
Depending on how you set up your SSH clients and UI apps like NX and FileZilla, it can be that you have to make some changes to the configurations
in these profiles. Here, we shortly show you how to set up MobaXTerm, PuTTY and NX correctly.

MobaXTerm
~~~~~~~~~
#. Right-click on the correct session and click on ‘edit session’

   .. _moba_edit_session:
   .. figure:: mfa_quickstart/moba_edit_session.png
      :align: left
      :alt: moba_edit_session
#. Under advanced settings. Be sure that ‘Use private key’ is not selected

   .. _moba_priv:
   .. figure:: mfa_quickstart/moba_priv.PNG
      :align: left
      :alt: moba_priv
#. c.	Click ‘Ok’

PuTTY
~~~~~
#. Select your saved session for the cluster connection and load it.
#. Under ‘SSH’, go to ‘Auth’. Select ‘Allow agent forwarding’ and remove any private key directories from under ‘Private key file for authentication’

   .. _putty:
   .. figure:: mfa_quickstart/putty.png
      :align: left
      :alt: putty
#. Save the profile under ‘Session’

NX
~~
#. Open NX and right-click your correct profile. Select ‘Edit connection’

   .. _nx_profile:
   .. figure:: mfa_quickstart/nx_profile.png
      :align: left
      :alt: nx_profile  
#. Go to the ‘Configuration’ tab and select 'Use key-based authentication with a SSH agent'

   .. _nx_config:
   .. figure:: mfa_quickstart/nx_config.PNG
      :align: left
      :alt: nx_config  
#. Click ‘Modify’ and verify that 'Forward authentication' is checked

   .. _nx_mod:
   .. figure:: mfa_quickstart/nx_mod.PNG
      :align: left
      :alt: nx_mod
         
