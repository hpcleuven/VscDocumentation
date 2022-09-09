Multi Factor Authentication (MFA)
=================================

About
-----

Multi Factor Authentication (MFA) is an augmented level of security with multiple factors, as in the name. These factors are:

- A valid private key
- Access to a VSC associated university account

The latter will be verified by prompting a VSC firewall link when trying to ssh to one of our KU Leuven clusters. When following this link, you will be asked to choose your university, and log in. If you already did that in a browser session (to access any other university-related websites), you do not need to log in again. If the login was succesfull, you will be redirected to a firewall.vscentrum.be page, with the message that your vsc identity was confirmed.

The benefits of this method are:

- keys without passphrase are less of a security problem
- users can't share keys
- users won't be able to connect if the university account is no longer valid

What do you need to use MFA on your vsc-account
-----------------------------------------------

With our MFA enabled login nodes, you can access the cluster in following ways:

- With ssh key + MFA prompt from IP addresses in any KU Leuven address range, any known LAN balancer address of other Flemish universities, any Belgian residential network, or a list of known institutes or organizations.
- With ssh key only from IP addresses on which `VSC firewall page`_ is opened and that are also in a KU Leuven address range or a Belgian residential network.
- With ssh key + confirmation from IP addresses on which `VSC firewall page`_ is opened and that are not in a KU Leuven address range and neither in a Belgian residential network. This confirmation is the same as the MFA prompt, but can also be answered by a popup on the HPC firewall page that the user has opened.
- (only on login[-tier1].hpc.kuleuven.be) With ssh key + MFA prompt if connecting from any other IP address that was already seen during the last 90 days (so a user can open `VSC firewall page`_ manually once, and then connect each month directly with the MFA prompt).

MFA Authentication without an agent
-----------------------------------

When you try to login to the cluster with a ssh-client (e.g. PuTTY, MobaXTerm...) and you have no agent running (see later):

- start any SSH session to a KU Leuven cluster and authenticate with your private vsc-key
- your ssh connection will prompt you a URL
- copy/paste this URL in your browser and use the VSC account authentication

Your SSH-connection will now be completed. This method also works from a Linux or Mac terminal.

UI applications with SSH connection in the background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some UI applications that use an SSH connection in the background, like NX or FileZilla, will not prompt you the firewall URL (other apps like WinSCP will do this however). If you want to use such an application without using an agent, you should first login to the KU Leuven cluster with an ssh-client on your machine. As long as you keep this connection open, you can connect with the other apps as well. Using an agent will avoid this extra step, which will be explained in the next part.

Remark:
- Be aware that it is not possible to connect to NX when using a ED25519 keytype. The RSA4096 keytype does allow you to connect. As this is the recommended keytype for connections to the HPC clusters, this should not be an issue for most users.

Authentication with an agent
----------------------------

In order to circumvent the annoyances of multiple MFA prompts or connecting to the cluster in a ssh-client before being able to use certain apps like NX, you can use an agent. This agent will store a certificate that contains the identity verification you did when following the firewall link. This way, you will only be asked to verify your identity once. Of course this certificate does not live forever. When using the built-in ssh-agent of Linux and Mac this will be as long as your agent lives, and when using the vscagent this will be 16h. There are two ways in which the certificates are stored in an agent:

- Previously injected: the agent will automatically store the certificate when you first connect to the cluster in the way as described above (built-in ssh-agents for Mac and Linux, but also in a future release of Pageant on Windows).
- Explicitly loaded in the agent: storing the certificate happens by opening the UI of an agent, where you specifically ask to create a certificate. You will be redirected to the firewall link to verify your identity (vscagent).

To adopt any of these methods, read the following parts. The methods you can use varies based on your OS.

Authentication with an agent on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**NOTE:** Download the `vscagent`_ here.

For MS-Windows systems the `vscagent`_ is available to serve as ssh-agent. It includes a “Renew VSC certificate” button that does exactly that to retrieve a certificate. Download the vscagent.exe file from the previously mentioned download link. If you have a centrally managed KU Leuven laptop, you should copy the vscagent.exe in your C:\\Workdir\\myapps and run it from there (create the folder if it does not exist on your system yet). For other machines, place it in a directory of your choice. Once opened, follow these steps:

- Go to the 'Configuration' tab:

  - For most users, the 'Enable KU Leuven server certificates' should be left **unchecked**. You should only check it and fill it in when you satisfy the next two conditions:
  
    - You are a KU Leuven user
    - You already use the KU Leuven server certificate. You are probably already using CertAgent in that case. Be aware that you can still keep using CertAgent next to the vscagent. You can add your credentials in the vscagent if you would prefer using only one agent. **If you have no idea what this means, you should skip the next step.**
    - If you have satisfied the previous two conditions and you would like to store your KU Leuven server certificate in your vscagent, check the 'Enable KU Leuven server certificates'. Otherwise proceed to the next step. Fill in the fields as follows:
  
      - Principals: uXXXXXX  
      - Role: kuleuven
      - TTL : 16h
      
  - check ‘Enable HPC user certificates‘
  - check ‘tier2-leuven’. 'tier1-leuven' is only for access to Breniac, which is unavaible for the majority of users.
  - Username : vscXXXXX
  - Save configuration file

