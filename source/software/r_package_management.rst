.. _R_package_management:

R package management
====================

Introduction
------------

There exist thousands of R packages, available from online repositories like CRAN,
Bioconductor or github. The more commonly used packages like `ggplot2`, `tidyverse` or `readr` 
are included in the centrally installed R modules or can be accessed by simply 
loading the R-bundle-CRAN and R-bundle-Bioconductor modules. 

.. code:: r

       $ module load R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2    

However, perhaps you want a more recent version of one specific package or the
package you need is not provided via our modules, in that case you may need to
set up your own personal R library to install those packages yourself.
Below you can find extensive documentation on how to manage your own R library
on our HPC infrastructure. If you do encounter problems when doing so, do not 
hesitate to contact support.

.. _r_package_management_standard_lib:

Standard R package installation
-------------------------------

It is important to realize that R will use by default the `$VSC_HOME/R` path
to install new packages. Since the home directory is only 3GB in size, it is not
the recommended location to install software. So, before we can begin with 
installing our packages, it is important to prepare our library location first.

R packages are compiled during the installation and as a result, they are optimized
for the hardware they were installed on. Packages installed on the one partition
may thus perform worse when used on another partition. R packages are often also
version specific and may not work with other versions of R. With this in mind,
we will first create a directory structure providing a unique path for each OS
version, hardware architecture and R version.

In this example we assume you will primarily compute on icelake with R version 4.2.2.

.. code-block:: bash

      $ mkdir -p ${VSC_DATA}/Rlibs/rocky8/icelake/R-4.2.2

Now that we've setup this directory, the next step is to make sure it is used 
by default when starting an R session. We can use the R_LIBS_USER variable to
specify our prefered install path in the ~/.Renviron file. By usesing system
variables such as `${VSC_ARCH_LOCAL}` or `${EBVERSIONR}` we can ensure that this
path always matches the OS and architecture of the compute node as well as the
R version of the currently loaded R module.

The following command creates the ~/.Renviron file and sets the R_LIBS_USER variable:

.. code-block:: bash

      $ echo "R_LIBS_USER=\${VSC_DATA}/Rlibs/\${VSC_OS_LOCAL}/\${VSC_ARCH_LOCAL}/R-\${EBVERSIONR}" > ~/.Renviron

R will now use this path as default install path, ensuring you are always installing
your packages in the appropriate R library folder.

.. note::

  This setup also works with the Open OnDemand RStudio Server app.

The next step is to load the appropriate R module and launch R.

.. code-block:: bash

      $ module load R/4.2.2-foss-2022b
      $ R

From here, installing packages can be as simple as:

.. code-block:: r

      > install.packages("DEoptim")


If you are unsure if R will install in the correct location, you can check where 
R will install your packages using the `.libPaths()` command in your R console.
This will list all known library locations, the first one being the default 
location.

.. code-block:: r

      > .libPaths()

You can also specify your desired library path as an extra argument in the install command.
This will take precedent over any defaults.

.. code-block:: r

      > Rlibs <- "/path/to/my/R_library"
      > install.packages("DEoptim", lib = Rlibs)

Alternatively you can download the desired package

.. code-block:: bash

      $ wget cran.r-project.org/src/contrib/Archive/DEoptim/DEoptim_2.0-0.tar.gz

and install it from the commandline with

.. code-block:: bash
  
      $ R CMD INSTALL DEoptim_2.0-0.tar.gz  -l ${VSC_DATA}/Rlibs/rocky8/icelake/R-4.2.2

If the installation of a package requires devtools, please review the :ref:`devtools documentation<r_devtools>`.


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
section, if Miniconda is not installed, we start with that. Download the
Bash script that will install it from
`conda.io <https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_
using, e.g., ``wget``::

   $ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

Once downloaded, run the installation script::

   $ bash Miniconda3-latest-Linux-x86_64.sh -b -p $VSC_DATA/miniconda3

Optionally, you can add the path to the Miniconda installation to the
PATH environment variable in your ``.bashrc`` file. This is convenient, but
may lead to conflicts when working with the module system, so make sure
that you know what you are doing in either case. The line to add to your
``.bashrc`` file would be::

   export PATH="${VSC_DATA}/miniconda3/bin:${PATH}"

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

Creating a new conda environment is straightforward::

   $ conda create -n science -c r r-essentials r-rodbc

This command creates a new conda environment called science, and
installs a number of R packages that you will probably want to have
handy in any case to preprocess, visualize, or postprocess your data.
You can of course install more, depending on your requirements and
personal taste.

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

To install an additional package, e.g., \`pandas`, first ensure that the
environment you want to work in is activated.

::

   $ source activate science

Next, install the package:

::

   $ conda install -c r r-ggplot2

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
