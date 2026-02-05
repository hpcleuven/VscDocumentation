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

Basic configuration for VSC
---------------------------

The main usage of the OpenSSH configuration is to automatically set options for
the ``ssh`` connections based on the hostname of the server. Avoiding having to
type the same options over and over again.

The following file is an example configuration for SSH that simplifies the
connection to all VSC clusters. Once added to your ``~/.ssh/config``, you will
be able to login to any VSC cluster with a simple command of the form ``ssh
<name_of_cluster>`` without having to specify your VSC ID or path the key
file.

.. code-block:: text
   :caption: Example SSH config file for VSC clusters

   ServerAliveInterval 60

   Host vsc.vub
       HostName login.hpc.vub.be
       User vsc00000
   Host vsc.ugent
       HostName login.hpc.ugent.be
       User vsc00000
   Host vsc.kuleuven
       HostName login.hpc.kuleuven.be
       User vsc00000
   Host vsc.uantwerpen
       HostName login.hpc.uantwerpen.be
       User vsc00000
   Host vsc.hortense
       HostName tier1.hpc.ugent.be
       User vsc00000

   Match User vsc00000
       IdentityFile ~/.ssh/id_rsa_vsc
       ForwardAgent yes
       ForwardX11 yes


Here, you should replace ``vsc00000`` with your VSC ID and ``~/.ssh/id_rsa_vsc``
with the actual path to your SSH private key.

This ``.ssh/config`` file is composed with the following entries:

ServerAliveInterval
    Global parameter that makes your SSH client to send a keep-alive message in
    all established connections every 60 seconds to prevent the connection from
    timing out.

Host
    Define connection settings based on the name of the target host (i.e. VSC
    cluster). For instance, we use this entry to define the real public
    hostname of the cluster and our username for that connection.

Match User
    Define connection settings based on the name of the user set in the
    connection. For instance, we use this entry to define that all connections
    using our VSC ID should also enable the SSH Agent forwarding and X
    forwarding, so you don't need to manually specify the ``-A`` and ``-X``
    flags respectively.

.. code-block:: bash
   :caption: Command to connect to Tier-2 cluster in KU Leuven

   $ ssh vsc.kuleuven


.. _ssh config link key vsc:

Link private key with VSC ID
----------------------------

You can configure OpenSSH to automatically link your private key whenever you
connect with your VSC ID. This avoids having to manually specify the path to
your VSC private key with the option ``-i ~/.ssh/id_rsa_vsc`` on your ``ssh``
command.

This can be achieved with the ``IdentityFile`` option under a ``Match User``
condition defined for your VSC ID. Assuming your private key is
``~/.ssh/id_rsa_vsc``, add the following lines to the end of your
``~/.ssh/config``:

.. code-block:: text

   Match User vsc00000
       IdentityFile ~/.ssh/id_rsa_vsc

Replace ``vsc00000`` with your VSC ID.

Link key with a host
--------------------

As alternative to linking your key with your VSC ID, you can also link your key
with a specific host. Specifying identity files allows you to have distinct
keys for different hosts, *e.g.* you can use one key pair to connect to VSC
infrastructure, and a different one for your departmental server.

This can be achieved with the ``IdentityFile`` option under a ``Host``
entry defined for target cluster/server. Assuming your private key is
``~/.ssh/id_rsa_another``, then you can write the ``Host`` entry as:

.. code-block:: text

   Host vsc.kuleuven
       HostName login.hpc.kuleuven.be
       User vsc00000
       IdentityFile ~/.ssh/id_rsa_another


Using a proxy host
------------------

You can configure SSH to connect to a host through some intermediate proxy
server. For instance, this can be useful to connect to a compute node through
the login nodes of your VSC cluster.

.. code-block:: text

    Host leibniz-via-kuleuven
        Hostname login.leibniz.antwerpen.vsc
        User vsc00000
        ProxyJump vsc.kuleuven

In this example, ``login.leibniz.antwerpen.vsc`` is the host you actually
want to log in to, and ``vsc.kuleuven`` is the host you are using as a proxy
jump host, i.e. you will log in to that one, but it will log
you through to the leibniz login node.

Setting up a tunnel
-------------------

If you require a tunnel to a remote host on a regular basis, you can
define such a connection in the SSH configuration file. For instance, to
forward the port 50005 on the target VSC cluster to port 50005 in your local
computer, you can do:

.. code-block:: text

   Host vsc.kuleuven.tunnel
       HostName login.hpc.kuleuven.be
       User vsc00000
       LocalForward 50005 login.hpc.kuleuven.be:50005

This ensures that a process on the login node that uses port 50005 can be
accessed from your computer on that same port number.

.. note::

   When choosing a port on a remote VSC system, it is good practice to
   use your VSC-number, since that would be unique.

The tunnel can now be established as follows:

.. code-block:: bash

   $ ssh -N vsc.kuleuven.tunnel


Modular configuration file
--------------------------

If you access many hosts, your ``.ssh/config`` file can grow very long.  In
that case, it might be convenient to group hosts into distinct files, and
include those into your main ``.ssh/config`` file.

.. code-block:: text
   :caption: Example *Include* entry in SSH configuration

   Include ~/.ssh/config_vsc


Links
-----

* `ssh_config manual page`_
* `ssh manual page`_

