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

Installing your own packages using conda
----------------------------------------

The easiest way to install and manage your own R environment is conda.


Installing Miniconda
~~~~~~~~~~~~~~~~~~~~

If you have Miniconda already installed, you can skip ahead to the next
section, if Miniconda is not installed, we start with that. Download the
Bash script that will install it from
`conda.io <https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh>`__
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

Additional information about conda can be found on its `documentation
site <https://conda.readthedocs.io/en/latest/>`__.

Alternatives to conda
---------------------

Setting up your own package repository for R is straightforward.

#. Load the appropriate R module, i.e., the one you want the R package
   to be available for::

      $ module load R/3.2.1-foss-2014a-x11-tcl

#. Start R and install the package::

      > install.packages("DEoptim")

#. Alternatively you can download the desired package::

      $ wget cran.r-project.org/src/contrib/Archive/DEoptim/DEoptim_2.0-0.tar.gz

#. These packages might depend on the specific R version, so you may
   need to reinstall them for the other version.
