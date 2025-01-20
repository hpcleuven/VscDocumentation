.. _OpenMP shared memory programming:

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
supercomputer. The current version of the OpenMP specification is 5.1,
released in November 2020.

However, not all compilers already fully support this standard. The
previous specification were OpenMP 5.0 (November 2018), OpenMP 4.5 (November
2015) and OpenMP 4.0 (July 2013).


Prerequisites
-------------

You should have a program that uses the OpenMP API.


Implementations
---------------

On the VSC clusters, the following compilers support OpenMP:

:ref:`Intel compilers <Intel OpenMP>` in the :ref:`Intel toolchain`
   The Intel compiler version 18.0 (intel/2018a and intel/2018b
   toolchains) offers almost complete OpenMP 4.5 support.

:ref:`GCC compilers <GCC OpenMP>` in the :ref:`FOSS toolchain`
   GCC 6.x (foss/2018a) offers full OpenMP 4.5
   support in C and C++, including offloading to some variants of the
   Xeon Phi and to AMD HSAIL and some support for OpenACC on NVIDIA.  For
   Fortran, OpenMP 4.0 is supported.

For an overview of compiler (version) support for the various OpenMP
specifications, see the `OpenMP compilers and tools`_ page.

.. note::

   The GCC OpenMP runtime is for most applications inferior
   to the Intel implementation.


Compiling OpenMP code
---------------------

See the instructions on the page about toolchains for compiling OpenMP code
with the :ref:`Intel <Intel OpenMP>` and :ref:`GCC <GCC OpenMP>` compilers.

.. note::

   It is in fact possible to link OpenMP object code compiled
   with GCC and the Intel compiler on the condition that the Intel OpenMP
   libraries and run-time is used (e.g., by linking using ``icc`` with the
   ``-qopenmp`` option), but the Intel manual is not clear which versions
   of ``gcc`` and ``icc`` work together well. This is only for specialists
   but may be useful if you only have access to object files and not to the
   full source code.


Running OpenMP programs
-----------------------

We assume you are already familiar with the job submission
procedure. If not, check the :ref:`Running jobs` section first.

Since OpenMP is intended for use in a shared memory context, when
submitting a job to the queue system, remember to request a single node
and as many processors as you need parallel
threads (e.g., ``-l nodes=1:ppn=4``). The latter should not exceed the number of
cores on the machine the job runs on. For relevant hardware information,
please consult the list of available :ref:`hardware <hardware>`.

You may have to set the number of cores that the program should use by
hand, e.g., when you don't use all cores on a node, because the
OpenMP runtime recognizes the number of cores available on the node,
and not respect the number of cores assigned to the job.

Depending on the program, this may be through a command
line option to the executable, a value in the input file or the
environment variable ``OMP_NUM_THREADS``. 

.. warning::

   Failing to set this value may result in threads competing with each other
   for resources such as cache and access to the CPU and thus (much) lower
   performance.


Further information
-------------------

-  `OpenMP`_ contains the specifications and some documentation. It is the web
   site of the OpenMP Architecture Review Board where the standard is
   discussed.
-  See also the pages in the :ref:`tutorials section <books>` and :ref:`online
   tutorials <web tutorials>`. 

The tutorial at the site of Lawrence Livermore National Laboratory `LLNL OpenMP tutorial`_ (LLNL) is highly recommended.

