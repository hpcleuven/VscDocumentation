.. _KU Leuven data management guidelines:

======================================
Data management and outflow guidelines
======================================

About
=====

This page contains guidelines related to managing your data on the different storage platforms VSC and KU Leuven have to offer. These guidelines concern organization on the different storage locations, as well as the flow of data between them.

While most of these guidelines can be applied to the differen types of storage available to you, this page mainly focuses on shared storage (i.e. staging/project storage, Tier-1 Data/Mango, L-drive, other local shared storage...).

This page also tries to follow the 'natural' build-up of a (shared) HPC project:

#. What kind of storage do you need?

#. Organize your directory structure on your shared storage

#. Safely store data

#. Keep track of your data

What kind of storage do you need?
=================================

Cluster storage
---------------

The VSC clusters offer a range of different storage types, all serving their own purpose. You can find more details on the :ref:`storage locations page <data location>`. Next to the VSC storage types, KU
Leuven also offers staging storage. This is technically the same type of storage as scratch (Lustre storage), but is meant for collaborating within a project. In case you are considering requesting a
staging storage, consider the following points:

- Are you sharing a large amount of input data or certain databases between different users? Do these need to be readily available on the cluster for an extended period of time? 
- Are you sharing computation tasks between different users?
- Are multiple users postprocessing certain output data?

If one or more of the above cases apply to you, it might be that you are eligible for staging storage.

Note that staging storage is not meant for:

- long-term storage: even though the data removal limitation on our regular scratch storage does not exist on staging, this does not mean that this storage is safe for long-term storage of data. Just as with regular scratch storage, there is no snapshotting or double copy for staging. If somebody accidentally removes data, or an unexpected system failure removes/corrupts data, your data is gone forever.
- extending your scratch storage: we can temporarily increase your scratch storage for free! In the case you are part of a team that uses a staging directory for a shared project, and you are computing on your own, but you lack scratch storage, also request this extension instead of moving your workflow to staging. This will also limit the cost of staging for your team, as we charge based on maximal usage, and not on quota limits.

You can request staging storage or extensions to your personal scratch in our `service catalogue <https://icts.kuleuven.be/sc/onderzoeksgegevens/english-version/HPC-storage>`_.

External/safe storage
---------------------

Next to cluster storage, it is also recommended to have a storage location to store data on which you are not actively computing anymore, but needs to be kept for later analysis or postprocessing, sharing
with other users/teams... It is also recommended that this storage, different from scratch/staging, has some form of data safety. This could be in the form of a double copy, snapshotting...

While there are multiple options available, there exists no such storage that is directly connected to the cluster. This means that moving data to and from this storage will take more time compared
to writing or reading from a storage located on the cluster. In most cases, a mount will not be available either, so simply providing a read or write path won't work.

Options for such a safe storage could be:

- group-, department-,...managed storage: some research groups or departments offer some kind of 'in-house' storage. In that case it will probably already be part of your workflow.
- KU Leuven archive or large volume storage (L and K drive)
- ManGO or Tier-1 data
- cold storage (FriGO)

All of the above options come with their own benefits, but also pricing. More information is available at the `KU Leuven storage guide <https://icts.kuleuven.be/storagewijzer/en>`_.

Create a data management plan
=============================

This is one of the first things your team should do when requesting access to the storage locations we mentioned above. KU Leuven offers extensive documentation, examples and tools, so be sure
to check out `the RDM Data Management Plan documentation pages <https://www.kuleuven.be/rdm/en/guidance/dmp>`_. As HPC workloads, and especially shared workloads, come with their own challenges, we
provide some extra suggestions here as well:

- Map your dataflow: where is your data coming from? What data is generated on the cluster, and what needs to be deleted and what can be kept? Where does that data need to move to?
- Estimate your needed storage capacity: what maximum amount of storage do you need at any given point? This is not so much a summation of sizes of each of your datasets, but more an exercise where you try to estimate how much storage will be used if you also consider inbetween (re)moving of data. 
- Identify shared resources: this could be shared input data, enrichment databases, shared software...
- Identify candidates for automation: could you perhaps automatically download your input data, process it and then remove the input data again within your job? Or perhaps you can automate syncing to your safe storage? This does not mean that you have to immediately automate these workflows. Identifying them however, can help you to make more informed decisions on for example directory structure.

Many of these points are discussed in more detail in the paragrahps below.

Take your time and organize a meeting within your team to draw the outlines of the management plan: as multiple people will be using the storage, there will be different workflows and preferences.
Invite the following people:

- the PI: they have a vision on past, current and future projects, and how they are related.
- At least some of the researchers working on HPC: they understand the day-to-day needs on the cluster.
- Data support roles: if you have anyone that supports you technicallly, involve them as well for their expertise on these subjects.


Organize your directory structure on your shared storage
========================================================

Note that KU Leuven has a wide range of documentation, tools and trainings available on the `Research Data Management pages <https://www.kuleuven.be/rdm/en>`_. They also offer
some `general guidelines on file organisation <https://www.kuleuven.be/rdm/en/guidance/data-standards/file-organisation>`_.

