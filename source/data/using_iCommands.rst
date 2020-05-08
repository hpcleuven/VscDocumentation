.. _using_iCommands:

Using iCommands
===============

iCommands is one of the client-side communication with iRODS server to provide users with data management and metadata management functions to do any required data-related actions. In other words ICommands is an Unix utilities that give users a command-line interface.
There are more than 50 iCommands. A regular user  however may use only a few of them for his/her daily needs. iRODS offers other user interfaces but the underlying point is that iCommands is the most powerful and easy-use interface to the data architecture.

All iCommands accept standard common line options (e.g., -a for all, -h for help) that gives more capabilities to the commands. To see a subset of these options and to know the details of any iCommands, you can follow the below specified options:

- You can visit `iCommands`_
- You can use the ``–h`` option with the command (e.g., ``iput –h``)
- You can use the ``ihelp`` command with the argument that you would like to learn more about (e.g., ``ihelp iput``).

Please keep in mind some iCommands don’t work with auto-complete of a tab press. Also remember that folders in iRODS are called as collection and you can run across object or data-object that represent a file in iRODS.

Now we can start working with iCommands based on a simple data management work flow that consists of “useful commands”, “working with directories (collections)”, “data upload and download” and “structuring data” .

Useful iRODS Commands
---------------------

These commands help us find and understand some information that we may need while implementing a data related task.

The most important command that will print out all commands will be::

$ ihelp

To know the settings details you can run::

$ ienv

To know about the detailed information about an user you can run the below command following with an user account.::

$ iuserinfo vscXXXXX

To be able to learn what an error code stand for, you can then use the command below with a code number.::

$ ierror 826000

If you want to log out from iRODS you can run ``iexit full`` , but be sure that you need to log on again by executing ``ssh irods.hpc.kuleuven.be | bash`` if you want to use iRODS again.

Working With Directories
------------------------

The iCommands that will be used in this part completely emulate standard Unix commands such as ``cd``, ``ls``, and ``pwd``.

To identify the current working collection use the ``ipwd`` command. The current working collection is the default location for data to be read or written. Basically this command tells you where you are in iRODS.::

$ ipwd
/kuleuven_tier1_pilot/home/vsc33586

To change the collection to the one yo want, you would use ``icd`` with an absolute path or a relative path. In other saying, navigate around to enter one of the (or the only) folder(s), do::

$ icd testCollection

To see the content of any collection(directory) use::

$ ils



.. include:: links.rst