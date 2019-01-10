Using MPI
=========

Purpose
-------

MPI is a language-independent communications protocol used to program
parallel computers. Both point-to-point and collective communication are
supported. MPI \\"is a message-passing application programmer interface,
together with protocol and semantic specifications for how its features
must behave in any implementation.\" MPI's goals are high performance,
scalability, and portability. MPI remains the dominant model used in
high-performance computing today.

The current version of the MPI standard is 3.0, but only the newest
implementations implement the full standard. The previous specifications
are the MPI 2.0 specification with minor updates in the MPI-2.1 and
MPI-2.2 specifications. The standardisation body for MPI is the `MPI
forum <\%22https://www.mpi-forum.org/\%22>`__.

Some background information
---------------------------

MPI-1.0 (1994) and its updates MPI-1.1 (1995), MPI-1.2 (1997) and
MPI-1.3 (1998) concentrate on point-to-point communication
(send/receive) and global operations in a static process topology. Major
additions in MPI-2.0 (1997) and its updates MPI-2.1 (2008) and MPI-2.2
(2009) are one-sided communication (get/put), dynamic process management
and a model for parallel I/O. MPI-3.0 (2012) adds non-blocking
collectives, a major update of the one-sided communication model and
neighbourhood collectives on graph topologies. The first update of the
MPI-3.1 specification was released in 2015, and work is ongoing on the
next major update, MPI-4.0.

The two dominant Open Source implementations are `Open
MPI <\%22https://www.open-mpi.org/\%22>`__ and
`MPICH <\%22https://www.mpich.org/\%22>`__. The latter has been through
a couple of name changes: It was originally conceived in the early '90's
as MPICH, then the complete rewrite was renamed to MPICH2, but as this
name caused confusion as the MPI standard evolved into MPI 3.x, the name
was changed again to MPICH, and the version number bumped to 3.0.
MVAPICH developed at Ohio State University is the offspring of MPICH
further optimised for InfiniBand and some other high-performance
interconnect technologies. Most other MPI implementations are derived
from one of these implementations.

At the VSC we offer both implementations: Open MPI is offered with the
GNU compilers in the `FOSS
toolchain <\%22/cluster-doc/development/toolchain-foss\%22>`__, while
the Intel MPI used in the `Intel
toolchain <\%22/cluster-doc/development/toolchain-intel\%22>`__ is
derived from the MPICH code base.

Prerequisites
-------------

You have a program that uses an MPI library, either developed by you, or
by others. In the latter case, the program's documentation should
mention the MPI library it was developed with.

Implementations
---------------

On VSC clusters, several MPI implementations are installed. We provide
two MPI implementations on all newer machines that can support those
implementations:

#. `Intel
   MPI <\%22/cluster-doc/development/toolchain-intel#intel-mpi\%22>`__
   in the intel toolchain

   #. Intel MPI 4.1 (intel/2014a and intel/2014b toolchains) implements
      the MPI-2.2 specification
   #. Intel MPI 5.0 (intel/2015a and intel/2015b toolchains) and Intel
      MPI 5.1 (intel/2016a and intel/2016b toolchains) implement the
      MPI-3.0 specification

#. `Open
   MPI <\%22/cluster-doc/development/toolchain-foss#openmpi\%22>`__ in
   the foss toolchain

   #. Open MPI 1.6 (foss/2014a toolchain) only implements the MPI-2.1
      specification
   #. Open MPI 1.8 (foss/2014b, foss/2015a and foss/2015b toolchains)
      and Open MPI 1.10 (foss/2016a and foss/2016b) implement the
      MPI-3.0 specification

When developing your own software, this is the preferred order to select
an implementation. The performance should be very similar, however, more
development tools are available for Intel MPI
(i.e.,\ `ITAC <\%22/cluster-doc/development/itac\%22>`__ for performance
monitoring).

Specialised hardware sometimes requires specialised MPI-libraries.

-  The interconnect in\ `Cerebro, the SGI UV shared memory machine at KU
   Leuven <\%22/infrastructure/hardware/hardware-kul#Cerebro\%22>`__\ ,
   provides hardware acceleration for some MPI functions. To take full
   advantage of the interconnect, it is necessary to use the SGI MPI
   library, part of the MPT packages which stands for Message Passing
   Toolkit (and also contains SGI's own implementation
   of\ `OpenSHMEM <\%22http://www.openshmem.org/site/\%22>`__\ ).
   Support is offered through additional toolchains (intel-mpt and
   foss-mpt).

   -  SGI MPT 2.09 (intel-mpt/2014a and foss-mpt/2014a toolchains)
      contains the SGI MPI 1.7 library which implements the MPI-2.2
      specification.
   -  SGI MPT 2.10 (not yet installed, contact\ `KU Leuven
      support <\%22/support/contact-support\%22>`__\ ) contains the SGI
      MPI 1.8 library which implements the MPI-3.0 specification.

Several other implementations may be installed, e.g.,
`MVAPICH <\%22http://mvapich.cse.ohio-state.edu/\%22>`__, but we assume
you know what you're doing if you choose to use them.

We also assume you are already familiar with the job submission
procedure. If not, check the \\"\ `Running
jobs <\%22/cluster-doc/running-jobs\%22>`__\\" section first.

Compiling and running
---------------------

See to the documentation about the
`toolchains <\%22/cluster-doc/development/toolchains\%22>`__.

Debugging
---------

For debugging, we recommend the ARM DDT debugger (formerly Allinea DDT,
module allinea-ddt). `Video tutorials are available on the Arm web
site <\%22https://developer.arm.com/products/software-development-tools/hpc/arm-forge/arm-ddt/video-demos-and-tutorials-for-arm-ddt\%22>`__.
(KU Leuven-only).

When using the intel toolchain, `Intel's Trace Analyser &
Collector <\%22/cluster-doc/development/itac\%22>`__ (ITAC) may also
prove useful.

Profiling
---------

To profile MPI applications, one may use `Arm MAP (formerly Allinea
MAP) <\%22https://www.arm.com/products/development-tools/hpc-tools/cross-platform/forge/map\%22>`__,
or
`Scalasca <\%22http://www.scalasca.org/software/scalasca-2.x/documentation.html\%22>`__.
(KU Leuven-only)

Further information
-------------------

-  `Intel
   MPI <\%22https://software.intel.com/en-us/intel-mpi-library\%22>`__

   -  `Documentation <\%22https://software.intel.com/en-us/articles/intel-mpi-library-documentation/\%22>`__
      (Latest version)

-  `Open MPI <\%22https://www.open-mpi.org/\%22>`__

   -  `Documentation <\%22https://www.open-mpi.org/doc/\%22>`__

-  SGI MPT, now HPE Performance Software MPI

   -  `Documentation <\%22https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-a00037728en_us&docLocale=en_US\%22>`__

-  `MPI forum <\%22https://www.mpi-forum.org\%22>`__, where you can also
   find the standard specifications

   -  `Standard documents <\%22https://www.mpi-forum.org/docs/\%22>`__

-  See also the pages in the `tutorials
   section <\%22/support/tut-book\%22>`__, e.g., for
   `books <\%22/support/tut-book/books#MPI\%22>`__ and `online
   tutorial <\%22/support/tut-book/web-tutorials\%22>`__

"
