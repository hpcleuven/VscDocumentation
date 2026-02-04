.. _Hydra cluster:

Hydra Cluster
=============

The VUB Hydra cluster is a heterogeneous Tier-2 cluster with a mixture of nodes
with varied hardware. The majority of nodes are non-GPU nodes for generic
multi-purpose compute, they are distributed in partitions depending on their CPU
microarchitectures and network interconnects. The cluster also contains a number
of nodes with NVIDIA GPUs, which are also distributed in partitions depending on
their GPU generation.

CPU-only nodes
--------------

===================  ==============  ============================================== ======  ==========  ===============
Slurm partition      nodes           processors |nbsp| per |nbsp| node              memory  local disk  network
===================  ==============  ============================================== ======  ==========  ===============
``zen4``             20              2x 32-core `AMD EPYC 9384X`_ (Genoa-X)         384 GB  450 GB SSD  25 Gbps
``zen5_mpi``         20+4\ :sup:`a`  2x 64-core `AMD EPYC 9535`_ (Turin)            768 GB  450 GB SSD  200 Gbps NDR-IB
``zen5_himem``       4               2x 64-core `AMD EPYC 9535`_ (Turin)            1.5 TB  450 GB SSD  200 Gbps NDR-IB
===================  ==============  ============================================== ======  ==========  ===============

:sup:`a` The ``zen5_himem`` nodes are also part of the ``zen5_mpi`` partition

GPU nodes
---------

===============   =================  =====    ================================  ==========  ==============================================  ==========  =================  ===============
Slurm partition   features           nodes    GPUs |nbsp| per |nbsp| node       GPU memory  processors |nbsp| per |nbsp| node               CPU memory  local |nbsp| disk  network
===============   =================  =====    ================================  ==========  ==============================================  ==========  =================  ===============
``pascal_gpu``                         4      2x `NVIDIA Tesla P100`_ (Pascal)  16 GB       2x 12-core `Intel Xeon E5-2650v4`_ (Broadwell)  256 GB      2 TB HDD           10 Gbps
``ampere_gpu``                         6      2x `NVIDIA A100`_ (Ampere)        40 GB       2x 16-core `AMD EPYC 7282`_ (Zen2 - Rome)       256 GB      2 TB SSD           100 Gbps EDR-IB
``ampere_gpu``    ``big_local_ssd``    4      2x `NVIDIA A100`_ (Ampere)        40 GB       2x 16-core `AMD EPYC 7282`_ (Zen2 - Rome)       256 GB      5.9 TB SSD         100 Gbps EDR-IB
===============   =================  =====    ================================  ==========  ==============================================  ==========  =================  ===============

.. _Hydra login nodes:

Login nodes
-----------

* nodes: 2 (fair share between all users)

* processors per node: 2x 12-core Intel Xeon Gold 6126 (Skylake)

* memory: 96GB (maximum per user: 12GB)

* 10GbE network connection

* Infiniband EDR connection to the storage

