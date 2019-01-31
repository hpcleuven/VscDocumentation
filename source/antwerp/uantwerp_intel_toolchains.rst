.. _Antwerp 2017a intel:

UAntwerp Intel toolchains
=========================

From version 2017a on of the Intel toolchains, the setup on the UAntwerp
is different from the one on some other VSC clusters:

-  A full install of all Intel tools for which we have a license at
   UAntwerp has been performed in a single directory tree as intended by
   Intel. There is a single module for the C/C++/Fortran compilers,
   Intel MPI, the libraries MKL (Math Kernel Library), IPP (Integrated
   Performance Primitives), TBB (Threading Building Blocks) and DAAL
   (Data Analytics Acceleration Library) and Intel-provided GDB-based
   debuggers. The Intel tools for code and performance analysis VTune
   Amplifier XE, Intel Trace Analyzer and Collector (ITAC), Intel
   Advisor XE and Intel Inspector XE are also installed, but these still
   have separate module files as they rely on overloading libraries in
   some cases.
-  There should be no need to run any of the configuration scripts
   provided by Intel, all variables should be set correctly by the
   module file. Contact user support if this is not the case. The
   configuration scripts should work as intended by Intel though should
   you want to use the compilers without loading the module.
-  Several variables specific for the way software is set up at the VSC
   are defined the way they would be defined if the Intel toolchain was
   defined in the standard VSC way through the module tree. As such, we
   expect that you should be able to use any Makefile developed for the
   standard VSC-setup.
-  All compiler components needed to develop applications with offload
   to a Xeon Phi expansion board are also provided in anticipation of
   the installation of such a cluster node for testing purposes in
   Leibniz.

Compilers
---------

-  The compilers work exactly in the way described on `the regular Intel
   toolchain web
   page <\%22/cluster-doc/development/toolchain-intel\%22>`__, including
   the MPI compiler wrappers. All links to the documentation on that
   page are also relevant.
-  Man pages for all commands have also been installed.

Debuggers
---------

-  Intel-adapted GDB debuggers have been installed

   -  Debugging regular Intel64 applications: ``gdb-ia``
   -  Debugging applications with offload to Xeon Phi: ``gdb-mic``

-  Manual pages and GNU info pages are available for both commands

Libraries
---------

Math Kernel Library (MKL)
~~~~~~~~~~~~~~~~~~~~~~~~~

MKL works exactly as in the regular VSC Intel toolchain. See `the MKL
section of web page on the VSC Intel
toolchain <\%22https://www.vscentrum.be/cluster-doc/development/toolchain-intel#intel-mathematical-libraries\%22>`__
for more information.

