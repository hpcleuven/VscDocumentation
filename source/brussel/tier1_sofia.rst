.. _sofia cluster:

.. grid:: 2
   :class-container: bg-transparent

   .. grid-item::

      .. image:: images/sofia-sun.png
         :width: 98%
         :class: bg-transparent

   .. grid-item::

      .. image:: images/sofia-supercomputer-logo.png
         :width: 100%
         :class: only-light bg-transparent sd-my-2

      .. image:: images/sofia-supercomputer-logo-light.png
         :width: 100%
         :class: only-dark bg-transparent sd-my-2

###############
sofia @ VUB-HPC
###############

**sofia** is the 4th VSC Tier-1 cluster, following *muk* (hosted by HPC-UGent, 2012-2016),
:ref:`BrENIAC<breniac hardware>` (hosted by HPC-Leuven, 2016-2022) and
:ref:`Hortense<Hortense hardware>` (hosted by HPC-Ugent, 2021-2027).

It is in production since July 7th 2026 and is hosted by Vrije Universiteit Brussel.

.. _sofia_help:

Getting help
============

Any questions, comments or problems related to Tier-1 **sofia** can be addressed to the central
support for VSC Tier-1 services:

.. card::
   :width: 50%
   :margin: 2 4 auto auto
   :text-align: center

   .. button-link:: mailto:support@vscentrum.be
      :color: info
      :expand:

      :fa:`envelope` **support@vscentrum.be**

Questions regarding Tier-1 Hortense should be send to:
`compute@vscentrum.be <mailto:compute@vscentrum.be>`_.

.. _sofia_hardware_details:

Hardware details
================

The **sofia** cluster consists of the following compute partitions:

===================  =============================  ============================  =============================  ===============================
Slurm partition      ``zen5_dense``                 ``zen5_himem``                ``zen4_h200``                  ``zen5_vis``
===================  =============================  ============================  =============================  ===============================
**Nodes**            56                             16                            22                             4
**GPUs per node**                                                                 8x `NVIDIA H200`_ (Hopper)     2x `NVIDIA RTX 5000 Ada`_ (Ada)
**GPU memory**                                                                    140 GB                         32 GB
**CPUs per node**    2x 192-core `AMD EPYC 9965`_   2x 96-core `AMD EPYC 9655`_   2x 96-core `AMD EPYC 9654`_    2x 96-core `AMD EPYC 9655`_ 
                     |br| (Zen5c Turin)             |br| (Zen5 Turin)             |br| (Zen4 Genoa)              |br| (Zen5 Turin)
**CPU memory**       742 GB                         1493 GB                       1493 GB                        1493 GB
                     |br| 1.9 GB/core               |br| 7.7 GB/core              |br| 7.7 GB/core               |br| 7.7 GB/core
**Local disk**       1.4 TB SDD                     1.4 TB SDD                    1.4 TB SDD                     1.4 TB SDD
**Interconnect**     200 Gbps                       400 Gbps                      800 Gbps                       400 Gbps
                     |br| NDR-IB                    |br| NDR-IB                   |br| NDR-IB                    |br| NDR-IB
===================  =============================  ============================  =============================  ===============================

Shared infrastructure:

- *storage*: 4.3 PiB shared scratch storage, IBM Storage Scale System
- *interconnect*: NVIDIA Quantum-2 InfiniBand, fat tree network with 2:1 blocking

.. _sofia_getting_access:

Getting access
==============

The **sofia** VSC Tier-1 cluster can only be accessed by people with an active
`Tier-1 compute project <https://www.vscentrum.be/compute>`__ .
Everyone is welcome to request a *starting grant* or *collaborative grant* to
apply for their Tier-1 compute project.

.. _sofia_web_portal:

Web portal
----------

The Tier-1 cluster **sofia** has its own :ref:`OnDemand Web Portal<compute
portal>`. Users with an active project in **sofia** can access it at `sofia
OnDemand`_.

.. card::
   :width: 50%
   :margin: 2 4 auto auto
   :text-align: center

   .. button-link:: https://portal.sofia.vub.be/
      :color: primary
      :expand:

      web portal: :fas:`circle-play` **sofia OnDemand**

More information about the usage of the web portal is available at
:ref:`compute portal`.

.. _sofia_terminal_ssh:

Terminal interface
------------------

You can use SSH to connect to the :ref:`terminal interface<terminal interface>`
of the Tier-1 cluster **sofia** with your VSC account. 

.. card::
   :width: 50%
   :margin: 2 4 auto auto
   :text-align: center

   **login.sofia.vub.be**

