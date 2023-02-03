.. _cli:

============================
Command Line Interface (CLI)
============================

The Globus CLI allows you to manage and transfer data from the command line.
It is available for Windows, Mac and Linux (examples below taken from Linux).


Getting started with the CLI
----------------------------

Currently, a version of the Globus CLI is already available on the Tier-2 Cluster of the VUB (Hydra) and can be loaded as follows::

      module load Globus-CLI

In other environments, the Globus CLI can be installed as a python package.
You can install this in a Python Virtual Environment as follows::

      $ /usr/bin/python3 -m venv venv_globus
      $ source ./venv_globus/bin/activate
      $ pip install globus-cli

You can now authenticate by executing::

      $ globus login

This should generate a url, which you should paste into your browser. 
If you had no running session, you will be asked to log in to Globus.

Paste the token you get on this site in your terminal, and you are logged in to the globus CLI!

You can confirm this by listing your globus ID's as follows::

      $ globus whoami


Transferring data
---------------------

In Globus, every collection has an ID. In the Globus CLI, you need this ID to list or transfer data from/to a collection.

You can look up the ID's of collections and endpoints with the command 'globus endpoint search'::

      $ globus endpoint search 'VSC KU Leuven tier2 scratch'
      ID                                   | Owner                                                        | Display Name
      ------------------------------------ | ------------------------------------------------------------ | ---------------------------
      872a58ab-02b9-4233-a3e0-f017ed8ab090 | 91aed976-e7a6-4ae9-9e95-fda50e6cab01@clients.auth.globus.org | VSC KU Leuven tier2 scratch

You can find the names of all VSC collections in our table of :ref:`globus-available-collections`.

.. warning::
    We recommend to search based on the names in the tables referenced above.  
    Globus endpoint search shows both endpoints and collections matching your query.  
    While collections are directly accessible, endpoints are not, and this might cause confusion.  

You can list the contents of a collection with 'globus ls', followed by the collection id.
You can specify a directory path on the collection after a colon::

      # Making a variable for the collection ID for convenience
      $ kuleuventier2scratch=872a58ab-02b9-4233-a3e0-f017ed8ab090

      # To list a collection from the root: 
      $ globus ls $kuleuventier2scratch        
            nproject/
            nscratch/
            project/
            scratch/                                                            
      
      # To list a specific directory:
      # (In this snippet, a real VSC account is replaced with 'vscxxxxx')
      $ globus ls $kuleuventier2scratch:scratch/xxx/vscxxxxx/test
            statistics/
            survey_user1.csv
            survey_user2.csv
            survey_user3.csv

The first time you access a particular collection from the CLI, the CLI will ask for consent to manage your data in that collection.
It will ask you to run 'globus session consent [...]' and go to the provided url.
The consent is added to your session (so it's tied to one PC) and lasts until you use the 'globus logout' command. 

You can transfer a file between two endpoints as follows::

      # Also saving the destination endpoint in a variable for convenience
      vubtier2=2d1d4873-a849-4b9c-bd34-2034a2163003

      $ globus transfer $kuleuventier2scratch:path/to/data/on/kuleuven/tier2 \
               $vubtier2:path/to/data/on/VUB/tier2 --label "test_transfer"

      Message: The transfer has been accepted and a task has been created and queued for execution
      Task ID: 4dff3446-5512-11ed-ba54-d5fb255a47cc


For more documentation and examples about the globus CLI, see the official `Globus CLI documentation`_.


.. include:: links.rst


     
