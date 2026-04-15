.. _mindwell hardware:

Mindwell hardware
=================

Before mid 2026, a new cluster will be added to the KU Leuven/UHasselt's Tier-2 infrastructure.
In line with its predecessor :ref:`wICE <wice hardware>`, it will feature thin nodes,
large memory nodes, interactive nodes and GPU nodes.

Hardware details
----------------

- 40 thin nodes

  - 2 Intel Xeon Platinum 6972P CPUs\@2.4 GHz (Granite Rapids),
    96 cores each
  - 768 GiB RAM
  - default memory per core is 4000 MiB
  - 960 GB NVMe local disk
  - partitions ``batch_graniterapids|batch_graniterapids_long``

- 10 big memory nodes

  - 2 Intel Xeon 6972P CPUs \@2.4 GHz (Granite Rapids),
    96 cores each
  - 1536 GiB RAM
  - default memory per core is 8040 MiB
  - 3840 GB NVMe local disk
  - partition ``bigmem``

- 3 GPU nodes with 24 B200 GPUs in total

  - 2 AMD EPYC 9655 CPUs \@2.6 GHz (Turin),
    96 cores each
  - 1536 GiB RAM
  - default memory per core is 8040 MiB
  - 8 NVIDIA B200 SXM6 (Blackwell),
    192 GiB GDDR, connected with NVLink
  - 960 GB NVMe local disk
  - partition ``gpu_b200``

- 2 interactive nodes

  - 2 Intel Xeon 6972P CPUs \@2.4 GHz,
    96 cores each
  - 768 GiB RAM
  - default memory per core is 2000 MiB
  - maximum memory per core is 4000 MiB
  - 2 NVIDIA RTX 5000 (Ada), 32 GiB GDDR
  - 960 GB SSD local disk
  - partition ``interactive``


Storage
-------

As part of the :ref:`KU Leuven storage <KU Leuven storage>` infrastructure,
a new parallel filesystem will be installed together with the cluster
(IBM Storage Scale, 5.8 PB, connected over NDR).
We will assign scratch storage on this new filesystem and also offer project storage
(similar to the current `staging` storage).
The compute nodes will also be connected to the existing Lustre filesystem (through an
Infiniband HDR-100 network), so all your existing data will be accessible from the new cluster.

Additional highlights
---------------------

- Software modules will only be installed for toolchains starting from 2024a.
- All nodes are interconnected using an Infiniband NDR network.
- Similar to the wICE Sapphire Rapids and the H100 nodes, the new cluster is direct liquid cooled.
