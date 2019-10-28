.. include:: css.rst

.. _managing_and_transferring_files:

Managing and transferring files
-------------------------------

The File Manager
~~~~~~~~~~~~~~~~

After you have logged in to Globus, you will begin at the **File Manager**. The first time you use the File Manager, all fields will be blank.

.. image:: managing_and_transferring_files/filemanager-1.png


Globus Collections and Endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within Globus user data resides in a location called **Globus Collection**. Globus Collections can be hosted on various storage and computer systems, e.g., HPC clusters, laptops, or cloud storage. To use a collection you only need its name. It is not necessary to know any details about the storage or system where that collection is being hosted.

An **Endpoint** is a server that hosts collections. If you want to be able to access, share, transfer, or manage data using Globus, the first step is to create an endpoint on the system where the data is (or will be) stored.

To access a Globus Collection:

-  Click in the :bgrnd1:`Collection` field at the top of the File Manager page and search all available collections and endpoints by typing a collection/endpoint name or a description. Globus will list collections with matching names.

.. image:: managing_and_transferring_files/collection1.png

.. note:: At the VSC all Tier-1 and Tier-2 systems have dedicated Globus Collections. Type *vsc* in the search field to see the list.

-  Click on a collection. Globus will connect to the collection and display the default directory. Navigate either by typing the destination directory into the :bgrnd1:`Path` field, or browse the available directories below.


Transferring files
~~~~~~~~~~~~~~~~~~

VSC users can use Globus to transfer files and data between collections they have access to. Those can be, e.g., own VSC */scratch* and */data* directories on Tier-1 and Tier-2, or any other remote and local server collection.

To transfer data between two collections:

- Click :bgrnd1:`Transfer` or :bgrnd1:`Sync to...` in the command panel on the right side of the page. A new collection panel will open, with a :bgrnd1:`Transfer or Sync to` field at the top of the panel. Alternatively, use the :bgrnd1:`Panels` toggle button in the top right corner to split the directory tree panel and select a destination collection.

- Find and choose the second collection and connect to it as you did with the first one. Click on the left first collection and select all the files to transfer. The :bgrnd1:`Start` button at the bottom of the panel will become active. Between the two :bgrnd1:`Start` buttons at the bottom of the page, the :bgrnd1:`Transfer and Sync Options` tab provides access to several options. By default, Globus verifies file integrity after transfer using checksums. Change the transfer settings if you would like. You may also enter a label for the transfer.

- Click the :bgrnd1:`Start` button to transfer the selected files to the collection in the right panel. Globus will display a green notification panel - confirming that the transfer request was submitted - and add a badge to the :bgrnd1:`Activity` item in the command menu on the left of the page. You can navigate away from the File Manager, close the browser window, and even logout. Globus will optimize the transfer for performance, monitor the transfer for completion and correctness, and recover from network errors and collection downtime.

.. image:: managing_and_transferring_files/filetransfer-2.png

Completed file transfers can be seen in the :bgrnd1:`Activity` tab in the command menu on the left of the page. On the Activity page, click the arrow icon on the right to view details about the transfer. You will also receive an email with the transfer details.

.. include:: links.rst
