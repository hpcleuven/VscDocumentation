.. _KU Leuven data management guidelines:

======================================
Data management and outflow guidelines
======================================

About
=====

This page contains a wide range of guidelines related to managing your data on the different storage platforms VSC and KU Leuven have to offer. These guidelines concern organization on the different storage locations, as well as the flow of data between them.

While most of these guidelines can be applied to the storage available to you, this page focuses mainly on shared storage (i.e. staging/project storage, Tier-1 Data/Mango, L-drive, local storage...).

This page also tries to follow the 'natural' build-up of a (shared) HPC project:
1. What kind of storage do you need?
2. Organize your directory structure on your shared storage
3. Safely store data
4. Keep track of your data

What kind of storage do you need?
=================================

Cluster storage
---------------

The VSC clusters offer a range of different storage types, all serving their own purpose. You can find more about the details of the different storage types on the :ref:`storage locations page <_data location>`. KU Leuven also offers staging storage for their users, which is technically the same as scratch storage, but is meant for collaborating within a project. If you think this would be more suitable for you than the usual personal scratch storage, you should consider the following points:
- Are you sharing a large amount of input data or certain databases between different users? Do these need to be readily available on the cluster for an extended periode of time? 
- Are you sharing computation tasks between different users?
- Are multiple users postprocessing certain output data?

If one of the above cases apply to you, it might be that you are eligible for a staging storage.

Note that staging storage is not meant for:
- long-term storage: even though the data removal limitation on our regular scratch storage does not exist on staging, this does not mean that this storage is safe for long-term storage of data. Just as with regular scratch storage, there is no snapshotting or double copy for staging. If somebody accidentally removes data, or an unexpected system failure removes data, your data is gone forever.
- extending your scratch storage: we can temporarily increase your scratch storage for free! In the case you are part of a team that uses a staging directory for a shared project, and you are computing on your own, but you lack scratch storage, also request the extension instead of moving your workflow to staging. This will also limit the cost of that staging storage, as we charge based on maximal usage, and not on quota limits.

You can request staging storage or extensions to your personal scratch in our `service catalogue <https://icts.kuleuven.be/sc/onderzoeksgegevens/english-version/HPC-storage>`.

External/safe storage
---------------------

Next to cluster storage, it is also recommended to have a storage location where you can write data to that on which you are not actively computing anymore. It is also recommended that this storage,
different from scratch/staging, has some form of data safety. This could be in the form of a double copy, snapshotting...

While there are multiple options for such a storage, note that there is no such storage directly connected to the cluster. This means that you will have to copy or move this data to an external source.
Options for such a safe storage could be:

- group-, department-,...specific storage: some research groups or departments offer in-house storage. In that case it will probably already be part of your workflow.
- KU Leuven archive or large volume storage (L and K drive): more info at (link)
- ManGO or Tier-1 data: (description Jef + link)
- cold storage (FriGO): (description Jef + link)

All of the above options come with their own benefits, but also pricing. In case of doubt, feel free to contact the (RDM team). 

Create a data management plan
=============================

This is one of the first things your team should do when requesting access to the storage locations we mentioned above. While there is some more official information on data management plans (see ...),
you need to consider the following points:

- Map your dataflow: where is your data coming from? What data is generated on the cluster, and what needs to be deleted and what can be kept? Where does that data need to move to?
- Estimate your needed storage capacity: what maximum amount of storage do you need at any given point? This of course depends on the size of your datasets and the number of users working with such datasets, but you should also take into consideration that you might delete and move data from your staging storage.
- Identify shared resources: this could be shared input data, enrichment databases, shared software...
- Identify candidates for automation: could you perhaps automatically download your input data, process it and then remove the input data again within your job? Or perhaps you can automate syncing to your safe storage?

Many of these points are discussed in more detail in the paragrahps below.

Take your time and organize a meeting within your team to draw the outlines of this management plan: as multiple people will be using the storage, there will be different workflows and preferences.
Invite the following people:
   - the PI: they have a vision on past, current and future projects, and how they are related.
   - At least some of the researchers working on HPC: they understand the day-to-day needs on the cluster.
   - Data support roles: if you have anyone that (partially) supports you technicallly, involve them as well for their expertise on these subjects.


Organize your directory structure on your shared storage
========================================================

Note that KU Leuven has a wide range of documentation, tools and trainings available on the `Research Data Management pages <https://www.kuleuven.be/rdm/en>`. They also offer
some `General guidelines on File Organisation <https://www.kuleuven.be/rdm/en/guidance/data-standards/file-organisation>`.

It is worth spending some time on working out a directory structure on any of your storage locations. For shared storage this need is even higher. It is recommended to create directory structuring
guidelines within your team, or even incorporate pre-defined directory structuring in your workflow. This avoids that data gets lost in the plethora of directories that multiple users wil create over
multiple years. It is not possible to provide you with 'the best way' to organize data, but in the following paragrahps, you can find some tips and tricks.

