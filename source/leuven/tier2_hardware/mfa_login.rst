Multi Factor Authentication (MFA)
=================================

About
-----

Multi Factor Authentication (MFA) is an augmented level of security. Multi Factor Authentication (MFA) is an augmented level of security with multiple factors, as in the name. These factors are:

- A valid private key
- Access to an a VSC associated university account

The latter will be verified by prompting a VSC firewall link when trying to ssh to one of our KU Leuven clusters. When following this link, you will be asked to choose your university, and log in. If you already did that in a browser session (to access any other university-related websites), you do not need to log in again. If the login was succesfull, you will be redirected to a firewall.vscentrum.be page, with the message that your vsc identity was confirmed.

The benefits of this method are:

- keys without passphrase are less of a security problem
- users can't share keys
- users won't be able to connect if the university account is no longer valid

If there are any questions, remarks, potential bugs, experiences with workflows for other clients…, please send them to the HPC helpdesk: hpcinfo@kuleuven.be. 


What do you need to use MFA on your vsc-account
-----------------------------------------------

With our MFA enabled login nodes, you can access the cluster in following ways:

- With ssh key + MFA prompt from IP addresses in any KU Leuven address range, any known LAN balancer address of other Flemish universities, any Belgian residential network, or a list of known institutes or organizations.
- With ssh key only from IP addresses on which :ref:`vsc firewall page<firewallpage>` is opened and that are also in a KU Leuven address range or a Belgian residential network.
- With ssh key + confirmation from IP addresses on which :ref:`vsc firewall page<firewallpage>` is opened and that are not in a KU Leuven address range and neither in a Belgian residential network. This confirmation is the same as the MFA prompt, but can also be answered by a popup on the HPC firewall page that the user has opened.
- (only on login[-tier1].hpc.kuleuven.be) With ssh key + MFA prompt if connecting from any other IP address that was already seen during the last 90 days (so a user can open :ref:`vsc firewall page<firewallpage>` manually once, and then connect each month directly with the MFA prompt).

MFA Authentication without an agent
-----------------------------------

When you try to login to the cluster and you have no vsc-agent running:

- start any SSH session to a KU Leuven cluster and authenticate with your private vsc-key
- your ssh connection will prompt you a URL
- copy/paste this URL in your browser and use the VSC account authentication

Your SSH-connection will now be completed (This method also works from a Linux terminal)

Note that in case you are working with another type of UI that does an SSH-connection in the background, it is possible that you will first need to login with an ssh-client on your machine. WinSCP for example will also prompt you with the URL.

It is not possible to connect to NX when using a ED25519 keytype. The RSA4096 keytype does allow you to connect. You can login with your ssh key, but you will need to use :ref:`vsc firewall page<firewallpage>` or login through a terminal ssh before connecting to NX. The same goes for other applications (eg Filezilla) that will not prompt you the firewall URL when trying to ssh to the cluster through these applications. There are a couple of options here:

- keep an ssh session open to the cluster (Putty, MobaXterm...). You should now be able to connect without any problem.
- on Mac/Linux you can load your certificate in the ssh-agent
or use the vsc-agent, this will give a better user experience.

Authentication with an agent
----------------------------

In order to circumvent the annoyances of multiple MFA prompts, you can use an ssh-agent. The MFA prompt is bypassed if a previously injected certificate is used for authentication. A “previously injected certificate” means that a capable ssh-agent must be running on the user’s local computer, and that the user previously connected to the cluster by means of one of the previously mentioned nethods.

Authentication with an agent on Windows

**_NOTE:_** Download the :ref:`vscagent`.

For MS-Windows systems the :ref:`vscagent <vscagent>` is available to serve as ssh-agent, and also includes a “Renew VSC certificate” button that does exactly that to retrieve a certificate. Download it from the vsc-agent page. You can copy the vscagent.exe in your  C:\Workdir\myapps and run it from there if you have a KU Leuven central managed laptop. Once opened, follow these steps:

- Configuration:

  - go to the ‘Configuration’ tab
  - If you are a KU Leuven user, leave the 'Enable KU Leuven server certificates' box checked. Otherwise skip this step. Fill in these fields:

    - Principals: uXXXXXX  
    - Role: kuleuven
    - TTL : 16h
  - check ‘Enable HPC user certificates‘
  - check ‘tier2-leuven’
  - Username : vscXXXXX
  - Save configuration file

- SSH key(s)

  - Go to the ‘SSH Key Files’ tab
  - point to your private VSC-key

- Request a certificate

  - Go to the ‘SSH identities’ tab
  - renew certificate
  - Select ‘KU Leuven server certificate’ or ‘HPC Tier2 Leuven certificate’

You will need to do your second factor authentication to activate the certificate.

This agent also works for the NX-client. When you have your certificate, you will be able to connect to the cluster with your ssh-client, and using agent authentication. In a putty profile it is possible that you need to remove the path to your private key, if you have stored this in the profile.

Known issues: general
---------------------

#. It has happened that users cannot properly load the MFA URL. If that would happen to you, it is worth trying to paste the URL in a incognito browser window. This has only been verified to work in Chrome and does not seem to work in Firefox.
#. MobaXTerm: version 21.1 has known issues in combination with the vsc-agent. It does not always seem to find the certificate in your agent. Updating to the latest version should solve this.

.. _firewallpage: https://firewall.vscentrum.be
.. _vscagent: https://firewall.vscentrum.be/vscagent/latest/
