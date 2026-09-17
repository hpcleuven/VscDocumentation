.. grid:: 1 1 2 2
   :gutter: 4

   .. grid-item-card::
      :class-header: bg-secondary text-white text-center font-weight-bold

      :fas:`truck` VO Data
      ^^^^^^^^^^^^^^^^^^^^

      Location
          ``$VSC_DATA_VO``, ``$VSC_DATA_VO_USER``

      Purpose
          Storage of datasets or resulting data that must be stored in the
          cluster to carry out further computational jobs, and that can be shared
          with co-workers.

      Availability: Very high
          Accessible from login nodes, compute nodes and from all clusters in VSC.

      Capacity: High and expandable
          By default, 112.5 GB (soft limit), 125.0 GB (hard limit, 7 days grace time).
          Can be expanded upon request.

      Perfomance: Low
          Jobs must always copy any data needed from ``$VSC_DATA_VO`` to the scratch
          before the run and save any results from scratch into ``$VSC_DATA_VO``
          after the run.

      Reliability: Very High
          Data is stored in a redundant file system with data replication.

      Back-ups:
          Back-ups policy depends on each VSC cluster. Check the :ref:`storage
          hardware` characteristics of the ``VSC_DATA`` storage of your
          cluster.

   .. grid-item-card::
      :class-header: bg-secondary text-white text-center font-weight-bold

      :fas:`rocket` VO Scratch
      ^^^^^^^^^^^^^^^^^^^^^^^^

      Location
          ``$VSC_SCRATCH_VO``, ``$VSC_SCRATCH_VO_USER``

      Purpose
          Storage of temporary or transient data that can be shared with co-workers.

      Availability: High
          Accessible from login nodes and compute nodes in the local cluster. Not
          accessible from other VSC clusters.

      Capacity: High and expandable
          225 GB (soft limit), 250 GB (hard limit, 7 days grace time).
          Can be expanded upon request.

      Perfomance: High
          Preferred location for all data files read or written during the
          execution of a job. Suitable for all workload types.

      Reliability: Medium
          Data is stored in a redundant file system, but without replication.

      Back-ups:
          Back-ups policy depends on each VSC cluster. Check the :ref:`storage
          hardware` characteristics of the ``VSC_SCRATCH`` storage of your
          cluster.
