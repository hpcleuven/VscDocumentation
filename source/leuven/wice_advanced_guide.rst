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
optimized for wICE are available in ``/apps/leuven/icelake/2021a/modules/all``.
This directory has to be in the ``$MODULEPATH`` environment variable in order
to make those modules available. Normally this should happen automatically, but
in case of problems it is a good idea to check this. If for some reason it is
missing, it can be added by executing:

.. code-block:: shell

    $ module use /apps/leuven/icelake/2021a/modules/all

Note that in the future, newer versions of software will be compiled using
different toolchain versions. In order to use modules from different toolchain
versions, you can use:

.. code-block:: shell

    $ module use /apps/leuven/icelake/<toolchain-version>/modules/all

where valid choices for ``<toolchain-version`` look like ``2021a``, ``2022b``,
etc. Older versions of the toolchains will however not be provided because they
are not compatible with the new cluster. Please contact
:ref:`support <user support VSC>` if you run into problems arising from using
newer libraries than the ones provided on Genius.

.. note::

   If you are trying to write scripts that work on several VSC clusters, it can
   be handy to make use of environment variables like ``$VSC_ARCH_LOCAL``,
   which is set to the local architecture. As an example, the statement
   ``module use /apps/leuven/${VSC_ARCH_LOCAL}/2021a/modules/all`` will enable
   using skylake modules when you are on a Genius SkyLake node, icelake modules
   when you are on a wICE IceLake node, etc. Another environment variable that
   can be interesting is ``$VSC_INSTITUTE_CLUSTER``, which resolves to
   ``genius`` on Genius nodes and to ``wice`` on wICE nodes.

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

    $ module use /apps/leuven/skylake/2021a/modules/all
    $ module load worker/1.6.12-foss-2021a-wice

If instead you want to launch Worker jobs from an interactive job running on
wICE, you can use the ``worker/1.6.12-foss-2021a`` module (but do make sure
this is the version installed in a subdirectory of ``/apps/leuven/icelake``).

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
requires placing ``#!/bin/bash -l`` at the top of your Slurm jobscript, as
shown in the :ref:`wICE quick start guide <running jobs on wice>`.
