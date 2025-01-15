.. _collaboration: 

##############################
Sharing data and collaboration
##############################

Depending on your research project, different people might need different access to the data stored in Tier-1 Data.

Some projects are very open: everyone can work on all data in the project.  
Other projects, especially those with sensitive data, might need to be more strict in who can access which data and in which manner.
Tier-1 Data allows you to manage this in detail by assigning different levels of access to *groups*, which can consist of any number of users.

****************
Groups and users
****************
In Tier-1 Data, individual users can be put together in groups. 
Currently, we distinguish between two groups: project groups and access groups.  

A **project group** is created when a research group applies for a project in Tier-1 Data.
It includes all collaborators on the project, and has a shared collection.

**Access groups** are subgroups of a project group and are used to assign specific permissions to certain users based on their roles.
For example, data providers and data analysts may need different permissions on the datasets of the project. By creating an access group for data providers
with the users that have this role you can define which permissions all data providers have based on that role (e.g. writing data to a certain collection).
The same goes for data analysts, who would need read-only access to the datasets but write-access to a collection for results.
A user that has both roles will have both sets of permissions. This way, permissions are not assigned to individuals based on who they are but based on their role in the project.

For example:

- Chemistry (project group)  
  - Mary
  - John
  - Chris
- Chemistry_data_providers (access group)  
  - John
- Chemistry_data_analysts (access group)  
  - Mary
  - Chris 

Depending on the client, permissions can be applied to users and group.
However, in general we recommend using group permissions.

In the ManGO portal, permissions can only be applied at the group level.

***********
Permissions
***********

In Tier-1 Data, you can apply permissions to both data objects and collection.  
A permission gives a group or user a certain type of access.

There are 4 types of access: null (no permissions), read, write, own. As the table below shows,
these permissions are cumulative: write permissions imply read permissions, and own permissions imply write permissions.

.. list-table:: 
   :header-rows: 1

   * - Action
     - Read
     - Write
     - Own
   * - View
     - ✓
     - ✓
     - ✓
   * - Download (data object)
     - ✓
     - ✓
     - ✓
   * - Copy
     - ✓
     - ✓
     - ✓
   * - Edit/overwrite (data object)
     -
     - ✓
     - ✓
   * - Create new files/collections (collection)
     -
     - ✓
     - ✓
   * - Metadata
     - View
     - Edit
     - Edit
   * - Rename
     - 
     - 
     - ✓
   * - Move
     - 
     - 
     - ✓
   * - Delete
     - 
     - 
     - ✓
   * - Change permissions
     -
     -
     - ✓


'Null' access allows no actions. Assigning 'null' permissions is equivalent to removing existing permissions. 
    
Each permission relates to a specific collection or data object.  
For example, you can give a group access to a specific collection, but not to the subcollections or data objects under it.

- Chemistry (Mary - read)

  - ExperimentA (Mary - write)

    - result1.txt 
    - result2.txt 
    - result3.txt

  - ExperimentB

    - result1.txt 
    - result2.txt
    - result3.txt

In this example, Mary will see the collection Chemistry and its subcollection ExperimentA, but not ExperimentB.
Furthermore, she will not be able to see the data objects inside of ExperimentA.
However, she can upload new files to this collection herself. 

It's important to stress that one object can have multiple permissions:

- CollectionA

  - GroupA: read access
  - GroupB: read access
  - GroupC: write access
  - GroupD: own access

This way, it is possible that a person can derive access to an object from multiple permissions.
If Mary is part of both GroupA and GroupC, she will have write access to CollectionA (because this is the highest level of access given to her).  


Inheritance and recursiveness
=============================

If we would have to manage permissions individually for every new collection or data object, this would take a long time.
To solve this problem, we can make use of inheritance and recursiveness.

**Inheritance** is an attribute of a collection. If it is turned on, all collections or data objects that get created/uploaded under that collection inherit its permissions automatically:

- Chemistry

  - ExperimentA (Chemistry_data_providers - own, inheritance - on)

    - Newfile.txt (Chemistry_data_providers - own)
    - Newcollection (Chemistry_data_providers - own, inheritance - on)

If inheritance is turned off, permissions from the parent collection are not applied.
The person who creates/uploads new data objects/collections gets own access by default, but no other permissions are added:

- Chemistry

  - ExperimentA (Chemistry_data_providers - own, inheritance - off)

    - Newfile.txt (John - own)
    - Newcollection (John - own)

Inheritance only has an effect on data added *after* inheritance has been enabled.
If you enable inheritance for a collection, existing subcollections and data objects are not affected.

**Recursiveness** is an attribute of an action. When you apply permissions to a collection, you can do so recursively:
in that case, the permission will be applied to all the existing contents of the collection as well.
Unlike inheritance, applying permissions recursively does not affect data which is added later.


.. warning:: Past permissions on a data object or collection are overwritten by the new permissions. If you apply new permissions on a collection and/or its contents you cannot automatically reset the previous permissions; you will need to remember the previous permissions, and overwrite the current permissions again. 

Access to parent collection
===========================

In ManGO, if you want to share data with someone, they need access to all collections above it. Take the following example:

- Chemistry

  - ExperimentA

    - Input
    - Output

      - results.csv 

If you want to share the data object results.csv with someone, they need read access to Chemistry, ExperimentA and Output in order to browse to your data object.
Without this read access, they can't even see that Chemistry and its subcollections exist.

Some clients (like :ref:`the PRC <python-client>`) allow you to access data by providing the absolute path of the data object, instead of browsing.  
In this case, the user you want to share "results.csv" with only needs access to the parent collection of the data object (in this case, Output).


Ownership
=========

Every collection or data object has an owner defined in the database.  
This is the user who created the collection or uploaded the data object in question.
In some cases, the owner can also be a group. 

While the terms seem similar, ownership and own permissions aren't related. 
However, it should be noted that, for technical reasons, it's hard to deny the owner of an object access to it.  

