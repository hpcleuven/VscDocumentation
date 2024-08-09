.. role:: raw-html(raw)
    :format: html

.. _Vaughan hardware:

Vaughan hardware
================

The Vaughan cluster was installed in the summer of 2020. It is a NEC system consisting of
152 compute nodes with dual 32-core AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_
Rome generation CPUs connected through a HDR100 InfiniBand network.
All nodes have 256 GB RAM.
The nodes do not have a sizeable local disk.

Vaughan also contains 2 node types for GPU computing: 1 node with
four NVIDIA (Tesla) Ampere A100 GPU compute cards and 2 nodes equipped with
two AMD Instinct (Arcturus) MI100 GPU compute cards.

Access restrictions
-------------------

Access is available for faculty, students (master's projects under faculty
supervision), and researchers of the AUHA. The cluster is integrated in the VSC
network and runs to a large extent the standard VSC software setup.
It is also available to all
VSC users, though we appreciate that you contact the UAntwerp support team so
that we know why you want to use the cluster.

Jobs can have a maximal execution wall time of 3 days (72 hours).
Vaughan should only be used if you have large enough parallel jobs to or can
otherwise sufficiently fill up all cores of a compute node. Other jobs should
be use :ref:`Leibniz<Leibniz hardware>`
or the older :ref:`Hopper<Hopper hardware>` nodes.

Hardware details
----------------

- 152 compute nodes

    - 2 AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_ CPUs\@2.35 GHz (Rome), 32 cores each
    - 256 GB RAM
    - 240 GB SSD local disk (for OS, should not be used as main scratch)

- 1 NVIDIA GPU node

    - 2 AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_ CPUs\@2.35 GHz (Rome), 32 cores each
    - 4 NVIDIA (Tesla) Ampere A100, 40 GB SXM4
    - 256 GB RAM
    - 480 GB SSD local disk
    - :ref:`Instructions for using the GPU nodes <GPU computing UAntwerp>`

- 2 AMD GPU nodes

    - 2 AMD `Epyc 7452 <https://www.amd.com/en/products/cpu/amd-epyc-7452>`_ CPUs\@2.35 GHz (Rome), 32 cores each
    - 4 AMD Instinct (Arcturus) MI100
    - 256 GB RAM
    - 480 GB SSD local disk
    - :ref:`Instructions for using the GPU nodes <GPU computing UAntwerp>`

- 2 login nodes

    - 2 AMD `Epyc 7282 <https://www.amd.com/en/products/cpu/amd-epyc-7282>`_ CPUs\@2.8 GHz (Rome), 16 cores each
    - 256 GB RAM
    - 2x 480 GB SSD local disk (raid 1)

All nodes are connected using an InfiniBand HDR100 network. The compute nodes are logically
organised in 4 islands (i.e., nodes connected to a single switch) with respectively 32, 36 and twice 44 nodes each.
Storage is provided through the central :ref:`UAntwerp storage` system.


Login infrastructure
--------------------

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


Available resources
-------------------

Characteristics of the compute nodes
""""""""""""""""""""""""""""""""""""

**Vaughan is running the Slurm Workload Manager as its resource manager and scheduler.**
We do not support the PBS compatibility layer but encourage users to develop
proper Slurm job scripts as one can then fully exploit the Slurm features and
enjoy the power of the ``srun`` command when starting processes.

Make sure to read the following pages which give a lot of information on Slurm
and how to convert your Torque scripts:

* :ref:`running jobs`
* :ref:`Important differences between Slurm and Torque<Slurm_PBS_differences>`
* :ref:`Converting PBS/Torque options to Slurm <Slurm_convert_from_PBS>`

Since Vaughan is a homogeneous system with respect to CPU type, memory and
interconnect, it is not needed to specify any features.

Available partitions
""""""""""""""""""""

When submitting a job with ``sbatch`` or using ``srun``, you can choose to specify
the partition your job is submitted to. This indicates the type of your job and
imposes some restrictions, but may let your job start sooner.
When the option is omitted, your job is submitted to the default partition (*zen2*).

The following partitions are available:

============   =========================================================
Partition      Limits
============   =========================================================
*zen2*         Default. Maximum wall time of 3 days.
debug          Maximum 2 nodes with a maximum wall time of 1 hour.
short          Maximum wall time of 6 hours, with priority boost.
ampere_gpu     Submit to the NVIDIA Ampere GPU node.
arcturus_gpu   Submit to the AMD Arcturus GPU nodes.
============   =========================================================

See :ref:`GPU computing UAntwerp` for more information on using the GPU nodes.

Compiling for Vaughan
---------------------

To compile code for Vaughan, all ``intel``,
``foss`` and ``GCC`` modules can be used (the
latter being equivalent to ``foss`` but without MPI and the math libraries).


Optimization options for the Intel compilers
""""""""""""""""""""""""""""""""""""""""""""

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

Note that if you forget these options, the default for the Intel compilers
is to generate code using optimization level ``-O2`` (which is pretty good) but
for the Pentium 4 (``-march=pentium4``) which uses none of the new instructions
and hence also none of the vector instructions introduced since 2005,
which is pretty bad. Hence always specify ``-march=core-avx2`` (or any of the equivalent
architecture options specifically for Broadwell) when compiling code.

The ``-x`` and ``-ax``-based options don't function properly on AMD processors.
These options add CPU detection to the code, and whenever detecting AMD
processors, binaries refuse to work or switch to code for the ancient
Pentium 4 architecture. In particular, ``-xCORE-AVX2`` is known to produce
non-working code.


Optimization options for the GNU compilers
""""""""""""""""""""""""""""""""""""""""""

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

If you really need to use GCC version prior to version 8, ``-march=znver2``
is not yet available. On GCC 6 or 7, ``-march=znver1`` is probably the best
choice. However, avoid using GCC versions that are even older.

Note that if you forget these options, the default for the GNU compilers is
to generate unoptimized (level ``-O0``) code for a very generic CPU
(``-march=x86-64``) which doesn't exploit the performance potential of
the Vaughan CPUs at all. Hence one should always specify an appropriate
architecture (the ``-march`` flag) and appropriate optimization level
(the ``-O`` flag) as explained in the previous paragraph.


Further documentation
"""""""""""""""""""""
* :ref:`Intel toolchains <Intel toolchain>`
* :ref:`FOSS toolchains (contains GCC) <FOSS toolchain>`



Origin of the name
------------------

Vaughan is named after `Dorothy Vaughan <https://en.wikipedia.org/wiki/Dorothy_Vaughan>`_,
an Afro-American mathematician who worked for NACA and NASA.
During her 28-year career, Vaughan prepared for the introduction of machine computers in
the early 1960s by teaching herself and her staff the programming language of Fortran.
She later headed the programming section of the Analysis and Computation Division (ACD)
at Langley.



