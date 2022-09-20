.. _tier1_data_architecture:

Tier-1 Data Platform Architecture
=================================


The VSC Tier-1 Data component is based on the open source software iRODS. The following image shows the high level archirecture of the platform.

.. image:: architecture/general_overview.png

The current deployment is based in a unique iRODS zone (“kuleuven_tier1_pilot”) with a single iCAT database configured on High Availability. There are three distributed storage resources: 2 POSIX based systems and 1 Ceph Object Storage system). 
One of the POSIX systems and the Ceph based storage are physically installed at the KU Leuven Heverlee datacenter while the other POSIX system is installed at the KU Leuven datacenter located in Leuven center and act as a replica of the POSIX system located in Heverlee. 

That means that for every object registered in the Data platform 2 copies will be automatically stored (one in Heverlee and one Leuven). 

The third storage system will be used for the moment to store a third copy of some selected data objects. 

A user can access iRODS from a local computer and/or the VSC Tier-1 and Tier-2 systems using different types of user clients.  At this moment they are available:  iCommands, the YODA portal client , WebDAV clients and a Python Client.

iCommands is an utility that give users a command-line interface to operate on data in iRODS. 

The portal client-YODA is a user friendly web based application to provide researchers and their partners with a workspace and an archive that enables them to collaborate, deposit and preserve research data.

With the aid of WebDAV protocol, a Drag and Drop Access to iRODS is ensured by means of some apps/tools (e.g. WebDAV mapping, Cyberduck and WinSCP) that enable data transfer.

PRC is a Python Client API to establish a secure connection to iRODS and to be able to interoperate with iRODS from python programs.
