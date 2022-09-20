.. _data_discovery:

Data Discovery
==============

iRODS allows users and administrators to access and contribute descriptive information about their data (metadata). This metadata improves the search experience and therefore better enables data discovery. Users can search for data objects using any metadata descriptor as search terms. 
Both automatic, system-generated metadata and user-created metadata are supported in iRODS. 

What is metadata?
-----------------

Metadata is often called data about data. It describes the data in some way, such as providing information about the content, context of its origin or use, quality, condition, and associations to other data and objects. Metadata can describe a collection, a file or a component of file.
Metadata can be embedded in a data object, or stored in a database and linked to the object it describes. Metadata is used to facilitate data discovery to improve search and retrieval. 

Scholars classify metadata into three categories: descriptive, structural, and administrative. Descriptive metadata is intended to support data discovery and identification. Title, abstract and keywords are some example to descriptive metadata. Structural metadata describes the structure of the data object. For example, title page, chapters, how pages are ordered, number of pages, etc. Administrative metadata is intended to facilitate management and processing of the data. Identifying how the data was created, its file type, resolution, copyright information, licensing
information, access privileges are some administrative metadata examples.

Why metadata?
-------------

Metadata serves a variety of purposes, with resource discovery one of the most common. Here, it can be compared to effective cataloging, which includes identifying resources, defining them by criteria, bringing similar resources together and distinguishing among those that are dissimilar.
It is also a means of facilitating interoperability and integrating resources. Using metadata to describe resources enables its understanding by humans as well as machines. 
In addition to supporting data discovery, metadata also organizes and provides contextual and historical information about data objects, identifies structural relationships within and between data objects.

Create Attribute, Value, Unit triples
-------------------------------------

iRODS provides the user with the possibility to create Attribute-Value-Unit (AVU) triples and associate them with the data. The triplets are stored in the iCAT catalogue (in the database), which can be queried to identify and retrieve the correct objects.
This enables us to ask the iRODS system to provide me all data (files and collections) based on the matching query criteria.
First we will explore how to create these AVU triples for which we can search later.

- Annotate a data file::

    $ imeta add -d test1.txt weight 2 kg

    $ imeta add -d test1.txt 'author' 'Jan Ooghe' 'ICTS'

    $ imeta add -d test1.txt 'shareable' yes

For the last one we put the 'Unit' part empty. That means unit is not mandatory to write if there is no relevant element for that. Please note that apostrophes are not mandatory but are needed to store Values containing spaces.

- Annotate a collection::

    $ imeta add -C dataExample 'type' 'collection'
    
    $ imeta add -C dataExample 'book' 'chemistry' 'KULeuven'

List metadata
-------------

In order to list metadata of a file we do::

$ imeta ls -d test1.txt

and to list a collection's metadata::

$ imeta ls -C dataExample

Queries of data
---------------

The imeta command allows users to define simple queries::

$ imeta qu -d weight = 2

However we should use sql-like queries with ``iquest`` command for more sophisticated searches.

With the following command we can fetch the data file, given the attribute 'author'::

$ iquest "select COLL_NAME, DATA_NAME, META_DATA_ATTR_VALUE where META_DATA_ATTR_NAME like 'author'" 

We can find our text1.txt file with the below query:

::

    $ iquest "select DATA_NAME,DATA_SIZE where DATA_SIZE BETWEEN '20' '30'"

        DATA_NAME = test1-restore.txt
        DATA_SIZE = 26
        ---------------------------------------
        DATA_NAME = test1.txt
        DATA_SIZE = 26
        ---------------------------------------

These examples illustrate the importance of metadata in the data management domain.