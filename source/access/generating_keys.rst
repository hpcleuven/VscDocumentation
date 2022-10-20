#############
Security Keys
#############

Unlike your institute account, VSC accounts don't use regular fixed
passwords but a key pair consisting of a public an private key because
that is a more secure authentication technique.  To apply for a VSC
account, you need a public/private key pair.

.. _create key pair:

Create a public/private key pair
================================

A key pair consists of a private and a public key.

#. The private key is stored on the computer(s) you use to access the VSC
   infrastructure and always stays there.
#. The public key is stored on the  VSC systems you want to access, allowing
   to prove your identity through the corresponding private key.
  
.. warning::

   It is clear from the above that it is very important to protect your
   private key well. Therefore:
   
   - You should choose a strong passphrase to protect your private key.
   - You should not share your key pair with other users.
   - If you have accounts at multiple supercomputer centers (or on other
     systems that use SSH), you should seriously consider using a
     different key pair for each of those accounts. In that way, if a key
     would get compromised, the damage can be controlled.
   - For added security, you may also consider to use a different key pair
     for each computer you use to access your VSC account. If your
     computer is stolen, it is then easy to disable access from that
     computer while you can still access your VSC account from all your
     other computers. The procedure is explained on a separate web
     page ":ref:`access from multiple machines`".

How to generate such a key pair depends on your operating system. We
describe the generation of key pairs in the client sections below:

.. toctree::
   :maxdepth: 2

   generating_keys_on_windows
   generating_keys_on_linux
   generating_keys_on_os_x

