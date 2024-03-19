.. _Breniac hardware UAntwerp:

################
Breniac hardware
################

The Breniac compute nodes should be used for:

* Jobs that need more than 128 GB of memory to run properly and that do not need
  more than 28 cores per node.
* Batches of single core jobs (that cannot be run on your own computer).
* Jobs that do not fit in a maximum wall time of 3 days and cannot be restarted
  cheaply.

For bigger parallel jobs, consider using the :ref:`Leibniz<Leibniz hardware>` and 
:ref:`Vaughan<Vaughan hardware>` nodes.

*************
Compute nodes
*************

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to.
When the option is omitted, your job is submitted to the only partition (**skylake**).

The maximum execution wall time for jobs is **7 days** (168 hours). Note however that
this feature should not be abused as there is only very little software that really
needs this.

===============  ======  ===================================================================================  ======  ==========  =======
Slurm partition  nodes   processors per node                                                                  memory  local disk  network
===============  ======  ===================================================================================  ======  ==========  =======
**skylake**      23      2x 14-core Intel Xeon `Gold 6132 <https://ark.intel.com/products/123541>`_ \@2.6GHz  192 GB  500 GB      EDR-IB
===============  ======  ===================================================================================  ======  ==========  =======

.. _Breniac login UAntwerp:

********************
Login infrastructure
********************

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

- 2 login nodes

  - 2 Xeon `Gold 6132 <https://ark.intel.com/products/123541>`_ CPUs\@2.6GHz (Skylake), 14 cores each
  - 192 GB RAM
  - 2x 500 GB HDD local disk (raid 1)

*********************
Compiling for Breniac
*********************

To compile code for Breniac, all ``intel``, 
``foss`` and ``GCC`` modules can be used (the 
latter being equivalent to ``foss`` but without MPI and the math libraries).

.. note::
  Do not forget to load one of the ``intel``, ``foss`` or ``GCC`` toolchain modules
  before compiling software!

Optimization options for the Intel compilers
============================================

.. seealso::
  For more information, please see the shared 
  :ref:`Intel toolchain<Intel toolchain>` documentation.

To optimize for Breniac, compile on the Breniac login 
or compute nodes. Use either ``-xHost`` or Skylake architecture specific options.
Combine this with either optimization 
level ``-O2`` or ``-O3``. For some codes, the additional optimizations at
level ``-O3`` actually produce slower code (often the case if the code
contains many short loops).

|Warning| If you forget these options, the default for the Intel compilers
is to generate code using optimization level ``-O2`` for architecture ``-march=pentium4``.
While ``-O2`` gives pretty good results, compiling for the Pentium 4 architecture uses 
none of the new instructions nor the vector instructions introduced since 2005.

Optimization options for the GNU compilers
==========================================

.. seealso::
  For more information, please see the shared 
  :ref:`FOSS toolchain<FOSS toolchain>` documentation.

To optimize for Breniac, compile on the Breniac login 
or compute nodes.
Use the ``-march=native`` or ``-march=skylake`` architecture options.
Combine this with either optimization 
level ``-O2`` or ``-O3``. In most cases, and especially for
floating point intensive code, ``-O3`` will be the preferred optimization level
with the GNU compilers as it only activates vectorization at this level
whereas the Intel compilers already offer vectorization at level ``-O2``.

|Warning| If you forget to specify these options, the default for the GNU compilers is
to generate unoptimized (level ``-O0``) code for a very generic CPU 
(``-march=x86-64``), which doesn't exploit the performance potential of
the Breniac CPUs at all.

*******
History
*******

Deployment
==========

In 2023, the KU Leuven Tier-1 Breniac cluster was decommissioned. During the summer of 2023, 
24 of the Breniac compute nodes were recovered for use at UAntwerp, replacing the Hopper compute cluster.    


Origin of the name
==================

Breniac is named after the decommissioned Tier-1 Breniac cluster.
