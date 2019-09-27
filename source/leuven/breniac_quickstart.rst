Breniac quick start
===================

:ref:`Breniac <Breniac hardware>` is the VSC's Tier-1 cluster.

.. include:: tier1_hardware/breniac_login_nodes.rst


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
long queuing times.  For this purpose, 4 nodes have been reserved as debugging
nodes.  A few restrictions apply:

- you can only submit a single debug job at the time,
- the debug job can use at most 4 nodes, and
- the maximum walltime for a debug job is 1 hour.

To submit a job to run on the debug nodes, you have to specify the partition::

   $ qsub -l nodes=2:ppn=28:broadwell  -l walltime=2:00:00  l qos=debugging \
          -A myproject  myjobscript.pbs
