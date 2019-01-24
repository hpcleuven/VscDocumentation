.. _Toolchains:

Toolchains
==========

What are toolchains?
--------------------

A toolchain is a collection of tools to build (HPC) software
consistently. It consists of

-  compilers for C/C++ and Fortran,
-  a communications library (MPI), and
-  mathematical libraries (linear algebra, FFT).

Toolchains at the VSC are versioned, and refreshed twice a year. All
software available on the cluster is rebuild when a new version of a
toolchain is defined to ensure consistency. Version numbers consist of
the year of their definition, followed by either ``a`` or ``b``, e.g.,
``2014a``. Note that the software components are not necessarily the
most recent releases, rather they are selected for stability and
reliability.

Available toolchains at the VSC
-------------------------------

Two toolchain flavors are standard across the VSC on all machines that
can support them:

-  `Intel
   toolchain <\%22https://www.vscentrum.be/cluster-doc/development/toolchain-intel\%22>`__,
   based on Intel software components,
-  `FOSS
   toolchain <\%22https://www.vscentrum.be/cluster-doc/development/toolchain-foss\%22>`__,
   based on free and open source software.

It may be of interest to note that the Intel C/C++ compilers are more
strict with respect to the standards than the GCC C/C++ compilers, while
for Fortran, the GCC Fortran compiler tracks the standard more closely,
while Intel's Fortran allows for many extensions added during Fortran's
long history. When developing code, one should always build with both
compiler suites, and eliminate all warnings.

On average, the Intel compiler suite produces executables that are 5 to
10 % faster than those generated using the GCC compiler suite. However,
for individual applications the differences may be more significant with
sometimes significantly faster code produced by the Intel compilers
while on other applications the GNU compiler may produce much faster
code.

Additional toolchains may be defined on specialised hardware to extract
the maximum performance from that hardware.

-  On Cerebro, the SGI UV shared memory system at the KU Leuven, you
   need to use the SGI MPI-library (called MPT for Message Passing
   Toolkit) to get the maximum performance from the interconnect (which
   offers hardware acceleration for some MPI functions). On that
   machine, two additional toolchains are defined, ``intel-mpt`` and
   ``foss-mpt``, equivalent to the standard ``intel`` and ``foss``
   toolchains respectively but with the MPI library replaced with MPT.

For detailed documentation on each of these toolchains, we refer to the
pages linked above in this document.

"
