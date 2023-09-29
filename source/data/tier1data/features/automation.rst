###################
Workflow automation
###################

************************
Why workflow automation?
************************

Research data management covers a lot of tasks, some of which are
repetitive. For example, a workflow might include pre-processing of
files, adding certain metadata, or emptying a certain directory
regularly.

Automating repetitive tasks that are usually done manually, has two
goals. First of all, it can save users a lot of time. Secondly, it
eliminates human error. When a user needs to apply the same action to a
lot of files, mistakes are bound to happen.

By using scripts, we can automate a lot of these processes, keeping our
hands free for other tasks.

*************************
How to automate workflows
*************************


Client-side automation
======================

Users can automate workflows themselves on the client-side. 
We have two clients which can be integrated easily into your HPC workflow:

* :ref:`iCommands<icommands>` are bash commands and can thus be integrated into your job scripts
* Users who use Python in their HPC jobs can integrate the :ref:`Python client<python-client>` in their script

This way, you can easily retrieve data to be used in calculations, store results, add metadata and do other tasks automatically when you submit a job.

Of course, these clients can also be used outside of the HPC environment.



Machine accounts
----------------

By default, authentication to Tier-1 Data is limited to 60 hours (via the Python client) or 168 hours (via iCommands).
However, some automated processes require longer authentication.

For these cases, we created machine accounts: these are accounts that authenticate with a token, which lasts for 4 years.
To activate these machine accounts, go to the page of your project on the `ManGO portal <https://mango.vscentrum.be/>`_, 
either by clicking on the downwards arrow next to your zone name and select your project, 
or by surfing to https://mango.vscentrum.be/data-platform/project/<your_project>.

At the bottom of the page, you can activate two machine accounts for your project:

- <project_name>_ingress is meant for writing operations. By default, it has write access on the top collection of your project.
- <project_name>_egress is meant for reading operations. By default, it has read access on the top collection of your project.

Click on 'retrieve API token' to get the token for one of the machine accounts.
The following page contains the token, as well as instructions to authenticate with it.
Be sure to store the token information safely, for example in a password manager.

If you ever lose the token, or think it was compromised, you can generate a new token by clicking on 'Retrieve API token' again.
This will also immediately invalidate the previous token. 

Server-side automation
======================

Client-side automation suits workflows when tasks can be triggered deliberately, or at specific times.
However, some workflow have tasks that should be executed when specific events happen: for example, every time a file is uploaded, every time metadata is added, every time a user downloads a file, ...
In these cases, server-side automation can prove a solution. 

iRODS, the software behind Tier-1 Data, has a rule engine which can execute processes based on events happening in the system.
Every event, from a file being uploaded to users logging in, is defined as a Policy Enforcement Point (PEP).  
Administrators from the RDM team can add code to these PEPs. 

If you have a workflow which you think requires server-side automation, send your request to data@vscentrum.be.
From there, we can discuss how to automate the proposed workflow.

Whether a proposal is accepted will depend on:  

- Complexity  
- Feasability  
- Potential to be generalized for use in other groups


