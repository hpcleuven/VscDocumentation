.. _Hortense hardware:

Hortense @ HPC-UGent
====================

.. contents::
    :depth: 3
    :local:
    :backlinks: none

General information
-------------------

**Hortense** is the 3rd VSC Tier-1 cluster, following *muk* (hosted by HPC-UGent, 2012-2016)
and *BrENIAC* (hosted by HPC-Leuven, 2016-2022).

The Hortense cluster also has an internal name ``dodrio``.

It is available since 2021, is hosted by Ghent University,
and maintained and supported by the HPC-UGent team.

In 2023 a second phase was added, more than doubling the existing capacity of the system.

End of 2025, the decommissioning process of cluster Hortense will start.
This is in anticipation of the 4th VSC Tier-1 cluster that will become available at the VUB datacenter from end 2025.


.. _hortense_hardware_details:

Hardware details
----------------

Hortense consists of the following partitions:

- ``dodrio/cpu_rome_rhel9``: phase 1 main partition:
   - 342 workernodes, each with:
       - 2x 64-core AMD Epyc 7H12 CPU 2.6 GHz ("Rome" microarchitecture, 128 cores per node)
       - 238 GiB usable RAM (~1.85GB/core), no swap
       - 480 GB SSD local disk
- ``dodrio/cpu_rome_512_rhel9``: large-memory partition:
   - 42 workernodes, each with:
       - 2x 64-core AMD Epyc 7H12 CPU 2.6 GHz ("Rome" microarchitecture, 128 cores per node)
       - 488 GiB usable RAM (~3.8GB/core), no swap
       - 480 GB SSD local disk
- ``dodrio/cpu_milan_rhel9``: phase 2 main partition:
   - 384 workernodes, each with:
       - 2x 64-core AMD Epyc 7763 CPU 2.45 GHz ("Milan" microarchitecture, 128 cores per node)
       - 238 GiB usable RAM (~1.85GB/core), no swap
       - 480 GB SSD local disk
- ``dodrio/gpu_rome_a100_40``: GPU partition:
   - 20 workernodes, each with:
       - 2x 24-core AMD Epyc 7402 CPU 2.8 GHz (48 cores per node)
       - 4x NVIDIA A100-SXM4 (40 GB GPU memory), NVLink3
       - 238 GiB usable RAM (~4.95GB/CPU core), no swap
       - 480 GB SSD local disk
- ``dodrio/gpu_rome_a100_80``: phase 2 GPU partition:
   - 20 workernodes, each with:
       - 2x 24-core AMD Epyc 7402 CPU 2.8 GHz (48 cores per node)
       - 4x NVIDIA A100-SXM4 (80 GB GPU memory), NVLink3
       - 488 GiB usable RAM (~10GB/CPU core), no swap
       - 480 GB SSD local disk
- ``dodrio/debug_milan_rhel9``: interactive and debug partition:
   - 4 workernodes, each with:
       - 32-core AMD Epyc 7513 CPU 2.6 GHz (128 oversubscribed cores as seen by scheduler)
       - 1 shared NVIDIA L4 (24 GB GPU memory)
       - 1 NVIDIA L4 (24 GB GPU memory)
       - 488 GiB usable RAM (~3.8GB/oversubscribed core), no swap
       - 100 GB SSD local disk
- ``dodrio/cpu_rome_all_rhel9``: combination of ``cpu_rome_rhel9`` and ``cpu_rome_512_rhel9``
- ``dodrio/gpu_rome_a100``: combination of ``gpu_rome_a100_40`` and ``gpu_rome_a100_80``

Shared infrastructure:

- *storage*: 5.4 PB shared scratch storage, based on `Lustre <https://www.lustre.org>`_ (see ``$VSC_SCRATCH_PROJECTS_BASE``);
- *interconnect*: InfiniBand HDR-100 (~12.5GB/sec), 2:1 fat tree topology

  - for the GPU partition specifically: dual HDR Infiniband

.. note:: A high-level overview of the cluster can be obtained by running the ``pbsmon -P`` command.

.. _hortense_getting_access:

Getting access
--------------

.. _hortense_access_policy:

Access policy
*************

**The Hortense VSC Tier-1 cluster can only be accessed by people with an active Tier-1 compute project.**

Tier-1 compute project resources are always allocated for a given period.
After this period expires, the users of this project lose access to all resources granted within that project.
This includes storage in addition to compute resources (CPU and GPU).

As soon as a project expires, project members:

* will no longer be able to use any remaining CPU cycles, GPU cycles or credits
* will no longer have access to the dedicated project folders
* will lose access to the Tier-1 cluster, unless they have another active project

See https://www.vscentrum.be/compute for more information on requesting access, rules and regulations.


.. _hortense_login_nodes:

Login nodes (SSH)
*****************

You can use SSH to connect to the login nodes of the Tier-1 Hortense cluster with your VSC account:

* from the public internet, use ``tier1.hpc.ugent.be``
* from within the VSC network, use ``tier1.gent.vsc``

More general information about SSH login is available in the
:ref:`terminal
interface` section.

