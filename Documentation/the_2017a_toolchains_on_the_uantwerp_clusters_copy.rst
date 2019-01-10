The 2017a toolchains on the UAntwerp clusters
=============================================

Important changes
-----------------

The 2017a toolchain is the toolchain thatwill be carried forward to
Leibniz and will be available after the operating system upgrade of
Hopper. Hence it is meant to be as complete as possible. We will only
make a limited number of programs available in the 2016b toolchain
(basically those that show much better performance with the older
compiler or that do not compile with the compilers in the 2017a
toolchains).

Important changes in the 2017a toolchain:

-  The Intel compilers have been installed in a single directory tree,
   much the way Intel intends the install to be done. The intel/2017a
   module loads fewer submodules and instead sets all required
   variables. The install now also contains the Thread Building Blocks
   (TBB), Integrated Performance Primitives (IPP) and Data Analytics
   Acceleration Library (DAAL). All developer tools (debugger,
   Inspector, Advisor, Vtune Amplifier, ITAC) are enabled by loading the
   inteldevtools/2017a module rather than independent modules for each
   tool. More information is available on `the documentation page on the
   Intel compilers @
   UAntwerp <\%22/infrastructure/hardware/hardware-ua/intel\%22>`__.
-  The Python install now also contains a number of packages that
   previously where accessed via separate modules:

   -  matplotlib, so there is no longer a separate module to load
      matplotlib.
   -  lxml

-  The R install now also contains a selection of the Bioconductor
   routines, so no separate module is needed to enable the latter.
-  netCDF is now a single module containing all 4 interfaces rather than
   4 separate modules that installed each interface in a different
   directory tree (three of which all relied on the module for the
   fourth). This should ease the installation of code that uses the
   netCDF Fortran or one of the C++ interfaces and expects all netCDF
   libraries to be installed in the same directory.

We will skip the 2017b toolchain as defined by the VSC as we have
already upgraded the 2017a toolchain to a more recent update of the
Intel 2017 compilers to avoid problems with certain applications.

Available toolchains
--------------------

There are currently three major toolchains on the UAntwerp clusters:

-  The Intel toolchain, which includes the Intel compilers and tools,
   matching versions of the GNU compilers, and all software compiled
   with them.

   -  `Modules in the intel/2017a
      toolchain <\%22/infrastructure/hardware/hardware-ua/toolchain-2017a-intel\%22>`__

-  The FOSS toolchain, built out of open-source components. It is mostly
   used for programs that don’t install with the Intel compilers, or by
   users who want to do development with Open MPI and other open-source
   libraries.
   The FOSS-toolchain has a number of subtoolchains: Gompi, GCC and
   GCCcore, and some programs are installed in these subtoolchains
   because they don’t use the additional components that FOSS offers.

   -  `Modules in the foss/2017a toolchain and its
      subtoolchains <\%22/infrastructure/hardware/hardware-ua/toolchain-2017a-foss\%22>`__

-  The system toolchain (sl6 or centos7), containing programs that only
   use system libraries or other tools from this toolchain.

   -  `Modules in the system toolchain for CentOS
      7 <\%22/infrastructure/hardware/hardware-ua/toolchain-system-centos7\%22>`__

The tables below list the last available module for a given software
package and the corresponding version in the 2017a toolchain. Older
versions can only be installed on demand with a very good motivation, as
older versions of packages also often fail to take advantage of advances
in supercomputer architecture and offer lower performance. Packages that
have not been used recently will only be installed on demand.

Several of the packages in the system toolchain are still listed as “on
demand” since they require licenses and interaction with their users is
needed before we can install them.

"
