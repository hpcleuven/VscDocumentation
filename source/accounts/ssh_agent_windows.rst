.. _ssh agent windows:

##############################
SSH Agent with Windows OpenSSH
##############################

Recent versions of Windows include a built-in `OpenSSH Authentication
Agent`_ service, commonly referred to as ``ssh-agent``. It holds your
private keys and SSH certificates in memory so that native Windows OpenSSH
commands (e.g. ``ssh``, ``scp`` and ``sftp``), and command line tools that
speak the standard OpenSSH agent protocol, such as ``step`` when obtaining
a :ref:`Smallstep certificate <smallstep-certificate>`, do not need your
passphrase or :ref:`Multi Factor Authentication <mfa_login>` on every
connection.

.. note::

   This is not the only SSH agent available on Windows, e.g. :ref:`Pageant`
   is another one. Separate agents do not share keys or certificates:
   loading one into this agent does not make it available in another.
   This agent should not be used for clients such as
   :ref:`PuTTY <terminal putty>`, :ref:`MobaXterm <terminal mobaxterm>` or
   :ref:`FileZilla <FileZilla>`; we recommend using another documented SSH
   agent for those instead.

Prerequisites
=============

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      To access KU Leuven clusters, only an approved
      :ref:`VSC account <access>` is needed as a prerequisite.

   .. tab-item:: UAntwerpen
      :sync: ua

      Before you start ``ssh-agent``, you need a private key in OpenSSH
      format. See :ref:`generating keys windows` to find out how to
      generate and use one.

   .. tab-item:: UGent
      :sync: ug

      Before you start ``ssh-agent``, you need a private key in OpenSSH
      format. See :ref:`generating keys windows` to find out how to
      generate and use one.

   .. tab-item:: VUB
      :sync: vub

      Before you start ``ssh-agent``, you need a private key in OpenSSH
      format, or a certificate obtained via
      :ref:`Multi Factor Authentication <mfa_login>`. See
      :ref:`generating keys windows` to find out how to generate a key.

Starting the agent
==================

The following commands will enable and automatically start the SSH Agent
service on your system. You only need to do this once, from an
**elevated** (Run as Administrator) PowerShell or Command Prompt:

.. code-block:: PowerShell

   # The ssh-agent service is disabled by default. Configure it to start
   # automatically, then start it.
   $ Set-Service -Name ssh-agent -StartupType Automatic
   $ Start-Service ssh-agent

   # The following command should return a status of Running
   $ Get-Service ssh-agent

Managing keys with SSH agent
============================

.. code-block:: PowerShell

   # Add your private key. Fill in the path to your private key correctly.
   $ ssh-add C:\Users\<user>\.ssh\id_rsa_vsc

You will then be asked to enter your passphrase.

To list the keys and certificates that the agent is managing:

.. code-block:: PowerShell

   $ ssh-add -l

You can now use native Windows OpenSSH commands (e.g. ``ssh``, ``scp`` and
``sftp``) without having to enter your passphrase again.

Besides keys, the agent can also hold SSH certificates. To obtain a VSC
certificate, see :ref:`Multi Factor Authentication <mfa_login>`; the
requesting tool loads it into the agent for you.

.. seealso::

   `Microsoft documentation on the OpenSSH Authentication Agent
   <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement>`__
