.. _generating keys mobaxterm:

##############################
Generating keys with MobaXterm
##############################

By default, there is no SSH client software available on Windows, so you
will typically have to install one yourself. A popular option is
:ref:`MobaXterm <terminal mobaxterm>`, which is a freely terminal client that
can also  generate your keys on Windows.

Requirements
------------

* Windows operating system
* :ref:`MobaXterm <terminal mobaxterm>`

Create a public/private key pair
--------------------------------

The following steps explain how to generate an SSH key pair in ``OpenSSH`` format
using the MobaXterm application. You can install MobaXterm on your computer
following :ref:`our installation instructions <mobaxterm install>`.

#. Launch the ``MobaXterm_Personal`` executable file inside the
   ``MobaXterm`` folder.

#. In the **Tools** menu choose the **MobaKeyGen (SSH key generator)** option,
   a panel like this one will appear:

   .. _mobaxterm-sshkey-generator:
   .. figure:: generating_keys_mobaxterm/mobaxterm_sshkey_generator.png
      :alt: mobaxterm ssh key generator


#. Make sure the option **RSA** is chosen and **Number of bits in a generated
   key** is set to **4096**. Press the button **Generate**. As shown below,
   you will be requested to move the mouse in the **Key** area to generate some
   entropy; do so until the green bar is completely filled.

   .. _mobaxterm-sshkey-entropy:
   .. figure:: generating_keys_mobaxterm/mobaxterm_sshkey_entropy.png
      :alt: mobaxterm ssh key entropy

#. When the process is over you will see its result as shown below. Enter a
   comment in the **Key comment** field and a strong passphrase.

   .. _mobaxterm-sshkey-passphrase:
   .. figure:: generating_keys_mobaxterm/mobaxterm_sshkey_passphrase.png
      :alt: mobaxterm ssh key passphrase

#. Click on the **Save public key** button and save it to some desired
   location; we recommend to name it ``id_rsa_vsc.pub``. You must upload this
   public key to your `VSC account page`_ before you can login to a VSC cluster.

#. Finally click on the **Save private key** button and save that file also;
   we recommend to name this file ``id_rsa_vsc.ppk``. As the *private* part of
   the name suggests, this file should not be shared, you must keep it in a safe
   location in your computer.
   You will have to remember where you saved it, as you will need it to
   connect to the cluster after you receive the confirmation that your account
   is active.

