.. _metalnx:

Metalnx Portal Client for VSC Users
===================================

Metalnx is a graphical user interface and serves as a client to iRODS. It helps to simplify most administration, collection management, and metadata management tasks removing the need to memorize the long list of iCommands. It allows users to manage content and metadata associated with content.

You can reach the Metalnx portal by clicking `Metalnx <https://irods.hpc.kuleuven.be/metalnx/>`__.

You will need to authenticate with your institutional account and then you will be automatically login on the interface with your VSC account. Users from some institutions might encounter a second login page, but the credentials should already be filled in.

Metalnx portal is mainly composed of two panes. The left pane keeps the relevant tabs of our deployment instance and the right pane provides us with the selected tabs’ functionalities.

.. image:: metalnx/metalnx_general.PNG

**Collections**: Under this tab, we can perform all data object (= a file) and collection related activities
 
- Uploading files
- Moving files/collections 
- Copying files/collections 
- Renaming files/collections 
- Applying metadata templates
- Downloading files 

Behind any collection or file, you can press 'View info' for the following options:

- Adding metadata to files/collections
- Adding files/collections to favorites
- Setting permissions
- Getting previews of files

This tab and its functionalities are mostly used in Metalnx.

**Search**: This tab gives search options based on the metadata and properties parameters (currently not available due to a bug in the software that should be fixed soon).

**Templates**: We can here create our own metadata templates or import a template from outside in a json format. These can then be applied to files or collections.

**Shared Links**: Here you can see the links shared by other users.

**Favorites**: Here you can see your bookmarked collections and files.

**Public**: here you can reach the public area collections.

**Trash**: Here you can see the files and collections moved to trash bin.