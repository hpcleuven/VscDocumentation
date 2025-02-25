.. _messed up keys:

Messed up keys
==============

There are two cases in which your keys may have been messed up and cannot be
used any more. In both cases you can fix this situation on your own in a few
easy steps via the `VSC account page`_.

.. warning::

   Allow for at least half an hour for any change to your public keys to
   propagate through the VSC systems and be able to log in with them.

Update missing keys in the cluster
----------------------------------

The keys that were stored in the ``.ssh`` subdirectory of your home directory
on the cluster were accidentally deleted, or the ``authorized_keys`` file was
accidentally deleted.

#. Go to the `VSC account page`_
#. Choose your institute and log in
#. At the top of the page, click 'Edit Account'
#. Press the 'Update' button on that web page

.. _upload_new_ssh_key:

Upload a new SSH key to your VSC account
----------------------------------------

Keys that are lost (*i.e.* stolen or deleted file of the private key) or locked
(*i.e.* a lost passphrase of the key) must be replaced with new ones:

#. :ref:`Generate a new public/private key pair <create key pair>`
#. :ref:`Replace old public key with new one in your VSC account page <replace
   compromised key>`

