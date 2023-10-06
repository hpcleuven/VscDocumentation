################
Thinking Cluster
################

.. note::

   Thinking was a KU Leuven/UHasselt's Tier-2 cluster, which was decomissioned
   in 2018. This page is only for any possible future reference.

Thinking had thin nodes, large memory nodes, as well as GPGPU nodes.
This cluster was running CentOS 6, but is was gradually being migraged to CentOS 7.

Thinking CentOS 6
=================

Login infrastructure
--------------------

Direct login using SSH was possible to all login infrastructure without restrictions.

- Two login nodes for SSH access are available.

  - login1.hpc.kuleuven.be
  - login2.hpc.kuleuven.be


Hardware details
----------------

- 176 ivybridge nodes

  - 2 Xeon E5-2680 v2 CPUs\@2.8 GHz, 10 cores each
  - 64 GB RAM
  - feature ``ivybridge``

- 32 ivybridge nodes

  - 2 Xeon E5-2680 v2 CPUs\@2.8 GHz, 10 cores each
  - 128 GB RAM
  - feature ``ivybridge``

- 48 haswell nodes

  - 2 Xeon E5-2680 v3 CPUs\@2.5 GHz, 12 cores each
  - 64 GB RAM
  - feature ``haswell``

- 86 haswell nodes

  - 2 Xeon E5-2680 v3 CPUs\@2.5 GHz, 12 cores each
  - 128 GB RAM
  - feature ``haswell``

- 5 GPGPU nodes

  - 2 Xeon E5-2650 v3 CPUs\@2.3 GHz, 10 cores each
  - 64 GB RAM
  - 2 NVIDIA K40c\@750 MHz, 12 GB GDDR
  - partition ``gpu``

In the older partition of the cluster, nodes are connected via a QDR infiniband
interconnect, while the newer partition has a faster FDR interconnect.  See the
diagram below.

.. figure:: thinking_hardware/thinking.png
  :alt: Thinking hardware diagram

Thinking CentOS 7
=================

Login infrastructure
--------------------

Direct login is using SSH is possible to all login infrastructure without restrictions.

- Two ivybridge login nodes for SSH access are available. **Note:** these are
  ivybridge nodes, so for better performance, build your software on a haswell
  compute node.

  - login5\-tier2.hpc.kuleuven.be
  - login6\-tier2.hpc.kuleuven.be
	
- One haswell login node for SSH access.	

  - login7\-tier2.hpc.kuleuven.be
  - login8\-tier2.hpc.kuleuven.be

Hardware details
----------------
- 10 ivybridge nodes

  - 2 Xeon E5-2680 v2 CPUs@2.8 GHz, 10 cores each
  - 64 GB RAM (4) / 128 GB RAM (6)
  - feature ``ivybridge``

- 10 haswell nodes

  - 2 Xeon E5\-2680 v3 CPUs\@2.5 GHz, 12 cores each
  - 128 GB RAM
  - feature ``haswell``

In the older partition of the cluster, nodes are connected via a QDR infiniband
interconnect, while the newer partition has a faster FDR interconnect.  See the
diagram below.

.. figure:: thinking_hardware/thinking_centos7.png
  :alt: Thinking CentOS 7 hardware diagram

