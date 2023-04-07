Superdome quick start guide
===========================

The :ref:`Superdome <Superdome hardware>` is a shared memory machine
which is intended for applications requiring large amounts of RAM
on a single host.

As Superdome is part of the Genius cluster, please also see the
:ref:`Tier-2 access page<tier2_login_nodes>` for general information
on how to access Genius.

How to run a job on Superdome?
------------------------------

To submit jobs to Superdome from a Genius login node you need to select either
the ``superdome`` or ``superdome_long`` Slurm partition, depending on whether
your job needs less than 3 days or less than 7 days.

The CPU resources on Superdome are furthermore allocated on the basis of entire
sockets and not on the basis of individual cores as on other partitions.
Since the 112 cores in Superdome are grouped in 8 sockets (see the
:ref:`Superdome hardware page<Superdome hardware>`), this means that all
Superdome jobs get access to a number of cores which is a multiple of 14.

The allocation for the following job will hence consist of an entire socket
(and its 14 cores)::

  $ sbatch -M genius -p superdome -A myaccount --ntasks=1 myscript.slurm

By default, each task will be launched on a separate socket. The following
job will therefore get two sockets (and so 28 cores in total)::

  $ sbatch -M genius -p superdome -A myaccount --ntasks=2 myscript.slurm

If you want to get multiple Slurm tasks per socket you will need to use the
``--ntasks-per-socket`` option, for example::

  $ sbatch -M genius -p superdome -A myaccount --ntasks=28 --ntasks-per-socket=14 myscript.slurm

.. note::

   The maximum amount of memory per core for Superdome is 53.5 GB, which is also
   the default value. Your jobs will hence by default receive 749 GB of RAM per
   allocated socket.

