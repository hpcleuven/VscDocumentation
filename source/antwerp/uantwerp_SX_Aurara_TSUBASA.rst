.. _UAntwerp NEC SX Aurora:

NEC SX Aurora TSUBASA
=====================

NEC vector computing
--------------------

Vector computing has been around in supercomputing since the 1960s. It is a 
form of Single Instruction Multiple Data parallelism. It works as its name 
implies: It does not only have instructions that operate on scalar values,
but also instructions that operate on a whole vector at once. 

NEC has been building vector computers since the mid 1980s. The first models
were announced in 1983 and became available in 1985. Between June 2002 and
June 2004, the Earth Simulator, a vector computer build by NEC, was the
fastest machine on the Top-500 list. Though vector computers have stayed 
around, clusters based on standard scalar microprocessors pushed them
into very specific niche markets. However, as GPU computing has 
renewed the interest in SIMD-like computing models and hardware,
there is a renewed interest in vector computing.

The NEC SX Aurora is a big change from previous vector computers from NEC.
It tries to combine the best of traditional vector computers and clusters
with (GPU) accelerators.

- Previous SX-series computers were self-standing machines that ran their
  own UNIX-based Operating System on their main processors. 
  The SX Aurora vector processors however are implemented as PCIe boards
  that are plugged into a regular x86 server. the operating system is 
  regular x86 Linux; processes running on the vector engines (as the
  boards are called in NEC terminology) offload operating system
  applications to the x86 CPU of the so-called vector host. Since this is
  done in the libc library, this is completely transparent to the user.
- Each vector engine has its own very fast memory. The vector engines use
  HBM2 memory, the same type of memory used in high-end GPU computing 
  systems, but the peak memory bandwidth is even higher than that of a
  NVIDIA V100 board, NVIDIA's offering at the time the SX Aurora was
  launched. The memory hierarchy is similar as on a CPU, with L1 and
  L2 cache private to each of the 8 cores of the vector engines and
  a shared L3 cache.
- The SX Aurora node can execute both regular x86 programs and VE
  (vector engine) programs. Both are started the same way from the
  standard Linux shells. The operating system recognizes the type of 
  binary and starts it on the appropriate processor type.
- Besides running a program fully on the vector engine (safe the
  transparent offloading of OS operations to the host CPU), the 
  Aurora also supports two types of offloading. It is possible to 
  write programs that run on the host x86 CPU but offload certain
  operations in a GPU-like way to the vector engines. This execution
  model makes it easier to port code from GPU systems to the Aurora.
  However, it is also possible to write programs that run on the 
  vector engines but offload scalar code to the x86 host.
- Previous SX-series computers were big endian machines. However,
  for compatibility of data formats with x86, the SX Aurora uses
  the little-endian byte order.
- Each Vector Host can contain up to 8 Vector Engines. However,
  the memory is not shared between the vector host and the vector
  engines or among the vector engines. Each vector engine also has its
  own process space. Vector Engines can communicate with each other
  through MPI. Larger machines can be built by linking multiple
  vector hosts through InfiniBand.

The software environment consists of the NEC C, C++ and Fortran
compilers, a MPI library specifically for the vector engines, and 
a large library of numeric routines (called NEC Numeric Library Collection
or NLC), that also contains BLAS, LAPACK and FFTW-compatible
routines.
 
UAntwerp obtained a A300-2 system in the seeding campaign. This 
node contains two type 10B vector engines. In return, we promised
to test the technology for our applications and to report about
our experiences to NEC.


Using the SX Aurora at UAntwerp
-------------------------------

Access to the SX Aurora node is currently restricted. Users interested
in experimenting on this node should contact the UAntwerp support team
(hpc@uantwerpen.be). You will be asked to give some feedback on your
experiences.

The Aurora node is not yet integrated in the queueing system. Until
demand would make this necessary, they can be used for experimenting
in an interactive way. The node can be used through ssh from the login
nodes of leibniz and has the name ``aurora`` or long name
``aurora.leibniz.antwerpen.vsc`` (the latter can be used to reach
the node from other nodes also).

For general documentation of the software development environment
and the OS environment, we refer to the NEC documentation:

- An `overview of the manuals <https://www.hpc.nec/documents/>`_.
  We don't have the NQSV and ScaTeFS components at UAntwerp.
- The documentation is part of the 
  `NEC Aurora Forum <https://www.hpc.nec/>`_
  which also contains a `web forum <https://www.hpc.nec/forums/>`_
  where users can interact.

We also developed two modules to ease access to the NEC tools
and compilers:

- ``veutils`` defines a number of aliases for standard Linux tools
  (such as ``ps`` and ``top``) that also have versions for the vector
  engines
- ``vesetup`` sets up the software development environment. We do
  support multiple versions of the compilers and libraries on 
  the system; each version of the ``vesetup`` module supports a
  set of compatible compilers, MPI libraries and NLC library.
  
Please use the standard Lmod module commands such as ``module spider``
and ``module help`` to obtain more information about these modules.