There are 2 login nodes for Hortense: ``login57`` and ``login58``, both having Red Hat Enterprise Linux release 9.4 as operating system.
When logging in using SSH, you will be assigned to either of these login nodes,
based on the IP address of the host you are connecting from.

If you need to access a *specific* login node (for example because you have a ``screen`` or ``tmux`` session
running there), just run "``ssh login58``" to jump to ``login58`` if you were logged in to ``login57``,
or use "``ssh login57``" to jump to ``login57`` from ``login58``.

.. note::
  The available resources on the Hortense login nodes are very limited:
  there are only 8 cores and ~60GB of RAM memory available on each login node,
  and these resources are shared by everyone that is logged in there.

  **Please only use the Hortense login nodes as an access portal!**

  For resource-intensive interactive tasks, like software compilation, testing software or job scripts, etc.,
  please use an interactive job, either via ``qsub -I`` (see also :ref:`hortense_resource_manager`)
  or through the :ref:`hortense_web_portal`.


.. _hortense_login_nodes_host_keys:

Host keys
+++++++++

The first time you log in to the Hortense login nodes, a fingerprint of the host key will be shown.
Before confirming the connection, verify the correctness of the host key, to ensure you are
connecting to the correct system.

**Please verify that the fingerprint of the host key is *one* of the following**:

* for ECDSA host key:

  * ``90:c7:d5:29:b3:c8:8c:fc:d4:c6:d7:14:68:bc:0a:7b`` (MD5)
  * ``1Q6syHAJnrybhPJPX87gmLKsKRUVDZAy+5N96RbELBg`` (SHA256)

* for ED25519 host key:

  * ``d0:8e:19:5a:bb:dc:32:45:53:82:ed:ae:10:07:83:72`` (MD5)
  * ``IPfUtYyl12Vr+1QEb53uoNq4DzaIPUGipWunNjwVpwI`` (SHA256)

* for RSA host key:

  * ``53:48:19:2b:bf:e2:a3:e7:45:a9:cd:fe:83:c3:98:a1`` (MD5)
  * ``B8R1oVM02ikstqnwBAvvM0CH7cZxvwWuek/BroqNoxI`` (SHA256)

The type of fingerprint that will be shown depends on the version and configuration of your SSH client.

.. _hortense_web_portal:

Web portal
**********

To access Tier-1 Hortense you can also use the `Open On-Demand` web portal
https://tier1.hpc.ugent.be.

More information about the usage of the web portal is available in https://docs.hpc.ugent.be/web_portal/.

.. note::

   If you are using the Hortense web portal from outside of the network of a Flemish university,
   you will first need to open the `VSC Firewall`_ web app and log in with your VSC account.

   Keep the browser tab with firewall app open as long as you want to use the web portal!

.. _hortense_scratch_globus:

Hortense scratch via Globus
***************************

To access your data in your (project) scratch directory on Tier-1 Hortense,
you should use Globus via the `VSC UGent Tier1 projects` endpoint.

More general information about Globus is available at :ref:`globus platform`.


Managing project members
************************

Managing members of a project can be done by the Principal Investigator (PI) and group moderators of the project
via the `VSC accountpage <https://account.vscentrum.be>`_, as follows:

* Go to the `Edit Group <https://account.vscentrum.be/django/group/edit>`_ tab;
* Select the group that corresponds to the project you want to manage.
  For projects on the Tier-1 cluster *Hortense*, the group names all start with "``gpr_compute_``".
* Click the ``Edit`` button once the group that corresponds to your Tier-1 project is selected.
* Change group membership via the ``Manage members`` section on the next page:

  * **To remove a project member**:, click the ``x`` next to the VSC account that was invited
    in the ``Members`` subsection.
  * **To invite someone to join the project**: click the box in the ``Invite users`` subsection,
    add select a VSC account ID to send a join invitation to. Note that you can filter the accounts
    to select by (partially) typing the name of the VSC account.
  * **To cancel a pending invitation**: use the ``x`` next to the VSC account that was invited.
  * **To promote a project member to group moderator**: click the box in the ``Moderators`` subsection
    and select their VSC account ID.

* **Click** ``Update`` **to apply the changes you made.**

Keep in mind that:

* Group join invitations need to be *accepted* first before the VSC account is added to the group.
* It can take a while (about one hour) before any changes in group membership are reflected on the system itself.

Sending a request to join a project
***********************************

You can submit a request to join a Tier-1 project to the moderators of the corresponding group
via the `VSC accountpage <https://account.vscentrum.be>`_, as follows:

* Go to the `New/Join Group <https://account.vscentrum.be/django/group/new>`_ tab;
* Select the group that corresponds to the project you want to join in the ``Join group`` section.
  For projects on the Tier-1 cluster *Hortense*, the group names all start with "``gpr_compute_``".
* In the ``Message`` field, add a short message that will be included in the join request that will
  be sent to the group moderators. Make it clear who you are, and why you want to join the project.
* **Click** ``Submit`` **to send the group join request.**

Keep in mind that:

* Your request needs to be approved by one of the group moderators before your VSC account is added to the group.
* It can take a while (about one hour) before any changes in group membership are reflected on the system itself.

