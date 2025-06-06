.. _storage hardware:

#############################
Tier-2 Storage Infrastructure
#############################

The storage attached to our HPC clusters is organized according to the
:ref:`VSC storage guidelines <data location>`.

All HPC clusters in VSC have their own shared storage solution accessible
from all nodes within that cluster. The so-called ``VSC_DATA`` and
``VSC_SCRATCH`` use this type of storage and constitute the main storage of the
cluster.

Each compute node also has a local storage that can be used by jobs for
temporary storage. This is usually referred to as ``VSC_SCRATCH_NODE`` or just
``TMPDIR``. In general, ``VSC_SCRATCH`` is preferred over the local storage on
the node as the most performant option for scratch files.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      .. include:: /leuven/tier2_hardware/kuleuven_storage_quota_table.rst

      For more information check: :ref:`KU Leuven storage`

   .. tab-item:: UGent
      :sync: ug

      .. include:: /gent/storage_quota_table.rst

      For more information check: :ref:`HPC-UGent Shared storage <UGent storage>`

   .. tab-item:: UAntwerpen
      :sync: ua

      .. include:: /antwerp/tier2_hardware/uantwerp_storage_quota_table.rst

      For more information check: :ref:`UAntwerp storage`

   .. tab-item:: VUB
      :sync: vub

      .. include:: /brussels/tier2_hardware/vub_storage_quota_table.rst

      For more information check: :ref:`VUB storage`

