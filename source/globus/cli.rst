.. _cli:

Command Line Interface (CLI)
----------------------------

In addition to the web interface, also a set of Globus CLI tools are available.
These are useful for automating your transfer processes, including the
scheduling of recurrent transfers.


Getting started with the CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Globus CLI documentation`_. contains an adequate introduction to the CLI.
The following only includes VSC-specific examples and tips.

The latest release can be locally installed in e.g. a Python Virtual
Environment as follows::

      $ /usr/bin/python3 -m venv venv_globus
      $ source ./venv_globus/bin/activate
      $ pip install globus-cli

One of the dependencies is currently `incompatible with Python3's ASCII encoding
<https://click.palletsprojects.com/en/7.x/python3/>`_, requiring a change in the
locale settings::

      $ export LC_ALL=en_US.utf-8 && export LANG=en_US.utf-8

You can now authenticate by executing::

      $ globus login

and logging in via the generated URL, which will provide an access token.
The available VSC endpoints can be then listed as follows::

      $ globus endpoint search "VSC Tier"
      ID                                   | Owner                         | Display Name
      ------------------------------------ | ----------------------------- | --------------------
      4f9698ae-5644-11eb-a45c-0e095b4c2e55 | linuxicts@globusid.org        | VSC KU Leuven Tier1
      2e1e56a4-3faa-11eb-b185-0ee0d5d9299f | linuxicts@globusid.org        | VSC KU Leuven Tier2
      ff4d98be-5c46-11e9-a623-0a54e005f950 | hpcuantwerpen@globusid.org    | VSC UAntwerpen Tier2
      bc2900d0-516c-11e9-bf30-0edbf3a4e7ee | hpcugent@globusid.org         | VSC UGent Tier2
      c62f6838-88f5-11e9-b807-0a37f382de32 | wapoelma@vub.ac.be            | VSC VUB Tier2

To transfer a file from e.g. the KU Leuven Tier2 scratch to the Tier1 scratch::

      $ endpoint_src=2e1e56a4-3faa-11eb-b185-0ee0d5d9299f
      $ endpoint_dest=4f9698ae-5644-11eb-a45c-0e095b4c2e55
      $ globus transfer $endpoint_src:$VSC_SCRATCH/testfile.tgz \
               $endpoint_dest:$VSC_SCRATCH/testfile.tgz --label "test_transfer"
      Message: The transfer has been accepted and a task has been created and queued for execution
      Task ID: 335cffea-9ef7-42dc-aac2-11cc312c3e51

Many more examples can be found in the `Globus CLI documentation`_.


Scheduling transfers with Globus-Timer-CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
