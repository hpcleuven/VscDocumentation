.. _python_client:

Python API Client - PRC
=======================

PRC is an API client implemented in python to access to iRODS. The main goal of PRC is to offer researchers means to manage their data in python. With the help of this client, users can manage their research data. Currently supported operations with PRC are quite various and range from “put/get data objects“ to “execution of iRODS rules”. We will cover here basic ones in addition to VSC-PRC (the Vlaams Supercomputing Centrum (VSC) extensions to the Python iRODS Client).

This client will be used inside the VSC like iCommands instead of reaching iRODS server from outside the VSC.

Installing/Requirements -- (Module_Maxime)
------------------------------------------

PRC requires Python 2.7 or 3.4+. Installation with pip is easy! To install with pip::

$ pip install python-irodsclient

or::

$ pip install git+https://github.com/irods/python-irodsclient.git[@branch|@commit|@tag]

A Secure Connection Settings
----------------------------

We will connect to iRODS using environment files as shown below.

::

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
        pass

Working with Collections
------------------------

A user can connect to a specific iRODS collection and see the some basic information with that. Also a user can reach to sub-collections and create a new collection.

To reach a specific collection, we should specify its absolute path.

::
    
    coll = session.collections.get("/kuleuven_tier1_pilot/home/vsc33586")

Once we get the response of a specific collection, we can simply check the id or path of this instance.

::

    coll.id
    11482

::

    coll.path
    '/kuleuven_tier1_pilot/home/vsc33586'

In order to see sub-collections of a collection:

::

    for i in coll.subcollections:
        print(i)

    <iRODSCollection 156064 b'Book'>
    <iRODSCollection 195699 b'dataExample'>
    <iRODSCollection 158305 b'KULeuven'>
    <iRODSCollection 156076 b'Math'>

We can also see the data files (objects) of a collection with the following command:

::

    for i in coll.data_objects:
        print(i)

    <iRODSDataObject 203376 2016_Book_RecommenderSystems.pdf>
    <iRODSDataObject 156079 algebra_linear>
    <iRODSDataObject 180004 hello.r>
    <iRODSDataObject 195936 HPCintro.pdf>
    <iRODSDataObject 203385 irods_VSC.txt>
    <iRODSDataObject 179989 list.r>
    <iRODSDataObject 156055 stream.txt>

It is possible to create a collection under a specific location.

:: 

    new_coll = session.collections.create("/kuleuven_tier1_pilot/home/vsc33586/data_test")
    new_coll.id

    285438

.. note:: If a collection we want to create has already existed, the PRC doesn't do anything, neither complains nor overwrites on the existed collection.

We can create a collection even recursively:

::

    coll_rec = session.collections.create("/kuleuven_tier1_pilot/home/vsc33586/test_A/test_B")
    coll_rec.name

    'test_B'

Working with data objects (files)
---------------------------------

To create a new data object, use the following code. 

::

    obj_new = session.data_objects.create("/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj")
    
    obj_new.path
    '/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj'

To get an existing data object and to see the imported object's details:

::

    obj = session.data_objects.get("/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj")
    
    obj.id
    285450

    obj.name
    'data_obj'

    obj.collection
    <iRODSCollection 285438 b'data_test'>

If we use built-in python vars function with the argument of obj, we can see all values related to this data object in a dictionary.

::

    vars(obj)

    {'manager': <irods.manager.data_object_manager.DataObjectManager at 0x7f811c06bbd0>,
    'collection': <iRODSCollection 285438 b'data_test'>,
    'id': 285450,
    'collection_id': 285438,
    'name': 'data_obj',
    'replica_number': 0,
    'version': None,
    'type': 'generic',
    'size': 0,
    'resource_name': 'tier1-p-irods-posix-3-b',
    'path': '/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj',
    'owner_name': 'vsc33586',
    'owner_zone': 'kuleuven_tier1_pilot',
    'replica_status': '1',
    'status': None,
    'checksum': None,
    'expiry': '00000000000',
    'map_id': 0,
    'comments': None,
    'create_time': datetime.datetime(2020, 6, 29, 7, 8, 26),
    'modify_time': datetime.datetime(2020, 6, 29, 7, 8, 26),
    'resc_hier': 'default;tier1-p-irods-2020-pilot;tier1-p-irods-2020-pilot-replication;tier1-p-irods-posix;tier1-p-irods-posix-1-4;tier1-p-irods-posix-3-b-2-b;tier1-p-irods-posix-3-b-weight;tier1-p-irods-posix-3-b',
    'resc_id': '10087',
    'replicas': [<irods.data_object.iRODSReplica tier1-p-irods-posix-3-b>],
    '_meta': None}

We can also upload an existing file (locally) as a new data object to iRODS. To do this we use "put" method.
First argument is the local file we want to upload and the second argument is the absolute path (collection + file name we have given) that well take the local data object.)

::

    session.data_objects.put("test1.txt","/kuleuven_tier1_pilot/home/vsc33586/data_test/test1.txt")

To see the result we can get the uploaded data object.

::

    obj2 = session.data_objects.get("/kuleuven_tier1_pilot/home/vsc33586/data_test/test1.txt")

    obj2.id
    285684

Reading and writing files
-------------------------

PRC provides file-like objects to be able to manipulate data file.

::

    obj = session.data_objects.get("/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj")

    with obj.open('r+') as f:
        f.write("Hello iRODS\n".encode())
        f.write("This is a test file".encode())
        f.seek(0)
        for line in f:
            print(line)
    
    b'Hello iRODS\n'
    b'This is a test file'

Working with metadata
---------------------

In order to work with metadata we first import the relevant class.

::

    from irods.meta import iRODSMeta

If we try to check a file with no metadata attached, the result should be an empty list.

::

    obj = session.data_objects.get("/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj")
    print(obj.metadata.items())

    []

Let’s now add some metadata. As we did with iCommand, we can add multiple AVU's with the same name field.

::

    obj.metadata.add('key1', 'value1', 'units1')
    obj.metadata.add('key1', 'value2')
    obj.metadata.add('key2', 'value3')
    
    print(obj.metadata.items())
    [<iRODSMeta 161995 key1 value1 units1>, <iRODSMeta 161998 key1 value2 None>, <iRODSMeta 162001 key2 value3 None>]




