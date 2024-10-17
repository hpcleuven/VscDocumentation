.. _module_system_basics:

Module system basics
====================

Many software packages are installed as modules. These packages range from
compilers, interpreters and mathematical libraries to the actual scientific
software applications.

All VSC sites use a Lua based implementation called `Lmod`_. Interacting
with the module system happens via the ``module`` command  or its shorter
equivalent ``ml``.


Available modules
~~~~~~~~~~~~~~~~~

To view a list of available software packages, use the command
``module av``. The output will look similar to this:

::

   $ module av

   ---------------- /apps/leuven/rocky8/icelake/2023a/modules/all -----------------
   ATK/2.38.0-GCCcore-12.3.0                               (D)
   Armadillo/12.6.2-foss-2023a                             (D)
   Bison/3.8.2                                             (D)
   ...
   CP2K/2023.1-foss-2023a                                  (D)
   CP2K/2023.1-intel-2023a
   ...
   zlib/1.2.13                                             (D)

   ---------------- /apps/leuven/rocky8/icelake/2022b/modules/all -----------------
   ATK/2.38.0-GCCcore-12.2.0                               (D)
   ...


Module names
~~~~~~~~~~~~

In general, the anatomy of a module name is

::

   <package>/<version>-<toolchain>[-<extra>]

For e.g. ``GROMACS/2023.3-foss-2023a-PLUMED-2.9.0``, we have

- ``<package>``: GROMACS, the name of the software package,
- ``<version>``: 2023.3, the GROMACS Version,
- ``<toolchain>``: foss-2023a, the toolchain GROMACS was built with, and
- ``<extra>``: ``PLUMED-2.9.0``, the version of PLUMED this GROMACS installation
  can inter-operate with and will load as a dependency.

Toolchains such as ``intel-2023a`` or ``foss-2023a`` refer to the 2023a
versions of the :ref:`toolchains <toolchains>` based on the Intel and GNU
compilers respectively. Certain modules may not belong to a particular toolchain.

When different modules exist for the same package, for example because it has
been compiled with two different toolchains, please consider trying out the
different modules so as to choose the one that performs best for your workloads.


Searching for modules
~~~~~~~~~~~~~~~~~~~~~

Often, when looking for some specific software, you will want to filter
the list of available modules, since it tends to be rather large.
For a (case-insensitive) search for modules containing the word ``python``,
you can either try

::

   $ module av python

or, for a more comprehensive search

::

   $ module spider python


To restrict the search to modules where the package name ends with ``python``,
add a trailing slash (e.g. ``module av python/``).

.. note:

   The module command writes its output to standard error, rather than standard
   output. If you want to use pipes for filtering, consider using ``2>&1``
   or ``|&`` (e.g. ``module av |& grep -i python``).


Info on modules
~~~~~~~~~~~~~~~

The ``spider`` sub-command can also be used to provide information on a specific
module, e.g.

::

   $ module spider Python/3.11.3-GCCcore-12.3.0

   ----------------------------------------------------------------------------
   Python: Python/3.11.3-GCCcore-12.3.0
   ----------------------------------------------------------------------------
    Description:
      Python is a programming language that lets you work more quickly and
      integrate your systems more effectively.

      ...

      More information
      ================
       - Homepage: https://python.org/

      Included extensions
      ===================
      flit_core-3.9.0, packaging-23.1, pip-23.1.2, setuptools-67.7.2,
      setuptools_scm-7.1.0, tomli-2.0.1, typing_extensions-4.6.3, wheel-0.40.0


More technical information can be obtained using the ``show`` sub-command.
It will show which other modules will get loaded and in which ways various
environment variables (``PATH``, ``LD_LIBRARY_PATH``, ...) will be modified,
e.g.:

::

   $ module show Python/3.11.3-GCCcore-12.3.0


Loading modules
~~~~~~~~~~~~~~~

A module is loaded using the ``module load`` command, e.g.:

::

   $ module load CP2K

will load the default ``CP2K`` module (``CP2K/2023.1-foss-2023a`` in this
example).

