.. role:: raw-html(raw)
    :format: html

.. _Vaughan hardware:

################
Vaughan hardware
################

************
Intended use
************

Jobs can have a maximal execution wall time of 3 days (72 hours).
Vaughan should only be used if you have large enough parallel jobs to or can
otherwise sufficiently fill up all cores of a compute node. Other jobs should
be use :ref:`Leibniz<Leibniz hardware>`
or the :ref:`Breniac<Breniac hardware UAntwerp>` nodes.

****************
Hardware details
****************

CPU compute nodes
=================

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to. This indicates the type of your job and
imposes some restrictions, but may let your job start sooner.
When the option is omitted, your job is submitted to the default partition (**zen2**).

The maximum execution wall time for jobs is **3 days** (72 hours).

===============  ======  ==========================================================================================  ======  ==========  =========
Slurm partition  nodes   processors per node                                                                         memory  local disk  network
===============  ======  ==========================================================================================  ======  ==========  =========
**zen2**         152     2x 32-core AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_ \@2.35 GHz  256 GB  240 GB SSD  HDR100-IB
zen3             24      2x 32-core AMD `Epyc 7543 <https://www.amd.com/en/products/cpu/amd-epyc-7543>`_ \@2.80 GHz  256 GB  500 GB SSD  HDR100-IB
zen3_512         16      2x 32-core AMD `Epyc 7543 <https://www.amd.com/en/products/cpu/amd-epyc-7543>`_ \@2.80 GHz  512 GB  500 GB SSD  HDR100-IB
===============  ======  ==========================================================================================  ======  ==========  =========

