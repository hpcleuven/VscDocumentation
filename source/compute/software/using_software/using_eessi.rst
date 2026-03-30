.. _using-eessi:

Using EESSI
===========

The `European Environment for Scientific Software Installations <https://www.eessi.io>`_
(EESSI, pronounced as "easy") provides an additional stack of scientific
software, next to installations which are provided locally and located in the
``/apps/${VSC_INSTITUTE}`` directory. Compared to the local installations, the advantages
of EESSI for VSC users are:

* Since EESSI is a collaboration between many partners of the HPC community, a
  wide range of scientific software is readily available and can be streamed
  on-demand. This means users no longer need to wait for a support team to do
  the local installation, provided the required modules are
  `available in EESSI <https://www.eessi.io/docs/available_software>`_.
* EESSI distributes software using `CernVM-FS <https://cernvm.cern.ch/fs/>`_, which provides good
  performance when accessing software.
* Because EESSI works on a large range of systems, including laptops, HPC
  clusters and cloud infrastructure, workflows making use of EESSI software
  are portable.

If you want to know more details, you can have a look at the
`introductory EESSI documentation <https://www.eessi.io/docs/overview>`_. The
remainder of this section will focus on the practical aspects of using EESSI
on the VSC clusters.

.. note::

   You can check if EESSI is supported by executing ``ls /cvmfs/software.eessi.io``
   and verify it prints some files and directories. If on the other hand the
   command results in ``ls: cannot access '/cvmfs/software.eessi.io': No such file or directory``,
   this means EESSI is not supported.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: UAntwerpen
      :sync: ua

      EESSI is currently not (yet) available on the UAntwerpen clusters.

Althought EESSI is typically installed on all nodes of participating VSC clusters,
the modules for the software provided by EESSI are not available by default, and some commands need to be
run to set up EESSI in your session. Also note that modules from EESSI are not
compatible with locally installed modules, so the recommended commands to set
up EESSI first make the locally installed modules unavailable:

.. code-block:: shell

   # Force unload any cluster module
   module --force purge
   # Make EESSI available as a module
   unset MODULEPATH
   module use /cvmfs/software.eessi.io/init/modules/
   # Load an EESSI module
   module load EESSI/2025.06


These setup commands need to be executed in each session where you want to use
EESSI. Note that you can search for other EESSI versions by running
``module avail EESSI``. After loading the EESSI module, you can use the
``module`` commands as described in the section on
:ref:`module system basics <module_system_basics>`, but now those commands will interact
with the EESSI software stack instead of locally installed modules. For example:

.. code-block:: shell

   $ module av GROMACS
   -- /cvmfs/software.eessi.io/versions/2025.06/software/linux/x86_64/intel/skylake_avx512/modules/all --
      GROMACS/2025.2-foss-2025a

As you can see, the path above the listed module indicates this module indeed
comes from EESSI. Also note how EESSI automatically figured out the most
appropriate module based on the architecture of the node where these commands
are executed.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      If for any reason you want to switch back to locally installed modules, you
      can execute the following commands:

      .. code-block:: shell

         # Unload EESSI
         module purge
         # Restore your original modulepath
         unset MODULEPATH
         module use /apps/leuven/etc/modules:/apps/leuven/common/modules/all:/usr/share/lmod/lmod/modulefiles/Core
         # Restore the cluster module, the version depends on the node you are working on
         module load cluster/wice/batch

      or simply start a new session on the cluster.

   .. tab-item:: UGent
      :sync: ug

      If for any reason you want to switch back to locally installed modules, you
      can execute the following commands:

      .. code-block:: shell

         # Unload EESSI
         module purge
         # Restore your original modulepath
         unset MODULEPATH
         module use /etc/modulefiles/vsc
         # Restore the cluster module, the version depends on the node you are working on
         module load cluster/doduo

      or simply start a new session on the cluster.

   .. tab-item:: VUB
      :sync: vub

      If for any reason you want to switch back to locally installed modules, 
      simply start a new session on the cluster.


Additional links:

- Overview of available software: https://eessi.io/docs/available_software/
- Overview of systems where EESSI is available: https://eessi.io/docs/systems/
- Adding software to EESSI: https://eessi.io/docs/adding_software/overview/
- Building software on top of EESSI: https://www.eessi.io/docs/using_eessi/building_on_eessi/
- Using EESSI in CI environments like GitHub Actions: https://eessi.io/docs/using_eessi/eessi_in_ci/
- Recording of "Introduction to EESSI" talk (FOSDEM 2026, recorded 1 Feb 2026): https://www.youtube.com/watch?v=1AZZqhvQIgo
- EESSI trainings & events: https://www.eessi.io/docs/training-events/
- EESSI "Happy Hour" weekly community online meetings: https://eessi.io/docs/training-events/happy-hours-sessions/
