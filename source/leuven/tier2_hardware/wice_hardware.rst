.. _wice hardware:

wICE hardware
===============

wICE is KU Leuven/UHasselt's latest Tier-2 cluster. 
It has thin nodes, large memory nodes, interactive nodes and GPU nodes.
This cluster is in production since February 2023.

Hardware details
----------------

- 172 thin nodes 
   
  - 2 Intel Xeon Platinum 8360Y CPUs\@2.4 GHz (Ice lake), 36 cores each
  - 256 GB RAM 
  - 960 GB SSD local disk
  - partitions ``batch/batch_long``, :ref:`submit options <submit to wice compute node>`

- 5 big memory nodes

  - 2 Intel Xeon Platinum 8360Y CPUs\@2.4 GHz (Ice lake), 36 cores each
  - 2048 GB RAM
  - 960 GB SSD local disk
  - partition ``bigmem``, :ref:`submit options <submit to wice big memory node>`

- 4 GPU nodes, 16 GPU devices

  - 2 Intel Xeon Platinum 8360Y CPUs\@2.4 GHz (Ice lake), 36 cores each
  - 512 GB RAM
  - 4 NVIDIA A100 SXM4, 80 GB GDDR, connected with NVLink
  - 960 GB SSD local disk
  - partition ``gpu``, :ref:`submit options <submit to wice GPU node>`

- 5 interactive nodes

  - 2 Intel Xeon Gold 8358 CPUs\@2.6 GHz (Ice lake), 32 cores each
  - 512 GB RAM
  - 1 NVIDIA A100, 80 GB GDDR 
  - 960 GB SSD local disk
  - partition ``interactive``, :ref:`submit options <submit to wice interactive node>`

The nodes are connected using an Infiniband HDR-100 network, the islands are indicated on the diagram below.

.. figure:: wice_hardware/wice.png
   :alt: wICE hardware diagram


Hardware details (extension)
----------------------------
We are currently installing and testing additional hardware for wICE,
which will be made accessible during the spring of 2024:

- 68 thin nodes

  - 2 Intel Xeon Platinum 8468 CPUs (Sapphire Rapids),
    48 cores each :raw-html:`<br />`
    The base and max CPU frequencies are 2.1 GHz and 3.8 GHz, respectively.
  - 256 GB RAM
  - 960 GB SSD local disk
  - partitions ``batch_sapphirerapids/batch_sapphirerapids_long``

- 4 GPU nodes, 16 GPU devices

  - 2 AMD EPYC 9334 CPUs (Genoa),
    32 cores each :raw-html:`<br />`
    The base and max CPU frequencies are 2.7 GHz and 3.9 GHz, respectively.
  - 770 GB RAM
  - 4 NVIDIA H100 SXM4, 80 GB HBM3, connected with NVLink
  - 960 GB SSD local disk
  - partition ``gpu_h100``

- 1 huge memory node

  - 2 Intel Xeon Platinum 8360Y CPUs (Ice lake),
    36 cores each :raw-html:`<br />`
    The base and max CPU frequencies are 2.4 GHz and 3.5 GHz, respectively.
  - 8192 GB RAM
  - 960 GB SSD local disk
  - partition ``hugemem``

The thin nodes and GPU nodes are all in the same Infiniband HDR-100 network
island. These nodes are furthermore the first ones in the data center
to be direct liquid cooled.
