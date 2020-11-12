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

Jobs can have a maximal execution wall time of 3 days (72 hours), except on the
"hopper" compute nodes of Leibniz were it is possible to submit 7 days jobs on
request (motivation needed). 

Please also consider using the newer cluster Vaughan for big parallel jobs
that can use 64 cores or multiples thereof as soon as that cluster becomes 
available.

The login nodes and regular compute nodes are freely available. Contact 
UAntwerp user support (hpc@uantwerpen.be) for access to the visualization node
and accelerator nodes (free of charge but controlled access).

Hardware details
----------------

- 152 regular compute nodes

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 128 GB RAM (144 nodes) or 256 GB RAM (8 nodes)
    - 120 GB SSD local disk

- 24 "hopper" compute nodes (recovered from the former Hopper cluster)

    - 2 Xeon `E5-2680v2 <https://ark.intel.com/products/75277>`_ CPUs\@2.8 GHz (Ivy Bridge), 10 cores each
    - 64 GB RAM (144 nodes) or 256 GB RAM (24 nodes)
    - 500 GB local disk
    - :ref:`Instructions for the hopper compute nodes <UAntwerp hopper nodes>`

- 2 GPGPU nodes

   - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
   - 128 GB RAM
   - 2 NVIDIA P100, 16 GB HBM2
   - 120 GB SSD local disk
   - :ref:`Instructions for the GPGPU nodes <GPU computing UAntwerp>`
   
- 1 vector computing node (NEC SX-Aurora TSUBASA model A300-2)

   - 1 Xeon `Gold 6126 <https://ark.intel.com/products/120483>`_ CPU\@2.60 GHz (Skylake) with 12 cores
   - 96 GB RAM
   - 2 `NEC SX-Aurora Vector Engines type 10B <https://www.nec.com/en/global/solutions/hpc/sx/vector_engine.html>`_ 
     (per card 8 cores \@1.4 GHz, 48 GB HBM2)
   - 240 GB SSD local disk
   - :ref:`Instructions for the NEC SX-Aurora node <UAntwerp NEC SX Aurora>`

- 2 login nodes

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 256 GB RAM
    - 120 GB SSD local disk

- 1 visualization node

    - 2 Xeon `E5-2680v4 <https://ark.intel.com/products/75277>`_ CPUs\@2.4 GHz (Broadwell), 14 cores each
    - 256 GB RAM
    - 1 NVIDIA Quadro P5000
    - 120 GB SSD local disk
    - :ref:`Instructions for the visualization node <remote visualization UAntwerp>`

The nodes are connected using an InfiniBand EDR network except for the "hopper" compute nodes that utilize
FDR10 InfiniBand. 
More info on the storage system is available on the :ref:`UAntwerpen storage` page.


Login infrastructure
--------------------

Direct login is possible to both login nodes and to the visualization node.

- From outside the VSC network: use the external interface names. Outside of
  Belgium, a :ref:`VPN connection <VPN>` to the UAntwerp network is required.
- From inside the VSC network (e.g., another VSC cluster): use the internal
  interface names.

===================   =================================  ============================
..                    External interface                 Internal interface
===================   =================================  ============================
Login generic         login\-leibniz.hpc.uantwerpen.be   ..
Login\                login1\-leibniz.hpc.uantwerpen.be  ln1.leibniz.antwerpen.vsc
                                                         login1.leibniz.antwerpen.vsc
..                    login2\-leibniz.hpc.uantwerpen.be  ln2.leibniz.antwerpen.vsc
                                                         login2.leibniz.antwerpen.vsc
Visualisation node    viz1\-leibniz.hpc.uantwerpen.be    viz1.leibniz.antwerpen.vsc
===================   =================================  ============================


Characteristics of the compute nodes
------------------------------------

To remain compatible with the typical VSC setup, a number of properties 
can be used in job scripts. However, only one is really useful in the current
setup of leibniz to select the proper node type, ``mem256``.

============       ====================================================================================
property           explanation
============       ====================================================================================
broadwell          only use Intel processors from the Broadwell family (E5-XXXXv4) 
                   (Not needed at the moment as this is CPU type is selected automatically)
ivybridge          only use Intel processors from the Ivy Bridge family (E5-XXXXv2)
                   Not needed at the moment as there is no automatic selection of the queue for the
                   IVy Bridge nodes. Specify ``-q hopper`` instead.
gpu                only use the GPGPU nodes of Leibniz.
                   Not needed at the moment as there is no automatic selection of the queue for the
                   GPGPU nodes at the moment. Specify ``-q gpu`` instead.
ib                 use InfiniBand interconnect 
                   (Not needed at the moment as all nodes are connected to the InfiniBand interconnect)
mem128             use nodes with 128 GB RAM (roughly 112 GB available). 
                   This is the majority of the nodes on Leibniz.
                   Requesting this as a feature ensures that you get a node with 128 GB of memory and
                   keep the nodes with more memory available for other users who really need that
                   feature.
mem256             use nodes with 256 GB RAM (roughly 240 GB available). 
                   This property is useful if you submit a batch of jobs that require more than 4 GB of 
                   RAM per processor but do not use all cores and you do not want to use a tool to 
                   bundle jobs yourself such as Worker, as it helps the scheduler to put those jobs on 
                   nodes that can be further filled with your jobs.
============       ====================================================================================


Compiling for Leibniz
---------------------

To compile code for Leibniz, all ``intel``, 
``foss`` and ``GCC`` modules can be used (the 
latter equivalent to ``foss`` but without MPI and the math libraries).


Optimization options for the Intel compilers
""""""""""""""""""""""""""""""""""""""""""""

To optimize specifically for Leibniz, compile on one of the Leibniz login 
or compute nodes and combine the option ``-xHost`` with either optimization 
level ``-O2`` or ``-O3``. For some codes, the additional optimizations at
level ``-O3`` actually produce slower code (often the case if the code
contains many short loops).

Note that if you forget these options, the default for the Intel compilers
is to generate code at optimization level ``-O2`` (which is pretty good) but
for the Pentium 4 (``-march=pentium4``) which uses none of the new instructions
and hence also none of the vector instructions introduced since 2005,
which is pretty bad. Hence always specify ``-xHost`` (or any of the equivalent
architecture options specifically for Broadwell for specialists) when
compiling code.


Optimization options for the GNU compilers
""""""""""""""""""""""""""""""""""""""""""

Never use the default GNU compilers installed
on the system, but always load one of the ``foss`` or ``GCC`` modules.

To optimize for Leibniz, compile on one of the Leibniz login 
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

