Xeon Phi @UAntwerp
==================

Leibniz has one compute node equipped with a Xeon Phi coprocessor from
the Knights Landing generation (the first generation with support for
the AVX-512 instruction set). For cost reasons we have opted for the
PCIe coprocessor model rather than an independent node based on that
processor. Downside is the lower memory capacity directly available to
the Xeon Phi processor though.

The goals for the system are:

-  Having a test device for AVX-512 code as it was too early to purchase
   Sky Lake Xeon CPUs.
-  Assessing the performance of the Xeon Phi compared to regular compute
   nodes to determine whether it is interesting to further invest in
   this technology for a later cluster or cluster update.

The system is set up in such a way that once you have access to the Xeon
Phi node, you can also log on to the Xeon Phi card itself and use it as
an independent system. Your regular VSC directories will be mounted (at
least for UAntwerp users, others on request). As such you can also test
code to run on independent Xeon Phi systems, the kind of setup that
Intel is currently promoting.

The module system is not yet implemented on the Xeon Phi coprocessor,
but modules do work on the host. It does imply though that some setup
may be required when running native programs on the Xeon Phi.

Getting access
--------------

Contact `the UAntwerp support team <\%22/support/contact-support\%22>`__
to get access to the Xeon Phi node.

Users of the Xeon Phi node are expected to report back on their
experiences. We are most interested in users who can also compare with
running on regular nodes as we will use this information for future
purchase decisions.

Currently the node is not yet in the job system, you can log on manually
to the node but need to check if noone else is using the node.

Compiling for the Xeon Phi
--------------------------

We currently support compiling code for the Xeon Phi with the Intel
compilers included in the 2017a and later toolchains (i.e., Intel
compiler version 17 and higher).

Compared to the earlier Knights Corner based Xeon Phi system installed
in the Tier-2 infrastructure at the KU Leuven, there are a number of
changes. All come down to the fact that the Knights Landing Xeon Phi has
much more in common with the regular Intel CPUs than was the case for
the earlier generation.

-  Don't use the -mmic compiler option to compile code for the Xeon Phi.
   This option generates code for the Knights Corner instruction set
   which is not compatible with the Knights Landing processors. Instead,

   -  Use -xMIC-AVX512 to compile code that runs natively on the Xeon
      Phi
   -  Use -qoffload-arch:mic-avx512 (in combination met -xHost) for
      programs that run on the host but offload sections to the Xeon
      Phi.

   In most cases you'll also want to use -qopenmp to enable OpenMP, the
   primary programming model for the Xeon Phi.
-  Similarly, environment variables that start with MIC are for KNC
   only. KNL uses the same libraries as regular x86-64 code.
-  Mind the meaning of the \_MIC_\_ preprocessor macro in old Xeon Phi
   code. It is set when compiling for the KNC generation cards, but some
   code may use it wrongly for conditional compilation of parts of
   offloaded code, which really should have been done through
   \__TARGET_ARCH_MIC which works for both KNC and KNL. For conditional
   compilation of code for KNL in both offload and native routines, one
   should use the \__AVX512F_\_ feature macro.

Running applications on the Xeon Phi
------------------------------------

-  Programs that use offloading are started in the same way as regular
   host programs. Nothing special needs to be done. The offloaded code
   runs on the coprocessor under the userid micuser.
-  Simple native programs can be started from the host using the
   micnativeloadex command followed by the name of the executable and
   other arguments. The micnativeloadex command will look up all shared
   libraries used by the executable and make sure that they are uploaded
   to the Xeon Phi. To find the libraries, it uses the environment
   variable SINK_LD_LIBRARY_PATH. For programs that only rely on a
   compiler module, our compiler modules take care of the proper
   definition of this variable. Your program will run on the coprocessor
   under a special userid, micuser, which also implies that you cannot
   acces your own files!
   *According to the Xeon Phi manuals, certain requests are send
   automatically to the host but it is not clear at the moment what this
   implies.*
-  The second way to start native programs is to log on to the Xeon Phi
   using ssh (ssh mic0) and work the way you would on a regular cluster
   node. You will see the same directories that you also see on the
   regular Xeon Phi node (minus the /small file system at the moment)
   and will have access to the same data in the same way.
   *The module system has not yet been implemented on the Xeon Phi.*

"