It is worth spending some time on creating a directory structure for any of your storage locations, but for shared storage this need is even higher. It is recommended to create directory structuring
guidelines within your team, or even incorporate pre-defined directory structuring in your workflow. This avoids that data gets lost in the plethora of directories that multiple users will create over
multiple years. It is not possible to provide you with 'the best way' to organize data, but in the following paragrahps, you can find some tips and tricks.

Organize directories according to scope
---------------------------------------

Place the directories with the largest scope on the top level, and decrease scope when going deeper in your directory structure. In practice, this often means that you have your project directories
on the top level, followed by a user/researcher directory (e.g. by using the vsc id), and then the different experiments a user is doing. Of course, you could add an extra top directory ``projects``
(or something similar), if you would like to add top directories for input data or software (see later). Organizing your data 'project first' (and user later) avoids that project data gets spread out over
multiple directories, making it easier to collaborate and find data of past projects. Switching the user directory and project directory would only make sense if there is only a single user per
project, and in that case you are probably better of using ``$VSC_SCRATCH``.

Divide input, intermediate and output data directories
------------------------------------------------------

While you are probably already making this division on a certain level in your directory tree, this paragraph is more focused on deciding on what level you should be making it. This will mostly depend
on the level of data sharing within your team, and on the potential need of syncing your input data to your safe storage.

If you are sharing input data (or perhaps certain enrichment databases) with other teammembers, it would make sense to place these in a separate directory on a higher level than the experiment directory
you need that input data for. How much higher will depend on the level of sharing. If you have certain data that is needed over different projects, it is clear that you could place this in a separate input
directory above the project level. You could then opt for a top-level ``input_data`` and ``output_data`` directory, potentially with mirrored project directories in both (in case you have project-specific
input data as well).

Whether or not you need to sync your input or intermediate data to your safe storage, will also influence what the best directory level is for that data. In case you only need to store your output data,
it makes more sense to separate your input, intermediate and output data on a level higher than the project-level. This makes it easier for your syncing processes, as you just need to sync a single
directory, instead of filtering out certain subdirectories. Of course, if you need to keep everything, it could make sense to have all data from your workflow packed together inside a project directory.
Again, if it would make the most sense to store all this data together on an experiment or user level, you would probably be better of with storing your data on ``$VSC_SCRATCH``. This also holds up for the
case where your team is only sharing certain (enrichment) databases. Nothing stops you from having a minimal staging storage for those databases, and performing the rest of your workflow on ``$VSC_SCRATCH``.

In case you are working with sensitive data, a well thought-out separation of the different data types is even more important. Having the above-mentioned separation allows you to control access
to specific data on a relatively high level. In case you are working with data for which some privacy concerns exist, it is recommended to contact our `servicedesk <hpcinfo@kuleuven.be>`_.


Location of software
--------------------

In some cases it might be interesting to install your software in your shared storage as well. The only real use-case for this however, is when you are sharing certain software between different
users. While it might be tempting to install all of your software here, it is probably better to place them somewhere else if there is no intend of sharing the installation. Make the following
considerations:

- Are you using existing (licensed) software? In that case it is probably best to not install it yourself, but contact our `servicedesk <hpcinfo@kuleuven.be>`_ instead. We might be able to install your software as a module. In case we have a reason to not install it as a module, and you indeed want to share your software between teammembers, an installation in staging would be appropriate. If it is for personal use, consider installing it in a personal directory (e.g. ``$VSC_DATA``).
- Are you compiling your own code? If multiple people are using your compiled software, you have a good case to place it in the staging storage. If it is for personal use, use a personal directory. Note that developing code together is not a good use-case for putting your code on staging. :ref:`Version control systems <version control systems>` are meant for exactly that, and avoid many of the dangers of working on the exact same scripts on a local file system. As soon as you are developing code (even alone), you should include a version control system in your workflow. If you are unfamiliar with this concept, know that ICTS offers `a yearly course on version control <https://admin.kuleuven.be/icts/opleidingen/opleidingsaanbod/version-control-hybrid>`_. In case you missed it, there is a lot of information and qualitative online courses available on this subject. Search for: version control, git, GitHUB, GitLab. KU Leuven also hosts its `own GitLab <https://gitlab.kuleuven.be/>`_.
- Are you running your code in a sort of virtual environment (e.g. a :ref:`Python venv <venv_python>` or a :ref:`conda environment <conda for Python>`)? Depending on the type of virtual environment, sharing is not always the best option. Conda environments are not easily shared between users and belong in a personal directory. Python venvs can be shared between users, and could be placed in staging if needed. Beware that especially conda environments create a lot of files, which can be detrimental for your inode quota! Another good replacement for both Python venvs and conda environments, is using a :ref:`container <hpc containers>`. A container can be shared between multiple users, and contains a whole separate environment. This allows the flexibility of a conda environment, but without the high file count.

If you really need to install your software within staging, similar rules as in the previous paragraph apply: create a separate software directory on the appropriate level. This will again depend on the
level of sharing (used by the whole group, for specific projects...). 


Safely store data
=================

At a certain point, you will need to start moving data out of staging, and to a safer external storage. Not only do you need to think what data you should store there, there are also multiple options
when considering transfer tools.

