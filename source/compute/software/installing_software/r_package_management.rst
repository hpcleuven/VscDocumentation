.. _R_package_management:

R package management
====================

There are thousands of R packages available online. The most popular
indexed repositories are `CRAN`_ and `Bioconductor`_. While you can also many
single package repositories on `GitHub`_.

How to find available R packages in modules?
--------------------------------------------

* The module **R** provides a basic installation with a minimum set of R
  packages just to allow development in R (*e.g.* with :ref:`devtools <r_devtools>`)
* The module **R-bundle-CRAN** provides an extensive collection of R packages
  from the `CRAN`_ repository. Packages cover all scientific domains.
* The module **R-bundle-Bioconductor** provides an extensive collection of R
  packages from the `Bioconductor`_ repository. Packages cover the bio sciences.
* Some R packages can be provided with specific modules. This happens for R
  packages that need a large collections of libraries (*e.g.* INLA, Seurat) or
  for R packages that need specific non-R dependencies (*e.g.* RPostgreSQL)

R packages as module extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R package are typically installed as extensions in software modules that bundle
many of them. Hence, the name of software modules alone might not be useful to
find a particular R Package. It is necessary to search them with the ``module``
command.

1. Use ``module spider`` to find the available extensions for some R package.
   For instance ``ggplot2``:

   .. code-block:: console

      $ module spider ggplot2
      --------------------------------
        ggplot2:
      --------------------------------
        Versions:
          ggplot2/3.4.4 (E)
          ggplot2/3.5.1 (E)

      Names marked by a trailing (E) are extensions provided by another module.
      --------------------------------
        For detailed information about a specific "ggplot2" package (including how
        to load the modules) use the module's full name.
        Note that names that have a trailing (E) are extensions provided by other modules.
        For example:
          module spider ggplot2/3.5.1
      --------------------------------

2. Once you identify the exact name of the extension and its version, search
   again to find the module that contain it:

   .. code-block:: console

      $ module spider ggplot2/3.5.1
      --------------------------------
        ggplot2: ggplot2/3.5.1 (E)
      --------------------------------
        This extension is provided by the following modules. To access the
        extension you must load one of the following modules. Note that any
        module names in parentheses show the module location in the software
        hierarchy.

        R-bundle-CRAN/2024.11-foss-2024a

Installing your own R packages
------------------------------

It is possible that the available software modules in your cluster do not
contain all R packages you need, or that the package versions do not meet your
requirements. In such a case, you can install those R packages locally on your
own.

The sections below explain different methods to carry out the installation of R
packages in VSC clusters. In general, installing software with R is relative
simple but it is important to note the following caveats and potential
pitfalls:

* Do not install R on your own. All methods described herein use a central
  installation of R from some software module as base and install R packages on
  top of it. This provides a solid foundation to build your projects.

* By default, R uses the ``$VSC_HOME/R`` path to install new packages. Since
  your home directory has :ref:`limited quota <quota>`, it is not recommended
  to use it to install software. Instead, you can use ``$VSC_DATA``.

* R packages often include code written in compiled languages (*i.e.* C++
  or Fortran). The centrally installed R modules are configured to compile
  such extensions with optimizations for the CPU architecture being used in
  the installation (*e.g.* the ``-march=native`` option on GCC compilers). This
  means that such R packages with compiled code may not work on other VSC
  clusters or partitions than the one used for their installation.

* A given version of an R package may only work with certain R versions.
  For example, a package installed with R version 4.2.2 may not work when used
  with R 4.4.1. Since many different R versions are typically available on VSC
  clusters, you should always be aware of the active version of R and make sure
  it is compatible with the R package in use.

.. note:: 

   Do not hesitate to contact your :ref:`local support team <tech support VSC>`
   if you experience any trouble carrying out the installation of R packages on
   VSC clusters.

.. _r_package_management_with_vsc_rproject:

RStudio Projects with vsc-Rproject
----------------------------------

