Genius
======

.. note::

   Genius is a KU Leuven/UHasselt Tier-2 cluster which is still in operation,
   but most of its hardware has already been decommissioned. This page is only
   for possible future reference.

.. toctree::
   :hidden:

   memory_bandwidth_and_latency_genius.rst


Hardware details
----------------

- thin nodes

  - 86 Skylake nodes

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake),
      18 cores each :raw-html:`<br />`
      (1 NUMA domain and 1 L3 cache per CPU)
    - 192 GiB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency genius skylake>`)
    - 200 GB SSD local disk
    - partition ``batch|batch_long`` and ``interactive``

  - 144 Cascadelake nodes

    - 2 Xeon Gold 6240 CPUs\@2.6 GHz (Cascadelake),
      18 cores each :raw-html:`<br />`
      (1 NUMA domain and 1 L3 cache per CPU)
    - 192 GiB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency genius cascadelake>`)
    - default memory per core is 5000 MiB
    - 200 GB SSD local disk
    - partition ``batch|batch_long``

  - 4 Naples AMD nodes

    - 2 EPYC 7501 CPUs\@2.0 GHz,
      32 cores each :raw-html:`<br />`
      (4 NUMA domains and 8 L3 caches per CPU)
    - 256 GiB RAM
    - 200 GB SSD local disk
    - partition ``amd``

- 10 big memory nodes

  - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake),
    18 cores each :raw-html:`<br />`
    (1 NUMA domain and 1 L3 cache per CPU)
  - 768 GiB RAM
  - default memory per core is 21000 MiB
  - 200 GB SSD local disk
  - partition ``bigmem|bigmem_long``

- 1 huge memory node ``Superdome``

  - 8 Xeon Gold 6132 CPUs\@2.6 GHz (Skylake), 14 cores each
  - 6 TiB RAM
  - default memory per core is 53500 MiB
  - partition ``superdome|superdome_long``

- 5 GPU nodes, 20 GPU devices

  - 5 P100 nodes

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake),
      18 cores each :raw-html:`<br />`
      (1 NUMA domain and 1 L3 cache per CPU)
    - 192 GiB RAM
    - default memory per core is 5000 MiB
    - 4 NVIDIA P100 SXM2\@1.3 GHz, 16 GiB GDDR, connected with NVLink
    - 200 GB SSD local disk
    - partition ``gpu_p100|gpu_p100_long``


The nodes were connected using an Infiniband EDR network (bandwidth 25 Gb/s).
The islands are indicated on the diagram below.

.. figure:: genius.png
   :alt: Genius hardware diagram

