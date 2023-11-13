The module system
=================

Many software packages are installed as modules. These packages include
compilers, interpreters, mathematical software such as Matlab and SAS,
as well as other applications and libraries. 

All VSC sites have implemented a specific version of the module system
, called `Lmod`_. It is highly compatible with the standard
module system, but has some extra capabilities and some ifferences.
To interact with the module system the ``module`` command  or the handy shortcut command ``ml`` can be used.

.. _module system basics:

Using the module system
-----------------------

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
- ``<extra>``: additional suffix, ``Python-3.6.4``, the version of Python this Boost version
  was installed with.

If packages include something like ``intel-2021a`` or ``foss-2021a`` in their name,
means that these are packages installed with the 2021a versions of the :ref:`toolchains <toolchains>`
based on the Intel and GNU compilers respectively. The other packages do 
not belong to a particular toolchain. The name of the packages also
includes a version number (right after the /) and sometimes other
packages they need.


List loaded modules
~~~~~~~~~~~~~~~~~~~

To get an overview of the currently loaded modules, use ``module list``
or ``ml`` (without specifying extra arguments).


In a default environment, you should see a single ``cluster`` module
loaded:

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      By default the cluster module of the node where you are logged in is loaded.
      The cluster module will set the correct modulepath for the node on which you are logged in.

   .. tab-item:: UGent

      n a default environment, you should see a single cluster module loaded:

      ::

         $ ml
         Currently Loaded Modules:
         1) cluster/victini (S)
         Where:
         S:  Module is Sticky, requires --force to unload or purge

         (for more details on sticky modules, see the section on ``ml purge``)

         :ref:`lmod UGent <Lmod Gent>`

   .. tab-item:: UAntwerp (AUHA)

      ADD INFO

   .. tab-item:: VUB

      ADD INFO 


List available modules
~~~~~~~~~~~~~~~~~~~~~~

To view a list of available software packages, use the command
``module av``. The output will look similar to this:

::

   $ module av
   ---------------- /apps/leuven/rocky8/icelake/2022b/modules/all -----------------
   ATK/2.38.0-GCCcore-12.2.0                   (D)
   Armadillo/11.4.3-foss-2022b
   Autoconf/2.71-GCCcore-12.2.0
   Automake/1.16.5-GCCcore-12.2.0
   ...
   ---------------- /apps/leuven/rocky8/icelake/2021a/modules/all -----------------
   ABAQUS/2023-hotfix-2306
   ANTLR/2.7.7-GCCcore-10.3.0-Java-11
   ASE/3.22.0-intel-2021a
   ...
   zlib/1.2.11
   zlib/1.2.12
   zstd/1.4.9-GCCcore-10.3.0


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

For more comprehensive searches, you can use the Lmod specific ``module spider``, e.g.,

::

   $ module spider python

Note that ``spider`` is case-insensitive and looks for partial matches.
If you only need to look for the python modules, you can try to include / in the module search 

::

   $ module spider python/

Info on modules
~~~~~~~~~~~~~~~

If you search on the full modulename the ``spider`` subcommand will give you more information.
E.g.in which cluster module it is available, and what the included extensions are. E.g.

::

   $ module spider Python/3.9.5-GCCcore-10.3.0

   ----------------------------------------------------------------------------
   Python: Python/3.9.5-GCCcore-10.3.0
   ----------------------------------------------------------------------------
    Description:
      Python is a programming language that lets you work more quickly and
      integrate your systems more effectively.


    You will need to load all module(s) on any one of the lines below before the
    "Python/3.9.5-GCCcore-10.3.0" module is available to load.

      cluster/genius/amd
      cluster/genius/amd_long
      cluster/genius/batch
    ...

        Help:
      Description
      ===========
      Python is a programming language that lets you work more quickly and integrate your systems
       more effectively.


      More information
      ================
       - Homepage: https://python.org/


      Included extensions
      ===================
      alabaster-0.7.12, appdirs-1.4.4, asn1crypto-1.4.0, atomicwrites-1.4.0,
      attrs-21.2.0, Babel-2.9.1, bcrypt-3.2.0, bitstring-3.1.7, blist-1.3.6,
      CacheControl-0.12.6, cachy-0.3.0, certifi-2020.12.5, cffi-1.14.5,
      chardet-4.0.0, cleo-0.8.1, click-7.1.2, clikit-0.6.2, colorama-0.4.4,
      crashtest-0.3.1, cryptography-3.4.7, Cython-0.29.23, decorator-5.0.7,
      distlib-0.3.1, docopt-0.6.2, docutils-0.17.1, ecdsa-0.16.1, filelock-3.0.12,
      ...

