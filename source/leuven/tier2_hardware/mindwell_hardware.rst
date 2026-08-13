.. _mindwell hardware:

Mindwell hardware
=================

The KU Leuven / UHasselt Tier-2 cluster *Mindwell* entered
production around mid 2026. Mindwell contains thin nodes, large memory
nodes and GPU nodes.

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
  - default memory per core is 8000 MiB
  - 3840 GB NVMe local disk
  - partition ``bigmem``

- 3 GPU nodes with 24 B200 GPUs in total

  - 2 AMD EPYC 9655 CPUs \@2.6 GHz (Turin),
    96 cores each
  - 1536 GiB RAM
  - default memory per core is 8000 MiB
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

A new IBM Storage Scale (also known as GPFS) parallel filesystem with a capacity
of 5.8 PB is connected over NDR to the Mindwell cluster. Both scratch and project
storage (the latter being similar to the `staging` storage on the Lustre parallel
filesystem) are available on this new filesystem.
The Mindwell compute nodes are also connected to the existing Lustre filesystem
(through an Infiniband HDR-100 network), so all your existing
data is accessible from the new cluster. Please read more about the
:ref:`available scratch filesystems <leuven_scratch>` for detailed information and
best practices.

Additional highlights
---------------------

- Software modules are only provided for toolchains starting from 2024a
  (CPU partitions) or 2025a (GPU partitions).
- All nodes are interconnected using an Infiniband NDR network.
- Similar to the wICE Sapphire Rapids and the H100 nodes, the new cluster is direct liquid cooled.
