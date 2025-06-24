.. _R_package_management:

R package management
====================

Introduction
------------

There exist thousands of R packages, available from online repositories like CRAN,
Bioconductor or github. Depending on the R version, the more commonly used packages like `ggplot2`, `tidyverse` or `readr` 
are either already included in the centrally installed R module or can be accessed by
loading the `R-bundle-CRAN` and `R-bundle-Bioconductor` modules, e.g.:

.. code:: r

       $ module load R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2    

It is possible, however, that these modules do not contain all R packages you need
or that the package versions do not meet your requirements. In this case you will
need to locally install those packages, as will be described below. Do not hesitate
to contact your local support team when encountering issues during these local installations.


.. _r_package_management_with_vsc_rproject:

RStudio Projects and HPC
------------------------

Researchers that need to use many custom environments in R (`i.e.` with R packages not
provided in modules) can easily manage such environments with so-called `RStudio Projects`.
RStudio Projects provide a self-contained, organized environment in R. Each project has 
its own directory, workspace and history which helps avoid conflicts between different
analyses. This structure encourages best practices such as modular code, as well as the 
use of relative filepaths and version control (e.g. git integration). 

However, using RStudio Projects on a heterogenous HPC system posses a couple challenges.
A first challenge stems from the fact that R packages are version dependent, which requires
that each newly created project is associated with a specific R installation (or R module).
While a package manager like `renv <https://rstudio.github.io/renv/articles/renv.html>`_
introduce some facilities in this direction compared to basic R, `renv` was not developed
with heterogeneous HPC hardware in mind.
This also immediately introduces the second challenge. By default, R packages are compiled
for the specific CPU microarchitecture of the system used for their installation.
Ideally you would want your project's package library to be compatible with as many architectures as
possible without sacrificing performance. 

With these difficulties in mind, we have developed vsc-Rproject which provides a convenient 
way to manage RStudio Project environments in a way that is compatible with our heterogenous 
HPC infrastructure. Check the instructions for :ref:`vsc-Rproject<vsc-Rproject>` and jump onto
your VSC cluster to start using it. 

.. _r_package_management_standard_lib:

Standard R package installation
-------------------------------

Firstly, it is important to realize that R by default uses the `$VSC_HOME/R` path
to install new packages. Since `$VSC_HOME` has limited quota, it is not
the recommended location to install software. Instead, we recommend to use `$VSC_DATA`.

Secondly, it should be kept in mind that R packages often include extensions written in
compiled languages (e.g. C++ or Fortran) and that the centrally installed R modules are
configured to compile these extensions with optimizations for the CPU architecture at hand.
This means that such R packages cannot in general be used on different partitions than the
one they were created on.

Thirdly, R packages may also only work with certain versions of R and not with other versions.

With these three considerations in mind, we recommend to use a directory structure which
provides a unique path for each OS version, hardware architecture and R version.
The example below creates such a structure for a Rocky8 OS, Icelake CPU and R version 4.2.2:

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

The easiest way to install and manage your own R environment(s) is conda.

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
