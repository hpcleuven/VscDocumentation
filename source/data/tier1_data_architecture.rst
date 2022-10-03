.. _tier1_data_architecture:

Tier-1 Data Platform Architecture
=================================


The VSC Tier-1 Data component is based on the open source software iRODS. The following image shows the high level archirecture of the platform.

.. image:: architecture/general_overview.png

The current deployment is based in a unique iRODS zone (“kuleuven_tier1_pilot”) with a single iCAT database configured on High Availability. There are three distributed storage resources: 2 POSIX based systems and 1 Ceph Object Storage system).

A user can access iRODS from a local computer and/or the VSC Tier-1 and Tier-2 systems using different types of user clients. At this moment there are available: programming clients such as iCommands and a Python client; web applications such as MetaLnx and (soon) the KU Leuven Data Portal; and various clients implementing WebDAV.

iCommands is an utility that gives users a command-line interface to operate on data in iRODS. PRC is a Python Client API to establish a secure connection to iRODS and to be able to interoperate with iRODS from python programs.

With the aid of the WebDAV protocol, Drag and Drop Access to iRODS is ensured by means of some apps/tools (e.g. WebDAV mapping, Cyberduck and WinSCP) that enable data transfer.
