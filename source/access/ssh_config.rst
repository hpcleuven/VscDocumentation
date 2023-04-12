SSH config
==========

The SSH configuration file resides in the ``.ssh`` directory in your home
directory (at least when using Linux or macOS).  It is simply called
``config``.  It is not created by default, so you would have to create the
initial version.

.. warning::

   Make sure only the  owner has read and write permissions,
   neither group nor world should be able to read the file, i.e.,
   ::
   
      $ chmod 700 ~/.ssh/config


.. _linking key with vsc-id linux:

Linking your private key with your VSC-id
-----------------------------------------

To avoid having to specify your VSC private key every time you login, we highly
recommend linking your key to your VSC-id.

Assuming your private key is ``~/.ssh/id_rsa_vsc``, add the following
lines to your ``~/.ssh/config``:

::

   Match User vscXXXXX
       IdentityFile ~/.ssh/id_rsa_vsc

Replace vscXXXXX with your VSC-id.


Simple usage
------------

To simplify login in to a host, e.g., ``login.hpc.kuleuven.be`` as user
``vsc50005``, you can add the following:

::

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

::

   $ ssh hpc


How to link your key with a host?
---------------------------------

As alternative to linking your key with your VSC-id, you can also link your key
with a specific host.  Specifying identity files allows you to have distinct
keys for different hosts, e.g., you can use one key pair to connect to VSC
infrastructure, and a different one for your departmental server.

Assuming your private key is ``~/.ssh/id_rsa_vsc``, then you can
use it to connect by specifying the ``IdentityFile`` attribute, i.e.,

::

   Host hpc
       HostName login.hpc.kuleuven.be
       User vsc50005
       ForwardAgent yes
       ForwardX11 yes
       IdentityFile ~/.ssh/id_rsa_vsc


How to use a proxy host?
------------------------

To use a host as a proxy, but log in through it on another node, the
following entry can be added:

::

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


How to set up a tunnel?
-----------------------

If you require a tunnel to a remote host on a regular basis, you can
define a connection in the SSH configuration file, e.g.,

::

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

::

   $ ssh -N hpc_tunnel


How to create a modular configuration file?
-------------------------------------------

If you access many hosts, your ``.ssh/config`` file can grow very long.  In
that case, it might be convenient to group hosts into distinct files, and
include those into your main ``.ssh/config`` file, e.g.,

::

   Include ~/.ssh/config_vsc


Links
-----

-  `ssh_config manual page`_
-  `ssh manual page`_

