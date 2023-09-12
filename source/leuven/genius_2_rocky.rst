.. _genius_2_rocky:

Migration of Genius to Rocky 8
==============================

The operating system on :ref:`Genius <genius hardware>` nodes will be updated
from CentOS 7 to Rocky 8, the same operating system that is currently
running on :ref:`wICE <wice hardware>` nodes. This update is strictly
necessary because CentOS 7 will be
`discontinued <https://www.redhat.com/en/engage/migrate-from-centos-20230404>`__
and this poses security concerns. We have tried to make the migration as
transparently as possible for users, but still there are a few changes to take
into account. The first important item is that the way you can search for and
load modules has changed. This probably affects all users and you are urged
to carefully read the section on :ref:`centrally installed modules <impact_on_central_software>`.
The second item is that users that installed their own software (this includes
conda environments), will need to reinstall the software for the new OS. More
details are outlined :ref:`below <impact_on_user_installed_software>`. If you
still encounter problems *after* reading this documentation page, you can
contact the :ref:`support team <user support VSC>`.

.. note::

   Until the migration takes place on September 25, some test nodes are
   available. If you want to test your software or your Conda environment
   you can do so as follows:

   On the `VSC account page`_, request access to the group ``lpt2_rocky8_pilot``.
   Once approved by the admins, you can submit jobs to the reserved Rocky 8
   nodes by specifying the option ``--reservation=genius_rocky8_pilot`` to
   your submit command.


.. _impact_on_central_software:

Searching and loading centrally installed modules
-------------------------------------------------

Introduction
~~~~~~~~~~~~

A lot of scientific software is centrally available on the VSC clusters. To
avoid conflicts between different software packages, the installations are
offered as modules (specifically, the `Lmod system <https://lmod.readthedocs.io/en/latest/>`__
is used). The executables, libraries, headers, ... of a certain module can only
be used after that module has been loaded. By loading a certain set of modules,
you can easily set up an environment that has precisely the software you need.

When an HPC cluster is not completely homogeneous (for instance there are
differences regarding architecture or operating system between nodes), it is
important to use the appropriate modules in your jobs. Using a module that is
not suited for the node on which the job is running, can give suboptimal
performance, or even completely fail to work. This is why modules are
organized in different *software stacks*, differentiated by the operating
system, the architecture, and the toolchain version. The good news is that in
general you do not need to worry too much about this, as in most cases the
correct software stack will be made available in a job automatically thanks
to the *cluster modules*, as explained in the :ref:`next section <cluster_module>`.
If you are interested in more technical details, you can read the section on
:ref:`manually modifying the modulepath <manually_modifying_modulepath>`,
which is oriented towards advanced users.

.. _cluster_module:

The cluster module
~~~~~~~~~~~~~~~~~~

One crucial point to understand, is that a module is *available* only if it is
located inside a directory contained in the ``$MODULEPATH`` environment
variable. The ``$MODULEPATH`` environment variable is a colon-separated list of
directories, and you can list all modules located inside those directories
with the ``module avail`` command. The different software stacks mentioned
earlier are located in different directories (see the
:ref:`next section <manually_modifying_modulepath>` for more details), so in
order to make sure you are loading modules from the appropriate software stack,
you need to make sure your ``$MODULEPATH`` variable contains the appropriate
paths for the node where you want to use a module.

Because working with the different directories containing different software
stacks is cumbersome, we advise users to rely on the *cluster* module to set
the ``$MODULEPATH`` variable. The *cluster* module can be handled identically
as other modules, but instead of making executables or libraries available,
its only purpose is to set up your environment to make the correct modules
available. The *cluster* module is always available and you can see which
versions can be loaded by executing ``module avail cluster``.

On the login nodes and inside a job environment, the correct version of the
cluster will be loaded automatically. This means that for these cases, you do
not need to take any special action: the modules from the appropriate software
stack will be the only ones available to you. As a result of this change, you
do not need to do ``module use/unuse`` in your jobscripts. Such lines can be
perfectly removed from your jobscript (unless you deal with an exceptional
case).

