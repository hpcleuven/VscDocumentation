.. _breniac hardware:

BrENIAC
=======

.. toctree::
   :hidden:

   memory_bandwidth_and_latency_breniac

.. include:: breniac_login_nodes.rst


Hardware details
----------------

- 408 Skylake nodes

  - 2 Xeon Gold 6132 CPU\@2.6GHz, 14 cores each
  - 192 GB RAM (:ref:`memory bandwith and latency measurements <memory bandwidth and latency breniac skylake>`)
  - 75 GB SSD local disk

- 436 Broadwell nodes

  - 2 Xeon E5-2680v4 CPUs\@2.4GHz, 14 cores each
  - 128 GB RAM (:ref:`memory bandwith and latency measurements <memory bandwidth and latency breniac broadwell>`)
  - 75 GB SSD local disk

- 144 Broadwell nodes

  - 2 Xeon E5-2680v4 CPUs\@2.4GHz, 14 cores each
  - 256 GB RAM
  - 75 GB SSD local disk

The nodes were connected using an Infiniband EDR network.

.. figure:: breniac.png
   :alt: BrENIAC hardware diagram

BrENIAC storage
---------------

Aside from VSC_HOME and VSC_DATA, the following storage locations
were available on this cluster:

+--------------------------+--------+----------+--------+----------------+
|Variable                  | Type   |  Access  |Backup  | Default quota  |
+==========================+========+==========+========+================+
|$VSC_SCRATCH              | GPFS   |  BrENIAC |NO      | 1 TB           |
|$VSC_SCRATCH_SITE         |        |          |        |                |
+--------------------------+--------+----------+--------+----------------+
|$VSC_SCRATCH_NODE         | ext4   | BrENIAC, |NO      | 75 GB          |
|                          |        | job only |        |                |
+--------------------------+--------+----------+--------+----------------+
