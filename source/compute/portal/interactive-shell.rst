.. _ood_interactive_shell:

Interactive shell
-----------------

This app will launch a shell on a compute node in the requested partition,
allowing you to use the requested resources within a Linux terminal.  This
differs from the shell accessed via the "Clusters - Login (Server) Shell Access"
menu item, which connects you to one of the login nodes.

Shell environment
~~~~~~~~~~~~~~~~~

The default environment of your interactive shell is the same as when
launching an interactive job from the terminal with ``srun --pty bash -l``.
