.. _wice_t2_leuven_advanced:

===================
wICE advanced guide
===================

.. _wice_compilation:

Compiling software
------------------

Compared to the SkyLake and CascadeLake CPUs on Genius, the wICE nodes
feature more recent CPU models such as Intel IceLake, Intel Sapphire Rapids
and AMD Genoa. While architectural differences between SkyLake and CascadeLake
CPUs can be neglected, the differences with newer CPU models are more
substantial. When it comes to GPUs there are also significant differences in
the capabilities of P100, V100, A100 and H100 GPUs.

When locally installing software yourself, we therefore recommend to have
separate installations for the different types of CPUs and (if applicable)
GPUs on which you intend to run the software. This rule applies most strongly
to performance-critical code which is compiled from source. It applies less
strongly to precompiled binaries or interpreted code such as pure Python
scripts (meaning that it is typically not necessary to e.g. create different
Conda environments for different CPU types).

.. note::

    Remember that precompiled binaries (as is often the case when e.g. Conda
    or PyPI are involved) are not guaranteed to deliver optimal performance
    for the target device. In case of doubt, performance-critical parts of
    an application should not rely on precompiled binaries and instead use
    optimized binaries as provided by the centrally installed modules and/or
    by local installations from source.

.. note::

    Older toolchains (compilers, BLAS libraries, ...) may not be able to take
    full advantage of newer CPU models and so we typically recommend using
    the most recent available toolchains. Sapphire Rapids CPUs provide new
    'AMX' instructions, for example, which may be useful for AI applications.
    When using GNU compilers, however, the GCC version needs to be
    sufficiently recent (>= v11) in order to generate AMX code.

To let jobs use the correct installation at runtime, you can make use of
predefined environment variables such as ``${VSC_ARCH_LOCAL}`` (and possibly
``${VSC_ARCH_SUFFIX}`` and ``${VSC_INSTITUTE_CLUSTER}``) to organize your
installations.

For software using CPUs, the different installations would be:

- one for SkyLake and CascadeLake CPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``skylake`` or ``cascadelake``)
- one for IceLake CPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``icelake``)
- one for Sapphire Rapids CPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``sapphirerapids``)

For software which also uses GPUs, this would be:

- one for SkyLake CPUs with P100 GPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``skylake``)
- one for CascadeLake CPUs with V100 GPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``cascadelake``)
- one for IceLake CPUs with A100 GPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``icelake``)
- one for AMD Genoa CPUs with H100 GPUs
  :raw-html:`<br />`
  (``${VSC_ARCH_LOCAL}`` = ``zen4`` and ``${VSC_ARCH_SUFFIX}`` = ``-h100``)

Compiling software for a particular CPU/GPU model can be done in an
interactive job (``srun ...``) submitted to a partition containing
the target device(s) (see e.g. :ref:`genius hardware` and
:ref:`wice hardware`).

Many dependencies you might need are centrally installed. The modules
that are optimized for wICE are available when the appropriate
:ref:`cluster module <cluster_module>` is loaded. In most cases this will
happen automatically, but in case of problems it is a good idea to double check
the ``$MODULEPATH`` environment variable; it should contain paths that look as
starting with ``/apps/leuven/rocky8/${VSC_ARCH_LOCAL}${VSC_ARCH_SUFFIX}``
where ``${VSC_ARCH_LOCAL}${VSC_ARCH_SUFFIX}`` indicates the architecture of the
node in question.

Similar to other VSC clusters, wICE supports two families of common toolchains:
:ref:`FOSS <FOSS toolchain>` and :ref:`Intel <Intel toolchain>`. Next to that,
various `subtoolchains <https://docs.easybuild.io/common-toolchains/>`__ are
available. For more general information on software development on the VSC,
have a look at this :ref:`overview <software_development>`.


.. _wice_memory_hierarchy:

Memory hierarchy
----------------

When running applications in parallel it is often a good idea to take the
memory hierarchy into account (for example when pinning MPI processes
in :ref:`hybrid MPI/OpenMP calculations <hybrid_mpi_openmp_programs>`).
The nodes in the ``batch`` partition on Genius and wICE are the simpler ones
with a single NUMA domain and L3 cache per CPU, with the usual core-private
L1 and L2 caches. Other node types may feature more than one NUMA domain per
CPU and (in the case of AMD CPUs) more than one L3 cache per CPU.
The 48 cores in a Sapphire Rapids CPU, for example, share a large L3 cache
but are organized in 4 groups of 12 cores, each group associated with one
NUMA domain. For a complete overview, please consult the
:ref:`genius hardware` and :ref:`wice hardware` pages.

.. note::

    You can also retrieve this information using the ``lstopo-no-graphics``
    command. When on a compute node, keep in mind that the output will only
    be complete if all available cores have been allocated to your job.


.. _wice_worker:

Worker
------

The :ref:`Worker framework <worker framework>`, which allows to conveniently
parameterize simulations, is available on wICE. An attention point is that
if you want to lauch Worker jobs from the Genius login nodes, you will need to
use a specific module:

.. code-block:: shell

    $ module load worker/1.6.12-foss-2021a-wice

If instead you want to launch Worker jobs from an interactive job running on
wICE, you can use the ``worker/1.6.12-foss-2021a`` module. But do make sure
this is the version installed *specifically* for wICE, which you can check
by looking at the installation directory of worker. For example, the path
returned by ``which worker`` should start with ``/apps/leuven/rocky8/icelake``
or ``/apps/leuven/rocky8/sapphirerapids`` or ``/apps/leuven/rocky8/zen4-h100``.

Also note that the Worker support for Slurm is not yet complete. Both
the ``-master`` option for ``wsub`` and the ``wresume`` tool currently
only work for PBS/Torque and hence should not be used in the case of Slurm.

All the resources furthermore need to be specified inside the Slurm script
used as input for Worker (passing resources via the command line is not
supported). Various examples can be found in a `development branch
<https://github.com/gjbex/worker/tree/development_slurm/examples/>`__.
