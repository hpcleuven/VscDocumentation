.. _genius_2_rocky:

Genius migration to Rocky 8
===========================
The :ref:`Genius <genius hardware>` operating system will be changed from CentOS 7 to Rocky 8. This is the same OS as currently running on :ref:`wICE <wice hardware>`.
The migration will be done on September 25.
Sofware installed on wICE is not impacted, because there is no change of OS on wICE.

.. note::

   Tests nodes are available. If you want to test your software or your Conda environment you can do so as follows:

   On the `VSC account page`_, request access to the group ``lpt2_rocky8_pilot``.
   Once approved by the admins, you can submit jobs to the reserved Rocky 8 nodes by specifying the option ``--reservation=genius_rocky8_pilot``.
   To switch to the modules that have already been reinstalled for Rocky 8, first execute::

      module load cluster/genius/batch
     
   for the CPU nodes (which are inside the ``batch`` partition), and::

      module load cluster/genius/gpu_p100
     
   for the GPU node (which is in the ``gpu_p100`` partition).
   This will set your module path to point to the new modules for Rocky 8.


.. _impact_on_central_software:

Impact on centrally installed modules
-------------------------------------
Current Genius software needs to be reinstalled because dependencies on the OS libraries will break the existing software.
All centrally installed modules which have seen recent use, starting from 2018a toolchains, will be re-installed (as far as possible). Older toolchains will not be migrated.
Unused modules are not migrated automatically, but we strongly advise to use modules in the most recent toolchains (2021a).

In order to distinguish between the old CentOS 7 and the new Rocky 8 software installations, an additional level is introduced in the ``/apps`` hierarchy::

   /apps/leuven/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}${VSC_ARCH_SUFFIX}/TOOLCHAIN_VERSION/modules/all

e.g.::

   /apps/leuven/rocky8/skylake/2018a/modules/all 
  
This convention is in line with other VSC sites and will also be used on wICE and future clusters.


.. _impact_on_user_installed_software:

Impact on user-installed software
---------------------------------
If you have installed a software package yourself in your own account, and you did this on a Genius CentOS 7 node, it must be recompiled on Genius on a node with the new OS.
This can be done on one of the available test nodes. Please request access to the lpt2_rocky8_pilot group.

.. _impact_on_conda:

Impact on Conda environments
----------------------------
The Conda environment you installed might need reinstallations. If you already have a Conda environment that works on wICE, it also should work on Genius after the migration.
If you only have a Conda environment working on Genius, it's best to create a new Conda installation. In this case, it is recommended to recreate your environment for full compatibility with the new OS. Best practice is to choose a new installation folder with explicit mention of the new OS, e.g. ::

   ${VSC_DATA}/miniconda3-rocky
  
You can then use this Conda environment after the migration. You can prepare this on the test nodes.


.. _impact_on_starting_jobs:

Impact on starting jobs on Genius and wICE
------------------------------------------
In order to minimize the changes you need to make to your jobscripts, an appropriate module path (``$MODULEPATH``) will be set by default at the start of your job of the the migration of Genius to Rocky 8 OS. This new module path will now contain all toolchain versions, starting from 2018a on Genius and starting from 2021a on wICE. This is an important change! Previously the modulepath was set to a single toolchain, that would not change over time. You might have set a module path in your jobscripts to refer to newer toolchains.

.. note::

   If you have set a module path explicitly in your jobscript, you can remove it from your jobscript or change it to the module path for Rocky 8.



Using cluster modules
~~~~~~~~~~~~~~~~~~~~~

Instead of working with a single default, unchanging, modulepath, refering to a single default toolchain, a new approach is taken. Each cluster partition will have a so called cluster module that sets the ``$MODULEPATH`` that is valid for the specific nodes in the cluster partition. The cluster module will detect the underlying CPU architecture and uses this for setting the path correctly.


.. _check_available_software:

Check available software
~~~~~~~~~~~~~~~~~~~~~~~~
On the login node you will be able to load the different available cluster modules (only for experimentation, not for actual computing). In order to do this you can query the available cluster moduels with::

   $ module avail

this wil show the available cluster modules::

   --------------------------- /apps/leuven/etc/modules ---------------------------
   cluster/default
   cluster/genius/amd_long               (S)
   cluster/genius/amd                    (S)
   cluster/genius/batch_debug            (S)
   cluster/genius/batch_long             (S)
   cluster/genius/batch                  (S)
   ...
   cluster/wice/batch
   ...

Loading any of this modules on the login node::

   $ module load cluster/genius/batch

will set the module path for the modules that are applicable for the Genius ``batch`` partition::

   $ module load cluster/wice/batch

will set the the module path of the wICE ``batch`` partition. When you do this on the login node you can examine wich modules are available with the regular commands, e.g.::

   $ module avail
   $ module spider cp2k

