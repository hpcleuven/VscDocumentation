Hortense @ HPC-UGent
====================

.. warning::

    This documentation is still being completed,
    as Hortense is being prepared for testing.

    More information and details will be added in the coming days.

.. contents::
    :depth: 3
    :local:
    :backlinks: entry

General information
-------------------

**Hortense** is the 3rd VSC Tier-1 cluster, following *muk* (hosted by HPC-UGent, 2012-2016)
and *BrENIAC* (hosted by HPC-Leuven, 2016-2022).

The first phase of Hortense is also named ``dodrio``.

It is available since 2021, is hosted by Ghent University,
and maintained and supported by the HPC-UGent team.


Hardware details
----------------

Hortense currently consists of 3+1 partitions:

- ``dodrio/cpu_rome``: main partition:
   - 294 workernodes, each with:
       - 2x 64-core AMD Epyc 7H12 CPU 2.6 GHz (128 cores per node)
       - 256 GiB RAM (~2GB/core), no swap
- ``dodrio/cpu_rome_512``: large-memory partition:
   - 42 workernodes, each with:
       - 2x 64-core AMD Epyc 7H12 CPU 2.6 GHz (128 cores per node)
       - 512 GiB RAM (~4GB/core), no swap
- ``dodrio/gpu_rome_a100``: GPU partition:
   - 20 workernodes, each with:
       - 2x 24-core AMD Epyc 7402 CPU 2.8 GHz (48 cores per node)
       - 4x NVIDIA A100-SXM4 (40 GB GPU memory), NVLink3
       - 256 GiB RAM (~5GB/CPU core), no swap
- ``dodrio/cpu_rome_all``: combination of ``cpu_rome`` and ``cpu_rome_512``

Shared infrastructure:

- *storage*: 3 PB shared scratch storage, based on `Lustre <https://www.lustre.org>`_ (see ``$VSC_SCRATCH_PROJECTS_BASE``);
- *interconnect*: InfiniBand HDR-100 (~12.5GB/sec), 2:1 fat tree topology

  - for the GPU partition specifically: dual HDR-100 Infiniband

.. note:: A high-level overview of the cluster can be obtained by running the ``pbsmon`` command.

Getting access
--------------

To access the Tier-1 Hortense cluster, use SSH to connect to the dedicated login node with your VSC account:

* from the public internet, use ``tier1.hpc.ugent.be``
* from within the VSC network, use ``tier1.gent.vsc``

More general information about SSH login is available at :ref:`acccess_data_transfer`.

.. note::
  There is currently only one small login node (16 cores, 64GB RAM) available.

  **Please only use the login node as an access portal!**

  For resource-intensive tasks, like software compilation, testing job scripts, etc., please use an interactive job.

.. note::
  The login node of the Tier-1 Hortense cluster are currently only accessible via SSH.

  Alternative methods (using NX, a web portal) will be available soon.

System-specific aspects
-----------------------

*(more information soon)*

Software
--------

Operating system
****************

Both login nodes and workernodes in Hortense use *Red Hat Enterprise Linux 8 (RHEL8)* as operating system.

Resource manager
****************

`Slurm <https://slurm.schedmd.com/>`_ is used as resource manager and job scheduler.

A `Torque <https://github.com/adaptivecomputing/torque>`_ frontend
(implemented by the VSC support team in the ``jobcli`` Python library)
that provides *wrapper commands* for the familiar Torque commands ``qsub``, ``qstat``, ``qdel``, etc. is available.

**We strongly recommend using the Torque frontend for submitting and managing your jobs!**

Commands for job submission & management
++++++++++++++++++++++++++++++++++++++++

* ``qsub``: submit job script(s);
* ``qsub -I``: submit an interactive job;
* ``qstat``: get a list of all currently queued and running jobs;
* ``qdel``: delete jobs;
* ``qalter``: change submitted jobs;
* ``qhold``: put jobs on hold;
* ``qrls``: release held jobs;

General command options
+++++++++++++++++++++++

The following options are supported for each of the Torque frontend commands listed above:

* ``--help``: show supported command options;
* ``--version``: print version information for jobcli and Slurm;
* ``--debug``: show detailed information about how the command is executed in the backend (Slurm);

  * for ``qsub``, this includes the contents of the job script as it will be submitted;

* ``--dryrun``: see how a command *would* be executed, without actually the corresponding backend commands;

`#PBS` header lines in job script
+++++++++++++++++++++++++++++++++

Resource specifications and job metadata for a job can be specified via ``#PBS`` lines in the header of the job script.

See ``qsub --help`` for a list of supported options.

For example:

.. code:: shell

  #!/bin/bash
  #PBS -l nodes=1:ppn=64
  #PBS -l walltime=10:00:00

Submitting to a specific cluster partition
++++++++++++++++++++++++++++++++++++++++++

To submit to a specific partition, swap to the corresponding ``cluster/dodrio`` module before running the ``qsub`` command.

For example, to submit a GPU job:

.. code:: shell

    module swap cluster/dodrio/gpu_rome_a100
    qsub job_script.sh

A list of available partitions can be obtained using ``module avail cluster/dodrio``.

To check the currently active partition, use ``module list cluster``.

Limitations for jobs
++++++++++++++++++++

Maximum walltime
################

The maximum walltime that jobs can request is 3 days (72 hours): ``-l walltime=72:0:0``.

Jobs that request more walltime will be refused by the resource manager at submission time ("``Requested time limit is invalid``").

Scientific software
*******************

A central software stack with a rich set of scientific libraries, tools, and applications
is available via the ``module`` command, and was installed using `EasyBuild <https://easybuild.io>`_.

Use ``module avail`` to see which software versions are available,
and load one or more modules via the ``module load`` command to start using them.

If software that you require is missing, please submit a software installation request
via https://www.ugent.be/hpc/en/support/software-installation-request .

Resources
---------

* kickoff meeting (23 Nov 2021) -
  slides: :download:`download PDF <VSC_Tier-1_Hortense_kickoff_meeting_2021-11-23.pdf>` -
  recording: `watch on YouTube <https://www.youtube.com/watch?v=o0kNNsNT_rs>`_

Getting help
-------------

For questions and problems related to Tier-1 Hortense, please contact the central
support address for Tier-1 compute: `compute@vscentrum.be <mailto:compute@vscentrum.be>`_.
