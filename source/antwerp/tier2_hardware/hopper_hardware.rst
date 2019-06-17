.. _Hopper hardware:

Hopper hardware
===============

Hopper was installed in 2014. It is a HP system consisting of 168 nodes with 2
10-core Intel `E5-2680v2 <https://ark.intel.com/products/75277>`_ Ivy Bridge
generation CPUs connected through a FDR10 InfiniBand network. 144 nodes have a
memory capacity of 64 GB while 24 nodes have 256 GB of RAM memory.

Access restrictions
-------------------

Access ia available for faculty, students (master's projects under faculty
supervision), and researchers of the AUHA. The cluster is integrated in the VSC
network and runs the standard VSC software setup. It is also available to all
VSC-users, though we appreciate that you contact the UAntwerpen support team so
that we know why you want to use the cluster.

Jobs can have a maximal execution wall time of 3 days (72 hours).


Hardware details
----------------

- 168 compute nodes

    - 2 Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (IvyBridge), 10 cores each
    - 64 GB RAM (144 nodes) or 256 GB RAM (24 nodes)
    - 500 GB local disk

- 3 login nodes

    - 2 Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (IvyBridge), 14 cores each
    - 64 GB RAM
    - 500 GB local disk

The nodes are connected using an Infiniband FDR10 network.
Storage is provided through a 100 TB DDN SFA7700 disk array with 4 storage servers.
More info on the storage system is available on the :ref:`UAntwerpen storage` page.


Login infrastructure
--------------------

Direct login is possible to both login nodes and to the visualization node.

- From outside the VSC network: use the external interface names. Outside of
  Belgium, a VPN connection to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal interface names.

===================   =================================  ===========================
..                    External interface                 Internal interface
===================   =================================  ===========================
Login generic         login.hpc.uantwerpen.be            ..
..                    login\-hopper.hpc.uantwerpen.be    ..
Login                 login1\-hopper.hpc.uantwerpen.be   ln01.hopper.antwerpen.vsc
..                    login2\-hopper.hpc.uantwerpen.be   ln02.hopper.antwerpen.vsc
..                    login3\-hopper.hpc.uantwerpen.be   ln03.hopper.antwerpen.vsc
===================   =================================  ===========================


Characteristics of the compute nodes
------------------------------------

Since Hopper is currently a homogenous system with respect to CPU type and
interconnect, it is not needed to specify the corresponding properties (see
also the page on specifying resources, output files and notifications).

However, to make it possible to write job scripts that can be used on both
Hopper and Leibniz (or other VSC clusters) and to prepare for future extensions
of the cluster, the following features are defined:

============       ====================================================================================
property           explanation
============       ====================================================================================
ivybridge          only use Intel processors from the IvyBridge family (E5-XXXv2)
                   (Not needed at the moment as this is the only CPU type)
ib                 use InfiniBand interconnect
                   (Not needed at the moment as all nodes are connected to the InfiniBand interconnect)
mem64	           use nodes with 64 GB RAM (58 GB available)
mem256	           use nodes with 256 GB RAM (250 GB available)
============       ====================================================================================
