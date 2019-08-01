SSH config
==========

The SSH configuration file resides in the ``.ssh`` directory in your home
directory (at least when using Linux or MacOS X).  It is simply called
``config``.  It is not created by default, so you would have to create the
initial version.

.. warning::

   Make sure only the  owner has read and write permissions,
   neither group nor world should be able to read the file, i.e.,
   ::
   
      $ chmod 700 .ssh/config


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
system.  You can have as many host defintions as you want in the configuration
file.

.. note::

   Due to this configuration, every SSH connection to ``login.hpc.kuleuven.be``
   established using the ``hpc`` alias has agent forwarding and X forwarding
   enabled, so you don't need to specify the ``-A`` and ``-X`` flags
   respectively.

   For any host you connect to, the server keep-alive interval is set to
   60 seconds.

Now you can simply log in to ``login.hpc.kuleuven.be`` using the ``hpc`` alias:

::

   $ ssh hpc


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


How to create a modular configuration file?
-------------------------------------------

If you access many hosts, your ``.ssh/config`` file can grow very long.  In
that case, it might be convenient to group hosts into distinct files, and
include those into your main ``.ssh/config`` file, e.g.,

::

   Include ~/.ssh/config_vsc
