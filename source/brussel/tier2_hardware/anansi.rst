.. _Anansi cluster:

Anansi Cluster
==============

The VUB Anansi cluster is a small system designed for interactive use and
test/debug jobs. It sits next to :ref:`Hydra cluster` and both clusters share the
same network and :ref:`storage system <VUB storage>`, which simplifies testing
those jobs that will be run on Hydra.

The particularity of Anansi is that its computational resources are distributed
following a non-exclusive policy. This means that resources such as CPU cores
and GPUs allocated to jobs in Anansi might be shared with other jobs. The only
resource that is kept exclusive is system memory.

Shared resources combined with a maximum walltime of 12 hours maximizes the
availability of this cluster for quick interactive use and test/debug tasks,
avoiding wait time in queue.

Technical characteristics of Anansi:

=============== =====  ==============================  ==========  ==============================================  ==========  =================  ===============
Slurm partition nodes  GPUs |nbsp| per |nbsp| node     GPU memory  processors |nbsp| per |nbsp| node               CPU memory  local |nbsp| disk  network
=============== =====  ==============================  ==========  ==============================================  ==========  =================  ===============
| pascal_gpu    1      | 4x `NVIDIA GeForce 1080Ti`_   11 GB       2x 16-core `Intel Xeon E5-2683v4`_ (Broadwell)  512 GB      250GB HDD          10 Gbps
| ada_gpu       2      | 4x `NVIDIA L40S`_             45 GB       2x 32-core `AMD EPYC 9335`_ (zen5)              384 GB      850GB SDD          200 Gbps NDR-IB
=============== =====  ==============================  ==========  ==============================================  ==========  =================  ===============

Login nodes
-----------

Anansi uses the same :ref:`login nodes of Hydra <Hydra login nodes>`.

