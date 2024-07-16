.. _mango-portal:

############
ManGO Portal
############

The `ManGO portal <https://mango.vscentrum.be/>`_ is a graphical web interface for Tier-1 Data.
It allows users to manage their data in an intuitive way, without any installations,
with a strong focus on managing :ref:`metadata<metadata>`.

When logging in, you will be redirected to the login page of your institution. 
This takes you to an overview with one or multiple zones with at least one of the following options:

- Select 'Enter portal' to enter that zone via the ManGO portal.
- Select 'How to Connect' to get credentials for logging in to other clients, like :ref:`iCommands` or the :ref:`the PRC<python-client>`.
- Selecting the downward arrow opens an overview of all projects you are member of in that zone. Clicking on the project name sends you to the project management page. 

If you select the first option, you will be sent to the ManGO Portal home page:

.. figure:: ../images/mango_portal/mango_portal_main_page.png
  :width: 1000
  :alt: The main page of the ManGO portal


This main page has four main tabs:

- **Collections**, where you can manage the data in your collections.
- **Search**, where you can search for data objects and collections based on different criteria.
- **Trash**, where you can inspect and manage your :ref:`trash collection <trash>`.
- **Metadata schemas**, where you can view and mana metadata schemas.

*************************************
Managing collections and data objects
*************************************

The Collections tab provides an overview of the collections you have access to and lets you browse through them.
Clicking on the name of a subcollection shows you its contents under the "Content" tab: both subcollections and data objects.
If you click on a data object instead, you go to its page, which does not have such a "Content" tab.

Above the name of the current collection or data object, a breadcrumb menu allows you to go back to a collection on top of it. 
Next to the name, clicking on the pencil icon allows you to rename the active collection or data object.

The page of a collection also includes buttons to create a new collection and upload files,
which are only available if you have the right :ref:`permissions<collaboration>`.
Also depending on your permissions you may see a dropdown menu of bulk actions, allowing you to move, copy or delete one or more
collections or data objects at a time.
To do so, click on the checkbox next to the names of the collections or data objects, select your desired action and click on "apply".
When copying or moving, a list of collections will appear where you can browse to select a destination.
Notice that only data objects, not collections, can be copied.

Data objects do not have a "Content" tab, as they cannot contain any objects. 
Instead, they have a "System properties" tab, which contains some basic information about the object.
They also provide a "Preview" tab in which you can see a preview of the contents of your data object.
Previews are currently possible for the following filetypes:

* JPG
* JPEG
* PNG
* PDF 
* TIF
* TIFF
* GIF

Next to these specific tabs, both collections and data objects have a :ref:`"Metadata" <edit-metadata>` and :ref:`"Permissions" <edit-permissions>` tab
for inspection and management of metadata and permissions respectively.

******************************
Uploading and downloading data
******************************

Uploading and downloading data
==============================

Clicking on 'Upload files...' opens a white box, where you can put one or multiple files to be uploaded to the current collection:

- By dragging files from your local pc into the white box.
- By clicking inside the white box, which opens your file explorer, where you can select your files. 

.. image:: ../images/mango_portal/mango_portal_upload.png
  :width: 800
  :alt: Uploading files via the ManGO portal


If you made a mistake, you can click on 'Remove file' under the file in question. 
When you are ready, click on 'Start uploading files' to upload your selection. 

To download a single data object, you can click on the download-icon next to it:

.. figure:: ../images/mango_portal/mango_portal_download_from_dataobject_page.png

   *Downloading from the page of the data object*

.. figure:: ../images/mango_portal/mango_portal_download_from_parent_page.png

   *Downloading from the page of the parent collection*


You can also download multiple data objects at once, as long as they are part of the same collection.
To do so, go to the page of the collection and select the checkbox next to each data object you want to download.
Next, select 'Download' in the dropdown and click on 'apply':

.. image:: ../images/mango_portal/mango_portal_bulk_download.png
  :width: 800
  :alt: Downloading multiple data objects at the same time

The data objects will be downloaded together as a tar file.
A tar file is similar to a Zip folder, and can be extracted with a program like `7-Zip <https://www.7-zip.org/>`_ on Windows, or with the command `tar -xf <filename>` on Linux.

Uploads and downloads via the ManGO portal are limited to 5GB and 50GB per file respectively.
While it is possible to upload/download multiple files at once, it isn't possible to upload a folder or download a collection as a whole at the moment. 
If you want to transfer larger amounts of data via a graphical interface, you can use `Globus <https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/globus/globus_main_index.html>`_.

