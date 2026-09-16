.. _mfa_login:

Multi Factor Authentication (MFA)
=================================

Multi Factor Authentication (MFA) is an augmented level of security.
As the name suggests, MFA requires additional steps with human intervention
when authenticating.

MFA is mandatory for accessing the :ref:`terminal interface` on the following
VSC clusters:

.. include:: clusters_mfa.rst

Login to Open OnDemand
----------------------

|KULUH|
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

.. note::

   Additional access restrictions (for instance when connecting from abroad
   or from a non-managed laptop) may apply, which require that you first
   authorize your connection on the `VSC Firewall`_. See
   :ref:`this page <location_access_restrictions>` for more information.

Using an :ref:`ssh agent` allows to store so-called SSH certificates which then
are made available to any other client program needing to use that same connection.
Getting an SSH certificate involves MFA but this only needs to be performed
once since a certificate can be used multiple times as long as it remains valid.

Both certificates below are accepted on:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`
       * Tier-2 :ref:`Mindwell <mindwell hardware>`

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`

       |sofia|

       * Tier-1 :ref:`sofia <sofia cluster>`

There are two ways to acquire such an SSH certificate:

.. toctree::
   :hidden:

   Smallstep certificate <mfa_login_smallstep>
   Firewall-based certificate <mfa_login_firewall>

.. grid:: 2
   :gutter: 4

   .. grid-item-card:: Firewall-based certificate
      :columns: 12 12 6 6
      :link: mfa_login_firewall
      :link-type: doc

      Works with any SSH client, including PuTTY and MobaXterm.

   .. grid-item-card:: Smallstep certificate
      :columns: 12 12 6 6
      :link: mfa_login_smallstep
      :link-type: doc

      Uses the ``step`` CLI. On Windows, only works from PowerShell or the
      Command Prompt, not from GUI clients such as PuTTY and MobaXterm.

Once you have a certificate loaded into your agent, it can be used as long
as the agent remains alive and the certificate itself has not expired (they
have a lifetime of 16 hours). Do not forget to set up your client so that
it contacts your SSH agent when opening new connections (thereby making use
of the certificates). For a few common clients the corresponding
documentation pages are listed below.

====================================== ==================== =====================
SSH Client name                        Purpose              Operating System
====================================== ==================== =====================
:ref:`OpenSSH <OpenSSH access>`        text-based terminal  Linux, macOS
:ref:`OpenSSH <windows_client>`        text-based terminal  Windows
:ref:`PuTTY <terminal putty>`          text-based terminal  Windows
:ref:`MobaXterm <terminal mobaxterm>`  text-based terminal  Windows
:ref:`FileZilla <FileZilla>`           file transfer        Windows, Linux, macOS
====================================== ==================== =====================

.. _mfa quick start:

Connecting without an SSH agent
-------------------------------

Most clients (such as PuTTY or MobaXterm) can also be made to work *without*
an :ref:`ssh agent`. Keep in mind, however, that this approach tends to be
less convenient since each new connection will require multi-factor
authentication.

Certain clients (such as :ref:`FileZilla <FileZilla>` or ``sshfs``)
furthermore do not show you the firewall
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