There are two ways to authenticate with SSH to **sofia**, with an :ref:`SSH
key<ssh keys>` in your VSC account page or with :ref:`Multi-factor
Authentication (MFA)<mfa_login>`. Different restrictions apply to each:

SSH certificates with MFA
    Set up your SSH connection to connect to **sofia** with your VSC ID and a
    SSH certificate via MFA as described in :ref:`mfa-with-ssh-agent`.
    You can connect to **sofia** from any Belgian public network with this
    method of authentication.

SSH keys in VSC Account Page
    Configure your :ref:`SSH client<terminal ssh>` as you have already done for
    other VSC Tier-2 clusters to connect to **sofia** with your
    VSC ID and your SSH key of choice in your VSC account page.
    This method of authentication is restricted to the Flemish university
    networks. This means that you need to connect to **sofia** from within your
    university premises, use your university :ref:`VPN<vpn>` or connect from
    another VSC Tier-2 compute cluster.

.. sealso::
   
   Access from abroad requires additional permissions. See the instructions
   related to VUB at :ref:`location_access_restrictions`.

Login nodes
^^^^^^^^^^^

There are 2 login nodes in **sofia**: ``login01`` and ``login02``.

Upon login you will be assigned to either of these login nodes. If you need to
access a *specific* login node (for example because you have a ``screen`` or
``tmux`` session running there), you can jump between login nodes with the
commands ``ssh login01`` or ``ssh login02``. Make sure your SSH keys are
properly forwarded with an :ref:`SSH agent<OpenSSH agent>`.

.. warning::

   Compute intensive tasks are not allowed on the login nodes. Please use an
   interactive job, preferentially on the ``zen5_vis`` partition, either via
   ``salloc -p zen5_vis`` or through the :ref:`sofia_web_portal`.

.. _sofia_login_nodes_host_keys:

SSH Host keys
^^^^^^^^^^^^^

The first time you log in to the **sofia** login nodes, a fingerprint of the
host key will be shown. Before confirming the connection, please verify the
correctness of the host key to ensure you are connecting to the correct system.

The fingerprint that will be shown depends on the version and configuration of
your SSH client, check that the one shown corresponds to one of the following:

* for ECDSA host key:

  * ``78:2f:bd:30:95:7f:ba:eb:c4:bf:29:71:fd:1f:2b:b7`` (MD5)
  * ``Trw7Gwirs3k9QdH2n2fB9NGrNKPwG8mVK3Yfy8VPc2Y`` (SHA256)

* for ED25519 host key:

  * ``bf:4d:d3:55:ce:72:cd:dd:a7:bf:44:62:97:5f:22:2d`` (MD5)
  * ``IPZeanj7AVbBYFyc1KBFfd+hMxyDbIGyOghn2uQkuww`` (SHA256)

* for RSA host key:

  * ``5e:2e:21:11:c6:8e:1e:1f:c9:7c:d2:38:c7:f6:f9:35`` (MD5)
  * ``vS9fAoDO52dWCXS/obPS5u95irhJiKo1PfV4dyJl2Mg`` (SHA256)

.. _sofia_access_policy:

Access and retention policy
---------------------------

The resources of a Tier-1 compute project are always allocated for a given
period of time. Once the project expires, users of the project will not be able
to use any more resources granted within that project.

.. attention::

   Data retention of project data is 90 days.

Use of resources stops at the end of the day of the last day of the project.
Users of the project will still be able to access their data for 60 days after
that date. The following details the changes at each stage once a project ends:

End date of the project:
    * :fas:`times` SSH login to **sofia**
    * :fas:`times` OnDemand Web portal of **sofia**
    * :fas:`times` write data to **sofia** project directory
    * :fas:`check` read data in **sofia** project directory via :ref:`Globus <sofia_globus>`
    * :fas:`check` read data in **sofia** home directory via :ref:`Globus <sofia_globus>`

60 days after end of project:
    * :fas:`times` read data in **sofia** project directory via :ref:`Globus <sofia_globus>`
    * :fas:`times` read data in **sofia** home directory via :ref:`Globus <sofia_globus>`

90 days after end of project:
    * :fas:`times` all project data in **sofia** deleted

.. seealso::

   More information on requesting access, rules and regulations can be found in 
   https://www.vscentrum.be/compute

.. _sofia_login_nodes:

Storage
=======

The Tier-1 cluster **sofia** has 4.3 PiB of very fast storage. This is a shared
storage available on all login and compute nodes of the cluster. It is used to
provide scratch storage for jobs (*i.e.* project directories), as well as
user's home directories and it also holds the installations of scientific
software.

.. _sofia_globus:

Globus on sofia
---------------

The **sofia** scratch storage can be accessed via the :ref:`globus platform`.
You can find the link to the endpoints of **sofia** in Globus in the link
below.

