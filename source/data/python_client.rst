.. _python_client:

Python API Client - PRC
=======================

The Python iRODS Client (PRC) is an API client implemented in python to access to iRODS. The main goal of the PRC is to offer researchers means to manage their data in python. With the help of this client, users can manage their research data. Currently supported operations with PRC are quite various and range from “put/get data objects“ to “execution of iRODS rules”. We will cover here basic ones in addition to VSC-PRC (the Vlaams Supercomputing Centrum (VSC) extensions to the Python iRODS Client).

This client will be used inside the VSC like iCommands instead of reaching iRODS server from outside the VSC.

Installing/Dependencies
-----------------------

We recommend to set up PRC and VSC-PRC via the module system as follows:

::

    module use /apps/leuven/common/modules/all
    module load vsc-python-irodsclient

.. note:: PRC and VSC-PRC require Python 3 and hence cannot be used with Python 2 interpreters.


.. note:: There is also a module on the HPC clusters of KU Leuven with only the bare python-irodsclient (version 1.1.4).
    You can use it as follows:
 
    ::

        module use /apps/leuven/<node_architecture>/2021a/modules/all
        module load python-irodsclient/1.1.4-GCCcore-10.3.0

    You should replace <node_architecture> with the architecture of the (login) node you are on ('cascadelake', 'skylake' or 'broadwell').

    However, in the following examples, the module 'vsc-python-irodsclient' will be used.  


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

    new_coll = session.collections.create('/kuleuven_tier1_pilot/home/vsc33586/data_test')
    new_coll.id

    285438

.. note:: If a collection we want to create already exists, the PRC doesn't do anything, and neither complains nor overwrites the existed collection.

We can create a collection even recursively:

::

    coll_rec = session.collections.create('/kuleuven_tier1_pilot/home/vsc33586/test_A/test_B')
    coll_rec.name

    'test_B'

Working with data objects (files)
---------------------------------

To create a new data object, use the following code. 

::

    obj_new = session.data_objects.create('/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj')
    
    obj_new.path
    '/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj'

To get an existing data object and to see the imported object's details:

::

    obj = session.data_objects.get('/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj')
    
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

    session.data_objects.put('test1.txt','/kuleuven_tier1_pilot/home/vsc33586/data_test/test1.txt')

To see the result we can get the uploaded data object.

::

    obj2 = session.data_objects.get('/kuleuven_tier1_pilot/home/vsc33586/data_test/test1.txt')

    obj2.id
    285684

If we would like to delete the data object, we use the code below. But notice that the force option is important, since a data object in the trash does still exist.

::

    obj.unlink(force=True)

Reading and writing files
-------------------------

The PRC provides file-like manipulations for data objects:.

::

    obj = session.data_objects.get('/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj')

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

    obj = session.data_objects.get('/kuleuven_tier1_pilot/home/vsc33586/data_test/data_obj')
    print(obj.metadata.items())

    []

Let's now add some metadata. As we did with the iCommand, we can add multiple AVU's with the same name field.

::

    obj.metadata.add('key1', 'value1', 'units1')
    obj.metadata.add('key1', 'value2')
    obj.metadata.add('key2', 'value3')
    
    print(obj.metadata.items())
    [<iRODSMeta 161995 key1 value1 units1>, <iRODSMeta 161998 key1 value2 None>, <iRODSMeta 162001 key2 value3 None>]

We can update any added metadata with Python's item indexing syntax referring an existing attribute to set all AVU's with name field "key2" to a single value and unit.

::

    meta_update = iRODSMeta('key2', 'python_API_training', 'version1')
    obj.metadata[meta_update.name] = meta_update
    
    print(obj.metadata.items())
    [<iRODSMeta 161995 key1 value1 units1>, <iRODSMeta 161998 key1 value2 None>, <iRODSMeta 291438 key2 python_API_training version1>]

If we know an AVU key is present only once, we can use the get_one method as in the following example. This method returns an AVU for the given unique attribute.

::

    print(obj.metadata.get_one('key2'))
    <iRODSMeta 291438 key2 python_API_training version1>

To remove a specific AVU from an object, use the following command.

