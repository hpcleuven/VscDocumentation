.. _generating keys putty:

##########################
Generating keys with PuTTY
##########################

By default, there is no SSH client software available on Windows, so you
will typically have to install one yourself. We recommend to use `PuTTY`_,
which is freely available. Follow the instructions on :ref:`terminal putty` to
install it on your computer.

Requirements
------------

* Windows operating system
* :ref:`PuTTY<terminal putty>`

Create a public/private key pair
--------------------------------

To generate a public/private key pair, you can use the *PuTTYgen* key
generator. This will already be available if you
:ref:`installed PuTTY as described in our documentation<terminal putty>`.
If it is not the case, you can download it from the `PuTTY download site`_.

Start *PuTTYgen* on your computer and follow the following steps:

#. In 'Parameters' (at the bottom of the window), choose 'RSA' and
   set the number of bits in the key to 4096:

   .. figure:: generating_keys_putty/puttygen_initial.png
      :alt: Initial PuTTYgen screen

#. Click on 'Generate'. To generate the key, you must move the mouse
   cursor over the PuTTYgen window (this generates some random data that
   PuTTYgen uses to generate the key pair). Once the key pair is
   generated, your public key is shown in the field 'Public key for
   pasting into OpenSSH authorized_keys file'.

#. Next, you should specify a passphrase in the 'Key passphrase' field
   and retype it in the 'Confirm passphrase' field. Remember, the
   passphrase protects the private key against unauthorized use, so it
   is best to choose one that is not too easy to guess. Additionally, it
   is adviced to fill in the 'Key comment' field to make it easier
   identifiable afterwards.
   
   .. figure:: generating_keys_putty/puttygen_filled_out.png
      :alt: Filled PuTTYgen screen

#. Finally, save both the public and private keys in a secure place
   (i.e., a folder on your personal computer, or on your personal USB
   stick, ...) with the buttons 'Save public key' and 'Save private
   key'. We recommend to use the name ``id_rsa_vsc.pub`` for the public
   key, and ``id_rsa_vsc.ppk`` for the private key.

If you use another program to generate a key pair, please remember that
they need to be in the OpenSSH format to access the VSC clusters.

.. _converting PuTTY keys:

Converting PuTTY keys to OpenSSH format
---------------------------------------

OpenSSH is a very popular command-line SSH client originating from the
Linux world but now available on many operating systems. Therefore its
file format is a very popular one. Some applications, such as Eclipse's
SSH components, can not handle private keys generated with PuTTY, only
OpenSSH compliant private keys. However, PuTTY's key generator
'PuTTYgen' (that was used to generate the public/private key pair in the
first place) can be used to convert the PuTTY private key to one that
can be used by Eclipse.

#. Start PuTTYgen.

#. From the 'Conversions' menu, select 'Import key' and choose the file
   containing your PuTTY private key that is used to authenticate on the
   VSC cluster.

#. When prompted, enter the appropriate passphrase.

#. From the 'Conversions' menu, select 'Export OpenSSH key' and save it
   as ``id_rsa_vsc``.
   Remember the file name and its location, it will have to be specified
   in the configuration process of, e.g., Eclipse.

#. Exit PuTTYgen.

