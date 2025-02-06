.. _python-client:

########################
Python-iRODSClient - PRC
########################

The Python-iRODSClient (PRC) is an API to iRODS, the underlying system behind Tier-1 Data.
The goal of the PRC is to offer researchers means to manage their data in Tier-1 Data through python.

************
Installation
************

The Python-iRODSclient can be installed with pip as follows:

.. code-block:: sh

   pip install python-irodsclient

On Genius and wICE, the Tier-2 HPC clusters of the KU Leuven, the Python-irodsclient (version 1.1.4.) is already installed as a module. You can install this module as follows:

.. code-block:: sh

   module use /apps/leuven/<node_architecture>/2021a/modules/all
   module load python-irodsclient/1.1.4-GCCcore-10.3.0

You should replace <node_architecture> with the architecture of the
(login) node you are on ('cascadelake', 'skylake' or 'broadwell').

On Hortense and Stevin, the HPC-clusters of UGent, you can load the module as follows:

.. code-block:: sh

    module load python-irodsclient/1.1.4-GCCcore-11.2.0

**************
Authenticating
**************

There are three ways to authenticate with the Python-iRODSclient:

1. Follow the instructions on the `ManGO portal <https://mango.vscentrum.be/>`_
   > 'How to Connect' > 'Python Client on Windows'. This method, despite the
   title, should work for any operating system.

2. Windows users can download `iinit.exe <https://rdmrepo-proxy.icts.kuleuven.be/artifactory/coz-p-foz-generic-public/iinit.signed.exe>`_.
   Double click on the file and enter your zone name in the window that pops
   up. You might need to put the file in a folder that doesn't require administrator rights.  

3. Linux users can first authenticate with :ref:`icommands`. 
   The user is also authenticated for the Python-iRODSClient.

.. note::
  Method 1 and 2 authenticate you for approximately 60 hours, and method 3 for approximately 7 days.  

Creating a session
------------------

To take actions in Tier-1 Data, you need to create an iRODSSession object. 

In a script, this can be done as follows:

.. code-block:: python
   :linenos:

   import os
   import ssl
   from irods.session import iRODSSession
   try:
       env_file = os.environ['IRODS_ENVIRONMENT_FILE']
   except KeyError:
       env_file = os.path.expanduser('~/.irods/irods_environment.json')

   ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
   ssl_settings = {'ssl_context': ssl_context}

   with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:
       [your code here]

In an interactive session you might want to replace the with statement above with:

.. code-block:: python

   session = iRODSSession(irods_env_file=env_file, **ssl_settings)

In that case, you should clean up your session at the end:

.. code-block:: python

   session.cleanup()

***********
Collections
***********

Via the PRC, you can retrieve any collection in Tier-1 Data as an iRODSCollection object.
This can be done as follows:

.. code-block:: python

   coll = session.collections.get("/path/to/existing/collection")


You can also create a collection with the PRC.
This method will return an iRODSCollection object as well.

.. code-block:: python

   coll = session.collections.create("/path/to/newCollection")


This iRODSCollection object contains serveral attributes with information about the collection:

.. list-table:: 
   :header-rows: 1
   :widths: 20 40 40

   * - Attribute 
     - Result
     - Example
   * - ``coll.id``
     - The ID of the collection
     - ``10074``
   * - ``coll.name``
     - the name of the collection
     - ``'biology'``
   * - ``coll.path``
     - The full path of the collection
     - ``'/set/home/biology'``
   * - ``coll.subcollections``
     - List of subcollections inside the collection (non-recursive)
     - ``[<iRODSCollection 32701 b'flora'>, <iRODSCollection 57012 b'fauna'>]``
   * - ``coll.data_objects``
     - List of data objects inside the collection (non-recursive)
     - ``[<iRODSDataObject 10473 readme.md>]``
   * - ``coll.metadata.items()``
     - List of metadata items attached to the collection
     - ``[<iRODSMeta 17481 department science None>, <iRODSMeta 27283 size 25 members>]``

It also contains some useful methods:

.. list-table:: 
   :header-rows: 1
   :widths: 20 80

   * - Method
     - Result
   * - ``coll.walk()``
     - Creates a generator object with all data objects and subcollections inside the collection (recursive)
   * - ``coll.move(destination)``
     - Moves collection to the destination given as argument
   * - ``coll.remove()``
     - Moves the collection and its contents to your trash collection



