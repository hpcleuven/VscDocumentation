.. _workflow_automation.rst:

Workflow automation
===================

iRODS provides a Rule System to automate data management tasks. Each organisation or project has its own policies and needs with regards to file housekeeping and metadata extraction. Examples of file operations are making regular backups, checking file integrity, cleaning up permissions, emptying the trash,... Metadata can be extracted from data files or accompanying text files to be stored to the iCAT catalog. This frees human users of having to apply repetitive actions, and ensures policies are applied consistently and without error.

This is made possible by the Rule Engine Plugin Framework (REPF), which executes the rules and keeps track of the execution state of all active rules (as rules can be immediate, have a delay or a condition). The framework keeps track of both User-level rules and System-level rules. 

User-level rules are stored locally and manually invoked by any user using the ``irule`` command, which runs it in the iRODS server. They are meant for personal or group use (if the user is part of that group) and are typically simple 'one-shot' workflow operations. System-defined rules are stored server-side by an iRODS developer or administrator and automatically invoked by the Rule Engine when a certain condition is met. This condition is called an 'event' or more formally a Policy Enforcement Point (PEP). They are meant for consistent data management of a whole zone or for complex group/project data management tasks.

Rules can be invoked in three ways: by directly calling the ``irule`` command on a rule file (only for User-level rules); by reaching a Policy Enforcement Point, triggering a System-level rule; or periodically via Delay rules (both for User-level and System-level rules). Resource-heavy, time-intensive processes are best executed as a system-level delay rules.

The Python iRODS Client (PRC) is executed client-side, making it somewhat less efficient than iRODS rule execution. Although both offer overlapping functionality, the delay mechanism used by iRODS rules is more graceful and these rules get stored centrally in the REPF. It is also possible to invoke a rule via the PRC.

This article focuses only on User-level rules. If you have more complex data processing pipelines, the Tier-1 Data Team (FOZ-RDM) at KU Leuven can create System-level rules for you. Please contact us at data@vscentrum.be.

Rule syntax
-----------

Rules can be written in Python, C++ or the iRODS Rule language. However, normal users can (for the time being) only execute rules written in the iRODS Rule language (either User-level or System-level rules). The iRODS Rule language is a domain specific scripting language composed of simple building blocks. It uses curly brackets, # for comments, variable names start with '*' and strings are enclosed by ' or ". The documentation for the language can be found here: https://docs.irods.org/4.2.10/plugins/irods_rule_language/.

::

    rulename{             # rulename, like 'extractMetaDataRule', followed by the body block
        on(condition){    # condition is optional
            delay(delay){ # delay is optional
                list of actions
            }
        }                 # condition is optional
    }

    input INPUT           # input is optional
    output OUTPUT


A rulefile can contain more than one rulename blocks, although only the first one gets executed. The second one can get called by the first one in the list of actions and its output can be saved as a variable for the caller. Some of the elements are optional. A rule without condition or delay gets executed immediately, once. 'Input' variables are optional (or can be set to null) and can be used to store a global variable for all rules inside the rulefile or prompt for user input.

It is not illegal syntax to use a condition in a user-level rule, but the conditions can't be used to track system events similar to a what a PEP does. 

Executing rules
---------------

This rule prints 'Hello World' to the terminal:

::

    helloWorldRule{
        writeLine('stdout', 'Hello World!');
    }

    output ruleExecOut

 
``output ruleExecOut`` indicates that this rule is executable. Save this code in a file called myFirstRule.r and call it by issuing:

::

    $ irule -F myFirstRule.r

As said, we can call rules like this, just as if they would be functions:

::

    firstRule{
        writeLine('stdout', 'This is my first rule');
        secondRule()
    }

    secondRule{
        writeLine('stdout', 'This is my second rule');
    }

    output ruleExecOut

Variables and user input
------------------------

Variables can be assigned to in the body block or in an input variable. You can concatenate string variables with the '++' operator.

::

    advancedHelloWorldRule{
        #you can define a variable here
        *var1="Hello ";
        writeLine('stdout', *var1 ++ *var2);
    }

    #you can also define a variable here
    input *var2="World"
    output ruleExecOut


We can also prompt the user for input by assigning a variable to '$', with an optional default value. In the next example, the ``greeting1`` variable can be either set to what the user types or kept at its default value 'Hello' by hitting enter. When typing your prompted value, it should be enclosed with single or double quotes. Also note that variables are expanded in quoted strings.

::

    evenMoreAdvancedHelloWorldRule{
        writeLine("stdout","User says '*greeting1 *greeting2'")
    }
    input *greeting1 = $'Hello', *greeting2 = $'World'
    output ruleExecOut


There are also session state variables, for instance to retrieve the active user:

::

    veryAdvancedHelloWorldRule{
        writeLine("stdout","$userNameClient says '*greeting1 *greeting2'")
    }
    input *greeting1 = $'Hello', *greeting2 = $'World'
    output ruleExecOut


Another useful session state variable for User-level rules is ``$rodsZoneClient`` for the zone name. There are other session variables (like ``$collName``, ``$objPath``, ``$dataType``, ``$dataSize``, ``$chksum``,...) but these are only useful for System-level rules as they are out of scope in a User-level rule.

