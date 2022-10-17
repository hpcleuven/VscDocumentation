.. _Hopper hardware:

Hopper hardware
===============

Hopper was a compute cluster at UAntwerp in operation from late 2014 till the
summer of 2020. The cluster had 168 compute nodes with
dual 10-core Intel `E5-2680v2 <https://ark.intel.com/products/75277>`_
Ivy Bridge generation CPUs connected through an InfiniBand FDR10 network.
144 of those compute nodes had 64 GB RAM and 24 had 256 GB of RAM.

When the cluster was moved out in the summer of 2020 to make space for the
installation of :ref:`Vaughan<Vaughan hardware>`, the 24 nodes with 256 GB were recovered for further use.

Access restrictions
-------------------

The Hopper compute nodes should be used for:

  * Jobs that use old software that cannot be properly compiled to benefit from the
    extensions in the instruction sets of Leibniz and Vaughan, or that lack enough
    parallelism to fully exploit the Leibniz or Vaughan compute nodes (even taking 
    into account that multiple jobs launched nearly simultaneously can still make
    it possible to use the full capacity of a Leibniz or Vaughan compute node).
  * Jobs that need more than 128 GB of memory to run properly and that do not need
    more than 20 cores per node.
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

    - 2 Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (Ivy Bridge), 10 cores each
    - 256 GB RAM
    - 500 GB local disk

- 1 login node

    - 2 Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (Ivy Bridge), 10 cores each
    - 256 GB RAM
    - 500 GB local disk

The nodes are connected using an InfiniBand FDR10 network.
Storage is provided through the central :ref:`UAntwerp storage` system.


Login infrastructure
--------------------

Direct login is possible to the login node.

- From outside the VSC network: use the external interface name. Note that from outside of
  Belgium, a :ref:`VPN connection <VPN>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface name.

============   =================================  ============================
Login node     External interface                 Internal interface
============   =================================  ============================
generic name   login\-hopper.hpc.uantwerpen.be    login.hopper.antwerpen.vsc
============   =================================  ============================


Available resources
-------------------

Characteristics of the compute nodes
""""""""""""""""""""""""""""""""""""

**Hopper is running the Slurm Workload Manager as its resource manager and scheduler.**
We do not support the PBS compatibility layer but encourage users to develop
proper Slurm job scripts as one can then fully exploit the Slurm features and
enjoy the power of the ``srun`` command when starting processes.

Make sure to read the following pages which give a lot of information on Slurm
and how to convert your Torque scripts:

* :ref:`Local Slurm documentation <Antwerp Slurm>`
* :ref:`Important differences between Slurm and Torque<Antwerp Slurm_PBS_differences>`
* :ref:`Converting PBS/Torque options to Slurm <Antwerp Slurm_convert_from_PBS>`

Since Hopper is a homogeneous system with respect to CPU type, memory and
interconnect, it is not needed to specify any features.

Available partitions
""""""""""""""""""""

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to.
When the option is omitted, your job is submitted to the default partition (*ivybridge*).

For the Hopper nodes, only a single partition is available:

===========   =========================================================
Partition     Limits
===========   =========================================================
*ivybridge*   Default. Maximum wall time of 7 days.
===========   =========================================================

Origin of the name
------------------

Hopper is named after `Grace Hopper <https://en.wikipedia.org/wiki/Grace_Hopper>`_.
Grace Hopper was an American mathematician turned computer scientist and United States Navy
rear admiral. She worked as a programmer of some of the first computer systems and devised
hte theory of machine independent programming languages. Her work laid at the base of the 
programming language COBOL. 


