.. _wice_t2_leuven_advanced:

===================
wICE advanced guide
===================

.. _wice_compilation:

Compiling software
------------------

The wICE compute nodes feature Intel processors nicknamed IceLake, which are
the successors of the SkyLake and CascadeLake architectures which you can find
on Genius. Although architectural differences are rather small, it is highly
recommended to compile a version of your code specifically for wICE. A good approach
to compile on any cluster (such as wICE) is to launch an interactive job (with the
``srun`` command).

Many dependencies you might need are centrally installed. The modules that are
optimized for wICE are available when the appropriate
:ref:`cluster module <cluster_module>` is loaded. In most cases this will
happen automatically, but in case of problems it is a good idea to check.

Similar to other VSC clusters, wICE supports two toolchain flavors:
:ref:`FOSS <FOSS toolchain>` and :ref:`Intel <Intel toolchain>`. For more
general information on software development on the VSC, have a look at this
:ref:`overview <software_development>`.

.. _wice_worker:

Worker
------

The :ref:`Worker framework <worker framework>`, which allows to conveniently
parameterize simulations, is available on wICE. An attention point is that
if you want to lauch Worker jobs from the Genius login nodes, you will need to
use a specific module:

.. code-block:: shell

    $ module load worker/1.6.12-foss-2021a-wice

If instead you want to launch Worker jobs from an interactive job running on
wICE, you can use the ``worker/1.6.12-foss-2021a`` module (but do make sure
this is the version installed *specifically* for wICE.

Also note that the Worker support for Slurm is not yet complete. Both
the ``-master`` option for ``wsub`` and the ``wresume`` tool currently
only work for PBS/Torque and hence should not be used in the case of Slurm.

All the resources furthermore need to be specified inside the Slurm script
used as input for Worker (passing resources via the command line is not
supported). Various examples can be found in a `development branch
<https://github.com/gjbex/worker/tree/development_slurm/examples/>`__.


.. _wice_conda:

Conda on wICE
-------------

As the hardware is different on Genius and wICE, we advise
to have two separate :ref:`Conda installations <conda for Python>` (one for each
cluster). The :ref:`interactive Slurm partition on wICE<submit to wice interactive node>` 
can be used as an equivalent of the Genius login nodes for wICE, making it suited 
for Conda environment management.

To select the correct Conda installation when you log in and at the
start of your jobs, you can set up your ``~/.bashrc`` file in the following way:

.. code-block:: shell
   
   case ${VSC_INSTITUTE_CLUSTER} in
       genius)
           export PATH="${VSC_DATA}/miniconda3/bin:${PATH}"
           ;;
        wice)
           export PATH="${VSC_DATA}/miniconda3-wice/bin:${PATH}"
           ;;
   esac

Also keep in mind that applying your ``~/.bashrc`` settings in your Slurm jobs
requires placing ``#!/bin/bash -l`` at the top of your Slurm jobscript,
as emphasized in the :ref:`Site-specific Slurm info page <leuven_job_shell>`.
