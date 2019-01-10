Setting up the environment using Lmod at the HPC-UGent clusters
===============================================================

| To set up your environment for using a particular (set of) software
  package(s), you can use the modules that are provided centrally.
| On the Tier-2 of UGent and VUB, interacting with the modules is done
  via `Lmod <\%22http://lmod.readthedocs.io/en/latest/\%22>`__ (since
  August 2016), using the ``module`` command or the handy shortcut
  command ``ml``.

Quick introduction
------------------

A very quick introduction to Lmod. Below you will find more details and
examples.

-  ``ml`` lists the currently loaded modules, and is equivalent with
   ``module list``
-  ``ml GCC/4.9.3`` loads the ``GCC/4.9.3`` module, and is equivalent
   with ``module load GCC/4.9.3``
-  ``ml -GCC`` unloads the currently loaded ``GCC`` module, and is
   equivalent with ``module unload GCC``
-  ``ml av gcc`` prints the currently available modules that match *gcc*
   (case-insensitively), and is equivalent with ``module avail GCC``
-  ``ml show GCC/4.9.3`` prints more information about the ``GCC/4.9.3``
   module, and is equivalent with ``module show GCC``
-  ``ml spider gcc`` searches (case-insensitive) for *gcc* in all
   available modules over all clusters
-  ``ml spider GCC/4.9.3`` show all information about the module
   ``GCC/4.9.3`` and on which clusters it can be loaded.
-  ``ml save mycollection`` stores the currently loaded modules to a
   collection
-  ``ml restore mycollection`` restores a previously stored collection
   of modules

Module commands: using ``module`` (or ``ml``)
---------------------------------------------

--------------

Listing loaded modules: ``module list`` (or ``ml``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get an overview of the currently loaded modules, use ``module list``
or ``ml`` (without specifying extra arguments).

In a default environment, you should see a single ``cluster`` module
loaded:

::

   $ ml
   Currently Loaded Modules:
     1) cluster/delcatty (S)
     Where:
      S:  Module is Sticky, requires --force to unload or purge

(for more details on sticky modules, see the section on ``ml purge``)

--------------

Searching for available modules: module avail (or ml av) and ml spider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Printing all available modules: module avail (or ml av)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get an overview of all available modules, you can use
``module avail`` or simply ``ml av``:

::

   $ ml av
   ----------------------------- /apps/gent/CO7/haswell-ib/modules/all -----------------------------
      ABAQUS/6.12.1-linux-x86_64           libXext/1.3.3-intel-2016a                  (D)
      ABAQUS/6.14.1-linux-x86_64    (D)    libXfixes/5.0.1-gimkl-2.11.5
      ADF/2014.02                          libXfixes/5.0.1-intel-2015a
      ...                                  ...

In the current module naming scheme, each module name consists of two
parts:

-  the part before the first ``/``, corresponding to the *software
   name*; and
-  the remainder, corresponding to the software *version*, the *compiler
   toolchain* that was used to install the software, and a possible
   *version suffix*

For example, the module name
``matplotlib/1.5.1-intel-2016a-Python-2.7.11`` will set up the
environment for using *matplotlib* version *1.5.1*, which was installed
using the ``intel/2016a`` compiler toolchain; the version suffix
``-Python-2.7.11`` indicates it was installed for Python version 2.7.11.

The ``(D)`` indicates that this particular version of the module is the
default, but we strongly recommend to *not* rely on this as the default
can change at any point. Usuall, the default will point to the latest
version available.

--------------

Searching for modules: ml spider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The (Lmod-specific) ``spider`` subcommand lets you search for modules
across all clusters.

If you just provide a software name, for example ``gcc``, it prints on
overview of all available modules for GCC.

