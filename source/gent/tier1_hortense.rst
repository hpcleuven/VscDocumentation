Hortense @ HPC-UGent
====================

.. warning::

    This documentation is still being completed.

    More information and details will be added in the coming days.

    In case of questions, please contact `compute@vscentrum.be <mailto:compute@vscentrum.be>`_.

.. contents::
    :depth: 3
    :local:
    :backlinks: none

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

.. _hortense_getting_access:

Getting access
--------------

**The Hortense VSC Tier-1 cluster can only be used by people with an active Tier-1 compute project.**

See https://www.vscentrum.be/compute for more information on requesting access.

To access the Tier-1 Hortense cluster use the `web portal <https://tier1.hpc.ugent.be/>`_,
or use SSH to connect to the dedicated login node with your VSC account:

* from the public internet, use ``tier1.hpc.ugent.be``
* from within the VSC network, use ``tier1.gent.vsc``

You can find more information about the usage of the web portal in chapter "8 Using the HPC-UGent web portal"
in the `HPC Ugent tutorials <https://www.ugent.be/hpc/en/support/documentation.htm>`_

More general information about SSH login is available at :ref:`acccess_data_transfer`.

.. note::
  The ssh key of the login nodes changed. If you get a message like this (or similar):
    | ``@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@``
    | ``@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @``
    | ``@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@``
    | 
    | ``IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!``
    | ``Someone could be eavesdropping on you right now (man-in-the-middle attack)!``
    | ``It is also possible that a host key has just been changed.`` 
  or like this (or similar):
    | ``WARNING - POTENTIAL SECURITY BREACH!``
    | ``The server's host key does not match the one PuTTY has''
    | ``cached in the registry. This means that either the``
    | ``server administrator has changed the host key, or you` 
    | ``have actually connected to another computer pretending``
    | ``to be the server.``
  Then you have to check whether the new fingerprint of the host key is one of the following:
    | ``SHA256:1Q6syHAJnrybhPJPX87gmLKsKRUVDZAy+5N96RbELBg`` 
    | ``90:c7:d5:29:b3:c8:8c:fc:d4:c6:d7:14:68:bc:0a:7b``
    | ``SHA256:IPfUtYyl12Vr+1QEb53uoNq4DzaIPUGipWunNjwVpwI``
    | ``d0:8e:19:5a:bb:dc:32:45:53:82:ed:ae:10:07:83:72``
    | ``SHA256:B8R1oVM02ikstqnwBAvvM0CH7cZxvwWuek/BroqNoxI``
    | ``53:48:19:2b:bf:e2:a3:e7:45:a9:cd:fe:83:c3:98:a1``
  If it is a match then you can remove or replace the old key.

.. note::
  There are currently two small login nodes (each with 8 CPU cores and 64GB RAM) available. An user from 
  the same IP address weould always end up the same one (login55 or login56). 

  **Please only use the login node as an access portal!**

  For resource-intensive tasks, like software compilation, testing job scripts, etc., please use the debug partitiuon.

.. note::
  To access your data on your (project) scratch using Globus is possible via the `VSC UGent Tier2` endpoint.

  More general information about Globus is available at :ref:`managing_and_transferring_files`.

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

System-specific aspects
-----------------------

Project storage
***************

* Please be aware that storage space on $VSC_SCRATCH is limited per user to 3 GB.
* Instead, it is better to use the dedicated scratch storage space which is reserved for every Tier1 project.
* The environment variable $VSC_SCRATCH_PROJECTS_BASE points to the basefolder containing all project spaces.
* Project space is given the same name as your project.
* You can e.g. use this command to directly switch to your dedicated project space:

.. code:: shell

  cd $VSC_SCRATCH_PROJECTS_BASE/<yourprojectnamehere>


Read only filesystem
********************

The performance of the filee system is not always optimal in case of small files often read without
writing them (software stack, certain input files, for example ones for DNA sequencing). 
For those files we defined a read-only partition (mirroring the whole network file system). 
To access this read-only partition you have to simply suffix the path with ``/readonly``, 
for example use ``/readonly/$VSC_SCRATCH_PROJECT_BASE`` instead of ``$VSC_SCRATCH_PROJECT_BASE``.
Please be aware that we only update the read-only partition every half an hour on the login noodes,
and on the worker nodes every times when a job starts. For exmaple, if you place a file, for example,
to ``$VSC_SCRATCH_PROJECT_BASE/<project>/<file>`` on the login node, it would only appear at 
``/readonly/$VSC_SCRATCH_PROJECT_BASE/<project>/<file>`` up to 30 minutes later, or on the worker nodes
if a job starts. Please note that we do not update the read-only partition during a job, so nothing what you 
write during your simulation will appear there. 

We do advise to use the read-only partition whenever is possible, as it can seriouly speed up simulations.

.. note::
  If you have used hard-coded software paths before, or you linked your own software against the centrally 
  installed software, we advise to use EasyBuild iebvironmental variables ($EBROOT...) set by ``module load`` 
  commands, and you might have to recompile your software to achieve better performance.

Storage quota usage
*******************

* You can check personal and project storage quota usage by running the ``my_dodrio_quota`` command.
* If you want to check storage quota for specific projects, or for projects that are not listed automatically, use the ``-p`` option.
* For a list of all options, run ``my_dodrio_quota -h``.

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

Debug Partition
###############

Foo bar baz

Limitations for jobs
++++++++++++++++++++

Maximum walltime
################

The maximum walltime that jobs can request is 3 days (72 hours): ``-l walltime=72:0:0``.

Jobs that request more walltime will be refused by the resource manager at submission time ("``Requested time limit is invalid``").

.. _scientific_software:

Scientific software
*******************

A central software stack with a rich set of scientific libraries, tools, and applications
is available via the ``module`` command, and was installed using `EasyBuild <https://easybuild.io>`_.

Use ``module avail`` to see which software versions are available,
and load one or more modules via the ``module load`` command to start using them.

If software that you require is missing, please submit a software installation request
via https://www.ugent.be/hpc/en/support/software-installation-request .

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

Resources
---------

* kickoff meeting (23 Nov 2021) -
  slides: :download:`download PDF <VSC_Tier-1_Hortense_kickoff_meeting_2021-11-23.pdf>` -
  recording: `watch on YouTube <https://www.youtube.com/watch?v=o0kNNsNT_rs>`_

Getting help
-------------

For questions and problems related to Tier-1 Hortense, please contact the central
support address for Tier-1 compute: `compute@vscentrum.be <mailto:compute@vscentrum.be>`_.