.. card::
   :width: 50%
   :margin: 2 4 auto auto
   :text-align: center

   .. button-link:: /globus/collections.html#id3
      :color: secondary
      :expand:

      :fas:`cloud-upload-alt` **sofia Globus Collections**

.. note::

   Remember to back up your project data in **sofia**. Data will be deleted 90
   days after the project has expired. See our
   :ref:`retention policy<sofia_retention_policy>`.

.. _sofia_job_submission:

Home directory
--------------

The user’s ``$HOME`` directory in **sofia** is located on its own scratch file
system and is distinct from the user’s ``$VSC_HOME`` found in other Tier-2
clusters.

Therefore, users will have a default account setup upon their first login to
**sofia**. If you want copy any configuration files or customizations (*e.g.*
``.bashrc`` or any other dot files) from your Tier-2 cluster, you can do so
through :ref:`Globus <sofia_globus>`.

One advantage of this setup is that **sofia** remains accessible even if the
Tier-2 infrastructure on the user’s home institution is down.

VSC_DATA
--------

Your ``$VSC_DATA`` storage, which is hosted in your home institute, is not
directly accessible from **sofia**.

Users can access their ``$VSC_DATA`` storage with  :ref:`Globus <sofia_globus>`
and transfer any needed data in there to their project directory in the scratch
storage of **sofia**.

Node-local scratch
------------------

Each node in the cluster, including the login nodes, provides local storage for
temporary data that is not shared or visible to other users.

* Temporary storage on local node hard drive: ``$VSC_SCRATCH_NODE``, ``$TMPDIR``, ``/tmp`` and ``/var/tmp``
* Temporary storage on local node memory (RAM): ``/dev/shm``

.. note::

   Data placed in any of these temporary storage locations will be **deleted
   at the end of the active session**. For compute nodes this is at the end
   of your job and for login nodes whenever you log out of the cluster.

Job submission
==============

The Tier-1 cluster **sofia** uses the :ref:`Slurm job scheduler<running jobs>`.
Only Slurm-native commands are supported for managing your jobs.

Users must specify one of the available :ref:`partitions <sofia_hardware_details>` when submitting jobs.
Loading a ``cluster`` module is not required.

.. _sofia_job_environment:

Job environment
---------------

In **sofia**, both batch and interactive jobs start in a clean session environment. This
differs from the default Slurm behavior (``--export=ALL``). This approach
provides the following advantages:

* **reproducibility**: your jobs run consistently regardless of your current shell state
* **architecture alignment**: software modules will always be loaded for the
  hardware architectures in use, ensuring access to the correct and
  optimized software binaries

Propagating specific environment variables to your job can be done with the
``--export=<environment_variables>`` option in Slurm. See :ref:`slurm_job_env`
for more information.

If your workflow requires your full shell environment to be propagated, please
refer to the VUB-HPC documentation on `how to copy your full shell environment into your job
<https://hpc.vub.be/docs/faq/advanced/#how-can-i-copy-the-login-shell-environment-to-my-jobs>`__.

.. _sofia_job_memory:

Job memory
^^^^^^^^^^

The CPU memory allocated to Slurm jobs scales linearly with the
number of allocated CPU cores. See :ref:`sofia_hardware_details` for the
memory per core available in each partition.

All jobs must use the default memory allocation. Memory overrides ``--mem``,
``--mem-per-cpu``, and ``--mem-per-gpu`` are not allowed and will cause a job
submission error.

This policy avoids situations where CPU cores are available but cannot be
allocated because insufficient memory remains available on the node. It also
helps keep benchmark results representative of production runs by ensuring that
all jobs follow the same linear memory-per-core allocation.

.. _sofia_job_gpu:

GPU jobs
^^^^^^^^

In the ``zen4_h200`` partition, Slurm jobs are allocated a fixed ratio of
``24`` CPU cores per GPU (1/8 of the CPU cores on a node).  Job requests
that do not follow this ratio will be rejected.

We recommend the following ``#SBATCH`` directives to request GPU resources.
The example below requests 2 GPUs on a single node, with 1 task allocated per
GPU (2 tasks in total) and 24 CPU cores per task (48 cores in total):

.. code-block:: bash

   #SBATCH --partition=zen4_h200
   #SBATCH --nodes=1
   #SBATCH --gpus-per-node=2
   #SBATCH --ntasks-per-gpu=1
   #SBATCH --cpus-per-task=24

This policy avoids situations where GPUs are available but cannot be allocated
because insufficient CPU cores available on the node. It also helps keep
benchmark results representative of production runs by ensuring that all jobs
use the same core-to-GPU ratio.

