.. _wice_t2_leuven_rocky9:

=================
Rocky 9 migration
=================

The KU Leuven Tier-2 cluster wICE will migrate to Rocky 9.6 as the operating system.
Important differences at the system level are listed below.

+-------------+------------------+---------------------+
| Packages    |  Rocky Linux 8   | Rocky Linux 9       |
+=============+==================+=====================+
| kernel      | 4.18.0-553.58.1  | 5.14.0-570.42.2     |
+-------------+------------------+---------------------+
| bash        | 4.4.20           | 5.1.8               |
+-------------+------------------+---------------------+
| gcc         | 8.5.0            | 11.5.0              |
+-------------+------------------+---------------------+
| glibc       | 2.28             | 2.34                |
+-------------+------------------+---------------------+

Centrally installed modules have already been made available for Rocky 9 for
compute nodes that will be migrated, starting from toolchain 2021a.

.. _timing:

Timing
------

The wICE nodes will be migrated to the new OS in November 2025. We foresee a test period for all users until the end of October.
The Genius cluster will be decommissioned with the arrival of a new Tier-2 cluster at the end of the year. Genius will not be migrated to Rocky 9 anymore.
The new Tier-2 cluster will be launched with Rocky 9.

Please use the test period to try out the new OS before the actual migration
in order to avoid interrupting your workflow.

.. note::

   Be aware that toolchains older than 2021a will no longer be available after Genius has been decommissioned.

As always you can contact hpcinfo@kuleuven.be in case you have questions or remarks.

.. _how to test:

How to test
-----------

We have reserved several nodes of the ``batch``, ``batch_sapphirerapids``,
``gpu_a100`` and ``gpu_h100`` partitions for testing purposes.
To send jobs to these test nodes with Rocky 9, simply submit your job
with the **--reservation=rocky9_pilot** option, for example::

   $ sbatch --reservation=rocky9_pilot myjobscript.slurm

+-----------------------+-------------------+-----------------+
+ Partition             + CPU/GPU type      + Number of nodes +
+=======================+===================+=================+
+ batch,batch_icelake   + IceLake           +              12 +
+-----------------------+-------------------+-----------------+
+ batch_sapphirerapids  + Sapphire Rapids   +              12 +
+-----------------------+-------------------+-----------------+
+ gpu_a100              + IceLake / A100    +               1 +
+-----------------------+-------------------+-----------------+
+ gpu_h100              + Genoa / H100      +               1 +
+-----------------------+-------------------+-----------------+

As the pilot phase continues we may add more nodes to this reservation.
The following query can be used to look up the currently reserved nodes::

   $ scontrol -M wice show reservation rocky9_pilot --json | jq ".reservations[0].node_list"

If you are not a ``vsc3*`` user and also want to test, please ask the
helpdesk to add you to the reservation.

Additionally some of the login nodes have been migrated as well. To land on a
Rocky 9 login node, you need to connect to ``login-rocky9.hpc.kuleuven.be`` (as
opposed to the ``login.hpc.kuleuven.be`` server you normally use). Note that
the ``skylake`` architecture of the current login nodes is different from the
architectures in the ``rocky9_pilot`` reservation. One consequence is that
the ``module avail`` command might not show all modules relevant to
compute jobs. The ``module spider`` command can be used as an alternative,
see :ref:`the module system on Leuven clusters <leuven_module_system>` for
background information. If you encounter inconsistencies between modules
available for Rocky 8 and Rocky 9, please contact the support team.

.. _expected impact:

Expected impact
---------------

The impact of this upgrade will be small for most users. If you are only using
centrally installed modules, your ``module load`` commands will automatically
load the appropriate modules (e.g. the ones installed for Rocky 9 if you are
on a node with Rocky 9). Note that this may not apply if you are
manually modifying your module path (if in doubt, please consult
:ref:`The module system on Leuven clusters <leuven_module_system>`).

.. note::

   If you have been compiling your own software on Rocky 8, it is possible
   that this software will not run on Rocky 9. If this is the case or
   if you have any doubts, we recommend to recompile on a node with the new OS.
   When doing so, it can be convenient to use the ${VSC_OS_LOCAL} variable
   which describes the node's operating system (i.e. "rocky8" or "rocky9").

.. note::
   Keep in mind that also Python or R package installations may involve
   compiling steps for extensions and so may need to be redone for Rocky 9.

.. note::
   Conda environments created on Rocky 8 will normally continue to work
   on Rocky 9 (at least if the compiled components are provided by
   Conda packages, as is normally the case).

Known issues
------------

* Currently the CPU cores are unable to reach the maximal ('turbo') frequency.
  Compared to nodes with Rocky 8, you may therefore see somewhat lower performance
  if only a few cores are active while the other cores are idling.
  This issue is still being investigated.