::

    obj.metadata.remove('key1', 'value1', 'units1')
    
    print(obj.metadata.items())
    [<iRODSMeta 161998 key1 value2 None>, <iRODSMeta 291438 key2 python_API_training version1>]

We can also use a for loop to remove all existing AVUs from a data object.

::

    for avu in obj.metadata.items():
    obj.metadata.remove(avu)
    
    print(obj.metadata.items())
    []

General queries with PRC
------------------------

We can collect all Collection and DataObject objects of all projects that we are assigned to with the following general query. We can then use the result list for further lookups. 

::

    import os
    from irods.session import iRODSSession
    from irods.models import Collection, DataObject

    env_file = os.path.expanduser('~/.irods/irods_environment.json')
    with iRODSSession(irods_env_file=env_file) as session:
        query = session.query(Collection.name, DataObject.id, DataObject.name, DataObject.size, DataObject.create_time)
        
        for result in query:
            print('{}/{}, size={}, create_time={}'.format(result[Collection.name], result[DataObject.name], result[DataObject.size], result[DataObject.create_time]))

    /kuleuven_tier1_pilot/home/vsc33586/test_AA, size=0, create_time=2020-06-30 12:26:30
    /kuleuven_tier1_pilot/home/vsc33586/user.sh, size=67, create_time=2020-04-17 12:25:57
    /kuleuven_tier1_pilot/home/vsc33586/UserCreationScript_Bash_IRODS.txt, size=274, create_time=2020-05-15 14:15:34
    /kuleuven_tier1_pilot/home/vsc33586/dataExample/test1-restore.txt, size=35, create_time=2020-05-14 07:41:30
    /kuleuven_tier1_pilot/home/vsc33586/dataExample/test1.txt, size=26, create_time=2020-05-11 08:26:23
    /kuleuven_tier1_pilot/home/vsc33586/data_test/test2.txt, size=59, create_time=2020-06-29 08:58:51
    /kuleuven_tier1_pilot/home/vsc33586/KULeuven/alice1.txt, size=74703, create_time=2020-04-27 14:09:31

It's also possible to search for specific data records based on the general metadata query by filtering with AVU info.

::

    from irods.column import Criterion
    from irods.models import DataObject, DataObjectMeta, Collection, CollectionMeta
    from irods.session import iRODSSession
    import os
    env_file = os.path.expanduser('~/.irods/irods_environment.json')
    with iRODSSession(irods_env_file=env_file) as session:
        results = session.query(Collection, CollectionMeta).filter( Criterion('like', CollectionMeta.value, '%chem%'))
        for r in results:
            print(r[Collection.name], r[CollectionMeta.name], r[CollectionMeta.value], r[CollectionMeta.units])

    /kuleuven_tier1_pilot/home/vsc33586/dataExample 'book' 'chemistry' 'KuLeuven'

We can query with aggregation(min, max, sum, avg, count) like the following example;

::

    with iRODSSession(irods_env_file=env_file) as session:
        query = session.query(DataObject.owner_zone).max(DataObject.size)
        print(next(query.get_results()))
    
    {<irods.column.Column 412 D_OWNER_ZONE>: 'kuleuven_tier1_pilot', <irods.column.Column 407 DATA_SIZE>: 18672491605}


Instantiating iRODS objects from query results
----------------------------------------------

In addition to the general query that gets information out of the ICAT, we can instantiate certain iRODS objects mirroring the persisted entities (instances of Collection, DataObject, User, or Resource, etc.) of the ICAT.

::

    user = session.users.get('vsc33586')
    print(user)

    <iRODSUser 11479 vsc33586 rodsuser kuleuven_tier1_pilot>

We can do the same with creation, removal and unlink.

The example below retrieves a reference to an existing collection using *get*.

::

    col = session.collections.get('/kuleuven_tier1_pilot/home/vsc33586/dataExample')
    print(col)

    <iRODSCollection 11482 b'vsc33586'>

So, how can we know what properties variable *col*, a reference to an iRODS Collection object, has?
The following code gives us some useful information.

::

    [ x for x in dir(col) if not x.startswith('__') ]

    ['_meta',
    'data_objects',
    'id',
    'manager',
    'metadata',
    'move',
    'name',
    'path',
    'remove',
    'subcollections',
    'unregister',
    'walk']

