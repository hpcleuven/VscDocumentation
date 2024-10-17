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
SSH certificates agent. The firewall page method can be used without the need to set SSH
certificates with help of a certificates agent. The second method requires that first
the user gets a valid SSH session certificate and then proceeds with connecting to VSC.
Both methods employ MFA. The difference between the two is that the firewall authentication
will establish an active SSH certificate for a relatively short time and the user will be
asked to visit the VSC firewall page upon every subsequent connection attempt.
With the help of an SSH agent the proper certificates are valid for much longer and that
adds a lot of flexibility in using various applications used to connect to VSC.


MFA without an agent
--------------------

The following steps are applicable when you do not have an ssh agent running
and you want to log in to the cluster with an ssh client like PuTTY or
MobaXTerm. It also applies when using the ssh command in a terminal on Linux,
Mac, or WSL.

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

MFA with an agent
-----------------

Here we will show how users can acticate and store the SSH certificate in an SSH
agent. The VSC firewall and insiitutional login described above are also valid here.
The difference is that user will be required to perform them only once in order to 
set an active SSH certificate and which certificate will be stored in the running
SSH agent.

#. Make sure agent is running.
#. Open your SSH client and connect to the cluster.
#. You will be asked, depending on your system and network settings, to perform
   the authentication steps described above.
#. Upon successful connection the agent will automatically store your SSH certificate.
   The certificate will be active for a maximum of 16 hours. If you quit the agent
   before that then the stored certificates will be removed.

.. note::

    For `login[-tier1].hpc.kuleuven.be` only, a successful connection will
    white list your IP address for 90 days. Within that time frame, the first
    step mentioned above becomes optional.
    
.. note::

    The above method works fine to create the connection through MobaXTerm.
    The included file explorer will show you the files, but opening, downloading
    and uploading files from here does not work without the agent. If you would 
    like to use the file explorer, have a look at :ref:`Authentication with an ssh agent<mfa_agent>` . 

.. note::

    If you use PuTTY to login, highlighting the URL with your mouse/cursor will copy 
    it to your clipboard, and make it ready to paste into your browser.
    Therefore, do not use the Ctrl+C combination on your keyboard, or it will cancel 
    your login attempt.

GUI applications with SSH connection in the background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some applications such as FileZilla provide a Graphical User Interface
(GUI) that will setup an ssh connection under the hood. This leads to a problem
with step 3 from the last section, as those applications will typically not
prompt you the firewall URL (some applications like WinSCP will do this however).
To work around this, you should first login to the KU Leuven cluster with an
ssh-client on your machine as explained in the previous section. As long as you
keep this connection open, you can connect with the other apps as well. This
extra step can however also be avoided by using an ssh agent, which will be
explained in the next part.

.. note::

   This method will not always work for NX. It is highly recommended to use
   the method with an :ref:`ssh agent<mfa_agent>` when using MFA with NX.

.. note::

   It is currently not possible to connect to NX when using a ED25519 keytype.
   The RSA4096 keytype does allow you to connect. As this is the recommended
   keytype for connections to the HPC clusters, this should not be an issue for
   most users.

.. _mfa_agent:

Authentication with an ssh agent
--------------------------------

In order to circumvent the annoyance of multiple MFA prompts or connecting to
the cluster with an ssh client before being able to use certain apps like FileZilla,
you can use an agent. This agent will store a certificate that contains the
identity verification you did when following the firewall link. This way, you
will only be asked to verify your identity once. Of course this certificate
does not live forever. When using the built-in ssh-agent of Linux and Mac this
will be as long as your agent lives. 

Authentication with an agent on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Windows users, the recommended agent is Pageant which is automatically installed
together with PuTTY. Make sure you install version 0.78 or later.

Pageant stores the certificates together with your private SSH keys, which allows you
to use VSC facilities whenever you are prompted for your identity.
To setup your Pageant, please refer to :ref:`Using Pageant <using Pageant>`.

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

(to kill the agent use ``eval "$(ssh-agent -k)"``)

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

Configuration of ssh-clients and GUI apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have not yet set up your ssh-client or other apps that use ssh to be
able to use an agent, you might have to make some changes in your connection
profiles. Different apps will need different changes, but here we shortly show
what to do for MobaXTerm, PuTTY and NX:

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

- It has happened that users cannot properly load the MFA URL. If that would
  happen to you, it is worth trying to paste the URL in an incognito browser
  window. This has only been verified to work in Chrome and does not seem to
  work in Firefox.
- If you are using ``sshfs``, no link will be prompted to you as when using ``ssh``.
  This is intended to be this way. The recommended approach would be to use an
  ssh agent to store your certificate. This will avoid you having to connect
  with the MFA link every time when connecting to the cluster.

.. _VSC firewall page: https://firewall.vscentrum.be