`RStudio Projects <https://docs.posit.co/ide/user/ide/guide/code/projects.html>`__
provide a self-contained, organized environment in R that help manage software
installations for multiple research projects. Each *RStudio Project* has its own
working directory, workspace and history which helps to avoid conflicts between
different projects. It also allows to easily control the environment with
version control tools such as Git.

|Recommended| The :ref:`vsc-Rproject tool <vsc-Rproject>` helps you create
*RStudio Projects* without RStudio (so-called *RProjects*). It can be used from
the command line to create an *RProject* in any directory of choice, set up the
environment of the *RProject* (including selecting the correct R module) and
allows to build and install R packages in a more portable way. Once activated,
commands such as ``install.packages(...)`` or ``devtools::install_github(...)``
will automatically happen inside the active RProject and yield portable
installations in a well-defined location.

.. seealso::

   The documentation on **vsc-Rproject** provides step-by-step instructions:

   .. toctree::
      :maxdepth: 2

      vsc_rproject

.. _r_package_management_standard_lib:

R package manager
-----------------

R provides a simple package manager that can be used to install basic R
packages without compiled code and with a small amount of dependencies.

|Warning| The simplicity of the default R package manager is its strength and
weakness. Its easy to use but you should be aware of its limitations before
using it on complex projects:

* *No reproducibility*: it is hard to manage the versions of packages installed
  in R. Any future installation might upgrade some package and break your
  environment.

* *No isolation*: Installed packages are tight to a single version of R, but
  there is no way to easily activate/deactivate them. So whenever that specific
  version of R is used, those packages will be active in your environment.

* *No portability*: Installed packages with R might involve lower-level
  compiled code. The resulting binaries might break on other systems than the
  one used for the installation.

.. _r_package_management_install:

Installs with R package manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R package manager provides the method ``install.packages()`` to install
additional packages. This method is readily available in the R base library of
packages and it can be used to install packages from local or remote sources.

* simple case where package is downloaded from a remote repo (usually `CRAN`_)

  .. code-block:: r

     install.packages("ggplot2")

* install package from a specific repository such as R-Forge

  .. code-block:: r

     install.packages("ggplot2", repos = "http://R-Forge.R-project.org", dependencies = TRUE)

* install package from a local file

  .. code-block:: r

     install.packages("/path/to/ggplot2-3.5.1.zip", repos = NULL, type = "source")

.. warning::

   The method ``install.packages()`` does **not control the version** of the
   installed package in the system, which can be dangerous and result in
   non-working environments. To control which version of the package is
   installed we recommend to use :ref:`vsc-Rproject`, or alternatively you can
   use ``install_version()`` from the *remotes* library

   .. code-block:: r

      library(remotes)
      install_version("ggplot2", version = "3.5.1")

If you want to install R packages from GitHub or other Git repositories, you
can do so with the :ref:`devtools <r_devtools>` library. Check our
documentation on devtools:

.. toctree::
   :maxdepth: 2

   r_devtools

.. _r_package_management_location:

Location of installed R packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R will check multiple directories for required packages/libraries and will try
to install new packages in the top directory reported by the method ``libPaths()``

.. code-block:: r

   > .libPaths()
   [1] "/user/brussel/100/vsc10000/R/x86_64-pc-linux-gnu-library/4.4"
   [2] "/apps/brussel/RL8/skylake-ib/software/R-bundle-CRAN/2024.11-foss-2024a"
   [3] "/apps/brussel/RL8/skylake-ib/software/R/4.4.2-gfbf-2024a/lib64/R/library"

In the previous example:

* *[1]* is your personal R library. Can be changed with environment variable
  ``$R_LIBS_USER``. By default located at ``~/R/R.version$platform-library/x.y``.

* *[2]*  Site libraries added by module files. Read-only.

* *[3]*  Main R library of the active R interpreter. Read-only.

.. note::

   All these library paths are specific to the active version of R in use!

Considering the dependence of the installation on the active version of R and
the potential dependency on the CPU microarchitecture of the system in use, we
recommend using a :ref:`vsc-Rproject` instead. Alternatively, you can make a
directory structure that makes these distinctions on R version and system
architecture to be able to keep installations for different environments
separate.

