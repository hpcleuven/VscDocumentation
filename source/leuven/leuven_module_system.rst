.. _leuven_module_system:

The module system on Leuven clusters
====================================

This page offers additional information about the module system used on the
HPC clusters hosted at KU Leuven.


.. _module_hierarchy:

Module organization
~~~~~~~~~~~~~~~~~~~

When a cluster is not completely homogeneous (for instance there are
differences regarding architecture or operating system between nodes), it is
important to use the appropriate modules in your jobs. Using a module that is
not suited for the node on which the job is running, can give suboptimal
performance or may even completely fail to work.

This is why modules are organized in different *software stacks*,
differentiated by the operating system, the architecture, and the toolchain
version. The good news is that in general you do not need to worry too much
about this, as in most cases the correct software stack will be made available
in a job automatically thanks to the *cluster* modules, as explained in the
:ref:`next section <cluster_modules>`.

If you are interested in more technical details, you can read the section on
:ref:`manually modifying the modulepath <manually_modifying_modulepath>`,
which is oriented towards advanced users.


.. _cluster_modules:

The cluster modules
~~~~~~~~~~~~~~~~~~~

Background: a given module will only be available if it is located inside a
directory contained in the ``$MODULEPATH`` environment variable.
This ``$MODULEPATH`` environment variable is a colon-separated list of
directories, and you can list all modules located inside those directories
with the ``module avail`` command. The different software stacks mentioned
earlier are located in different directories (see the
:ref:`next section <manually_modifying_modulepath>` for more details), so in
order to make sure you are loading modules from the appropriate software stack,
the ``$MODULEPATH`` variable needs to contain the appropriate paths for the
node where you want to use a module.

Because working with the different directories containing different software
stacks is cumbersome, we advise users to rely on the cluster module to set
the ``$MODULEPATH`` variable. The cluster module can be handled identically
as other modules, but instead of making executables or libraries available,
its only purpose is to set up your environment to make the correct modules
available. The cluster module is always available and you can see which
versions can be loaded by executing ``module avail cluster``.

On the login nodes and inside a job environment, the correct version of the
cluster module will be loaded automatically. This means that for these cases,
you do not need to take any special action: the modules from the appropriate
software stack will be the only ones available to you. There is hence no need
for ``module use/unuse`` commands in your jobscripts (unless you deal with an
exceptional case).

.. note::

   The appropriate cluster module is only loaded automatically inside a job
   environment and on the login nodes. In other cases (for example when you
   ssh directly into a node), you will need to first load a cluster module
   yourself in order to make the correct modules available.

.. warning::

   If your jobscript contains the command ``module --force purge``, the
   cluster module will be unloaded and your ``$MODULEPATH`` will not contain
   the directory with the appropriate software stack. It will be necessary to
   load the correct cluster module or set your ``$MODULEPATH`` in another way.
   This is why we advise to not use ``module --force purge`` in your jobs,
   unless you are well aware of the consequences. Note that it is ok to
   execute ``module purge``, since the cluster modules are
   :ref:`sticky <module_purge>`.

A common scenario is that you want to search through the installed modules for
a software package you need, while you are on a login node. There are two ways
this can be done. In the example below we assume the commands are executed on
a Genius login node. The software package that is used as an example is
called ``CP2K``.

The first option is to load the cluster module corresponding to the node where
you eventually want to use a certain software package. If you are planning to
run jobs on the wICE batch partition, the commmand is:

.. code-block:: shell

   $ module load cluster/wice/batch

Note that the previously loaded cluster module will be automatically unloaded:
at most one cluster module can be loaded at a time. Now you can search for
modules containing ``CP2K`` by executing (the search is not case sensitive):

.. code-block:: shell

   $ module avail CP2K
   -- /apps/leuven/rocky8/icelake/2021a/modules/all --
      CP2K/8.2-foss-2021a         Libint/2.6.0-GCC-10.3.0-lmax-6-cp2k
      CP2K/8.2-intel-2021a (D)    Libint/2.6.0-iimpi-2021a-lmax-6-cp2k
      Libint/2.6.0-intel-compilers-2021.2.0-lmax-6-cp2k (D)

A second approach to search for installed software, is to use the
``module spider`` command. In contrast to the ``module avail`` command, with
``module spider`` Lmod will not only search for available modules (meaning
modules inside directories included in the current value of ``$MODULEPATH``),
but additionally will take into account additional entries that would be added
to ``$MODULEPATH`` in case a cluster module would be loaded. An example is:

.. code-block::

   $ module spider CP2K
   -------------------------------------
     CP2K:
   -------------------------------------
   Description:
         CP2K is a freely available (GPL) program, ...
   Versions:
           CP2K/5.1-intel-2018a
           CP2K/6.1-foss-2018a
           CP2K/6.1-intel-2018a
           CP2K/7.1-foss-2019b
           CP2K/7.1-intel-2019b
           CP2K/8.2-foss-2021a
           CP2K/8.2-intel-2021a
   -------------------------------------
     For detailed information about a specific "CP2K" package (including how
     to load the modules) use the module's full name.
     Note that names that have a trailing (E) are extensions provided by other
     modules. For example:
        $ module spider CP2K/8.2-intel-2021a
   -------------------------------------