.. note::

   The appropriate cluster module is only loaded automatically inside a job
   environment and on the login nodes. In other cases (for example when you
   ssh directly into a node), you will need to first load a cluster module in
   order to make the correct modules available.

.. warning::

   If your jobscript contains the command ``module --force purge``, the
   cluster module will be unloaded and your ``$MODULEPATH`` will not contain
   the directory with the appropriate software stack. It will be necessary to
   load the correct cluster module or set your ``$MODULEPATH`` in another way.
   This is why we advise to not use ``module --force purge`` in your jobs,
   unless you are well aware of the consequences. Note that it is ok to
   execute ``module purge``, since the cluster module is a
   `sticky module <https://lmod.readthedocs.io/en/latest/240_sticky_modules.html>`__
   , which means it is not unloaded with ``module purge``.

A common scenario is that you want to search through the installed modules for
a software package you need, while you are on a login node. There are two ways
this can be done. In the example below we assume the commands are executed on
a Genius login node.

The first option is to load the cluster module corresponding to the node where
you eventually want to use a certain software package. If you are planning to
run jobs on the wICE batch partition, the commmand is:

.. code-block:: shell

   $ module load cluster/wice/batch

Note that the previously loaded cluster module will be automatically unloaded:
at most 1 cluster module can be loaded at a time. Now you can search for
modules containing `CP2K` by executing (the search is not case sensitive):

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

   $ module --ignore-cache spider CP2K
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

As suggested as part of the output, you can obtain more information about one
of the available versions of the CP2K module by executing:

.. code-block:: shell

   $ module spider CP2K/8.2-intel-2021a

   -------------------------------------
     CP2K: CP2K/8.2-intel-2021a
   -------------------------------------
       Description:
         CP2K is a freely available (GPL) program, ...


    You will need to load all module(s) on any one of the lines below before
    the "CP2K/8.2-intel-2021a" module is available to load

      cluster/genius/amd
      cluster/genius/amd_long
      cluster/genius/batch
      ...
      cluster/wice/batch
      ...

This command which cluster modules will make the ``CP2K/8.2-intel-2021a``
available. As discussed earlier, loading ``cluster/wice/batch`` is one example
of a cluster module that suffices to make ``CP2K/8.2-intel-2021a`` available.
For more information about ``module spider``, have a look at the
`Lmod documentation page <https://lmod.readthedocs.io/en/latest/135_module_spider.html>`__

.. note::

   In contrast to previous behavior, modules from different toolchain versions
   will now be available automatically. On Genius, all modules since 2018a
   will be available, and on wICE, all modules starting from 2021a. For a few
   legacy modules, installation is impossible on a recent operating system. In
   such a case, it is recommended to use a replacement module from a newer
   toolchain version.

.. _manually_modifying_modulepath:

Manually modifying the modulepath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed in the previous section, the recommended approach to set your
``$MODULEPATH`` environment variable so modules from the correct software
stack are available, is by using the cluster module. It is however also
possible to manually the path where modules are searched.

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

.. _impact_on_user_installed_software:

Impact on user-installed software
---------------------------------
If you have installed a software package yourself in your own account, and you
did this on a Genius CentOS 7 node, it must be recompiled on Genius on a node
with the new OS. This can be done on one of the available test nodes. Please
request access to the lpt2_rocky8_pilot group.

Conda environments
----------------------------
The Conda environment you installed might need reinstallations. If you already
have a Conda environment that works on wICE, it also should work on Genius
after the migration. If you only have a Conda environment working on Genius,
it is best to create a new Conda installation. In this case, it is recommended
to recreate your environment for full compatibility with the new OS. Best practice
is to choose a new installation folder with explicit mention of the new OS, e.g.::

   ${VSC_DATA}/miniconda3-rocky

In order to install miniconda in a new directory you can ::

   bash Miniconda3-latest-Linux-x86_64.sh -b -p $VSC_DATA/miniconda3-rocky
   export PATH="${VSC_DATA}/miniconda3-rocky/bin:${PATH}
