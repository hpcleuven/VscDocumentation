.. _easybuild_spack:

EasyBuild and Spack
===================

`EasyBuild <https://easybuild.io>`_ and `Spack <https://spack.io>`_ are the two most prominent tools
that can be used to automate the installation of software from source code on HPC systems.

Both tools significantly facilitate software installation, and tap into the broad expertise of their respective communities.

EasyBuild
---------

EasyBuild is a tool to (build and) install (scientific) software.
It was originally created by `HPC-UGent <https://www.ugent.be/hpc/en>`_ in 2009,
and is available as open source software since 2012.

It automates the installation of (scientific) software from source code, and generates accompanying
environment module files so they can be used easily.

EasyBuild has strong focus on scientific software, collaboration, software performance, and HPC systems.

The `EasyBuild Slack <https://easybuild.io/join-slack>`_ is used as the main communication channel for worldwide community,
along with the `EasyBuild mailing list <https://lists.ugent.be/sympa/info/easybuild>`_.

EasyBuild is to the tool of choice for managing the central software stack on various HPC systems,
including the Tier-2 and Tier-1 clusters of the VSC, and various `EuroHPC JU <https://www.eurohpc-ju.europa.eu>`_ supercomputers (LUMI, JUPITER, ...).

Installing EasyBuild
~~~~~~~~~~~~~~~~~~~~

To install EasyBuild, use:

.. code-block:: bash

  pip install easybuild

We recommended to install EasyBuild a Python virtual environment.

After installing EasyBuild, you can run the ``eb`` command, for example to check the EasyBuild version:

.. code-block:: bash

    eb --version

Some addtional Python packages can be installed as optional dependencies for EasyBuild:

- ``rich`` (colors)
- ``archspec`` (CPU detection)

For more information on installing EasyBuild, see https://docs.easybuild.io/installation.


Configuring EasyBuild
~~~~~~~~~~~~~~~~~~~~~

Before you use EasyBuild, you should configure it.
This can be done via configuration files, environment variables, and command line options.

To show the active configuration, use:

.. code-block:: bash

    eb --show-config

To see *all* configuration options, use:

.. code-block:: bash

    eb --show-full-config

.. warning::

  Do not use default configuration!

  By default, EasyBuild will (ab)use a hidden directory in your home directory (``$HOME/.local/easybuild``).

An example minimal configuration via environment variables that is suitable to use in your VSC account:

.. code-block:: bash

  # configure EasyBuild to use $VSC_DATA/easybuild for everything (sources, software installations, etc.)
  export EASYBUILD_PREFIX=$VSC_DATA/easybuild
  # make an exception for the (temporary) build directories, which should be on local disk
  export EASYBUILD_BUILDPATH=/tmp/$USER

For more information on configuring EasyBuild, see https://docs.easybuild.io/configuration.

Basic usage of EasyBuild
~~~~~~~~~~~~~~~~~~~~~~~~

The basic usage workflow of EasyBuild is as follows:

#. Find an `easyconfig file <https://docs.easybuild.io/terminology/#easyconfig_files>`_ to install with ``eb --search``, or create one;
#. Assess what will be installed first using ``eb --missing`` (see also `here <https://docs.easybuild.io/using-easybuild#eb_missing>`_), ``eb -x`` (see also `here <https://docs.easybuild.io/extended-dry-run>`_), etc.
#. Use the ``eb`` command to install the easyconfig file, use ``--robot`` to enable dependency resolution (see also `here <https://docs.easybuild.io/using-easybuild/#use_robot>`_).
#. Load the environment module that was generated to start using the installed software.

For example, to install & use ``tblite``:

.. code-block:: bash

  eb --search tblite
  eb tblite-0.4.0-gfbf-2024a.eb --missing
  # build+install tblite (incl. dependencies)
  eb tblite-0.4.0-gfbf-2024a.eb --robot
  # make module available to load
  module use /path/to/modules/all
  # load tblite for usage
  module load tblite/0.4.0-gfbf-2024a

Note that existing environment module files will automatically be used for dependencies if they are visible via ``module avail``.


Links
~~~~~

For more information on EasyBuild, see:

- Website: https://easybuild.io
- Documentation: https://docs.easybuild.io
- EasyBuild tutorial: https://tutorial.easybuild.io
- GitHub organisation: https://github.com/easybuilders
- Slack channel: https://easybuild.io/join-slack
- Mailing list: https://lists.ugent.be/sympa/info/easybuild



Spack
-----

Spack is a package manager for supercomputers, which was originally created
by Lawrence Livermore National Lab (LLNL) in the US in 2014.

It automates software installation procedures, and can install pre-built software from binary cache,
and it particularly popular with software developers due to its usage model & specific features.

