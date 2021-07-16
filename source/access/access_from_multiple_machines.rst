.. _access from multiple machines:

Access from multiple machines
=============================

There are two possibilities.

#. You can copy your private key from the machine where you generated
   the key to the other computers you want to use to access the VSC
   clusters. If you want to use both PuTTY on Windows and the
   traditional OpenSSH client on macOS or Linux (or Windows with MobaXterm)
   and chose for this scenario, you should generate the key using PuTTY
   and then export it in OpenSSH format as explained on :ref:`the PuTTY
   pages <generating keys putty>`.
#. Alternatively, you can generate another key pair for the second
   machine following the instructions for your respective client
   (:ref:`Windows <generating keys windows>`, :ref:`macOS/OS
   X <generating keys linux>`, :ref:`Linux <generating keys linux>`)
   and then upload the new public key to your account.

   #. Go to the `VSC account page`_.
   #. Choose "Edit account".
   #. And then add the public key via that page. It can take half an
      hour before you can use the key.

We prefer the second scenario, in particular if you want to access the
clusters from a laptop or tablet, as these are easily stolen. In this
way, all you need to do if your computer is stolen or your key may be
compromised in another way, is to delete that key on the `VSC account page`_
(via "Edit account"). You can continue to work on your other devices.

.. include:: links.rst
