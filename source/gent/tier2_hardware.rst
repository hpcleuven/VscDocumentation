HPC-UGent Tier-2 hardware
=========================

The Stevin computing infrastructure consists of several Tier2 clusters which are hosted in the S10 datacenter of Ghent University.
This infrastructure is co-financed by FWO and Department of Economy, Science and Innovation (EWI).


Login nodes
-----------
Log in to the HPC-UGent infrastructure using SSH via login.hpc.ugent.be .


Compute clusters
----------------

 =============== ========== =========================================================== ===================== =========================== ======================= ===================
  cluster name    # nodes                    Processor architecture                     Usable memory/node    Local diskspace/node        Interconnect            Operating system
 =============== ========== =========================================================== ===================== =========================== ======================= ===================
  swalot              128    2 x 10-core Intel E5-2660v3 (Haswell-EP @ 2.6 GHz)         116 GiB               1 TB                        FDR InfiniBand          RHEL 8
  skitty               72    2 x 18-core Intel Xeon Gold 6140 (Skylake @ 2.3 GHz)       177 GiB               1 TB + 240GB SSD            EDR InfiniBand          RHEL 8
  victini              96    2 x 18-core Intel Xeon Gold 6140 (Skylake @ 2.3 GHz)       88 GiB                1 TB + 240 GB SSD           10 GbE                  RHEL 8
  joltik               10    2x 16-core Intel Xeon Gold 6242 (Cascade Lake @ 2.8 GHz)   256 GiB               800 GB SSD                  double EDR Infiniband   RHEL 8
                             + 4x NVIDIA Volta V100 GPUs (32GB GPU memory)

  kirlia+++             4    2 x 18-core Intel Xeon Gold 6240 (Cascade Lake @ 2.6 GHz)  738 GiB               1.6 TB NVME                 HDR-100 InfiniBand      RHEL 8
  doduo+              128    2x 48-core AMD EPYC 7552 (Rome @ 2.2 GHz)                  250 GiB               180 GB SSD                  HDR-100 InfiniBand      RHEL 8
  accelgor              9    2x 24-core AMD EPYC 7413 (Milan @ 2.2 GHz)                 500 GiB               180GB SSD                   HDR-100 InfiniBand      RHEL 8
                             + 4x NVIDIA Ampere A100 GPUs (80GB GPU memory)
  donphan++            12    2 x 18-core Intel Xeon Gold 6240 (Cascade Lake @ 2.6 GHz)  738 GiB               1.6 TB NVME                 HDR-100 InfiniBand      RHEL 8
                             + 1x shared NVIDIA Ampere A2 GPU (16GB GPU memory)
  gallade              12    2x 64-core AMD EPYC 7773X (Milan-X @ 2.2 GHz)              940 GiB               1.5 TB NVME                 HDR-100 InfiniBand      RHEL 8
 =============== ========== =========================================================== ===================== =========================== ======================= ===================

(+) default cluster  (++) interactive / debug  (+++) retiring

For most recent information about the available resources and cluster status, please consult https://www.ugent.be/hpc/en/infrastructure .


.. _UGent storage:

Shared storage
--------------

======================= ===================================================================================================== ===========================  ====================== ====================
Filesystem name         Intended usage                                                                                        Total storage space          Personal storage space VO storage space (+)
======================= ===================================================================================================== ===========================  ====================== ====================
*$VSC_HOME*             Home directory, entry point to the system                                                             51 TB                        3GB *(fixed)*          *(none)*
*$VSC_DATA*             Long-term storage of large data files                                                                 1.8 PB                       25GB *(fixed)*         250GB
*$VSC_SCRATCH*          Temporary fast storage of 'live' data for calculations                                                1.9 PB                       25GB *(fixed)*         250GB
*$VSC_SCRATCH_ARCANINE* Temporary very fast storage of 'live' data for calculations (recommended for very I/O-intensive jobs) 70 TB NVME                   *(none)*               *upon request*
======================= ===================================================================================================== ===========================  ====================== ====================

(+) Storage space for a group of users (Virtual Organisation or VO for short) can be increased significantly on request.

For more information, see our HPC-UGent tutorial: https://www.ugent.be/hpc/en/support/documentation.htm .


User documentation
------------------
Please consult https://www.ugent.be/hpc/en/support/documentation.htm .

In case of questions or problems, don't hesitate to contact the HPC-UGent support team via hpc@ugent.be,
see also https://www.ugent.be/hpc/en/support .
