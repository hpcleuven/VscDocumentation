.. _firewall-based-certificate:

##########################
Firewall-based certificate
##########################

This is one of the two ways to obtain an SSH certificate described in
:ref:`Connecting with an SSH agent <mfa-with-ssh-agent>`.

* Start up your SSH agent.

  .. tab-set::
     :sync-group: operating-system

     .. tab-item:: Windows
        :sync: win

        We recommend using the
        :ref:`Windows OpenSSH agent <ssh agent windows>` for PowerShell
        or Command Prompt users, and :ref:`Pageant` otherwise.

     .. tab-item:: macOS
        :sync: mac

        Use the default :ref:`OpenSSH agent`.

     .. tab-item:: Linux
        :sync: lin

        Use the default :ref:`OpenSSH agent`.

* Add the certificate to your agent: 

  .. tab-set::
     :sync-group: vsc-sites

     .. tab-item:: KU Leuven/UHasselt
        :sync: kuluh

        Connect to either the cluster's login node or to
        ``firewall.vscentrum.be``. With e.g. OpenSSH you can do:

        .. code-block:: bash

           ssh -A vsc98765@login.hpc.kuleuven.be
           # or
           ssh -A vsc98765@firewall.vscentrum.be

     .. tab-item:: Tier-1 sofia
        :sync: sofia

        Connect to ``firewall.vscentrum.be``. With e.g. OpenSSH you can
        do:

        .. code-block:: bash

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

  |kuluh| For KU Leuven users, the page looks like the following:

  .. _idp_page:
  .. figure:: mfa_login/idp_page.PNG
     :alt: idp_page

* |kuluh| If you are already connected to the internal network, then you will be only asked to
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
