.. _BLAS and LAPACK:

BLAS and LAPACK
===============

Scope
-----

On modern CPUs the actual performance of a program depends very much on
making optimal use of the caches.

Many standard mathematical algorithms have been coded in standard
libraries, and several vendors and research groups build optimised
versions of those libraries for certain computers. They are key to
extracting optimal performance from modern processors. Don't think you
can write a better dense matrix-matrix multiplication routine or dense
matrix solver than the specialists (unless you're a real specialist
yourself)!

Many codes use dense linear algebra routines. Hence it is no suprise
that in this field, collaboration lead to the definition of a lot of
standard functions and many groups worked hard to build optimal
implementations:

-  BLAS (Basic Linear Algebra Subprograms) is a library of vector,
   vector-vector, matrix-vector and matrix-matrix operations.
-  LAPACK, a library of dense and banded matrix linear algebra routines
   such as solving linear systems, the eigenvalue- and singular value
   decomposition. LAPACK95 defines Fortran95 interfaces for all
   routines.
-  ScaLAPACK is a distributed memory parallel library offering some
   functionality similar to LAPACK.

Reference Fortran implementations do exist, so you can always recompile
code using these libraries on systems on which the libraries are not
available.

BLAS and LAPACK at the VSC
--------------------------

We provide BLAS and LAPACK routines through the toolchains. Hence the
instructions for linking with the libraries are given on the toolchains
page.

-  The :ref:`Intel toolchain` provides the BLAS, LAPACK and ScaLAPACK
   interfaces through the Intel
   Math Kernel Library (MKL)
-  The :ref:`FOSS toolchain` provides open source implementations:

   -  the OpenBLAS BLAS library
   -  the standard LAPACK implementation
   -  the standard ScaLAPACK implementation

Links
-----

-  The LAPACK, LAPACK95 and ScaLAPACK manuals are published by SIAM, but
   there are online HTML versions available on Netlib (the repository
   that also contains the reference Fortran implementations):
_
   -  `LAPACK user guide`_ in the `Netlib BLAS repository`_
   -  `LAPACK95 user guide`_ in the `Netlib LAPACK repository`_
   -  `ScaLAPACK user guide`_ in the `Netlib ScaLAPACK repository`_

-  Documentation about specific implementations is available on the
   :ref:`Toolchains`.

   -  :ref:`Intel toolchain`
   -  :ref:`FOSS toolchain`

.. include:: links.rst
