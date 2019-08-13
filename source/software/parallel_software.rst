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
core to exploit modren CPU architecture.  All threads run on the same compute
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
| Skylake                 | AVX-512                |
+-------------------------+------------------------+

Software that is specically compiled to run on, e.g., Ivy Bridge will run
on a CPU of more recent generation such as a Skylake, but not with optimal
performance.  However, if software is built specifically to use, e.g.,
the AVX-512 instruction set, it will not run on older hardware such as
Haswell CPUs.

To build for a specific architecture both the Intel and GCC compiler family
offer command line options.

+------------------+-----------------+-------------------------------+
| CPU architecture | Intel compilers | GCC compilers                 |
+==================+=================+===============================+
| Ivy Bridge       | ``-xAVX``       | ``-march=ivybridge``          |
+------------------+-----------------+-------------------------------+
| Sandy Bridge     | ``-xAVX``       | ``-march=sandybridge``        |
+------------------+-----------------+-------------------------------+
| Haswell          | ``-xAVX2``      | ``-march=haswell``            |
+------------------+-----------------+-------------------------------+
| Broadwell        | ``-xAVX2``      | ``-march=broadwell``          |
+------------------+-----------------+-------------------------------+
| Skylake          | ``-xAVX-512``   | ``-march=skylake-avx512``     |
+------------------+-----------------+-------------------------------+
| detect host CPU  | ``-xHost``      | ``-march=native``             |
+------------------+-----------------+-------------------------------+

For example, the application compiled with the command below will be
optimized to run on a Haswell CPU::

   $ gcc -O3  -march=haswell  -o floating_point  floating_point.c

When using the Intel compiler family, it is possible to build software
that contains multiple code paths specific for the architecture that the
application is running on.  Additional code paths can be specified using
the ``-ax`` option.

+-------------------------+------------------------+
| additional code path    | Intel compiler option  |
+=========================+========================+
| Ivy Bridge/Sandy Bridge | ``-axCORE-AVX``        |
+-------------------------+------------------------+
| Haswell/Broadwell       | ``-axCORE-AVX2``       |
+-------------------------+------------------------+
| Skylake                 | ``-axCORE-AVX512``     |
+-------------------------+------------------------+

For the Intel compilers, the target architecture can be specified using the
``-x`` option, while additional code paths can be specified using ``-ax``.

For instance, the following compilation would create an executable with
code paths for AVX, AVX2 and AVX-512 instruction sets::

   $ icpc -O3  -xAVX  -axCORE-AVX2,CORE-AVX512 floating_point.cpp

Software that has been built using these options will run with the
appropriate instruction set on Ivy Bridge, Sandy Bridge, Haswell, Broadwell
and Skylake CPUs.

.. note::

   GCC doesn't support applications with multiple code paths, so you have
   to build multiple versions optimized for specific architectures.
   Dispatching can be done at runtime by checking the value of the
   ``$VSC_ARCH_LOCAL`` environment variable.


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

This is only possible when the application has been specically designed to do
so, or when your use case matches some common pattern.

- For installed software, check the manual.  It will be documented whether
  the application/library is multi-threaded, and how to use it.
- If you run an application many times for different parameter settings,
  check out the `worker framework documentation`_ or the
  `atools documentation`_.
- If you build your own software, there is some information below.

.. include:: links.rst