More technical information can be obtained using the ``show`` sub-command.
It will show which other modules will be loaded and what environment paths will be set.

::

   $ module show Python/3.9.5-GCCcore-10.3.0

   ...
   load("GCCcore/10.3.0")
   load("binutils/2.36.1-GCCcore-10.3.0")
   load("bzip2/1.0.8-GCCcore-10.3.0")
   load("zlib/1.2.11-GCCcore-10.3.0")
   load("libreadline/8.1-GCCcore-10.3.0")
   ...
   prepend_path("CMAKE_PREFIX_PATH","/apps/leuven/rocky8/skylake/2021a/software/Python/3.9.5-GCCcore-10.3.0")
   prepend_path("CPATH","/apps/leuven/rocky8/skylake/2021a/software/Python/3.9.5-GCCcore-10.3.0/include")
   prepend_path("LD_LIBRARY_PATH","/apps/leuven/rocky8/skylake/2021a/software/Python/3.9.5-GCCcore-10.3.0/lib")
   prepend_path("LIBRARY_PATH","/apps/leuven/rocky8/skylake/2021a/software/Python/3.9.5-GCCcore-10.3.0/lib")
   ...



Loading modules
~~~~~~~~~~~~~~~

A module is loaded using the command ``module load`` with the name of
the package, e.g., with the above list of modules,

::

   $ module load zlib 

will load the default ``zlib`` module.

If multiple versions are installed; the ``module load`` command will automatically choose the
default version, which is typically, but not always, the most
recent version. In the above example,

::

    $ module av zlib

    ---------------------------------------------------- /apps/leuven/rocky8/icelake/2022b/modules/all -----------------------------------------------------
    zlib/1.2.12-GCCcore-12.2.0    zlib/1.2.12 (D)
    ---------------------------------------------------- /apps/leuven/rocky8/icelake/2021a/modules/all -----------------------------------------------------
    zlib-ng/2.0.6-GCCcore-10.3.0    zlib/1.2.11-GCCcore-10.3.0    zlib/1.2.11    zlib/1.2.12

    Where:
    D:  Default Module

shows that zlib/1.2.12 is the default.
``module load zlib`` in this case will load the module ``zlib/1.2.13``. This may not be the
module that you want if you're using the GNU compilers. In that case,
the user should specify a particular version, e.g.,

::

   $ module load zlib/1.2.12-GCCcore-12.2.0

.. note::

   Loading modules with explicit versions is considered best practice.  It ensures
   that your scripts will use the expected version of the software, regardless of
   newly installed software.  Failing to do this may jeopardize the reproducibility
   of your results!

Modules need not be loaded one by one; the two 'load' commands
can be combined as follows::

   $ module load  FFTW/3.3.9-intel-2021a  Boost/1.76.0-intel-compilers-2021.2.0  

This will load the two modules and, automatically, the respective
toolchains with just one command ::

   $ module list

   Currently Loaded Modules:
   1) cluster/wice/interactive               (S)
   2) GCCcore/10.3.0
   3) zlib/1.2.11-GCCcore-10.3.0
   4) binutils/2.36.1-GCCcore-10.3.0
   5) intel-compilers/2021.2.0
   6) numactl/2.0.14-GCCcore-10.3.0
   7) UCX/1.10.0-GCCcore-10.3.0
   8) impi/2021.2.0-intel-compilers-2021.2.0
   9) iimpi/2021a
   10) imkl/2021.2.0-iimpi-2021a
   11) intel/2021a
   12) FFTW/3.3.9-intel-2021a

