.. _genius hardware:

Genius hardware
===============

.. toctree::
   :hidden:

   memory_bandwidth_and_latency_tier2.rst

Genius is one of KU Leuven/UHasselt's Tier-2 clusters, which is in production
since 2018. It has thin nodes, large memory nodes, as well as GPU nodes.

Hardware details
----------------

- 230 thin nodes 
   
  - 86 skylake nodes

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
    - 192 GiB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency skylake tier2>`)
    - 200 GB SSD local disk
    - feature skylake

  - 144 cascadelake nodes

    - 2 Xeon Gold 6240 CPUs\@2.6 GHz (Cascadelake), 18 cores each
    - 192 GiB RAM (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency cascadelake tier2>`)
    - 200 GB SSD local disk
    - feature cascadelake 

- 10 big memory nodes

  - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
  - 768 GiB RAM
  - 200 GB SSD local disk
  - partition ``bigmem``, specific Slurm :ref:`options <submit_genius_bigmem>` apply

- 22 GPGPU nodes, 96 GPU devices

  - 20 P100 nodes

    - 2 Xeon Gold 6140 CPUs\@2.3 GHz (Skylake), 18 cores each
    - 192 GiB RAM
    - 4 NVIDIA P100 SXM2\@1.3 GHz, 16 GiB GDDR, connected with NVLink
    - 200 GB SSD local disk
    - partition ``gpu_p100``, specific Slurm :ref:`options <submit_genius_gpu>` apply

  - 2 V100 nodes

    - 2 Xeon Gold 6240 CPUs\@2.6 GHz (Cascadelake), 18 cores each
    - 768 GiB RAM
    - 8 NVIDIA V100 SXM2\@1.5 GHz, 32 GiB GDDR, connected with NVLink
    - 200 GB SSD local disk
    - partition ``gpu_v100``, specific Slurm :ref:`options <submit_genius_gpu>` apply

- 4 AMD nodes

  - 2 EPYC 7501 CPUs\@2.0 GHz, 32 cores each
  - 256 GiB RAM
  - 200 GB SSD local disk
  - partition ``amd``, specific Slurm :ref:`options <submit_genius_amd>` apply

The nodes are connected using an Infiniband EDR network (bandwidth 25 Gb/s), the islands 
are indicated on the diagram below.

.. figure:: genius_hardware/genius.png
   :alt: Genius hardware diagram