If multiple versions are installed; the ``module load`` command will
automatically choose the default version, which is typically, but not always,
the most recent version. If, in this example, you would prefer to use same
version of CP2K but built with the ``intel-2023a`` toolchain, you would need
to specify:

::

   $ module load CP2K/2023.1-intel-2023a

.. note::

   Loading modules with explicit versions is considered as best practice. It ensures
   that your scripts will use the expected version of the software, regardless of
   newly installed software. Failing to do this may jeopardize the reproducibility
   of your results!

Modules need not be loaded one by one; two ``load`` sub-commands
can for example be combined as follows:

::

   $ module load CP2K/2023.1-foss-2023a GROMACS/2023.3-foss-2023a-PLUMED-2.9.0

.. warning::

   Do *not* load modules in your ``.bashrc``, ``.bash_profile`` or ``.profile``,
   you *will* shoot yourself in the foot at some point.  Consider using
   :ref:`module collections <collections of modules>` ``restore`` as a command
   line alternative (so *not* in the shell initialization files either!).


Conflicting modules
~~~~~~~~~~~~~~~~~~~

It is important to note that only modules that are compatible with
each other should be loaded together. The loaded modules should all
be associated with either the same toolchain or compatible (sub)toolchains
(see also https://docs.easybuild.io/common-toolchains/#toolchains_diagram).

For example, once you have loaded a module that uses the ``foss/2023a``
toolchain, all other modules that you load next should have been installed
with the same toolchain or with compatible (sub)toolchains such as
``GCCcore/12.3.0``, ``GCC/12.3.0`` and ``gompi/2023a``. Subtoolchains
compatible with e.g. ``intel/2023a`` include ``GCCcore/12.3.0``,
``intel-compilers/2023.1.0`` and ``iimpi/2023a``.

Additionally, two versions of the same software packages can not be loaded
together. If you e.g. loaded a ``Python/3.11.3-GCCcore-12.3.0`` module, then
also loading another ``Python`` module (either directly or as a dependency of
another module) will cause ``Python/3.11.3-GCCcore-12.3.0`` to be unloaded and
replaced by the new module (the same will happen to the modules which both
``Python`` modules load as dependencies).


List loaded modules
~~~~~~~~~~~~~~~~~~~

Obviously, the user needs to keep track of the modules that are
currently loaded. After executing the above load command, the list
of loaded modules will look similar to:

::

   $ module list
   Currently Loaded Modulefiles:
     1) cluster/wice/batch
     2) GCCcore/10.3.0
     ...
     16) OpenMPI/4.1.1-GCC-10.3.0
     17) OpenBLAS/0.3.15-GCC-10.3.0
     ...
     46) PLUMED/2.9.0-foss-2023a
     47) CP2K/2023.1-foss-2023a
     48) GROMACS/2023.3-foss-2023a-PLUMED-2.9.0

Note that this does not just show the two requested modules, but also all
the modules that got loaded automatically in order to satisfy (runtime)
dependencies of the explicitly loaded ``CP2K`` and ``GROMACS`` installations
(``PLUMED``, ``OpenMPI``, ``OpenBLAS``, etcetera).


Unloading modules
~~~~~~~~~~~~~~~~~

To unload a specific module, use the ``module unload`` command.
It works consistently with the ``load`` command, and reverses the latter's
effect. One can however unload automatically loaded modules manually, to
debug some problem.

::

   $ module unload CP2K

Notice that the version was not specified: the module system is
sufficiently clever to figure out what the user intends. However,
checking the list of currently loaded modules is always a good idea,
just to make sure.


.. _module_purge:

Purging modules
~~~~~~~~~~~~~~~

In order to unload all modules at once and start with a clean slate, use:

::

   $ module purge

This will not unload so-called `sticky modules
<https://lmod.readthedocs.io/en/latest/240_sticky_modules.html>`__, which
are special modules that do not normally need to be unloaded (for example
because they define the appropriate module paths and possibly other environment
variables). If really needed, sticky modules can be unloaded with
``module --force purge``.


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

         $ module load matplotlib/3.7.2-gfbf-2023a
         $ module load MATLAB/2023b

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