Let's check now the metadata of this instance. To see the result properly, we will use here the "pretty-print" module. 

::

    from pprint import pprint

    pprint((col.metadata.items()))

    [<iRODSMeta 195744 'type' 'collection' None>,
    <iRODSMeta 195747 'book' 'chemistry' 'KuLeuven'>]

We can see the sub-collections of a specific collection by using the walk method of this instance.

::

    col = session.collections.get('/kuleuven_tier1_pilot/home/vsc33586')

    for sub_coll in col.walk():
        pprint( sub_coll )

    < series of Python data structures giving the complete tree structure of *col* instance under collection 'vsc33586'>

If we wish to enumerate all collections in the iRODS catalog, we can use, as an alternative approach, general queries and the capabilities afforded by the PRC's object-relational mapping.

::

    from irods.collection import iRODSCollection
    from irods.models import Collection

    for result in session.query(Collection):
        print(iRODSCollection(session.collections,result))

    < all collections assigned to the user and their sub-collections in the iRODS catalog. >

If you would like to see more details and examples, you can have a look at the following link of original PRC documentation, `<https://github.com/irods/python-irodsclient>`_.

VSC Python iRODS Client (VSC-PRC)
---------------------------------

VSC-PRC's main goal is to make it easier for researchers to manage their data using iRODS, in particular on VSC's high performance computing infrastructure.

To this end, VSC-PRC offers a Python module and associated command line scripts:

* The ``vsc_irods`` Python module contains a ``VSCiRODSSession`` class
  which represents an extension of the corresponding ``iRODSSession`` class
  in PRC.

  A main feature is the possibility of using wildcards ("*") and tildes
  ("~") for specifying iRODS data objects and collections. For example,
  the following code will copy all files ending on '.txt' inside a
  'my_irods_collection' collection in your irods_home to the local working
  directory:

  ::

    with VSCiRODSSession() as session:
        session.bulk.get('~/my_irods_collection/*.txt', local_path='.')

  Other 'bulk' operations are available for:
  
  - uploading files and folders
  - removing data objects and collections
  - adding and modifying metadata
  - listing the disk usage

  More advanced search capabilities (i.e. beyond the above glob patterns)
  are also provided. For example, the following can be used to list all
  data objects in your irods_home ending on '.txt' and which possess a
  metadata entry with Attribute='Author' and Value='Me':

  ::

    with VSCiRODSSession() as session:
        for item in session.search.find('~', pattern='*.txt', types='f', object_avu=('Author', 'Me')):
            print(x)

  This can be used in conjunction with the 'bulk' operations, e.g.:

  ::

    with VSCiRODSSession() as session:
        iterator = session.search.find('~', pattern='*.txt', types='f', object_avu=('Author', 'Me'))
        session.bulk.get(iterator, local_path='.')


* VSC-PRC also comes with a set of scripts which make it easy to use the
  Python module from a Unix shell:

  - vsc-prc-find
  - vsc-prc-iget
  - vsc-prc-iput
  - vsc-prc-imkdir
  - vsc-prc-irm
  - vsc-prc-size
  - vsc-prc-imeta
  - vsc-prc-add-job-metadata

  Typing e.g. ``vsc-prc-find --help`` will show a description of the
  recognized arguments. The command-line equivalents of the three Python
  snippets above, for example, would look like this:

  ::

    vsc-prc-iget '~/my_irods_collection/*.txt' -d
    vsc-prc-find '~' -n '*.txt' --object_avu='Author;Me'
    vsc-prc-find '~' -n '*.txt' --object_avu='Author;Me' | xargs -i vsc-prc-iget {} -d

VSC-PRC is a complementary module created for supporting PRC operations on VSC.

In order to get a general overview of VSC-PRC, we recommend users to have a look at the “Introduction to VSC-PRC” tutorial at the following link, `<https://github.com/hpcleuven/vsc-python-irodsclient/blob/master/examples/introduction.ipynb>`_.

You can also find a HPC-specific example where the VSC-PRC is used in a jobscript at the following link, `<https://github.com/hpcleuven/vsc-python-irodsclient/blob/master/examples/jobscript_pbs.sh>`_.