It can generate environment module files for software installations, but also has its own mechanism
for *activating* software (via ``spack load``).

Spack focuses on scientific software & HPC systems, but also supports macOS & Windows.

The `Spack Slack <https://https//slack.spack.io>`_ is used as main communication channel for the worldwide community.

Installing and configuring Spack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can "install" Spack by cloning the Git repository:

.. code-block:: bash

  git clone https://github.com/spack/spack

.. warning::

   This implies using the (potentially unstable) development version,
   so you may want to download a `specific version <https://github.com/spack/spack/releases>`_ of Spack instead.

By default, Spack will installed software in the ``spack/opt/spack`` subdirectory of where it was installed,
so pick a good location (*not* your home directory in your VSC account).

Before using Spack, you need to set up your shell environment by sourcing the provided script,
for example (for bash shell):

.. code-block:: bash

  source spack/share/spack/setup-env.sh

You should also make Spack aware of available (system) compilers, using:

.. code-block:: bash

  spack compiler find

.. note::

   Be aware that by default Spack will cache some stuff in ``$HOME/.spack``.

For more information on installing and configuring Spack, see https://spack.readthedocs.io/en/latest/getting_started.html.

Basic usage of Spack
~~~~~~~~~~~~~~~~~~~~

Tbe basic usage workflow of Spack is as follows (using ``tblite`` as example software):

#. Check whether software is supported: ``spack list tblite``
#. Show details of specific software: ``spack info tblite``
#. Show dependency graph of specific software: ``spack graph tblite``
#. Install the software with ``spack install``, for example:
    - Instal tblite version 0.4.0 incl. Python bindings with system compiler:

      .. code-block:: bash

        spack install tblite@0.4.0 +python

    - Install tblite version 0.4.0 with GCC 13 as compiler:

      .. code-block:: bash

        # first install GCC 13
        spack install gcc@13
        # install tblite 0.4.0, incl. Python bindings, with GCC 13
        spack install tblite@0.4.0 +python %gcc@13

#. Load the software to starting using it:
    - ``spack find tblite``
    - ``spack load tblite``

Links
~~~~~

For more information on Spack, see:

- Website: https://spack.io
- Documentation: https://spack.readthedocs.io
- Slack channel: https://https://slack.spack.io
- GitHub organisation: https://github.com/spack


EasyBuild vs Spack
------------------

EasyBuild and Spack are quite similar in several ways, yet quite different in many other ways.

Similarities between EasyBuild & Spack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Both are open source software implemented in Python;
- Both are Developed & supported by a worldwide community;
- Both focus on scientific software, performance, HPC systems;
- Both require *no* admin privileges to build & install software;
- Both are highly configurable: you can tune them to your preferences;
- Both are an "expert system” for installing (scientific) software;
- Both wrap around commonly used tools like CMake, make, pip, ...;
- Neither are a magic solution: building software may still fail (compiler errors, etc.);

Differences between EasyBuild & Spack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The EasyBuild community is mostly European, while Spack is mostly US-based;
- EasyBuild is available under the GPLv2 open source license, while Spack is dual-licensed under Apache 2.0 + MIT;
- You can install EaysBuild via ``pip install``, Spack is typically installed with ``git clone``;
- EasyBuild mainly supports Linux, while Spack supports Linux, macOS, and Windows;
- EasyBuild has interesting features for HPC support teams, while Spack is more targeted towards software developers;
- EasyBuild has published frequent stable releases since 2012, Spack 1.0 was released in summer of 2025;
- EasyBuild strongly prefers building software from source code (when possible), Spack also has support for using a binary cache (pre-built binary packages);
- Both have specific features:
    - EasyBuild has integration with `Slurm <https://docs.easybuild.io/submitting-jobs/>`_, `GitHub <https://docs.easybuild.io/integration-with-github/>`_, and other tools;
    - The functionality of EasyBuild can be customized via `hooks <https://docs.easybuild.io/hooks/>`_;
    - Spack has support for `environments <https://spack.readthedocs.io/en/latest/environments_basics.html>`_.
    - Spack has good support for building `container images <https://spack.readthedocs.io/en/latest/containers.html>`_;

When (not to) use EasyBuild or Spack
------------------------------------

Both EasyBuild and Spack provide a uniform way of installing software, regardless of specifics of installation procedure. They automate (complex) software installation procedures, including required dependencies.
They can both be used to build a consistent (central) software stack, with software performance in mind,
and install same software stack across different systems/partitions.

Both leverage efforts by experienced people who contributed to these tools,
and you can get help through community channels (there's a dedicated Slack for both).

However, there is a *steep initial learning curve* for both. Some experience with compilers
& manually installing software can be helpful. You should take you some time to learn how
to use the tool you picked (docs, tutorial, etc.).

