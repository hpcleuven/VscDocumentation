Breniac hardware
================

**Breniac was the VSC's Tier-1 cluster hosted by KU Leuven, and it was decomissioned in December 2022.
This page is obsolete, and we keep it only for the future reference.**

.. include:: breniac_login_nodes.rst


Hardware details
----------------

- 408 skylake nodes

   - 2 Xeon Gold 6132 CPU\@2.6GHz, 14 cores each
   - 192 GB RAM (:ref:`memory bandwith and latency measurements <memory bandwidth and latency skylake tier1>`)
   - 75 GB SSD local disk

- 436 broadwell nodes

   - 2 Xeon E5-2680v4 CPUs\@2.4GHz, 14 cores each
   - 128 GB RAM (:ref:`memory bandwith and latency measurements <memory bandwidth and latency broadwell tier1>`)
   - 75 GB SSD local disk

- 144 broadwell nodes

   - 2 Xeon E5-2680v4 CPUs\@2.4GHz, 14 cores each
   - 256 GB RAM
   - 75 GB SSD local disk

The nodes were connected using an Infiniband EDR network.


|Breniac hardware|


Breniac storage
---------------

Your ``$VSC_HOME`` and ``$VSC_DATA`` directory are mounted on the Breniac
login and compute nodes.  See your VSC institute's information on local
storage about policies and quota.

.. note::

   ``$VSC_HOME`` and ``$VSC_DATA`` are mounted using NFS, so they can not
   be used for parallel I/O.  If your software benefits from using a
   parallel file system, please use ``$VSC_SCRATCH``.


+--------------------------+--------+----------+--------+----------------+
|Variable                  | Type   |  Access  |Backup  | Default quota  |
+==========================+========+==========+========+================+
|$VSC_SCRATCH              | GPFS   |  breniac |NO      | 1 TB           |
|$VSC_SCRATCH_SITE         |        |          |        |                |
+--------------------------+--------+----------+--------+----------------+
|$VSC_SCRATCH_NODE         | ext4   | breniac, |NO      | 75 GB          |
|                          |        | job only |        |                |
+--------------------------+--------+----------+--------+----------------+

The path names given below should be adapted to reflect your home
institution and VSC account number.

+--------------------------+------------------------------+
|Variable                  |Name                          |
+==========================+==============================+
|$VSC_HOME                 |/user/leuven/30X/vsc30XYZ     |
+--------------------------+------------------------------+
|$VSC_DATA                 |/data/leuven/30X/vsc30XYZ     |
+--------------------------+------------------------------+
|$VSC_SCRATCH              |/scratch/leuven/30X/vsc30XYZ  |
|$VSC_SCRATCH_SITE         |                              |
+--------------------------+------------------------------+
|$VSC_SCRATCH_NODE         |/local_scratch                |
+--------------------------+------------------------------+


.. |Breniac hardware| image:: breniac_hardware/breniac.png
  :width: 800
  :alt: Breniac hardware diagram
