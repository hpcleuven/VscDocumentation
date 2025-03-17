As long as you use an :ref:`SSH agent <SSH agent>` to manage your SSH
keys, you stay connected via FileZilla and you do not require additional
configuration.

Alternatively, recent versions of FileZilla also can manage private keys
on their own. The path to the private key must be provided in the option:
*Edit Tab* -> *options* -> *connection* -> *SFTP*. After that you should
be able to connect after being asked for passphrase.

.. figure:: filezilla/prefs_private_key.jpg
   :alt: FileZilla site manager with settings
