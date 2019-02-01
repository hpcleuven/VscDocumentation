Software stack
==============

Software installation and maintenance on HPC infrastructure such as the
VSC clusters poses a number of challenges not encountered on a
workstation or a departemental cluster. For many libraries and programs,
multiple versions have to installed and maintained as some users require
specific versions of those. And those libraries or executable sometimes
rely on specific versions of other libraries, further complicating the
matter.

The way Linux finds the right executable for a command, and a program
loads the right version of a library or a plug-in, is through so-called
environment variables. These can, e.g., be set in your shell
configuration files (e.g., ``.bashrc)``, but this requires a certain
level of expertise. Moreover, getting those variables right is tricky
and requires knowledge of where all files are on the cluster. Having to
manage all this by hand is clearly not an option.

We deal with this on the VSC clusters in the following way. First, we've
defined the concept of a :doc:`toolchain <toolchains>` on most of
the newer clusters. They consist of a set of compilers, MPI library and
basic libraries that work together well with each other, and then a
number of applications and other libraries compiled with that set of
tools and thus often dependent on those. We use tool chains based on the
Intel and GNU compilers, and refresh them twice a year, leading to
version numbers like 2014a, 2014b or 2015a for the first and second
refresh of a given year. Some tools are installed outside a toolchain,
e.g., additional versions requested by a small group of users for
specific experiments, or tools that only depend on basic system
libraries. Second, we use the module system to manage the environment
variables and all dependencies and possible conflicts between various
programs and libraries., and that is what this page focuses on.

.. _module system basics:

Basic use of the module system
------------------------------

Many software packages are installed as modules. These packages include
compilers, interpreters, mathematical software such as Matlab and SAS,
as well as other applications and libraries. This is managed with the
``module`` command.

To view a list of available software packages, use the command
``module av``. The output will look similar to this:

::

   $ module av
   ----- /apps/leuven/thinking/2014a/modules/all ------
   Autoconf/2.69-GCC-4.8.2
   Autoconf/2.69-intel-2014a
   Automake/1.14-GCC-4.8.2
   Automake/1.14-intel-2014a
   BEAST/2.1.2
   ...
   pyTables/2.4.0-intel-2014a-Python-2.7.6
   timedrun/1.0.1
   worker/1.4.2-foss-2014a
   zlib/1.2.8-foss-2014a
   zlib/1.2.8-intel-2014a

This gives a list of software packages that can be loaded. Some packages
in this list include ``intel-2014a`` or ``foss-2014a`` in their name.
These are packages installed with the 2014a versions of the toolchains
based on the Intel and GNU compilers respectively. The other packages do
not belong to a particular toolchain. The name of the packages also
includes a version number (right after the /) and sometimes other
packages they need.

Often, when looking for some specific software, you will want to filter
the list of available modules, since it tends to be rather large. The
module command writes its output to standard error, rather than standard
output, which is somewhat confusing when using pipes to filter. The
following command would show only the modules that have the string
'python' in their name, regardless of the case.

::

   $ module av |& grep -i python

A module is loaded using the command ``module load`` with the name of
the package. E.g., with the above list of modules,

::

   $ module load BEAST

will load the ``BEAST/2.1.2`` package.

For some packages, e.g., ``zlib`` in the above list, multiple versions
are installed; the ``module load`` command will automatically choose the
lexicographically last, which is typically, but not always, the most
recent version. In the above example,

::

    $ module load zlib

will load the module ``zlib/1.2.8-intel-2014a``. This may not be the
module that you want if you're using the GNU compilers. In that case,
the user should specify a particular version, e.g.,

::

   $ module load zlib/1.2.8-foss-2014a

Obviously, the user needs to keep track of the modules that are
currently loaded. After executing the above two load commands, the list
of loaded modules will be very similar to:

::

   $ module list
   Currently Loaded Modulefiles:
     1) /thinking/2014a
     2) Java/1.7.0_51
     3) icc/2013.5.192
     4) ifort/2013.5.192
     5) impi/4.1.3.045
     6) imkl/11.1.1.106
     7) intel/2014a
     8) beagle-lib/20140304-intel-2014a
     9) BEAST/2.1.2
    10) GCC/4.8.2
    11) OpenMPI/1.6.5-GCC-4.8.2
    12) gompi/2014a
    13) OpenBLAS/0.2.8-gompi-2014a-LAPACK-3.5.0
    14) FFTW/3.3.3-gompi-2014a
    15) ScaLAPACK/2.0.2-gompi-2014a-OpenBLAS-0.2.8-LAPACK-3.5.0
    16) foss/2014a
    17) zlib/1.2.8-foss-2014a

