.. _ssh_config:

OpenSSH Configuration
=====================

The SSH configuration file is located in the ``.ssh`` folder in your home
directory (*e.g.* on Linux or macOS) and it is simply called ``config``.
This ``.ssh/config`` file is not created by default, so you will probably have
to create the initial version yourself.

.. warning::

   Make sure only the owner has read and write permissions, neither group nor
   others should be able to read this configuration file:

   .. code-block:: bash

      $ chmod 600 ~/.ssh/config

Basic configuration
-------------------

The main usage of the OpenSSH configuration is to automatically set options for
the ``ssh`` connections based on the hostname of the server. Avoiding having to
type the same options over and over again.

The following is an example that simplifies the connection to a KU Leuven
cluster to just a ``ssh hpc`` command. The full hostname of the login node and
the VSC ID of the user will be automatically filled in by OpenSSH.

.. code-block:: text

   Host *
       ServerAliveInterval 60

   Host hpc
       HostName login.hpc.kuleuven.be
       User vsc50005
       ForwardAgent yes
       ForwardX11 yes

Here, you should replace ``login.hpc.kuleuven.be`` by the hostname of the
remote host you want to login to, and ``vsc50005`` by your user name on that
system.  You can have as many host definitions as you want in the configuration
file.

The first entry, i.e., ``Host *`` ensures that for any host you connect to,
the server keep-alive interval is set to 60 seconds.

The second entry, i.e., ``Host hpc`` specifies that every SSH connection to
``login.hpc.kuleuven.be`` established using the ``hpc`` alias has agent
and X forwarding enabled, so you don't need to specify the ``-A`` and ``-X``
flags respectively.

Now you can simply log in to ``login.hpc.kuleuven.be`` using the ``hpc`` alias:

.. code-block:: bash

   $ ssh hpc


.. _ssh config link key vsc:

Link private key with VSC ID
----------------------------

You can avoid having to specify your VSC private key on your ``ssh`` command
every time with the option ``-i ~/.ssh/id_rsa_vsc`` by configuring OpenSSH to
automatically link link your private key to your VSC ID. Hence, whenever you
connect to any VSC cluster (or other server) with your VSC ID, the correct SSH
key will be used.

Assuming your private key is ``~/.ssh/id_rsa_vsc``, add the following
lines to the end of your ``~/.ssh/config``:

.. code-block:: text

   Match User vscXXXXX
       IdentityFile ~/.ssh/id_rsa_vsc

Replace ``vscXXXXX`` with your VSC ID.

Link key with a host
--------------------

As alternative to linking your key with your VSC ID, you can also link your key
with a specific host.  Specifying identity files allows you to have distinct
keys for different hosts, e.g., you can use one key pair to connect to VSC
infrastructure, and a different one for your departmental server.

Assuming your private key is ``~/.ssh/id_rsa_vsc``, then you can
use it to connect by specifying the ``IdentityFile`` attribute, i.e.,

.. code-block:: text

   Host hpc
       HostName login.hpc.kuleuven.be
       User vsc50005
       ForwardAgent yes
       ForwardX11 yes
       IdentityFile ~/.ssh/id_rsa_vsc


Using a proxy host
------------------

To use a host as a proxy, but log in through it on another node, the
following entry can be added:

.. code-block:: text

    Host leibniz
        Hostname login.leibniz.antwerpen.vsc
        User vsc50005
        ProxyJump hpc
        ForwardAgent yes
        ForwardX11 yes

In this example, ``login.leibniz.antwerpen.vsc`` is the host you actually
want to log in to, and ``login.hpc.kuleuven.be`` is the host you are using
as a proxy jump host, i.e., you will log in to that one, but it will log
you through to the leibniz login node.

.. note::

   The alias ``hpc`` previously defined for ``login.hpc.kuleuven.be`` can
   be used to specify the proxy jump host.


Setting up a tunnel
-------------------

If you require a tunnel to a remote host on a regular basis, you can
define a connection in the SSH configuration file, e.g.,

.. code-block:: text

   Host hpc_tunnel
       HostName login.hpc.kuleuven.be
       User vsc50005
       ForwardAgent yes
       ForwardX11 yes
       LocalForward 50005 login.hpc.kuleuven.be:50005

This ensures that a process on the login node that uses port 50005 can be
accessed from your computer on that same port number.

.. note::

   When choosing a port on a remote VSC system, it is good practice to
   use your VSC-number, since that would be unique.  In the example above,
   the port number would be 50005 for VSC user ``vsc50005``.

The tunnel can now be established as follows:

.. code-block:: bash

   $ ssh -N hpc_tunnel


Modular configuration file
--------------------------

If you access many hosts, your ``.ssh/config`` file can grow very long.  In
that case, it might be convenient to group hosts into distinct files, and
include those into your main ``.ssh/config`` file, e.g.,

.. code-block:: text

   Include ~/.ssh/config_vsc


Links
-----

* `ssh_config manual page`_
* `ssh manual page`_

