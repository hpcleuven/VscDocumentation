.. _tier1_data_service:

######################################
:fa:`people-carry` Tier-1 Data Service
######################################

The Tier-1 supercomputing infrastructure in Flanders had until 2018 mainly been
targeted at users with serious calculation issues (typical HPC/HTC workloads).
Although this platform in its current form is already very successful, the
current focus on compute no longer meets all the needs of many researchers.
More and more users have computational work that makes intensive use of large
data sets. Migrating this data to and from the compute infrastructure whenever
it is to be used for a calculation is very inefficient because of the scale. It
is therefore necessary to add a data component where large data sets can be
stored for a longer period of time and from there also be processed
efficiently.

This service has as primary goal to offer the users a platform to easy manage
research data and help them to apply the **FAIR** principles to their research
data from the very beginning of their projects. This should make it easier to
transfer their research data and output at the end of the project to
institutional or domain specific repositories for publication and preservation
and when applicable ensure they are made publicly available (open access).

.. figure:: data_service/tier1_vsc_data.png

The Tier-1 Data component provides a service to allow users to store research
data during the active phase of the research data life cycle (that is, data
that is being collected and analyzed and has not yet being published). This
service for now is restricted to data of research projects that are using the
VSC Tier-1 Compute infrastructure. 

This platform should also help the researchers to run their scientific
workflows more efficiently by providing tools to automate data collection, data
quality control and stage in a and stage out data from and to Tier-1 Compute
system. 

This Tier-1 Data service is based on the Open Source software iRODS
(`irods.org`_). How to gain access to the Tier-1 Data iRODS instance is
explained in the article ':ref:`user_access`'.

.. toctree::
   :maxdepth: 3

   introduction_to_irods
   tier1_data_architecture
   data_discovery
   user_access
   irods_clients_index
   workflow_automation
   glossary
