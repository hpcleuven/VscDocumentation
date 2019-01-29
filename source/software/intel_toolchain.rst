.. _Intel toolchain:

Intel toolchain
===============

The ``intel`` toolchain consists almost entirely of software components
developed by Intel. When building third-party software, or developing
your own, load the module for the toolchain:

::

   $ module load intel/<version>

where ``<version>`` should be replaced by the one to be used, e.g.,
``2016b``. See the documentation on the software module system for more
details.

Starting with the ``2014b`` toolchain, the GNU compilers are also
included in this toolchain as the Intel compilers use some of the
libraries and as it is possible (though some care is needed) to link
code generated with the Intel compilers with code compiled with the GNU
compilers.

Compilers: Intel and Gnu
------------------------

Three compilers are available:

-  C: ``icc``
-  C++: ``icpc``
-  Fortran: ``ifort``

Compatible versions of the GNU C (``gcc``), C++ (``g++``) and Fortran
(``gfortran``) compilers are also provided.

For example, to compile/link a Fortran program ``fluid.f90`` to an
executable ``fluid`` with architecture specific optimization, use:

::

   $ ifort -O2 -xhost -o fluid fluid.f90

For documentation on available compiler options, we refer to the :ref:`links
to the Intel documentation at the bottom of this page <Intel documentation>`.
Do not forget to *load the toolchain module* first!

.. _Intel OpenMP:

Intel OpenMP
~~~~~~~~~~~~

The compiler switch to use to compile/link OpenMP C/C++ or Fortran code
is ``-qopenmp`` in recent versions of the compiler (toolchain
intel/2015a and later) or ``-openmp`` in older versions. For example, to
compile/link a OpenMP C program ``scatter.c`` to an executable
``scatter`` with architecture specific optimization, use:

::

   $ icc -qopenmp -O2 -xhost -o scatter scatter.c

Remember to specify as many processes per node as the number of threads
the executable is supposed to run. This can be done using the ``ppn``
resource, e.g., ``-l nodes=1:ppn=10`` for an executable that should be
run with 10 OpenMP threads. The number of threads should not exceed the
number of cores on a compute node.

.. _Intel MPI:

Communication library: Intel MPI
--------------------------------

For the intel toolchain, ``impi``, i.e., Intel MPI is used as the
communications library. To compile/link MPI programs, wrappers are
supplied, so that the correct headers and libraries are used
automatically. These wrappers are:

-  C: ``mpiicc``
-  C++: ``mpiicpc``
-  Fortran: ``mpiifort``

Note that the *names differ* from those of other MPI implementations.
The compiler wrappers take the same options as the corresponding
compilers.

Using the Intel MPI compilers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, to compile/link a C program ``thermo.c`` to an executable
``thermodynamics`` with architecture specific optimization, use:

::

   $ mpiicc -O2 -xhost -o thermodynamics thermo.c

For further documentation, we refer to :ref:`the links to the Intel
documentation at the bottom of this page <Intel documentation>`. Do
not forget to *load the toolchain module* first.

Running an MPI program with Intel MPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that an MPI program must be run with the exact same version of the
toolchain as it was originally build with. The listing below shows a PBS
job script ``thermodynamics.pbs`` that runs the ``thermodynamics``
executable.

::

   #!/bin/bash -l
   module load intel/<version>
   cd $PBS_O_WORKDIR
   mpirun -np $PBS_NP ./thermodynamics

The resource manager passes the number of processes to the job script
through the environment variable ``$PBS_NP``, but if you use a recent
implementation of Intel MPI, you can even omit ``-np $PBS_NP`` as Intel
MPI recognizes the Torque resource manager and requests the number of
cores itself from the resource manager if the number is not specified.

Intel mathematical libraries
----------------------------

The Intel Math Kernel Library (MKL) is a comprehensive collection of
highly optimized libraries that form the core of many scientific HPC
codes. Among other functionality, it offers:

-  BLAS (Basic Linear Algebra Subprograms), and extensions to sparse
   matrices
-  LAPACK (Linear Algebra PACKage) and ScaLAPACK (the distributed memory
   version)
-  FFT-routines including routines compatible with the FFTW2 and FFTW3
   libraries (Fastest Fourier Transform in the West)
-  Various vector functions and statistical functions that are optimised
   for the vector instruction sets of all recent Intel processor
   families

For further documentation, we refer to :ref:`the links to the Intel
documentation at the bottom of this page <Intel documentatino>`.

There are two ways to link the MKL library:

-  If you use icc, icpc or ifort to link your code, you can use the -mkl
   compiler option:

   -  -mkl=parallel or -mkl: Link the multi-threaded version of the
      library.
   -  -mkl=sequential: Link the single-threaded version of the library
   -  -mkl=cluster: Link the cluster-specific and sequential library,
      i.e., ScaLAPACK will be included, but assumes one process per core
      (so no hybrid MPI/multi-threaded approach)

   The Fortran95 interface library for lapack is not automatically
   included though. You'll have to specify that library seperately. You
   can get the value from the `MKL Link Line Advisor`_,
   see also the next item.