*************
Data objects
*************

Similar to collections, data objects can be retrieved as iRODSDataObjects:

.. code-block:: python

   obj = session.data_objects.get("/path/to/existing/data")

Creating an empty data object will return an iRODSDataObject as well:

.. code-block:: python

   new_obj = session.data_objects.create("/path/to/new/object")

This iRODSDataObject object contains serveral attributes with information about the data object:

.. list-table:: 
   :header-rows: 1
   :widths: 20 40 40

   * - Attribute 
     - Result
     - Example
   * - ``obj.id``
     - The ID of the data object
     - ``10074``
   * - ``obj.name``
     - The name of the data object
     - ``'readme.md'``
   * - ``obj.path``
     - The full path of the data object
     - ``'/set/home/biology/readme.md'``
   * - ``obj.size``
     - The size of the data object in bytes
     - ``100``
   * - ``obj.metadata.items()``
     - List of metadata items attached to the collection
     - ``[<iRODSMeta 17481 type documentation None>, <iRODSMeta 27283 author Emily None>]``

It also contains some useful methods:

.. list-table:: 
   :header-rows: 1
   :widths: 20 80

   * - Method
     - Result
   * - ``obj.chksum()``
     - Calculates and stores the checksum of the object in the database
   * - ``obj.open(mode)``
     - Opens the data object as a file object in Python in read ('r'), write ('w') or append 'a' mode
   * - ``obj.unlink()``
     - Moves the data object and to your trash collection

Please note that the 'open' method is not suited for heavy IO. 

*************************
Uploading and downloading
*************************

In most cases, users will not create empty data objects, but instead upload files from their local filesystem.
This can be done as follows:

.. code-block:: python

   session.data_objects.put("/path/to/local/file", "/path/to/collection")

If the destination refers to an (existing) collection, the PRC automatically appends the filename of the local file to the path.
However, you can also define a filename yourself, by appending it to the end of the path.

Earlier, we saw that the function ``session.data_objects.get()`` is used to retrieve a python representation of a data object.
However, when you provide a path to the local destination as second argument, it also downloads the data object to your pc:

.. code-block:: python

   session.data_objects.get('/path/to_existing/data_object', '/path/to/local/directory')

Here as well, you can just provide the path to a directory, or specify a filename.

***********
Permissions
***********

In the PRC, you can create iRODSAccess objects, which represent a permission on a certain collection or data object.
Each iRODSAccess object has an access type, a path it applies to, and the user or group that gets access.
These permissions can be applied with ``session.acls.set()``.
If the object in question is a collection, you can apply the permission recursively by adding the argument ``recursive = True``.

.. code-block:: python

   from irods.access import iRODSAccess
   access = iRODSAccess("read", "/path/to/collection/or/data/object", "John")
   session.acls.set(access, recursive = True)


You can also set or unset inheritance of a collection this way:

.. code-block:: python

   # Turning inheritance on
   access = iRODSAccess("inherit", "/path/to/collection")
   session.acls.set(access)

   # Turning inheritance off
   access = iRODSAccess("noinherit", "/path/to/collection")
   session.acls.set(access)


You can retrieve the permissions on an object with ``session.permissions.get(object)``. 
This will return a list of iRODSAccess objects:

.. code-block:: python

   coll = session.collections.get("/path/to/collection")
   permissions = session.acls.get(coll)


Lastly, you can give someone 'null' permissions to revoke their permissions on an object:

.. code-block:: python

   access = iRODSAccess("null", "/path/to/collection/or/data/object", "Chris")
   session.acls.set(access)

Note that ``session.acls.set()`` and ``sessions.acls.get()`` only work for the most recent releases of the Python-iRODSclient.
For older releases, you should replace 'acls' with 'permissions'.

********
Metadata
********

The following methods are available to work with metadata on collections and data objects:


.. list-table:: 
   :header-rows: 1
   :widths: 40 60

   * - Method
     - Result
   * - ``obj.metadata.add(attribute, value, <unit>)``
     - Adds the AVU to the object.
   * - ``obj.metadata.set(attribute, value, <unit>)``
     - Adds the AVU to the object. Overwrites previous AVUS with the same attribute name, if they exist.
   * - ``obj.metadata.items()``
     - Returns a list of all AVUS on the object as iRODSMeta objects.
   * - ``obj.metadata.remove(attribute, value, <unit>)``
     - Removes the AVU


