.. _icommands:

#########
iCommands
#########


iCommands is a command-line interface for iRODS, the open-source
software behind Tier-1 Data. For those who are familiar with Unix command-line
programs, it is a powerful and easy to use tool.

************
Installation
************

iCommands are currently installed on **all HPC clusters of the VSC.**   

You can of course also install iCommands on your local system. 
However, iCommands is only available for Linux environments. 
To get one, Windows users might consider installing :ref:`Windows Subsystem for Linux (WSL)<wsl>`.

You can install iCommands on different distributions as follows:

Centos 7:
=========

.. code-block:: sh

   # Installing prerequisites
   yum update
   yum install wget sudo

   # Add the iRODS repository to your package manager (if you haven't done so already)
   sudo rpm --import https://packages.irods.org/irods-signing-key.asc
   wget -qO - https://packages.irods.org/renci-irods.yum.repo | sudo tee /etc/yum.repos.d/renci-irods.yum.repo

   # Installing iCommands  
   yum install irods-icommands

Almalinux 8/Rocky Linux 8:
==========================

.. code-block:: sh

   # Installing prerequisites
   yum update 
   yum install wget sudo

   # Add the iRODS repository to your package manager (if you haven't done so already)
   sudo rpm --import https://packages.irods.org/irods-signing-key.asc
   wget -qO - https://packages.irods.org/renci-irods.yum.repo | sudo tee /etc/yum.repos.d/renci-irods.yum.repo

   # irods runtime needs to be installed manually because of https://github.com/k3s-io/k3s/issues/5588
   yum install irods-runtime 

   # Installing iCommands  
   yum install irods-icommands

Debian 11:
==========

.. code-block:: sh

   # Installing prerequisites
   apt-get update
   apt-get install wget lsb-release sudo gnupg

   # Add the iRODS repository to your package manager (if you haven't done so already)
   wget -qO - https://packages.irods.org/irods-signing-key.asc | sudo apt-key add -
   echo "deb [arch=amd64] https://packages.irods.org/apt/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/renci-irods.list
   sudo apt-get update

   # Installing iCommands  
   apt-get install irods-icommands

Ubuntu 18/20:
=============

.. code-block:: sh

   # Installing prerequisites
   apt-get update
   apt-get install wget lsb-core sudo

   # Add the iRODS repository to your package manager (if you haven't done so already)
   wget -qO - https://packages.irods.org/irods-signing-key.asc | sudo apt-key add -
   echo "deb [arch=amd64] https://packages.irods.org/apt/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/renci-irods.list
   sudo apt-get update

   # Installing iCommands 
   apt-get install irods-icommands

Ubuntu 22:
==========

.. code-block:: sh

   # Installing prerequisites
   apt-get update
   apt-get install gnupg wget sudo
   wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
   sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb

   # Add the iRODS repository to your package manager (if you haven't done so already)
   wget -qO - https://packages.irods.org/irods-signing-key.asc | sudo apt-key add -
   echo "deb [arch=amd64] https://packages.irods.org/apt/ focal main" | sudo tee /etc/apt/sources.list.d/renci-irods.list
   sudo apt-get update

   # Installing iCommands 
   apt-get install irods-icommands




**************
Authenticating
**************

Since the Tier-1 Data service requires PAM interactive authentication, you can authenticate either using the standardized :ref:`iron<iron-CLI>` client or following the iCommands specific steps below.

- First, install the `irods-auth-plugin-pam-interactive-client` package:

.. code:: sh

   sudo apt update
   sudo apt install irods-auth-plugin-pam-interactive-client

- Go to the `ManGO portal <https://mango.vscentrum.be/>`__ and log in. Click on "How to connect" next to your zone, copy the code under "With iCommands only for Linux operating systems" and paste it into your terminal. 


- Click the authentication link displayed in your terminal and complete the steps on https://auth.vscentrum.be/.

Alternatively, you can use one of the following commands to log in from HPC nodes: 

- On HPC clusters of the KU Leuven, use the command ``irods-setup --zone <zone> | bash``.  
  This command can also be used at the beginning of your job script to authenticate.
  This is especially recommended for long running jobs, since if they spend a lot of time in the queue and a long time running, this may exceed the standard 7 day authentication.  

- On other HPC clusters in Flanders, you can log in with ``ssh login.hpc.kuleuven.be irods-setup --zone <zone> | bash``.  
  This command can currently not be included in job scripts, since it requires interaction from the user.  

For most users, the ``<zone>`` will be the default zone 'vsc'.

************
Getting help
************

iCommands has a built-in documentation, which you can access from the
command line. The command ``ihelp`` gives an overview of all commands,
with a brief description.

To get the documentation for a specific command, you can either type
``ihelp <command>`` or ``command -h``.

*******************************
Similarities with UNIX commands
*******************************

To people who are used to working on a Linux command line, iCommands
will instantly feel familiar. Many unix commands have a direct Unix
counterpart. While the Unix commands work on the local workspace, the
iCommands work on the data in Tier-1 Data.

