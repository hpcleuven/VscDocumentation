.. _uantwerp_slurm_specifics:

Site-specific Slurm info
========================

While the :ref:`Running jobs in Slurm <running jobs>` and :ref:`job advanced`
pages provide basic and advanced information regarding Slurm, there are
additional points to consider when when using Slurm on Tier-2 clusters hosted
at UAntwerpen.


.. _uantwerp_pbs_to_slurm:

Converting from PBS to Slurm
----------------------------
Have a look at the :ref:`quick PBS-to-Slurm conversion tables <Slurm_convert_from_PBS>`
if you need help converting your PBS job scripts to Slurm. See also
:ref:`A list of important differences between Torque and Slurm <Slurm_PBS_differences>`.


.. _uantwerp_requesting_memory:

Requesting memory
-----------------
When requesting memory, keep in mind that no swap space is available in
case your application runs out of memory. Swapping is disabled because the nodes
don't have drives suitable for the load caused by swapping and because swapping
is extremely detrimental to performance.


.. _uantwerp_requesting_nodes:

Requesting nodes
----------------
On UAntwerp clusters we ask to only use the ``-N/--nodes`` option to request
(and use) full nodes. This is because in the current Slurm configuration
the empty cores cannot be used by other jobs. We furthermore ask to abstain
from the ``--nodes=<minimum number>-<maximum number>`` option without
consulting us first and discussing why it would make sense for your job.
