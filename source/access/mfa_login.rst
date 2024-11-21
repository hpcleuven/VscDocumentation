.. _mfa_leuven:

Multi Factor Authentication (MFA)
=================================

|KUL| Multi Factor Authentication (MFA) is an augmented level of security.
As the name suggests, MFA requires additional steps with human intervention
when authenticating.
MFA is mandatory for accessing KU Leuven infrastructures.
This document provides two methods to connect to the KU Leuven clusters with MFA.

The first method, *without* an :ref:`SSH agent <SSH agent>`, is easier to get started with,
but requires some repetitive steps with each connection, hence inconvenient on a long run.

The second method involves an :ref:`SSH agent <SSH agent>` and requires a few more
steps to set up. This approach is however more convenient in the long run because
a single authentication will suffice for multiple connections throughout the day,
without further intervention.

Below, we elaborate on these two approaches.

.. note::

   When connecting from abroad, you first need to login via the `VSC firewall page`_.

.. _mfa quick start:

Connecting without an SSH agent
-------------------------------

First of all, choose whether you want to login to the `VSC firewall page`_,
:ref:`Open OnDemand portal <ood_t2_leuven>`, or to the :ref:`Tier-2 login <tier2_login_nodes>`
page using a text-based terminal (such as PuTTY or MobaXterm).

.. tab-set::

   .. tab-item:: VSC firewall page

      Proceed to the `VSC firewall page`_ on your browser.

   .. tab-item:: Open OnDemand

      Proceed to the :ref:`Open OnDemand portal <ood_t2_leuven>`.
      If you are affiliated with KU Leuven, click on the KU Leuven logo.
      Otherwise, click on the VSC logo to proceed to the authentication page.

   .. tab-item:: text-based terminal

      You login via terminal (or PuTTY or MobaXterm) to one of the
      :ref:`Tier-2 login nodes <tier2_login_nodes>`.
      You are prompted with a login link:

      .. _firewall_link_mfa:
      .. figure:: mfa_login/firewall_link_mfa.PNG
         :alt: firewall_link_mfa

      Copy-paste the provided link in a browser and follow it.
      Note that when using PuTTY or MobaXterm, simply highlighting the link with your
      mouse will copy the URL to your clipboard.
      Avoid using 'CTRL-C', or it will send a ``SIGINT`` signal interrupting
      your process instead of performing a copy operation.

- From the drop-down menu, choose the institute you are affiliated with.

  .. figure:: mfa_login/vsc_firewall_institute.PNG
     :alt: Choose your institute

- You will be forwarded to the identity provider (IDP) of your institute,
  and you need to login in a usual way using your registered credentials.
  For KU Leuven users, the page looks like the following:

  .. _idp_page:
  .. figure:: mfa_login/idp_page.PNG
     :alt: idp_page

- If you are already connected to the internal network, then you will be only asked to
  identify yourself with the MFA of your choice, e.g, via a code sent to your registered
  phone, or an authenticator app:

  .. _reauthenticate_phone:
  .. figure:: mfa_login/reauthenticate_phone.PNG
     :alt: reauthenticate_phone

- Once you are successfully authenticated, you end up on a page telling you that your VSC 
  identity is confirmed.
  If you have already performed the previous login in that browser session, you will 
  immediately end up on this page:

  .. _firewall_confirmed:
  .. figure:: mfa_login/firewall_confirmed.PNG
     :alt: firewall_confirmed

  This step may not be necessary when connecting from a white-listed IP address,
  like the internal networks of the Flemish universities, using a static on-site
  IP as well as the insututional VPN.
  For example, if you have already logged upfront into your institution network
  then you might not be required to log in again depending on your browser
  session settings (e.g., accepted cookies).

- Go back to your browser, SSH client or terminal.
  You should now be connected to a login node on the cluster or to the OnDemand web portal,
  respectively.
  E.g. for a PuTTY session, a successful login is rewarded with
  a welcome message:

   .. _login_node:
   .. figure:: mfa_login/login_node.PNG
      :alt: login_node

That's it! You can continue doing your HPC work as usual.

.. note::

   For ``login.hpc.kuleuven.be`` only, a successful connection will whitelist
   your IP address for 90 days.
   Within that time frame, visiting the `VSC firewall page`_ might be optional.

.. _mfa-with-ssh-agent:

Connecting with an SSH agent
----------------------------

