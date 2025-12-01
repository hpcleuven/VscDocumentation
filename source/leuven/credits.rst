.. _KU Leuven credits:

Credits to use KU Leuven infrastructure
=======================================

KU Leuven uses a credit system to do accounting on the Tier-2 HPC systems it hosts.


How do I request credits on the KU Leuven Tier-2 systems
--------------------------------------------------------

KU Leuven users
~~~~~~~~~~~~~~~
You can request two types of job credits: introduction credits and project
credits.

Introduction credits
   This is a limited amount of free credits for test and development purposes.
Project credits
   These are job credits used for actual research and production runs.

You will find the relevant information to apply for both types of credits,
including pricing, in the `Service Catalog`_ (login required).

UHasselt users
~~~~~~~~~~~~~~
If you would like credits for a new project, please fill out the
`credit request form`_.

.. warning::

   Please read and follow the instructions in that form carefully!

If you require additional credits for an existing project, please contact
your VSC coordinator `Geert Jan Bex`_.

Other users
~~~~~~~~~~~

Please contact your VSC coordinator/contact or your :ref:`local support staff
<Contact VSC>`.


.. _leuven_job_cost_calculation:

Job cost calculation
~~~~~~~~~~~~~~~~~~~~

On Tier-2 clusters, we use Slurm for accounting purposes (on top of resource and
job management).
See :ref:`Slurm accounting <accounting_leuven>` page for additional information.
In Slurm terminology, the cost of a job depends on the trackable resources (TRES)
it consumes. Two distinct TRES are the number of CPU cores and GPU devices.
Different types of CPU and GPU nodes are given different weights
(``TRESBillingWeights``) which you can retrieve as follows for e.g. wICE::

   scontrol show partitions --clusters=wice

As an example, for a GPU node, the weights are configured as::

   TRESBillingWeights=CPU=2.546296296,GRES/gpu:a100-sxm4-80gb=141.6666667,GRES/shard:a100-sxm4-80gb=141.6666667

**CPU-only jobs**

The following formula applies::

   CPU TRESBillingWeights * num_cores * walltime

Where

- ``CPU TRESBillingWeights`` is the applied weight for CPU resources (see above)
- ``num_cores`` is the *effective* number of cores used for the job
- ``walltime`` is the number of minutes that the job ran

**GPU jobs**

The following formula applies::

   (CPU TRESBillingWeights * num_cores + GPU TRESBillingWeights * num_gpus) * walltime

Where

- ``CPU TRESBillingWeights`` is the applied weight for CPU resources (see above)
- ``GPU TRESBillingWeights`` is the applied weight for GPU resources (see above)
- ``num_cores`` is the *effective* number of cores used for the job
- ``num_gpus`` is the number of GPUs requested for the job
- ``walltime`` is the number of minutes that the job ran

.. note::

    *Effective* number of cores is not necessarily equal to what the user requests.
    E.g. if a job requests a single core/task, but the full memory of a node on wICE,
    then one node is blocked for such a job. Consequently, the effective number of cores
    will be 72, instead of 1.

.. note::

    The Tier-2 cluster has several types of compute nodes.
    Hence, different ``TRESBillingWeights`` apply to
    different resources on different partitions of Genius and wICE.
    The difference in cost between different machines/processors reflects
    the performance difference between those types of nodes.
    For additional information, you may refer to the
    `HPC Service Catalog <https://icts.kuleuven.be/sc/onderzoeksgegevens/hpc_vsc_page>`_
    (login required).

The difference in cost between different machines/processors reflects
the price-performance difference between those types of nodes. The total cost
of a job will be comparable on any compute node, but the
walltime will be different, depending on the performance of the nodes.

As an example, consider a job running on two nodes of the default partition on
Genius, where ``TRESBillingWeights=CPU=4.62963`` applies::

   $ sbatch --account=lp_myproject --clusters=genius --nodes=2 \
            --ntasks-per-node=36 myjobscript.slurm

If this job finishes in 2.5 hours (i.e., walltime is 150 minutes), the user
will be charged::

   floor(4.62963 * (2 * 36)) * 150 = 49 950 credits

You can also get such estimates from the ``sam-quote`` tool by providing it
with your job submission command::

   $ sam-quote sbatch --account=lp_myproject --clusters=genius --nodes=2 \
                      --ntasks-per-node=36 --time=2:30:00 myjobscript.slurm
   49950

Note that ``sam-quote`` assumes a worst-case scenario in which the job does
not stop before reaching its time limit.


Charge rates
------------

The table below shows the charge rates for each CPU and GPU type on Genius
and wICE. These values correspond to the number of Slurm credits needed
to allocate one core or GPU during one minute.

+---------+---------------------+----------+------------------------+
| Cluster | Resource            | Type     | ``TRESBillingWeights`` |
+=========+=====================+==========+========================+
| Genius  | Skylake             | CPU core | 4.62963                |
+         +---------------------+----------+------------------------+
|         | Skylake (bigmem)    | CPU core | 5.55556                |
+         +---------------------+----------+------------------------+
|         | Cascadelake         | CPU core | 4.62963                |
+         +---------------------+----------+------------------------+
|         | P100                | GPU      | 41.6667                |
+         +---------------------+----------+------------------------+
|         | V100                | GPU      | 59.5833                |
+---------+---------------------+----------+------------------------+
| wICE    | Icelake             | CPU core | 2.54630                |
+         +---------------------+----------+------------------------+
|         | Icelake (bigmem)    | CPU core | 4.39815                |
+         +---------------------+----------+------------------------+
|         | Icelake (hugemem)   | CPU core | 4.39815                |
+         +---------------------+----------+------------------------+
|         | Sapphire Rapids     | CPU core | 3.47222                |
+         +---------------------+----------+------------------------+
|         | Zen4 Genoa          | CPU core | 3.47222                |
+         +---------------------+----------+------------------------+
|         | A100                | GPU      | 141.667                |
+         +---------------------+----------+------------------------+
|         | H100                | GPU      | 569.444                |
+---------+---------------------+----------+------------------------+


.. _Geert Jan Bex: mailto:geertjan.bex@uhasselt.be
.. _credit request form:  https://admin.kuleuven.be/icts/onderzoek/hpc/request-project-credits
