.. _ood_interactive_shell:

Interactive shell
-----------------

This app will launch a shell on a compute node in the requested partition,
allowing you to use the requested resources within a Linux terminal.  This
differs from the shell accessed via the "Clusters - Login (Server) Shell Access"
menu item, which connects you to one of the login nodes.

Shell environment
~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Currently, the :ref:`cluster modules <cluster_modules>` are not automatically
      loaded when your session starts.  In order to use modules, one needs to
      explicitly load the cluster module that adheres to the choice of cluster and
      partition for his or her job.  For instance, if your job starts on wICE
      interactive partition, one needs to execute the following command::

          module load cluster/wice/interactive

      The same applies for other choices of partitions on Genius or wICE clusters.

   .. tab-item:: VUB
      :sync: vub

      The default environment of your interactive shell is the same as when
      launching an interactive job from the terminal with ``srun --pty bash -l``.
