.. _genius_decommissioning:

Genius decommissioning
======================

Most remaining parts of :ref:`Genius <Genius hardware>` will be
decommissioned when we start the pilot phases for the
:ref:`Tier-2 Mindwell cluster <mindwell hardware>`. This should happen
towards end of April.

.. note::

   Starting from the second week of March, many nodes from the `batch*`
   and `interactive` partitions on Genius will already be blocked to allow
   large-scale benchmarks to run on the new cluster. You will still be able
   to send jobs to those Genius partitions, but they may spend more time in
   the queue because of the reduced capacity.

The decommissioning will consist of retiring the following hardware:

- all Cascadelake CPU nodes (`batch*` partitions)
- all Skylake CPU nodes (`interactive` and `bigmem*` partitions)
- all nodes in the `dedicated*` partitions
- Superdome (`superdome*` partitions)

If you are still using the Genius CPU partitions, be prepared to switch
to the :ref:`wICE <wICE hardware>` CPU partitions since the final
decommissioning of this hardware is drawing near (towards the end of March,
as mentioned above).

The P100 and V100 GPU nodes will be kept online for a longer period
(`gpu_p100*` and `gpu_v100*` partitions).
If your compute tasks rely on these older GPUs because they cannot efficiently
use more powerful devices, you are welcome to reach out to us at
mailto:hpcinfo@kuleuven.be (in case you haven't been contacted by us already).

Note that the Tier-2 login nodes will remain in service until the end of 2026.
