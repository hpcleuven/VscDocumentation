MPI distributed programming
===========================

Purpose
-------

MPI (Message Passing Interface) is a language-independent communications
protocol used to program parallel computers. Both point-to-point and
collective communication are supported. MPI "is a message-passing application
programmer interface, together with protocol and semantic specifications for
how its features must behave in any implementation." MPI's goals are high
performance, scalability, and portability. MPI remains the dominant model
used in high-performance computing today.

The current version of the MPI standard is 4.0, but hardly any implementations
currently have support for the new features.  All recent
implementations support the full 3.1 standard though.

Some background information
---------------------------

MPI-1.0 (1994) and its updates MPI-1.1 (1995), MPI-1.2 (1997) and
MPI-1.3 (1998) concentrate on point-to-point communication
(send/receive) and global operations in a static process topology. Major
additions in MPI-2.0 (1997) and its updates MPI-2.1 (2008) and MPI-2.2
(2009) are one-sided communication (get/put), dynamic process management
and a model for parallel I/O. MPI-3.0 (2012) adds non-blocking
collectives, a major update of the one-sided communication model and
neighborhood collectives on graph topologies. An update of the specification,
MPI-3.1 was released in 2015. The MPI-4.0 was formally approved in June 2021.

The two dominant Open Source implementations are `Open MPI`_
and `MPICH`_. The latter has been through
a couple of name changes: It was originally conceived in the early '90's
as MPICH, then the complete rewrite was renamed to MPICH2, but as this
name caused confusion as the MPI standard evolved into MPI 3.x, the name
was changed again to MPICH, and the version number bumped to 3.0.
MVAPICH developed at Ohio State University is the offspring of MPICH
further optimized for InfiniBand and some other high-performance
interconnect technologies. Most other MPI implementations are derived
from one of these implementations.

At the VSC we offer both implementations: Open MPI is offered with the
GNU compilers in the ":ref:`FOSS toolchain`"
, while the Intel MPI used in the ":ref:`Intel toolchain`"
is derived from the MPICH code base.

Prerequisites
-------------

You have a program that uses an MPI library, either developed by you, or
by others. In the latter case, the program's documentation should
mention the MPI library it was developed with.

Implementations
---------------

On VSC clusters, several MPI implementations are installed. We provide
two MPI implementations on all newer machines that implement the MPI-3.1
specification.

#. :ref:`Intel MPI <Communication library: Intel MPI>` in the :ref:`Intel toolchain`
#. :ref:`Open MPI <Communication library: Open MPI>` in the :ref:`FOSS toolchain`


When developing your own software, this is the preferred order to select
an implementation. The performance should be very similar, however, more
development tools are available for Intel MPI
(e.g., ":ref:`ITAC`" for performance monitoring).

Several other implementations may be installed, e.g., `MVAPICH`_, but we assume
you know what you're doing if you choose to use them.

We also assume you are already familiar with the job submission
procedure. If not, check the ":ref:`Running jobs`" section first.

Compiling and running
---------------------

See to the documentation about the :ref:`toolchains`.

Debugging
---------

For debugging, we recommend the Arm DDT debugger (formerly Allinea DDT,
module allinea-ddt). The debugger and the profiler Arm MAP (formerly
Allinea MAP) are now bundled nito ArmForge, which is available as a
module on KU Leuven systems. Video tutorials are available on the
Arm website: `ARM-DDT video`_.  (KU Leuven-only).

When using the Intel toolchain, ":ref:`ITAC`" (ITAC) may also prove useful.

Profiling
---------

To profile MPI applications, one may use `Arm-MAP`_ (formerly Allinea
MAP) or `Scalasca docs`_.  (KU Leuven-only)

Further information
-------------------

-  `Intel MPI`_ web site

   -  `Intel MPI Documentation`_ (Latest version)

-  `Open MPI`_ web site 

   -  `Open MPI Documentation`_

-  SGI MPT, now HPE Performance Software MPI

   -  `HPE MPT Documentation`_

-  `MPI forum`_, where you can also
   find the standard specifications

   -  `MPI Standard documents`_

-  See also the pages in the tutorials section e.g., for
   :ref:`books` and online tutorial :ref:`web tutorials`

