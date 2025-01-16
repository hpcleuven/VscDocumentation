.. _interactive_shell:

Interactive shell
-----------------

This app will launch a shell on (one of) the requested node(s), allowing you to
use these compute resources from within a Linux terminal.  This is different
from the shell you get in the "Clusters - Login Server Shell Access" menu, which
directs you to one of the login nodes.

Shell environment:

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      Currently, the :ref:`cluster modules <cluster_modules>` are not automatically
      loaded when your session starts.  In order to use modules, one needs to
      explicitly load the cluster module that adheres to the choice of cluster and
      partition for his or her job.  For instance, if your job starts on wICE
      interactive partition, one needs to execute the following command::

          module load cluster/wice/interactive

      The same applies for other choices of partitions on Genius or wICE clusters.

   .. tab-item:: VUB

      By default, the environment of your interactive shell is the same as when
      launching an interactive job from the terminal with ``srun --pty bash -l``.
