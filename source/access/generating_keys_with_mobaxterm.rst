.. _generating keys mobaxterm:

##############################
Generating keys with MobaXterm
##############################

The following steps explain how to generate an SSH key pair in ``OpenSSH`` format
using the MobaXterm application.

#. Go to the `MobaXterm`_ website and download the free version. Make sure to
   select the **Portable edition** from the download page. Create a folder
   called ``MobaXterm`` in a known location in your computer and decompress the
   contents of the downloaded zip file inside it.

#. Double click the ``MobaXterm_Personal`` executable file inside the
   ``MobaXterm`` folder.
   The MobaXterm main window will appear on your screen. It should be similar to this one:

   .. _mobaxterm-main-window-sshkey:
   .. figure:: access_using_mobaxterm/mobaxterm_main_window.png
      :align: center
      :alt: mobaxterm main

#. In the **Tools** menu choose the **MobaKeyGen (SSH key generator)** option,
   a panel like this one will appear:

   .. _mobaxterm-sshkey-generator:
   .. figure:: generating_keys_with_mobaxterm/mobaxterm_sshkey_generator.png
      :align: center
      :alt: mobaxterm main


#. Make sure the option **RSA** is chosen and **Number of bits in a generated
   key** is set to **4096**. Press the button **Generate**. As shown below,
   you will be requested to move the mouse in the **Key** area to generate some
   entropy; do so until the green bar is completely filled.

   .. _mobaxterm-sshkey-entropy:
   .. figure:: generating_keys_with_mobaxterm/mobaxterm_sshkey_entropy.png
      :align: center
      :alt: mobaxterm main

#. When the process is over you will see its result as shown below. Enter a
   comment in the **Key comment** field and a strong passphrase.

   .. _mobaxterm-sshkey-passphrase:
   .. figure:: generating_keys_with_mobaxterm/mobaxterm_sshkey_passphrase.png
      :align: center
      :alt: mobaxterm main

#. Click on the **Save public key** button and save it to some desired
   location; we recommend to name it ``id_rsa_vsc.pub``. You must upload this public key to your
   your `VSC accountpage <https://account.vscentrum.be>`__ before you can login to a VSC cluster.

#. Finally click on the **Save private key** button and save that file also;
   we recommend to name this file ``id_rsa_vsc.ppk``. As the *private* part of
   the name suggests, this file should not be shared, you must keep it in a safe
   location in your computer.
   You will have to remember where you saved it, as you will need it to
   connect to the cluster after you receive the confirmation that your account
   is active.

