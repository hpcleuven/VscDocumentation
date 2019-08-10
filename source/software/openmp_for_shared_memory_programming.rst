OpenMP for shared memory programming
====================================

Purpose
-------

OpenMP (Open Multi-Processing) is an API that supports multi-platform
shared memory multiprocessing programming in C, C++, and Fortran, on
most processor architectures and operating systems. It consists of a set
of compiler directives, library routines, and environment variables that
influence run-time behavior.

OpenMP uses a portable, scalable model that gives programmers a simple
and flexible interface for developing parallel applications for
platforms ranging from the standard desktop computer to the
supercomputer. The current version of the OpenMP specification is 4.0.
It was released in July 2013 and is probably the biggest update of the
specification so far. However, not all compilers already fully support
this standard. The previous specification were the OpenMP 3.1
specification (July 2011) and OpenMP 3.0 specification (May 2008).
Versions prior to 4.0 concentrated on exploiting thread-level
parallelism on multicore machines in a portable way, while version 4.0
of the specifications adds support for vectorisation for the SIMD
instruction sets on modern CPUs and offload of computations to
accelerators (GPU, Xeon Phi, ...). The latter feature is an alternative
to the use of OpenACC directives.

Prerequisites
-------------

You should have a program that uses the OpenMP API.

Implementations
---------------

On the VSC clusters, the following compilers support OpenMP:

#.  :ref:`Intel compilers <Intel OpenMP>` in the intel toolchain

   #. The Intel compiler version 13.1 (intel/2014a and intel/2014b
      toolchains) implement the OpenMP 3.1 specification
   #. The Intel compiler version 14.0 (installed on some systems outside
      the toolchains, sometimes in a package with icc/2013_sp1 in its
      name) implements the OpenMP 3.1 specification and some elements of
      the OpenMP 4.0 specification (which was only just approved when
      the compiler was released)
   #. The Intel compiler version 15.0 (intel/2015a and intel/2015b
      toolchain) supports all of the OpenMP 4.0 specification except
      user-defined reductions. It supports offload to a Xeon Phi system
      (and to some Intel processor-integrated graphics, but that is not
      relevant on the VSC-clusters).
   #. The Intel compiler version 16.0 (intel/2016a and intel/2016b
      toolchains) offers almost complete OpenMP 4.0 support.
      User-defined reductions are now also supported.

#. :ref:`GCC OpenMP` in the foss toolchain

   #. GCC versions 4.8.2 (foss/2014a toolchain) and 4.8.3 (foss/2014b
      toolchain) support the OpenMP 3.1 specification.
   #. GCC version 4.9.2 (foss/2015a toolchain) and 4.9.3 (foss/2015b and
      foss/2016a toolchains) support the full OpenMP 4.0 specification.
      However, \\"offloaded\" code is run on the CPU and not on the GPU
      or any other accelerator. (In fact, OpenMP 4.0 is supported for
      C/C++ starting in GCC 4.9.0 and for Fortran in GC 4.9.1).
   #. GCC 5.4 (foss/2016b toolchain) offers full OpenMP 4.0 support and
      has the basics built in to support offloading.
   #. GCC 6.x (not yet part of a toolchain) offers full OpenMP 4.5
      support in C and C++, including offloading to some variants of the
      Xeon Phi and to AMD HSAIL and some support for OpenACC on NVIDIA.

When developing your own software, this is the preferred order to select
the toolchain. The GCC OpenMP runtime is for most applications inferior
to the Intel implementation.

We also assume you are already familiar with the job submission
procedure. If not, check the :ref:`Running jobs` section first.

Compiling OpenMP code
---------------------

See the instructions on the page about
:ref:`toolchains <Toolchains>` for
compiling OpenMP code with the Intel and GNU compilers.

Note that it is in fact possible to link OpenMP object code compiled
with gcc and the Intel compiler on the condition that the Intel OpenMP
libraries and run-time is used (e.g., by linking using icc with the
-openmp option), but the Intel manual is not clear which versions of gcc
and icc work together well. This is only for specialists but may be
useful if you only have access to object files and not to the full
source code.

Running OpenMP programs
-----------------------

Since OpenMP is intended for use in a shared memory context, when
submitting a job to the queue system, remember to request a single node
(i.e., ``-l nodes=1``) and as many processors as you need parallel
threads (e.g., ``-l ppn=4``). The latter should not exceed the number of
cores on the machine the job runs on. For relevant hardware information,
please consult the list of available :ref:`hardware <hardware>`.

You may have to set the number of cores that the program should use by
hand, e.g., when you don't use all cores on a node, because the
mechanisms in the OpenMP runtime that recognize the number of cores,
don't recognize the number of cores assigned to the job but the total
number of cores. Depending on the program, this may be trough a command
line option to the executable, a value in the input file or the
environment variable ``OMP_NUM_THREADS``. Failing to set this value may
result in threads competing with each other for resources such as cache
and access to the CPU and thus lower performance.

Further information
-------------------

-  `OpenMP`_ contains the
   specifications and some documentation. It is the web site of the
   OpenMP Architecture Review Board where the standard is discussed.
-  See also the pages in the :ref:`tutorials section <books>` and :ref:`online
   tutorials <web tutorials>`. 

The tutorial at the site of Lawrence Livermore National Laboratory `LLNL openMP tutorial`_ (LLNL) is highly recommended.

.. include:: links.rst
