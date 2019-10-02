Breniac quick start
===================

:ref:`Breniac <Breniac hardware>` is the VSC's Tier-1 cluster.

.. include:: tier1_hardware/breniac_login_nodes.rst


Building/using software
-----------------------

Since Breniac has two types of architectures, some care needs to be taken
when building software, or selecting software to run.  The newer skylake
CPUs support the AVX-512 instruction set, which improves vectoriazation
oncsiderably.  Both skylake and broadwell nodes support AVX2.

Computationally intensive software is best compiled with archtecture-specific
optimizations.  The software stack typically has versions optimized for the
two architectures, and the appropriate packages for an architecture are
the default on nodes with that architecture.

If you want to, e.g., check the availability of software for a different
architecture from the node you are currenly on, you can do that by adding
the appropriate module path, i.e.,

- for broadwell::

     $ module use /apps/leuven/broadwell/2018a/modules/all

- for skylake::

     $ module use /apps/leuven/skylake/2018a/modules/all

The compile options to use for a specific architecture, or to build a fat
binary (Intel only) are listed in the documentation on the :ref:`foss
toolchain <FOSS toolchain>` and the :ref:`Intel toolchain <Intel toolchain>`.

.. note::

   Please run a (:ref:`interactive <interactive jobs>`) job to do builds on nodes
   with the target architectures.  This is best practice in any case since software
   builds tax the shared login nodes, and may disrupt the work of other users.


Running jobs
------------

The way you submit jobs on Breniac is similar to what you are used to on VSC Tier-2
infrastructure, you can review the :ref:`documentation for a refresher <submitting jobs>`
if necessary.

.. warning::

   On Breniac an accounting system is used, so you need to specify a project using
   ``qsub``'s ``-A`` option.  If you are not familiar with a credit system,
   please read the :ref:`documentation on credit system <credit system basics>`.

.. note::

   Since we use a routing queue on Breniac, you are advised not to explicitly
   specify a queue using the ``-q`` option, but rather to simply specify the
   required walltime (at most 3 days).

There are several types of nodes in the Breniac cluster: compute nodes with skylake
CPUs, and nodes with broadwell CPUs.  The latter have either 128 or 256 GB RAM.  See
the documentation on :ref:`Breniac hardware <Breaniac hardware>` for details.


.. _submit to Breniac skylake node:

Submit to a skylake node
~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a skylake compute node it all boils down to specifying the required
number of nodes and cores, and desired feature. As the nodes have a single job
policy we recommend to always request all available cores per node (28 cores in
this case). For example to request 2 nodes with each 28 cores you can submit
like this::

   $ qsub -l nodes=2:ppn=28:skylake  -l walltime=2:00:00  -A myproject  myjobscript.pbs


.. _submit to Breniac broadwell node:

Submit to a broadwell node
~~~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a broadwell compute node in case you don't care whether the job ends
up on nodes with 128 or 256 GB RAM, you specify the required number of nodes and
cores, and desired feature. As the nodes have a single job policy we recommend to
always request all available cores per node (28 cores in this case). For example
to request 2 nodes with each 28 cores you can submit
like this::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  -A myproject  myjobscript.pbs

If you want to make sure your job will run on nodes with 128 GB RAM, you
add a feature specification::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  -l feature=mem128 \
          -A myproject  myjobscript.pbs


.. _submit to Breniac 256 GB broadwell node:

Submit to a 256 GB broadwell node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a broadwell compute node that has 256 GB RAM, you specify the required
number of nodes and cores, and desired feature. As the nodes have a single job policy
we recommend to always request all available cores per node (28 cores in this case).
For example to request 2 nodes with each 28 cores you can submit like this::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  -l feature=mem256 \
          -A myproject  myjobscript.pbs


Debug jobs on Breniac
---------------------

Debugging an application on a busy cluster can sometimes pose a problem due to
long queuing times.  For this purpose, 4 broadwell nodes have been reserved as
debugging nodes.  A few restrictions apply:

- you can only submit a single debug job at the time,
- the debug job can use at most 4 nodes, and
- the maximum walltime for a debug job is 1 hour.

To submit a job to run on the debug nodes, you have to specify the partition::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  l qos=debugging \
          -A myproject  myjobscript.pbs

