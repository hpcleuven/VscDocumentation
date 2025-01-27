.. _mfa_leuven:

Multi Factor Authentication (MFA)
=================================

Multi Factor Authentication (MFA) is an augmented level of security.
As the name suggests, MFA requires additional steps with human intervention
when authenticating.

MFA is mandatory for accessing the :ref:`terminal interface` on the following
VSC clusters:

.. include:: clusters_mfa.rst

.. note::

   If you are connecting from abroad, it is necessary that you first authorize
   your own connection on the `VSC Firewall`_

Login to Open OnDemand
----------------------

Users from all VSC sites can access the Open OnDemand portal at KU Leuven site.
For that, proceed to the :ref:`Open OnDemand portal <ood>`.
If you are affiliated with KU Leuven, click on the KU Leuven logo.
Otherwise, click on the VSC logo to choose your institute.
You will be then forwarded to the Identity Provider (IdP) of your institute to
complete the authentication procedure.
Once that succeeds, you will automatically login to the Open OnDemand homepage.

.. _mfa-with-ssh-agent:

Connecting with an SSH agent
----------------------------

Using an :ref:`ssh agent` allows to store so-called SSH certificates which then
are made available to any other client program needing to use that same connection.
Getting an SSH certificate involves MFA but this only needs to be performed
once since a certificate can be used multiple times as long as it remains valid.

You can acquire such an SSH certificate as follows:

* Start up your SSH agent
  
  * Windows: we recommend to use :ref:`Pageant`
  * macOS: use the default :ref:`OpenSSH agent`
  * Linux: use the default :ref:`OpenSSH agent`

* Connect to either the cluster's login node or to ``firewall.vscentrum.be``
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

* You will then be shown a URL which you will need to open in a browser:

  .. _firewall_link_mfa:
  .. figure:: mfa_login/firewall_link_mfa.PNG
     :alt: firewall_link_mfa

  Note that when using PuTTY or MobaXterm, simply highlighting the link
  with your mouse will copy the URL to your clipboard.
  Avoid using 'CTRL-C', or it will send a ``SIGINT`` signal interrupting
  your process instead of performing a copy operation.

* From the drop-down menu, choose the institute you are affiliated with.
  Below, we show an example of a KU Leuven user, but one has to pick the
  institute he/she is affiliated with.

  .. figure:: mfa_login/vsc_firewall_institute.PNG
     :alt: Choose your institute

* You will be forwarded to the Identity Provider (IdP) of your institute,
  and you need to login in a usual way using your registered credentials.
  For KU Leuven users, the page looks like the following:

  .. _idp_page:
  .. figure:: mfa_login/idp_page.PNG
     :alt: idp_page

* If you are already connected to the internal network, then you will be only asked to
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

* Once you are successfully authenticated, you end up on a page telling you that your VSC 
  identity is confirmed.
  If you have already performed the previous login in that browser session, you will 
  immediately end up on this page:

  .. _firewall_confirmed:
  .. figure:: mfa_login/firewall_confirmed.PNG
     :alt: firewall_confirmed

* An SSH certificate will now be injected back into the agent.

That's it! You can continue doing your HPC work as usual.

The certificate can be used as long as the agent remains alive and the
certificate itself has not expired (they have a lifetime of 16 hours).
Do not forget to set up your client so that it contacts your SSH agent
when opening new connections (thereby making use of the certificates).
For a few common clients the corresponding documentation pages are listed
below.

====================================== ==================== =====================
SSH Client name                        Purpose              Operating System
====================================== ==================== =====================
:ref:`OpenSSH <OpenSSH access>`        text-based terminal  Linux, macOS
:ref:`PuTTY <terminal putty>`          text-based terminal  Windows
:ref:`MobaXterm <terminal mobaxterm>`  text-based terminal  Windows
:ref:`NoMachine <NX start guide>`      graphical desktop    Windows, Linux, macOS
:ref:`FileZilla <FileZilla>`           file transfer        Windows, Linux, macOS
====================================== ==================== =====================


.. _mfa quick start:

Connecting without an SSH agent
-------------------------------

Most clients (such as PuTTY or MobaXterm) can also be made to work *without*
an :ref:`ssh agent`. Keep in mind, however, that this approach tends to be
less convenient since each new connection will require multi-factor
authentication.

Certain clients (such as :ref:`FileZilla <FileZilla>`, ``sshfs`` or
:ref:`NoMachine <NX start guide>`) furthermore do not show you the firewall
link needed for the MFA and hence can only function in combination with an SSH
agent holding an SSH certificate.

This being said, the agentless procedure runs as follows:

* Connect to a :ref:`Tier-2 login node <tier2_login_nodes>`
  using your chosen client application (e.g. MobaXterm).

* The application is then supposed to show the link to complete the MFA procedure
  (similar to the previous section).

* After passing the MFA challenge, you should now be connected to a login node.
  In plain SSH connections a successful login is rewarded with a welcome message:

  .. _login_node:
  .. figure:: mfa_login/login_node.PNG
     :alt: login_node


