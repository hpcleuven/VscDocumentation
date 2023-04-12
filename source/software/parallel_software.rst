.. _parallel software:

How do I run applications in parallel?
======================================

That depends.

.. _parallelism:

What is parallelism anyway?
---------------------------

Parallelism in the context of HPC can be defined at the level of

#. :ref:`instructions (vectorization) <vectorization>`,
#. :ref:`threads (shared memory) <multithreading>`,
#. :ref:`processes (distributed memory) <distributed programs>`,
#. hybrid (shared + distributed memory).

:ref:`Instruction-level parallelism <vectorization>` is essentially SIMD
(Single Instruction, Multiple Data) at the level of a single core in a
CPU.  It uses floating point or integer vector registers in the core in
order to perform the same operations on multiple values in the same clock
cycle.  Another term for this is vectorization.

Thread-level parallelism in the context of scientific computing means that
the application runs multiple threads, typically each on its own dedicated CPU
core to exploit modern CPU architecture.  All threads run on the same compute
node, and can interact through shared memory.

Process-level parallelism implies that an application consists of multiple
processes, potentially running on many compute nodes, and communicating
over the network.

The term hybrid parallelism refers to the combination of thread-level and
process-level parallelism.  For instance, a process can run on each compute
node, and each of these processes consists of multiple threads sharing data
on that node.

.. note::

   For most parallel applications, thread-level or process-level parallelism is
   combined with instruction-level parallelism.


.. _vectorization:

How can I vectorize my code?
----------------------------

Your application will typically be parallelized at instruction level, since
this is mostly done automatically by the compiler that has been used to
build your application if the right compiler options are specified.

- For installed software, your friendly user support person will typically have
  taken care of that.
- If you build your own software, some relevant information can be found below.

CPU instruction sets support vector operations, i.e., floating point
operations such as additions and multiplications can be performed on multiple
floating point numbers simultaneously.  The various CPU architectures have
added extensions to the original instruction sets.

+-------------------------+------------------------+
| CPU type                | vector instruction set |
+=========================+========================+
| Ivy Bridge/Sandy Bridge | AVX                    |
+-------------------------+------------------------+
| Haswell/Broadwell       | AVX2                   |
+-------------------------+------------------------+
| Skylake/Cascade Lake    | AVX-512                |
+-------------------------+------------------------+

Software that is specifically compiled to run on, e.g., Ivy Bridge will run
on a CPU of more recent generation such as a Skylake, but not with optimal
performance.  However, if software is built specifically to use, e.g.,
the AVX-512 instruction set, it will not run on older hardware such as
Haswell CPUs.

To build for a specific architecture both the Intel and GCC compiler family
offer command line options.  See the toolchain documentation for the
:ref:`Intel <Intel optimization>` and the :ref:`FOSS <GNU optimization>`
toolchains for an overview of the relevant compiler options.


.. _multithreading:

How can I run my application with multiple threads?
---------------------------------------------------

This is only possible when the application has been specifically designed
to do so.

- For installed software, check the manual.  It will be documented whether
  the application/library is multi-threaded, and how to use it.
- If you build your own software, there is some information below.

.. note::

   Typically, a multi-threaded application runs on a single compute node.  The
   threads communicate by exchanging information in memory, hence the term
   shared memory computing.

There are a few commonly used approaches to create a multi-threaded application:

`OpenMP`_
   This is by far the most popular approach for scientific software.  Many compilers
   (e.g., Intel and GCC) suites support it.  OpenMP defines directives that can be
   used in C, C++ and Fortran, as well as a runtime library.  Instructions are
   available for compiling and running OpenMP application with the
   :ref:`foss <GCC OpenMP>` and :ref:`Intel <Intel OpenMP>` toolchains.

`Threading Building Blocks`_ (TBB)
   Originally developed by Intel, this open source library offers many primitives for
   shared memory and data driven programming in C++.

`POSIX threads`_ (pthreads)
   Although it is possible to use a low-level threading library such as pthreads,
   this is typically not they way to go for scientific programming.


.. _distributed programs:

Can I run my application on multiple compute nodes?
---------------------------------------------------

This is only possible when the application has been specifically designed to do
so, or when your use case matches some common pattern.

- For installed software, check the manual.  It will be documented whether
  the application/library can be run distributed, and how to do that.
- If you run an application many times for different parameter settings, or
  on different data sets, check out the `worker framework documentation`_
  or the `atools documentation`_. for a comparison, see :ref:`worker or
  atools? <worker or atools>`
- If you build your own software, there is some information below.

For scientific software, the go-to library for distributed programming is an
implementation of MPI (Message Passing Interface).  This is a de-facto standard
implemented by many libraries and the API can be used from C/C++ and Fortran.

On the clusters, at least two implementations are available,
:ref:`Intel MPI <Communication library: Intel MPI>` in the Intel toolchain, and
:ref:`Open MPI <Communication library: Open MPI>` in the FOSS toolchain.


