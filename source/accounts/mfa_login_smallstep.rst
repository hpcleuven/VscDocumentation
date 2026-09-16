.. _smallstep-certificate:

#####################
Smallstep certificate
#####################

This is one of the two ways to obtain an SSH certificate described in
:ref:`Connecting with an SSH agent <mfa-with-ssh-agent>`.

.. note::

   On Windows, this method only works when connecting to the cluster from
   Windows PowerShell or the Command Prompt. PuTTy or MobaXterm users need
   to obtain a :ref:`Firewall-based certificate <firewall-based-certificate>`
   using Pageant instead.

* Install the ``step`` CLI. See the `Smallstep installation`_ documentation
  for more information.

.. tab-set::
   :sync-group: operating-system

   .. tab-item:: Windows
      :sync: win

      Install ``step-ca.exe`` and ``step.exe`` using Winget.
      Using Windows PowerShell or Command Prompt:

      .. code-block:: PowerShell

         winget install Smallstep.step-ca

   .. tab-item:: macOS
      :sync: mac

      Install ``step-ca`` and ``step`` using homebrew.
      In the terminal:

      .. code-block:: bash

         brew install step

   .. tab-item:: Linux
      :sync: lin

      Install the ``step-cli`` and ``step-ca`` packages. Instructions for
      specific Linux distributions can be found on the `Smallstep
      installation`_ documentation page.

* Set up (bootstrap) the environment. This creates the ``~/.step`` directory
  and only needs to happen the first time.

  .. code-block:: bash

     step ca bootstrap --context VSC --team VSC --team-url=https://hpc.vub.be/_static/VSC-CA.json

* Start up your SSH agent

.. tab-set::
   :sync-group: operating-system

   .. tab-item:: Windows
      :sync: win

      Use the built-in :ref:`Windows OpenSSH agent <ssh agent windows>`.

   .. tab-item:: macOS
      :sync: mac

      Use the default :ref:`OpenSSH agent`.

   .. tab-item:: Linux
      :sync: lin

      Use the default :ref:`OpenSSH agent`.

* Obtain a certificate. It has a lifetime of 16 hours.

  .. code-block:: bash

     step ssh login --context VSC

.. note::

   You can automatically obtain a certificate when connecting with SSH as a
   specific user ``vsc98765`` by adding the following to your
   :ref:`SSH config file <ssh_config>`:

   .. code-block:: text

      # Use Smallstep to handle the SSH connection and automatically renew/login when the certificate expires
      Match User vsc98765
          ProxyCommand step ssh proxycommand %r %h %p --context VSC

.. note::

   Smallstep can also issue a certificate without using an agent:

   .. code-block:: bash

      step ssh certificate <email> ~/.ssh/smallstep --context VSC --no-agent

   This creates a private key and certificate in your ``~/.ssh`` folder.
   You will need to pass ``-i ~/.ssh/smallstep`` to ``ssh``, or configure it
   in your :ref:`SSH config file <ssh_config>`, to use it.
