.. _Breniac hardware UAntwerp:

Breniac hardware
================

In 2023, the KU Leuven Tier-1 Breniac cluster was decommissioned. During the summer of 2023, 
24 of the Breniac compute nodes were recovered for use at UAntwerp, replacing the Hopper compute cluster.    
The Breniac cluster has 1 login node and 23 compute nodes with
dual 14-core Intel `Xeon Gold 6132 <https://ark.intel.com/products/123541>`_
Skylake generation CPUs connected through an EDR InfiniBand network.

Access restrictions
-------------------

The Breniac compute nodes should be used for:

  * Jobs that use old software that cannot be properly compiled to benefit from the
    extensions in the instruction sets of Leibniz and Vaughan, or that lack enough
    parallelism to fully exploit the Leibniz or Vaughan compute nodes (even taking 
    into account that multiple jobs launched nearly simultaneously can still make
    it possible to use the full capacity of a Leibniz or Vaughan compute node).
  * Jobs that need more than 128 GB of memory to run properly and that do not need
    more than 28 cores per node.
  * Batches of single core jobs (that cannot be run on your own computer).
  * Jobs that do not fit in a maximum wall time of 3 days and cannot be restarted
    cheaply.

Access is available for faculty, students (master's projects under faculty
supervision), and researchers of the AUHA. The cluster is integrated in the VSC
network but runs an older version of the standard VSC software setup.
It is also available to all
VSC users, though we appreciate that you contact the UAntwerp support team so
that we know why you want to use the cluster.

Jobs can have a maximal execution wall time of 7 days (168 hours). Note however that
this feature should not be abused as there is only very little software that really
needs this.


Hardware details
----------------

- 23 compute nodes

  - 2 Xeon `Gold 6132 <https://ark.intel.com/products/123541>`_ CPU\@2.6GHz (Skylake), 14 cores each
  - 192 GB RAM
  - 500 GB SSD local disk

- 1 login node

  - 2 Xeon `Gold 6132 <https://ark.intel.com/products/123541>`_ CPU\@2.6GHz (Skylake), 14 cores each
  - 192 GB RAM
  - 500 GB SSD local disk

The nodes are connected using an InfiniBand EDR network.
Storage is provided through the central :ref:`UAntwerp storage` system.


Login infrastructure
--------------------

Direct login is possible to the login node.

- From outside the VSC network: use the external interface name. Note that from outside of
  Belgium, a :ref:`VPN connection <vpn>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface name.

============   =================================  ============================
Login node     External interface                 Internal interface
============   =================================  ============================
generic name   login\-breniac.hpc.uantwerpen.be    login.breniac.antwerpen.vsc
============   =================================  ============================


Available resources
-------------------

Characteristics of the compute nodes
""""""""""""""""""""""""""""""""""""

**Breniac is running the Slurm Workload Manager as its resource manager and scheduler.**
We do not support the PBS compatibility layer but encourage users to develop
proper Slurm job scripts as one can then fully exploit the Slurm features and
enjoy the power of the ``srun`` command when starting processes.

Make sure to read the following pages which give a lot of information on Slurm
and how to convert your Torque scripts:

* :ref:`running jobs`
* :ref:`Important differences between Slurm and Torque<Slurm_PBS_differences>`
* :ref:`Converting PBS/Torque options to Slurm <Slurm_convert_from_PBS>`

Since Breniac is a homogeneous system with respect to CPU type, memory and
interconnect, it is not needed to specify any features.

Available partitions
""""""""""""""""""""

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to.
When the option is omitted, your job is submitted to the default partition (*skylake*).

For the Breniac nodes, only a single partition is available:

===========   =========================================================
Partition     Limits
===========   =========================================================
*skylake*     Default. Maximum wall time of 7 days.
===========   =========================================================

Origin of the name
------------------

Breniac is named after the decommissioned Tier-1 Breniac cluster.


