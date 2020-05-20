Security measures 20 May 2020
=============================

In response to reports of security incidents in several high-profile HPC centers
throughout Europe
(https://csirt.egi.eu/academic-data-centers-abused-for-crypto-currency-mining/), all
VSC sites are taking a number of concerted pre-emptive security actions. These actions
will affect you, although we are trying to minimize the impact as much as possible. 

Recurring examinations on the VSC clusters have so far indicated no abnormalities, but
we remain vigilant and have enhanced monitoring of our systems. However, we will take
a number of actions to further ensure the integrity and security of all VSC systems: 

Your current SSH keys will be revoked on May 27, 2020
-----------------------------------------------------

**We will effectively revoke all SSH public keys uploaded before 20 May 2020.** You
should generate a new SSH key pair and upload the new public key in the
`VSC account page <https://account.vscentrum.be>`_ (via ``Edit account`` tab). Instructions on how to create a
key pair and upload the public key :ref:`can be found here <upload_new_ssh_key>`.
 
.. note::

   For security reasons, please: 

   * use a *strong passphrase* to protect your private key,  

   * use *different* keys to access *different* machines,  

   * *never* share your SSH private key with another person. 


**On Wednesday 27 May 2020, we will revoke all the SSH-keys that were uploaded before 20
May 2020.** This operation will have no impact on your running jobs, but you will only be
able to access the VSC systems if you have uploaded a new key pair. 

.. warning::

   Upload a new SSH public key before 27 May 2020 to ensure you will still be able to connect to the VSC clusters with your VSC account!

If needed, you can still restore access to your VSC account on or after 27 May 2020 by uploading a new SSH public key.

.. note::

  Take into account that it takes a while before a new SSH public key becomes active on the system
  (it should not take longer than 1 hour after uploading the public key to the VSC account page).

Additional Firewall layer 
-------------------------

We will tighten access control to VSC systems, based on the IP address with which you
are connecting. From within university networks and most Belgian commercial internet
providers, VSC login nodes will remain accessible as they were before, requiring no
additional action from your part. All other IP domains will be blocked by default. If
you are connecting from one of those IP addresses, you have one of the following
options to get access to VSC login nodes: 

* use an VPN connection to your university network;  

* register your IP address by accessing (https://firewall.hpc.kuleuven.be/) and logging
  in with your institutional account. While this web connection is active a new
  SSH-session can be started.
  Active SSH sessions will remain active even when this web page is closed.

* contact your HPC support team and ask them to whitelist your IP-range (e.g., for
  industry access, automated processes). 

These IP filtering rules will go into effect starting 20 May 2020, 14h00 (CEST).

We understand that these actions require some effort from your side, but we hope you
can understand the necessity of these actions. We will keep on investigating to offer
you safe and user friendly ways to get access to the VSC clusters and keep you
informed about future developments. **If you have any questions, please contact us.**

.. include:: user_support_addresses.rst