Consult your project resource usage
***********************************

The Resource Application web app https://resapp.hpc.ugent.be allows you to consult your usage in a user-friendly way.

Please note that this app is still in ‘beta’.
(For instance, storage usage is not yet done, so this will show up 0 everywhere.)
In an upcoming development cycle, we will improve shortcomings and correct bugs.
Do not hesitate to give your feedback on using the Resource Application via compute@vscentrum.be

Practical usage:

* Open a webbrowser to https://resapp.hpc.ugent.be (The app will redirect you via the `VSC Firewall`_ application first, if needed.)
* The Resource Application shows you all Tier1-Hortense projects that you are a member of.
* By clicking on the dropdown arrow on the right in the initial Projects tab, you can consult the raw usage of one of your projects (in CPU hours and GPU hours).
* You can also view Logs and get more fine-grained usage details.
* When you click on the project name, you enter a new screen giving you information on allocation and cutoff. The orange box and number in the box refer to the 20% cutoff.

The 20% cutoff is for academic non-starting grant projects only, referring to paragraph 9(4) of the 'Regulations Governing Applications For Use of the Flemish Tier-1 Supercomputing Platform' (see https://www.vscentrum.be/_files/ugd/5446c2_21daee40839244c5a099a6d6bffaedb5.pdf).
This is 20% of the initial allocated compute time a project is at risk of losing, if that 20% has not yet been used during the first 3 months of the project.

Workshops/trainings
*******************

It is possible to organize research-oriented workshops or trainings using Tier1 Hortense resources, but this is solely the responsibility of the organizers. Organizers should be very much aware that availability of Tier1 or support staff can never be guaranteed. Organizers should therefore always have a backup plan at hand, which should include accepting the possibility that the workshop has to be cancelled due to unavailability of Tier1. The VSC or its staff can never be held accountable in case of problems.

Organizers should be moderator of an active Tier-1 compute project. This can be a starting grant or collaboration grant, but only if all participants of the workshop are academic users and no entrance fee is charged. If the workshop is open for industry participants or an entrance fee is charged, a paid-for compute project should be requested (see https://www.vscentrum.be/vsc4business). Do include a link to the public website with information about the workshop/training in your Tier-1 compute request.

It remains the responsibility of the organizers:

* to populate the active Tier-1 compute project with the vsc-ids of all participants
* to make sure participants without a vsc-id request one well in time (at least 2 weeks before the start of the workshop)
* to make sure that any required software is available and working as expected, tested at least 2 weeks before the start of the workshop
* to prepare and have at hand a fallback solution or strategy, should the Tier-1 resources be unavailable.

If the interactive partitions (debug) of Tier-1 are not sufficient, specific resource requests or reservations may be made. However, these should be clearly indicated up front in the project request. Additionally, for reservations the Tier1 support staff should be informed via compute@vscentrum.be at least 2 weeks before the workshop with the project group containing all vsc-ids that should be included in the reservation. Later additions will not be accepted.

These requirements may be adjusted as needed in the future, please make sure you take into account the latest requirements when organising workshops or trainings.
All communication regarding trainings or workshops should go via compute@vscentrum.be. 


.. _hortense_system_specific_aspects:

System-specific aspects
-----------------------

.. _hortense_local_storage:

Local storage
*************

In each node, a local storage device is available.
This storage space can be addressed with the environment variable $TMPDIR

.. code:: shell

  cd $TMPDIR


.. _hortense_home_on_scratch:

Home-on-scratch setup
*********************

On Tier-1 Hortense, the home directory (``$HOME``) corresponds to your personal scratch directory (``$VSC_SCRATCH``),
rather than your usual VSC home directory (``$VSC_HOME``).

This is done to ensure that Tier-1 Hortense can remain operational, even if there is maintenance being
performed on the Tier-2 shared storage filesystem of a VSC site (UGent, KUL, VUB, UAntwerpen),
or in case of problems with the network connection to the other VSC sites.

Although your VSC home directory is usually accessible via ``$VSC_HOME``,
we strongly recommend to *not* simply create symbolic links to files like your ``.bashrc`` startup script,
since that would defeat the purpose of this "home-on-scratch" setup.

This recommendation also applies to ``$VSC_DATA``: you should avoid using it in your job scripts as much as
possible, and ensure that your workflow only relies on the Hortense scratch filesystem. If you require any
data as input for your jobs, it should be copied to the Hortense scratch filesystem first.

.. _hortense_project_scratch_dirs:

Project scratch directories
***************************

* Please be aware that storage space on ``$VSC_SCRATCH`` (personal scratch directory) is limited per user to 3 GB.
* Instead, it is better to use the dedicated scratch storage space which is reserved for your Tier-1 project.
* The environment variable ``$VSC_SCRATCH_PROJECTS_BASE`` points to the base folder containing all project directories.
* Project directories are given the same name as your Tier-1 project (so *without* a prefix like ``gpr_compute_``).
* To change to your project scratch directory, you can use this command:

.. code:: shell

  cd $VSC_SCRATCH_PROJECTS_BASE/your_project_name

In this command, you should change '``your_project_name``' to the actual name of your project.


**As soon as a project expires, project scratch directories will NO LONGER be accessible.**
Please take this into account when planning your project execution.
Plan ahead and offload your data well before your project expires.

**Clean up and remove any remaining data in the project scratch folders before the project expires.**

Remaining data in project scratch folders for projects that have expired are earmarked for deletion.
The Tier1 operational team can delete this data without further notification.


.. _hortense_scratch_storage_quota_usage:

Scratch storage quota usage
***************************

* You can check personal and project storage quota usage by running the ``my_dodrio_quota`` command.
* If you want to check storage quota for specific projects, or for projects that are not listed automatically, use the ``-p`` option.
* For a list of all options, run ``my_dodrio_quota -h``.


.. _hortense_accessing_data_readonly:

Accessing data via ``/readonly``
********************************

Due to the fairly aggressive page cache purging policy of the `Lustre <https://www.lustre.org>`_
storage software that is used for the Tier-1 Hortense scratch filesystem, you may need to make some changes
to how you access data in your job scripts to avoid performance problems.

Whether or not this is required depends whether data is being read multiple times during your job.
If so, the extent of the performance impact depends on the number of files that are read,
how large those files are, how those files are being accessed (the I/O pattern), etc.
Note that this applies to both input data for your workloads, as well as
any software you have installed on the Tier-1 Hortense scratch filesystem (see also :ref:`hortense_software_readonly`).

To mitigate performance problems caused by the aggressive page cache purging,
you can access the data in your project scratch directory through the ``/readonly`` mount point,
rather than accessing it directly.

This is done by prefixing the path to files and directories with ``/readonly/`` in your job script:
rather than accessing your data via ``$VSC_SCRATCH_PROJECTS_BASE/...`` (or ``/dodrio/scratch/...``,
which you should not use), you just use ``/readonly/$VSC_SCRATCH_PROJECTS_BASE/...`` instead.
For example:

.. code:: shell

   export INPUT_DATA=/readonly/VSC_SCRATCH_PROJECTS_BASE/your_project_name/inputs/
   python example_process_data.py $INPUT_DATA


As the name suggests, the ``/readonly`` mount point only provides *read-only* access to your data.
Trying to make any changes to files that are accessed via ``/readonly`` will result in "``Read-only filesystem``" errors.

.. note::

   On the login nodes, there is a delay of maximum 30 minutes for changes to files (or new/removed
   files/directories) to be reflected through the ``/readlonly`` mount point.

   In jobs, any changes you make to files or directories in your project scratch directory should be reflected
   through the ``/readonly`` mount point, as long as the job started running *after* the changes were made.

   In addition, take into account that changes in your project scratch directory which are made while the job
   is running may *not* be reflected through the ``/readonly`` mount point (during that job).
   If your job script creates new files, updates existing files, etc., those changes may not be
   visible via ``/readonly`` during the lifetime of the job, so you should not assume that this will be the case.


.. _hortense_interactive_debug:

Interactive and debug partitions
********************************

A number of (small) interactive and debug partitions are available: `debug_rome`, `debug_milan` and `debug_milan_rhel9`
Purpose of these partitions is to quickly get access to a limited number of resources.

The limitations are a maximum of 5 jobs (running and/or waiting) in queue, only up to 3 running jobs and all running jobs may only allocate
a total of 8 CPU cores combined.
The CPUs are oversubscribed by a factor 4, which may lead to slower than expected run times when the usage is high.


Technical details of debug/interactive partitions
+++++++++++++++++++++++++++++++++++++++++++++++++

Partition `debug_rome` nodes have one NVIDIA V100 GPU that can be requested for exclusive access
(as with the GPU partitions) and also one less powerful GPU (NVIDIA Quadro P1000)
that is always available but shared across all jobs on that node.

Partition `debug_milan` nodes have one NVIDIA L4 GPU that can be requested for exclusive access
(as with the GPU partitions) and also one GPU NVIDIA L4 that is always available but shared across all jobs on that node.


Using the debug/interactive partitions
++++++++++++++++++++++++++++++++++++++

To make use of the partitions you can select the ``dodrio debug_rome``, ``dodrio debug_milan`` or ``dodrio debug_milan_rhel9`` options in the `Cluster` field in the
`Interactive Apps` forms on the webportal, or from the CLI

.. code:: shell

    module swap cluster/dodrio/debug_rome
    qsub job_script.sh

    module swap cluster/dodrio/debug_milan
    qsub job_script.sh

    module swap cluster/dodrio/debug_milan_rhel9
    qsub job_script.sh


No credits are consumed when using these partitions.

For some additional information, see the documentation on the
HPC-UGent Tier-2 interactive and debug cluster: https://docs.hpc.ugent.be/interactive_debug/.


Software
--------

Operating system
****************

Both login nodes and workernodes in Hortense use *Red Hat Enterprise Linux 8 (RHEL8)* as operating system.

.. _hortense_resource_manager:

Resource manager
****************

`Slurm <https://slurm.schedmd.com/>`_ is used as resource manager and job scheduler.

A `Torque <https://github.com/adaptivecomputing/torque>`_ frontend
(implemented by the VSC support team in the ``jobcli`` Python library)
that provides *wrapper commands* for the familiar Torque commands ``qsub``, ``qstat``, ``qdel``, etc. is available.

**We strongly recommend using the Torque frontend for submitting and managing your jobs!**

.. _hortense_job_submission_mgmt:

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

  * for ``qsub``, this includes the contents of the job script like it will be submitted;

* ``--dryrun``: see how a command *would* be executed, without actually executing the corresponding backend commands;

`#PBS` header lines in job script
+++++++++++++++++++++++++++++++++

Resource specifications and job metadata for a job can be specified via ``#PBS`` lines in the header of the job script.

See ``qsub --help`` for a list of supported options.

For example:

.. code:: shell

  #!/bin/bash
  #PBS -l nodes=1:ppn=64
  #PBS -l walltime=10:00:00

Specifying a project
++++++++++++++++++++

When submitting jobs to Hortense, it is required that you specify which project credits you want to use
(see also :ref:`hortense_getting_access`).

.. note::
   The terminology used by the Slurm backend is "*accounts*", while we usually refer to *projects*.

Specifying a project can be done in the ``qsub`` command, using the ``-A`` option:

.. code:: shell

  qsub -A example script.sh

Or via a ``#PBS`` header line in your job script:

.. code:: shell

  #PBS -A example

Another option is to define the ``$SLURM_ACCOUNT`` environment variable
(for example in your ``$HOME/.bashrc`` startup script on Hortense):

.. code:: shell

  export SLURM_ACCOUNT='example'

If you've specified an incorrect project name through one of the mechanisms mentioned above,
the ``qsub`` command will produce a helpful error that mentions the names of the projects
you currently have access to:

.. code:: shell

   $ qsub -A wrong_project script.sh
   ERROR: Specified account 'wrong_project' is not valid (valid account(s): valid_project_1, valid_project_2)

.. note::
    Be careful when you are a member of multiple Tier-1 Hortense projects,
    make sure that you always specify the correct project to avoid accidentally exhausting
    the credits of a project unintendedly.

Submitting to a specific cluster partition
++++++++++++++++++++++++++++++++++++++++++

To submit to a specific partition, swap to the corresponding ``cluster/dodrio`` module before running the ``qsub`` command.

For example, to submit a GPU job:

.. code:: shell

    module swap cluster/dodrio/gpu_rome_a100
    qsub job_script.sh

A list of available partitions can be obtained using ``module avail cluster/dodrio``.

To check the currently active partition, use ``module list cluster``.

.. _tier1_request_gpus:

Requesting GPU resources
++++++++++++++++++++++++

Don't forget to actively request GPU resources in your jobs or from the commandline.
Only loading the cluster/dodrio/gpu_rome_a100 module is not sufficient.
By default you'll get 12 cores per requested GPU (an explicit ppn= statement is not required).

.. code:: shell

    module swap cluster/dodrio/gpu_rome_a100
    qsub -l nodes=1:gpus=1

(The above example is for a single-node job, 1 GPU, and will also give you 12 CPU cores.)


Requesting memory
+++++++++++++++++

The default memory that your job will get access is the proportional
share of the total avaliable memory on the node:
If you request a full node, all usable memory will be available.
If you request ``N`` cores on a partition where nodes have ``M`` cores, you will get ``N/M``
of the total usable memory on the node. For the number of cores and available memory per cluster, please see our
:ref:`infrastructure <hortense_hardware_details>`,
or you can use the :ref:`web portal <hortense_web_portal>`, open
the desktop app and there you can browse it per partition and core using the
submission form (there is no need to start an actual desktop).

Please be aware! If you request more memory than the default memory would be,
you will be billed for the requested memory proportion of a node.
If you use ``X`` part of the memory on a partition where nodes have ``M`` cores,
you will be billed for ``X*M`` (rounded up for the next integer) cores,
even if your requested cores (``N``) are smaller than ``X*M``. 


Limitations for jobs
++++++++++++++++++++

Maximum walltime
################

The maximum walltime that jobs can request is 3 days (72 hours): ``-l walltime=72:0:0``.

Jobs that request more walltime will be refused by the resource manager at submission time ("``Requested time limit is invalid``").

.. _hortense_scientific_software:

Scientific software
*******************

A central software stack with a rich set of scientific libraries, tools, and applications
is available via the ``module`` command, and was installed using `EasyBuild <https://easybuild.io>`_.

Use ``module avail`` to see which software versions are available,
and load one or more modules via the ``module load`` command to start using them.

If software that you require is missing, please submit a software installation request
via https://www.ugent.be/hpc/en/support/software-installation-request .

.. _hortense_software_readonly:

Accessing software via ``/readonly`` mount point
++++++++++++++++++++++++++++++++++++++++++++++++

The central software stack on Tier-1 Hortense is provided via the ``/readonly`` mount point
(see also :ref:`hortense_accessing_data_readonly`). This is largely transparent as long as you
only load modules that are part of the central software stack.

If you install any software yourself in your project scratch directory, we highly recommend
you to also access it only through the ``/readonly`` mount point, since this can have a significant
performance benefit.

To ensure that the paths which are 'engraved' in your own software installations always start with ``/readonly/``,
for example in scripts or binaries that make part of the installation,
you should install the software using the ``dodrio-bind-readonly`` utility. This allows you to "rename" the path to your
project scratch directory so it starts with ``/readonly/``, while preserving sort-of write access to it
(``dodrio-bind-readonly`` actually provides an environment
where the ``/readonly/$VSC_SCRATCH_PROJECTS_BASE/...`` part is mapped to the real and writable
``$VSC_SCRATCH_PROJECTS_BASE/...`` path).

Assuming that the procedure to install the software is implemented in a script named ``install.sh``,
you can use ``dodrio-bind-readonly`` as follows:

.. code::

   dodrio-bind-readonly ./install.sh

The ``install.sh`` script should be implemented such that it installs the software to
``/readonly/$VSC_SCRATCH_PROJECTS_BASE/...``, that is a location in your project scratch directory that starts
with ``/readonly/``.

Or you can start a new shell session in which ``/readonly/$VSC_SCRATCH_PROJECTS_BASE/...`` is
accessible with write permissions:

.. code::

   dodrio-bind-readonly /bin/bash

.. note::

    This can only work when the ``dodrio-bind-readonly`` is used to map the base path for project scratch directories
    ``$VSC_SCRATCH_PROJECTS_BASE`` to ``/readonly/$VSC_SCRATCH_PROJECTS_BASE``, since otherwise
    any path that start with ``/readonly`` is indeed *read-only*, and trying to do any write operation
    would result in a "``Read-only file system``" error.

If you need any help with this, please contact the Tier-1 Hortense support team (see :ref:`hortense_help`).


.. _hortense_licensed_software:

Access to licensed software
+++++++++++++++++++++++++++

For licensed software, you may need to be a member of a specific group of users in order to access the available central software installations.

If not, you will see an error message as shown below when trying to load the module for the licensed software you would like to use:

.. code:: shell

   You are not part of 'gli_example' group of users that have access to this software.

Creating a software license group
#################################

If a license to use the software on the VSC Tier-1 cluster Hortense hosted by Ghent University is available, the Principal Investigator (PI) of the Tier-1 project should take the following steps to let project members use the license software:

1) Create a dedicated user group that only contains the VSC accounts that should be able to access the licensed software.
   This can be done via the VSC accountpage:

  * Visit https://account.vscentrum.be/django/group/new .
  * Use the "`Create new group`" section at the bottom of the page.
  * Pick a group name that starts with '``xli_``', where '``x``' corresponds to the first letter of the VSC site that your VSC account is connected with. **Note that this letter is prepend automatically to the specified group name!** The '``li_``' infix in the group name allows us to easily discriminate groups that are used to manage access to software licenses.
  * You are free to choose the last part of the group name after '``xli_``', but please keep these guidelines into account:

    * The group name should indicate to which software is is related.
    * The group name should indicate for which research group, or company, etc. it is for.
  * For example: '``gli_soft_grp``' would be a good group name for a licensed software application named '``soft``', and a (UGent) research group named '``grp``'.
  * The VSC account used to create the group will automatically be a moderator of that group, and add additional group members (and moderators), and approve join requests, via https://account.vscentrum.be/django/group/edit .
  * **Note that all members of this group should be allowed to use the licensed software!** It is the responsibility of the group moderators to ensure this is indeed (and remains to be) the case. The Tier-1 support team will not intervene in the management of this software license user group.

2) Contact `compute@vscentrum.be <mailto:compute@vscentrum.be>`_ to request that the users of this group should have access
   to the licensed software, and include the following information:

   * The name of the licensed software that the request relates to.
   * A list of names of centrally installed modules that group members should be able to use.
   * The name of the software license user group.
   * To which Tier-1 project your request relates to.
   * A document that clearly shows that you have a license for the software, or a reference to your project application that includes this already.
   * **Clearly mention that your request relates to the Hortense Tier-1 cluster in the subject of your message.**

