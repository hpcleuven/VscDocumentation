.. _mfa_leuven:

Multi Factor Authentication (MFA)
=================================

|KUL| Multi Factor Authentication (MFA) is an augmented level of security.
As the name suggests, MFA requires additional steps with human intervention
when authenticating.
MFA is mandatory for accessing KU Leuven infrastructures.
In this page, we explain how to login to the
:ref:`KU Leuven Open OnDemand portal <ood_t2_leuven>`, and how to use SSH clients
(such as PuTTY, terminal etc) with and without using an SSH agent.

.. note::

   When connecting from abroad, you first need to login via the
   `VSC firewall page <https://firewall.vscentrum.be>`_.

Login to Open OnDemand
----------------------

Users from all VSC sites can access the Open OnDemand portal at KU Leuven site.
For that, proceed to the :ref:`Open OnDemand portal <ood_t2_leuven>`.
If you are affiliated with KU Leuven, click on the KU Leuven logo.
Otherwise, click on the VSC logo to choose your institute.
You will be then forwarded to the Identity Provider (IdP) of your institute to
complete the authentication procedure.
Once that succeeds, you will automatically login to the Open OnDemand homepage.

.. _mfa quick start:

Connecting without an SSH agent
-------------------------------

Using SSH clients (such as PuTTY or terminal) is easier to setup *without*
an :ref:`SSH agent <SSH agent>`; however, on a long run, it involves repetitive authentication
which is not convenient.
Hence, we do not recommend this approach.
But, if you opt for this approach, here are the steps to follow:

- You login via terminal (or PuTTY or MobaXterm) to one of the
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
  Below, we show an example of a KU Leuven user, but one has to pick the
  institute he/she is affiliated with.

  .. figure:: mfa_login/vsc_firewall_institute.PNG
     :alt: Choose your institute

- You will be forwarded to the Identity Provider (IdP) of your institute,
  and you need to login in a usual way using your registered credentials.
  For KU Leuven users, the page looks like the following:

  .. _idp_page:
  .. figure:: mfa_login/idp_page.PNG
     :alt: idp_page

- If you are already connected to the internal network, then you will be only asked to
  identify yourself with the MFA authenticator app on your personal phone:

  .. _reauthenticate_phone:
  .. figure:: mfa_login/reauthenticate_phone.PNG
     :alt: reauthenticate_phone

  This step may not be necessary when connecting from a white-listed IP address,
  like the internal networks of the Flemish universities, using a static on-site
  IP as well as the institutional VPN.
  For example, if you have already logged upfront into your institution's network
  then you might not be required to log in again depending on your browser
  session settings (e.g., accepted cookies).

- Once you are successfully authenticated, you end up on a page telling you that your VSC 
  identity is confirmed.
  If you have already performed the previous login in that browser session, you will 
  immediately end up on this page:

  .. _firewall_confirmed:
  .. figure:: mfa_login/firewall_confirmed.PNG
     :alt: firewall_confirmed

- Go back to your browser, SSH client or terminal.
  You should now be connected to a login node on the cluster or to the OnDemand web portal,
  respectively.
  In plain SSH connections a successful login is rewarded with a welcome message:

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

SSH agents can store so-called SSH certificates which various client programs
(PuTTY, MobaXterm, NoMachine, FileZilla, WinSCP, ...) can then use to
authenticate.
Getting an SSH certificate also involves MFA but this only needs
to performed once since a certificate can be used multiple times as long as it
remains valid.
Certain clients (such as :ref:`FileZilla <FileZilla>` or
:ref:`NoMachine <NX start guide>`) furthermore do not show you the firewall
link needed for the MFA and hence can only function in combination with an SSH
agent holding an SSH certificate.

You can acquire such an SSH certificate as follows:

- Start up your SSH agent.
  Windows users are recommended to use :ref:`Pageant <using Pageant>`,
  while Linux and MacOS users can e.g. rely on :ref:`OpenSSH<SSH agent>`.

- Connect to either the cluster's login node or to ``firewall.vscentrum.be``
  with your terminal application of choice and with agent forwarding enabled.
  With e.g. OpenSSH you can do:

  .. code-block:: bash

     ssh -A vsc98765@login.hpc.kuleuven.be
     # or
     ssh -A vsc98765@firewall.vscentrum.be

  PuTTY users can find the agent forwarding option under the
  'Connection -> SSH -> Auth' tab.
  OpenSSH users may also automatically
  enable agent forwarding in their :ref:`SSH config file <ssh_config>`.

- This will provide a link to complete the MFA procedure (similar to the
  'text-based terminal' part of the previous section).

- An SSH certificate will now be injected back into the agent.

The certificate can be used as long as the agent remains alive and the
certificate itself has not expired (they have a lifetime of 16 hours).
Do not forget to set up your client so that it contacts your SSH agent
when opening new connections (thereby making use of the certificates).
For a few common clients the corresponding documentation pages are listed
below.

=========================================== ==================== =====================
SSH Client name                             Purpose              Operating System
=========================================== ==================== =====================
:ref:`PuTTY <text mode access using PuTTY>` text-based terminal  Windows
:ref:`MobaXterm <access using mobaxterm>`   text-based terminal  Windows
:ref:`NoMachine <NX start guide>`           graphical desktop    Windows, Linux, MacOS
:ref:`FileZilla <FileZilla>`                file transfer        Windows, Linux, MacOS
=========================================== ==================== =====================


