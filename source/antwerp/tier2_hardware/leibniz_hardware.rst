.. _Leibniz hardware:

Leibniz hardware
================

Leibniz was installed in the spring of 2017. It is a NEC system consisting of
152 nodes with 2 14-core Intel `E5-2680v4 <https://ark.intel.com/products/75277>`_ 
Broadwell generation CPUs connected through a EDR InfiniBand network. 144 of
these nodes have 128 GB RAM, the other
8 have 256 GB RAM. The nodes do not have a sizeable local disk. The cluster also
contains a node for visualisation and 3 node types for experimenting with accelerator:
2 nodes for GPU computing (NVIDIA Pascal
generation), one node with dual NEC SX-Aurora TSUBASA vector processors
and one node with an Intel Xeon Phi expansion board.

Access restrictions
-------------------

Access is available for faculty, students (master's projects under faculty
supervision), and researchers of the AUHA. The cluster is integrated in the VSC
network and runs the standard VSC software setup. It is also available to all
VSC-users, though we appreciate that you contact the UAntwerpen support team so
that we know why you want to use the cluster.

Jobs can have a maximal execution wall time of 3 days (72 hours).

The login nodes and regular compute nodes are freely available. Contact 
UAntwerp user support (hpc@uantwerpen.be) for access to the visualization node
and accelerator nodes (free of charge but controlled access).

Hardware details
----------------

- 152 compute nodes

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 128 GB RAM (144 nodes) or 256 GB RAM (8 nodes)
    - 120 GB SSD local disk

- 2 GPGPU nodes

   - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
   - 128 GB RAM
   - 2 NVIDIA P100, 16 GB HBM2
   - 120 GB SSD local disk
   - :ref:`Instructions <GPU computing UAntwerp>`
   
- 1 vector computing node (NEC SX-Aurora TSUBASA model A300-2)

   - 1 Xeon `Gold 6126 <https://ark.intel.com/products/120483>`_ CPU\@2.60 GHz (Skylake) with 12 cores
   - 96 GB RAM
   - 2 `NEC SX-Aurora Vector Engines type 10B <https://www.nec.com/en/global/solutions/hpc/sx/vector_engine.html>`_ 
     (per card 8 cores \@1.4 GHz, 48 GB HBM2)
   - 240 GB SSD local disk
   - :ref:`Instructions <UAntwerp NEC SX Aurora>`

- 1 Xeon Phi node

   - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
   - 128 GB RAM
   - Intel Xeon Phi 7220P PCIe card, 16 GB RAM
   - 120 GB SSD local disk

- 2 login nodes

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 256 GB RAM
    - 120 GB SSD local disk

- 1 visualization node

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 256 GB RAM
    - 1 NVIDIA Quadro P5000
    - 120 GB SSD local disk
    - :ref:`Instructions <remote visualization UAntwerp>`

The nodes are connected using an InfiniBand EDR network. 
More info on the storage system is available on the :ref:`UAntwerpen storage` page.


Login infrastructure
--------------------

Direct login is possible to both login nodes and to the visualization node.

- From outside the VSC network: use the external interface names. Outside of
  Belgium, a :ref:`VPN connection <VPN>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface names.

===================   =================================  =========================== 
..                    External interface                 Internal interface
===================   =================================  ===========================
Login generic         login\-leibniz.hpc.uantwerpen.be   ..
Login	              login1\-leibniz.hpc.uantwerpen.be  ln1.leibniz.antwerpen.vsc
..                    login2\-leibniz.hpc.uantwerpen.be  ln2.leibniz.antwerpen.vsc
Visualisation node    viz1\-leibniz.hpc.uantwerpen.be    viz1.leibniz.antwerpen.vsc
===================   =================================  ===========================


Characteristics of the compute nodes
------------------------------------

Since Leibniz is currently a homogeneous system with respect to CPU type and
interconnect, it is not needed to specify the corresponding properties (see
also the page on specifying resources, output files and notifications).

However, to make it possible to write job scripts that can be used on both
Hopper and Leibniz (or other VSC clusters) and to prepare for future extensions
of the cluster, the following features are defined:

============       ====================================================================================
property           explanation
============       ====================================================================================
broadwell          only use Intel processors from the Broadwell family (E5-XXXv4) 
                   (Not needed at the moment as this is the only CPU type)
ib                 use InfiniBand interconnect 
                   (Not needed at the moment as all nodes are connected to the InfiniBand interconnect)
mem128             use nodes with 128 GB RAM (roughly 112 GB available). 
                   This is the majority of the nodes on Leibniz.
mem256             use nodes with 256 GB RAM (roughly 240 GB available). 
                   This property is useful if you submit a batch of jobs that require more than 4 GB of 
                   RAM per processor but do not use all cores and you do not want to use a tool to 
                   bundle jobs yourself such as Worker, as it helps the scheduler to put those jobs on 
                   nodes that can be further filled with your jobs.
============       ====================================================================================
