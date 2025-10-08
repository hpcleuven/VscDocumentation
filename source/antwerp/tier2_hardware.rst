.. _UAntwerp hardware:

########################
UAntwerp Tier-2 Clusters
########################

********************
Login infrastructure
********************

You can log in to the CalcUA infrastructure in 2 ways: using SSH via ``login.hpc.uantwerpen.be``,
or using the :ref:`webportal<ood>` at ``portal.hpc.uantwerpen.be``. 
Note that webportal access at CalcUA is still in its testing stage: please report any problems to 
hpc@uantwerpen.be. 

When using SSH, you can also log in directly to the login nodes of the individual clusters
using one of the following hostnames. 

+----------------------------------------------------+-----------------------------------+-----------------------------------+
| Cluster                                            | Generic login name                | Individual login node             |
+====================================================+===================================+===================================+
|:ref:`Vaughan<Vaughan hardware>`                    |login-vaughan.hpc.uantwerpen.be    | | login1-vaughan.hpc.uantwerpen.be|
|                                                    |                                   | | login2-vaughan.hpc.uantwerpen.be|
+----------------------------------------------------+-----------------------------------+-----------------------------------+
|:ref:`Leibniz<Leibniz hardware>`                    | | login-leibniz.hpc.uantwerpen.be | | login1-leibniz.hpc.uantwerpen.be|
|                                                    | | **login.hpc.uantwerpen.be**     | | login2-leibniz.hpc.uantwerpen.be|
+----------------------------------------------------+-----------------------------------+-----------------------------------+
|:ref:`Visualization<remote visualization UAntwerp>` |viz1-leibniz.hpc.uantwerpen.be     |                                   |
+----------------------------------------------------+-----------------------------------+-----------------------------------+
|:ref:`Breniac<Breniac hardware UAntwerp>`           |login-breniac.hpc.uantwerpen.be    |                                   |
+----------------------------------------------------+-----------------------------------+-----------------------------------+

.. note:: Direct login is possible to all login nodes and to the visualization node *from within Belgium only*.
  From outside of Belgium, a :ref:`VPN connection <vpn>` to the UAntwerp network is required.

****************
Compute clusters
****************

The CalcUA infrastructure contains 3 compute clusters. 
Partitions in **bold** are the default partition for the corresponding cluster.

:ref:`Vaughan <Vaughan hardware>`
=================================

+--------------+-------+---------------------------------------------------+----------+---------------------+
| Partition    | Nodes |  CPU-GPU                                          | Memory   | Maximum wall time   |
+==============+=======+===================================================+==========+=====================+
| **zen2**     | 152   | 2x 32-core `AMD EPYC 7452`_                       |  256 GB  | 3 days              |
+--------------+-------+---------------------------------------------------+----------+---------------------+
| zen3         | 24    | 2x 32-core `AMD EPYC 7543`_                       |  256 GB  | 3 days              |
+--------------+-------+---------------------------------------------------+----------+---------------------+
| zen3_512     | 16    | 2x 32-core `AMD EPYC 7543`_                       |  512 GB  | 3 days              |
+--------------+-------+---------------------------------------------------+----------+---------------------+
| ampere_gpu   | 1     | | 2x 32-core `AMD EPYC 7452`_                     |  256 GB  | 1 day               |
|              |       | | 4x `NVIDIA A100`_ (Ampere) 40 GB SXM4           |          |                     |
+--------------+-------+---------------------------------------------------+----------+---------------------+
| arcturus_gpu | 2     | | 2x 32-core `AMD EPYC 7452`_                     |  256 GB  | 1 day               |
|              |       | | 2x `AMD Instinct MI100`_ (Arcturus) 32 GB HBM2  |          |                     |
+--------------+-------+---------------------------------------------------+----------+---------------------+

:ref:`Leibniz <Leibniz hardware>`
=================================

+---------------+-------+------------------------------------------------+----------------------+---------------------+
| Partition     | Nodes |  CPU-GPU                                       | Memory               | Maximum wall time   |
+===============+=======+================================================+======================+=====================+
| **broadwell** | 144   | 2x 14-core `Intel Xeon E5-2680v4`_             | 128 GB               | 3 days              |
+---------------+-------+------------------------------------------------+----------------------+---------------------+
| broadwell_256 | 8     | 2x 14-core `Intel Xeon E5-2680v4`_             | 256 GB               | 3 days              |
+---------------+-------+------------------------------------------------+----------------------+---------------------+
| pascal_gpu    | 2     | | 2x 14-core `Intel Xeon E5-2680v4`_           | 128 GB               | 1 day               |
|               |       | | 2x `NVIDIA Tesla P100`_ (Pascal) 16 GB HBM2  |                      |                     |
+---------------+-------+------------------------------------------------+----------------------+---------------------+

:ref:`Breniac <Breniac hardware UAntwerp>`
==========================================

+--------------+-------+-------------------------------------+--------+---------------------+
| Partition    | Nodes |  CPU                                | Memory | Maximum wall time   |
+==============+=======+=====================================+========+=====================+
| **skylake**  | 23    | 2x 14-core `Intel Xeon Gold 6132`_  | 192 GB | 7 days              |
+--------------+-------+-------------------------------------+--------+---------------------+

**********************
Storage infrastructure
**********************

The storage is organised according to the :ref:`VSC storage guidelines<data location>`.

.. include:: tier2_hardware/uantwerp_storage_quota_table.rst

.. seealso:: For more information on the file systems, please see the :ref:`UAntwerp storage` page.

.. toctree::
   :hidden:
   :maxdepth: 1
  
   tier2_hardware/vaughan_hardware
   tier2_hardware/leibniz_hardware
   tier2_hardware/breniac_hardware
   tier2_hardware/uantwerp_storage
   uantwerp_accounting
   uantwerp_slurm_specifics
   uantwerp_software
   remote_visualization_uantwerp
