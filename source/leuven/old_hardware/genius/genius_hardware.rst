Genius
======

.. note::

   Genius is a KU Leuven/UHasselt Tier-2 cluster which is still in operation,
   but parts of it have already been decommissioned. This page is only
   for possible future reference.


Hardware details
----------------

- thin nodes

  - 48 of the original 86 Skylake nodes have been decommissioned

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake),
      18 cores each :raw-html:`<br />`
      (1 NUMA domain and 1 L3 cache per CPU)
    - 192 GiB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency genius skylake>`)
    - 200 GB SSD local disk
    - partition ``batch|batch_long``

  - 4 Naples AMD nodes

    - 2 EPYC 7501 CPUs\@2.0 GHz,
      32 cores each :raw-html:`<br />`
      (4 NUMA domains and 8 L3 caches per CPU)
    - 256 GiB RAM
    - 200 GB SSD local disk
    - partition ``amd``

- GPU nodes

  - 5 P100 nodes

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake),
      18 cores each :raw-html:`<br />`
      (1 NUMA domain and 1 L3 cache per CPU)
    - 192 GiB RAM
    - default memory per core is 5000 MiB
    - 4 NVIDIA P100 SXM2\@1.3 GHz, 16 GiB GDDR, connected with NVLink
    - 200 GB SSD local disk
    - partition ``gpu_p100|gpu_p100_long``