Managing a software license group
#################################

To add one or more VSC accounts to an existing software license group:

* A group moderator can add the VSC accounts to the group via https://account.vscentrum.be/django/group/edit.
  A request to effectively join the group will be sent to each added VSC account, which must be approved first.
* A VSC account can submit a group join request via https://account.vscentrum.be/django/group/edit, which must be approved by one of the group moderators.

Likewise, a group moderator can manage the software license group via https://account.vscentrum.be/django/group/edit, by:

* Promoting a group member to group moderator.
* Removing existing group members (or moderators).

.. note:: Take into account that it takes a while (up to 1 hour) before any changes to a user group that were made in the VSC accountpage are active on the Tier-1 system itself.

If an existing software license group should *no longer have access* to central installations of installed software,
please contact `compute@vscentrum.be <mailto:compute@vscentrum.be>`_.

Phase 2
-------

In May 2023 a second phase was installed, adding 48 more nodes to the ``cpu_rome`` partition,
20 extra GPU nodes with double the CPU and GPU memory in the new ``gpu_rome_a100_80`` partition,
and 384 nodes using the newer AMD Milan CPUs called ``cpu_milan``. The `debug_rome` partition was
also made generally available.

The Lustre based scratch storage was also also doubled in volume to a total of 5.4 PB
while increasing the overal throughput as well.

