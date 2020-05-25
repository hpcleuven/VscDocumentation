.. _messed up keys:

Messed up keys
==============

You can fix this yourself in a few easy steps via the `VSC account page`_.

There are two ways in which you may have messed up your keys:

#. The keys that were stored in the ``.ssh`` subdirectory of your home
   directory on the cluster were accidentally deleted, or the
   ``authorized_keys`` file was accidentally deleted:

   #. Go to the `VSC account page`_.
   #. Choose your institute and log in.
   #. At the top of the page, click 'Edit Account'.
   #. Press the 'Update' button on that web page.
   #. Exercise some patience, within 30 minutes, your account should be
      accessible again.

#. You deleted your (private) keys on your own computer, or don't know
   the passphrase anymore

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
   #. You may now delete the entry for the \\"lost\" key if you know
      which one that is, but this is not crucial.
   #. Exercise some patience, within 30 minutes, your account should be
      accessible again.

.. include:: links.rst
