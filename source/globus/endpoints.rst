.. include:: css.rst

===============
Endpoints 
===============

With Globus, you might want to access data on various storage and computer systems, for example HPC clusters, laptops, or cloud storage. 
Directories on those systems can be exposed to Globus as a **collection**.
To search and access a collection, you only need its name.
However, you can only access collections if one of your linked accounts has access to the system.
For example, the collection exposing KU Leuven's Tier-2 Scratch is only accessible for people with a VSC-account. 

An **endpoint** is a server that hosts one or multiple collections.




Available collections
------------------

Both the KU Leuven and the VSC host a number of collections:


+------------------------------------------+-------------------+----------------+------------------+
| Name                                     | Account needed    | High assurance | Guest collections| 
+==========================================+===================+================+==================+
| KU Leuven Onedrive                       | KULeuven account  | Yes            | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC iRODS set.irods.icts.kuleuven.be     | iRODS account     | No             | Yes              |
+------------------------------------------+-------------------+----------------+------------------+
| VSC iRODS ghum.irods.icts.kuleuven.be    | iRODS account     | No             | Yes              |
+------------------------------------------+-------------------+----------------+------------------+
| VSC iRODS gbiomed.irods.icts.kuleuven.be | iRODS account     | No             | Yes              |
+------------------------------------------+-------------------+----------------+------------------+
| VSC iRODS irods.hpc.kuleuven.be          | iRODS account     | No             | Yes              |
+------------------------------------------+-------------------+----------------+------------------+
| VSC VUB Hydra                            | VSC account       | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC UGent Tier2 filesystems              | UGent account     | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC UGent Tier1 Projects                 | VSC account       | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC UAntwerpen Tier2                     | UAntwerpen account| No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC KU Leuven tier1 scratch              | VSC account       | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC KU Leuven tier2 scratch              | VSC account       | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC KU Leuven user directories           | VSC account       | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+
| VSC KU Leuven data directories           | VSC account       | No             | No               |
+------------------------------------------+-------------------+----------------+------------------+

.. _globus-local-endpoints:

Local endpoints
------------------


Users can create and manage endpoints on their personal computers via `Globus Connect Personal`_. Globus Connect Personal is available for all major operating systems. Download the software and follow the installation instructions. During the setup process you will be asked to set the local endpoint. Each endpoint has a unique ID. Those ones created or managed by you are associated with your Globus account.

To access and manage your local endpoints:

- Start the **Globus Connect Personal** applet.

- From a browser log into Globus and in the File Manager navigate to :bgrnd1:`Endpoints`. Then select the :bgrnd1:`Administered by you` tab.

- To change the attributes of an endpoint click on its name. You can adjust a variety of settings like private or public, endpoint name, contact info, and encryption.

.. image:: local_endpoints/endpoints1.png

.. warning:: Users should use caution and carefully select the privacy permissions and attributes when creating endpoints on their personal computers.




Creating a managed endpoint
---------------------------

The five Flemish universities have a `High Assurance subscription <https://www.globus.org/subscriptions>`_ for Globus, which allows the creation of extra managed endpoints. 

VSC users and researchers from those universities can create their own managed endpoint under this subcription.  

You can find the technical prerequites `here <https://docs.globus.org/globus-connect-server/v5.4/#globus_connect_server_prerequisites>`_.

If you want create your own managed endpoint, please mail to data@vscentrum.be. 


.. include:: links.rst