With the new GPU nodes, a renaming of the gpu node partitions occured. Users can most likely
still use the same ``gpu_rome_a100`` partition that now includes all GPU nodes (and only select the
``gpu_rome_a100_40`` or ``gpu_rome_a100_80`` for specific cases, e.g. when requiring the
larger amount of GPU/CPU memory of the ``gpu_rome_a100_80`` nodes).

In the startup period, users are encouraged to try out the ``cpu_milan`` partition to compare performance
and overal functioning with the ``cpu_rome`` partitions. No credits will be billed for the usage of the ``cpu_milan``
partition during this period.

Once in production (July 7th 2023, when the June 2023 cut-off becomes active),
projects will be given access to either the ``cpu_rome`` partitions or the ``cpu_milan`` partition
(with billing of used credits on both partitions).

The support team will try to keep the list of available software modules the same on the ``cpu_rome`` and
``cpu_milan`` partitions. If you notice modules are missing or not functioning properly,
please contact the Tier-1 Hortense support team (see :ref:`hortense_help`).

With both phases active, the cluster crossed the symbolic threshold of 100,000 cores.
However, at the moment there is no partition defined that can be selected to use all cores.
If users can provide a proper case and motivation, you can contact support to request such partition
to give you access to all the available resources.


Gradual decommissioning
-----------------------