It is important to note at this point that, e.g., ``iimpi/2021a`` is
also listed, although it was not loaded explicitly by the user. This is
because ``FFTW/3.3.9-intel-2021a`` depends on it, and the system administrator
specified that the ``intel`` toolchain module that contains this
compiler should be loaded whenever the ``FFTW/3.3.9-intel-2021a`` module is loaded. There
are advantages and disadvantages to this, so be aware of automatically
loaded modules whenever things go wrong: they may have something to do
with it!


.. warning::

   Do *not* load modules in your ``.bashrc``, ``.bash_profile`` or ``.profile``,
   you *will* shoot yourself in the foot at some point.  Consider using
   :ref:`module collections <collections of modules>` ``restore`` as a command
   line alternative (so *not* in the shell initialization files either!).




Unloading modules
~~~~~~~~~~~~~~~~~

To unload a module, one can use the ``module unload`` command. It works
consistently with the ``load`` command, and reverses the latter's
effect. One can however unload automatically loaded modules manually, to
debug some problem.

::

   $ module unload FFTW

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

   It is a good habit to use this command in SLURM scripts, prior to loading
   the modules specifically needed by applications in that job script. This
   ensures that no version conflicts occur if the user loads module using
   his ``.bashrc`` file.


.. note::

   In case the cluster you are working on is using cluster modules, these will
   not be unloaded. It defines some important environment variables that point 
   to the location of centrally installed software/modules, 
   and others that are required for submitting jobs and possibly interfacing with the cluster resource manager.
      

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

Conflicting modules
~~~~~~~~~~~~~~~~~~~ 

It is important to note that **only modules that are compatible with
each other can be loaded together. In particular, modules must be
installed either with the same toolchain as the modules that** are
already loaded, or with a compatible (sub)toolchain.

For example, once you have loaded one or more modules that were
installed with the ``intel/2022a`` toolchain, all other modules that you
load should have been installed with the same toolchain.

In addition, only **one single version** of each software package can be
loaded at a particular time. For example, once you have the
``Python/3.9.5-GCCcore-10.3.0`` module loaded, you can not load a
different version of Python in the same session/job script; neither
directly, nor indirectly as a dependency of another module you want to
load.


.. _specialized software stacks:

Specialized software stacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The list of software available on a particular cluster can be
unwieldingly long and the information that ``module av`` produces
overwhelming. Therefore the administrators may have chosen to only show
the most relevant packages by default, and not show, e.g., packages that
aim at a different cluster, a particular node type or a less complete
toolchain. Those additional packages can then be enabled by loading
another module first. E.g., to get access to the modules in 
the an incomplete toolchain 

   ::

      $ module load clustername/20XXa-experimental


.. _lmod_command_overview:

Overview module commands
~~~~~~~~~~~~~~~~~~~~~~~~

A very quick introduction to Lmod. Below you will find more details and
examples.

-  ``ml`` lists the currently loaded modules, and is equivalent with
   ``module list``
-  ``ml GCC/4.9.3`` loads the ``GCC/4.9.3`` module, and is equivalent
   with ``module load GCC/4.9.3``
-  ``ml -GCC`` unloads the currently loaded ``GCC`` module, and is
   equivalent with ``module unload GCC``
-  ``ml av gcc`` prints the currently available modules that match ``*gcc*``
   (case-insensitively), and is equivalent with ``module avail GCC`` or
   ``module avail gcc``
-  ``ml show GCC/4.9.3`` prints more information about the ``GCC/4.9.3``
   module, and is equivalent with ``module show GCC``
-  ``ml spider gcc`` searches (case-insensitive) for ``*gcc*`` in all
   available modules over all clusters
-  ``ml spider GCC/4.9.3`` show all information about the module
   ``GCC/4.9.3`` and on which clusters it can be loaded.
-  ``ml save mycollection`` stores the currently loaded modules to a
   collection
-  ``ml restore mycollection`` restores a previously stored collection
   of modules

