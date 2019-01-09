FOSS toolchain
==============

The ``foss`` toolchain consists entirely of free and open source
software components. When building third-party software, or developing
your own, load the module for the toolchain:

::

   $ module load foss/<version>

where ``<version>`` should be replaced by the one to be used, e.g.,
``2014a``. See the documentation on the software module system for more
details.

Compilers: GNU
--------------

Three GCC compilers are available:

-  C: ``gcc``
-  C++: ``g++``
-  Fortran: ``gfortran``

For example, to compile/link a Fortran program ``fluid.f90`` to an
executable ``fluid`` with architecture specific optimization for
processors that support AVX instructions, use:

::

   $ gfortran -O2 -march=corei7-avx -o fluid fluid.f90

Documentation on GCC compiler flags and options is available on the
`project's website <\%22http://gcc.gnu.org/onlinedocs/\%22>`__. Do not
forget to load the toolchain module first!

GCC OpenMP
~~~~~~~~~~

The compiler switch to use to compile/link OpenMP C/C++ or Fortran code
is ``-fopenmp``. For example, to compile/link a OpenMP C program
``scattter.c`` to an executable ``scatter`` with optimization for
processors that support the AVX instruction set, use:

::

   $ gcc -fopenmp -O2 -march=corei7-avx -o scatter scatter.c

Remember to specify as many processes per node as the number of threads
the executable is supposed to run. This can be done using the ``ppn``
resource, e.g., ``-l nodes=1:ppn=10`` for an executable that should be
run with 10 OpenMP threads. The number of threads should not exceed the
number of cores on a compute node.

Note that the OpenMP runtime library used by GCC is of inferior quality
when compared to Intel's, so developers are strongly encouraged to use
the ```intel`` toolchain <\%22#intel-toolchain\%22>`__ when
developing/building OpenMP software.

Communication library: Open MPI
-------------------------------

For the ``foss`` toolchain, Open MPI is used as the communications
library. To compile/link MPI programs, wrappers are supplied, so that
the correct headers and libraries are used automatically. These wrappers
are:

-  C: ``mpicc``
-  C++: ``mpic++``
-  Fortran: ``mpif77``, ``mpif90``

The compiler wrappers take the same options as the corresponding
compilers.

Using the MPI compilers from Open MPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, to compile/link a C program ``thermo.c`` to an executable
``thermodynamics`` with architecture specific optimization for the AVX
instruction set, use:

::

   $ mpicc -O2 -march=corei7-avx -o thermodynamics thermo.c

Extensive documentation is `provided on the Open MPI project's
website <\%22https://www.open-mpi.org/doc/\%22>`__. Do not forget to
load the toolchain module first.

Running an Open MPI program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that an MPI program must be run with the exact same version of the
toolchain as it was originally build with. The listing below shows a PBS
job script ``thermodynamics.pbs`` that runs the ``thermodynamics``
executable.

::

   #!/bin/bash -l 
   module load intel/<version> 
   cd $PBS_O_WORKDIR 
   mpirun ./thermodynamics

The hosts and number of processes is retrieved from the queue system,
that gets this information from the resource specification for that job.

FOSS mathematical libraries
---------------------------

The foss toolchain contains the basic HPC mathematical libraries, it
offers:

-  `OpenBLAS <\%22http://www.openblas.net/\%22>`__ (Basic Linear Algebra
   Subsystem)
-  `Lapack <\%22http://www.netlib.org/lapack/\%22>`__\ (Linear Algebra
   PACKage)
-  ScaLAPACK (Scalable Linear Algebra PACKage)
-  `FFTW <\%22http://www.fftw.org/\%22>`__ (Fastest Fourier Transform in
   the West)

Other components
----------------

-  From the 2015b series on, binutils was added to the toolchain. The
   binutils package contains the assembler used by gcc, and the standard
   OS assembler doesn't always support the newer instructions that are
   used on newer cluster nodes.

Version numbers
---------------

+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
|           | 2018a  | 2017b  | 2017a  | 2016b  | 2016a  | 2015b  | 2015a  | 2014b | 2014a |
+===========+========+========+========+========+========+========+========+=======+=======+
| GCC       | 6.4.0  | 6.4.0  | 6.3    | 5.4    | 4.9.3  | 4.9.3  | 4.9.2  | 4.8.3 | 4.8.2 |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
| OpenMPI   | 2.1.2  | 2.1.1  | 2.0.2  | 1.10.3 | 1.10.2 | 1.8.8  | 1.8.4  | 1.8.1 | 1.6.5 |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
| OpenBLAS  | 0.2.20 | 0.2.20 | 0.2.19 | 0.2.18 | 0.2.15 | 0.2.14 | 0.2.13 | 0.2.9 | 0.2.8 |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
| LAPACK    | 3.8.0  | 3.8.0  | 3.3.6  | 3.6.1  | 3.6.0  | 3.5.0  | 3.5.0  | 3.5.0 | 3.5.0 |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
| ScaLAPACK | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2 | 2.0.2 |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
| FFTW      | 3.3.7  | 3.3.6  | 3.3.6  | 3.3.4  | 3.3.4  | 3.3.4  | 3.3.4  | 3.3.4 | 3.3.3 |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+
| binutils  | 2.28   | 2.28   | 2.27   | 2.26   | 2.25   | 2.25   | /      | /     | /     |
+-----------+--------+--------+--------+--------+--------+--------+--------+-------+-------+

Further information on FOSS components
--------------------------------------

-  `Overview of GCC manuals (all
   versions) <\%22https://gcc.gnu.org/onlinedocs/\%22>`__
-  OpenMPI documentation

   -  `2.0.x
      (foss/2017a) <\%22https://www.open-mpi.org/doc/v2.0/\%22>`__
   -  `1.10.x (foss/2016a and
      foss/2016b) <\%22https://www.open-mpi.org/doc/v1.10/\%22>`__
   -  `1.8.x (foss/2014b, foss/2015a and
      foss/2015b) <\%22https://www.open-mpi.org/doc/v1.8/\%22>`__
   -  `1.6.x
      (foss/2014a) <\%22https://www.open-mpi.org/doc/v1.6/\%22>`__

-  The `OpenBLAS project page <\%22http://www.openblas.net/\%22>`__ and
   `documentation
   Wiki <\%22https://github.com/xianyi/OpenBLAS/wiki\%22>`__
-  `Generic BLAS/LAPACK/ScaLAPACK
   documentation <\%22/cluster-doc/development/blas-lapack#Links\%22>`__
-  `FFTW documentation <\%22http://www.fftw.org/#documentation\%22>`__
-  `GNU binutils
   documentation <\%22https://sourceware.org/binutils/docs/\%22>`__

"
