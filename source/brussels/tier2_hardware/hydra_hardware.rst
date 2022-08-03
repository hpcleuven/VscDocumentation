.. _Hydra hardware:

Hydra hardware
===============

The VUB Hydra cluster is an heterogeneous cluster with a mixture of nodes with
varied hardware. The majority of nodes are non-GPU nodes for generic
multi-purpose compute, they are distributed in partitions depending on their CPU
microarchitectures and network interconnects. The cluster also contains a number
of nodes with NVIDIA GPUs, which are also distributed in partitions depending on
their GPU generation.

CPU-only nodes
--------------

===============  ======  ==========================================  ======  ==========  =======
Slurm partition  nodes   processors per node                         memory  local disk  network
===============  ======  ==========================================  ======  ==========  =======
ivybridge_mpi    16      2x 10-core INTEL E5-2680v2 (Ivybridge)      256 GB  900 GB      QDR-IB
broadwell        27      2x 14-core INTEL E5-2680v4 (Broadwell)      256 GB    1 TB      10 Gbps
broadwell_himem  1       4x 10-core INTEL E7-8891v4 (Broadwell)      1.5 TB    4 TB      10 Gbps
skylake          22      2x 20-core INTEL Xeon Gold 6148 (Skylake)   192 GB    1 TB      10 Gbps
skylake_mpi      31      2x 20-core INTEL Xeon Gold 6148 (Skylake)   192 GB    1 TB      EDR-IB
===============  ======  ==========================================  ======  ==========  =======

GPU nodes
---------

===============  ======  ===============================  ==========  =======================================  ==========  ==========  =======
Slurm partition  nodes   GPUs per node                    GPU memory  processors per node                      CPU memory  local disk  network
===============  ======  ===============================  ==========  =======================================  ==========  ==========  =======
pascal_gpu       4       2x Nvidia Tesla P100 (Pascal)    16 GB       2x 12-core INTEL E5-2650v4 (Broadwell)   256 GB      2 TB        10 Gbps
ampere_gpu       8       2x Nvidia A100 (Ampere)          40 GB       2x 16-core AMD EPYC 7282 (Zen2)          256 GB      2 TB        EDR-IB
===============  ======  ===============================  ==========  =======================================  ==========  ==========  =======

Login nodes
-----------

* nodes: 2 (fair share between all users)

* processors per node: 2x 12-core INTEL Xeon Gold 6126 (Skylake)

* memory: 96GB (maximum per user: 12GB)

* 10GbE network connection

* Infiniband EDR connection to the storage

