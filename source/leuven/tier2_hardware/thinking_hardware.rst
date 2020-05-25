Thinking7 hardware
==================

Thinking is KU Leuven/UHasselt's older Tier-2 cluster. It has thin nodes,
as well as GPGPU nodes.


Login infrastructure
--------------------

You can access Thinking by using 

- ``login-thinking.hpc.kuleuven.be``

This will loadbalance your connection to one of the 4 Thinking login nodes
 
Direct login is using SSH is possible to all login infrastructure without restrictions.

- Two ivybridge login nodes for SSH access are available.

  .. note::

     These are ivybridge nodes, so for better performance, build your software on
     a haswell compute node.

  - ``login5-tier2.hpc.kuleuven.be``
  - ``login6-tier2.hpc.kuleuven.be``
     
- One haswell login node for SSH access and one for
  :ref:`TurboVNC<TurboVNC start guide>` access.	

  - ``login7-tier2.hpc.kuleuven.be``
  - ``login8-tier2.hpc.kuleuven.be``


Hardware details
----------------

- 144 haswell nodes

  - 2 Xeon E5\-2680 v3 CPUs\@2.5 GHz, 12 cores each
  - 64 GB RAM (48 nodes) / 128 GB RAM (96 nodes) (:ref:`memory bandwidth and latency measurements <memory bandwidth and latency haswell tier2>`)
  - feature ``haswell``

- 5 GPGPU nodes

  - 2 Xeon E5-2650 v3 CPUs\@2.3 GHz, 10 cores each
  - 64 GB RAM
  - 2 NVIDIA K40c\@750 MHz, 12 GB GDDR
  - partition ``gpu``
  - feature ``K40c``

In the older partition of the cluster, nodes are connected via a QDR infiniband interconnect, while the newer partition has a faster FDR interconnect.  See the diagram below.

A :ref:`quick start guide <Thinking7 quick start guide>` is available to get you
started on submitting jobs to the updated ThinKing cluster.

|Thinking CentOS 7 hardware|

.. |Thinking CentOS 7 hardware| image:: thinking_hardware/thinking_centos7.png
  :width: 800
  :alt: Thinking CentOS 7 hardware diagram

