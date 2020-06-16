HPC-UGent Tier-2 hardware
=========================

The Stevin computing infrastructure consists of several Tier2 clusters which are hosted in the S10 datacenter of Ghent University.
This infrastructure is co-financed by FWO and Department of Economy, Science and Innovation (EWI).


Login nodes
-----------
Log in to the HPC-UGent infrastructure using SSH via login.hpc.ugent.be .


Compute clusters
----------------

 =============== ========== ========================================================= ===================== =========================== ======================= 
  cluster name    # nodes                    Processor architecture                    Usable memory/node      Local diskspace/node          Interconnect       
 =============== ========== ========================================================= ===================== =========================== ======================= 
  phanpy               16    2 x 12-core Intel E5-2680v3(Haswell-EP @ 2.5 GHz)         480 GiB               3 x 400 GB(SSD, striped)    FDR InfiniBand         
  golett              200    2 x 12-core Intel E5-2680v3(Haswell-EP @ 2.5 GHz)         53 GiB                500 GB                      FDR-10 InfiniBand      
  swalot              128    2 x 10-core Intel E5-2660v3(Haswell-EP @ 2.6 GHz)         116 GiB               1 TB                        FDR InfiniBand         
  skitty               72    2 x 18-core Intel Xeon Gold 6140(Skylake @ 2.3 GHz)       177 GiB               1 TB                        EDR InfiniBand         
                                                                                                             240 GB SSD                                         
  victini*             96    2 x 18-core Intel Xeon Gold 6140(Skylake @ 2.3 GHz)       88 GiB                1 TB                        10 GbE                 
                                                                                                             240 GB SSD                                         
  joltik               10    2x 16-core Intel Xeon Gold 6242(Cascade Lake @ 2.8 GHz)   256 GiB               800 GB SSD                   double EDR Infiniband  
                             4x NVIDIA Volta V100 GPUs (32GB GPU memory)                                                                      
  kirlia               16    2 x 18-core Intel Xeon Gold 6240(Skylake @ 2.6 GHz)       738 GiB               1.6 TB NVME                     HDR-100 InfiniBand
 =============== ========== ========================================================= ===================== =========================== ======================= 

(*) default cluster

For most recent information about the available resources and cluster status, please consult https://www.ugent.be/hpc/en/infrastructure .


Shared storage
--------------

====================== ===================================================================================================== ===========================  ====================== ====================
Filesystem name        Intended usage                                                                                        Total storage space          Personal storage space VO storage space (*)
====================== ===================================================================================================== ===========================  ====================== ====================
*$VSC_HOME*            Home directory, entry point to the system                                                             51 TB                        3GB *(fixed)*          *(none)*
*$VSC_DATA*            Long-term storage of large data files                                                                 1.8 PB                        25GB *(fixed)*         250GB
*$VSC_SCRATCH*         Temporary fast storage of 'live' data for calculations                                                1.9 PB                         25GB *(fixed)*         250GB
*$VSC_SCRATCH_PHANPY*  Temporary very fast storage of 'live' data for calculations (recommended for very I/O-intensive jobs) 39 TB SSD                    *(none)*               *(none)*
====================== ===================================================================================================== ===========================  ====================== ====================

(*) Storage space for a group of users (Virtual Organisation or VO for short) can be increased significantly on request.

For more information, see our HPC-UGent tutorial: https://www.ugent.be/hpc/en/support/documentation.htm .


User documentation
------------------
Please consult https://www.ugent.be/hpc/en/support/documentation.htm .

In case of questions or problems, don't hesitate to contact the HPC-UGent support team via hpc@ugent.be,
see also https://www.ugent.be/hpc/en/support .
