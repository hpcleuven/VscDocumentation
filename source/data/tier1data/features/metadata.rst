.. _metadata:

########
Metadata
########


Tier-1 Data allows users to add descriptive information about data objects and collections in the form of metadata.
Contextualizing data with metadata has several advantages:

- The context of the data is more clear for researchers that are not familiar with it (even yourself in the future!)
- Data can be searched back based on its metadata
- Metadata can be used to steer different processes, e.g. a collection could be tagged as 'to be archived'.

*****************
What is metadata?
*****************

Metadata is often called "data about data". It describes the data in some
way, such as providing information about the content, origin, usage,
quality, condition, and associations to other data and
objects. Metadata can describe a collection, a file or a component of
file. Metadata can be embedded in a data object or stored in a database
and linked to the object it describes. Importantly, it can be used to facilitate
data discovery, improving search and retrieval.

Metadata can be descriptive, structural, or administrative.
Descriptive metadata is intended to support data discovery and identification,
such as title, abstract and keywords.
Structural metadata describes the structure of an item, e.g. chapters, how
pages are ordered, number of pages, etc.
Administrative metadata is intended to facilitate the management and processing of the data.
Some examples are date and manner of creation, file type, resolution,
copyright information, licensing information and access privileges.

*****************
Why metadata?
*****************

Metadata serves a variety of purposes, with resource discovery one of
the most common. Here, it can be compared to effective cataloging, which
includes identifying resources, defining them by criteria, and categorizing them
based on these criteria.
It also facilites interoperability and the integration of resources.
Moreover, metadata can be read and understood by humas as well as machines.
In addition to supporting data discovery, metadata also organizes and provides contextual and
historical information about data objects, identifies structural
relationships within and between data objects.

************************
Metadata in Tier-1 Data
************************


In Tier-1 Data, metadata are stored as so-called AVUs (attribute-value-unit triples).  
In many cases (when units are not used) they can be viewed as key-value pairs.


.. list-table::
   :header-rows: 1

   * - Attribute name
     - Value
     - Units
   * - Name
     - Apple
     - 
   * - Category
     - Fruit
     - 
   * - Colour
     - Green
     - 
   * - Size
     - 10
     - cm   
   * - Sourness
     - 3.5
     - Ph

The attribute name represents the 'label' or name of some characteristic or property,
while the value, naturally, indicates the value that said property takes for the item in question.
The units are an optional field, meant for specifying measurement units.
For example, 'size 10' may not be informative enough; we may need to know in which units (meters, centimeters, parsecs...) this measurement is expressed.

AVUs can be added both to collections and data objects.
All metadata in Tier-1 Data are stored in the database as case-sensitive strings.

*****************
Adding metadata
*****************

Metadata can be added to data in Tier-1 Data in three ways:

1) Manually adding an AVU to an object

   Adding AVUs to objects manually is the default method, and is possible via the ManGO portal, iCommands and the Python client. 

2) Automatic extraction of metadata from file headers

   Many types of files contain contextual information in their header. 
   In the ManGO Portal, you can inspect which contextual information is hidden in your data objects, select the information you find relevant, and add it as AVUs.

3) Adding metadata via schemas

   Adding metadata manually can be time-consuming, and prone to human errors (like typos).
   In the ManGO portal, you can create metadata schemas.
   These schemas allow you to ask for specific fields and put restrictions on the answers users give.
   Then, you and your colleagues can use apply these schemas to add metadata to objects via an online form. 







