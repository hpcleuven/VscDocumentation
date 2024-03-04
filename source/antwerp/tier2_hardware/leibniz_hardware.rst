.. _Leibniz hardware:

################
Leibniz hardware
################

The Leibniz cluster is the default UAntwerp cluster.
Besides regular compute nodes, it contains 2 NVIDIA GPU compute nodes, and a :ref:`visualization node <remote visualization UAntwerp>`.

For larger jobs, consider using the newer :ref:`Vaughan<Vaughan hardware>`.
For smaller jobs, longer jobs or batches of single core jobs, 
consider using the :ref:`Breniac<Breniac hardware UAntwerp>` nodes.

*******************
Compute nodes
*******************

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to.
When the option is omitted, your job is submitted to the default partition (**broadwell**).

CPU compute nodes
=================

The maximum execution wall time for jobs is **3 days** (72 hours).

===============  ======  =============================================================================  ======  ==========  =======
Slurm partition  nodes   processors per node                                                            memory  local disk  network
===============  ======  =============================================================================  ======  ==========  =======
**broadwell**    144     2x 14-core Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ \@2.4 GHz  128 GB  120 GB SSD  EDR-IB
broadwell_256    8       2x 14-core Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ \@2.4 GHz  256 GB  120 GB SSD  EDR-IB
===============  ======  =============================================================================  ======  ==========  =======

GPU compute nodes
=================

The maximum execution wall time for jobs is **1 day** (24 hours).

===============  =====  =======================================================================================  ==========  =============================================================================  ======  ==========  =======
Slurm partition  nodes  GPUs per node                                                                            GPU memory  processors per node                                                            memory  local disk  network
===============  =====  =======================================================================================  ==========  =============================================================================  ======  ==========  =======
pascal_gpu       2      2x NVIDIA Tesla `P100 (Pascal) <https://www.nvidia.com/en-us/data-center/tesla-p100/>`_  16 GB HBM2  2x 14-core Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ \@2.4 GHz  128 GB  120 GB      EDR-IB
===============  =====  =======================================================================================  ==========  =============================================================================  ======  ==========  =======

.. seealso:: See :ref:`GPU computing UAntwerp` for more information on using the GPU nodes.

.. _Leibniz login:

********************
Login infrastructure
********************

Direct login is possible to both login nodes and to the visualization node.

- From outside the VSC network: use the external interface names. Note that from outside of
  Belgium, a :ref:`VPN connection <vpn>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface names.

=========================  =================================  ============================
Node                       External interface                 Internal interface
=========================  =================================  ============================
Login node (generic name)  login\-leibniz.hpc.uantwerpen.be   login.leibniz.antwerpen.vsc
Login node (per node)      login1\-leibniz.hpc.uantwerpen.be  login1.leibniz.antwerpen.vsc
..                         login2\-leibniz.hpc.uantwerpen.be  login2.leibniz.antwerpen.vsc
Visualisation node         viz1\-leibniz.hpc.uantwerpen.be    viz1.leibniz.antwerpen.vsc
=========================  =================================  ============================

- 2 login nodes

  - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
  - 256 GB RAM
  - 2x 1 TB HDD local disk (raid 1)

- 1 visualization node

  - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
  - 1 NVIDIA Quadro P5000
  - 256 GB RAM
  - 2x 1 TB HDD local disk (raid 1)
  - :ref:`Instructions for using the visualization node <remote visualization UAntwerp>`
    
*********************
Compiling for Leibniz
*********************

To compile code for Leibniz, all ``intel``, 
``foss`` and ``GCC`` modules can be used (the 
latter being equivalent to ``foss`` but without MPI and the math libraries).


Optimization options for the Intel compilers
============================================

To optimize for Leibniz, compile on the Leibniz login 
or compute nodes. Use either ``-xHost`` or Broadwell architecture specific options.
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

|Warning| Never use the default GNU compilers installed
on the system, but always load one of the ``foss`` or ``GCC`` modules.

To optimize for Leibniz, compile on the Leibniz login 
or compute nodes.
Use the ``-march=native`` or ``-march=broadwell`` architecture options.
Combine this with either optimization 
level ``-O2`` or ``-O3``. In most cases, and especially for
floating point intensive code, ``-O3`` will be the preferred optimization level
with the GNU compilers as it only activates vectorization at this level
whereas the Intel compilers already offer vectorization at level ``-O2``.

|Warning| If you forget to specify these options, the default for the GNU compilers is
to generate unoptimized (level ``-O0``) code for a very generic CPU 
(``-march=x86-64``), which doesn't exploit the performance potential of
the Leibniz CPUs at all. Always specify an appropriate
architecture (the ``-march`` flag) and appropriate optimization level
(the ``-O`` flag) as explained in the previous paragraph.


Further documentation
======================
* :ref:`Intel toolchains <Intel toolchain>`
* :ref:`FOSS toolchains (contains GCC) <FOSS toolchain>`

*******
History
*******

Deployment
==========

The Leibniz cluster was installed in the spring of 2017. It is a NEC system consisting of
152 compute nodes with dual 14-core Intel `E5-2680v4 <https://ark.intel.com/products/75277>`_ 
Broadwell generation CPUs connected through an EDR InfiniBand network. 144 of
these nodes have 128 GB RAM, the other
8 have 256 GB RAM. The nodes do not have a sizeable local disk.

Leibniz also
contains a node for visualisation and 
2 GPU nodes with two NVIDIA Tesla P100 GPU compute cards for experimenting with accelerators.

All nodes are connected using an InfiniBand EDR network. The regular compute nodes
are logically organised in 5 islands with 24 nodes, 1 island with 22 nodes and 1 island
with 10 nodes (including the 8 nodes with 256 GB RAM).
Storage is provided through the central :ref:`UAntwerp storage` system.

Origin of the name
==================

Leibniz is named after `Gottfried Wilhelm Leibniz <https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz>`_,
a German multi-disciplinary scientist living in the late 17th and early 18th century. 
Leibniz may be best known as a developer of differential and integral calculus,
independently of the work of Isaac Newton.  But his contributions to science do not stop 
there. Leibniz also refined the binary number system, the foundation of nearly all modern
computers. He also designed mechanical calculators on which one could do the four basic
operations (add, subtract, multiply and divide). In all, Leibniz made contributions to
philosophy, mathematics, physics and technology, and several other fields.
