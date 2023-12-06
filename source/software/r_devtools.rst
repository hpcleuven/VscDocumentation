.. _r_devtools:

R installing packages with devtools
===================================

Introduction
~~~~~~~~~~~~

The installation of some R packages may require the use of devtools.
Devtools is an R package that facilitates the installation of other
R packages from github, gitlab, bitbucket or other repositories.
In what follows github will be used as an example, please consult the
devtools_ documentation for examples of other repositories.

Depending on how your R library is managed, you will need a slightly different
approach to use or install devtools.

A Standard R library
~~~~~~~~~~~~~~~~~~~~

When you are using a standard R library that you use alongside an 
R module or with RStudio Server, you can use the devtools that is
included in the module. The following steps assume that you already
have a standard R library located in your ``$VSC_DATA/R`` directory. 
If you have not yet set up your R library, first set up your :ref:`R library<r_package_management>`.

Using the module devtools to install R packages
-----------------------------------------------

From an interactive session on a Genius or wICE compute node you can load
your prefered R module and launch R.



::

   $ module load R/4.1.0-foss-2021a
   $ R

By default, the R library path will point to the module R library.
If this is the case, first set the R library to your personal R library path.



::

   > # check that the [1] R library path points to your personal R library
   > .libPaths()
   > # set the R library path if this was not the case.
   > .libPaths("/data/leuven/XXX/vscXXXXX/R/")

Load devtools and install your package from github.



::

   > library(devtools)
   > devtools::install_github("Developer/Package")

A Conda R environment 
~~~~~~~~~~~~~~~~~~~~~

If you are using conda to manage your R packages, you should first install
devtools in your conda environment. The following steps assume that you 
already have a conda R environment named "science". If you do not yet have
a conda R environment, First create a :ref:`conda environment<Python packages>`.

Using the conda devtools to install R packages
----------------------------------------------

From an interactive session on a Genius or wICE compute node, activate your 
R environment and install devtools



::

   $ source activate science
   $ conda install -c conda-forge r-devtools

Launch R and make sure that the R library 
path points to your conda library.



::

   $ R



::

   > # check that the [1] R library path points to your conda R library
   > .libPaths()
   > # set the R library path if this was not the case.
   > .libPaths("/data/leuven/XXX/vscXXXXX/miniconda3/envs/science/lib/R/library")

Load devtools and install your package from github.



::

   > library(devtools)
   > devtools::install_github("Developer/Package")

.. _devtools: https://www.rdocumentation.org/packages/devtools/versions/2.4.5
