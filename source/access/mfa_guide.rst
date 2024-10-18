.. _mfa_guide:

MFA Guide
=========

General information
-------------------

Mutli-Factor Authentication (MFA) is mandatory when connecting to the VSC network.
In the context of SSH connections it sets an increased level of security by requiring
an additional verification step. MFA ensures that even if an attacker obtains your SSH login
credentials, such as username and password, they won’t be able to access the VSC netowrk
without that additional authentication factor.

Currently, there are two ways to connect to VSC: via the `VSC firewall page`_ and via
SSH certificates. The firewall page method can be used without the need to set SSH
certificates with help of a certificate agent. The second method requires that first
the user gets a valid SSH session certificate and then proceeds with connecting to VSC.
Both methods employ MFA. The difference between the two is that the firewall authentication
will establish an active SSH certificate for a relatively short time and the user will be
asked to visit the VSC firewall page upon every subsequent connection attempt.
With the help of an SSH agent the proper certificates are valid for much longer and that
adds a lot of flexibility in using various applications used to connect to VSC.

.. _mfa_no_agent:

MFA without an agent
--------------------

The following steps are applicable when you do not have an ssh agent running
and you want to log in to the cluster with an ssh client like PuTTY or
MobaXTerm. It also applies when using the ssh command in a terminal on Linux,
Mac, or Windows Subsystem for Linux (WSL).

#. Visit the `VSC firewall page`_ 
#. [optional] Login with your institution credentials.
   This step may not be necessary when connecting from a white-listed IP address,
   e.g., the Flemish universities internal networks such as static on-site
   IP as well as the insututional VPN.
   For example, if you have already logged upfront into your institution network
   then you might not be required to log in again depending on your browser
   session settings (e.g., accepted cookies). In that case you will only be
   asked to confirm the firewall login via your selected choice for MFA.
#. You will be asked to authorize the firewall request. Click 'Authorize'.
#. You will now see a confirmation that you have successfully logged in.
#. Proceed with the SSH terminal client of your choice to connect to VSC.

Note: The firewall authentication is **mandatory** when you are connecting from abroad.

.. _mfa_agent:

MFA with an agent
-----------------

Users can also, upon establishing an SSH connection, store the SSH certificate in an SSH agent.
The VSC firewall and institutional login steps described above are also valid here.
The difference is that the user will be required to perform them only once in order to 
set an active SSH certificate which will be then stored in the running SSH agent.
Here are the necessary steps:

#. Make sure the agent is running.
#. Open your SSH client and connect to the cluster.
#. You will be asked, depending on your system and network settings, to perform
   the authentication steps described above.
#. Upon successful connection the agent will automatically store your SSH certificate.
   The certificate will be active for a maximum of 16 hours. If you quit the agent
   before that then the stored certificates will be removed.

For a more thorough explanation on how to set up an agent on Windows and Mac OSx/Linux
machines please take a look at the following section below.
The necessary steps have also been described in details in :ref:`mfa quick start`.

.. _mfa_agent_windows:

Authentication with an agent on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Windows users, the recommended agent is Pageant which is automatically installed
together with PuTTY. Make sure you install version 0.78 or later.

Pageant stores the certificates together with your private SSH keys, which allows you
to use VSC facilities whenever you are prompted for your identity.
To setup your Pageant, please refer to :ref:`Using Pageant <using Pageant>` in
the :ref:`mfa quick start`, or go to the respecitive section further below :ref:`mfa_client_config`.
Reminder: in order to store the session SSH certificate make sure Pageant
is already up and running in the background before attempting a conneciton with Putty.

.. _mfa_agent_nix:

Authentication with an agent on Linux/Mac/WSL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Linux, Mac, and WSL you can use the SSH agent included in the OpenSSH package
by following these instructions to configure it correctly.

.. note::
   Before starting out with the built-in SSH agent, you should know that using an SSH agent
   poses a possible security threat when you are not using this with care. When using an
   SSH agent for a connection to a remote server, all certificates that are stored in your agent
   are visible for root users on the remote server. So be sure to **only** use the agent
   for trusted servers. If you would prefer more secure set-ups, have a look at 
   :ref:`Secure your SSH agent set-up<secure_ssh_agent>` .

First of all, verify that your agent is running. You can do this by executing:: 

    ssh-add -l

If the agent is not running, you will get a
``Could not open a connection to your authentication agent.`` message. In this
case you can start an instance of the agent with::

    eval $(ssh-agent)

.. note::
   If you start your agent in this way, it is only accessible within the context of your 
   current shell. If you want to connect with NoMachine NX, you should also start your 
   NoMachine client from within this shell via the ``nxplayer`` command. Otherwise it will 
   not be able to access the certificate stored in your agent.

If your agent is running, the ``ssh-add -l`` will list the identities that were
added to the ssh-agent. If none are added, the output will state
``The agent has no identities.``. You can add your key with::

    ssh-add </path/to/your/private/key> 
    
Now ``ssh-add -l`` should show your key.

Depending on how ssh is configured, it might be that your key will not be
stored by default. It is probably best to verify the following steps before
continuing:

#. Adapt or create a profile for your cluster connection in the config file in
   your ``.ssh`` folder. If you do not have a config file there, create one first.
   From your home dir::

      touch ~/.ssh/config
      chmod 600 ~/.ssh/config

#. In this file you can create a profile for each of your connections and add
   options specifically for that connection. For Tier-2::

      Host login.hpc.kuleuven.be
        ForwardAgent yes
        PubkeyAuthentication yes
        ChallengeResponseAuthentication yes
        PreferredAuthentications publickey,keyboard-interactive