-  Or you can specify all libraries explictly. To do this, it is
   strongly recommended to use Intel's `MKL Link Line Advisor`_,
   and will also tell you how to link the MKL library with code
   generated with the GNU and PGI compilers.
   **Note:** On most VSC systems, the variable MKLROOT has a different
   value from the one assumed in the Intel documentation. Wherever you
   see ``$(MKLROOT)`` you may have to replace it with
   ``$(MKLROOT)/mkl``.

MKL also offers a very fast streaming pseudorandom number generator, see
the documentation for details.

Intel toolchain version numbers
-------------------------------

+------+------+------+------+------+------+------+------+------+------+
|      | 2018 | 2017 | 2017 | 2016 | 2016 | 2015 | 2015 | 2014 | 2014 |
|      | a    | b    | a    | b    | a    | b    | a    | b    | a    |
+======+======+======+======+======+======+======+======+======+======+
| icc/ | 2018 | 2017 | 2017 | 16.0 | 16.0 | 15.0 | 15.0 | 13.1 | 13.1 |
| icpc | .1.1 | .4.1 | .1.1 | .3   | .1   | .3   | .1   | .3   | .3   |
| /ifo | 63   | 96   | 32   | 2016 | 2015 | 2015 | 2014 | 2013 | 2013 |
| rt   |      |      |      | 0425 | 1021 | 0407 | 1023 | 0617 | 0607 |
+------+------+------+------+------+------+------+------+------+------+
| Inte | 2018 | 2017 | 2017 | 5.1. | 5.1. | 5.03 | 5.0. | 4.1. | 4.1. |
| l    | .1.1 | .3.1 | .1.1 | 3.18 | 2.15 | .304 | 2.04 | 3.04 | 3.04 |
| MPI  | 63   | 96   | 32   | 1    | 0    | 8    | 4    | 9    | 5    |
+------+------+------+------+------+------+------+------+------+------+
| Inte | 2018 | 2017 | 2017 | 11.3 | 11.3 | 11.2 | 11.2 | 11.1 | 11.1 |
| l    | .1.1 | .3.1 | .1.1 | .3.2 | .1.1 | .3.1 | .1.1 | .2.1 | .1.1 |
| MKL  | 63   | 96   | 32   | 10   | 50   | 87   | 33   | 44   | 06   |
+------+------+------+------+------+------+------+------+------+------+
| GCC  | 6.4. | 6.4. | 6.3. | 4.9. | 4.9. | 4.9. | 4.9. | 4.8. | /    |
|      | 0    | 0    | 0    | 4    | 3    | 3    | 2    | 3    |      |
+------+------+------+------+------+------+------+------+------+------+
| binu | 2.28 | 2.28 | 2.27 | 2.26 | 2.25 | 2.25 | /    | /    | /    |
| tils |      |      |      |      |      |      |      |      |      |
+------+------+------+------+------+------+------+------+------+------+

.. _Intel documentation:

Further information on Intel tools
----------------------------------

-  All Intel documentation of recent software versions is available in
   the `Intel Software Documentation Library`_
   The documentation is typically available for the most recent version
   and sometimes one older version of te compiler and libraries.
-  Some other useful documents:

   -  `Step by Step Performance Optimization with Intel® C++
      Compiler <https://software.intel.com/en-us/articles/step-by-step-optimizing-with-intel-c-compiler>`_.
      Despite the title, the remarks also hold for the C and Fortran
      compilers.
   -  `Direct link to the C/C++ compiler 15.0 user and reference
      guide <https://software.intel.com/en-us/compiler_15.0_ug_c>`_
      (2015a and 2015b toolchains)
   -  `Direct link to the C/C++ compiler 16.0 user and reference
      guide <https://software.intel.com/en-us/intel-cplusplus-compiler-16.0-user-and-reference-guide\%22>`_
      (2016a and 2016b toolchains)
   -  `Direct link to the Fortran compiler 16.0 user and reference
      guide <https://software.intel.com/en-us/intel-fortran-compiler-16.0-user-and-reference-guide>`_
      (2016a and 2016b toolchains)
   -  `Page with links to the documentation of the most recent version
      of Intel
      MPI <https://software.intel.com/en-us/articles/intel-mpi-library-documentation>`_

-  MKL

   -  `Link page to the documentation of MKL 11.2/11.3 on the Intel web
      site <https://software.intel.com/en-us/articles/intel-math-kernel-library-documentation/>`_
      (toolchains 2015a till 2016b)
   -  `MKL Link Line
      Advisor <https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor>`_

-  `Generic BLAS/LAPACK/ScaLAPACK
   documentation <BLAS and LAPACK>`


 .. index::
    single: compiler
    single: MPI
    single: OpenMP
    single: Intel MPI
    single: MKL
    single: BLAS
    single: LAPACK
