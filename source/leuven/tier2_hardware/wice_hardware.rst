.. _wice hardware:

wICE hardware
===============

wICE is KU Leuven/UHasselt's latest Tier-2 cluster. 
It has thin nodes, large memory nodes, interactive nodes and GPU nodes.
This cluster is in production since February 2023
and has been extended with additional compute nodes in early 2024.


Hardware details
----------------

- 240 thin nodes

  - 172 IceLake nodes

    - 2 Intel Xeon Platinum 8360Y CPUs\@2.4 GHz (IceLake),
      36 cores each :raw-html:`<br />`
      (1 NUMA domain and 1 L3 cache per CPU)
    - 256 GiB RAM
    - 960 GB SSD local disk
    - partitions ``batch/batch_long``,
      :ref:`submit options <submit to wice compute node>`

  - 68 Sapphire Rapids nodes

    - 2 Intel Xeon Platinum 8468 CPUs (Sapphire Rapids),
      48 cores each :raw-html:`<br />`
      (4 NUMA domains and 1 L3 cache per CPU) :raw-html:`<br />`
      The base and max CPU frequencies are 2.1 GHz and 3.8 GHz, respectively.
    - 256 GiB RAM
    - 960 GB SSD local disk
    - partitions ``batch_sapphirerapids/batch_sapphirerapids_long``
      :ref:`submit options <submit to wice compute node>`

- 5 big memory nodes

  - 2 Intel Xeon Platinum 8360Y CPUs\@2.4 GHz (Ice lake),
    36 cores each :raw-html:`<br />`
    (2 NUMA domains and 1 L3 cache per CPU)
  - 2048 GiB RAM
  - 960 GB SSD local disk
  - partition ``bigmem``,
    :ref:`submit options <submit to wice big memory node>`

- 1 huge memory node

  - 2 Intel Xeon Platinum 8360Y CPUs (Ice lake),
    36 cores each :raw-html:`<br />`
    (1 NUMA domain and 1 L3 cache per CPU) :raw-html:`<br />`
    The base and max CPU frequencies are 2.4 GHz and 3.5 GHz, respectively.
  - 8 TiB RAM
  - 960 GB SSD local disk
  - partition ``hugemem``,
    :ref:`submit options <submit to wice big memory node>`

- 8 GPU nodes

  - 4 nodes with 16 A100 GPUs in total

    - 2 Intel Xeon Platinum 8360Y CPUs\@2.4 GHz (Ice lake),
      36 cores each :raw-html:`<br />`
      (2 NUMA domains and 1 L3 cache per CPU)
    - 512 GiB RAM
    - 4 NVIDIA A100 SXM4, 80 GiB GDDR, connected with NVLink
    - 960 GB SSD local disk
    - partition ``gpu``,
      :ref:`submit options <submit to wice GPU node>`

  - 4 nodes with 16 H100 GPUs in total

    - 2 AMD EPYC 9334 CPUs (Genoa),
      32 cores each :raw-html:`<br />`
      (4 NUMA domains and 4 L3 caches per CPU) :raw-html:`<br />`
      The base and max CPU frequencies are 2.7 GHz and 3.9 GHz, respectively.
    - 768 GiB RAM
    - 4 NVIDIA H100 SXM5, 80 GiB HBM3, connected with NVLink
    - 960 GB SSD local disk
    - partition ``gpu_h100``,
      :ref:`submit options <submit to wice GPU node>`

- 5 interactive nodes

  - 2 Intel Xeon Gold 8358 CPUs\@2.6 GHz (Ice lake),
    32 cores each :raw-html:`<br />`
    (2 NUMA domains and 1 L3 cache per CPU)
  - 512 GiB RAM
  - 1 NVIDIA A100, 80 GiB GDDR
  - 960 GB SSD local disk
  - partition ``interactive``,
    :ref:`submit options <submit to wice interactive node>`

All nodes of the same type are interconnected using an Infiniband HDR-100
network, except the H100 GPU and hugemem nodes which can only communicate
over ethernet (no high-performance interconnect). The corresponding
network islands are indicated on the diagram below.
All nodes are furthermore connected to the Lustre parallel file system
through an Infiniband HDR-100 network.

.. figure:: wice_hardware/wice.png
   :alt: wICE hardware diagram

The Sapphire Rapids and H100 GPU nodes are the first ones
in the data center to be direct liquid cooled.
