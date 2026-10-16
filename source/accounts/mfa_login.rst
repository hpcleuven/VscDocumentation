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

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Users from all VSC sites can access the Open OnDemand portal at the KU
      Leuven site using multi-factor authentication (MFA), without requiring
      any additional setup or special action. For that, proceed to the
      :ref:`Open OnDemand portal <ood>`. If you are affiliated with KU
      Leuven, click on the KU Leuven logo. Otherwise, click on the VSC
      logo to choose your institute. You will then be forwarded to the
      Identity Provider (IdP) of your institute to complete the
      authentication procedure. Once that succeeds, you will
      automatically log into the Open OnDemand homepage.

   .. tab-item:: VUB
      :sync: vub

      Users from all VSC sites can access the VUB Open OnDemand portal
      using multi-factor authentication (MFA), without requiring any
      additional setup or special action.
      For that, proceed to the :ref:`Open OnDemand portal <ood>`.
      Select your institute from the dropdown menu. You will then be
      forwarded to the Identity Provider (IdP) of your institute to
      complete the authentication procedure. Once that succeeds, you
      will automatically log into the Open OnDemand homepage.

.. _mfa-with-ssh-agent:

Obtaining an SSH certificate
----------------------------

An SSH certificate is a short-lived credential that allows SSH-based client
tools, such as ``ssh``, ``scp``, ``sftp``, and tools that use SSH internally, to
authenticate to the VSC HPC clusters. Obtaining an SSH certificate requires
multi-factor authentication (MFA), but MFA is only required when the
certificate is issued or renewed. While the certificate remains valid, it can
be reused for multiple SSH connections without repeating the MFA procedure.
SSH certificates replace the previously used long-lived public/private SSH key
pairs as the credential used for authentication to the VSC HPC clusters.

.. warning:: |VUB| We recommend that all users switch to SSH certificates from
   now on. The current login method using private/public SSH key pairs will be
   disabled on **1 March 2027**.  If you use special or automated workflows,
   please test certificate-based access as soon as possible. If it does not
   work for your use case, contact us at hpc@vub.be so we can help.

.. note::

   Additional access restrictions (for instance when connecting from abroad
   or from a non-managed laptop) may apply, which require that you first
   authorize your connection on the `VSC Firewall`_. See
   :ref:`this page <location_access_restrictions>` for more information.

There are two ways to acquire such an SSH certificate:

.. toctree::
   :hidden:

   Firewall-based certificate <mfa_login_firewall>
   Smallstep certificate <mfa_login_smallstep>

.. grid:: 2
   :gutter: 4

   .. grid-item-card:: Firewall-based certificate
      :columns: 12 12 6 6
      :link: mfa_login_firewall
      :link-type: doc
      :class-card: border-info border-5

      Works with any SSH client, including PuTTY and MobaXterm.

   .. grid-item-card:: Smallstep certificate
      :columns: 12 12 6 6
      :link: mfa_login_smallstep
      :link-type: doc
      :class-card: border-info border-5

      Uses the ``step`` CLI. On Windows, only works from PowerShell or the
      Command Prompt, not from GUI clients such as PuTTY and MobaXterm.

VSC clusters that accept these certificates:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`wICE <wice hardware>`
       * Tier-2 :ref:`Mindwell <mindwell hardware>`

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`

       |sofia|

       * Tier-1 :ref:`sofia <sofia cluster>`

An :ref:`ssh agent` can store the certificate and make it available to these
client programs automatically. In some cases, agentless alternatives are also
available; see the certificate-based methods below.

Once you have a certificate loaded into your SSH agent, it can be used as long
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