The indentation is not strictly necessary, but is recommended for readability.

If you now connect to the cluster using your standard ``ssh`` command, the
certificate will automatically be stored for as long as your agent lives. 

If you want to use apps that use ``ssh`` in the background (NX, FileZilla), you 
should also first inject a certificate in your agent before trying to connect.
This can be done by connecting to the VSC firewall page with agent forwarding::

    ssh -A vsc12345@firewall.vscentrum.be

.. note::

   You might have to adapt some options in the configuration of your
   connection profiles in some apps. Have a look at
   :ref:`Configuration of ssh-clients and UI apps<mfa_client_config>` below. 
   
.. _secure_ssh_agent:   

Secure your SSH agent set-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are ways to protect yourself from possible malicious attempts
to use certificates stored in your SSH agent on your local machine. A root user
on any remote server can access those certificates, and can use those to connect
to the remote servers for which you also have a certificate stored in your agent, 
and this connection will happen in your name. Luckily, as the agent only lives
for a limited time this threat also only exists for a limited time.
You also don't expose your private key.

Before diving into the technical settings, the first step to ensure your security,
is vigilance. Think about what connections could potentially pose a risk. Avoid
adding those to your agent. When connecting to our cluster you set up the agent
to avoid that you need to follow the firewall link every time. If you see no special
need for using an agent, it is probably better to avoid it.

If you do wish to use multiple certificates in your agent, you can also add
your key to your agent using::

    ssh-add -c /path/to/your/private/key
    
The ``-c`` will ask for a confirmation every time you (or in the worst case someone
else in your name) tries to use the agent to connect to a remote server. You will
manually have to click ``ok`` before. You might have to install the package ``ssh-askpass``
on your local machine first.

.. _mfa_client_config:

GUI applications with SSH connection in the background
------------------------------------------------------

Some applications such as MobaXTerm and FileZilla provide a Graphical User Interface
(GUI) which makes them very useful when connecting to remote sites. However,
such an application may not always prompt you to copy/paste the VSC firewall link to
set up the necessary SSH certificate.

Therefore, one way to connect to VSC is to first connect with an ssh-client 
on your machine as explained in the previous sections.
In the case of not having an SSH certificate agent running then as long as you
keep that connection open you can connect with the other apps as well.
In case you have already stored the SSH certificate in a running agent
you can then proceed with connecting to VSC with the application.

.. note::

   Some GUI applications may not always work when connecting to VSC
   without an agent. For example, NX is one of them.
   Therefore, it is highly recommended in such cases to use the agent
   connection method :ref:`ssh agent<mfa_agent>`.

Configuration of ssh-clients and GUI apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have not yet set up your ssh-client or other apps that use ssh to be
able to use an agent, you might have to make some changes in your connection
profiles. Different apps will need different changes. For an explanation
with screenshots for the various GUI apps please refer to :ref:`mfa quick start`.
Here below we shortly show what to do for PuTTY, MobaXTerm, NX, and FileZilla:

- PuTTY

  - Under 'Session' in the tree menu enter the remote hostname. The default port is 22.
  - Under 'Connection/SSH' ensure the protocol is set to SSH.
  - Under 'Connection/SSH/Auth' ensure that using Pageant and agent forwarding are active.
  - Under 'Connection/SSH/Auth/Credentials' make sure that there are no private keys specified
    in the 'Private key file for authentication' field.
  - Go back to 'Session' and save your newly created session.
  - Now you can load and open it to connect to VSC.

- MobaXTerm

  - From the menu click on 'New session'.
  - Click on the 'SSH' tab and fill in the remote server hostname. The username 
  - can be left empty but then you will have to type it every time you want to connect.
  - Under the 'SSH' tab select the 'Advanced SSH settings' sub-tab and set the
    'SSH-Browser type' to 'SFTP protocol'.
  - Uncheck 'Use private key' if selected
  - click 'Ok'

  .. note::
  
     MobaXTerm can also import existing Putty Sessions. You can then right-click
     on an imported session to edit it. Make sure that the SSH settings are correct.
    
- NX

  - Right-click on the connection to the Tier-2 cluster
  - Click on 'Edit connection'
  - Select the 'Configuration' tab
  - Select 'Use key-based authentication with a SSH agent'
  - Click 'Modify' and verify that 'Forward authentication' is checked

- FileZilla

  - Under ‘File’ open the ‘Site Manager’ and click on ‘New Site’.
  - Set the protocol to 'SFTP - SHH File Transfer Protocol', enter the VSC hostname you wish to connect to,
  - set the logon type to 'Ask for password', and type your VSC username. The port field can be left empty.
    Usually for SFTP/SSH protocols the port is 22.
  - [optional] Under the ‘Advanced’ tab you can also set the directory you wish to open by default
    upon login, e.g, your 'VSC_DATA' by typing its full linux path.
  - Click 'Connect' to connect to VSC. You may be prompted to enter your SSH passphrase.

Known issues - General remarks
------------------------------

- It has happened that some users cannot properly load the MFA URL. If that would
  happen to you, it is worth trying to paste the URL in an incognito browser
  window. This has only been verified to work in Chrome and does not seem to
  work in Firefox.
- If you are using ``sshfs``, no link will be prompted to you as when using ``ssh``.
  This is intended to be this way. The recommended approach would be to use an
  ssh agent to store your certificate. This will avoid you having to connect
  with the MFA link every time when connecting to the cluster.

.. _VSC firewall page: https://firewall.vscentrum.be

