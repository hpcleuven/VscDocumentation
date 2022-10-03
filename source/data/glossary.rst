.. _glossary:

Glossary of iRODS
=================

**API**

An Application Programming Interface (API) is a computing interface to enable other software to communicate with it. Basically, an API specifies how software components should interact. iRODS defines a client API and expects that clients connect and communicate with iRODS servers in this controlled manner. iRODS has an API written in C, and another written in Java (Jargon). Other languages have wrappers around the C API (Python, PHP, etc.).

**AVU**

Attribute-Value-Unit (AVU) triples are associated with Collections or Data Objects and are the building blocks of metadata.

**Client**

A client in the iRODS client-server architecture gives users an interface to interact with iRODS to manipulate iRODS objects based on users' account profile and access level. iRODS clients include: WebDAV clients, web interfaces, iCommands, Python API etc. The programming clients are more fully fledged and also allow users to automate some repetitive works.

**Collection**

A Collection is the logical representation of physical containers, similar to directories or folders that are found in a file system. A Collection can have sub-collections, and hence provides a hierarchical structure. 

**Grid**

The hardware, operating system, and other machinery that support a Zone.

**Data Object**

A Data Object is a data file that is stored in iRODS. It is given a unique internal identifier in iRODS (allowing a global name space), and is associated with (situated in) a single Collection.

**iCAT**

The iCAT, or iRODS Metadata Catalog, is a database (e.g. PostgreSQL, MySQL, Oracle) that stores references to and between the iRODS entities in an iRODS Zone: Data Objects, Collections, Users and Groups. It also stores information such as system metadata, the mapping between logical and physical storage locations and user-defined metadata (AVUs). There is one iCAT per iRODS Zone.

**iCommands**

iCommands are Unix utilities that give users a command-line interface to operate on data in the iRODS system. iCommands provide the most comprehensive set of client-side standard iRODS manipulation functions.

**Inheritance**

Collections have an attribute named Inheritance. When a Collection has this attribute set to Enabled, new Data Objects and Collections added to this Collection inherit the access permissions (ACLs) of the Collection.

**Logical Name**

This a virtual identifier used by iRODS to uniquely name a Data Object, Collection, Resource, or User. 

**Metadata**

Metadata is data about data. Metadata can include system or user-defined attributes associated with a Data Object, Collection or Resource stored in the iCAT database. The metadata is in the form of AVUs (attribute-value-unit tuples). 

**Microservice**

Microservices are small, well-defined procedures/functions that perform a certain server-side task and are either compiled into the iRODS server code or packaged independently as shared objects. Rules invoke Microservices to implement data management policies.

**Policy Enforcement Point (PEP)** 

An event trigger in iRODS is called a PEP (Policy Enforcement Point) and it invokes an interpreted rule script via the rule engine configured in iRODS' server for the purpose of influencing a data management operation.

**Replica**

An identical, physical copy of a Data Object on another storage server.

**Resources**

A resource, or storage resource, is a software/hardware system that stores digital data. iRODS clients can operate on local or remote data stored on different types of resources through a common interface.

**Rules**

Rules are definitions of actions that are to be performed by the server. These actions are defined in multiple ways, depending on the language that is used to define the actions. The native language in iRODS is the iRODS Rule Language that defines actions with microservices and other actions.

**Rule Engine**

The Rule Engine interprets Rules written in one of the supported rule engine plugin languages. 

**Server**

An iRODS server is software that interacts with the access protocol of a specific storage system. It enables storing and sharing data distributed geographically and across administrative domains.

**Vault**

The physical location of Data Objects on a storage device. 

**Workflow** 

Some form of computation or action performed on Data Objects, with a specific start and end point.

**Zone**

An iRODS deployment is called a Zone.