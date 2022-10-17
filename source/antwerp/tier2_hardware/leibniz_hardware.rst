.. _Leibniz hardware:

Leibniz hardware
================

The Leibniz cluster was installed in the spring of 2017. It is a NEC system consisting of
152 compute nodes with dual 14-core Intel `E5-2680v4 <https://ark.intel.com/products/75277>`_ 
Broadwell generation CPUs connected through a EDR InfiniBand network. 144 of
these nodes have 128 GB RAM, the other
8 have 256 GB RAM. The nodes do not have a sizeable local disk.

Leibniz also
contains a node for visualisation and 3 node types for experimenting with accelerators:
2 nodes for GPU computing with two NVIDIA Pascal P100 GPU compute cards,
1 node with dual NEC SX-Aurora TSUBASA vector processors
and 1 node with an Intel Xeon Phi expansion board.

Access restrictions
-------------------

Access is available for faculty, students (master's projects under faculty
supervision), and researchers of the AUHA. The cluster is integrated in the VSC
network and runs the standard VSC software setup. It is also available to all
VSC users, though we appreciate that you contact the UAntwerp support team so
that we know why you want to use the cluster.

Jobs can have a maximal execution wall time of 3 days (72 hours).
On the accelerator nodes, a shorter wall time of 1 day applies.
For big parallel jobs, consider using the newer cluster :ref:`Vaughan<Vaughan hardware>`,
which has nodes with 64 cores.


Hardware details
----------------

- 152 regular compute nodes

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 128 GB RAM (144 nodes) or 256 GB RAM (8 nodes)
    - 120 GB SSD local disk

- 2 NVIDIA GPU nodes

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 2 NVIDIA Pascal P100, 16 GB HBM2
    - 128 GB RAM
    - 120 GB SSD local disk
    - :ref:`Instructions for using the GPU nodes <GPU computing UAntwerp>`
   
- 1 vector computing node (NEC SX-Aurora TSUBASA model A300-2)

    - 1 Xeon `Gold 6126 <https://ark.intel.com/products/120483>`_ CPU\@2.60 GHz (Skylake) with 12 cores
    - 2 `NEC SX-Aurora Vector Engines type 10B <https://www.nec.com/en/global/solutions/hpc/sx/vector_engine.html>`_ 
      (per card 8 cores \@1.4 GHz, 48 GB HBM2)
    - 96 GB RAM
    - 240 GB SSD local disk
    - :ref:`Instructions for using the NEC SX-Aurora node <UAntwerp NEC SX Aurora>`

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

All nodes are connected using an InfiniBand EDR network. The regular compute nodes
are logically organised in 5 islands with 24 nodes, 1 island with 22 nodes and 1 island
with 10 nodes (including the 8 nodes with 256 GB RAM).
Storage is provided through the central :ref:`UAntwerp storage` system.


Login infrastructure
--------------------

Direct login is possible to both login nodes and to the visualization node.

