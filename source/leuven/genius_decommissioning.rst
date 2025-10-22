.. _genius_decommissioning:

Genius decommissioning
======================

Most remaining parts of :ref:`Genius <Genius hardware>`  will be
decommissioned when we start the acceptance tests for the
:ref:`new Tier-2 cluster <2025 hardware>`. This will take place either in
the middle of January 2026 at the earliest or at the end of February 2026
at the latest. In December we should be able to set a more specific date.

The current plan is to retire the following hardware:

- all Cascadelake CPU nodes (`batch*` partitions)
- all Skylake CPU nodes (`interactive` and `bigmem*` partitions)
- all nodes in the `dedicated*` partitions
- Superdome (`superdome*` partitions)

We are currently evaluating whether the P100 and V100 GPU nodes need to be
kept online for a longer period (`gpu_p100*` and `gpu_v100*` partitions).
If your compute tasks rely on these older GPUs because they cannot efficiently
use more powerful devices, you are welcome to reach out to us at
mailto:hpcinfo@kuleuven.be (in case you haven't been contacted by us already).

Note that the Tier-2 login nodes will remain in service until the end of 2026.
