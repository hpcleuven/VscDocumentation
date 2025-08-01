.. _vsc-Rproject:

vsc-Rproject
============

Introduction
------------

``vsc-Rproject`` is a command-line tool that facilitates the setup,
management and use of RStudio Projects on VSC HPC clusters.
Two main advantages of using ``vsc-Rproject`` are that the project settings and R libraries
are kept separate for each project, and that compiled extensions are easier
to manage in a cluster with heterogeneous hardware.

.. note::

   In what follows, the term 'vsc-Rproject environment' refers to the
   environment created by vsc-Rproject. This environment enables the use of an
   associated RStudio Project.

How to use
----------

vsc-Rproject can be used by simply loading the corresponding module.

.. code:: bash

   $ module load vsc-Rproject


Then, use the ``vsc-rproject`` command for its different functionalities.

.. code:: bash

   $ vsc-rproject --help
   $ vsc-rproject --version

The ``vsc-rproject`` command provides four sub-commands that can be used to ``configure`` default behaviour
or ``create``, ``activate``, or ``deactivate`` a vsc-Rproject environment.

.. _creating_a_project:

Creating a project
~~~~~~~~~~~~~~~~~~

The command ``vsc-rproject create`` allows you to create a new RStudio Project together with a vsc-Rproject environment.

When creating a new project, the only required argument is a project name.

We recommend to always provide a "modules file" when creating new projects.
This is a simple text file listing a module (full name and version) per line.
With a modules file, vsc-Rproject will ensure that these modules are always
loaded upon activating the corresponding vsc-Rproject environment.
If no modules file is provided, the default R module will be used instead.

The following command will create a ``modules.txt`` file in your data directory,
containing the following modules:

- ``R/4.4.1-gfbf-2023b``
- ``R-bundle-CRAN/2024.06-foss-2023b``

.. code:: bash

   $ printf "R/4.4.1-gfbf-2023b\nR-bundle-CRAN/2024.06-foss-2023b\n" > $VSC_DATA/modules.txt


.. note::

   When you specify a modules file, it should always contain the R module.

To create a new RStudio Project and vsc-Rproject environment using this modules file, run the following command:

.. code:: bash

   $ vsc-rproject create MyProject --modules="$VSC_DATA/modules.txt"

This will create a new RStudio Project named 'MyProject' at the default location: ``$VSC_DATA/Rprojects``.
The modules.txt file will be used when creating the project, and is stored in ``$VSC_DATA/Rprojects/.vsc-rproject/modules.env``.

.. note::

   If you wish to update the modules list for an existing project, you should manually
   add it to the ``$VSC_DATA/Rprojects/.vsc-rproject/modules.env`` file.


The project folder will contain ``.Renviron``, ``.Rprofile`` and
``.R/Makevars`` configuration files, which are therefore specific to the
project.

The ``.Renviron`` file will set the ``R_LIBS_USER`` variable to point to the project's R package library.
This can be found at the root of the project, under ``/library/<OS>/R``.

The ``.Rprofile`` file will be configured to set the CRAN mirror to ``"https://cloud.r-project.org"`` (default)
and set the ``R_MAKEVARS_USER`` variable to point to the project's ``.R/Makevars`` file.

The ``.R/Makevars`` file can be used to control the compilation process when installing
new R packages by modifying the compiler flags. vsc-Rproject's default behaviour
is to change the ``-march`` compiler flag for all relevant compilers from `native`
to `x86-64-v4`.

.. note::

   Compared to ``-march=native``, the ``-march=x86-64-v4`` compiler flag will discard
   certain microarchitecture-specific optimizations (potentially with a minor
   performance impact) to allow for a more generic installation which will run
   on any AVX512-capable x86-64 CPU (e.g. Skylake and newer for Intel CPUs and
   Zen4 and newer for AMD CPUs). For most users this will be the more desirable
   option as it makes switching between different types of compute nodes a lot
   easier. If some of the node types you want to utilize do not support this
   microarchitecture level, you can e.g. choose ``-march=x86-64-v3`` instead.

.. warning::

   Compiler options such as ``-march=x86-64-v3`` and ``-march=x86-64-v4`` are
   only supported in GCC version 11 and later. If you are using an older
   version of R that relies on an earlier GCC version, ``-march=x86-64-v...``
   will not be recognized. In such cases, you can run ``gcc --target-help``
   to view the list of supported ``-march`` values and choose a more
   appropriate setting.


If you want to enable git within the RStudio Project you can add the ``--enable-git`` flag.
To automatically activate the vsc-Rproject environment after creating it, use ``--activate``.

If you are not satisfied with the default behaviour, you can modify the behaviour
of ``vsc-rproject create`` by providing additional command-line arguments.
You can specify ``--location`` to create your project in a different location.
The ``--cran`` argument can be used to provide a specific CRAN mirror for your project.
Finally ``--march`` allows you to choose a different microarchitecture optimization
for your project.


For more information, see:

.. code:: bash

   $ vsc-rproject create --help


.. note::

   Alternatively, you may also want to  modify your default settings more permanently via ``vsc-rproject configure``.
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

   You can at all times check your current default settings with ``vsc-rproject --defaults``.

``vsc-rproject configure`` allows you to set your prefered default R with ``--default-r``.
You may also set a new default location for your RStudio Projects with ``--location``.
Finally you can still configure your prefered default CRAN mirror using ``--cran``
and the default ``-march`` compiler settings with ``--march``.

These personal configurations will be stored in ``$VSC_HOME/.vsc-rproject-config``.

You can provide an alternative path for this configuration file by setting
the ``$VSC_RPROJECT_CONFIG`` environment variable. This e.g. allows to
apply different defaults for different clusters.
If ``$VSC_RPROJECT_CONFIG`` is set, ``vsc-rproject`` will consider it and use it if possible.
If ``$VSC_RPROJECT_CONFIG`` is not set (default) ``vsc-rproject`` will use the default config file in ``$VSC_HOME/.vsc-rproject-config``.

If at any point you wish to reset your configuration to the the original default settings, simply run:

.. code:: bash

   $ vsc-rproject configure --reset

vsc-Rproject and RStudio Server
-------------------------------

When launching a new session via the :ref:`Studio Server <rstudio-server>` app in the Open Ondemand portal, you can use the ``pre-run scriplet`` to load the vsc-Rproject environment.

.. code::

   module load vsc-Rproject; vsc-rproject activate MyProject

.. warning::

   The R module selected in the OnDemand form must match the R module that was used to create the project!
   Otherwise dependency conflicts may arise as RStudio Server will replace the modules loaded via the pre-run scriplet.

Once inside the RStudio session, you still need to open the RStudio Project via the interface.