End 2025, the gradual decommissioning of Tier-1 Compute Hortense will be initiated.
Around this time, the 4th VSC Tier-1 cluster will become available at the VUB datacenter.

T̵h̵e̵ ̵e̵n̵t̵i̵r̵e̵ ̵R̵o̵m̵e̵ ̵p̵a̵r̵t̵i̵t̵i̵o̵n̵ ̵i̵s̵ ̵e̵n̵d̵ ̵o̵f̵ ̵l̵i̵f̵e̵ ̵N̵o̵v̵e̵m̵b̵e̵r̵ ̵2̵0̵2̵5̵,̵ ̵a̵n̵d̵ ̵w̵i̵l̵l̵ ̵b̵e̵ ̵s̵h̵u̵t̵
d̵o̵w̵n̵ ̵b̵y̵ ̵e̵n̵d̵ ̵2̵0̵2̵5̵.̵
̵T̵h̵i̵s̵ ̵i̵m̵p̵l̵i̵e̵s̵ ̵t̵h̵a̵t̵ ̵t̵h̵e̵ ̵p̵a̵r̵t̵i̵t̵i̵o̵n̵s̵ c̵p̵u̵_̵r̵o̵m̵e̵, c̵p̵u̵_̵r̵o̵m̵e̵_̵a̵l̵l̵,
c̵p̵u̵_̵r̵o̵m̵e̵_̵5̵1̵2̵, d̵e̵b̵u̵g̵_̵r̵o̵m̵e̵ w̵i̵l̵l̵ ̵a̵l̵l̵ ̵d̵i̵s̵a̵p̵p̵e̵a̵r̵.̵
̵D̵e̵p̵e̵n̵d̵i̵n̵g̵ ̵o̵n̵ ̵V̵S̵C̵ ̵p̵l̵a̵n̵s̵,̵ ̵t̵h̵e̵ a̵1̵0̵0̵_̵4̵0̵ p̵a̵r̵t̵i̵t̵i̵o̵n̵ ̵m̵a̵y̵ ̵a̵l̵s̵o̵ ̵d̵i̵s̵a̵p̵p̵e̵a̵r̵.̵
H̵o̵w̵e̵v̵e̵r̵,̵ ̵t̵h̵e̵r̵e̵ ̵c̵u̵r̵r̵e̵n̵t̵l̵y̵ ̵i̵s̵ ̵n̵o̵ ̵c̵o̵n̵f̵i̵r̵m̵a̵t̵i̵o̵n̵ ̵r̵e̵g̵a̵r̵d̵i̵n̵g̵ ̵t̵h̵i̵s̵.̵

