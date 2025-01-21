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

===============  ======  ============================================== ======  ==========  =======
Slurm partition  nodes   processors |nbsp| per |nbsp| node              memory  local disk  network
===============  ======  ============================================== ======  ==========  =======
broadwell_himem  1       4x 10-core `Intel Xeon E7-8891v4`_ (Broadwell) 1.5 TB  4 TB HDD    10 Gbps
skylake          22      2x 20-core `Intel Xeon Gold 6148`_ (Skylake)   192 GB  1 TB HDD    10 Gbps
skylake_mpi      32      2x 20-core `Intel Xeon Gold 6148`_ (Skylake)   192 GB  1 TB HDD    EDR-IB
skylake_mpi      16      2x 14-core `Intel Xeon Gold 6132`_ (Skylake)   192 GB  450 GB HDD  EDR-IB
zen4             20      2x 32-core `AMD EPYC 9384X`_ (Genoa-X)         384 GB  450 GB SSD  25 Gbps
===============  ======  ============================================== ======  ==========  =======

GPU nodes
---------

=============== ===============  =====  ==================================  ==========  ==============================================  ==========  =================  =======
Slurm partition features         nodes  GPUs |nbsp| per |nbsp| node         GPU memory  processors |nbsp| per |nbsp| node               CPU memory  local |nbsp| disk  network
=============== ===============  =====  ==================================  ==========  ==============================================  ==========  =================  =======
| pascal_gpu                     4      | 2x `NVIDIA Tesla P100`_ (Pascal)  16 GB       2x 12-core `Intel Xeon E5-2650v4`_ (Broadwell)  256 GB      2 TB HDD           10 Gbps
| ampere_gpu                     6      | 2x `NVIDIA A100`_ (Ampere)        40 GB       2x 16-core `AMD EPYC 7282`_ (Zen2 - Rome)       256 GB      2 TB SSD           EDR-IB
| ampere_gpu    | big_local_ssd  4      | 2x `NVIDIA A100`_ (Ampere)        40 GB       2x 16-core `AMD EPYC 7282`_ (Zen2 - Rome)       256 GB      5.9 TB SSD         EDR-IB
=============== ===============  =====  ==================================  ==========  ==============================================  ==========  =================  =======

Login nodes
-----------

* nodes: 2 (fair share between all users)

* processors per node: 2x 12-core Intel Xeon Gold 6126 (Skylake)

* memory: 96GB (maximum per user: 12GB)

* 10GbE network connection

* Infiniband EDR connection to the storage

