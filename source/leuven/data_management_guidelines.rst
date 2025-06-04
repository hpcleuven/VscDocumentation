.. _KU Leuven data management guidelines:

==============================
HPC data management guidelines
==============================

About
=====

This page offers guidelines on how to manage your data on the different storage platforms which VSC and KU Leuven have to offer and how to transfer data between them. While most of these guidelines can be applied to any storage available to you, the focus will lie on shared storage related to KU Leuven (e.g. staging storage, Tier-1 Data / Mango, L-drive, other local shared storage).

This page is structured as follows:

#. Choosing the right types of storage

#. Tips for your data management plan

#. Structuring your files and directories

#. Data outflow to long-term storage

#. Keeping track of your data


Choosing the right types of storage
===================================

You will normally require at least the following two kinds of storage:

- storage which is integrated in the HPC infrastructure
- external storage where you can move data to on which you are not actively computing anymore

HPC storage
-----------
Carefully consider which type(s) of HPC storage are best suited for your work. The different VSC clusters all offer a :ref:`set of HPC storage locations<data location>`. For the Tier-2 clusters hosted at KU Leuven this is supplemented with so-called 'staging' storage. Staging uses the same (Lustre based) platform as the scratch storage and is also intended for larger amounts of data. Compared to scratch storage, however, staging is better suited for data which:

- either needs to be shared by multiple users in a research project
- and/or should not be subjected to the automatic cleanup

Note that staging (even in the absence of automatic cleanup) should not be considered as a 'safe' storage location. Just like scratch, staging is single-copy and does not offer snapshots or backups. If somebody accidentally removes data or an unexpected system failure removes or corrupts data, this data is gone forever.

Also keep in mind that staging is a paid service (charged based on peak usage per month) while temporarily increasing your scratch quotum can be done for free. If you only need more workspace for your own calculations, it may therefore be more advantageous to ask for a higher scratch quotum than to make more use of staging. For all storage related requests, see the `HPC Service Catalog <https://icts.kuleuven.be/sc/onderzoeksgegevens/english-version/HPC-storage>`_.

External storage
----------------
As a general rule, data should be removed from HPC storage once it is no longer needed in further computations or postprocessing. Usually at least part of this data needs to be preserved for e.g. possible future reanalysis, sharing with other researchers, publication, et cetera. Such data then first needs to be copied to external storage (a process typically referred to as 'outflow'). Carefully consider your choice of external storage, in particular when it comes to (long-term) data safety, pricing, and how well it can be reached from within the HPC environment. Your options may include:

- 'in-house' storage managed in your research group or department
- KU Leuven archive storage (K-drive) or large volume storage (L-drive)
- ManGO or Tier-1 data
- cold storage (`FriGO <https://rdm-docs.icts.kuleuven.be/frigo/index.html>`_)

For more information, please consult the `KU Leuven storage guide <https://icts.kuleuven.be/storagewijzer/en>`_.


Tips for your data management plan
==================================

The `RDM Data Management Plan (DMP) documentation pages <https://www.kuleuven.be/rdm/en/guidance/dmp>`_ offer extensive documentation, examples and tools for setting up your DMP. For projects which involve HPC, we recommend to also consider the following:

- Map your dataflow:
  where is your data coming from? Which data gets generated on the cluster? What needs to be deleted and what needs to be be kept? Where should that data be preserved?
- Estimate your needed storage capacity:
  what is the maximum storage volume you will need at any given point in time? Note that this will be less than the sum of all datasets involved if you plan to (re)move data in between different stages of your project.
- Identify shared resources to avoid duplication:
  this could be shared input data, enriched databases, shared software installations, ...
- Identify opportunities for automation:
  is it possible to automatically download your input data, process it and then remove the input data all within your compute job? Is it possible to periodically sync to (safe) external storage in an automatic way? Even if such parts of your workflow have not yet been automated, knowing what possibilities exist may allow more informed decisions on for example directory structure.

Many of these points will be discussed in more detail in the sections below.

We recommend to gather your research team to draw the outlines of the DMP. Especially when multiple people will be using the stored data, there will be different workflows and preferences. Consider inviting the following people:

- the PI(s): for a vision on past, current and future projects and how they are related
- at least some of the researchers using the HPC: they understand the day-to-day needs on the cluster
- data support staff: for their technical expertise


Structuring your files and directories
======================================

It is worth spending some time on a suitable directory structure and file naming convention for your project, especially in the case of shared storage. We recommend to agree on a clear approach within your team (e.g. definining in advance which directory structure to use). This helps to avoid loosing data in scattered directories which multiple users would otherwise tend to create. This is best clearly documented so that any new collaborators can also follow these guidelines.

Many best practices are already described on the `RDM file organization <https://www.kuleuven.be/rdm/en/guidance/data-standards/file-organisation>`_ page. One of the main points is to have a logical hierarchy with higher level broader topics and more specific folders within. A simple structure that tends to work well is to have a top-level directory for the research project which contains a subdirectory for each collaborator (possibly based on VSC IDs). Individual experiments can then be placed in separate directories within the user's subdirectory. If needed, related projects can be placed in a common parent directory.

As mentioned before, also think about where (shared) data and software are best located. Input datasets, enriched databases and software may be specific to one experiment or be used across different projects (and everything in between) and their position in the hierarchy should reflect this.

Your backup/outflow strategy may also partly determine what is the most appropriate structure. Ideally, such a sync to external storage should be a fairly straightforward operation (e.g. just a single command). In case you want to transfer all project data (inputs, outputs, intermediary files, ...) then that will be easy to do. When you only want to transfer certain types of data (for example only the outputs), however, then certain directory structures might be more convenient than others. This of course also depends on features supported by your transfer tool (rsync / irsync / mango_ingest / Globus CLI / ...) such as the ability to include or exclude certain directory patterns.

