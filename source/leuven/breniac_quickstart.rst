Breniac quick start guide
=========================

:ref:`Breniac <Breniac hardware>` is the VSC's Tier-1 cluster.

.. include:: tier1_hardware/breniac_login_nodes.rst


Building/using software
-----------------------

Since Breniac has two types of architectures, some care needs to be taken
when building software, or selecting software to run.  The newer skylake
CPUs support the AVX-512 instruction set, which improves vectorization
considerably.  Both skylake and broadwell nodes support AVX2.

Computationally intensive software is best compiled with architecture-specific
optimizations.  The software stack typically has versions optimized for the
two architectures, and the appropriate packages for an architecture are
the default on nodes with that architecture.

If you want to, e.g., check the availability of software for a different
architecture from the node you are currently on, you can do that by adding
the appropriate module path, i.e.,

- for broadwell::

     $ module use /apps/leuven/broadwell/2018a/modules/all

- for skylake::

     $ module use /apps/leuven/skylake/2018a/modules/all

The compile options to use for a specific architecture, or to build a fat
binary (Intel only) are listed in the documentation on the :ref:`foss
toolchain <FOSS toolchain>` and the :ref:`Intel toolchain <Intel toolchain>`.

.. note::

   Please run a (:ref:`interactive <interactive jobs>`) job to do builds
   on nodes with the target architectures.  This is best practice in any
   case since software builds tax the shared login nodes, and may disrupt
   the work of other users.


Running jobs
------------

The way you submit jobs on Breniac is similar to what you are used to
on VSC Tier-2 infrastructure, you can review the :ref:`documentation
for a refresher <submitting jobs>` if necessary.

.. warning::

   On Breniac an accounting system is used, so you need to specify a
   project using ``qsub``'s ``-A`` option.  If you are not familiar with
   a credit system, please read the :ref:`documentation on credit system
   <credit system basics>`.

The charge rate is the same for all nodes, i.e., 1 credit per node-day.

.. note::

   Since we use a routing queue on Breniac, you are advised not to explicitly
   specify a queue using the ``-q`` option, but rather to simply specify the
   required walltime (at most 3 days).

There are several types of nodes in the Breniac cluster: compute nodes
with skylake CPUs, and nodes with broadwell CPUs.  The latter have either
128 or 256 GB RAM.  See the documentation on :ref:`Breniac hardware
<Breaniac hardware>` for details.


.. _submit to Breniac skylake node:

Submit to a skylake node
~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a skylake compute node it all boils down to specifying the
required number of nodes and cores, and desired feature. As the nodes have
a single job policy we recommend to always request all available cores per
node (28 cores in this case). For example to request 2 nodes with each 28
cores you can submit like this::

   $ qsub -l nodes=2:ppn=28:skylake  -l walltime=2:00:00  \
          -A myproject  myjobscript.pbs


.. _submit to Breniac broadwell node:

Submit to a broadwell node
~~~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a broadwell compute node in case you don't care whether the
job ends up on nodes with 128 or 256 GB RAM, you specify the required
number of nodes and cores, and desired feature. As the nodes have a single
job policy we recommend to always request all available cores per node (28
cores in this case). For example to request 2 nodes with each 28 cores you
can submit like this::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  \
          -A myproject  myjobscript.pbs

If you want to make sure your job will run on nodes with 128 GB RAM, you
add a feature specification::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  -l feature=mem128  \
          -A myproject  myjobscript.pbs


.. _submit to Breniac 256 GB broadwell node:

Submit to a 256 GB broadwell node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To submit to a broadwell compute node that has 256 GB RAM, you specify the
required number of nodes and cores, and desired feature. As the nodes have
a single job policy we recommend to always request all available cores per
node (28 cores in this case).  For example to request 2 nodes with each 28
cores you can submit like this::

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

To submit a job to run on the debug nodes, you have to specify the Quality
Of Service (``qos``)::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  -l qos=debugging \
          -A myproject  myjobscript.pbs



Job communication and network islands
-------------------------------------

Breniac's interconnect is partitioned into islands. The communication
latency will be minimal for nodes that are part of the same island.

Hence if your job runs on less than 24 nodes (or 672 cores) you can
request that all nodes the job runs on are in the same island.  This
is done by specifying the ``singleisland`` feature::

   $ qsub -l nodes=20:ppn=28  -l walltime=2:00:00  -l feature=singleisland \
          -A myproject  myjobscript.pbs


Running on specific nodes/islands
---------------------------------

You can request that your job runs on specific nodes, islands or racks,
for, e.g., benchmarking purposes.

.. note::

   On a busy cluster this means that the queue time of your jobs may
   increase substantially, so only request specific nodes, islands or
   racks when you really need to.

Running jobs on specific nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run a job on node ``r13i03n1``, you would request::

   $ qsub -l nodes=r13i03n1:ppn=28  -l walltime=2:00:00  \
          -A myproject  myjobscript.pbs

To submit a job on multiple nodes, e.g., ``r13i03n1`` and ``r13i03n2``,
use the following syntax::

   $ qsub -l nodes=r13i03n1:ppn=28+r13i03n2:ppn=28  -l walltime=2:00:00  \
          -A myproject  myjobscript.pbs


Running jobs on specific islands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The islands are indicated on the visual representation of the
cluster in the :ref:`hardware documentation <Breniac hardware>`.  The
names of islands follow the pattern ``r<xx>i<yy>``, where ``<xx>`` is
the number of the rack, and ``<yy>`` depends on the rack.

- For ``<xx>`` is ``01`` to ``04``: ``<yy>`` is ``01``, ``11`` or ``23``.
- For ``<xx>`` is ``05``: ``<yy>`` is ``01`` or ``11``.
- For ``<xx>`` is ``06`` to ``09``: ``<yy>`` is ``01``, ``11`` or ``23``.
- For ``<xx>`` is ``11`` to ``r14``: ``<yy>`` is ``03`` or ``15``.
- For ``<xx>`` is ``15``: ``<yy>`` is ``03``.
- For ``<xx>`` is ``16`` to ``r19``: ``<yy>`` is ``03`` or ``15``.

To, e.g., run on island ``r16i15`` specify the resource request as::

   $ qsub -l nodes=10:ppn=28  -l walltime=2:00:00  -l feature=r16i15  \
          -A myproject  myjobscript.pbs

.. note::

   Not all islands have the same number of nodes, e.g., ``r01i01`` has
   20 nodes, while ``r01i11`` has 24.  Consult the :ref:`visual
   representation  of the cluster <Breniac hardware>` for an overview.


Running jobs on specific racks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For larger jobs that still fit within a single rack, you can specify
that rack as ``r<xx>`` where ``<xx>`` is ``01`` to ``09``, or ``11`` to
``19``.  For example, to request 40 nodes in ``r02``, you would
request::

   $ qsub -l nodes=40:ppn=28  -l walltime=2:00:00  -l feature=r02  \
          -A myproject  myjobscript.pbs

.. note::

   Not all racks have the same number of nodes, e.g., ``r01`` has
   68 nodes, while ``r12`` has 48.  Consult the :ref:`visual
   representation  of the cluster <Breniac hardware>` for an overview.
