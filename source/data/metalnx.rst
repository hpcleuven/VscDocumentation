.. _metalnx:

Metalnx Portal Client for VSC Users
===================================

Metalnx is a graphical user interface and serves as a client to iRODS. It helps to simplify most administration, collection management, and metadata management tasks removing the need to memorize the long list of iCommands. It allows users to manage content and metadata associated with content.

You can reach the Metalnx portal here: `<https://irods.hpc.kuleuven.be/metalnx/>`_.

You will need to authenticate with your institutional account and then you automatically login on the interface with your VSC account. Users from some institutions might encounter a second login page, but the credentials should already be filled in.

The Metalnx portal is mainly composed of two panes. The left pane keeps the relevant tabs of our deployment instance and the right pane provides us with the selected tabs' functionalities.

.. image:: metalnx/metalnx_general.PNG

**Collections**: Under this tab, we can perform all data object (= a file) and collection-related activities:
 
- Creating collections
- Uploading files
- Moving files/collections 
- Copying files/collections 
- Renaming files/collections 
- Applying metadata templates
- Downloading files
- Removing collections and files

Behind any collection or file, you can press 'View info' for the following options:

- Viewing system-generated metadata
- Adding metadata to files/collections
- Adding files/collections to favorites
- Setting permissions to files/collections
- Getting previews of files

This tab and its functionalities are mostly used in Metalnx.

**AVU Search**: This tab gives search options based on the metadata and properties parameters (currently not available due to a bug in the software that should be fixed soon). This would allow you to query the Attribute-Value-Unit triples defined in iRODS.

**Templates**: We can here create our own metadata templates or import a template from outside in a json format. A template provides any number of predefined AVUs. When applying such a template to a files or collections, it prompts to complete or modify the predefined AVU. Only the attribute name is required, and this can be used to ensure that users make use of the same attribute to store the same type of information. The same attribute can occur multiple times in the schema and the AVUs. By adding a value and unit in the template, you help users in quickly selecting the right possibilities.

**Shared Links**: Here you can see the links shared by other users.

**Favorites**: Here you can see your bookmarked collections and files.

**Public**: Here you reach the public area collections. These are stored in the /kuleuven_tier1_pilot/home/public/ Collection.

**Trash**: Here you can see the files and collections moved to the trash bin after either a soft delete (without -f flag) with an iRODS iCommand or via the delete functionality of Metalnx.