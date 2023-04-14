.. _genius hardware:

Genius hardware
===============

Genius is KU Leuven/UHasselt's most recent Tier-2 cluster. It has thin nodes, large memory nodes, as well as GPGPU nodes.

.. include:: genius_login_nodes.rst

Hardware details
----------------

- 230 thin nodes 
   
   - 86 skylake nodes

      - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
      - 192 GB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency skylake tier2>`)
      - 200 GB SSD local disk
      - feature skylake

   - 144 cascadelake nodes

      - 2 Xeon Gold 6240 CPUs\@2.6 GHz (Cascadelake), 18 cores each
      - 192 GB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency cascadelake tier2>`)
      - 200 GB SSD local disk
      - feature cascadelake 

- 10 big memory nodes

   - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
   - 768 GB RAM
   - 200 GB SSD local disk
   - partition ``bigmem``, specific ``qsub`` :ref:`options <submit to genius big memory node>` apply.

- 22 GPGPU nodes, 96 GPU devices

   - 20 P100 nodes

      - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
      - 192 GB RAM
      - 4 NVIDIA P100 SXM2\@1.3 GHz, 16 GB GDDR, connected with NVLink
      - 200 GB SSD local disk
      - partition ``gpu``, specific ``qsub`` :ref:`options <submit to genius GPU node>` apply.

   - 2 V100 nodes

      - 2 Xeon Gold 6240 CPUs\@2.6 GHz (Cascadelake), 18 cores each
      - 768 GB RAM
      - 8 NVIDIA V100 SXM2\@1.5 GHz, 32 GB GDDR, connected with NVLink
      - 200 GB SSD local disk
      - partition ``gpu``, specific ``qsub`` :ref:`options <submit to genius GPU node>` apply.


- 4 AMD nodes

   - 2 EPYC 7501 CPUs\@2.0 GHz, 32 cores each
   - 256 GB RAM
   - 200 GB SSD local disk
   - partition ``amd``, specific ``qsub`` :ref:`options <submit to genius AMD node>` apply.

The nodes are connected using an Infiniband EDR network (bandwidth 25 Gb/s), the islands are indicated on the diagram below.

|Genius hardware|

.. |Genius hardware| image:: genius_hardware/genius.png
  :width: 700
  :alt: Genius hardware diagram
