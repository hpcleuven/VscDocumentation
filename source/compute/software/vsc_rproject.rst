.. _vsc-Rproject:

vsc-Rproject
============

Introduction
------------

vsc-Rproject is an in-house developed command-line tool that integrates the use of
RStudio Projects into our HPC environment. It facilitates the creation, management
and use of the RStudio Project and its associates vsc-Rproject environment.

.. note::

   In what follows, the term "vsc-Rproject environment" refers to the environment
   created by vsc-Rproject which enables the use of the associated RStudio Project
   on our HPC system.

How to use
----------

vsc-Rproject can be used by simply loading the module.

.. code:: bash

   $ module load vsc-Rproject


Then, use the ``vsc-rproject`` command to use its different functionalities.

.. code:: bash

   $ vsc-rproject --help
   $ vsc-rproject --version

The ``vsc-rproject`` command provides four sub-commands that can be used to ``configure`` default behaviour
or ``create``, ``activate``, or ``deactivate`` a vsc-Rproject environment.

.. _creating_a_project:

Creating a project
~~~~~~~~~~~~~~~~~~

The ``create`` sub-command allows you to create a new RStudio Project alongside its vsc-Rproject environment.

When creating a new project, the only required argument is a project name.

It is however strongly encouraged to also provide a "modules file".
This is a simple text file listing one module (full name and version) per line.
When providing a modules file, vsc-Rproject will ensure that these modules
are always loaded upon activating the vsc-Rproject environment.
If no modules file is provided, the default R module will be used instead.

The following command will create a modules.txt file in your home directory,
containing the following modules:

- ``R/4.4.1-gfbf-2023b``
- ``R-bundle-CRAN/2024.06-foss-2023b``

.. code:: bash

   $ printf "R/4.4.1-gfbf-2023b\nR-bundle-CRAN/2024.06-foss-2023b\n" > ~/modules.txt


.. note::

   When you specify a modules file, it should always contain the R module.

To create a new RStudio Project and vsc-Rproject environment using this modules file, run the following command:

.. code:: bash

   $ vsc-rproject create MyProject --modules="$VSC_HOME/modules.txt"

This will create a new RStudio Project named "MyProject" at the default location: ``$VSC_DATA/Rprojects``.
The modules.txt file will be used when creating the project and stored in ``$VSC_DATA/Rprojects/.vsc-rproject/modules.env``.

.. note::

   If you wish to update the modules list for an existing project, you should manually
   add it to the `.vsc-rproject/modules.env` file.


Within this project folder, a project specific ``.Renviron``, ``.Rprofile`` and ``.R/Makevars`` file will be created.

The ``.Renviron`` will set the ``R_LIBS_USER`` variable to point to the project's R package library.
This can be found at the root of the project, under ``/library/<OS>/R``.

The ``.Rprofile`` will be configured to set the CRAN mirror to ``"https://cloud.r-project.org"`` (default)
and set the ``R_MAKEVARS_USER`` variable to point to the project's ``.R/Makevars`` file.

The ``.R/Makevars`` file can be used to control the compilation process when installing
new R packages by modifying the compiler flags. vsc-Rproject's default behaviour
is to change the ``-march`` compiler flag for all relevant compilers from "native"
to "x86-64-v4".

.. note::

   While compiling with "-march=native" will result in better performance for a single
   type of CPU microarchitecture, the "-march=x86-64-v4" setting marginally compromises
   performance, to allow for a more generic installation compatible with microarchitectures
   from skylake or more recent. For most users this will be the more desirable option
   as it makes switching between different types of compute nodes a lot easier.

.. warning::

   The ``-march=x86-64-v4`` flag is used as the default for microarchitecture optimization
   targeting Intel Skylake and newer processors. However, this flag is only supported
   in GCC version 11 and later. If you are using an older version of R that relies
   on an earlier GCC version, ``-march=x86-64-v4`` may not be recognized.
   In such cases, you can run ``gcc --target-help`` to view the list of supported
   ``-march`` values and choose a more appropriate setting.


If you want to enable git within the RStudio Project you can add the ``--enable-git`` flag.
To automatically activate the vsc-Rproject environment after creating it, use ``--activate``.

If you are not satisfied with the default behaviour, you can modify the behaviour
of ``vsc-rproject create`` by providing additional command-line arguments.
You can specify ``--location`` to create your project in a different location.
The ``--cran`` argument can be used to provide a specific CRAN mirror for your project.
Finally ``--march`` allows you to choose a different the microarchitecture optimization
for your project.


For more information, see:

.. code:: bash

   $ vsc-rproject create --help


.. note::

   Alternatively, you may also want to  modify your default settings more permanently via `vsc-rproject configure`.
   See :ref:`Default project configuration <default_project_configuration>` for more details.

.. _activating_a_project:

Activating a project
~~~~~~~~~~~~~~~~~~~~

The ``activate`` sub-command can be used to activate an already existing vsc-Rproject environment.

.. code:: bash

   $ vsc-rproject activate MyProject

Activating a vsc-Rproject environment will load all the relevant modules listed in the modules file and
set the ``$VSC_RPROJECT`` environment variable which can be used to access the root directory of the project.

.. _deactivating_a_project:

Deactivating a project
~~~~~~~~~~~~~~~~~~~~~~

The ``deactivate`` sub-command deactivates the active vsc-Rproject environment.
Doing so will purge all loaded modules except for the cluster module and the vsc-Rproject module itself.
Additionally, it will unset the ``$VSC_RPROJECT`` variable.

.. code:: bash

   $ vsc-rproject deactivate


.. _default_project_configuration:

Default project configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to change the default behaviour of vsc-Rproject, you can configure your
personal default settings with the ``configure`` sub-command.

.. note::

   You can at all times check your current default settings with `vsc-rproject --defaults`.

``vsc-rproject configure`` allows you to set your prefered default R with ``--default-r``.
You may also set a new default location for your RStudio Projects with ``--location``.
Finally you can still configure your prefered default CRAN mirror using ``--cran``
and the default ``-march`` compiler settings with ``--march``.

These personal configurations will be stored in ``$VSC_HOME/.vsc-rproject-config``.

To further support working on a heterogeneous HPC environment the ``$VSC_RPROJECT_CONFIG``
environment variable can be used to specify an alternative ``.vsc-rproject-config`` file.
This allows for switching between different configurations depending on your needs.
e.g. working on different clusters.

If ``$VSC_RPROJECT_CONFIG`` is set, ``vsc-rproject`` will consider it and use it if possible.
If ``$VSC_RPROJECT_CONFIG`` is not set (default) ``vsc-rproject`` will use the default config file: ``~/.vsc-rproject-config``.

If at any point you wish to reset your configuration to the the original default settings, simply run:

.. code:: bash

   $ vsc-rproject configure --reset

vsc-Rproject and RStudio Server
-------------------------------

When launching a new session via :ref:`Studio Server <rstudio-server>`, you can use the ``pre-run scriplet`` to load the vsc-Rproject environment.

.. code::

   module load vsc-Rproject; vsc-rproject activate MyProject

.. warning::

   The R module selected in the OnDemand form must match the R module that was used to create the project!
   Otherwise dependency conflicts may arise as RStudio Server will replace the modules loaded via the pre-run scriplet.

Once inside the RStudio session, you still need to open the RStudio Project via the interface.
