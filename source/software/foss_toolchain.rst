.. _FOSS toolchain:

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
processors that support AVX2 instructions, use::

   $ gfortran -O2  -march=haswell  -o fluid  fluid.f90


Documentation on GCC other compiler flags and options is available on the
project's website for the `GCC documentation`_.

.. note::

   Do not forget to load the toolchain module first!


.. _GNU optimization:

Optimizing for a CPU architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To optimize your application or library for specific CPU architectures,
use the appropriate option listed in the table below.

+------------------+---------------------------+
| CPU architecture | compiler option           |
+==================+===========================+
| Ivy Bridge       | ``-march=ivybridge``      |
+------------------+---------------------------+
| Sandy Bridge     | ``-march=sandybridge``    |
+------------------+---------------------------+
| Haswell          | ``-march=haswell``        |
+------------------+---------------------------+
| Broadwell        | ``-march=broadwell``      |
+------------------+---------------------------+
| Skylake          | ``-march=skylake-avx512`` |
+------------------+---------------------------+
| detect host CPU  | ``-march=native``         |
+------------------+---------------------------+

.. note::

   GCC doesn't support applications with multiple code paths, so you have
   to build multiple versions optimized for specific architectures.
   Dispatching can be done at runtime by checking the value of the
   ``$VSC_ARCH_LOCAL`` environment variable.


.. _GCC OpenMP:

GCC OpenMP
~~~~~~~~~~

The compiler switch to use to compile/link OpenMP C/C++ or Fortran code
is ``-fopenmp``. For example, to compile/link a OpenMP C program
``scattter.c`` to an executable ``scatter``, use::

   $ gcc -fopenmp  -O2  -o scatter  scatter.c

.. note::

   The OpenMP runtime library used by GCC is of inferior quality
   when compared to Intel's, so developers are strongly encouraged to use
   the :ref:`Intel toolchain` when developing/building OpenMP software.


Running an OpenMP job
^^^^^^^^^^^^^^^^^^^^^

When submitting a job, remember to specify as many processes per node
as the number of threads the executable is supposed to run. This can
be done using the ``ppn`` resource specification, e.g.,
``-l nodes=1:ppn=10`` for an executable that should be run with 10
OpenMP threads.

.. warning::

   The number of threads *should not* exceed the number of cores on a
   compute node.


.. _OpenMPI:

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
``thermodynamics``::

   $ mpicc -O2  -o thermodynamics  thermo.c

Extensive documentation is provided on the `Open MPI documentation`_ site.

.. note::

   Do not forget to load the toolchain module first.


Running an Open MPI program
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that an MPI program must be run with the exact same version of the
toolchain as it was originally build with. The listing below shows a PBS
job script ``thermodynamics.pbs`` that runs the ``thermodynamics``
executable.

::

   #!/bin/bash -l 

   module load foss/<version> 
   cd $PBS_O_WORKDIR 
   mpirun ./thermodynamics

The hosts and number of processes is retrieved from the queue system,
that gets this information from the resource specification for that job.


FOSS mathematical libraries
---------------------------

The foss toolchain contains the basic HPC mathematical libraries, it
offers:

-  `OpenBLAS`_ (Basic Linear Algebra Subprograms)
-  LAPACK from the `Netlib LAPACK repository`_ (Linear Algebra PACKage)
-  ScaLAPACK from the `Netlib ScaLAPACK repository`_ (Scalable Linear Algebra PACKage)
-  `FFTW`_ (Fastest Fourier Transform in the West)

Other components
----------------

-  From the 2015b series on, binutils was added to the toolchain. The
   binutils package contains the assembler used by gcc, and the standard
   OS assembler doesn't always support the newer instructions that are
   used on newer cluster nodes.

Version numbers
---------------

+-----------+--------+--------+--------+--------+--------+--------+
|           | 2019a  | 2018b  | 2018a  | 2017b  | 2017a  | 2016b  |
+===========+========+========+========+========+========+========+
| GCC       | 8.2.0  | 7.3.0  | 6.4.0  | 6.4.0  | 6.3    | 5.4    |
+-----------+--------+--------+--------+--------+--------+--------+
| Open MPI  | 3.1.3  | 3.1.1  | 2.1.2  | 2.1.1  | 2.0.2  | 1.10.3 |
+-----------+--------+--------+--------+--------+--------+--------+
| OpenBLAS  | 0.3.5  | 0.3.1  | 0.2.20 | 0.2.20 | 0.2.19 | 0.2.18 |
+-----------+--------+--------+--------+--------+--------+--------+
| LAPACK    |        |        |        |        | 3.7.0  | 3.6.1  |
+-----------+--------+--------+--------+--------+--------+--------+
| ScaLAPACK | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  | 2.0.2  |
+-----------+--------+--------+--------+--------+--------+--------+
| FFTW      | 3.3.8  | 3.3.8  | 3.3.7  | 3.3.6  | 3.3.6  | 3.3.4  |
+-----------+--------+--------+--------+--------+--------+--------+
| binutils  | 2.32   | 2.30   | 2.28   | 2.28   | 2.27   | 2.26   |
+-----------+--------+--------+--------+--------+--------+--------+


Further information on FOSS components
--------------------------------------

-  Overview of `GCC documentation`_ (all versions)
-  Open MPI documentation

   -  `3.1.x (foss/2018b and foss/2019a) <https://www.open-mpi.org/doc/v3.1/>`_
   -  `2.1.x (foss/2017b and foss/2018a) <https://www.open-mpi.org/doc/v2.1/>`_
   -  `2.0.x (foss/2017a) <https://www.open-mpi.org/doc/v2.0/>`_
   -  `1.10.x (foss/2016b) <https://www.open-mpi.org/doc/v1.10/>`_

-  The `OpenBLAS`_ project page and `OpenBLAS Wiki`_
-  :ref:`Generic BLAS/LAPACK/ScaLAPACK documentation <BLAS and LAPACK>`
-  `FFTW documentation`_
-  `GNU binutils documentation`_

 .. index::
    single: compiler
    single: MPI
    single: OpenMP
    single: Open MPI

.. include:: links.rst