::

   $ ml spider gcc
   ---------------------------------------------------------------------------------
     GCC:
   ---------------------------------------------------------------------------------
        Versions:
           GCC/4.7.2
           GCC/4.8.1
           GCC/4.8.2
           GCC/4.8.3
           GCC/4.9.1
           GCC/4.9.2
           GCC/4.9.3-binutils-2.25
           GCC/4.9.3
           GCC/4.9.3-2.25
           GCC/5.3.0
        Other possible modules matches:
           GCCcore
   ---------------------------------------------------------------------------------
     To find other possible module matches do:
         module -r spider '.*GCC.*'
   ---------------------------------------------------------------------------------
     For detailed information about a specific \"GCC\" module (including how to load the modules) use the module's full name.
     For example:
        $ module spider GCC/4.9.3
   ---------------------------------------------------------------------------------

Note that ``spider`` is case-insensitive.

If you use ``spider`` on a full module name like GCC/4.9.3-2.25 it will
tell on which cluster(s) that module available:

::

   $ ml spider GCC/4.9.3-2.25
   ---------------------------------------------------------------------------------
     GCC: GCC/4.9.3-2.25
   ---------------------------------------------------------------------------------
        Other possible modules matches:
           GCCcore
       You will need to load all module(s) on any one of the lines below before the \"GCC/4.9.3-2.25\" module
       is available to load.
         cluster/delcatty
         cluster/golett
         cluster/phanpy
         cluster/raichu
         cluster/swalot
       Help:
          The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada,
          as well as libraries for these languages (libstdc++, libgcj,...). - Homepage: http://gcc.gnu.org/
   ---------------------------------------------------------------------------------
     To find other possible module matches do:
         module -r spider '.*GCC/4.9.3-2.25.*'

This tells you that the module named ``GCC/4.9.3-2.25`` is available on
the clusters ``delcatty``, ``golett``, ``phanpy``, ``raichu`` and
``swalot``. It also tells you what the module contains and a URL to the
homepage of the software.

--------------

Available modules for a particular software package: module avail <name> (or ml av <name>)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To check which modules are available for a particular software package,
you can provide the software name to ``ml av``.

For example, to check which versions of IPython are available:

::

   $ ml av ipython
   ----------------------------- /apps/gent/CO7/haswell-ib/modules/all -----------------------------
   IPython/3.2.3-intel-2015b-Python-2.7.10    IPython/3.2.3-intel-2016a-Python-2.7.11 (D)

Note that the specified software name is treated case-insensitively.

Lmod does a *partial* match on the module name, so sometimes you need to
use ``/`` to indicate the end of the software name you are interested
in:

::

   $ ml av GCC/
   ----------------------------- /apps/gent/CO7/haswell-ib/modules/all -----------------------------
   GCC/4.9.2    GCC/4.9.3-binutils-2.25    GCC/4.9.3    GCC/4.9.3-2.25    GCC/5.3.0    GCC/6.1.0-2.25 (D)

--------------

Inspecting a module using module show (or ml show)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see how a module would change the environment, use ``module show`` or
``ml show``:

::

   $ ml show matplotlib/1.5.1-intel-2016a-Python-2.7.11
   ----------------------------- /apps/gent/CO7/haswell-ib/modules/all -----------------------------
   whatis(\"Description: matplotlib is a python 2D plotting library which produces publication quality figures in a variety of 
   hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python 
   and ipython shell, web application servers, and six graphical user interface toolkits. - Homepage: http://matplotlib.org \")
   conflict(\"matplotlib\")
   load(\"intel/2016a\")
   load(\"Python/2.7.11-intel-2016a\")
   load(\"freetype/2.6.2-intel-2016a\")
   load(\"libpng/1.6.21-intel-2016a\")
   prepend_path(\"LD_LIBRARY_PATH\",\"/apps/gent/CO7/haswell-ib/software/matplotlib/1.5.1-intel-2016a-Python-2.7.11/lib\")
   prepend_path(\"LIBRARY_PATH\",\"/apps/gent/CO7/haswell-ib/software/matplotlib/1.5.1-intel-2016a-Python-2.7.11/lib\")
   setenv(\"EBROOTMATPLOTLIB\",\"/apps/gent/CO7/haswell-ib/software/matplotlib/1.5.1-intel-2016a-Python-2.7.11\")
   setenv(\"EBVERSIONMATPLOTLIB\",\"1.5.1\")
   setenv(\"EBDEVELMATPLOTLIB\",\"/apps/gent/CO7/haswell-ib/software/matplotlib/1.5.1-intel-2016a-Python-2.7.11/easybuild/matplotlib-1.5.1-intel-2016a-Python-2.7.11-easybuild-devel\")
   prepend_path(\"PYTHONPATH\",\"/apps/gent/CO7/haswell-ib/software/matplotlib/1.5.1-intel-2016a-Python-2.7.11/lib/python2.7/site-packages\")
   setenv(\"EBEXTSLISTMATPLOTLIB\",\"Cycler-0.9.0,matplotlib-1.5.1\")
   help([[ matplotlib is a python 2D plotting library which produces publication quality figures in a variety of
    hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python
    and ipython shell, web application servers, and six graphical user interface toolkits. - Homepage: http://matplotlib.org

Note that both the direct changes to the environment as well as other
modules that will be loaded are shown.

If you're not sure what all of this means: don't worry, you don't have
to know; just load the module and try using the software.

--------------

Loading modules: module load <modname(s)> (or ml <modname(s)>)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To effectively apply the changes to the environment that are specified
by a module, use ``module load`` or ``ml`` and specify the name of the
module.

For example, to set up your environment to use matplotlib:

::

   $ ml matplotlib/1.5.1-intel-2016a-Python-2.7.11
   $ ml
   Currently Loaded Modules:
     1) cluster/delcatty                                    (S)  12) zlib/1.2.8-intel-2016a
     2) GCCcore/4.9.3                                          13) libreadline/6.3-intel-2016a
     3) binutils/2.25-GCCcore-4.9.3                            14) ncurses/6.0-intel-2016a
     4) icc/2016.1.150-GCC-4.9.3-2.25                          15) Tcl/8.6.4-intel-2016a
     5) ifort/2016.1.150-GCC-4.9.3-2.25                        16) SQLite/3.9.2-intel-2016a
     6) iccifort/2016.1.150-GCC-4.9.3-2.25                     17) Tk/8.6.4-intel-2016a-no-X11
     7) impi/5.1.2.150-iccifort-2016.1.150-GCC-4.9.3-2.25      18) GMP/6.1.0-intel-2016a
     8) iimpi/8.1.5-GCC-4.9.3-2.25                             19) Python/2.7.11-intel-2016a
     9) imkl/11.3.1.150-iimpi-8.1.5-GCC-4.9.3-2.25             20) freetype/2.6.2-intel-2016a
    10) intel/2016a                                            21) libpng/1.6.21-intel-2016a
    11) bzip2/1.0.6-intel-2016a                                22) matplotlib/1.5.1-intel-2016a-Python-2.7.11

Note that even though we only loaded a single module, the output of
``ml`` shows that a whole bunch of modules were loaded, which are
required dependencies for *matplotlib*, including both the *compiler
toolchain* that was used to install *matplotlib* (i.e. ``intel/2016a``,
and its dependencies) and the module providing the *Python* installation
for which *matplotlib* was installed (i.e.
``Python/2.7.11-intel-2016a``).

--------------

Conflicting modules
^^^^^^^^^^^^^^^^^^^

It is important to note that **only modules that are compatible with
each other can be loaded together. In particular, modules must be
installed either with the same toolchain as the modules that** are
already loaded, or with a compatible (sub)toolchain.

For example, once you have loaded one or more modules that were
installed with the ``intel/2016a`` toolchain, all other modules that you
load should have been installed with the same toolchain.

In addition, only **one single version** of each software package can be
loaded at a particular time. For example, once you have the
``Python/2.7.11-intel-2016a`` module loaded, you can not load a
different version of Python in the same session/job script; neither
directly, nor indirectly as a dependency of another module you want to
load.

See also `the topic \\"module conflicts\" in the list of key differences
with the previously used module system <\%22#module_conflicts\%22>`__.

--------------

Unloading modules: module unload <modname(s)> (or ml -<modname(s)>)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To revert the changes to the environment that were made by a particular
module, you can use ``module unload`` or ``ml -<modname>``.

For example:

::

   $ ml
   Currently Loaded Modules:
     1) cluster/golett (S)
   $ which gcc
   /usr/bin/gcc
   $ ml GCC/4.9.3
   $ ml
   Currently Loaded Modules:
     1) cluster/golett (S)   2) GCC/4.9.3
   $ which gcc
   /apps/gent/CO7/haswell-ib/software/GCC/4.9.3/bin/gcc
   $ ml -GCC/4.9.3
   $ ml
   Currently Loaded Modules:
     1) cluster/golett (S)
   $ which gcc
   /usr/bin/gcc

--------------

Resetting by unloading all modules: ml purge (module purge)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To reset your environment back to a clean state, you can use
``module purge`` or ``ml purge``:

::

   $ ml
   Currently Loaded Modules:
     1) cluster/delcatty                                    (S)  11) bzip2/1.0.6-intel-2016a
     2) GCCcore/4.9.3                                          12) zlib/1.2.8-intel-2016a
     3) binutils/2.25-GCCcore-4.9.3                            13) libreadline/6.3-intel-2016a
     4) icc/2016.1.150-GCC-4.9.3-2.25                          14) ncurses/6.0-intel-2016a
     5) ifort/2016.1.150-GCC-4.9.3-2.25                        15) Tcl/8.6.4-intel-2016a
     6) iccifort/2016.1.150-GCC-4.9.3-2.25                     16) SQLite/3.9.2-intel-2016a
     7) impi/5.1.2.150-iccifort-2016.1.150-GCC-4.9.3-2.25      17) Tk/8.6.4-intel-2016a-no-X11
     8) iimpi/8.1.5-GCC-4.9.3-2.25                             18) GMP/6.1.0-intel-2016a
     9) imkl/11.3.1.150-iimpi-8.1.5-GCC-4.9.3-2.25             19) Python/2.7.11-intel-2016a
    10) intel/2016a
   $ ml purge
   The following modules were not unloaded:
      (Use \"module --force purge\" to unload all):
     1) cluster/delcatty
   [15:21:20] vsc40023@node2626:~ $ ml
   Currently Loaded Modules:
     1) cluster/delcatty (S)

Note that, on HPC-UGent, the ``cluster`` module will always remain
loaded, since it defines some important environment variables that point
to the location of centrally installed software/modules, and others that
are required for submitting jobs and interfacing with the cluster
resource manager ( ``qsub``, ``qstat``, ...).

As such, you should **not** (re)load the ``cluster`` module anymore
after running ``ml purge``. See also `the topic on the purge command in
the list of key differences with the previously used module
implementation <\%22#module_load_cluster\%22>`__.

--------------

Module collections: ml save, ml restore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a set of modules that you need to load often, you can save
these in a *collection* (only works with Lmod).

First, load all the modules you need, for example:

::

   ml HDF5/1.8.16-intel-2016a GSL/2.1-intel-2016a Python/2.7.11-intel-2016a

Now store them in a collection using ``ml save``:

::

   $ ml save my-collection

Later, for example in a job script, you can reload all these modules
with ``ml restore``:

::

   $ ml restore my-collection

With ``ml savelist`` you can get a list of all saved collections:

::

   $ ml savelist
   Named collection list:
     1) my-collection
     2) my-other-collection

To inspect a collection, use ``ml describe``.

To remove a module collection, remove the corresponding entry in
``$HOME/.lmod.d``.

--------------

Lmod vs Tcl-based environment modules
-------------------------------------

In August 2016, we switched to
`Lmod <\%22https://www.tacc.utexas.edu/research-development/tacc-projects/lmod\%22>`__
as a modules tool, a modern alternative to the outdated & no longer
actively maintained `Tcl-based environment modules
tool <\%22http://modules.sourceforge.net\%22>`__.

Consult the `Lmod documentation web
site <\%22http://lmod.readthedocs.io/en/latest/\%22>`__ for more
information.

--------------

Benefits
~~~~~~~~

-  significantly more responsive module commands, in particular
   ``module avail``
-  a better and easier to use interface (e.g. case-insensitive
   ``avail``, the ``ml`` command, etc.)
-  additional useful features, like defining & restoring module
   collections