+-------------------------------+-----------------------+-------------+
| Unix command                  | iCommand              | use         |
+===============================+=======================+=============+
| cd                            | icd                   | change      |
|                               |                       | current     |
|                               |                       | working     |
|                               |                       | directory   |
|                               |                       | /collection |
+-------------------------------+-----------------------+-------------+
| pwd                           | ipwd                  | show the    |
|                               |                       | current     |
|                               |                       | working     |
|                               |                       | directory   |
|                               |                       | /collection |
+-------------------------------+-----------------------+-------------+
| ls                            | ils                   | list the    |
|                               |                       | current     |
|                               |                       | working     |
|                               |                       | directory   |
|                               |                       | /collection |
+-------------------------------+-----------------------+-------------+
| mkdir                         | imkdir                | create      |
|                               |                       | directory   |
|                               |                       | /collection |
+-------------------------------+-----------------------+-------------+
| cp                            | icp                   | copy a      |
|                               |                       | file/data   |
|                               |                       | object or   |
|                               |                       | collectio   |
|                               |                       | n/directory |
+-------------------------------+-----------------------+-------------+
| mv                            | imv                   | move a      |
|                               |                       | file/data   |
|                               |                       | object or   |
|                               |                       | collectio   |
|                               |                       | n/directory |
+-------------------------------+-----------------------+-------------+
| chmod                         | ichmod                | changing    |
|                               |                       | permissions |
+-------------------------------+-----------------------+-------------+
| …                             | …                     | …           |
+-------------------------------+-----------------------+-------------+

Just like Unix commands, iCommands work with both absolute and relative
paths. For example, to go from ``/<zone>/home/<project>`` to
``/<zone>/home/<project>/raw_data`` you can use both of the following
options:

.. code-block:: sh

   icd raw_data

   icd /<zone>/home/<project>/raw_data

Like with Unix commands, you can use ``.`` to refer to the current
working collection, and ``..`` to refer to one level above the current
collection.

An important difference is that iCommands have no shell expansion. If
you try to use autocompletion with iCommands, or use wildcards (*), it
will be filled in based on the data in your local directory. This can
yield unexpected results.

*************************
Uploading and downloading
*************************

To upload data from your local directory to Tier-1 Data, you can use the
command ``iput``. You can upload individual files but also whole
directories, by using the ``-r`` option, which stands for ‘recursive’.

.. code-block:: sh

   iput <filename>
   iput -r  <directory>

You can optionally specify a destination as second argument. If you
leave the destination blank, iput will take the current working
collection as destination by default.

To download data objects or whole collections from Tier-1 Data to your local
directory, you can use the command ``iget``:

.. code-block:: sh

   iget <data_object>
   iget -r <collection>

``iget`` downloads data to your current working directory, unless you
specify another destination as second argument.

It is also possible with iCommands to sync a local directory and a
collection in Tier-1 Data with the command ``irsync``. This command makes a
comparison between the data on both sides. Any data from the source
which is missing in the destination, is transferred. If files are
present in both the source and destination, ``irsync`` will calculate
checksums to see whether the version in the destination is still up to
date.

.. code-block:: sh

   # syncronizing data from a local directory to a Tier-1 Data collection
   irsync -r <directory> i:<collection>

   # syncronizing data from a Tier-1 Data collection to a local directory
   irsync -r i:<collection> <directory>

***********
Permissions
***********

The command ``ichmod`` can be used to give groups or users :ref:`permissions and inheritance<collaboration>` on objects.

You can give a group or user access on an object as follows:

.. code-block:: sh

   ichmod <read/write/own> <group/user> <object_path>

You can remove the access of a group or user on an object by giving them 'null' access:

.. code-block:: sh

   ichmod null <group/user> <object_path>

When giving or removing access to a collection, you can use the ``-r`` flag to apply the permissions recursively.
That way, they are applied to all contents of the collection:

.. code-block:: sh

   ichmod -r <read/write/own> <group/user> <collection_path>

The command can be used to change the inheritance property of a collection as follows:

.. code-block:: sh

   # changing inheritance for one collection
   ichmod <inherit/noinherit> <collection_path>

   # changing inheritance recursively
   ichmod -r <inherit/noinherit> <collection_path>

********
Metadata
********

The command ``imeta`` can be used to add, list, manipulate and remove :ref:`metadata<metadata>` on data objects and collections.

You can add any AVU to a data object as follows:

.. code-block:: sh

   imeta add -d <filename> <attribute> <value> <units>

As always, the units are optional.

The flag '-d' is necessary, and indicates the operation is applied to a data object.
For collections, the flag needed is '-C'.

The following command can also be used to add a new AVU to an object.
The difference with ``imeta add`` is that it will overwrite if there is an AVU with the same attribute but a different value (and units).

.. code-block:: sh

   imeta set -d <filename> <attribute> <value> <units>

You can list the metadata on an object as follows:

.. code-block:: sh

   imeta ls -d <filename>

Lastly, you can remove a specific AVU as follows:

.. code-block:: sh

   imeta rm -d <filename> <attribute> <value> <units>

imeta also has other options, which you can discover by using ``imeta -h``.

