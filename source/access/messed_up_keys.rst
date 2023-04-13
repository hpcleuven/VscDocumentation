.. _messed up keys:

Messed up keys
==============

There are two cases in which your keys may have been messed up and cannot be
used any more. In both cases you can fix this situation yourself in a few easy
steps via the `VSC account page`_.

Update missing keys in the cluster
----------------------------------

The keys that were stored in the ``.ssh`` subdirectory of your home directory
on the cluster were accidentally deleted, or the ``authorized_keys`` file was
accidentally deleted.

#. Go to the `VSC account page`_.
#. Choose your institute and log in.
#. At the top of the page, click 'Edit Account'.
#. Press the 'Update' button on that web page.
#. Exercise some patience, within 30 minutes, your account should be
   accessible again.

.. _upload_new_ssh_key:

Upload a new SSH key to your VSC account
----------------------------------------

You deleted your (private) keys on your own computer, or don't remember the
passphrase. In such a case, the only solution is to re-generate a new pair of
keys and upload it to your VSC account.

#. Generate a new public/private key pair. Follow the procedure
   outlined in the client sections for
   :ref:`Linux <generating keys linux>`,
   :ref:`Windows <generating keys windows>` and :ref:`macOS
   <generating keys macos>` (formerly OS X).
#. Go to the `VSC account page`_.
#. Choose your institute and log in.
#. At the top of the page, click 'Edit Account'.
#. Upload your new public key adding it in the 'Add Public Key'
   section of the page. Use 'Browse...' to find your public key,
   press 'Add' to upload it.
#. You may now delete the entry for the "lost" key if you know
   which one that is, but this is not crucial.
#. Exercise some patience, within 30 minutes, your account should be
   accessible again.