The example below creates such a file structure for the R library by using VSC
environment variables that define the current system in use. Under ``Rlibs``,
we make a subdirectory for the current operating system ``$VSC_OS_LOCAL``, then
another subdirectory for the current system architecture ``$VSC_ARCH_LOCAL``
and then one last subdirectory for the active version of R:

.. code-block:: bash

   $ module load R/4.5.1-gfbf-2025a
   $ mkdir -p ${VSC_DATA}/Rlibs/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}/R-${EBVERSIONR}

The next step is to ensure that R uses that new location in the R package
installation process. This can be done by setting the ``R_LIBS_USER`` variable
in the ``~/.Renviron`` file as follows:

.. code-block:: bash

   $ echo 'R_LIBS_USER=${VSC_DATA}/Rlibs/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}/R-${EBVERSIONR}' >> ~/.Renviron

R will now use this path as default install path, ensuring you are always installing
your packages in the appropriate R library folder.

.. note::

   This configuration in ``~/.Renviron`` will also work in
   :ref:`Open OnDemand <ood>` apps such as :ref:`RStudio Server <rstudio-server>`.

The next step is to load the appropriate R module, run R and check ``libPaths()``:

.. code-block:: bash

   $ module load R/4.5.1-gfbf-2025a
   $ R
   R> .libPaths()
   [1] "/data/brussel/100/vsc10000/Rlibs/RL9/zen2/R-4.5.1"
   [2] "/apps/brussel/RL9/zen2-ib/software/R/4.5.1-gfbf-2025a/lib64/R/library"

From here, you can install packages with :ref:`install.packages
<r_package_management_install>` and it will use the well-defined location we
made for this environment.

You can also specify your desired library path as an extra argument in the
install command. This will take precedence over any environment variables or
default settings:

.. code-block:: r

   > Rlibs <- "/path/to/my/R_library"
   > install.packages("DEoptim", lib = Rlibs)

Alternatively you can manually download the sources of the desired R package
and install it from the command line with ``R CMD INSTALL`` and explicitly set
the location of the installation:

.. code-block:: console

   $ wget cran.r-project.org/src/contrib/Archive/DEoptim/DEoptim_2.0-0.tar.gz
   $ module load R/4.5.1-gfbf-2025a
   $ R CMD INSTALL DEoptim_2.0-0.tar.gz  -l ${VSC_DATA}/Rlibs/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}/R-${EBVERSIONR}

.. _r_package_management_conda:

R packages using Conda
----------------------

:ref:`conda_based_managers` provide an alternative solution to manage
self-contained environments of R packages. Such *Conda* environments can not
only have R packages but also packages in other languages. However, it is not
possible to combine *Conda* environments with software modules.

Creating a Conda environment for R
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Follow the guide in :ref:`conda_based_managers` to active some Conda
   distribution of your choice.

2. Create a new Conda environment including some version of R in it:

   .. code-block:: bash

      # search available R versions
      $ conda search -c conda-forge r-base
      # select one for your new Conda environment
      $ conda create -n science -c conda-forge r-base=<version> r-essentials

   This command creates a new Conda environment called ``science``, and installs
   your preferred R version from the conda-forge channel as well as the
   r-essentials bundle which includes number of commonly used R packages such as
   ``ggplot2``, ``glmnet``, ``dplyr``, ``tidyr``, and ``shiny``.

   .. note::

      A lot of bioconda and bioconductor packages are not in sync with their
      dependencies, therefore you may need to create a separate environment for
      each of those packages to avoid conflicts.

3. Activate the environment:

   .. code-block:: bash

      $ source activate science

   Where *science* is the name of the environment previously created.

4. You can now install an additional package (*e.g.* ``rodbc``)

   .. code-block:: bash

      $ conda install -c conda-forge r-rodbc

   Note that Conda will take care of all dependencies, including non-R
   libraries. This ensures that you work in a consistent environment.

5. Once all required packages are installed, you can launch R or run R scripts
   with the new packages.

.. seealso::

   For additional information on how to manage Conda environments, please check
   :ref:`conda_based_managers`.


