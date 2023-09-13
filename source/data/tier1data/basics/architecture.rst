.. _architecture:

########################
Tier-1 Data Architecture
########################

The Tier-1 Data platform is based on the open source software `iRODS <https://irods.org>`_.
The image below shows the high level architecture of the platform:

.. figure:: ../images/introduction/tier1data_architecture.png
   :alt: A schematic representation of the architecture of Tier-1 Data with, from bottom to top: the storage layer, the layer of iRODS middleware, and the different clients users can use.  

An single installation of iRODS is called a 'zone'.
By default, new projects are creates in our general zone 'VSC'.
Separate zones can be created for confidentiality or efficiency reasons for different projects. 

Each zone has a Rule engine and an iCAT
database, which contains metadata, permissions and an index of all file locations.
Inside a zone, each project has their own folder. 

The data itself is synchronized on two separate hardware storage
systems, each 27 PB large, located at Leuven and at Heverlee (ICTS KU Leuven). 
The data is protected against calamities at either site by synchronizing it in real-time at hardware level. 
One system does not function as a backup for the other, so this is no protection against accidental instructions
(i.e. user mistakes) to delete data. 
Snapshots are made at regular intervals (hourly, daily and monthly) in case data needs to be recovered.
For data recovery in case of emergency, please contact data@vscentrum.be. 

An iRODS zone can be accessed from different systems:

- The HPC clusters of the Flemish Supercomputing Center (VSC)
- Your laptop
- Scientific instruments like scanners and microscopes


From each of these systems, access is facilitated by a variety of clients:

- Programming clients
    + :ref:`iCommands` is a package that gives users a command-line interface to operate on data in iRODS.
    + The :ref:`Python-iRODSClient (PRC)<python-client>` is a Python client API that can make a secure connection to iRODS so that you can integrate your iRODS data interactions within your (existing) python programs.
- The :ref:`ManGO Portal <mango-portal>`: the web front-end for Tier-1 Data, which provides a very user-friendly approach.

Finally, data exchange between zones and externally is possible thanks to Globus. More information can be found in the :ref:`Globus <globus platform>` documentation.