To remain compatible with the typical VSC setup, a number of features 
can be used in job scripts (e.g. with Slurm's ``--constraint`` option).
However, only the following features are really useful in the current
setup of Vaughan to select regular compute nodes based on the amount
of available memory.

=======  ====================================================================================
Feature  Explanation
=======  ====================================================================================
mem256   Use nodes with 256 GB RAM (roughly 240 GB available). 
         This is the majority of the regular compute nodes on Vaughan.
         Requesting this as a feature ensures that you only get nodes with 128 GB of memory
         and keep the nodes with more memory available for other users who really need that
         feature.
mem512   Use nodes with 512 GB RAM (roughly 500 GB available). 
         This property is useful if you submit a batch of jobs that require more than 4 GB of 
         memory per processor but do not use all cores and you do not want to use a tool
         such as Worker to bundle jobs yourself, as it helps the scheduler to put those jobs 
         on nodes that can be further filled with your jobs.
=======  ====================================================================================

.. comment
    All nodes are connected using an InfiniBand HDR100 network. The Rome compute nodes are logically
    organised in 4 islands (i.e., nodes connected to a single switch) with respectively 32, 36 and twice 44 nodes each.
    The 40 Milan compute nodes form an additional island.
    Storage is provided through the central :ref:`UAntwerp storage` system.

GPU compute nodes
=================

The maximum execution wall time for GPU jobs is 1 day (24 hours).

===============  ======  =======================  ==========  ==========================================================================================  ======  ==========  =========
Slurm partition  nodes   GPUs per node            GPU memory  processors per node                                                                         memory  local disk  network
===============  ======  =======================  ==========  ==========================================================================================  ======  ==========  =========
ampere_gpu       1       4x Nvidia A100 (Ampere)  40 GB SXM4  2x 32-core AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_ \@2.35 GHz  256 GB  480 GB SSD  HDR100-IB
arcturus_gpu     2       2x AMD MI100 (Arcturus)  32 GB HBM2  2x 32-core AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_ \@2.35 GHz  256 GB  480 GB SSD  HDR100-IB
===============  ======  =======================  ==========  ==========================================================================================  ======  ==========  =========

See :ref:`GPU computing UAntwerp` for more information on using the GPU nodes.

********************
Login infrastructure
********************

Direct login is possible to both login nodes.

- From outside the VSC network: use the external interface names. Note that from outside of
  Belgium, a :ref:`VPN connection <vpn>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface names.

============   =================================  ============================
Login node     External interface                 Internal interface
============   =================================  ============================
generic name   login\-vaughan.hpc.uantwerpen.be   login.vaughan.antwerpen.vsc
per node       login1\-vaughan.hpc.uantwerpen.be  login1.vaughan.antwerpen.vsc
..             login2\-vaughan.hpc.uantwerpen.be  login2.vaughan.antwerpen.vsc
============   =================================  ============================

.. comment
    ======  ==========================================================================================  ======  ======================  =========
    nodes   processors per node                                                                         memory  local disk              network
    ======  ==========================================================================================  ======  ======================  =========
    2       2x 16-core AMD `Epyc 7282 <https://www.amd.com/en/products/cpu/amd-epyc-7282>`_ \@2.8 GHz   256 GB  2x 480 GB SSD (raid 1)  HDR100-IB
    ======  ==========================================================================================  ======  ======================  =========

*********************
Compiling for Vaughan
*********************

To compile code for Vaughan, all ``intel``,
``foss`` and ``GCC`` modules can be used (the
latter being equivalent to ``foss`` but without MPI and the math libraries).

Optimization options for the Intel compilers
============================================

As the processors in Vaughan are made by AMD, there is no explicit support
in the Intel compilers. However, by choosing the appropriate compiler
options, the Intel compilers still produce very good code for Vaughan that
will often beat code produced by GCC (certainly for Fortran codes as gfortran
is a rather weak compiler).
To optimize specifically for Vaughan, compile on the Vaughan login
or compute nodes and combine the option ``-march=core-avx2`` with either optimization
level ``-O2`` or ``-O3``. For some codes, the additional optimizations at
level ``-O3`` actually produce slower code (often the case if the code
contains many short loops).

|Warning| If you forget these options, the default for the Intel compilers
is to generate code using optimization level ``-O2`` for architecture ``-march=pentium4``.
While ``-O2`` gives pretty good results, compiling for the Pentium 4 architecture uses 
none of the new instructions nor the vector instructions introduced since 2005.

The ``-x`` and ``-ax``-based options don't function properly on AMD processors.
These options add CPU detection to the code, and whenever detecting AMD
processors, binaries refuse to work or switch to code for the ancient
Pentium 4 architecture. In particular, ``-xCORE-AVX2`` is known to produce
non-working code.


Optimization options for the GNU compilers
==========================================

We suggest to use the newest GNU compilers available on Vaughan
(preferably version 9 or more recent) as the support for AMD processors
has improved a lot recently. Never use the default GNU compilers installed
on the system, but always load one of the ``foss`` or ``GCC`` modules.

To optimize for Vaughan, compile on the Vaughan login
or compute nodes and combine either the option ``-march=native``
or ``-march=znver2`` with either optimization
level ``-O2`` or ``-O3``. In most cases, and especially for
floating point intensive code, ``-O3`` will be the preferred optimization level
with the GNU compilers as it only activates vectorization at this level
(whereas the Intel compilers already offer vectorization at level ``-O2``).

.. comment
    If you really need to use GCC version prior to version 8, ``-march=znver2``
    is not yet available. On GCC 6 or 7, ``-march=znver1`` is probably the best
    choice. However, avoid using GCC versions that are even older.

|Warning| If you forget these options, the default for the GNU compilers is
to generate unoptimized (level ``-O0``) code for a very generic CPU
(``-march=x86-64``) which doesn't exploit the performance potential of
the Vaughan CPUs at all. Always specify an appropriate
architecture (the ``-march`` flag) and appropriate optimization level
(the ``-O`` flag) as explained in the previous paragraph.

Further documentation
=====================

* :ref:`Intel toolchains <Intel toolchain>`
* :ref:`FOSS toolchains (contains GCC) <FOSS toolchain>`

*******
History
*******

Deployment
==========

The Vaughan cluster was installed in the summer of 2020. It is a NEC system consisting of
152 compute nodes with dual 32-core AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_
Rome generation CPUs connected through an HDR100 InfiniBand network.
All nodes containing Rome CPUs have 256 GB RAM.
The nodes do not have a sizeable local disk.

Vaughan also contains 2 node types for GPU computing: 1 node with
four NVIDIA (Tesla) Ampere A100 GPU compute cards and 2 nodes equipped with
two AMD Instinct (Arcturus) MI100 GPU compute cards.

In the summer of 2023, the Vaughan cluster was extended. This extension
consists of 24 compute nodes with dual 32-core AMD `Epyc 7543 <https://www.amd.com/en/products/cpu/amd-epyc-7543>`_
Milan generation CPUs and 256 GB. An additional 16 nodes have 512 GB RAM.
All Milan nodes are connected through an HDR200 InfiniBand network.

Origin of the name
==================

Vaughan is named after `Dorothy Vaughan <https://en.wikipedia.org/wiki/Dorothy_Vaughan>`_,
an Afro-American mathematician who worked for NACA and NASA.
During her 28-year career, Vaughan prepared for the introduction of machine computers in
the early 1960s by teaching herself and her staff the programming language of Fortran.
She later headed the programming section of the Analysis and Computation Division (ACD)
at Langley.