Querying iRODS
--------------

Just like in the iquest iCommand and with the PRC we can query iCAT and retrieve matching fields for entities (data objects or collections). These fields are called 'Persistent State Information'. Rules can also access 'Session state information', such as the ``$userNameClient`` variable above. To see which persistent fields are available, use ``iquest attrs``.

The following rule prints all data objects whose logical path contains the word 'test'. Note that COLL_NAME is the whole path with the collection name at the end:

::
    
    queryRule{
        foreach(*i in SELECT COLL_NAME, DATA_NAME WHERE COLL_NAME like '%test%'){
            *coll = *i.COLL_NAME;
            *data = *i.DATA_NAME;
            writeLine("stdout", "*coll/*data");
        }
        writeLine("stdout", "listing done");
    }

Microservices and custom functions
----------------------------------

iRODS already provides a whole library of functions to interact with it via the Rule system, called microservices. Microservices are written in C within the iRODS source code. These can be called in the rule body as any other action.

You can find an overview of all available microservices in the  `iRODS documentation <https://docs.irods.org/4.2.8/>`__ under the tab `Doxygen <https://docs.irods.org/4.2.8/doxygen/>`__. These pages also contain their function arguments and types.

There are microservices for rule management, manipulating data objects, collections and their metadata, managing the iCAT database,... It also includes basic functions like email (``msiSendStdoutAsEmail``), string and key-value manipulation. The following example creates a new collection:

::

    createCollRule {
            *path="/$rodsZoneClient/home/$userNameClient/newCollection";
            msiCollCreate(*path, 0, *Status);
            writeLine("stdout", "Collection *path created");

    } 
    output ruleExecOut

You can of course also save data objects from a local disk with the ``msiDataObjPut`` microservice. As an input variable you should use the absolute path of a file. The second argument for ``msiDataObjPut`` is the iRODS resource where you want to save the file. A resource, or storage resource, is a software/hardware system that stores digital data. You can identify the available resources with the ``ilsresc`` command.

::

    createDORule {
            *path="/$rodsZoneClient/home/$userNameClient/newCollection"
            *destName="test.txt"
            writeLine("stdout", "Saving file *path/*destName ...")
            msiDataObjPut("*path/*destName","default","localPath=*file++++forceFlag=",*Status)
            writeLine("stdout", "File *path/*file created")
    }

    input *file="/home/x/y/z/test.txt"
    output ruleExecOut


In your rulefile, you can define functions to contain oft-used functionality. Functions can be thought of as microservices written in the rule language and are called similarly. It's also possible to pass variables to a function, and let it return its result. 

::

    functionRule {
        *c = sq(5)
        writeLine('stdout',*c)
    }

    sq(*a){
            *b=*a * *a
            *b
    }

    input null
    output ruleExecOut


Delayed execution rules
-----------------------

A rule action can be executed (as a System-level rule or with ``irule``) at a certain point in the future by delaying it or scheduling it at a certain time. To express this, a timing syntax based on XML is provided:

 - ET: Absolute time when something should be performed, for instance at 8:00 PM: <ET>20:00</ET>.
 - PLUSET: Delay execution for a certain amount of time from now, for instance <PLUSET>10s</PLUSET> or <PLUSET>1m</PLUSET>.
 - EF: Perform execution every n time units, for a certain amount of time. The default is forever. For instance, <EF>1d</EF> for daily.

The full syntax is provided `here <https://docs.irods.org/4.2.10/plugins/pluggable_rule_engine/#examples>`__.

::

    backupRule{
            delay("<ET>00:00</ET><PLUSET>1d</PLUSET>"){
                msiTarFileCreate(*file,*coll,*resource,*flag);
                writeLine("stdout","Created tar file *file for collection *coll on resource *resc");
            }
    }
    input *file="/$rodsZoneClient/home/$userNameClient/backup_newCollection.tar", *coll="/$rodsZoneClient/home/$userNameClient/newCollection", *resource="default", *flag="force"
    output ruleExecOut

This backs up the provided collection daily at midnight. You can test this delay rule has been executed by replacing it with '<ET>00:00</ET><PLUSET>1m</PLUSET>' and calling ``ils -l`` to see the timestamp changing.

The following example syncs between 2 collections in 10 seconds from now and repeats it hourly, forever:

::

    syncRule{
        delay("<PLUSET>10s</PLUSET><EF>1h</EF>"){
                msiCollRsync(*srcColl,*destColl,*resource,"IRODS_TO_IRODS",*Status);
                writeLine("stdout","Synchronized collection *srcColl with collection *destColl");
        }
    }

    input *srcColl="/$rodsZoneClient/home/$userNameClient/newCollection", *destColl="/$rodsZoneClient/home/$userNameClient/newCollection_sync",*resource="default"
    output RuleExecOut

There are three useful iCommands to track the active delayed rules:

- ``iqstat``: show the queue status of delayed rules, and note the id
- ``iqmod``: modify certain values in existing delayed rules (owned by you)
- ``iqdel``: remove a delayed rule (owned by you) from the queue, by giving the id