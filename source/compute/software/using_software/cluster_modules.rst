.. _cluster_modules_general:

Cluster modules
===============

Background
~~~~~~~~~~

It is common for HPC clusters to be heterogeneous, meaning there are
differences regarding architecture or operating system between nodes. In that
case it is important to use modules appropriate for the nodes in your job.
Using a module that is not suited for the node on which the job is running,
can give suboptimal performance or may even completely fail to work.

This is why modules are organized in different *software stacks*,
differentiated by (at least) the operating system and the architecture.
The good news is that in general you do not need to worry too much
about this, as in most cases the correct software stack will be made available
in a job automatically. On some VSC sites, this happens through the use of
*cluster* modules, as explained in the :ref:`next section <cluster_modules>`.

If you are interested in more technical details, you can read the section on
:ref:`manually modifying the modulepath <manually_modifying_modulepath>`,
which is oriented towards advanced users.


.. _cluster_modules:

The ``cluster`` modules
~~~~~~~~~~~~~~~~~~~~~~~

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      This site makes use of ``cluster`` modules.

   .. tab-item:: UAntwerpen
      :sync: ua

      This site does *not* make use of ``cluster`` modules, the following section
      is not relevant.

   .. tab-item:: UGent
      :sync: ug

      This site makes use of ``cluster`` modules.

   .. tab-item:: VUB
      :sync: vub

      This site makes use of ``cluster`` modules, but not to set the
      ``$MODULEPATH`` variable. The following section is thus irrelevant.


A given module will only be available if it is located inside a
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
stacks is cumbersome, we advise users to rely on a ``cluster`` module to set
the ``$MODULEPATH`` variable on VSC sites with support for ``cluster`` modules.
The ``cluster`` module can be handled identically as other modules, but instead
of making executables or libraries available, its only purpose is to set up
your environment to make the correct modules available. Cluster modules are
always available and you can see which versions can be loaded by executing
``module avail cluster/``. The anatomy of the name of a ``cluster`` module is

::

   cluster/<cluster_name>/<partition_name>

or

::

   cluster/<cluster_name>

A few examples are ``cluster/wice/batch``, ``cluster/wice/gpu_h100``,
``cluster/shinx`` and ``cluster/dodrio/gpu_rome_a100_rhel9``.

On the login nodes and inside a job environment, the correct version of the
``cluster`` module will be loaded automatically.
This means that for these cases, you do not need to take any special action:
the modules from the appropriate software stack will be the only ones available
to you. There is hence no need for ``module use/unuse`` commands in your
jobscripts (unless you deal with an exceptional case).

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Make sure to include ``#!/bin/bash -l`` as the shebang at the top of
      your jobscript as explained :ref:`here <leuven_job_shell>`. This is
      required to load the correct ``cluster`` module.

      The appropriate ``cluster`` module is only loaded automatically inside a job
      environment and on the login nodes. In other cases (for example when you
      ssh directly into a node), you will need to first load a ``cluster`` module
      yourself in order to make the correct modules available.

   .. tab-item:: UGent
      :sync: ug

      Note that the ``cluster`` module will always remain
      loaded, since it defines some important environment variables that point
      to the location of centrally installed software/modules, and others that
      are required for submitting jobs and interfacing with the cluster
      resource manager ( ``qsub``, ``qstat``, ...).

.. warning::

   If your jobscript contains the command ``module --force purge``, the
   ``cluster`` module will be unloaded and your ``$MODULEPATH`` will not contain
   the directory with the appropriate software stack. It will be necessary to
   load the correct ``cluster`` module or set your ``$MODULEPATH`` in another way.
   This is why we advise to not use ``module --force purge`` in your jobs,
   unless you are well aware of the consequences. Note that it is ok to
   execute ``module purge``, since the ``cluster`` modules are
   :ref:`sticky <module_purge>`.

.. _searching_for_software:

Searching for software
~~~~~~~~~~~~~~~~~~~~~~


.. _searching_for_software:

Searching for software
~~~~~~~~~~~~~~~~~~~~~~

A common scenario is that you want to search through the installed modules for
a software package you need, while you are on a login node. There are two ways
this can be done. The software package that is used as an example is called
``CP2K``.

The first option is to load the ``cluster`` module corresponding to the node where
you eventually want to use a certain software package.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      If you are planning to run jobs on the wICE batch partition, the commmand is
      ``module load cluster/wice/batch``. Note that the previously loaded cluster
      module will be automatically unloaded: at most one ``cluster`` module can be
      loaded at a time.

   .. tab-item:: UGent
      :sync: ug

      If you are planning to run jobs on the donphan cluster, the command is
      ``module swap cluster/donphan``. The ``swap`` command makes sure the
      previously loaded ``cluster`` module is unloaded.

Now you can search for modules containing ``CP2K`` by executing (the search is
done *case insensitive*):

.. code-block:: shell

   $ module avail cp2k 
   -- /apps/leuven/rocky9/icelake/2021a/modules/all --
      CP2K/8.2-foss-2021a         Libint/2.6.0-GCC-10.3.0-lmax-6-cp2k
      CP2K/8.2-intel-2021a (D)    Libint/2.6.0-iimpi-2021a-lmax-6-cp2k
      Libint/2.6.0-intel-compilers-2021.2.0-lmax-6-cp2k (D)

A second approach to search for installed software, is to use the
``module spider`` command. In contrast to the ``module avail`` command, with
``module spider`` Lmod will not only search for available modules (meaning
modules inside directories included in the current value of ``$MODULEPATH``),
but additionally will take into account additional entries that would be added
to ``$MODULEPATH`` in case a ``cluster`` module would be loaded. An example is:

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

This command shows which ``cluster`` modules will make the ``CP2K/8.2-intel-2021a``
module available. As discussed earlier, loading ``cluster/wice/batch`` is one
example of a ``cluster`` module that suffices to make ``CP2K/8.2-intel-2021a``
available. For more information about ``module spider``, have a look at the
`Lmod documentation page <https://lmod.readthedocs.io/en/latest/135_module_spider.html>`__
or the :ref:`page about the basics of modules <module_system_basics>`.


.. _manually_modifying_modulepath:

Manually modifying the modulepath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed in the previous section, the recommended approach to set your
``$MODULEPATH`` environment variable is by using the ``cluster`` module on VSC
sites supporting it. This will make modules from the correct software stack
available. It is however also possible to manually modify the path where
modules are searched. This is however only recommended in special use cases
for advanced users.

Each software stack is located in a directory whose name typically involves
environment variables such as ``$VSC_INSTITUTE_LOCAL``, ``$VSC_OS_LOCAL``,
``$VSC_ARCH_LOCAL`` and ``$VSC_ARCH_SUFFIX``. Some details differ between
VSC sites and the best approach is to check the content of the ``$MODULEPATH``
variable for the structure. A few examples are given below:

.. code-block:: shell

   /apps/leuven/rocky9/icelake/2025a/modules/all
   /apps/gent/RHEL9/zen2-ib/modules/all
   /apps/antwerpen/modules/rocky9/software-zen2/2025a/all
   /apps/brussel/RL9/zen2-ib/modules/2025a/all

In order to add such a software stack to your modulepath, the
``module use`` command can be used:

.. code-block:: shell

   module use /apps/leuven/rocky9/icelake/2025a/modules/all

To remove the entry again:

.. code-block:: shell

   module unuse /apps/leuven/rocky9/icelake/2025a/modules/all

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Keep in mind that also ``/apps/leuven/common/modules/all`` is part of your
      default ``$MODULEPATH``. This module collection is intended for packages which
      have no operating system or toolchain dependencies. Typical examples are
      packages which are distributed as precompiled binaries such as FLUENT.