As suggested by the output, you can obtain more information about one
of the available versions of the ``CP2K`` module by executing:

.. code-block:: shell

   $ module spider CP2K/8.2-intel-2021a

   -------------------------------------
     CP2K: CP2K/8.2-intel-2021a
   -------------------------------------
       Description:
         CP2K is a freely available (GPL) program, ...


    You will need to load all module(s) on any one of the lines below before
    the "CP2K/8.2-intel-2021a" module is available to load

      cluster/genius/batch
      cluster/genius/batch_debug
      cluster/genius/batch_long
      ...
      cluster/wice/batch
      ...

This command shows which cluster modules will make the ``CP2K/8.2-intel-2021a``
module available. As discussed earlier, loading ``cluster/wice/batch`` is one
example of a cluster module that suffices to make ``CP2K/8.2-intel-2021a``
available. For more information about ``module spider``, have a look at the
`Lmod documentation page <https://lmod.readthedocs.io/en/latest/135_module_spider.html>`__

.. note::

   In contrast to previous behavior, modules from different toolchain versions
   are now available automatically. On Genius, all modules since 2018a
   are available, and on wICE, all modules starting from 2021a. For a few
   legacy modules, installation is impossible on a recent operating system. In
   such a case, it is recommended to use a replacement module from a newer
   toolchain version. Alternatively you can consider to run your legacy
   software inside a container, but this is only the best option in some
   specific cases.


.. _manually_modifying_modulepath:

Manually modifying the modulepath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed in the previous section, the recommended approach to set your
``$MODULEPATH`` environment variable, is by using the cluster module. This
will make modules from the correct software stack available. It is however
also possible to manually modify the path where modules are searched.

Each software stack is located in a directory with the following hierarchical
structure::

   /apps/leuven/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}${VSC_ARCH_SUFFIX}/TOOLCHAIN_VERSION/modules/all

e.g.:

.. code-block:: shell

   /apps/leuven/rocky8/skylake/2018a/modules/all

This convention is in line with other VSC sites and will also be used on wICE
and future clusters. In order to add such a directory to your modulepath, the
following command can be used:

.. code-block:: shell

   module use /apps/leuven/rocky8/skylake/2018a/modules/all

To remove the entry again:

.. code-block:: shell

   module unuse /apps/leuven/rocky8/skylake/2018a/modules/all

Keep in mind that also ``/apps/leuven/common/modules/all`` is part of your
default ``$MODULEPATH``. This module collection is intended for packages which
have no operating system or toolchain dependencies. Typical examples are
packages which are distributed as precompiled binaries such as FLUENT.

.. _using_eessi_leuven:

Using modules from EESSI
~~~~~~~~~~~~~~~~~~~~~~~~

The `European Environment for Scientific Software Installations <https://www.eessi.io>`_
(EESSI, pronounced as "easy") provides an additional stack of scientific
software, next to installations which are done locally and located in the
``/apps/leuven`` directory. Compared to the local installations, the advantages
of EESSI for VSC users are:

* Since EESSI is a collaboration between many partners of the HPC community, a
  wide range of scientific software is readily available and can be streamed
  on-demand. This means users no longer need to wait for a support team to do
  the local installation, provided the required modules are
  `available in EESSI <https://www.eessi.io/docs/available_software/overview>`_.
* EESSI distributes software using the CernVM File System, which provides good
  performance when accessing software
* Because EESSI works on a large range of systems, including laptops, HPC
  clusters and cloud infrastructure, workflows making use of EESSI software
  are portable

If you want to know more details, you can have a look at the
`introductory EESSI documentation <https://www.eessi.io/docs/overview>`_. The
remainder of this section will focus on the practical aspects of using EESSI
on the VSC clusters.

Althought EESSI is installed on all nodes of the KU Leuven Tier-2 cluster,
the EESSI modules are not available by default and some commands need to be
run to set up EESSI in your session. Also note that modules from EESSI are not
compatible with locally installed modules, so the recommended commands to set
up EESSI first make the locally installed modules unavailable:

.. code-block:: shell

   # Force unload any cluster module
   module --force purge
   # Make EESSI available as a module
   export MODULEPATH=/cvmfs/software.eessi.io/init/modules/
   # Load an EESSI module
   module load EESSI/2023.06

These setup commands need to be executed in each session where you want to use
EESSI. Note that you can search for other EESSI versions by running
``module avail EESSI``. After loading the EESSI module, you can use the
``module`` commands as described above, but now those commands will interact
with the EESSI software stack instead of locally installed modules. For example:

.. code-block:: shell

   $ module avail PyTorch
   -- /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/icelake/modules/all --
      PyTorch/2.1.2-foss-2023a

As you can see, the path above the listed module indicates this module indeed
comes from EESSI. Also note how EESSI automatically figured out the most
appropriate module based on the architecture of the node where these commands
are executed.

If for any reason you want to switch back to locally installed modules, you
can execute the following commands:

.. code-block:: shell

   # Unload EESSI
   module purge
   # Restore your original modulepath
   export MODULEPATH=/apps/leuven/etc/modules:/apps/leuven/common/modules/all:/usr/share/lmod/lmod/modulefiles/Core
   # Restore the cluster module, the version depends on the node you are working on
   module load cluster/wice/batch

or simply start a new session on the cluster.
