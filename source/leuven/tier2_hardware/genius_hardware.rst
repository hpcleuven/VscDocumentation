Genius hardware
===============

Genius is KU Leuven/UHasselt's most recent Tier-2 cluster. It has thin nodes, large memory nodes, as well as GPGPU nodes.

- 86 thin nodes

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
    - 192 GB RAM
    - 200 GB SSD local disk

- 10 big memory nodes

   - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
   - 768 GB RAM
   - 200 GB SSD local disk
   - specific ``qsub`` :ref:`options <submit to genius big memory node>`

- 20 GPGPU nodes

   - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
   - 192 GB RAM
   - 4 NVIDIA P100\@1.3 GHz, 16 GB GDDR, connected with NVLink
   - 200 GB SSD local disk
   - specific ``qsub`` :ref:`options <submit to genius GPU node>`

- 4 AMD nodes

   - 2 EPYC 7501 CPUs\@2.0 GHz, 32 cores each
   - 264 GB RAM

The nodes are connected using an Infiniband EDR network (bandwidth 25 Gbit/s), the islands are indicated on the diagram below.

|Genius hardware|

.. |Genius hardware| image:: genius_hardware/genius.png
  :width: 700
  :alt: Genius hardware diagram
