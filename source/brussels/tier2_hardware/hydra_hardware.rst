.. _Hydra hardware:

Hydra hardware
===============

The VUB Hydra cluster contains a mix of nodes containing Intel processors with different CPU microarchitectures and different interconnects in different sections of the cluster. The cluster also contains a number of nodes with NVIDIA GPUs.

Hardware details
----------------

=======  ==========================================  ======  ======  =======  ==================================================
nodes    processor                                   memory  disk    network  extra
=======  ==========================================  ======  ======  =======  ==================================================
11       2x 10-core INTEL E5-2680v2 (ivybridge)      128 GB  900 GB  QDR-IB
20       2x 10-core INTEL E5-2680v2 (ivybridge)      256 GB  900 GB  QDR-IB
6        2x 10-core INTEL E5-2680v2 (ivybridge)      128 GB  900 GB  QDR-IB   2x Tesla K20Xm NVIDIA GPGPUs 6Gb/node (kepler)
27       2x 14-core INTEL E5-2680v4 (broadwell)      256 GB    1 TB  10 Gbps
1        4x 10-core INTEL E7-8891v4 (broadwell)      1.5 TB    4 TB  10 Gbps
4        2x 12-core INTEL E5-2650v4 (broadwell)      256 GB    2 TB  10 Gbps  2x Tesla P100 NVIDIA GPGPUs 16 Gb/node (pascal)
1        2x 16-core INTEL E5-2683v4 (broadwell)      512 GB    8 TB  10 Gbps  4x GeForce 1080Ti NVIDIA GPUs 12 Gb/node (geforce)
22       2x 20-core INTEL Xeon Gold 6148 (skylake)   192 GB    1 TB  10 Gbps
31       2x 20-core INTEL Xeon Gold 6148 (skylake)   192 GB    1 TB  EDR-IB
=======  ==========================================  ======  ======  =======  ==================================================

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

* Intel Skylake (Xeon Gold 6126) - 24 cores in total (fair share between all users)

* 96GB memory (maximum per user: 12GB) 

* 10GbE network connection 

* Infiniband EDR connection to the storage 

User documentation
------------------------

For documentation on Hydra usage, consult the documentation website:

https://hpc.vub.be/documentation

For question or problems, contact the VUB HPC team: hpc@vub.be