Integrated Performance Primitives (IPP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  What? The Intel Integrated Performance Primitives is a software
   library that provides a broad range of functionality, including
   general signal and image processing, computer vision, data
   compression, cryptography, and string manipulation. The functions are
   heavily optimised for the Intel processors.
-  Documentation

   -  `Getting started with Intel® Integrated Performance Primitives
      2017 for Linux\*
      OS <\%22https://software.intel.com/en-us/get-started-with-ipp-for-linux\%22>`__
   -  Developer guide and various tutorials in `the Intel Software
      Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__

Threading Building Blocks (TBB)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  What? A C++ template library for task parallelism. The library is
   developed by Intel, but now available under the Apache 2.0 license
   and runs also with non-Intel compilers, so you don't have to be
   concerned about vendor lock-in.
-  Documentation

   -  `The Intel Threading Building Blocks web
      site <\%22https://www.threadingbuildingblocks.org/\%22>`__
   -  Documentation in the `Intel Software Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__

Data Analytics Acceleration Library (DAAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  What? A library with building blocks covering all stages of data
   analytics: data acquisition from a data source, preprocessing,
   transformation, data mining, modeling, validation, and decision
   making. The implementation is heavily optimised for Intel processors.
-  Documentation

   -  `Getting Started with Intel® Data Analytics Acceleration Library
      for
      Linux <\%22https://software.intel.com/en-us/get-started-with-daal-for-linux\%22>`__
   -  Documentation in the `Intel Software Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__

Code and performance analysis
-----------------------------

VTune Amplifier XE
~~~~~~~~~~~~~~~~~~

-  What? VTune Amplifier is a tool for runtime analysis of serial and
   shared memory applications. For a list of features, please consult
   the `Getting Started with VTune web
   page <\%22https://software.intel.com/en-us/get-started-with-vtune\%22>`__.
-  Module: ``VTune/<toolchain version>``, e.g., ``VTune/2017a``.
-  How? VTune Amplifier is started through the ``amplxe-gui`` (GUI
   version) or ``amplxe-cl`` (command line version) command.
-  Documentation:

   -  `Getting started with VTune web page on the Intel web
      site <\%22https://software.intel.com/en-us/get-started-with-vtune\%22>`__
   -  `VTune Amplifier training page by
      Intel <\%22https://software.intel.com/en-us/intel-vtune-amplifier-xe-support/training\%22>`__
   -  Intel VTune Amplifier documentation in the `Intel Software
      Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__
   -  Man page for ``amplxe-cl`` (after loading the appropriate VTune
      module)

ITAC - Intel Trace Analyzer and Collector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  What? ITAC is a graphical tool to understand MPI application
   behaviour. A full set of features can be found on the `Getting
   Started with Intel Trace Analyzer and Colllector
   page <\%22https://software.intel.com/en-us/get-started-with-itac\%22>`__.
-  How? Analysis is a two-step operation:

   #. Run your application using the ``-trace`` option of mpirun to
      collect data in a ``.stf`` file.
   #. Analyse the data using ``traceanalyzer``

-  Module: ``itac/<toolchain version>``, e.g., ``itac/2017a``.
-  Documentation:

   -  `Getting started with Intel Trace Analyzer and Collector on the
      Intel web
      site <\%22https://software.intel.com/en-us/get-started-with-itac\%22>`__
   -  `Training videos on the Intel
      site <\%22https://software.intel.com/en-us/intel-trace-analyzer-support/training\%22>`__
   -  Intel Trace Analyzer and Collector documentation in the `Intel
      Software Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__
   -  Manual pages for the library functions and some commands

Advisor
~~~~~~~

-  What? Advisor is a code analysis tool that works with the compilers
   to give advise on vectorization and threading for both the Xeon and
   Xeon Phi processors.
-  How? Advisor uses output generated by the compiler when building a
   full optimized release build and as such expects that some additional
   options are specified when compiling the application. The resulting
   compiler output can then be analized using the ``advixe-gui``
   command.
-  Module: ``Advisor/<toolchain version>``, e.g., ``Advisor/2017a``.
-  Documentation

   -  `Getting started with Intel
      Advisor <\%22https://software.intel.com/en-us/get-started-with-advisor\%22>`__
   -  Intel Advisor documentation in the `Intel Software Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__
   -  Manual page for ``advixe-cl``

Inspector
~~~~~~~~~

-  What? Inspector is a run-time analysis error checking tool for
   dynamic memory and threading errors.
-  How? Inspector uses a debug build of you application. The application
   is run from within Inspector. Inspector can be started with the
   ``inspxe-gui`` (GUI version) or ``inspxe-cl`` (Command Line version)
   command.
-  Module: ``Inspector/<toolchain version>``, e.g., ``Inspector/2017a``.
-  Documentation:

   -  `Getting started with Intel Inspector - Linux
      OS <\%22https://software.intel.com/en-us/node/595380\%22>`__
   -  `Intel Online Training
      material <\%22https://software.intel.com/en-us/intel-inspector-xe-support/training\%22>`__
   -  `Intel Inspector Help - Linux
      OS <\%22https://software.intel.com/en-us/inspector-user-guide-linux\%22>`__
   -  Further Intel Inspector documentation in the `Intel Software
      Documentation
      Library <\%22https://software.intel.com/en-us/documentation\%22>`__
   -  Manual page for ``inspxe-cl``

"
