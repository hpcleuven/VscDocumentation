.. _data_recovery:

##################
HPC Data Recovery
##################

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`wICE <wICE hardware>`
       * Tier-2 :ref:`Mindwell <Mindwell hardware>`

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`
       * Tier-1 :ref:`sofia <sofia cluster>`

Some VSC compute clusters keep regular data *snapshots* on their shared storage systems. This
can include the storage of ``VSC_HOME``, ``VSC_DATA`` and ``VSC_SCRATCH`` in your
account as well as project folders or ref:`Virtual Organizations <vo>`.

.. seealso::
   The documentation on :ref:`storage hardware` has a detailed description of each
   storage solution on our VSC compute clusters.

Storage snapshots keep the state of files and directories at fixed moments in
time. We take regular snapshots at varying time intervals depending on their
age. The older the snapshots, the less frequent they are. This means that if
you accidentally delete or make changes to files in the cluster, you are more
likely to recover that data in the same state it was lost the sooner you act.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      .. list-table::
         :header-rows: 1
         :align: center

         * - Age of data
           - Snapshot frequency
           - Storage locations
         * - Less than 1 day
           - Hourly
           - ``VSC_HOME``, ``VSC_DATA``
         * - Between 1 and 7 days
           - Daily
           - ``VSC_HOME``, ``VSC_DATA``
         * - Between 1 and 4 weeks
           - Weekly
           - ``VSC_HOME``, ``VSC_DATA``

   .. tab-item:: VUB
      :sync: vub

      .. list-table::
         :header-rows: 1
         :align: center

         * - Age of data
           - Snapshot frequency
           - Storage locations
         * - Less than 3 days
           - Hourly
           - ``VSC_HOME``, ``VSC_DATA``, ``VSC_DATA_VO``
         * - Between 3 and 7 days
           - Daily
           - ``VSC_HOME``, ``VSC_DATA``, ``VSC_DATA_VO``
         * - Between 1 and 4 weeks
           - Weekly
           - ``VSC_HOME``, ``VSC_DATA``, ``VSC_DATA_VO``
         * - More than 4 weeks
           - Monthly
           - ``VSC_HOME``, ``VSC_DATA``, ``VSC_DATA_VO``
         * -
           -
           -
         * - Less than 7 days
           - Daily
           - ``VSC_SCRATCH``, ``VSC_SCRATCH_VO``


   .. tab-item:: Tier-1 sofia
      :sync: sofia

      .. list-table::
         :header-rows: 1
         :align: center

         * - Age of data
           - Snapshot frequency
           - Storage locations
         * - Less than 7 days
           - Daily
           - ``HOME``, ``VSC_SCRATCH``, ``VSC_SCRATCH_PROJECTS_BASE``


.. _restoring_snapshot:

Restoring old files/folders
===========================

Restoring a file or directory from one of the snapshots is relatively easy.
Snapshots are located somewhere in the file system of the cluster. Once you
locate your snapshot (see below) you can restore your own files to a previous
version just by copying the file from one of the snapshots to its desired
location.

Some sites might provide specific tools to carry out the restoration of files
from snapshots. Please see the instructions below that correspond to your
cluster of choice.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      .. include:: hpc_data_recovery_leuven.rst

   .. tab-item:: VUB
      :sync: vub

      .. include:: hpc_data_recovery_mysnapshots.rst

   .. tab-item:: Tier-1 sofia
      :sync: sofia

      .. include:: hpc_data_recovery_mysnapshots.rst

