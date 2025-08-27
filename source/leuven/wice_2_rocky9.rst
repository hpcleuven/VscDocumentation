.. _wice_t2_leuven:

=================
Rocky 9 migration
=================

The KU Leuven Tier-2 cluster wICE will migrate to Rocky 9.5 as the operating system.
Important differences at the system level are listed below.

+-------------+------------------+---------------------+
| Packages    |  Rocky Linux 8   | Rocky Linux 9       |
+=============+==================+=====================+
| kernel      | 4.18.0-513.24.1  | 5.14.0-503.38.1     |           
+-------------+------------------+---------------------+
| bash        | 4.4.20           | 5.1.8               | 
+-------------+------------------+---------------------+
| gcc         | 8.5.0            | 11.5.0              |
+-------------+------------------+---------------------+
| glibc       | 2.28             | 2.34                |
+-------------+------------------+---------------------+

Please note that central installed modules are already available for Rocky 9, starting from toolchain 2021a.

.. _timing:

Timing
------

The wICE nodes will be migrated to the new OS in November. We forsee a test period for all users until end of October.
The Genius cluster will be decommissioned with the arrival of a new Tier-2 cluster at the end of the year. Genius will not be migrated to Rock9 anymore.
The new Tier-2 cluster will be launched with Rocky9.

Please use the test period to try out the new OS before the actual migration
in order to avoid interrupting your workflow. 

.. note::

   Be aware that with the decommissioning of Genius toolchains older that 2021a will not be available anymore.

As always you can contact hpcinfo@kuleuven in case you have questions or remarks.

.. _how to test:

How to test
-----------

In order to give users the chance to test out the new operating system,
some nodes of the batch, batch_sapphirerapids, gpu_a100 and gpu_h100 partitions
have alreay been upgraded. To submit jobs to the upgraded nodes,
simply submit your job with the **--reservation=rocky9_pilot** option to one of the partitions.
::
   $ sbatch --account=lp_myproject --clusters=wice --reservation=rocky9_pilot\
            --nodes=2 --ntasks-per-node=72 --time=2:00:00 myjobscript.slurm

Without mentioning a partition you will arrive on the default batch partitions wich contains icelake nodes.

+-----------------------+-------------------+-----------------+
+ partition             + CPU/GPU type      + number of nodes +
+=======================+===================+=================+
+ batch,batch_icelake   + icelake           +               8 +
+-----------------------+-------------------+-----------------+
+ batch_sapphirerapids  + sapphire rapids   +              16 +
+-----------------------+-------------------+-----------------+
+ gpu_a100              + icelake / A100    +               1 +
+-----------------------+-------------------+-----------------+
+ gpu_h100              + genoa / H100      +               1 +
+-----------------------+-------------------+-----------------+

.. _expected impact:

Expected impact
---------------

The impact of this upgrade will be small for most users. In case
you are only using centrally installed modules, the modules that are
appropriate for the new operating system will be loaded automatically
when necessary, assuming you are using the cluster modules correctly,
see :ref:`module system<leuven_module_system>`.

.. note::

   When you are compiling your own software (which can also be the case
   if you have installed your own Python or R packages), it might be necessary
   to recompile on a node with the new operating system. If your compiled
   software does not link to system libraries, it is possible the old
   executables will still work. In case of doubt, we recommend to recompile.
   It can be handy to make use of the ${VSC_OS_LOCAL} variable, which will
   be set to rocky8 or rocky9 depending on the node you are on.