Organize directories according to scope
---------------------------------------

Place the directories with the largest scope on the top level, and decrease scope when going deeper in your directory structure. In practice, this often means that you have your project directories
on the top level, followed by a user/researcher directory (e.g. by using the vsc id), and then the different experiments a user is doing. Of course, you could add an extra top directory `projects`
(or something similar), if you would like to add top directories for input data or software (see 3). Organizing your data 'project first' (and user later) avoids that project data gets spread out over
multiple directories, making it easier to collaborate and find data of past projects. Switching the user directory and project directory would only make sense if there is only a single user per
project, and in that case you are probably better off using `$VSC_SCRATCH`.

Divide input, intermediate and output data directories
------------------------------------------------------

While you are probably already making this division on a certain level in your directory tree, this paragraph is more focused on deciding on what level you are making this separation. This will mostly depend
on the level of data sharing within your team, and on the potential need of syncing your input data to your safe storage.

If you are sharing input data (or perhaps certain enrichment databases) with other teammembers, it would make sense to place these in a separate directory on a higher level than the experiment directory
you need that input data for. How much higher will depend on the level of sharing. If you have certain data that is needed over different projects, it is clear that you could place this in a separate input
directory above the project level. You could then opt for a top-level `input_data` and `output_data` directory, potentially with mirrored project directories in both (in case you have project-specific
input data as well).

Whether or not you need to sync your input or intermediate data to your safe storage, will also influence what the best location is for that data. In case you only need to store your output data, it makes
more sense to separate your input, intermediate and output data on a level higher than the project-level. This makes it easier for your syncing processes, as you just need to sync a single directory,
instead of filtering out certain subdirectories. Of course, if you need to keep everything, it could make sense to have all data from your workflow packed together inside a project directory. Again, if it
would make the most sense to store all this data together on an experiment or user level, you would probably be better of with storing your data on `$VSC_SCRATCH`. This also holds up in the case where your
team is only sharing certain (enrichment) databases. Nothing stops you from having a minimal staging storage which contains those databases, and performing the rest of your workflow on `$VSC_SCRATCH`.

In case you are working with sensitive (input) data, a well thought-out separation of the different data types is even more important. Having the above-mentioned separation allows you to control access
to specific data on a relatively high level. In case you are working with data for which some privacy concerns exist, it is recommended to contact our (servicedesk).


Location of software
--------------------

In some cases it might also be interesting to install your software in your shared storage as well. The only real use-case for this, would be when you are sharing certain software between different
users. While it might be tempting to install all of your software there, it is probably better to install it somewhere else if you are not planning on sharing the software. Make the following
considerations:

- Are you using any existing (licensed) software? In that case it is probably best to not install it yourself, but contact our (servicedesk) instead. We might be able to install your software as a module. Inn case we have a reason to not install it as a module, and you indeed want to share your software between teammembers, an installation in staging would be appropriate. If it is for personal use, consider installing it in a personal directory (e.g. `$VSC_DATA`).
- Are you compiling your own code? Again, if multiple people are using your compiled software, you have a good case to place it in the staging storage. If it is for personal use, use a personal directory. Note that developing code together is also not a good use-case for putting your code on staging. :ref:`Version control systems <_version control systems>` are meant for exactly that, and avoid many of the dangers of working on the exact same scripts on a local file system. As soon as you are developing code (even alone), you should include a version control system in your workflow. If you are unfamiliar with this concept, know that ICTS offers `a yearly course on version control <https://admin.kuleuven.be/icts/opleidingen/opleidingsaanbod/version-control-hybrid>`. In case you missed it, know that there is a lot of information and qualitative online courses available on this subject. Search for: version control, git, GitHUB, GitLab. KU Leuven also hosts its `own GitLab <https://gitlab.kuleuven.be/>`.
- Are you running your code in a sort of virtual environment (e.g. a Python venv or a conda env)? Depending on the type of virtual environment, sharing is not always the easiest option. Conda environments are not easily shared between users and belong in a personal environment. Python venvs can be shared between users, and could be placed in staging if needed. Beware that especially conda environments create a lot of files, which can be detrimental for your inode quota! Another good replacement for both Python venvs and conda environments, is using a :ref:`container <_hpc containers>`. A container can be shared between multiple users, and contains a whole separate environment. This allows the flexibility of a conda environment, but without the high file count.

If you really need to install your software within staging, similar rules as in the previous paragraph apply: create a separate software directory on the appropriate level. This will again depend on the
level of sharing (used by the whole group, for specific projects...). 


Safely store data
=================

At a certain point, you will need to start moving data out of staging, and to a safer external storage (as mentioned in the first paragraph). Not only do you need to think what data you should store there,
there are also multiple options when considering transfer tools.

What data do you need to move to safe storage?
----------------------------------------------