When working with sensitive data, one more point to consider is that access restrictions are easiest to handle high up in the hierarchy (e.g. at the project level). If you need additional guidance in for example setting the right permissions and ownerships, don't hesitate to reach out to our `service desk <hpcinfo@kuleuven.be>`_


Location of software
--------------------
Aside from regular data, also local software installations can be placed on shared storage such as staging. In general we recommend to only do this when really required, i.e. when a large or complex software installation needs to be shared between different users. Software which is only for your own use is best left in a non-shared location such as your ``$VSC_DATA``. Keep in mind that most software can be offered as centrally installed modules (send your requests to the `service desk <hpcinfo@kuleuven.be>`_).

A few more things to keep in mind:

- When developing software with multiple people, it may sound tempting to place the code on shared storage for this purpose. A much better practice, however, is to stick to personal copies in combination with a suitable :ref:`version control system <version control systems>`. Know that ICTS offers `a yearly course on version control <https://admin.kuleuven.be/icts/opleidingen/opleidingsaanbod/version-control-hybrid>`_ and that KU Leuven also hosts `an own GitLab instance <https://gitlab.kuleuven.be/>`_.

- Conda environments tend to take up a lot of disk space as well as inodes (number of files and directories). Inode counts can be strongly reduced by installing such environments in a :ref:`container <hpc containers>`.

- Carefully consider where to place your software installations in your directory structure. Ask yourself e.g. whether or not the software needs to be available to the whole group and whether it will be used for a single research project or across several ones. In general, software installation directories are best well separated from other types of data in your project.


Data outflow to long-term storage
=================================

Two more points are worth considering with regards to outflow: (1) selecting which data to transfer and (2) which transfer tools to use.

Which data needs to be moved to external storage?
-------------------------------------------------
Your HPC storage may contain a variety of data (publicly available datasets, measurements from your instruments, generated output data, intermediate files, et cetera). While you could just move everything to your external storage, we recommend to only transfer the data which **really** needs to be preserved after the active computation phase. Aside from reducing your storage demands and associated costs, this also improves searchability. This triage is best done before your outflow activities (transferring everything first and cleaning up later usually means the cleanup does not get done). If data meets any of the following criteria, then it is likely to be a good candidate for outflow:

- Data which is expensive to regenerate in terms of compute time, transfer time and/or human effort.
- Data which needs to be shared with people without access to VSC facilities, such as external partners in a research project or the general public (for example through :ref:`Globus <globus-sharing>` or `KU Leuven RDR <https://www.kuleuven.be/rdm/en/rdr>`_).

Examples of data which are not well suited for outflow include the following:

- Source code: this is best handled via (version controlled) software repositories instead, such as GitHub or GitLab.
- Compiled software: rather than storing the binaries (which can have various requirements which may not be satisfiable in the future), it is best to store your installation recipes and logs instead.
- Public databases: if data is already available elsewhere, then additional copies are normally not needed.
- Work in progress: parts such as individual experiments that are still undergoing regular changes are better only processed once ready. It may be useful to use directory names such as ``tmp_...`` or ``wip_...`` for such cases and let your sync tool skip such directories by default.

Also keep in mind that external storage can function as a (temporary) intermediary, for example:

- If the data still needs to be processed further, but you need to free some space for other (more urgent) projects or experiments.
- If the data needs to be used on different HPC sites, possibly with some delay in between (e.g. production runs on Tier-1 followed by postprocessing on Tier-2).
- If the data is publicly available but download times are too high, in which case you would benefit from a nearby 'cache'.

Data transfer tools
-------------------
There are multiple ways in which you can transfer data to or from HPC storage:

- Globus: either through its :ref:`web <globus-web>` or :ref:`command-line <cli>` interface. Multiple :ref:`managed collections <globus-collections>` exist, including collections for ManGO, Tier-1 Data and KU Leuven network drives. If no managed collection exists (e.g. for a local hard disk), you can still create a :ref:`local endpoint <globus-local-endpoints>`. For more information, please see the :ref:`Globus documentation pages <globus platform>`.
- iCommands/Python iRODS client/ManGO Portal: tools allowing data transfers to and from an iRODS-managed platform (i.e. ManGO and Tier-1 Data). For more information, please see the :ref:`corresponding research data page <clients>`.
- Classic command-line tools (such as ``rsync`` and ``sftp``) and various GUI applications (see also the :ref:`data transfer page <data transfer>`).


Keeping track of your data
==========================

Once multiple storage locations are involved, you will need to keep an overview of where everything is located (e.g. which input data has been staged in on HPC storage, which data has flowed out, et cetera). We advise to include this topic in your project meetings (e.g. the current status, planned data transfers and cleanups, possible quota constraints, ...) and to monitor disk usage on a regular basis. For HPC storage you can use command-line tools such as ``du`` and ``myquota``. For staging storage we also offer ``duduckdb``, which allows you to query a database with information on the disk usage for your staging directory.

Automating (part of) your data operations can of course be helpful in this regard. One possibility to consider is to automatically transfer and/or clean up data as part of your compute jobs. Automation of course tends to require well-defined directory structures (see above).

Including sufficient metadata is also essential. Even basic approaches such as README files will already be helpful (e.g. with information about the project or experiment and with references to relevant publications and repositories). Certain middleware such as :ref:`iRODS <metadata>` (used in ManGO and Tier-1 Data) offer a lot more possibilities when it comes to metadata.
