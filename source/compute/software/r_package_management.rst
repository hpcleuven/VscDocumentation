.. _R_package_management:

R package management
====================

.. _r_package_management_intro:

Introduction
------------

There exist thousands of R packages, available from online repositories like CRAN,
Bioconductor or github. Depending on the R version, the more commonly used packages like `ggplot2`, `tidyverse` or `readr`
are either already included in the centrally installed R module or can be accessed by
loading the `R-bundle-CRAN` and `R-bundle-Bioconductor` modules, e.g.:

.. code:: r

       $ module load R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2

It is possible, however, that these modules do not contain all R packages you
need or that the package versions do not meet your requirements. In this case
you will need to install those packages locally. Do not hesitate to contact
your local support team when encountering issues along the way.

The sections below explain different ways to go about these installations.
These assume that you are either using a centrally installed R module
(:ref:`Using RStudio Projects<r_package_management_with_vsc_rproject>`,
:ref:`Standard R package installation<r_package_management_standard_lib>`)
or Conda (:ref:`Installing R packages using Conda<r_package_management_conda>`).
In all cases, however, it is best to keep the following in mind:

* By default, R uses the ``$VSC_HOME/R`` path to install new packages.
  Since ``$VSC_HOME`` has limited quota, it is not the recommended location
  to install software. Instead, we recommend to use ``$VSC_DATA``.

* R packages often include extensions written in compiled languages (e.g.
  C++ or Fortran). The centrally installed R modules are configured to compile
  these extensions with optimizations for the CPU architecture at hand
  (specifically the ``"-march=native"`` option when using GCC compilers).
  This means that R extensions compiled in this way may not work
  on other partitions than the one they were created on.

* A given version of an R package may only work with certain R versions.
  For example, a package installed with R version 4.2.2 may not work when used with
  R 4.4.1. Since typically many different R versions are available,
  as a user you should always be aware of the correct version to use for
  your project(s).


.. _r_package_management_with_vsc_rproject:

Using RStudio Projects with vsc-Rproject
----------------------------------------

When using a centrally installed R module, you can easily manage your own
R environments with custom packages using so-called
`RStudio Projects <https://docs.posit.co/ide/user/ide/guide/code/projects.html>`_.
RStudio Projects provide a self-contained, organized environment in R. Each project has
its own working directory, workspace and history which helps to avoid conflicts between different
projects. This structure encourages best practices such as using relative paths
and version control (e.g. git).

The :ref:`vsc-Rproject tool <vsc-Rproject>` helps you create RStudio Projects,
and allows to compile extensions in a more portable way. The tool furthermore
simplifies setting up your R environment (including selecting the correct R
module). Once activated, commands such as ``install.packages(...)`` or
``devtools::install_github(...)`` will yield portable installations in a
well-defined, project specific location.


.. _r_package_management_standard_lib:

Standard R package installation
-------------------------------

In case `vsc-Rproject` does not suit your needs, then you can still go about
your local package installations as follows.

Considering the dependence of the compiled package on the host OS version, CPU microarchitecture
and R version (see the :ref:`Intro<r_package_management_intro>`), we recommend
to use a directory structure that makes these distinctions. The example below
creates such a structure for a Rocky8 OS, Icelake CPU and R version 4.2.2:

.. code-block:: bash

      # From within an interactive session on an icelake compute node:
      $ module load R/4.2.2-foss-2022b
      $ mkdir -p ${VSC_DATA}/Rlibs/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}/R-${EBVERSIONR}

The next step is to ensure such install locations are used by default in the R package installation process.
This can be done by setting the `R_LIBS_USER` variable to in the `~/.Renviron` file as follows:

.. code-block:: bash

      $ echo 'R_LIBS_USER=${VSC_DATA}/Rlibs/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}/R-${EBVERSIONR}' >> ~/.Renviron

The `${VSC_OS_LOCAL}` and `${VSC_ARCH_LOCAL}` environment variables are predefined
and match the OS version (e.g. `rocky8`) and CPU model (e.g. `icelake`) of the node.
The `${EBVERSIONR}` variable contains the R version (e.g. `4.2.2`) of the currently loaded
R module.

