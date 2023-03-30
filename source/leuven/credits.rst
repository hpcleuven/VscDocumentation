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


Job cost calculation
~~~~~~~~~~~~~~~~~~~~

On Tier-2 clusters, we use Slurm for accounting purposes (on top of resource and 
job management).
See :ref:`Slurm accounting <accounting_leuven>` page for additional information.
In Slurm terminology, the cost of a job depends on the trackable resources (TRES)
it consumes. Two distinct TRES are the number of CPU cores and GPU devices. 
Different types of CPU and GPU nodes are given different weights 
(``TRESBillingWeights``) which you can retrieve as follows for e.g. wICE::

   scontrol show partitions -M wice

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
- ``num_gpus`` is the *effective* number of GPUs used for the job
- ``walltime`` is the number of minutes that the job ran

.. note::

    *effective* number of cores is not necessarily equal to what the user requests.
    E.g. if a job requests a single core/task, but the full memory of a node on wICE,
    then one node is blocked for such a job. Consequently, the effective number of cores
    will be 72, instead of 1.

    Similarly, on a node with 4 GPUs, if a user requests to use a single GPU, one-fourth
    of cores will be assigned to the job. So, e.g. on wICE ``num_cores`` will be 18.

.. note::

    *effective* number of GPUs deserves an explanation. If a user requests e.g. 2 GPUs
    for a job, then ``num_gpus`` will be 2. However, in certain cases, we allow multiple
    users to share a GPU (called sharding). In such cases, ``num_gpus`` could be a factor
    between zero and one.

.. note::

    The Tier-2 cluster has several types of compute nodes.
    Hence, different ``TRESBillingWeights`` applies to 
    different resources on different partitions of Genius and wICE.
    The difference in cost between different machines/processors reflects
    the performance difference between those types of nodes.
    For additional information, you may refer to the 
    `HPC Service Catalog<https://icts.kuleuven.be/sc/onderzoeksgegevens/hpc_vsc_page>`_
    (login required).

The difference in cost between different machines/processors reflects
the price-performance difference between those types of nodes. The total cost
of a job will be comparable on any compute node, but the
walltime will be different, depending on the performance of the nodes.

In the examples below, you run your jobs on a ``skylake`` node, for which
we charge 10 000 Slurm credits per hour.

An example of a job running on multiple nodes and cores is given below::

   $ sbatch -A lp_astrophysics_014 -M genius -N 2 -ntasks-per-node 36 simulation_3415.slurm

For Genius thin nodes we have ``TRESBillingWeights=CPU=4.62963``.
If this job finishes in 2.5 hours (i.e., walltime is 150 minutes), the user
will be charged::

   4.62963 * (2 * 36) * 150 = 50 000 credits


Charging rates
--------------

The charge rate for the various node types of Genius and wICE are listed in the table
below.  
The reported cost is the number of Slurm credits needed per core/GPU per minute.

+---------+-----------------+------------------------+
| Cluster | node type       | TRESBillingWeights     |
+=========+=================+========================+
| Genius  | skylake         | 4.62963                |
|         | cascadelake     | 4.62963                |
|         | skylake bigmem  | 5.55556                |
|         | Nvidia P100 GPU | 41.6667                |
|         | Nvidia V100 GPU | 59.5833                |
+---------+-----------------+------------------------+
| wICE    | icelake         | 2.54630                |
|         | icelake bigmem  | 4.39815                |
|         | Nvidia A100 GPU | 141.667                |
+---------+-----------------+------------------------+



How do I get credits to use the Tier-1 infrastructure
-----------------------------------------------------

Access to the Tier-1 is project-based, if you have a starting grant or
an approved project, or you pay for your compute time, you should have
received information on your job credits.
If not, please refer to the `official VSC website <https://www.vscentrum.be/>`_, or
:ref:`contact your VSC support team <Contact VSC>`.


.. _Geert Jan Bex: mailto:geertjan.bex@uhasselt.be
.. _credit request form:  https://admin.kuleuven.be/icts/onderzoek/hpc/request-project-credits
.. include:: ../jobs/links.rst
.. include:: links.rst
