HPC-UGent Tier-2 hardware
=========================

The Stevin computing infrastructure consists of several Tier2 clusters which are hosted in the S10 datacenter of Ghent University.
This infrastructure is co-financed by FWO and Department of Economy, Science and Innovation (EWI).


Login nodes
-----------
Log in to the HPC-UGent infrastructure using SSH via login.hpc.ugent.be .


Compute clusters
----------------

============	=======	====================================================	===========	=========================	============
cluster name	# nodes	Processor architecture                               	Memory/node	Local diskspace/node		Interconnect
============	=======	====================================================	===========	=========================	============
phanpy		16	2 x 12-core Intel E5-2680v3 (Haswell-EP @ 2.5 GHz)	512 GB		3 x 400 GB (SSD, striped)	FDR InfiniBand
golett		200	2 x 12-core Intel E5-2680v3 (Haswell-EP @ 2.5 GHz)	64 GB		500 GB				FDR-10 InfiniBand
swalot		128	2 x 10-core Intel E5-2660v3 (Haswell-EP @ 2.6 GHz)	128 GB		1 TB				FDR InfiniBand
skitty		72	2 x 18-core Intel Xeon Gold 6140 (Skylake @ 2.3 GHz)	192 GB		1 TB & 240 GB SSD		EDR InfiniBand
victini*	96	2 x 18-core Intel Xeon Gold 6140 (Skylake @ 2.3 GHz)	96 GB		1 TB & 240 GB SSD		10 GbE
============	=======	====================================================	===========	=========================	============

(*) default cluster

For most recent information about the available resources and cluster status, please consult https://www.ugent.be/hpc/en/infrastructure .


Shared storage
--------------

====================== ===================================================================================================== ===========================  ====================== ====================
Filesystem name        Intended usage                                                                                        Total storage space          Personal storage space VO storage space (*)
====================== ===================================================================================================== ===========================  ====================== ====================
*$VSC_HOME*            Home directory, entry point to the system                                                             35 TB                        3GB *(fixed)*          *(none)*
*$VSC_DATA*            Long-term storage of large data files                                                                 702 TB *(can grow to 1 PB)*  25GB *(fixed)*         250GB
*$VSC_SCRATCH*         Temporary fast storage of 'live' data for calculations                                                1 PB                         25GB *(fixed)*         250GB
*$VSC_SCRATCH_PHANPY*  Temporary very fast storage of 'live' data for calculations (recommended for very I/O-intensive jobs) 35 TB SSD                    *(none)*               *(none)*
====================== ===================================================================================================== ===========================  ====================== ====================


(*) Storage space for a group of users (Virtual Organisation or VO for short) can be increased significantly on request.

For more information, see our HPC-UGent tutorial: https://www.ugent.be/hpc/en/support/documentation.htm .


User documentation
------------------
Please consult https://www.ugent.be/hpc/en/support/documentation.htm .

In case of questions or problems, don't hesitate to contact the HPC-UGent support team via hpc@ugent.be,
see also https://www.ugent.be/hpc/en/support .