If you want to add lots of metadata to the same object, it can take long to do this with one function call for each AVU.
To speed things up, the PRC offers a function that allows you to add or remove several AVU's from an object in one API call:

.. code-block:: python

   from irods.meta import iRODSMeta, AVUOperation
   obj.metadata.apply_atomic_operations(AVUOperation(operation='add', avu=iRODSMeta('attribute1','value1','unit1')),
                                        AVUOperation(operation='add', avu=iRODSMeta('attribute2','value2','unit2')),
                                        AVUOperation(operation='add', avu=iRODSMeta('attribute3','value3','unit3'))
                                       )

The same can be used to remove several AVUs from an object in one call, but if you want to remove all of them there is a handier method.

.. code-block:: python

   obj.metadata.remove_all()

*********
Searching 
*********

The PRC allows you to build queries, which are database searches for specific information about collections, data objects, metadata...
For example, to get the names and sizes of all the data objects you have access to, you can write the following query:

.. code-block:: python

   from irods.models import DataObject

   query = session.query(DataObject)
   for result in query:
      print(result[DataObject.name], result[DataObject.size])


Before you write your query, you should import the relevant classes from the module irods.models.
These are the most important classes, with some of their attributes:


.. list-table:: 
   :header-rows: 1
   :widths: 25 25 50

   * - Class
     - Represents
     - Searchable attributes
   * - ``irods.models.Collection``
     - A collection in iRODS
     - id, name, parent_name, owner_name, inheritance, create_time, modify_time...
   * - ``irods.models.DataObject``
     - A data object in iRODS
     - id, collection_id, name, size, path, owner_name, status, checksum, create_time, modify_time...
   * - ``irods.models.CollectionMeta``
     - A metadata AVU on a collection
     - id, name, value, units, create_time, modify_time
   * - ``irods.models.DataObjectMeta``
     - A metadata AVU on a data object
     - id, name, value, units, create_time, modify_time
   * - ``irods.models.User``
     - A user or group in iRODS
     - id, name, type, zone, create_time, modify_time

Unfortunately, Classes from iRODS.models have some attributes which can be confusing:

- ``Collection.name`` contains the full path of the collection.
- ``DataObject.name`` contains only the name of the data object.
- ``DataObject.path`` contains the physical path of the data object, i.e. the location where the file physically is stored in the data centers.
- ``CollectionMeta.name`` and ``DataObjectMeta.name`` contain the attribute of the AVU.

You can find the logical path of a data object by putting together its Collection.name and DataObject.name, with a slash in between.


You can combine different classes in one query.
For example, you can search for data objects and their parent collections as follows:

.. code-block:: python

   from irods.models import Collection, DataObject

   query = session.query(Collection, DataObject)
   for result in query:
      print(f"{result[DataObject.name]} is part of collection {result[Collection.name]}")

Of course, often you will want to restrict the results of your query based on some criteria.
This can be done via the `filter()` method; 
for example, the following query searches for Data Objects with the AVU 'type: organic'.

.. code-block:: python

   from irods.column import Criterion
   from irods.models import DataObject, Collection, CollectionMeta

   query = session.query(DataObject, Collection)
   query.filter(Criterion('=', DataObjectMeta.name, 'type'))
   query.filter(Criterion('=', DataObjectMeta.value, 'organic'))

   for result in query:
      print(result[Collection.name], result[DataObject.name])


As comparison operators, for filtering, you can use:

- '=' for exact matches
- '!=' for excluding certain terms
- 'like' for partial matches
- 'not like' for excluding certain patterns

If you use 'like' and 'not like', you should use '%' as wildcard character.
For example, ``Criterion('like', Collection.name, '/set/home/biology%')`` will match the collection ``/set/home/biology`` and all its subcollections.  
However, be aware that searching for partial matches has a higher performance cost than searching for exact matches.  

***************
Further reading
***************

If you would like to see more details and examples, you can have a look
at the following link of original PRC documentation,
https://github.com/irods/python-irodsclient.

