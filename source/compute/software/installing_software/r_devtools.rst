.. _r_devtools:

R packages with devtools
========================

The installation of some R packages may require the use of `devtools
<https://devtools.r-lib.org/>`__. The devtools package facilitates the
development of your own R packages as well as the installation of R packages
from Git repositories such as GitHub, Gitlab or Bitbucket.

In the following we will use GitHub as example. Please consult the
`devtools documentation`_ for examples with other repositories.

The devtools package is already available in all software modules of R
found in the central libraries of VSC clusters.

.. code-block:: console

   $ module load R/4.5.1-gfbf-2025a
   $ R
   > library(devtools)
   > sessioninfo::session_info()
   ## ─ Session info ────────────────────
   ##  setting  value
   ##  version  R version 4.5.1 (2025-06-13)
   ##  [...]
   ## ─ Packages ────────────────────────
   ##  package     * version date (UTC) lib source
   ##  cachem        1.1.0   2024-05-16 [2] CRAN (R 4.5.1)
   ##  cli           3.6.5   2025-04-23 [2] CRAN (R 4.5.1)
   ##  devtools    * 2.4.6   2025-10-03 [2] CRAN (R 4.5.1)
   ##  [...]

Installs in local R library
---------------------------

Installations with devtools in a :ref:`local R library <r_package_management_standard_lib>`
follow the same :ref:`location rules <r_package_management_location>`
as for the default package manager in R.

You can check and control the list of library paths with ``.libPaths()`` as usual:

.. code-block:: r

   # First check that the R library path points to your local R library:
   .libPaths()
   # Set the R library path if this is not the case. e.g.
   .libPaths("/data/leuven/XXX/vscXXXXX/Rlibs/rocky8/icelake/R-4.2.2")

Once the target location is set, then you can install a package from GitHub
with devtools as follows:

.. code-block:: r

   library(devtools)
   install_github("Developer/Package")

Devtools in a Conda environment
-------------------------------

If you are using Conda to manage your R packages, you should first install
devtools in your :ref:`Conda environment <conda_based_managers>`.
The following steps assume that you already have a working Conda environment
with R named *science*. If you do not yet have such an environment, you can
create one by following the instructions in :ref:`r_package_management_conda`. 

In the following example, it is assumed that your miniconda environment is
installed in ``$VSC_DATA/miniconda3``.

1. Activate your conda environment and install devtools

   .. code-block:: console

      $ source activate science
      $ conda install -c conda-forge r-devtools

2. Launch R and load devtools

   .. code-block:: r

      ## Check that the R library path points to your conda R library
      .libPaths()
      ## Set the R library path if this was not the case.
      .libPaths("/data/<vsc-site>/xxx/vscxxxxx/miniconda3/envs/science/lib/R/library")
      ## Load devtools and e.g. install your package from github:
      library(devtools)

3. Install some R package with devtools

   .. code-block:: r

      devtools::install_github("Developer/Package")

.. _devtools documentation: https://www.rdocumentation.org/packages/devtools