Update 1 November 2025: The operational phase of the 4th Tier-1 has, unfortunately, 
suffered a delay. As a result, the VSC is considering to keep the entire Rome 
partition active for a longer time. We are currently awaiting official confirmation on this plan.

Migration to RHEL9 operating system
-----------------------------------

To maintain operational safety, the operating system of Hortense will be updated to **Red Hat Enterprise Linux version 9 (RHEL9)**
(going up from RHEL8).

This implies that by November 2025, when the RHEL8 Rome partition is decommissioned, your software and/or workflow will need to be compliant with the RHEL9 OS if you still want to run jobs.
As of the 2nd cutoff in 2025 (June'25), compatibility of your workflow/software with the new RHEL9 operating system will be a hard requirement.

Please test your workflow and software as soon as possible and ensure that you are ready for this transition.


Update to RHEL9 of Milan partitions
***********************************

We have made separate partitions of workernodes that run RHEL9 as operating systems:
``debug_milan_rhel9`` and ``cpu_milan_rhel9``.

The partition ``cpu_milan_rhel9`` will be gradually increased to contain more nodes of the Milan partition that run RHEL9 as operating system.

To make use of these partitions you can select the ``dodrio cpu_milan_rhel9`` or ``dodrio debug_milan_rhel9`` options in the `Cluster` field in the
`Interactive Apps` forms on the webportal, or from the command line:

.. code:: shell

    module swap cluster/dodrio/cpu_milan_rhel9
    qsub job_script.sh

    module swap cluster/dodrio/debug_milan_rhel9
    qsub job_script.sh


Impact of changes during maintenance of May 2025
************************************************

With the downtime of May 2025, during which significant maintenance was done on the cooling infrastructure,
several changes were made:

* RHEL9 login nodes
* ``cpu_milan_rhel9`` as default partition
* Moving of nodes from ``cpu_milan`` to ``cpu_milan_rhel9`` partition
* Lower memory limits
* OS updates (Linux kernel, GPU drivers, Slurm)

More info in the subsections below.


RHEL9 login nodes
+++++++++++++++++

2 new login nodes running the RHEL9 operating system were added (``login57`` and ``login58``)

- By default, you will land on one of these when logging in via ``tier1.hpc.ugent.be``;
- The RHEL8 login nodes (``login55`` and ``login56``) are still available,
  you can SSH into those via ``ssh tier1-rhel8``;
- From a RHEL8 login node, you can SSH into a RHEL9 login node via ``ssh tier1-rhel9``;
- Warnings will be printed when you swap to a RHEL8 partition on a RHEL9 login node (and vice versa),
  since the software provided via the ``module`` system will not be compatible with the login node
  you are working on:

.. code::

   [vsc40000@login57 ~]$ module swap cluster/dodrio/cpu_rome

    We advise you to log in to a RHEL 8 login node when using the cpu_rome partition.

    The cpu_rome partition is using RHEL 8 as operating system,
    while the login node you are logged in to is using RHEL 9.

    To avoid problems with testing installed software or submitting jobs,
    it is recommended to switch to a RHEL 8 login node by running 'ssh tier1-rhel8'


``cpu_milan_rhel9`` as default partition
++++++++++++++++++++++++++++++++++++++++

The ``cpu_milan_rhel9`` partition was made the default partition (it was ``cpu_rome`` before the maintenance of May'25).

To submit jobs to a Rome partition, you first need to swap to a corresponding partition:

.. code::

   module swap cluster/dodrio/cpu_rome

Moving of nodes from ``cpu_milan`` to ``cpu_milan_rhel9`` partition
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Additional nodes in the Milan partition have been migrated to RHEL9.

Hence, the ``cpu_milan_rhel9`` partition has grown to 128 nodes,
and fewer nodes are available in the ``cpu_milan`` partition now.

Over the next couple of months, additional Milan nodes will be migrated to RHEL9 (see planning below).

Lower memory limits
+++++++++++++++++++

The maximum amount of RAM memory that can be used by jobs has been lowered a bit,
to ensure more memory is available for the operating system (filesystem cache, monitoring, Slurm, etc.).

.. csv-table::

    "**partition**", "**max. mem per node**"

    ``cpu_rome``, ~238GB
    ``cpu_rome_512``, ~488GB
    ``cpu_milan`` + ``cpu_milan_rhel9``, ~238GB
    ``gpu_rome_a100_40``, ~238GB
    ``gpu_rome_a100_80``, ~488GB
    ``debug_rome``, ~224GB
    ``debug_milan`` + ``debug_milan_rhel9``, ~488GB

OS updates (May 2025)
+++++++++++++++++++++

Operating system updates were performed on both RHEL8 and RHEL9 nodes, including a more recent Linux kernel,
updated GPU drivers, and the latest Slurm version (24.05).

Planning for migration to RHEL9
*******************************

* End of June'25: migrate more Milan nodes to RHEL9 (256 nodes in ``cpu_milan_rhel9``, rest in ``cpu_milan``);
* **Thu 28 Aug 2025: complete migration of Milan nodes to RHEL9** (all Milan nodes in ``cpu_milan_rhel9``, none in ``cpu_milan``);
* Nov'25: decommissioning of Rome partition (``cpu_rome``, ``cpu_rome_512``, ``cpu_rome_all``);

Resources
---------

* kick-off meeting (15 March 2022) -
  slides: :download:`download PDF <VSC_Tier-1_Hortense_kickoff_meeting_2022-03-15.pdf>` -
  recording: `watch on YouTube <https://www.youtube.com/watch?v=ENQrgMc2BAY>`__
* phase 2 kick-off meeting (26 March 2023) -
  slides: :download:`download PDF <VSC_Tier-1_Hortense_phase-2_kickoff_meeting_2023-05-26.pdf>` -
  recording: `watch on YouTube <https://www.youtube.com/watch?v=kH9XZZntc8U>`__

.. _hortense_help:

Getting help
-------------

For questions and problems related to Tier-1 Hortense, please contact the central
support address for Tier-1 compute: `compute@vscentrum.be <mailto:compute@vscentrum.be>`_.