-  drop-in replacement for Tcl-based environment modules (existing Tcl
   module files do not need to be modified to work)
-  module files can be written in either Tcl or Lua syntax (and both
   types of modules can be mixed together)

--------------

Key differences
~~~~~~~~~~~~~~~

The switch to Lmod should be mostly transparent, i.e. **you should not
have to change your existing job scripts**.

Existing ``module`` commands should keep working as they were before the
switch to Lmod.

However, there are a couple of minor differences between Lmod & the old
modules tool you should be aware of:

-  module conflicts are *strictly* enforced
-  ``module purge`` does not unload the ``cluster`` module
-  ``modulecmd`` is not available anymore (only relevant for EasyBuild)

| 
| See below for more detailed information.

--------------

Module conflicts are strictly enforced
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Conflicting modules can no longer be loaded together*.

Lmod has been configured to report an error if any module conflict
occurs (as opposed to the default behaviour which is to unload the
conflicting module and replace it with the one being loaded).

Although it seemed like the old modules did allow for conflicting
modules to be loaded together, this was highly discouraged already since
it usually resulted in a broken environment. Lmod will ensure no changes
are made to your existing environment if a module that conflicts with an
already module is loaded.

If you do try to load conflicting modules, you will run into an error
message like:

::

   $ module load Python/2.7.11-intel-2016a
   $ module load Python/3.5.1-intel-2016a 
   Lmod has detected the following error:  Your site prevents the automatic swapping of modules with same name.
   You must explicitly unload the loaded version of \"Python\" before you can load the new one. Use swap (or an unload
   followed by a load) to do this:
      $ module swap Python  Python/3.5.1-intel-2016a
   Alternatively, you can set the environment variable LMOD_DISABLE_SAME_NAME_AUTOSWAP to \"no\" to re-enable same name

Note that although Lmod suggests to unload or swap, we recommend to try
and make sure you *only load compatible* modules together\ *, and
certainly*\ **not**\ *to define ``$LMOD_DISABLE_SAME_NAME_AUTOSWAP``.*

--------------

module purge does not unload the cluster module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Using ``module purge`` effectively resets your environment to a
  pristine *working* state, i.e. the ``cluster`` module *stays loaded*
  after the ``purge``.
| As such, it is no longer required to run ``module load cluster`` to
  restore your environment to a working state.

When you do run ``module load cluster`` when a ``cluster`` is already
loaded, you will see the following warning message:

::

   WARNING: 'module load cluster' has no effect when a 'cluster' module is already loaded.
   For more information, please see https://www.vscentrum.be/cluster-doc/software/modules/lmod#module_load_cluster

To change to another cluster, use ``module swap`` or ``ml swap``; for
example, to change your environment for the ``golett`` cluster, use
``ml swap cluster/golett``.

If you are frequently see the warning above pop up, you may have
something like this in your ``$VSC_HOME/.bashrc`` file:

::

   . /etc/profile.d/modules.sh
   module load cluster

If you do, please remove that, and include this *at the top* of your
``~/.bashrc`` file:

::

   if [ -f /etc/bashrc ]; then
           . /etc/bashrc
   fi

--------------

modulecmd is not available anymore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``modulecmd`` command is not available anymore, and has been replacd
by the ``lmod`` command.

| This is only relevant for EasyBuild, which has be to configured to use
  Lmod as a modules tool, since by default it expects that ``modulecmd``
  is readily available.
| For example:

::

   export EASYBUILD_MODULES_TOOL=Lmod

See `the EasyBuild
documentation <\%22http://easybuild.readthedocs.io/en/latest/Configuration.html#supported-configuration-types\%22>`__
for other ways of configuring EasyBuild to use Lmod.

You should not be using ``lmod`` directly in other circumstances, use
either ``ml`` or ``module`` instead.

Questions or problems
---------------------

In case of questions or problems, please do not hesitate to contact the
support HPC team. HPC-UGent support team can be reached via
`hpc@ugent.be <\%22mailto:hpc@ugent.be\%22>`__. The HPC-VUB support team
can be reached via `hpc@vub.ac.be <\%22mailto:hpc@ugent.be\%22>`__.

"
