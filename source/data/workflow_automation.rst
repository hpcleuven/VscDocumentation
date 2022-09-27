.. _workflow_automation.rst:

Workflow automation
===================

iRODS provides a Rule System to automate data management tasks. Each organisation or project has its own policies and needs with regards to file housekeeping and metadata extraction. Examples of file operations are making regular backups, checking file integrity, cleaning up permissions, emptying the trash,... Metadata can be extracted from data files or accompanying text files to be stored to the iCAT catalog. This frees human users of having to apply repetitive actions, and ensures policies are applied consistently and without error.

This is made possible by the Rule Engine Plugin Framework (REPF), which executes the rules and keeps track of the execution state of all active rules (as rules can be immediate, have a delay or a condition). The framework keeps track of both User-level rules and System-level rules. 

User-level rules are stored locally and manually invoked by any user using the ``irule`` command, which runs it in the iRODS server. They are meant for personal or group use (if the user is part of that group) and are typically simple 'one-shot' workflow operations. System-defined rules are stored server-side by an iRODS developer or administrator and automatically invoked by the Rule Engine when a certain condition is met. This condition is called an 'event' or more formally a Policy Enforcement Point (PEP). They are meant for consistent data management of a whole zone or for complex group/project data management tasks.

Rules can be invoked in three ways: by directly calling the ``irule`` command on a rule file (only for User-level rules); by reaching a Policy Enforcement Point, triggering a System-level rule; or periodically via delayed execution (both for User-level and System-level rules). The delay mechanism is used for resource-heavy, time-intensive processes that can occur one or more times in the future at regular intervals.

The Python iRODS Client (PRC) is executed client-side, making it somewhat less efficient than iRODS rule execution. Although both offer overlapping functionality, the delay mechanism used by iRODS rules is more graceful and these rules get stored centrally in the REPF. It is also possible to invoke a rule via the PRC.

This article focuses only on User-level rules. If you have more complex data processing pipelines, the Tier-1 Data Team (FOZ-RDM) at KU Leuven can create System-level rules for you.

Rule syntax
-----------

User-level rules can only be written in the iRODS Rule language, System-level rules can also be written in other languages (Python, C++ or JavaScript). The iRODS Rule language is a domain specific scripting language composed of simple building blocks. It uses curly brackets, # for comments, variable names start with '*' and strings are enclosed by ' or ". The documentation for the language can be found here: https://docs.irods.org/4.2.10/plugins/irods_rule_language/.

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

As said, we can chain rules like this:

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


We can also prompt the user for input by assigning a variable to '$', with an optional default value. The ``greeting1`` variable can be either set to what the user types or kept at its default value 'Hello' by hitting enter. When typing your prompted value, it should be enclosed with single or double quotes! Also note that (session) variables are expanded in quoted strings.

::

    evenMoreAdvancedHelloWorldRule{
        writeLine("stdout","User says '*greeting1 *greeting2'")
    }
    input *greeting1 = $'Hello', *greeting2 = $'World'
    output ruleExecOut


There are also session state variable, for instance to retrieve the active user:

::

    evenMoreAdvancedHelloWorldRule{
        writeLine("stdout","$userNameClient says '*greeting1 *greeting2'")
    }
    input *greeting1 = $'Hello', *greeting2 = $'World'
    output ruleExecOut


Another useful session state variable for User-level rules is ``$rodsZoneClient`` for the zone name. There are other session variables (like ``$collName``, ``$objPath``, ``$dataType``, ``$dataSize``, ``$chksum``,...) but these are only useful for System-level rules.

Querying iRODS
--------------

Just like in the iquest iCommand and with the PRC we can query iCAT and retrieve matching fields for entities (data objects or collections). These fields are called 'Persistent State Information'. Rules can also access 'Session state information', such as the $userNameClient variable above. To see which persistent fields are available, use ``iquest attrs``.

The following rule prints all data objects whose logical path contain the word 'test'. Note that COLL_NAME is the whole path with the collection name at the end:

::
    
    queryRule{
        foreach(*i in SELECT COLL_NAME, DATA_NAME WHERE COLL_NAME like '%test%'){
            *coll = *i.COLL_NAME;
            *data = *i.DATA_NAME;
            writeLine("stdout", "*coll/*data");
        }
        writeLine("stdout", "listing done");
    }

Microservices and Custom functions
---------------------------

iRODS already provides a whole library of functions to interact with it via the Rule system, called microservices. 
Microservices are written in C within the iRODS sourcecode.

You can find an overview of all available microservices in the  `iRODS documentation <https://docs.irods.org/4.2.8/>`__ under the tab `Doxygen <https://docs.irods.org/4.2.8/doxygen/>`__. These pages also contain the function arguments and types.

There are microservices for rule management, manipulating data objects, collections and their metadata, managing the iCAT database,... It also includes basic functions like email, string and key-value manipulation.

::

    myTestRule{
        delay("<PLUSET>1m</PLUSET>"){
            writeLine("stdout",”Writing message with a delay.");
            msiSendStdoutAsEmail(*Mailto, "Sending email");
        }
    }

In your rulefile, you can define functions to contain oft-used functionality. These can be written as inline functions or within a function block. Functions can be thought of as microservices written in the rule language.