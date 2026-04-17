.. _sofia cluster:

sofia @ VUB-HPC
===============

.. contents::
    :depth: 3
    :local:
    :backlinks: none

General information
-------------------

**sofia** is the 4th VSC Tier-1 cluster, following *muk* (hosted by HPC-UGent, 2012-2016),
*BrENIAC* (hosted by HPC-Leuven, 2016-2022) and *Hortense* (hosted by HPC-Ugent, 2021-2026).

It will be available in the second half of 2026, is hosted by Vrije Universiteit Brussel,
and maintained and supported by the VUB-HPC team.

.. _sofia_hardware_details:

Hardware details
----------------

The **sofia** cluster consists of the following partitions:

- ``zen5_dense``: CPU partition:
   - 56 workernodes, each with:
       - 2x AMD EPYC 9965 192-Core CPU (Turin Dense) 2.25 GHz ("Zen 5c" microarchitecture, 384 cores per node)
       - 770 GiB usable RAM (~2 GiB/core), 7.6 GiB swap (local SSD)
       - 1.4 TiB SSD local disk
- ``zen5_himem``: large-memory partition:
   - 16 workernodes, each with:
       - 2x AMD EPYC 9655 96-Core CPU (Turin) 2.6 GHz ("Zen 5" microarchitecture, 192 cores per node)
       - 1.5 TiB usable RAM (~8 GiB/core), 7.6 GiB swap (local SSD)
       - 1.4 TiB SSD local disk
- ``zen4_h200``: GPU partition:
   - 22 workernodes, each with:
       - 2x AMD EPYC 9654 96-Core CPU (Genoa) 2.4 GHz (192 cores per node)
       - 8x NVIDIA H200-SXM5 (141 GiB GPU memory), Nvlink4
       - 1.5 TiB usable RAM (~8 GiB/CPU core), 7.6 GiB swap (local SSD)
       - 1.4 TiB SSD local disk
- ``zen5_vis``: interactive and debug partition:
   - 4 workernodes, each with:
       - 2x AMD EPYC 9655 96-Core CPU (Turin) 2.6 GHz ("Zen 5" microarchitecture, 192 cores per node)
       - 2x NVIDIA RTX 5000 Ada Generation (32 GiB GPU memory)
       - 1.5 TiB usable RAM (~8 GiB/CPU core), 7.6 GiB swap (local SSD)
       - 1.4 TiB SSD local disk

Shared infrastructure:

- *storage*: 4.3 PiB shared scratch storage, IBM Storage Scale System;
- *interconnect*: NVIDIA Quantum-2 InfiniBand, fat tree network with 2:1 blocking
   - ~400 Gb/s for GPU and large-memory partition
   - ~200 Gb/s for CPU partition

.. _sofia_getting_access:

Getting access
--------------

.. _sofia_access_policy:

Access policy
*************

**The sofia VSC Tier-1 cluster can only be accessed by people with an active Tier-1 compute project.**

Tier-1 compute project resources are always allocated for a given period.
After this period expires, the users of this project lose access to all resources granted within that project.
This includes storage in addition to compute resources (CPU and GPU).

As soon as a project expires, project members:

* will no longer be able to use any remaining CPU cycles, GPU cycles or credits
* will no longer have access to the dedicated project folders
* will lose access to the Tier-1 cluster, unless they have another active project

See https://www.vscentrum.be/compute for more information on requesting access, rules and regulations.


.. _sofia_login_nodes:

Login nodes (SSH)
*****************

You can use SSH to connect to the login nodes of the Tier-1 **sofia** cluster with your VSC account:

* from the public internet, use ``sofia.hpc.vub.be``

More general information about SSH login is available in the
:ref:`terminal
interface` section. Note that for access from abroad an extra step is needed. See the VUB tab at
:ref:`location_access_restrictions`.

There are 2 login nodes for **sofia**: ``login01`` and ``login02``, both having Rocky Linux release 9.7 as operating system.
When logging in using SSH, you will be assigned to either of these login nodes,
based on the IP address of the host you are connecting from.

If you need to access a *specific* login node (for example because you have a ``screen`` or ``tmux`` session
running there), just run "``ssh login01``" to jump to ``login01`` if you were logged in to ``login02``,
or vice versa. Make sure your ssh keys are properly configured or forwarded.

.. note::
  The available resources on the **sofia** login nodes are shared by everyone that is logged in there.

  **Please only use the sofia login nodes as an access portal!**

  For resource-intensive interactive tasks, like software compilation, testing software or job scripts, etc.,
  please use an interactive job, either via ``salloc`` and in the future through the :ref:`sofia_web_portal`.

.. _sofia_login_nodes_host_keys:

Host keys
+++++++++

The first time you log in to the **sofia** login nodes, a fingerprint of the host key will be shown.
Before confirming the connection, verify the correctness of the host key, to ensure you are
connecting to the correct system.

**Please verify that the fingerprint of the host key is *one* of the following**:

* for ECDSA host key:

  * ``78:2f:bd:30:95:7f:ba:eb:c4:bf:29:71:fd:1f:2b:b7`` (MD5)
  * ``Trw7Gwirs3k9QdH2n2fB9NGrNKPwG8mVK3Yfy8VPc2Y`` (SHA256)

* for ED25519 host key:

  * ``bf:4d:d3:55:ce:72:cd:dd:a7:bf:44:62:97:5f:22:2d`` (MD5)
  * ``IPZeanj7AVbBYFyc1KBFfd+hMxyDbIGyOghn2uQkuww`` (SHA256)

* for RSA host key:

  * ``5e:2e:21:11:c6:8e:1e:1f:c9:7c:d2:38:c7:f6:f9:35`` (MD5)
  * ``vS9fAoDO52dWCXS/obPS5u95irhJiKo1PfV4dyJl2Mg`` (SHA256)

The type of fingerprint that will be shown depends on the version and configuration of your SSH client.

.. _sofia_web_portal:

Web portal
**********

The **sofia** web portal will not yet be available during the pilot phase.

More information about the usage of the web portal is available at :ref:`compute portal`.

.. _sofia_scratch_globus:

sofia scratch via Globus
************************

Accessing the **sofia** scratch via Globus will not yet be possible during the pilot phase.

More general information about Globus is available at :ref:`globus platform`.

.. _sofia_help:

Getting help
-------------

For questions and problems related to Tier-1 **sofia**, please contact the central
support address for Tier-1 support: `support@vscentrum.be <mailto:support@vscentrum.be>`_.

Questions regarding Tier-1 Hortense will need to go to: `compute@vscentrum.be <mailto:compute@vscentrum.be>`_.
