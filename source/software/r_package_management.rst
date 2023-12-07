.. _R_package_management:

R package management
====================

Introduction
------------

Most of the useful R packages come in the form of packages that can be
installed separately. Some of those are part of the default installation
on VSC infrastructure. Given the astounding number of packages, it is
not sustainable to install each and everyone system wide. Since it is
very easy for a user to install them just for himself, or for his
research group, that is not a problem though. Do not hesitate to contact
support whenever you encounter trouble doing so.

Standard R package installation
-------------------------------

Setting up your own package repository for R is straightforward.

#. Load the appropriate R module, i.e., the one you want the R package
   to be available for::

      $ module load R/3.2.1-foss-2014a-x11-tcl

#. Start R and install the package (preferably in your $VSC_DATA directory)::

      > install.packages("DEoptim", lib="/data/leuven/304/vsc30468/R/")

#. Alternatively you can download the desired package::

      $ wget cran.r-project.org/src/contrib/Archive/DEoptim/DEoptim_2.0-0.tar.gz

      and install it with::
  
      $ R CMD INSTALL DEoptim_2.0-0.tar.gz  -l /$VSC_DATA/R/
      
#. These packages might depend on the specific R version, so you may
   need to reinstall them for the other version.
   
Some R packages depend on libraries installed on the system.  In that case,
you first have to load the modules for these libraries, and only then proceed
to the R package installation.  For instance, if you would like to install
the `gsl` R package, you would first have to load the module for the GSL
library, .e.g., ::

   $ module load GSL/2.5-GCC-6.4.0-2.28

Note that R packages often depend on the specific R version they were installed
for, so you may need to reinstall them for other versions of R.

Installing R packages using conda
---------------------------------

.. note::

    Conda packages are incompatible with the software modules.
    Usage of conda is discouraged in the clusters at UAntwerpen, UGent,
    and VUB.

The easiest way to install and manage your own R environment(s) is conda.


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

Additional information about conda can be found on its `documentation site <https://conda.readthedocs.io/en/latest/>`__.

For installing R packages from github or other repositories see also :ref:`R devtools<r_devtools>`:
