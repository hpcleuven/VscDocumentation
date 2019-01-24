.. _SSH agent:

Using ssh-agent
===============

The OpenSSH program ssh-agent is a program to hold private keys used for
public key authentication (RSA, DSA). The idea is that you store your
private key in the ssh authentication agent and can then log in or use
sftp as often as you need without having to enter your passphrase again.
This is particularly useful when setting up a ssh proxy connection
(e.g., for the tier-1 system muk) as these connections are more
difficult to set up when your key is not loaded into an ssh-agent.

This all sounds very easy. The reality is more difficult though. The
problem is that subsequent commands, e.g., the command to add a key to
the agent or the ssh or sftp commands, must be able to find the ssh
authentication agent. Therefore some information needs to be passed from
ssh-agent to subsequent commands, and this is done through two
*environment variables*: ``SSH_AUTH_SOCK`` and ``SSH_AGENT_PID``. The
problem is to make sure that these variables are defined with the
correct values in the shell where you start the other ssh commands.

.. _start SSH agent:

Starting ssh-agent: Basic scenarios
-----------------------------------

There are a number of basic scenarios

#. You're lucky and your system manager has set up everything so that
   ssh-agent is started automatically when the GUI starts after logging
   in and the environment variables are hence correctly defined in all
   subsequent shells. You can check for that easily: type

   ::

      $ ssh-add -l

   If the command returns with the message

   ::

      Could not open a connection to your authentication agent.

   then ssh-agent is not running or not configured properly, and you'll
   need to follow one of the following scenarios.

#. Start an xterm (or whatever your favourite terminal client is) and
   continue to work in that xterm window or other terminal windows
   started from that one:

   ::

      $ ssh-agent xterm &
          

   The shell in that xterm is then configured correctly, and when that
   xterm is killed, the ssh-agent will also be killed.

#. ssh-agent can also output the commands that are needed to configure
   the shell. These can then be used to configure the current shell or
   any further shell, e.g., if you're a bash user, an easy way to start
   a ssh-agent and configure it in the current shell, is to type

   ::

      $ eval `ssh-agent -s`
          

   at the command prompt. If you start a new shell (e.g., by starting an
   xterm) from that shell, it should also be correctly configured to
   contact the ssh authentication agent. A better idea though is to
   store the commands in a file and excute them in any shell where you
   need access to the authentication agent, e.g., for bash users:

   ::

      $ ssh-agent -s >~/.ssh-agent-environment
      . ~/.ssh-agent-environment
          

   and you can then configure any shell that needs access to the
   authentication agent by executing

   ::

      $ . ~/.ssh-agent-environment

          

   Note that this will not necessarily shut down the ssh-agent when you
   log out of the system. It is not a bad idea to explicitly kill the
   ssh-agent before you log out:

   ::

      $ ssh-agent -k
          

Managing keys
-------------

Once you have an ssh-agent up and running, it is very easy to add your
key to it. If your key has the default name(id_rsa), all you need to do
is to type

::

   $ ssh-add

at the command prompt. You will then be asked to enter your passphrase.
If your key has a different name, e.g., id_rsa_cluster, you can specify
that name as an additional argument to ssh-add:

::

   $ ssh-add ~/.ssh/id_rsa_cluster

To list the keys that ssh-agent is managing, type

::

   $ ssh-add -l

You can now use the OpenSSH commands :ref:`ssh <OpenSSH access>`,
:ref:`sftp and scp <scp and sftp>` without having to enter your passphrase
again.

Starting ssh-agent: Advanced options
------------------------------------

In case ssh-agent is not started by default when you log in to your
computer, there's a number of things you can do to automate the startup
of ssh-agent and to configure subsequent shells.

Ask your local system administrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're not managing your system yourself, you can always ask your
system manager if he can make sure that ssh-agent is started when you
log on and in such a way that subsequent shells opened from the desktop
have the environmental variables ``SSH_AUTH_SOCK`` and ``SSH_AGENT_PID`` set
(with the first one being the most important one).

And if you're managing your own system, you can dig into the manuals to
figure out if there is a way to do so. Since there are so many desktop
systems avaiable for Linux systems (gnome, KDE, Ubuntu unity, ...) we
cannot offer help here.

A semi-automatic solution in bash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This solution requires some modifications to .bash_profile and .bashrc.
Be careful when making these modifications as errors may lead to trouble
to log on to your machine. So test by executing these files with
``source ~/.bash_profile`` and ``source ~/.bashrc``.

This simple solution is based on option 3 given above to start
ssh-agent.

#. You can define a new shell command by using the `bash alias
   mechanism <https://www.gnu.org/software/bash/manual/bash.html#Aliases>`_.
   Add the following line to the file .bashrc in your home directory:

   ::

      alias start-ssh-agent='/usr/bin/ssh-agent -s >~/.ssh-agent-environment; . ~/.ssh-agent-environment'
          

   The new command start-ssh-agent will now start a new ssh-agent, store
   the commands to set the environment variables in the file
   .ssh-agent-environment in your home directory and then "source"
   that file to execute the commands in the current shell (which then
   sets ``SSH_AUTH_SOCK`` and ``SSH_AGENT_PID`` to appropriate values).

#. Also put the line

   ::

      [[ -s ~/.ssh-agent-environment ]] && . ~/.ssh-agent-environment &>/dev/null
          

   in your .bashrc file. This line will check if the file
   ssh-agent-environment exists in your home directory and "source"
   it to set the appropriate environment variables.

#. As explained in the `GNU bash manual <https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files>`_,
   ``.bashrc`` is only read when starting so-called interactive non-login
   shells. Interactive login shells will not read this file by default.
   Therefore it is `advised in the GNU bash manual
   <https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files>`_
   to add the line

   ::

      [[ -s ~/.bashrc ]] && . ~/.bashrc
          

   to your ``.bash_profile``. This will execute ``.bashrc`` if it exists
   whenever ``.bash_profile`` is called.

You can now start a SSH authentication agent by issuing the command
``start-ssh-agent`` and add your key :ref:`as indicated
above <start SSH agent>` with ``ssh-add``.

An automatic and safer solution in bash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One disadvantage of the previous solution is that a new ssh-agent will
be started every time you execute the command start-ssh-agent, and all
subsequent shells will then connect to that one.

The following solution is much more complex, but a lot safer as it will
first do an effort to see if there is already a ssh-agent running that
can be contacted:

#. It will first check if the environment variable ``SSH_AUTH_SOCK`` is
   defined, and try to contact that agent. This makes sure that no new
   agent will be started if you log on onto a system that automatically
   starts an ssh-agent.
#. Then it will check for a file .ssh-agent-environment, source that
   file and try to connect to the ssh-agent. This will make sure that no
   new agent is started if another agent can be found through that file.
#. And only if those two tests fail will a new ssh-agent be started.

This solution uses a Bash function.

#. Add the following block of text to your ``.bashrc`` file:

   ::

      start-ssh-agent() {
      #
      # Start an ssh agent if none is running already.
      # * First we try to connect to one via SSH_AUTH_SOCK
      # * If that doesn't work out, we try via the file ssh-agent-environment
      # * And if that doesn't work out either, we just start a fresh one and write
      #   the information about it to ssh-agent-environment for future use.
      #
      # We don't really test for a correct value of SSH_AGENT_PID as the only 
      # consequence of not having it set seems to be that one cannot kill
      # the ssh-agent with ssh-agent -k. But starting another one wouldn't 
      # help to clean up the old one anyway.
      #
      # Note: ssh-add return codes: 
      #   0 = success,
      #   1 = specified command fails (e.g., no keys with ssh-add -l)
      #   2 = unable to contact the authentication agent
      #
      sshfile=~/.ssh-agent-environment
      #
      # First effort: Via SSH_AUTH_SOCK/SSH_AGENT_PID
      #
      if [ -n \"$SSH_AUTH_SOCK\" ]; then
        # SSH_AUTH_SOCK is defined, so try to connect to the authentication agent
        # it should point to. If it succeeds, reset newsshagent.
        ssh-add -l &>/dev/null 
        if [[ $? != 2 ]]; then 
          echo \"SSH agent already running.\"
          unset sshfile
          return 0
        else
          echo \"Could not contact the ssh-agent pointed at by SSH_AUTH_SOCK, trying more...\"
        fi
      fi
      #
      # Second effort: If we're still looking for an ssh-agent, try via $sshfile
      #
      if [ -e \"$sshfile\" ]; then
        # Load the environment given in $sshfile
        . $sshfile &>/dev/null
        # Try to contact the ssh-agent
        ssh-add -l &>/dev/null 
        if [[ $? != 2 ]]; then 
          echo \"SSH agent already running; reconfigured the environment.\"
          unset sshfile
          return 0
        else
          echo \"Could not contact the ssh-agent pointed at by $sshfile.\"
        fi
      fi
      #
      # And if we haven't found a working one, start a new one...
      #
      #Create a new ssh-agent
      echo \"Creating new SSH agent.\"
      ssh-agent -s > $sshfile && . $sshfile    
      unset sshfile
      }
          

   A shorter version without all the comments and that does not generate
   output is

   ::

      start-ssh-agent() {
      sshfile=~/.ssh-agent-environment
      #
      if [ -n \"$SSH_AUTH_SOCK\" ]; then
        ssh-add -l &>/dev/null 
        [[ $? != 2 ]] && unset sshfile && return 0
      fi
      #
      if [ -e \"$sshfile\" ]; then
        . $sshfile &>/dev/null
        ssh-add -l &>/dev/null 
        [[ $? != 2 ]] && unset sshfile && return 0
      fi
      #
      ssh-agent -s > $sshfile && . $sshfile &>/dev/null
      unset sshfile
      }
          

   This defines the command ``start-ssh-agent``.

#. Since start-ssh-agent will now first check for a usable running
   agent, it doesn't harm to simply execute this command in your .bashrc
   file to start a SSH authentication agent. So add the line

   ::

      start-ssh-agent &>/dev/null
          

   after the above function definition. All output is sent to ``/dev/null``
   (and hence not shown) as a precaution, since ``scp`` or ``sftp``
   sessions fail when output is generated in ``.bashrc`` on many systems
   (typically with error messages such as \\"Received message too long\"
   or "Received too large sftp packet"). You can also use the newly
   defined command start-ssh-agent at the command prompt. It will then
   check your environment, reset the environment variables ``SSH_AUTH_SOCK``
   and ``SSH_AGENT_PID`` or startk a new ssh-agent.

#. As explained in the `GNU bash manual
   <https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files>`_,
   ``.bashrc`` is only read when starting so-called interactive non-login
   shells. Interactive login shells will not read this file by default.
   Therefore it is `advised in the GNU bash
   manual <https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files>`_
   to add the line

   ::

      [[ -s ~/.bashrc ]] && . ~/.bashrc
          

   to your ``.bash_profile``. This will execute ``.bashrc`` if it exists
   whenever ``.bash_profile`` is called.

You can now simply add your key :ref:`as indicated above <start SSH agent>` with
``ssh-add`` and it will become available in all shells.

The only remaining problem is that the ssh-agent process that you
started may not get killed when you log out, and if it fails to contact
again to the ssh-agent when you log on again, the result may be a
built-up of ssh-agent processes. You can always kill it by hand before
logging out with ``ssh-agent -k``.

Links
-----

-  `ssh-agent manual page <http://man.openbsd.org/ssh-agent>`_ (external)
-  `ssh-add manual page <http://man.openbsd.org/ssh-add>`_ (external)
