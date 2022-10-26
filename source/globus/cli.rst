.. _cli:

============================
Command Line Interface (CLI)
============================

The Globus CLI allows you to manage and transfer data from the command line.
It is available for Windows, Mac and Linux (examples below taken from Linux).


Getting started with the CLI
----------------------------

The Globus CLI can be installed as a python package.
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

      $ Globus endpoint search 'VSC KU Leuven tier2 scratch'
      ID                                   | Owner                                                        | Display Name
      ------------------------------------ | ------------------------------------------------------------ | ---------------------------
      872a58ab-02b9-4233-a3e0-f017ed8ab090 | 91aed976-e7a6-4ae9-9e95-fda50e6cab01@clients.auth.globus.org | VSC KU Leuven tier2 scratch

You can find the names of all VSC collections in our table of :ref:`globus-available-collections`.

Since these ID's are long and not very readable, it is convenient to store these as a variable::

      $ tier2scratch=872a58ab-02b9-4233-a3e0-f017ed8ab090

      # Let's also make a variable for VSC KU Leuven tier1 scratch
      $ tier1scratch=903bb22d-45ef-41e2-9627-c925822e463f

You can list the contents of a collection with 'globus ls', followed by the collection id.
You can specify a directory path on the collection after a colon::

      # To list a collection from the root: 
      $ globus ls $tier2scratch        
            nproject/
            nscratch/
            project/
            scratch/                                                            
      
      # To list a specific directory:
      $ globus ls $tier2scratch:scratch/337/vsc33731/test
            statistics/
            survey_user1.csv
            survey_user2.csv
            survey_user3.csv

The first time you access a particular collection from the CLI, the CLI will ask for consent to manage your data in that collection.
It will ask you to run 'globus session consent [...]' and go to the provided url.
The consent is added to your session (so it's tied to one PC) and lasts until you use the 'globus logout' command. 

You can transfer a file between two endpoints as follows::

      $ globus transfer $tier2scratch:scratch/337/vsc33731/test/survey_user1.csv \
               $tier1scratch:337/vsc33731/test/survey_user1.csv --label "test_transfer"

      Message: The transfer has been accepted and a task has been created and queued for execution
      Task ID: 4dff3446-5512-11ed-ba54-d5fb255a47cc


For more documentation and examples about the globus CLI, see the official `Globus CLI documentation`_.


Scheduling transfers with Globus-Timer-CLI
------------------------------------------

Transfers can also be scheduled to happen in the future (instead of being
executed immediately as in the example above) and to be repeated on a regular
basis. These services are enabled by the Globus Timer API. The corresponding
CLI tools can be installed in your Python (virtual) environment using Pip
(`Globus-Timer-CLI on PyPi`_).

The above example can then be made to start at a certain point in the future 
and to be repeated every 7 days::

      $ globus-timer job transfer \
                     --name test_transfer_weekly \
                     --label "test_transfer_weekly" \
                     --interval 604800 \
                     --start '2021-06-02T11:00:00' \
                     --source-endpoint $endpoint_src \
                     --dest-endpoint $endpoint_dest \
                     --item $VSC_SCRATCH/testfile.tgz $VSC_SCRATCH/testfile.tgz false
      Name:            test_transfer
      Job ID:          6aa3ca88-8ae4-442d-99da-c5a89821c299
      Status:          new
      Start:           2021-06-02T09:00:00+00:00
      Interval:        7 days, 0:00:00
      Next Run At:     2021-06-09T09:00:00+00:00
      Last Run Result: NOT RUN

For more information on the available transfer options and monitoring tools,
please consult `Globus-Timer-CLI on PyPi`_.

.. warning::

      Times in the globus-timer outputs are always in UTC time,
      not in our local (CEST) time.

.. include:: links.rst



.. todo:
      - Why can you see old endpoints? 

     
