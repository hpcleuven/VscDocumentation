.. _Hydra hardware:

Hydra hardware
===============

The VUB Hydra cluster is an heterogeneous cluster with a mixture of nodes with
varied hardware. The majority of nodes are non-GPU nodes for generic
multi-purpose compute, they are distributed in partitions depending on their CPU
microarchitectures and network interconnects. The cluster also contains a number
of nodes with NVIDIA GPUs, which are also distributed in partitions depending on
their GPU generation.

Hardware details
----------------

* Generic nodes

===============  ======  ==========================================  ======  ==========  =======
Slurm partition  nodes   processors per node                         memory  local disk  network
===============  ======  ==========================================  ======  ==========  =======
ivybridge_mpi    16      2x 10-core INTEL E5-2680v2 (ivybridge)      256 GB  900 GB      QDR-IB
broadwell        27      2x 14-core INTEL E5-2680v4 (broadwell)      256 GB    1 TB      10 Gbps
broadwell_himem  1       4x 10-core INTEL E7-8891v4 (broadwell)      1.5 TB    4 TB      10 Gbps
skylake          22      2x 20-core INTEL Xeon Gold 6148 (skylake)   192 GB    1 TB      10 Gbps
skylake_mpi      31      2x 20-core INTEL Xeon Gold 6148 (skylake)   192 GB    1 TB      EDR-IB
===============  ======  ==========================================  ======  ==========  =======

* GPU nodes

===============  ======  ===============================  ==========  =======================================  ==========  ==========  =======
Slurm partition  nodes   GPUs per node                    GPU memory  processors per node                      CPU memory  local disk  network
===============  ======  ===============================  ==========  =======================================  ==========  ==========  =======
kepler_gpu       6       2x Nvidia Tesla K20Xm (kepler)   6 GB        2x 10-core INTEL E5-2680v2 (ivybridge)   128 GB      900 GB      QDR-IB
pascal_gpu       4       2x Nvidia Tesla P100 (pascal)    16 GB       2x 12-core INTEL E5-2650v4 (broadwell)   256 GB      2 TB        10 Gbps
ampere_gpu       6       2x Nvidia A100 (ampere)          40 GB       2x 16-core AMD EPYC 7282 (zen2)          256 GB      2 TB        EDR-IB
===============  ======  ===============================  ==========  =======================================  ==========  ==========  =======

Access restrictions
-------------------

Access is available for faculty members, students (master's projects under faculty
supervision), and researchers of the VUB, as well as VSC users of other Flemish universities.

The cluster is integrated in the VSC network and runs the standard VSC software setup.

Jobs can have a maximal execution wall time of 5 days (120 hours).

Login infrastructure
--------------------

Users with a VSC account (VSC-ID) can connect to Hydra via the following hostname:

* <VSC-ID>@login.hpc.vub.be

Hardware specs:

* 2x Intel Skylake (Xeon Gold 6126) - 24 cores in total (fair share between all
  users)

* 96GB memory (maximum per user: 12GB)

* 10GbE network connection

* Infiniband EDR connection to the storage

User documentation
------------------------

For documentation specific to the VUB cluster, please consult the documentation
at:

https://hpc.vub.be/docs/

For question or problems, please contact the VUB HPC team: hpc@vub.be
