.. include:: css.rst

=========
Endpoints
=========

With Globus, you might want to access data on various storage and computer systems, for example HPC clusters, laptops, or cloud storage. 
Directories on those systems can be exposed to Globus as a **collection**.
To search and access a collection, you only need its name.
However, you can only access collections if one of your linked accounts has access to the system.
For example, the collection exposing KU Leuven's Tier-2 Scratch is only accessible for people with a VSC-account. 

An **endpoint** is a server that hosts one or multiple collections.



.. _globus-available-collections:

Available collections
---------------------

The VSC hosts a number of collections:


.. list-table:: Overview of collections for HPC systems
   :header-rows: 1

   * - Name
     - Collection
     - High assurance
     - Guest collections
   * - VUB Tier-2 
     - `VSC VUB Hydra <https://app.globus.org/file-manager/collections/2d1d4873-a849-4b9c-bd34-2034a2163003/overview>`_
     - No
     - Yes
   * - UGent Tier-2
     - `VSC UGent Tier2 filesystems <https://app.globus.org/file-manager/collections/e9247cdf-2c76-42ef-81d4-1c3f772ce719/overview>`_
     - No
     - Yes
   * - UGent Tier-1
     - `VSC UGent Tier1 projects <https://app.globus.org/file-manager/collections/ce533ba6-0b81-4640-bdc6-f3a6ff2d4b74/overview>`_
     - No
     - No
   * - UAntwerpen Tier-2
     - `VSC UAntwerpen Tier2 <https://app.globus.org/file-manager/collections/6a13242d-6506-4b3d-a49c-ac981b35ab7d/overview>`_
     - No
     - No
   * - KU Leuven Tier-2 (scratch)
     - `VSC KU Leuven tier2 scratch <https://app.globus.org/file-manager/collections/82c495cc-aef8-40ad-88df-f9c92bee82d3/overview>`_
     - No
     - Yes
   * - KU Leuven Tier-2 (user directories)  
     - `VSC KU Leuven user directories <https://app.globus.org/file-manager/collections/b4ad28e2-d444-485f-97c5-ca5f6e0d3a2b/overview>`_
     - No
     - No
   * - KU Leuven Tier-2 (data directories)
     - `VSC KU Leuven data directories <https://app.globus.org/file-manager/collections/38948f53-d4f5-4e94-afa5-ad364c7a66b8/overview>`_
     - No
     - Yes

.. Note::
      The collection 'VSC KU Leuven tier2 scratch' also contains the staging directories, under :bgrnd1:`/project`

.. list-table:: Overview of collections for Tier-1 Data
   :header-rows: 1

   * - Name
     - Collection
     - High assurance
     - Guest collections
   * - Tier-1 Data: kuleuven_tier1_pilot zone
     - `VSC iRODS irods.hpc.kuleuven.be <https://app.globus.org/file-manager/collections/7b4afc9a-e89d-4a79-bc8e-a2d9b1c53eda/overview>`_
     - No
     - Yes
   * - Tier-1 Data: VSC zone
     - `VSC iRODS vsc.irods.hpc.kuleuven.be <https://app.globus.org/file-manager/collections/3e97664d-d90b-488b-9f49-09a24cfaf022/overview>`_
     - No
     - Yes
   * - Tier-1 Data: VSC-climate zone
     - `VSC iRODS vsc-climate.irods.hpc.kuleuven.be <https://app.globus.org/file-manager/collections/ca51285b-4598-4c12-89f2-9e5de8b13e04/overview>`_
     - No
     - No





 



.. _globus-local-endpoints:

Local endpoints
------------------


Users can create and manage endpoints on their personal computers via `Globus Connect Personal`_. Globus Connect Personal is available for all major operating systems. Download the software and follow the installation instructions. During the setup process you will be asked to set the local endpoint. Each endpoint has a unique ID. Those ones created or managed by you are associated with your Globus account.

To access and manage your local endpoints:

- Start the **Globus Connect Personal** applet.

- From a browser log into Globus and in the File Manager navigate to :bgrnd1:`Endpoints`. Then select the :bgrnd1:`Administered by you` tab.

- To change the attributes of an endpoint click on its name. You can adjust a variety of settings like private or public, endpoint name, contact info, and encryption.

.. figure:: local_endpoints/endpoints1.png

.. warning:: Users should use caution and carefully select the privacy permissions and attributes when creating endpoints on their personal computers.




Creating a managed endpoint
---------------------------

The five Flemish universities have a `High Assurance subscription <https://www.globus.org/subscriptions>`_ for Globus, which allows the creation of extra managed endpoints. 

VSC users and researchers from those universities can create their own managed endpoint under this subscription.  

You can find the technical prerequisites `here <https://docs.globus.org/globus-connect-server/v5.4/#globus_connect_server_prerequisites>`_.

If you want create your own managed endpoint, please mail to data@vscentrum.be. 