What data needs to be moved to the safe storage?
------------------------------------------------

When computing on a cluster, you often use a wide range of types of data to arrive at your final output. Perhaps you are using publicly available datasets, output from certain measurement equipment,
generated data... You also might create different types of intermediate data that you do not need for your final analysis.  While you could just move everything to your safe storage, this could easily
lead to an explosion of data there, influencing not only your cost, but also decreasing searchability of your storage. For this reason: work out in detail what data **really** needs to be kept after
the active computation phase. For as well input, intermediate, output and postprocessed data, you should place your data on your safe storage in the following scenarios:

- If your data is (computationally) expensive to generate. It is often not very easy to make a clear distinction on when the (compute) cost becomes high enough to justify storing it on a remote safe storage. Compute cost vs transfer cost (time of transferring) is not the only factor that plays a role here though. If generating the data requires a lot of effort from the user (e.g. complex workflows), or if the total runtime is quite long (sequential run code on a low amount of resources can for example have a low computational cost, but take a very long time), you could also consider moving this data to your safe storage.
- If you are sharing data with collaborators that do not have access to our HPC facilities. This could be a associated research group with whom you have to :ref:`share data <collaboration>`, but also if you need to make your data public (for example through the :ref:`Globus sharing functionality <globus-sharing>` or by using `KU Leuven RDR <https://www.kuleuven.be/rdm/en/rdr>`_).
- If you or somebody else needs to perform extra (postprocessing) steps on your data, but you need to create space for computation of other projects/experiments, you can (temporarily) store data on your safe storage as well.
- If you are computing on multiple machines (e.g. expensive computation on Tier-1 and postprocessing on Tier-2), your safe storage can be a sort of inbetween storage, especially when there is some time between those steps.


What shouldn't you move to your safe storage:

- Code or compiled software: in most cases, a version control system is a much better way to store your source code. Compiled software almost never makes sense to store, as in most cases it is built for a specific node architecture and operating system. Just store your source code, together with your compilation scripts, in a version controlled environment (code repository).
- Public databases. Unless there is a high cost to downloading them, or you need to perform expensive postprocessing steps on them. Another positive usecase would be that you are working with automated workflows that allow you to read directly from your safe storage (advanced).
- Unstructured directories from team members. This last one might be a bit less obvious, but it happens all the time that users create certain directories or files just to test or debug things. In many cases, these directories are not removed afterwards, and when that member leaves the group, it is not clear what the directory contains. It can then be very tempting to move the whole thing to your safe storage with the idea that this can be cleaned up later. As this almost never happens, it is much better to just try to figure out what they are, while still on staging. Having good guidelines on how to structure your directory tree, and asking team members to create such directories with for example a ``tmp`` prefix (or just in their own directories), will avoid such scenarios.


How should you transfer your data
---------------------------------

There are multiple platforms available to transfer your data:

- Globus: a platform that allows transfers in with their :ref:`web interface <globus-web>`, or their :ref:`command line interface <cli>`. There are multiple :ref:`managed collections <globus-collections>` available, including collections for ManGO, Tier-1 Data, OneDrive, the KU Leuven large volume storages... In case you want to transfer to or from somewhere where there is no managed collection, you can still create a :ref:`local endpoint <globus-local-endpoints>`. You can find the full documentation on our :ref:`Globus pages <globus platform>`.
- iCommands/Python iRODS client/ManGO Portal: tools that allows users to transfer data to and from an iRODS-managed platform (i.e. ManGO and Tier-1 Data). The full documentation can be found on :ref:`VSC docs <clients>`.
- classic transfer tools like ``rsync``, ``sftp``...


Keep track of your data
=======================

When you start using multiple locations to store your data, you will somehow need to keep an eye on how data is moving between the different locations. This will help in keeping your storage locations
as clean as possible, as well as making sure that all data ends up in its supposed end location eventually. There are multiple ways to handle this:

- automation: this is for sure the superior method, but very often also the hardest to achieve. This does not mean that you have to fully automate your dataflow, but perhaps you could implement: automatic syncing of output data to a safe storage as soon as job finishes, automatic cleaning of intermediate/input data... Automation will become a lot easier if you have well-organized directory trees on your storage locations, especially if you can mirror that structure (partially) between those different locations.
- Monitor your storage on a regular basis. While there are standard Linux tools like ``du`` that allow you to do this, there is also a KU Leuven-developed tool called ``duduckdb`` (or the eventual name, possibly a link to the eventual documentation here) that allows you to quickly query a database that contains information on the disk usage on your staging directory.
- Train new researchers in following your teams directory policies! If people start to deviate from the written rules, it will become harder and harder to keep track of what exactly is on your storage.
- Make data management a regular part of (PI-researcher) meetings. Discuss what data you currently have on compute storage, whether or not data can be moved or deleted from there, identify risks of reaching max quota...
- add documentation to your directories: a simple README file with some information about a certain project or experiment, can make it much easier to figure out what a directory exactly contains. You can even link to the eventual published paper, a repository... A lot of this information could also be added by making use of :ref:`iRODS metadata <metadata>` (only for ManGO or Tier-1 Data users).
