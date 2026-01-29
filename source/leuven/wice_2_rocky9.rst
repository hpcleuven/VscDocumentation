.. _wice_t2_leuven_rocky9:

=================
Rocky 9 migration
=================

We plan to update the KU Leuven Tier-2 cluster wICE to Rocky Linux 9.6 as the
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

* The open pilot phase starts from Wednesday 4th until Tuesday 17th of February 2026. 

* The actual migration will take place on Wednesday 18 February 2026. On this day, wICE
  will be unavailable, but the jobs in the queue stay in pending state until the migration
  is completed and the machine is released.

.. _reserved_hardware:

Reserved hardware
-----------------

During the open pilot phase, the following reservations will allow you test your application
on dedicated hardware. Each ``<ReservationName>`` targets a specific hardware on wICE:

* ``rocky9_icelake`` allows you to use up to 12 Icelake nodes
* ``rocky9_sapphirerapids`` allows you to use up to 12 Sapphire Rapids nodes
* ``rocky9_a100`` allows you to use one GPU A100 node
* no reservation is already created for the H100 GPU nodes

.. _how_to_prepare:

Prepare before testing
----------------------

If you are only using centrally-installed modules, your ``module load`` commands
will automatically load the appropriate modules (e.g. the ones installed for Rocky 9 if you are
on a node with Rocky 9). Note that this may not apply if you are manually modifying your module
path (if in doubt, please consult
:ref:`The module system on Leuven clusters <leuven_module_system>`).

If you have been compiling your own software on Rocky 8, it is possible
that this software will not run on Rocky 9. If this is the case or
if you have any doubts, we recommend to recompile on a node with the new OS.
When doing so, it can be convenient to use the ``${VSC_OS_LOCAL}`` variable
which describes the node's operating system (i.e. "rocky8" or "rocky9").

Keep in mind that also Python or R package installations may involve
compiling steps for extensions and may need to be redone for Rocky 9.

Conda environments created on Rocky 8 will normally continue to work
on Rocky 9 (at least if the compiled components are provided by
Conda packages, as is normally the case).

.. _how to test:

Using reserved nodes
--------------------

In order to :ref:`prepare your software <how_to_prepare>`, you need to use one of the
:ref:`target reservations <reserved_hardware>`:

  * add ``--reservation=<ReservationName>`` to your ``srun`` or ``sbatch`` commands
    on the command line, or
  * add ``#SBATCH --reservation=<ReservationName>`` to your jobscripts, or
  * specify the ``<ReservationName>`` in the text field 'Reservation' in the
    :ref:`Open OnDemand <ood>` form for any app

.. _expected impact:

Expected impact
---------------

We have learned from the first migration attempt that the impact of this upgrade will be small
for most users. Currently the CPU cores are unable to reach the maximal ('turbo') frequency.
Compared to nodes with Rocky 8, you may therefore see somewhat lower performance
if only a few cores are active while the other cores are idling.
This issue is still being investigated.