- Go to the 'SSH key(s)' tab

  - point to your private VSC-key

- Request a certificate

  - Go to the ‘SSH identities’ tab
  - click 'Renew certificate'
  - Select ‘HPC Tier2 Leuven certificate’ for the certificate for the Tier2 cluster
  - If you are storing your KU Leuven server certificate in this agent as well, you can also renew the ‘KU Leuven server certificate’

The agent will automatically open the firewall link in your browser. Here you can verify your identity. You are now able to connect to the cluster using any ssh-client or with UI apps like NX and FileZilla. it might be that you have to adapt some options in the configuration of these apps. Have a look at the 'Configuration of ssh-clients and UI apps' below.

Authentication with an agent on Linux/Mac
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Linux and Mac you can use the built-in ssh-agent. If you would prefer a user interface, you can also use the the previously mentioned vscagent.
Instead of downloading 'vscagent.exe' download 'vscagent' and run 'vscagent gui'and follow the above procedure to configure it.
**Be aware that the vscagent does not work for Macs with an M1 processor!**

If you prefer using the built-in ssh-agent, use the following instructions to configure it correctly. First of all, verify that it is running. You can do this by executing:: 

    ssh-add -l

If the agent is not running, you will get a 'Could not open a connection to your authentication agent.' message. In this case you can start the agent with::

    eval $(ssh-agent)

(to kill the agent use ``eval "$(ssh-agent -k)"``)

If your agent is running, the ``ssh-add -l`` will show the identities that were added to the ssh-agent. If none are added, the output will state 'The agent has no identities.'. You can add your key with ``ssh-add </path/to/your/private/key>``. Now ``ssh-add -l`` should show your key.

Now, depending on how ssh is configured, it might be that your key will not be stored by default. It is probably best to verify the following steps before continuing:

#. Adapt or create a profile for your cluster connection in the config file in your .ssh folder. If you do not have a config file there, create one first. From your home dir::

   touch ~/.ssh/config
   chmod 600 ~/.ssh/config

In this file you can create a profile for each of your connections and add options specifically for that connection. For Tier-2::

   Host login.hpc.kuleuven.be
     ForwardAgent yes
     PubkeyAuthentication yes
     ChallengeResponseAuthentication yes
     PreferredAuthentications publickey,keyboard-interactive

The indentation is not strictly necessary, but is recommended for readability.

If you now connect to the cluster using your standard 'ssh' command, the certificate will automatically be stored for as long as your agent lives. If you want to use apps that use ssh in the background (NX, FileZilla), you will have to do this connection to the cluster as well. You are free to log out of that session afterwards. 

Remark:
- You might have to adapt some options in the configuration of your connection profiles in some apps. Have a look at 'Configuration of ssh-clients and UI apps' below.

Configuration of ssh-clients and UI apps
----------------------------------------

As you have probably not yet set up your ssh-client or other apps that use ssh to be able to use an agent, you might have to make some changes in your connection profiles. Similar apps will need similar changes, but here we shortly show what to do for MobaXTerm, PuTTY and NX:

- MobaXTerm

  - right-click on the user session you have created to connect to the Tier-2 cluster and choose 'Edit Session'
  - Select the 'Advanced SSH settings' tab
  - Uncheck 'Use private key' if selected
  - click 'Ok'
    
- PuTTY

  - Load your profile to connect to the Tier-2 cluster
  - Go to 'Auth' under 'Connection'
  - Be sure that 'Allow agent forwarding' is checked
  - If you have a private key file stored under 'Private key file for authentication', remove it
    
- NX

  - Right-click on the connection to the Tier-2 cluster
  - Click on 'Edit connection'
  - Select the 'Configuration' tab
  - Select 'Use key-based authentication with a SSH agent'
  - Click 'Modify' and verify that 'Forward authentication' is checked

Known issues - General remarks
------------------------------

#. It has happened that users cannot properly load the MFA URL. If that would happen to you, it is worth trying to paste the URL in a incognito browser window. This has only been verified to work in Chrome and does not seem to work in Firefox.
#. MobaXTerm: version 21.1 has known issues in combination with the vscagent. It does not always seem to find the certificate in your agent. Updating to the latest version should solve this.
#. If you are using sshfs, no link will be prompted to you as when using ssh. This is intended to be this way. The recommended approach would be to use an ssh agent to store your certificate. This will avoid you having to connect with the MFA link every time when connecting to the cluster.
#. Safari does not properly load the vscagent download page. 
#. Some ssh-clients have their own built-in agents that can prompt you the firewall link. You are free to use these instead of the vscagent as well. Be aware that Pageant (PuTTY agent) does not support this for the moment. If this would become standard practice in the future, we might adopt these as default agents instead of the vscagent.

.. _VSC firewall page: https://firewall.vscentrum.be
.. _vscagent: https://firewall.vscentrum.be/vscagent/latest/