It is important to note at this point that, e.g., ``icc/2013.5.192`` is
also listed, although it was not loaded explicitly by the user. This is
because ``BEAST/2.1.2`` depends on it, and the system administrator
specified that the ``intel`` toolchain module that contains this
compiler should be loaded whenever the ``BEAST`` module is loaded. There
are advantages and disadvantages to this, so be aware of automatically
loaded modules whenever things go wrong: they may have something to do
with it!

To unload a module, one can use the ``module unload`` command. It works
consistently with the ``load`` command, and reverses the latter's
effect. One can however unload automatically loaded modules manually, to
debug some problem.

::

   $ module unload BEAST

Notice that the version was not specified: the module system is
sufficiently clever to figure out what the user intends. However,
checking the list of currently loaded modules is always a good idea,
just to make sure...

In order to unload all modules at once, and hence be sure to start with
a clean slate, use:

::

   $ module purge

It is a good habit to use this command in PBS scripts, prior to loading
the modules specifically needed by applications in that job script. This
ensures that no version conflicts occur if the user loads module using
his ``.bashrc`` file.

Finally, modules need not be loaded one by one; the two 'load' commands
can be combined as follows:

::

   $ module load  BEAST/2.1.2  zlib/1.2.8-foss-2014a

This will load the two modules and, automatically, the respective
toolchains with just one command.

To get a list of all available module commands, type:

::

   $ module help


.. _specialized software stacks:

Specialized software stacks
---------------------------

The list of software available on a particular cluster can be
unwieldingly long and the information that ``module av`` produces
overwhelming. Therefore the administrators may have chose to only show
the most relevant packages by default, and not show, e.g., packages that
aim at a different cluster, a particular node type or a less complete
toolchain. Those additional packages can then be enabled by loading
another module first. E.g., on hopper, the most recent UAntwerpen
cluster when we wrote this text, the most complete and most used
toolchains were the 2014a versions. Hence only the list of packages in
those releases of the ``intel`` and ``foss`` (GNU) toolchain were shown
at the time. Yet

::

   $ module av

returns at the end of the list:

::

   ...
   ifort/2015.0.090                   M4/1.4.16-GCC-4.8.2
   iimpi/7.1.2                        VTune/2013_update10
   ----------------------- /apps/antwerpen/modules/calcua ------------------------
   hopper/2014a hopper/2014b hopper/2015a hopper/2015b hopper/2016a hopper/2016b 
   hopper/all   hopper/sl6   perfexpert   turing

The packages such as ``hopper/2014b`` enable additional packages when
loaded.

Similarly, on ThinKing, the KU Leuven cluster:

::

   $ module av
   ...
   -------------------------- /apps/leuven/etc/modules/ --------------------------
   cerebro/2014a   K20Xm/2014a     K40c/2014a      M2070/2014a     thinking/2014a
   ictstest/2014a  K20Xm/2015a     K40c/2015a      phi/2014a       thinking2/2014a

shows modules specifically for the thin node cluster ThinKing, the `SGI
shared memory system
Cerebro <\%22/infrastructure/hardware/hardware-kul#Cerebro\%22>`__,
three types of NVIDIA GPU nodes and the Xeon Phi nodes. Loading one of
these will show the appropriate packages in the list obtained with
``module av``. E.g.,

::

   module load cerebro/2014a

will make some additional modules available for Cerebro, including two
additional toolchains with the SGI MPI libraries to take full advantage
of the interconnect of that machine.


Explicit version numbers
------------------------

As a rule, once a module has been installed on the cluster, the
executables or libraries it comprises are never modified. This policy
ensures that the user's programs will run consistently, at least if the
user specifies a specific version. Failing to specify a version may
result in unexpected behavior.

Consider the following example: the user decides to use the GSL library
for numerical computations, and at that point in time, just a single
version 1.15, compiled with the foss toolchain is installed on the
cluster. The user loads the library using:

::

   $ module load GSL

rather than

::

   $ module load GSL/1.15-foss-2014a

Everything works fine, up to the point where a new version of GSL is
installed, e.g., 1.16 compiled with both the ``intel`` and the ``foss``
toolchain. From then on, the user's load command will load the latter
version, rather than the one he intended, which may lead to unexpected
problems.
