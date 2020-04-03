Superdome quick start guide
===========================

The :ref:`Superdome <Superdome hardware>` is a shared memory machine, i.e.,
it can be used to run multi-threaded application that require large amounts
of RAM.


How to connect to Superdome?
----------------------------

Superdome does not have a dedicated login node, so in order to work with the
system users can connect to the same login node used for Genius.

.. include:: tier2_hardware/genius_login_nodes.rst

How to run a job on Superdome?
------------------------------

Jobs can be submitted from the login node, however, there are a few crucial
differences.  To submit jobs to Superdome you need to

- specify the partition ``superdome``,
- specify the queue ``qsuperdome``, and
- use ``-L`` for specifying resources.

The resource specification is specified in terms of ``tasks``, ``lprocs``
and ``place``.

``tasks``
   For Superdome, the number of tasks is always equal to 1.
``lprocs``
   The number of logical processors is essentially the number of cores
   you want to use for your job.
``place``
   The place determines where the logical processors are executed, and
   is ``numanode`` for Superdome.  Each ``numanode`` has 14 cores and 750 GB of
   RAM, so if you want to use, e.g., 28 cores, you would specify
   ``lprocs=28:place=numanode=2``.


For example::
  
   $ qsub  -l partition=superdome  -q qsuperdome  -L tasks=1:lprocs=42:place=numanode=3 \
           -A lp_myproject  my_job.pbs
  
Without specifying the ``superdome`` partition and ``qsuperdome`` queue, your jobs
will be submitted to Genius, and will probably not be able to start, since the
resources you specify are not available.


.. note::

   When submitting to Superdome no explicit memory request should be added.
   Memory will scale with the number of NUMA-nodes. You will have exclusive
   access to the memory of the requested NUMA-nodes. The Superdome has 8
   NUMA-nodes, so if you want 1/8th of the Superdome's memory (750 GB) you
   have to request ``lprocs=14:place=numanode=1``. If you want to use 1/4th
   (1.5 TB), your request should state ``lprocs=28:place=numanode=2``, for
   3/4th of the memory (4.5 TB), you would use ``lprocs=84:place=numanode=6``,
   and so on.


If your application requires fewer cores than the 14 a NUMA-node has, but
you need more memory than the default, you should specify that explicitely.
For instance, if you would have a sequential program that required 500 GB of
RAM, you would use ``-L tasks=1:lprocs=1:place=numanode=1:memory=500gb``.

However, keep in mind that if the memory you require exceeds that of a
NUMA-node, you would have to request multiple nodes to accommodate for
the total amount of memory.  For example, if a sequential program would
require 1 TB of RAM, you would specify:
``-L tasks=1:lprocs=1:place=numanode=2:memory=1tb``.

More documentation on the ``-L`` NUMA-aware resource specification can be
found in the vendor's `documentation
<http://docs.adaptivecomputing.com/9-0-3/MWM/Content/topics/NUMA/-Lresource.htm>`_.
