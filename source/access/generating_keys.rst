########################
:fas:`key` Security Keys
########################

Connections to VSC clusters are always encrypted to secure your data. Hence,
you will need a cryptographic key pair, so-called SSH key, to log in to the VSC
clusters via the terminal interface.

.. _create key pair:

Create a public/private key pair
================================

A key pair consists of a private and a public key.

#. The private key is stored on the computer(s) you use to access the VSC
   infrastructure and always stays there.
#. The public key is stored on the VSC systems you want to access, allowing
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
     page ":ref:`access_multiple_computers`".

How to generate such a key pair depends on your operating system. We
describe the generation of key pairs in the client sections below:

.. toctree::
   :hidden:

   generating_keys_on_windows
   generating_keys_with_openssh_on_os_x
   generating_keys_with_openssh

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: :fab:`windows` Windows
       :columns: 12 4 4 4
       :link: generating_keys_on_windows
       :link-type: doc

       Generating keys

    .. grid-item-card:: :fab:`apple` macOS
       :columns: 12 4 4 4
       :link: generating_keys_with_openssh_on_os_x
       :link-type: doc

       Generating keys

    .. grid-item-card:: :fab:`linux` Linux
       :columns: 12 4 4 4
       :link: generating_keys_with_openssh
       :link-type: doc

       Generating keys

.. _upload public key:
   
Upload public key to VSC account page
=====================================

Every time that you make a new SSH key pair for your VSC account, you have to
upload the public part of the key to your `VSC account page`_. Once uploaded it
will be distributed across the VSC clusters.

.. warning::

   Allow for at least half an hour for any change to your public keys to
   propagate through the VSC systems and be able to log in with them.

The upload procedure is slightly different depending on the motivation for the
new SSH key.

First key of your account
-------------------------

You already have an active VSC account and this is the first public key you
will add to it:

#. Go to the `Edit VO <https://account.vscentrum.be/django/account/edit>`_ tab
   of your `VSC account page`_
#. Scroll down to the section *Add public key*
#. Click *Browse* to select the file of your public key
#. Click *Upload extra public key* and wait for the upload to complete
#. Click *Update*
#. Verify that the new public key is listed under *Manage public keys*

Additional key for your account
-------------------------------

You already have an active VSC account with a public key and want to add an
additional key to be able to connect to the VSC clusters from a different
computer:

#. Go to the `Edit VO <https://account.vscentrum.be/django/account/edit>`_ tab
   of your `VSC account page`_
#. Scroll down to the section *Add public key*
#. Click *Browse* to select the file of your public key
#. Click *Upload extra public key* and wait for the upload to complete
#. Click *Update*
#. Verify that both the old and new public key is listed under *Manage public
   keys*

.. _replace compromised key:

Replace compromised key
-----------------------

You already have an active VSC account with a public key, but it got
compromised and must be replaced with a new one:

#. Go to the `Edit VO <https://account.vscentrum.be/django/account/edit>`_ tab
   of your `VSC account page`_
#. Scroll down to *Manage public keys*
#. Select the *Delete this key* checkbox of the compromised key
#. Scroll down to the section *Add public key*
#. Click *Browse* to select the file of your new public key
#. Click *Upload extra public key* and wait for the upload to complete
#. Click *Update*
#. Verify that the new public key is listed under *Manage public keys*

