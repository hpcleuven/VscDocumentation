####################################
Where can I store what kind of data?
####################################

VSC provides multiple storage solutions with different strengths and
capabilities to cover all stages of data management in the research life cycle.
A general description of the different personal storage locations available to
all VSC accounts is described in :ref:`data location`.

* All VSC compute clusters have access to a common :ref:`VSC data directory`,
  so-called *VSC_DATA*. This storage is reliable to save your data and
  convenient to move it across different clusters. However *VSC_DATA* might not
  be particularly fast.

* The fastest storage in terms of I/O is the :ref:`VSC scratch space` of each
  compute cluster, so-called *VSC_SCRATCH*. This storage is the default choice
  to store data used by computational jobs. The limitation of the scratch is
  that it is not shared across multiple VSC clusters and files might be deleted
  after a certain time.

* Structured data needs special treatment and VSC provides an object store
  specically designed to handle such data in the :ref:`tier1_data_service`.