.. _edit-permissions:

***********
Permissions
***********

To view the :ref:`permissions<collaboration>` on a collection or data object, click on it and then go to the tab 'Permissions'. 

.. figure:: ../images/mango_portal/mango_portal_permissions.png
  :width: 800
  :alt: An overview of the permissions on a collection


If you have 'own' permissions yourself, you can add new permissions at the bottom of the page, remove permissions by clicking on the trash bin icon,
and switch on/off the inheritance for collection permissions.

You can give permissions to any group that you are member of. 
To do so, select the group and the rights you want to give from their respective dropdown menus and click on 'apply.'
If you are applying permissions to a collection, you can also indicate whether to apply the permissions recursively.

.. _edit-metadata:

**************
Metadata
**************

Every collection or data object has its own :ref:`metadata<metadata>` tab.
When you click on this tab, you can see all metadata which is added to the object. 

.. figure:: ../images/mango_portal/mango_portal_metadata_overview.png
  :alt: getting an overview of the metadata on an object


If only manual metadata is added, you get one overview of all the metadata.
However, if the metadata comes from multiple sources, the overview is split into tabs:

- Metadata added via schemas can be found in the tab with the name of the respective schema     
- Metadata added via automatic extraction can be found in the tab 'analysis'  
- Manually added metadata can be found in the tab 'other'   


On the right ride of each AVU, you may see the icons of a blue pencil and a red trashbin.
Clicking on the former allows you to overwrite the AVU, while the latter allows you to delete it.
If you do not have rights to edit/delete this metadata, these buttons may be absent.   


Adding metadata manually
========================

To add metadata manually, click on 'Add metadata' under the list of existing AVUs.  
This creates a window where you can freely add any AVU you want. 

.. figure:: ../images/mango_portal/mango_portal_metadata_manual.png
  :alt: Adding metadata manually 


Adding metadata via schemas
===========================

If you or one of your colleagues has created and published a metadata schema, you can apply it to a collection or data object.
To do so, select the schema name from the dropdown under the metadata overview, and click on 'apply schema'.


For more information about creating schemas, see the section on :ref:`metadata schemas<schemas>`

.. figure:: ../images/mango_portal/mango_portal_metadata_schema.png
  :alt: Adding metadata via a schema
  :width: 500

This will open a form where you can fill in the metadata that the creator specified.

.. figure:: ../images/mango_portal/mango_portal_metadata_schema_2.png
  :alt: Adding metadata via a schema (2)
  :width: 500

Metadata extraction
===================

To extract metadata from inside a data object, go to the tab 'Metadata inspection and extraction' of that object.  
When you click on 'Inspect with Tika', you will get an overview of all metadata which Apache Tika could find inside.

To actually add this information as metadata to the object, click on the checkbox behind the elements you are interested in, and click on 'Add selected metadata items as regular metadata'.  
Now this information will appear in the metadata overview, and will also be searcheable.
Note that you cannot edit metadata added via metadata extraction: you can only delete it.

Analysis by Apache Tika may also give an OCR (Optical Character Recognition) reading, which is an overview of all text recognized in e.g. an image.
This feature is a proof of concept, and this information can currently not be added as metadata. 


Searching
=========

The ManGO portal contains both a quick search bar and an advanced search form. 

The quick search bar is located on top of the webpage.   
You can find data objects and collections with it, by searching based on one of the following criteria:

- Name of the object
- Owner of the object
- Metadata fields containing the keyword 'name', 'title', 'description', 'comment' or 'summary'

To search, just type your search term in the search bar and press 'enter'.
You will get a list with links to the matching data objects/collections.

.. figure:: ../images/mango_portal/mango_portal_search_bar.png
  :alt: Searching via the search bar
  :width: 800

The advanced search tab is located on the left side of the screen.
This brings you to a form where you can search for data objects and collection based on several criteria.
You can also search based on any metadata fields.

If you want to search based on schema metadata, you will need to use the following convention:

- Attribute name: mgs.<schema_id>.<field_id>
- Attribute value: <value>

For example, if you want to search based on the field 'instrument' from the schema 'chemistry', you will need to search for attribute name 'mgs.chemistry.instrument'.

.. figure:: ../images/mango_portal/mango_portal_search_advanced.png
  :alt: Searching via the search tab
  :width: 800
