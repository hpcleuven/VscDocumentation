.. _wice_t2_leuven_rocky9:

=================
Rocky 9 migration
=================

.. note::

   The wICE OS update to Rocky 9 was originally planned for November 2025.
   We have however decided to postpone it until the performance issues with
   Intel Turbo Boost have been resolved (see the bottom of this page).

   Once we are confident that these performance issues can be resolved,
   we will plan a new (short) test phase.

   In the meantime, nodes where Rocky 9 has been deployed for testing purposes
   will be gradually reverted to Rocky 8. The associated ``rocky9_pilot``
   Slurm reservation will eventually be removed.

We plan to update the KU Leuven Tier-2 cluster wICE to Rocky Linux 9 as the
operating system. Important differences at the system level are listed below.

+-------------+------------------+---------------------+
| Packages    | Rocky Linux 8    | Rocky Linux 9       |
+=============+==================+=====================+
| kernel      | 4.18.0-553.58.1  | 5.14.0-570.42.2     |
+-------------+------------------+---------------------+
| bash        | 4.4.20           | 5.1.8               |
+-------------+------------------+---------------------+
| gcc         | 8.5.0            | 11.5.0              |
+-------------+------------------+---------------------+
| glibc       | 2.28             | 2.34                |
+-------------+------------------+---------------------+

Centrally installed modules have already been made available for Rocky 9,
starting from toolchain 2021a.

.. _timing:

Timing
------

(To be decided)

.. _how to test:

How to test
-----------

(To be revisited)

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