R will now use this path as default install path, ensuring you are always installing
your packages in the appropriate R library folder.

.. note::

  This `.Renviron` configuration will also work as expected in Open OnDemand apps
  such as RStudio Server.

The next step is to load the appropriate R module and run R.

.. code-block:: bash

      # From within an interactive session on an icelake compute node:
      $ module load R/4.2.2-foss-2022b
      $ R

From here, installing packages can be as simple as:

.. code-block:: r

      > install.packages("DEoptim")


If you are unsure whether R will install your desired package in the correct location, you can first list
the known library locations by executing `.libPaths()`. The first location is the
default one.

You can also specify your desired library path as an extra argument in the install command.
This will take precedence over any defaults.

.. code-block:: r

      > Rlibs <- "/path/to/my/R_library"
      > install.packages("DEoptim", lib = Rlibs)

Alternatively you can download the desired package

.. code-block:: bash

      $ wget cran.r-project.org/src/contrib/Archive/DEoptim/DEoptim_2.0-0.tar.gz

and install it from the command line with

.. code-block:: bash

      # From within an interactive session on an icelake compute node:
      $ module load R/4.2.2-foss-2022b
      $ R CMD INSTALL DEoptim_2.0-0.tar.gz  -l ${VSC_DATA}/Rlibs/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}/R-${EBVERSIONR}

If the installation of a package requires devtools, please consult the :ref:`devtools documentation<r_devtools>`.


.. _r_package_management_conda:

Installing R packages using conda
---------------------------------

.. note::

    Conda packages are incompatible with the software modules.
    Usage of conda is discouraged in the clusters at UAntwerpen, UGent,
    and VUB.

The paragraphs below illustrate how to install and use R and R packages
in a Conda environment.

.. _install_miniconda_r:

Installing Miniconda
~~~~~~~~~~~~~~~~~~~~

If you have Miniconda already installed, you can skip ahead to the next
section, if Miniconda is not installed please follow our :ref:`guide to installing miniconda <install_miniconda_python>`.

.. _create_r_conda_env:

Creating an environment
~~~~~~~~~~~~~~~~~~~~~~~

First, ensure that the Miniconda installation is in your PATH
environment variable. The following command should return the full path
to the conda command::

   $ which conda

If the result is blank, or reports that conda can not be found, modify
the \`PATH\` environment variable appropriately by adding miniconda's bin
directory to PATH.

The next step is to create a new conda environment which can be done as follows::

   $ conda search -c conda-forge r-base  # select one of available versions for the step below
   $ conda create -n science -c conda-forge r-base=<version> r-essentials


This command creates a new conda environment called "science", and installs your prefered R
version from the conda-forge channel as well as the r-essentials bundle which includes number
of commonly used R packages such as ggplot2, glmnet, dplyr, tidyr, and shiny.

.. note::

   A lot of bioconda and bioconductor packages are not in sync with their dependencies, therefore you may need to create a separate environment for each of those packages to avoid conflicts.

Working with the environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To work with an environment, you have to activate it. This is done with,
e.g.,

::

   $ source activate science

Here, science is the name of the environment you want to work in.


Install an additional package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install an additional package, e.g., ``rodbc``, first ensure that the
environment you want to work in is activated.

::

   $ source activate science

Next, install the package:

::

   $ conda install -c conda-forge r-rodbc

Note that conda will take care of all dependencies, including non-R
libraries. This ensures that you work in a consistent environment.

Updating/removing
~~~~~~~~~~~~~~~~~

Using conda, it is easy to keep your packages up-to-date. Updating a
single package (and its dependencies) can be done using:

::

   $ conda update r-rodbc

Updating all packages in the environment is trivial:

::

   $ conda update --all

Removing an installed package:

::

   $ conda remove r-mass

Deactivating an environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To deactivate a conda environment, i.e., return the shell to its
original state, use the following command

::

   $ source deactivate

More information
~~~~~~~~~~~~~~~~

Additional information about conda can be found on its `documentation site <https://docs.conda.io/en/latest/>`__.

For installing R packages from github or other repositories see also :ref:`R devtools<r_devtools>`:
