.. _terminal putty:

####################
Terminal using PuTTY
####################

Prerequisite
============

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      To access KU Leuven clusters, only an approved
      :ref:`VSC account<access>` is needed.

   .. tab-item:: UAntwerpen
      :sync: ua

      To access clusters hosted at these sites, you need a
      :ref:`public/private key pair <create key pair>` of which the public key
      needs to be :ref:`uploaded via the VSC account page <upload public key>`.

   .. tab-item:: UGent
      :sync: ug

      To access clusters hosted at these sites, you need a
      :ref:`public/private key pair <create key pair>` of which the public key
      needs to be :ref:`uploaded via the VSC account page <upload public key>`.

   .. tab-item:: VUB
      :sync: vub

      To access clusters hosted at these sites, you need a
      :ref:`public/private key pair <create key pair>` of which the public key
      needs to be :ref:`uploaded via the VSC account page <upload public key>`.

.. _putty install:

Installation
============

`PuTTY`_ is a Windows program that has to be installed on your computer. Open
`PuTTY's download page <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`__
and download the *Package file* that corresponds to your system (usually 64-bit
x86). Once the download completes, execute the downloaded ``.msi`` installer.
The installer will guide you through the rest of the installation.

Connecting to VSC clusters
==========================

When you start the PuTTY executable 'putty.exe', a configuration screen
pops up. Follow the steps below to setup the connection to (one of) the
VSC clusters.

.. warning::

   In the screenshots, we show the setup for user ``vsc98765`` to the
   genius cluster at KU Leuven via the login node ``login.hpc.kuleuven.be``.
   Please keep in mind to:

   #. replace ``vsc98765`` with your own VSC user name

   #. replace ``login.hpc.kuleuven.be`` with the name of the login node of the
      VSC cluster you want to access, which can be found in the cluster
      description on :ref:`tier1 hardware` or :ref:`tier2 hardware`

* Within the category 'Session', in the field 'Host Name', type in a valid
  hostname of the :ref:`Tier-1<tier1 hardware>` or
  :ref:`Tier-2<tier2 hardware>` VSC cluster you want to connect to.

  .. figure:: putty_access/text_mode_access_using_putty_01.png

* In the category *Connection* > *Data*, in the field 'Auto-login
  username', put in <vsc-account>, which is your VSC username that you
  have received by mail after your request was approved.

  .. figure:: putty_access/text_mode_access_using_putty_02.png

* Based on the destination VSC site that you want to login to, choose one of the
  tabs below and proceed.

  .. tab-set::
     :sync-group: vsc-sites

     .. tab-item:: KU Leuven/UHasselt
        :sync: kuluh

        Select the *SSH* > *Auth* > *Credentials* tab, and remove any private
        key from the box 'Private key file for authentication'.

        .. figure:: putty_access/putty_priv_key.png
           :alt: putty private key

        In the category *Connection* > *SSH* > *Auth*, make sure that the
        option 'Attempt authentication using Pageant' is selected.
        It is also recommended to enable agent forwarding by ticking the
        'Allow agent forwarding' checkbox.

        .. figure:: putty_access/text_mode_access_using_putty_03.png

     .. tab-item:: UAntwerpen
        :sync: ua

        In the category *Connection* > *SSH* > *Auth* > *Credentials*, click on
        'Browse', and select the private key that you generated and saved above.

        .. figure:: putty_access/text_mode_access_using_putty_04.png

        Here, the private key was previously saved in the folder
        ``C:\Users\Me\Keys``.
        In older versions of Windows, you would have to use
        ``C:\Documents and Settings\Me\Keys``.

     .. tab-item:: UGent
        :sync: ug

        In the category *Connection* > *SSH* > *Auth* > *Credentials*, click on
        'Browse', and select the private key that you generated and saved above.

        .. figure:: putty_access/text_mode_access_using_putty_04.png

        Here, the private key was previously saved in the folder
        ``C:\Users\Me\Keys``.
        In older versions of Windows, you would have to use
        ``C:\Documents and Settings\Me\Keys``.

     .. tab-item:: VUB
        :sync: vub

        In the category *Connection* > *SSH* > *Auth* > *Credentials*, click on
        'Browse', and select the private key that you generated and saved above.

        .. figure:: putty_access/text_mode_access_using_putty_04.png

        Here, the private key was previously saved in the folder
        ``C:\Users\Me\Keys``.
        In older versions of Windows, you would have to use
        ``C:\Documents and Settings\Me\Keys``.

* In the category Connection > SSH > X11, click the 'Enable X11 Forwarding'
  checkbox:

  .. _putty x11 forwarding:

  .. figure:: putty_access/text_mode_access_using_putty_05.png

* Now go back to the 'Session' tab, and fill in a name in the 'Saved Sessions'
  field and press 'Save' to permanently store the session information.

* To start a session, load it from Sessions > Saved Sessions, and click 'Open'.

  .. _putty_load_saved_session:
  .. figure:: putty_access/putty_load_saved_session.png
     :alt: putty_load_saved_session

  .. tab-set::
     :sync-group: vsc-sites

     .. tab-item:: KU Leuven/UHasselt
        :sync: kuluh

        You will be then prompted to copy/paste the firewall link into your
        browser and complete the :ref:`Multi Factor Authentication (MFA) <mfa_leuven>`
        procedure. With PuTTY, users only need to highlight the link with their
        mouse in order to copy it to the clipboard.

        .. figure:: putty_access/putty_mfa.png
           :alt: PuTTY MFA URL

        Then, with the right-click from your mouse or CTRL-V, you can paste the MFA link
        into your browser to proceed with the authentication to ``login.hpc.kuleuven.be``.

     .. tab-item:: UAntwerpen
        :sync: ua

        Now pressing 'Open' should ask for your passphrase, and connect
        you to ``login.hpc.uantwerpen.be``.

     .. tab-item:: UGent
        :sync: ug

        Now pressing 'Open' should ask for your passphrase, and connect
        you to ``login.hpc.ugent.be``.

     .. tab-item:: VUB
        :sync: vub

        Now pressing 'Open' should ask for your passphrase, and connect
        you to ``login.hpc.vub.be``.

The first time you make a connection to the login node, a Security Alert
will appear and you will be asked to verify the authenticity of the
login node.

.. figure:: putty_access/text_mode_access_using_putty_06.png

For future sessions, just select your saved session from the list and
press 'Open'.

Managing SSH keys with Pageant
==============================

At this point, we highly recommend setting up an :ref:`ssh agent`. A widely
used SSH agent is :ref:`Pageant` which is installed automatically with PuTTY.

Pageant can be used to manage SSH keys and certificates for multiple clients,
such as PuTTY, :ref:`WinSCP<WinSCP transfer>`, :ref:`FileZilla<FileZilla>`,
as well as the :ref:`NX client for Windows<NX start guide>` so that you don't
need to enter the passphrase all the time.

:ref:`pageant`

Proxies and network tunnels to compute nodes
============================================

Network communications between your local machine and some node in the cluster
other than the login nodes will be blocked by the cluster firewall. In such a
case, you can directly open a shell in the compute node with an SSH connection
using the login node as a proxy or, alternatively, you can also open a network
tunnel to the compute node which will allow direct communication from software
in your computer to certain ports in the remote system. This is also useful to
run client software on your Windows machine, e.g., ParaView or Jupyter
notebooks that run on a compute node.

.. toctree::

   putty_ssh_proxy
   putty_ssh_tunnel

.. _troubleshoot_putty:

Troubleshooting PuTTY connection issues
=======================================

If you have trouble accessing the infrastructure, the support staff will
likely ask you to provide a log.  After you have made a failed attempt to connect,
you can obtain the connection log by

#. right-clicking in PuTTY's title bar and selecting **Event Log**.

#. In the dialog window that appears, click the **Copy** button to copy the
   log messages.  They are copied as text and can be pasted in your message
   to support.