When computing on a cluster, you often use a wide range to arrive at your final output. Perhaps you are using publicly available databases, output from certain measurement equipment, generated data. You
also might create different types of intermediate data that you do not need for your final analysis. While you could just move everything to your safe storage, it is often better to decide beforehand what
you should store for a longer time. For as well input, intermediate, output and postprocessed data, you can use the following rules:

- If your data is (computationally) expensive to generate, it probably makes sense to store it on your safe storage. It is often not very easy to make a clear distinction on when the (compute) cost becomes high enough to justify storing it on a remote safe storage. Take into consideration the size of your data as well. The larger the data, the higher the computational cost can be. Transfering to and from such a storage can take some time as well, so it can often be as interesting to just recompute your data. Of course, next to the effective compute cost, you could also take into consideration the amount of time it takes a researcher to create this data. If you need to download input data from multiple sources, or it is a complicated workflow, it can sometimes be beneficial to just store the data.
- If you need to make your data available to the public/other researchers, it would make sense to write it your safe storage, Note that platforms like ManGO and Tier-1 Data offer easy options to make certain datasets publicly available (link?)
- If you or somebody else needs to perform extra (postprocessing) steps on your data, but you need to create space for computation of other projects/experiments, you can (temporarily) store data on your safe storage as well.
- If you are computing on multiple machines (e.g. expensive computation on Tier-1 and postprocessing on Tier-2), your safe storage can be a sort of inbetween storage, especially when there is some time between those steps.


What shouldn't you move to your safe storage:

- Code or compiled software: in most cases, a version control system is a much better way to store your source code. Compiled software almost never makes sense to store, as in most cases it is built for a specific node architecture and operating system. Just store your source code, together with your compilation scripts.
- Public databases. Unless there is a high cost to downloading them, or you need to perform expensive postprocessing steps on them. Another case would be that you are working with automated workflows that allow you to read directly from your safe storage (advanced).
- Unstructured directories from team members. This last one might be a bit less obvious, but it happens all the time that we create certain directories or files just to test or debug things. In many cases, these directories are then not removed, and when that member leaves the group, it is not really clear what the directory contains. It can then be very tempting to move the whole thing to your safe storage with the idea that this can be cleaned up later. As this almost never happens, it is much better to just try to figure out what they are while still on staging. Having good guidelines on how to structure your directory tree, and asking team members to create such directories with for example a `tmp` prefix, will avoid such scenarios.


How should you transfer your data
---------------------------------

There are multiple platforms available to transfer your data:

- Globus: a platform that allows transfers in with their :ref:`web interface <_globus-web>`, or their :ref:`command line interface <_cli>`. There are multiple :ref:`managed collections <_globus-collections>` available, including collections for ManGO, Tier-1 Data, OneDrive, the KU Leuven large volume storages... In case you want to transfer to or from somewhere where there is no managed collection, you can still create a :ref:`local endpoints <_globus-local-endpoints>`. You can find the full documentation on our :ref:`Globus pages on VSC docs <_globus platform>`.
- iCommands/Python iRODS client/ManGO Portal: tools that allows users to transfer data to and from an iRODS-managed platform (i.e. ManGO and Tier-1 Data). The full documentation can be found on :ref:`VSC docs < _clients>`.
- classic transfer tools like `rsync`, `sftp`...


Keep track of your data
=======================

When you start using multiple locations to store your data, you will somehow need to keep an eye on how data is moving between the different locations in order to keep your storage locations as clean as
possible, but as well making sure that all data ends up in its supposed end location eventually. There are multiple ways to handle this:

- automation: this is for sure the superior method, but could be hard to implement. This does not mean that you have to fully automate your dataflow, but perhaps you could implement automatic syncing of output data to a safe storage as soon as job finishes, automatic cleaning of intermediate/input data... Automation will become a lot easier if you have well-organized directory trees on your storage locations, especially if you can mirror that structure (partially) between those different locations. Next to using the above-mentioned command-line tools, you could also use tools like ManGO Ingest (link needed).
- Monitor your storage on a regular basis. While there are standard Linux tools like `du` that allow you to do this, there is also a KU Leuven-developed tool called `duduckdb` (or the eventual name, possibly a link to the eventual documentation here) that allows you quickly query a database that contains information on the usage of your staging directory. With this, you can easily spot large directories, and even link them to users.
- Train new researchers in following your teams directory policies! If people start to deviate from the written rules, it will become harder and harder to keep track of what exactly is on your storage.
- Make data management a regular part of PI-researcher meetings. Discuss what data you currently have on compute storage, whether or not data can be moved or deleted from there... Data management is the part that people keep forgetting until it is too late...
- add documentation to your directories: a simple README file with some information about a certain project or experiment, can make it much easier to figure out what a directory exactly contains. You can even link to the eventual published paper, a repository... A lot of this information could also be added by making use of metadata when using ManGO or Tier-1 Data. (add link)
