VSC environment variables
=========================

For convenience, a number of environment variables are defined that can
help you when you write job scripts, or require specific initialization
to use certain hardware.

The list below is intended for reference only, the relevant
documentation should be consulted for the exact semantics.


Storage
-------

Please see the documentation on :ref:`storage options <data location>`.

``$VSC_HOME``
   The path to your home directory.
``$VSC_DATA``
   The path to your data directory.
``$VSC_SCRATCH``
   The path to your scratch directory on the cluster you are currently using.
``$VSC_SCRATCH_SITE``
   The path to your scratch directory at the site you are currently using,
   often the same as ``$VSC_SCRATCH``.
``$VSC_SCRATCH_NODE``
   The path to your scratch directory on the compute node your job is running
   on.
``$VSC_SCRATCH_GLOBAL``
   The path to a VSC-wide scratch volume (future work). Currently pointing to
   ``$VSC_SCRATCH`` or ``$VSC_SITE_SCRATCH``.


Hardware & OS
-------------

Please see the the documentation on :ref:`VSC hardware <hardware>`.

``$VSC_ARCH_LOCAL``
   CPU architecture, set per node in the cluster, e.g., ``skylake`` or ``haswell``.
``$VSC_INSTITUTE_CLUSTER``
   Name of the cluster you are currently on, e.g., ``leibniz`` or ``genius``.


Hub
---

VSC hardware is hosted on four sites, the VSC hubs.  These are

- Antwerp: ``antwerpen``
- Brussels: ``brussel``
- Ghent: ``gent``
- Leuven: ``leuven``

``$VSC_INSTITUTE``
   Name of the VSC hub your account is associated with.
``$VSC_INSTITUTE_LOCAL``
   Name of the VSC hub you are currently using.