- From outside the VSC network: use the external interface names. Note that from outside of
  Belgium, a :ref:`VPN connection <VPN>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface names.

=========================   =================================  ============================
Node                        External interface                 Internal interface
=========================   =================================  ============================
Login node (generic name)   login\-leibniz.hpc.uantwerpen.be   login.leibniz.antwerpen.vsc
Login node (per node)       login1\-leibniz.hpc.uantwerpen.be  login1.leibniz.antwerpen.vsc
..                          login2\-leibniz.hpc.uantwerpen.be  login2.leibniz.antwerpen.vsc
Visualisation node          viz1\-leibniz.hpc.uantwerpen.be    viz1.leibniz.antwerpen.vsc
=========================   =================================  ============================


Available resources
-------------------

Characteristics of the compute nodes
""""""""""""""""""""""""""""""""""""

**Leibniz is running the Slurm Workload Manager as its resource manager and scheduler.**
We do not support the PBS compatibility layer but encourage users to develop
proper Slurm job scripts as one can then fully exploit the Slurm features and
enjoy the power of the ``srun`` command when starting processes.

Make sure to read the following pages which give a lot of information on Slurm
and how to convert your Torque scripts:

* :ref:`Local Slurm documentation <Antwerp Slurm>`
* :ref:`Important differences between Slurm and Torque<Antwerp Slurm_PBS_differences>`
* :ref:`Converting PBS/Torque options to Slurm <Antwerp Slurm_convert_from_PBS>`

To remain compatible with the typical VSC setup, a number of features 
can be used in job scripts (e.g. with Slurm's ``--constraint`` option).
However, only the following features are really useful in the current
setup of Leibniz to select regular compute nodes based on the amount
of available memory.

=======   ====================================================================================
Feature   Explanation
=======   ====================================================================================
mem128    Use nodes with 128 GB RAM (roughly 112 GB available). 
          This is the majority of the regular compute nodes on Leibniz.
          Requesting this as a feature ensures that you only get nodes with 128 GB of memory
          and keep the nodes with more memory available for other users who really need that
          feature.
mem256    Use nodes with 256 GB RAM (roughly 240 GB available). 
          This property is useful if you submit a batch of jobs that require more than 4 GB of 
          memory per processor but do not use all cores and you do not want to use a tool
          such as Worker to bundle jobs yourself, as it helps the scheduler to put those jobs 
          on nodes that can be further filled with your jobs.
=======   ====================================================================================

Available partitions
""""""""""""""""""""

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to.
When the option is omitted, your job is submitted to the default partition (*broadwell*).

The following partitions are available:

===========   =========================================================
Partition     Limits
===========   =========================================================
*broadwell*   Default. Maximum wall time of 3 days.
pascal_gpu    Submit to the Pascal GPU nodes.
===========   =========================================================


Compiling for Leibniz
---------------------

To compile code for Leibniz, all ``intel``, 
``foss`` and ``GCC`` modules can be used (the 
latter being equivalent to ``foss`` but without MPI and the math libraries).


Optimization options for the Intel compilers
""""""""""""""""""""""""""""""""""""""""""""

To optimize specifically for Leibniz, compile on the Leibniz login 
or compute nodes and combine the option ``-xHost`` with either optimization 
level ``-O2`` or ``-O3``. For some codes, the additional optimizations at
level ``-O3`` actually produce slower code (often the case if the code
contains many short loops).

Note that if you forget these options, the default for the Intel compilers
is to generate code using optimization level ``-O2`` (which is pretty good) but
for the Pentium 4 (``-march=pentium4``) which uses none of the new instructions
and hence also none of the vector instructions introduced since 2005,
which is pretty bad. Hence always specify ``-xHost`` (or any of the equivalent
architecture options specifically for Broadwell for specialists) when
compiling code.


Optimization options for the GNU compilers
""""""""""""""""""""""""""""""""""""""""""

Never use the default GNU compilers installed
on the system, but always load one of the ``foss`` or ``GCC`` modules.

To optimize for Leibniz, compile on the Leibniz login 
or compute nodes and combine either the option ``-march=native``
or ``-march=broadwell`` with either optimization 
level ``-O2`` or ``-O3``. In most cases, and especially for
floating point intensive code, ``-O3`` will be the preferred optimization level
with the GNU compilers as it only activates vectorization at this level
whereas the Intel compilers already offer vectorization at level ``-O2``.

Note that if you forget these options, the default for the GNU compilers is
to generate unoptimized (level ``-O0``) code for a very generic CPU 
(``-march=x86-64``) which doesn't exploit the performance potential of
the Leibniz CPUs at all. Hence one should always specify an appropriate
architecture (the ``-march`` flag) and appropriate optimization level
(the ``-O`` flag) as explained in the previous paragraph.


Further documentation:
""""""""""""""""""""""
* :ref:`Intel toolchains <Intel toolchain>`
* :ref:`FOSS toolchains (contains GCC) <FOSS toolchain>`


Origin of the name
------------------

Leibniz is named after `Gottfried Wilhelm Leibniz <https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz>`_,
a German multi-disciplinary scientist living in the late 17th and early 18th century. 
Leibniz may be best known as a developer of differential and integral calculus,
independently of the work of Isaac Newton.  But his contributions to science do not stop 
there. Leibniz also refined the binary number system, the foundation of nearly all modern
computers. He also designed mechanical calculators on which one could do the four basic
operations (add, subtract, multiply and divide). In all, Leibniz made contributions to
philosophy, mathematics, physics and technology, and several other fields.

