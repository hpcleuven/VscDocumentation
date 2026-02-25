.. _genius_decommissioning:

Genius decommissioning
======================

Most remaining parts of :ref:`Genius <Genius hardware>`  will be
decommissioned when we start the acceptance tests for the
:ref:`new Tier-2 cluster <2025 hardware>`. This should happen
sometime between the second week and the fourth week of March.

The following hardware will then be retired:

- all Cascadelake CPU nodes (`batch*` partitions)
- all Skylake CPU nodes (`interactive` and `bigmem*` partitions)
- all nodes in the `dedicated*` partitions
- Superdome (`superdome*` partitions)

The P100 and V100 GPU nodes will be kept online for a longer period
(`gpu_p100*` and `gpu_v100*` partitions).
If your compute tasks rely on these older GPUs because they cannot efficiently
use more powerful devices, you are welcome to reach out to us at
mailto:hpcinfo@kuleuven.be (in case you haven't been contacted by us already).

Note that the Tier-2 login nodes will remain in service until the end of 2026.
