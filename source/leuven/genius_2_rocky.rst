.. _genius_t2_leuven:

Genius migration 2 Rocky8 
=========================
The :ref:`Genius <genius_hardware>` operating system will be changed from CentOS 7 to Rocky 8. This is the same OS as currently running on :ref:`wICE <wice_hardware>`. 
The migration will be done on September 25th.
Sofware installed on wICE is not impacted, because there is no change of OS on wICE.

.. note::

   Tests nodes are available. If you want to test your software or your conda environment you can do so.
   On the `VSC account page <www.account.vscentrum.be>`_ request access to the group ``lpt2_rocky8_pilot``
   submit jobs to the nodes by selecting the Slurm reservation for these nodes with the ``--reservation=genius_rocky8_pilot`` Slurm option.
   To switch to the modules that have already been reinstalled for Rocky 8, first execute::

      module load cluster/genius/batch
     
   for the CPU nodes (which are inside the ``batch`` partition), and::

      module load cluster/genius/gpu_p100
     
   for the GPU node (which is in the ``gpu_p100`` partition).
   This will set your module path to point to the new modules for Rocky 8.


.. _impact_on_central_software:

Impact on centrally managed installed modules
---------------------------------------------

Current Genius software needs to be reinstalled because depencenies on the OS libraries will break the existing software.
All centrally installed and used modules, starting from toolchain 2018a, will be re-installed (as far as possible). Older toolchains will not be migrated. 
Unused modules are not migrated automatically, but we stronly advise to use modules in the most recent toolchain (which is 2021a).

In order to make distiction between the old CentOS 7 and the new Rocky 8 software installations, an additional hierarchy level is added according to follwoing scheme::

   /apps/leuven/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}${VSC_ARCH_SUFFIX}/TOOLCHAIN_VERSION/modules/all

e.g. ::

   /apps/leuven/rocky8/skylake/2018a/modules/all 
  
This convention is in line with other VSC sites and will be used also on wICE and future clusters.

.. _impact_on_user_installed_software:

Impact on self compiled and installed software
----------------------------------------------
If you have installed a software yourself in your own account, it must be recompiled on Genius, with the new OS.

.. _impact_on_conda:

Impact on conda environments
----------------------------

The conda environment you installed might need reinstallations. If you already have a conda environment that works on wICE, it also should work on Genius after the migration.
If you only have a conda environment working on Genius, it's best to create a new conda installation. In this case, it is recommended to recreate your working environment for full compatibility. Best practice is to choose a new installation folder with explicit mention of the new OS, e.g. ::

   ${VSC_DATA}/miniconda3-rocky
  
Then, you can use the appropriate conda environment after the migration.


.. _running_jobs_on_genius:

Impact on running jobs on Genius
--------------------------------
In order to minimize impact on your jobscripts, the appropriate module path will be loaded by default at the start of your job. The new module path will now contain all toolchain versions, starting from 2018a.
If you have set a module path explicitly in your jobs script, you can remove it from your jobscript or change it to the module path for Rocky 8.


.. _check_available_software:

Check available software
~~~~~~~~~~~~~~~~~~~~~~~~
On the login node you will be able to load the different available modulepaths (only for experimentation, and not for actual computing). In order to do this in an easy manner, cluster modules have been created for each partition.
The follwoing cluster modules are available ::

   $ module load cluster/genius/batch

will set the modulepath for the modules that are applicable for the Genius ``batch`` partition ::

   $ module load cluster/wice/batch

will set the the modulepath of the wICE ``batch`` partition. When you do this on the login node you can examine wich modules are available with the regular commands, e.g.::

   $ module avail
   $ module spider cp2k

