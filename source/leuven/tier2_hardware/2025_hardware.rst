.. _2025 hardware:

Tier-2 2025 new cluster 
=======================

This year a new cluster will be added to the KU Leuven/UHasselt's environment.
Inline with wICE it features thin nodes, large memory nodes, interactive nodes and GPU nodes.
This cluster will be installed at the end of 2025, below you can already checkout the specs.


Hardware details
----------------

- 40 thin nodes

  - 40 Granite Rapids nodes

    - 2 Intel Xeon Intel Xeon 6972P CPUs\@2.4 GHz,
      96 cores each 
    - 768 GiB RAM
    - default memory per core is TBA
    - 960 GB NVMe local disk
    - partitions TBA ``batch_granite``,

- 10 big memory nodes

  - 2  Intel  Xeon Intel Xeon 6972P CPUs\@2.4 GHz,
    96 cores each 
  - 1536 GiB RAM
  - default memory per core is TBA
  - 3840 GB NVMe local disk
  - partition TBA ``bigmem``,

- 3 GPU nodes

  - 3 nodes with 24 B200 GPUs in total

    - 2 AMD EPYC 9655\@2.6 GHz (Ice lake),
      96 cores each 
    - 1536 GiB RAM
    - default memory per core is TBA
    - 8 NVIDIA B200 SXM6, 192 GiB GDDR, connected with NVLink
    - 960 GB NVMe local disk
    - partition TBA ``gpu|gpu_b200``,

- 2 interactive nodes

  - 2 Intel  Xeon Intel Xeon 6972P CPUs\@2.4 GHz,
    96 cores each :raw-html:`<br />`
    (2 NUMA domains and 1 L3 cache per CPU)
  - 768 GiB RAM
  - default memory per core is TBA
  - 2 NVIDIA RTX 5000, 32 GiB GDDR
  - 960 GB SSD local disk
  - partitions TBA ``interactive``,

All nodes are interconnected using an Infiniband NDR 
network
All nodes are connected to the Lustre parallel file system
through an Infiniband HDR-100 network.

Just as wICE Sapphire Rapids, the new cluster is direct liquid cooled.

Storage
-------

A new parallel filesystem will be installed together with the cluster.
IBM Storage Scale, 5.8 PB . This filesystem will be connected over NDR.

A connection to the existing Lustre filesystem will be setup, 
to make sure your existing data is accessible from the new cluster.

Scratch will be provided on the new filesystem and also project storage equivalent with current staging functionality.

