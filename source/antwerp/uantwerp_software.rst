.. _UAntwerp software:

##############################
UAntwerp software instructions
##############################

********************************
Searching for installed software
********************************

After logging in, the ``calcua/all`` module will be loaded automatically.
This will let you search through all (centrally) installed software using the
``module`` command's search capabilities.

|Recommended| Once you have found the specific software module you would like
to use, load the corresponding version-specific ``calcua`` module.
This will also restrict your next searches and module loads to modules in the same
version of the software stack, which avoids compatibility errors.

|Example| Loading a module
  To load the GCC module, you can execute the following commands.

  .. code-block:: bash

     module purge

     module load calcua/2023a
     module load GCC/12.3.0

There are three commands to search for a module:

* Search in the list of activated modules
   Activated modules are modules that can be loaded without first
   loading another ``calcua`` module.

   .. code-block:: bash

      module av Python

   will search for an activated module whose name or version string contains ``Python``.

* Search in the list of all available modules
   This  search also includes modules that require loading other
   modules first.

   .. code-block:: bash

      module spider Python

   If you need more information about the module, including which modules you might need to load,
   you can also use ``module spider`` using a specific module version.

   The explanation given about the module(s) that need to be loaded,
   can be a bit confusing. You have to take only one line from the output and load
   all modules on that line.

   |Example| Using ``module spider`` with a version
     If you want more specific information on ``Python/3.11.3-GCCcore-12.3.0``,
     you can use

     .. code-block:: bash

        $ module spider Python 3.11.3-GCCcore-12.3.0
          -----------------------------------------------------------------
          Python: Python/3.11.3-GCCcore-12.3.0
          -----------------------------------------------------------------
            Description:
              Python is a programming language that lets you work more
              quickly and integrate your systems more effectively.


            You will need to load all module(s) on any one of the lines below
            before the "Python/3.11.3-GCCcore-12.3.0" module is available to load.

              calcua/2023a
              calcua/all

     In this case, it suffices to first load either ``calcua/2023a``,
     or ``calcua/all``: it is not required to load both.

* Search through the whatis-information
   Each module also contains a limited amount of additional information that can be shown with
   the ``module whatis`` command, e.g.

   .. code-block:: bash

      module whatis Python/3.11.3-GCCcore-12.3.0

   You can search through this 'whatis'-information of installed modules using ``module keyword``

   .. code-block:: bash

      module keyword CMake

If you did not find the software you want to use, please do not hesitate to contact
the UAntwerp support team at hpc@uantwerpen.be.

****************************
Installing your own software
****************************

Installation directories
========================

Additional packages or software distributions should be installed
on VSC_DATA or VSC_SCRATCH, depending on the circumstances.

* |UA| **Users with a vsc2xxxx account**

  When working on the UAntwerp clusters, VSC_DATA is a local file
  system for you. We expect that for :ref:`Python <Python packages>` packages
  (and similarly for :ref:`R <R_package_management>` and :ref:`Perl <Perl packages>`),
  **VSC_DATA** will give better performance than VSC_SCRATCH due to the amount of file
  metadata accesses that occur when running Python.

  |Example| To install the ``sphinx`` Python package, you can use the following command

  .. code-block:: bash

     pip install --prefix=${VSC_DATA}/python_lib sphinx

* |VUB| |UG| |KUL| **Users with a different home institution**

  VSC_DATA is a file system at your local
  institution. Due to the distance between our clusters and your home institution, file access to
  VSC_DATA will have a high latency.

  Installing the packages that you need locally on **VSC_SCRATCH**
  will give much better performance.

Easybuild
=========

TODO ``init-easybuild-user.sh``


Python packages
===============

The preferred method of installing additional Python packages on the UAntwerp cluster is using ``pip``, ``easy_install``
or ``python setup``, depending on what the package supports. This does require that all non-Python and in
some cases Python dependencies are already installed. However, it makes maximum use of what is already
installed on the systems, with a minimal number of additional files.

.. seealso::
  For more detailed instructions on how to install additional python packages using ``pip``, see :ref:`python packages`.

.. warning::
  Like with Conda, when you install from binaries available on
  `PyPi <https://pypi.org/>`_, they will likely not be optimized for the specific CPUs on our system.
  Moreover, not all binary wheels are compatible with the Linux version that we use. The CalcUA support team
  always tries to compile packages from source using up-to-date compilers and only uses binary wheels when
  nothing else works in a reasonable time.

Conda
=====

We discourage the use of Conda-variants for various reasons. It should only be used if nothing else works.

* Conda installations avoid using libraries already present on the system, effectively installing their own
  Linux distribution in the Conda directories. As such they consume **a lot
  of disk space** and can put a high load on the file system. Expect slower performance just because of that
  already.
* As Conda effectively installs its own upper layers of a Linux/GNU-system and doesn't use security-sensitive
  libraries from our system, it is **up to you to keep it secure** by frequently updating. This is particularly
  important for those packages that make connections of the internet. If you're not using any of these, this
  does not need to be a big concern.
* The Conda repositories contain a mix of very well optimized binary packages and packages that are **not
  optimized** for modern CPUs. In some cases, multiple versions are available, but as a Conda user you need to be
  well aware of where to find these. As an example, the Intel Python distribution with properly optimized NumPy, SciPy and
  a few other performance-critical packages is also available via Conda.

  The generic CPU that is used for
  binaries that should run on everything is usually an ancient Pentium 4 or Core CPU. For some code, e.g.,
  dense linear algebra and FFT, using the newer instructions of more recent processors can give a big speed
  boost for those routines, up to a factor 4 on Leibniz and Vaughan and up to a factor of 7 or so on the
  Skylake partition of the previous Tier-1 cluster BrENIAC.

If you do need to use conda, you should wrap it in a container. This way we can at least mitigate the stress on the 
filesystem of a standard conda installation due to the creation of many small files.

`hpc_container_wrapper <https://github.com/CSCfi/hpc-container-wrapper>`_ is a tool that helps you create an 
Apptainer image and provide wrapper scripts to call executables within the container environment. To containerize 
your conda environment with ``hpc_container_wrapper``, you need your conda environment file ``environment.yaml``. 
This is a reproducible collection of packages, dependencies, and channels. Here is an example of such a file:

.. code-block :: bash

    # environment.yaml
    name: bsoup4
    channels:
      - conda-forge
    dependencies:
      - beautifulsoup4
      - ...

To create the container in the directory ``$VSC_SCRATCH/bsoup``:

.. code-block :: bash
    
    $ module load hpc-container-wrapper
    $ conda-containerize new --prefix "$VSC_SCRATCH/containers/bsoup" environment.yaml

You can now use your containerized installation by prepending your path:

.. code-block :: bash
    
    $ export PATH="$VSC_SCRATCH/containers/bsoup/bin:$PATH"
    $ which python
     $VSC_SCRATCH/bsoup/bin/python

If you still miss packages, you can update the container with a post-install script:

.. code-block :: bash

    $ echo 'conda install -c bioconda pyfaidx' > post.sh
    $ conda-containerize update --post-install  post.sh "$VSC_SCRATCH/containers/bsoup"

.. seealso::
  For the general use of `Apptainer`_ (without hpc_container_wrapper), see :ref:`hpc containers`.
