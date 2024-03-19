.. _Hopper hardware:

########################
UAntwerp Hopper hardware
########################

.. seealso:: See :ref:`UAntwerp hardware` for more information 
  on the current state of the UAntwerp infrastructure.

The Hopper compute nodes were used for:

* Jobs that used old software that could not be properly compiled to benefit from the
  extensions in the instruction sets of :ref:`Leibniz<Leibniz hardware>` and 
  :ref:`Vaughan<Vaughan hardware>`, or that lack enough parallelism 
  to fully exploit the :ref:`Leibniz<Leibniz hardware>` or 
  :ref:`Vaughan<Vaughan hardware>` compute nodes (even taking 
  into account that multiple jobs launched nearly simultaneously can still make
  it possible to use the full capacity of a :ref:`Leibniz<Leibniz hardware>` or 
  :ref:`Vaughan<Vaughan hardware>` compute node).
* Jobs that needed more than 128 GB of memory to run properly and that did not need
  more than 20 cores per node.
* Batches of single core jobs (that could not run on your own computer).
* Jobs that did not fit in a maximum wall time of 3 days and could not be restarted cheaply.

Jobs had a maximal execution wall time of 7 days (168 hours).

*********************
Compute nodes
*********************

When submitting a job with ``sbatch`` or using ``srun``, you could choose to specify
the partition your job was submitted to.
When the option was omitted, your job was submitted to the default partition (**ivybridge**).

The maximum execution wall time for jobs was **7 days** (168 hours).

===============  ======  ===================================================================================  ======  ==========  ========
Slurm partition  nodes   processors per node                                                                  memory  local disk  network
===============  ======  ===================================================================================  ======  ==========  ========
**ivybridge**    23      2x 10-core Intel Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ \@2.8 GHz  256 GB  500 GB      FDR10-IB
===============  ======  ===================================================================================  ======  ==========  ========

*********************
Login infrastructure
*********************

Direct login was possible to the login node.

- From outside the VSC network: use the external interface name. Note that from outside of
  Belgium, a :ref:`VPN connection <vpn>` to the UAntwerp network was required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface name.

============   =================================  ============================
Login node     External interface                 Internal interface
============   =================================  ============================
generic name   login\-hopper.hpc.uantwerpen.be    login.hopper.antwerpen.vsc
============   =================================  ============================

- 1 login node

  - 2x 10-core Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (Ivy Bridge)
  - 256 GB RAM
  - 500 GB local disk

*******
History
*******

Deployment
==========

Hopper was a compute cluster at UAntwerp in operation from late 2014 till the
summer of 2020. The cluster had 168 compute nodes with
dual 10-core Intel `E5-2680v2 <https://ark.intel.com/products/75277>`_
Ivy Bridge generation CPUs connected through an InfiniBand FDR10 network.
144 of those compute nodes had 64 GB RAM and 24 had 256 GB of RAM.

When the cluster was moved out in the summer of 2020 to make space for the
installation of :ref:`Vaughan<Vaughan hardware>`, the 24 nodes with 256 GB were recovered for further use.

These last 24 nodes were decommissioned in the summer of 2023. They were replaced
by the :ref:`Breniac<Breniac hardware UAntwerp>` cluster, re-using nodes previously belonging 
to the decommissioned :ref:`breniac hardware`.

Origin of the name
==================

Hopper was named after `Grace Hopper <https://en.wikipedia.org/wiki/Grace_Hopper>`_.
Grace Hopper was an American mathematician turned computer scientist and United States Navy
rear admiral. She worked as a programmer of some of the first computer systems and devised
the theory of machine independent programming languages. Her work laid at the base of the 
programming language COBOL. 


