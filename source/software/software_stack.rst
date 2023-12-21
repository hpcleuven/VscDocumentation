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
   ----- /apps/leuven/skylake/2018a/modules/all ------
   Autoconf/2.69-GCC-4.8.2
   Autoconf/2.69-intel-2018a
   Automake/1.14-GCC-4.8.2
   Automake/1.14-intel-2018a
   BEAST/2.1.2
   ...
   pyTables/2.4.0-intel-2018a-Python-2.7.6
   timedrun/1.0.1
   worker/1.4.2-foss-2018a
   zlib/1.2.8-foss-2018a
   zlib/1.2.8-intel-2018a


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

Searching modules
~~~~~~~~~~~~~~~~~

Often, when looking for some specific software, you will want to filter
the list of available modules, since it tends to be rather large.
The following command would only show the modules that have the string
'python' in their name, regardless of the case.

::

   $ module av python

Note that the search done by ``module av`` is case-agnostic, meaning that
you will get the same result even if you search like ``module av pYThoN``.
For more comprehensive searches, you can use ``module spider``, e.g.,

::

   $ module spider python

However, the output result can be in some cases very exhaustive.


Info on modules
~~~~~~~~~~~~~~~

The ``spider`` sub-command can also be used to provide information about
a specific module, e.g.,

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

will load the module ``zlib/1.2.12`` (at the time of thiw writing), which
is a version built relying on the system compilers. This,
however, may not be the module that you exactly want. Therefore, it is
strongly recommended that the user would load a particular version, e.g.,

::

   $ module load zlib/1.2.12-GCCcore-12.2.0

.. note::

   Loading modules with explicit versions is considered best practice.  It ensures
   that your scripts will use the expected version of the software, regardless of
   newly installed software.  Failing to do this may jeopardize the reproducibility
   of your results!

Modules need not be loaded one by one; two or more 'load' commands
can be combined as follows::

   $ module load Boost/1.81.0-GCC-12.2.0 Python/3.10.8-GCCcore-12.2.0

This will load the two modules and, automatically, the respective
toolchains with just one command.

.. warning::

   Do *not* load modules in your ``.bashrc``, ``.bash_profile`` or ``.profile``,
   you *will* shoot yourself in the foot at some point.  Consider using
   :ref:`module collections <collections of modules>` ``restore`` as a command
   line alternative (so *not* in the shell initialization files either!).

.. warning::

   It is also recommended not to mix modules from e.g. ``intel`` toolchain, with
   modules from the ``foss`` toolchain, due to conflicting dependencies.


List loaded modules
~~~~~~~~~~~~~~~~~~~

Obviously, the user needs to keep track of the modules that are
currently loaded. After executing the above two load commands, the list
of loaded modules will be very similar to:

::

   $ module list
   Currently Loaded Modulefiles:
   1) cluster/genius/login         (S)   8) gzip/1.12-GCCcore-12.2.0        15) Tcl/8.6.12-GCCcore-12.2.0
   2) GCCcore/12.2.0                     9) lz4/1.9.4-GCCcore-12.2.0        16) SQLite/3.39.4-GCCcore-12.2.0
   3) zlib/1.2.12-GCCcore-12.2.0        10) zstd/1.5.2-GCCcore-12.2.0       17) GMP/6.2.1-GCCcore-12.2.0
   4) binutils/2.39-GCCcore-12.2.0      11) ICU/72.1-GCCcore-12.2.0         18) libffi/3.4.4-GCCcore-12.2.0
   5) GCC/12.2.0                        12) Boost/1.81.0-GCC-12.2.0         19) OpenSSL/1.1
   6) bzip2/1.0.8-GCCcore-12.2.0        13) ncurses/6.3-GCCcore-12.2.0      20) Python/3.10.8-GCCcore-12.2.0
   7) XZ/5.2.7-GCCcore-12.2.0           14) libreadline/8.2-GCCcore-12.2.0

It is important to note at this point that, e.g., ``XZ/5.2.7-GCCcore-12.2.0``
is also listed, although it was not explicitly loaded by the user. This is
because ``Boost/1.81.0-GCC-12.2.0`` depends on it, and the system administrator
specified that the ``GCCcore/12.2.0`` toolchain module that contains this
compiler should be loaded whenever this ``Boost`` module is loaded. There
are advantages and disadvantages to this, so be aware of automatically
loaded modules; whenever things go wrong, they may have something to do
with it!


Unloading modules
~~~~~~~~~~~~~~~~~

To unload a module, one can use the ``module unload`` command. It works
consistently with the ``load`` command, and reverses the latter's
effect. One can however unload automatically loaded modules manually, to
debug some problem.

::

   $ module unload Boost

Notice that the version was not specified: the module system is
sufficiently clever to figure out what the user intends. However,
checking the list of currently loaded modules is always a good idea,
just to make sure!


Purging modules
~~~~~~~~~~~~~~~

In order to unload all modules at once, and hence be sure to start with
a clean slate, use:

::

   $ module purge

.. note::

   It is a good habit to use this command in your job scripts, prior to loading
   the modules specifically needed by your applications. This
   ensures that no version conflicts occur if the user loads module using
   his ``.bashrc`` file (see the warning above).


Getting help
~~~~~~~~~~~~

To get a list of all available module commands, type:

::

   $ module help


.. _collections of modules:

Collections of modules
~~~~~~~~~~~~~~~~~~~~~~

Although it might seem convenient to set up your working environment
by loading modules in your ``.bashrc`` or ``.profile`` file, this
practice is error prone and you will end up shooting yourself in the
foot at some point.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The list of software available on a particular cluster can be
unwieldingly long and the information that ``module av`` produces can be
overwhelming. Therefore the administrators may have chosen to only show
the most relevant packages by default, and not show, e.g., packages that
aim at a different cluster, a particular node type or a less complete
toolchain. Those additional packages can then be enabled by loading
another module first. E.g., to get access to the modules in
the (at the time of writing) incomplete 2019a toolchain on UAntwerpen's
leibniz cluster, one should first enter

   ::

      $ module load leibniz/2019a-experimental
