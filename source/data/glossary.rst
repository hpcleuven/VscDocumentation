.. _glossary:

Glossary of iRODS
=================

**API**

An Application Programming Interface (API) is a computing interfaces to enable other software to communicate with it. Basically, an API specifies how software components should interact.  iRODS defines a client API and expects that clients connect and communicate with iRODS servers in this controlled manner. iRODS has an API written in C, and another written in Java (Jargon). Other languages have wrappers around the C API (Python, PHP, etc.).

**Client**

A Client in the iRODS client-server architecture gives users an interface to manipulate Data Objects. iRODS clients include: iCommands, web interfaces, Python API etc.

**Collection**

A Collection is the logical representation of physical containers, similar to directories or folders that are found in a file system. A Collection can have sub-collections, and hence provides a hierarchical structure. 

**Grid**

Grid The hardware, operating system, and other machinery that support a Zone.

**Data Object**

A Data Object is a data file that is stored in iRODS. It is given a unique internal identifier in iRODS (allowing a global name space), and is associated with (situated in) a Collection.

**iCAT**

The iCAT, or iRODS Metadata Catalog, is a database (e.g. PostgreSQL, MySQL, Oracle) that stores metadata about the Data Objects, Collections, Users, and Groups in an iRODS Zone. There is one iCAT per iRODS Zone.

**iCommands**

iCommands are Unix utilities that give users a command-line interface to operate on data in the iRODS system. iCommands provide the most comprehensive set of client-side standard iRODS manipulation functions.

**Inheritance**

Collections have an attribute named Inheritance. When a Collection has this attribute set to Enabled, new Data Objects and Collections added to this Collection inherit the access permissions (ACLs) of the Collection.

**Logical Name**

This a virtual identifier used by iRODS to uniquely name a Data Object, Collection, Resource, or User. 

**Metadata**

Metadata is data about data. Metadata can include system or user-defined attributes associated with a Data-Object, Collection or Resource stored in the iCAT database. The metadata is in the form of AVUs (attribute-value-unit tuples). 

**Microservice**

Microservices are small, well-defined procedures/functions that perform a certain server-side task and are either compiled into the iRODS server code or packaged independently as shared objects. Rules invoke Microservices to implement data management policies.

**Policy Enforcement Point (PEP)** 

A event trigger in iRODS called PEP and it invokes an interpreted rule script via the iRODS rule engine for the purpose of influencing a data management operation.

**Replica**

An identical, physical copy of a Data Object.

**Resources**

A resource, or storage resource, is a software/hardware system that stores digital data. iRODS clients can operate on local or remote data stored on different types of resources through a common interface.

**Rules**

Rules are definitions of actions that are to be performed by the server. These actions are defined in multiple ways, depending on the language that is used to define the actions. The native language in iRODS is  iRODS Rule Language that defines actions with microservices and other actions.

**Rule Engine**

The Rule Engine interprets Rules written in one of the supported rule engine plugin languages. 

**Server**

An iRODS server is software that interacts with the access protocol of a specific storage system. It enables storing and sharing data distributed geographically and across administrative domains.

**Vault**

The physical location of Data Objects on a storage device. 

**Workflow** 

Some form of computation or action performed on Data Objects.

**Zone**

An iRODS deployment is called as Zone.