It is a common practice that Windows/Linux/MacOS users use different SSH clients
or GUI apps in order to interact with the HPC infrastructures.
The standard login method will prompt you the MFA URL every time you try to connect to the
:ref:`login nodes <tier2_login_nodes>`. 
However, not all SSH clients prompt you the firewall link.
While this can be cumbersome, setting up an SSH agent and generating an SSH certificate will
avoid all this.
Examples of such apps are :ref:`FileZilla <FileZilla>` or :ref:`NoMachine <NX start guide>`.
Now, you have two possibilities:

- For using some apps (such as NoMachine and FileZilla), it is possible to first connect to
  the cluster using PuTTY or terminal.
  Once your terminal connection succeeds, your :ref:`SSH agent <SSH agent>` will hold your
  SSH certificate.
  Eventually, the certificate is used by NoMachine or FileZilla to complete the authentication.

- Another method is contacting the `VSC firewall page <https://firewall.vscentrum.be>`_
  with PuTTY or terminal, while the 'agent forwarding' is enabled.
  PuTTY users find the agent forwarding option under the 'Connection -> SSH -> Auth' tab.
  The Linux/MacOS users can execute the following command:

  .. code-block:: bash

     ssh -A vsc98765@firewall.vscentrum.be

  When authenticating via the VSC firewall page, you will not land on a login node.
  This has an advantage when using other SSH clients such as NX or FileZilla.

  In either case, while the connection is pending, you need to copy/paste the URL into your browser.
  Once you are asked: 'Are you trying to log in from <IP address>? YES / NO',
  click 'YES'. This approach is recommended for FileZilla and NoMachine users.

- However, we encourage the users to setup an :ref:`SSH agent <SSH agent>`, because
  SSH clients can be configured to work seamlessly with an agent.
  
Below, we provide a brief listing of few SSH clients.
Please refer to the documentation page for each app for a correct setup of your
SSH agent with the provided link.

=========================================== ==================== =====================
SSH Client name                             Purpose              Operating System
=========================================== ==================== =====================
:ref:`PuTTY <text mode access using PuTTY>` text-based terminal  Windows
:ref:`MobaXterm <access using mobaxterm>`   text-based terminal  Windows
:ref:`NoMachine <NX start guide>`           graphical desktop    Windows, Linux, MacOS
:ref:`FileZilla <FileZilla>`                file transfer        Windows, Linux, MacOS
=========================================== ==================== =====================

Setting up an SSH agent for MFA
-------------------------------

The setup for your SSH agent depends on the choice of the operating system on your local machine,
and that falls under either of the following two categories:

-	Windows machines
-	Linux or macOS machines 

Windows machines
~~~~~~~~~~~~~~~~

Windows users are recommended to use Pageant as an SSH agent.
For detailed information, please refer to the dedicated page about 
:ref:`Using Pageant <using Pageant>`. 

Linux and Mac machines
~~~~~~~~~~~~~~~~~~~~~~

On Linux and MacOS it is common to use OpenSSH, which is commonly integrated in the
local operating system.
For detailed information, please refer to :ref:`setting up your SSH agent for Linux and MacOS <SSH agent>`.
Below, we provide recommendations on incorporating MFA in your new or existing SSH setup.

- Before using your agent, it is best to verify the state of your agent.
  Open a terminal. Verify if your agent is running with ``ssh-add -l``. 
  If it is not running you will get the following error: 
  ``Could not open a connection to your authentication agent``

  If this is the case, start your agent with ``eval $(ssh-agent)``

- You now need to create or adapt a profile for the cluster in your
  ~/.shh/config file.
  If you notice you do not have this file yet, create it
  with the following command, you should adapt the permissions as well::

     touch ~/.ssh/config
     chmod 600 ~/.ssh/config
   
- Open your ``~/.ssh/config`` with a text editor, and make sure it looks like this::

     Host login.hpc.kuleuven.be
       ForwardAgent yes
       PubkeyAuthentication yes
       ChallengeResponseAuthentication yes
       PreferredAuthentications publickey,keyboard-interactive
        
- You can now ``ssh`` to the cluster.
  Upon the first successful connection, a so-called SSH certificate will be
  produced and injected back into the SSH agent.
  The SSH agent keeps the certificate while it runs silently in the background.
  Bear in mind that the certificates are valid for maximum 16 hours.

