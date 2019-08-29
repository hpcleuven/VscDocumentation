Software stack
==============

Software installation and maintenance on HPC infrastructure such as the
VSC clusters poses a number of challenges not encountered on a
workstation or a departmental cluster. For many libraries and programs,
multiple versions have to installed and maintained as some users require
specific versions of those. In turn, those libraries or executables sometimes
rely on specific versions of other libraries, further complicating the
matter.

The way Linux finds the right executable for a command, and a program
loads the right version of a library or a plug-in, is through so-called
environment variables. These can, e.g., be set in your shell
configuration files (e.g., ``.bashrc``), but this requires a certain
level of expertise. Moreover, getting those variables right is tricky
and requires knowledge of where all files are on the cluster. Having to
manage all this by hand is clearly not an option.

We deal with this on the VSC clusters in the following way. First, we've
defined the concept of a :ref:`toolchain <toolchains>`. They consist of
a set of compilers, MPI library and
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
programs and libraries, and that is what this page focuses on.


.. _module system basics:

Using the module system
-----------------------

Many software packages are installed as modules. These packages include
compilers, interpreters, mathematical software such as Matlab and SAS,
as well as other applications and libraries. This is managed with the
``module`` command.

Available modules
~~~~~~~~~~~~~~~~~

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


Module names
~~~~~~~~~~~~

In general, the anatomy of a module name is

::

   <package>/<version>-<toolchain>[-<extra>]

For example  for ``Boost/1.66.0-intel-2018a-Python-3.6.4``, we
have

- ``<package>``: Boost, the name of the library,
- ``<version>``: 1.66.0, the version of the Boost library,
- ``<toolchain>``: intel-2018a, the toolchain Boost was built with, and
- ``<extra>``: ``Python-3.6.4``, the version of Python this Boost version
  can inter-operate with.

Some packages in the list above include ``intel-2014a`` or ``foss-2014a`` in their name.
These are packages installed with the 2014a versions of the :ref:`toolchains <toolchains>`
based on the Intel and GNU compilers respectively. The other packages do
not belong to a particular toolchain. The name of the packages also
includes a version number (right after the /) and sometimes other
packages they need.

Searching modules
~~~~~~~~~~~~~~~~~

Often, when looking for some specific software, you will want to filter
the list of available modules, since it tends to be rather large. The
module command writes its output to standard error, rather than standard
output, which is somewhat confusing when using pipes to filter. The
following command would show only the modules that have the string
'python' in their name, regardless of the case.

::

   $ module av |& grep -i python

For more comprehensive searches, you can use ``module spider``, e.g.,

::

   $ module spider python


Info on modules
~~~~~~~~~~~~~~~

The ``spider`` sub-command can also be used to provide information on on modules, e.g.,

::

   $ module spider Python/2.7.14-foss-2018a
   
   ---------------------------------------------
     Python: Python/2.7.14-foss-2018a
   -------------------------------------------
       Description:
           Python is a programming language that lets you work more
           quickly and integrate your systems more effectively. 
   
   
       This module can be loaded directly: module load Python/2.7.14-foss-2018a

More technical information can be obtained using the ``show`` sub-command, e.g.,

::

   $ module show Python/2.7.14-foss-2018a


Loading modules
~~~~~~~~~~~~~~~

A module is loaded using the command ``module load`` with the name of
the package, e.g., with the above list of modules,

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

.. note::

   Loading modules with explicit versions is considered best practice.  It ensures
   that your scripts will use the expected version of the software, regardless of
   newly installed software.  Failing to do this may jeopardize the reproducibility
   of your results!

Modules need not be loaded one by one; the two 'load' commands
can be combined as follows::

   $ module load  BEAST/2.1.2  zlib/1.2.8-foss-2014a

This will load the two modules and, automatically, the respective
toolchains with just one command.

.. warning::

   Do *not* load modules in your ``.bashrc``, ``.bash_profile`` or ``.profile``l,
   you *will* shoot yourself in the foot at some point.  Consider using
   :ref:`module collections <collections of modules>` ``restore`` as a command
   line alternative (so *not* in the shell initialization files either!).


List loaded modules
~~~~~~~~~~~~~~~~~~~

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


Unloading modules
~~~~~~~~~~~~~~~~~

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


Purging modules
~~~~~~~~~~~~~~~

In order to unload all modules at once, and hence be sure to start with
a clean slate, use:

::

   $ module purge

.. note::

   It is a good habit to use this command in PBS scripts, prior to loading
   the modules specifically needed by applications in that job script. This
   ensures that no version conflicts occur if the user loads module using
   his ``.bashrc`` file.


Getting help
~~~~~~~~~~~~

To get a list of all available module commands, type:

::

   $ module help


.. _collections of modules:

Collections of modules
~~~~~~~~~~~~~~~~~~~~~~

Although it is convenient to set up your working environment by loading
modules in your ``.bashrc`` or ``.profile`` file, this is error prone and
you will end up shooting yourself in the foot at some point.

The module system provides an alternative approach that lets you set up
an environment with a single command, offering a viable alternative to
polluting your ``.bashrc``.

Define an environment

   #. Be sure to start with a clean environment
      ::
   
         $ module purge
   
   #. Load the modules you want in your environment, e.g.,
      ::
   
         $ module load matplotlib/2.1.2-intel-2018a-Python-3.6.4
         $ module load matlab/R2019a
   
   #. save your environment, e.g., as ``data_analysis``
      ::
     
          $ module save data_analysis

Use an environment

   ::
   
      $ module restore data_analysis

List all your environments

   ::
   
      $ module savelist

Remove an environment

   ::
   
      $ rm ~/.lmod.d/data_analysis


.. _specialized software stacks:

Specialized software stacks
---------------------------

The list of software available on a particular cluster can be
unwieldingly long and the information that ``module av`` produces
overwhelming. Therefore the administrators may have chosen to only show
the most relevant packages by default, and not show, e.g., packages that
aim at a different cluster, a particular node type or a less complete
toolchain. Those additional packages can then be enabled by loading
another module first. E.g., to get access to the modules in 
the (at the time of writing) incomplete 2019a toolchain on UAntwerpen's 
leibniz cluster, one should first enter

   ::

      $ module load leibniz/2019a-experimental
