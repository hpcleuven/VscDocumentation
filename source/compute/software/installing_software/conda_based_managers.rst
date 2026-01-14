.. _conda_based_managers:

Conda-based environment managers
================================

TODO-GSSI

.. _conda for Python:

Install Python packages using conda
-----------------------------------

.. note::

    Conda packages are incompatible with the software modules.
    Usage of conda is discouraged in the clusters at UAntwerpen, UGent,
    and VUB.

The easiest way to install and manage your own Python environment is
conda.  Using conda has some major advantages.

-  You can create project-specific environments that can be shared with
   others and (up to a point) across platforms.  This makes it easier to
   ensure that your experiments are reproducible.
-  conda takes care of the dependencies, up to the level of system libraries.
   This makes it very easy to install packages.

However, this last advantage is also a potential drawback: you have to
review the libraries that conda installs because they may not have
been optimized for the hardware you are using.  For linear algebra, conda
will typically use Intel MKL runtime libraries, giving you performance that
is on par with the Python modules for `numpy` and `scipy`.

However, care has to be taken in a number of situations.  When you require
``mpi4py``, conda will typically use a library that is not configured and
optimized for the networks used in our clusters, and the performance impact
is quite severe.  Another example is TensorFlow when running on CPUs, the
default package is not optimized for the CPUs in our infrastructure, and will
run sub-optimally.  (Note that this is not the case when you run TensorFlow on
GPUs, since conda will install the appropriate CUDA libraries.)

These issues can be avoided by using the `Intel oneAPI Python Distribution`_
that contains `Intel MPI`_ and optimized versions of packages such as
scikit-learn and TensorFlow.

.. _install_miniconda_python:

Install Miniconda
~~~~~~~~~~~~~~~~~

If you have Miniconda already installed, you can skip ahead to the next
section, if Miniconda is not installed, we start with that. Download the
Bash script that will install it from `conda.io <https://conda.io/>`_
using, e.g., ``wget``::

   $ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

Once downloaded, run the installation script::

   $ bash Miniconda3-latest-Linux-x86_64.sh -b -p $VSC_DATA/miniconda3

.. warning::

   It is important to use ``$VSC_DATA`` to store your conda installation
   since environments tend to be large, and your quota in ``$VSC_HOME``
   would be exceeded soon.

Optionally, you can add the path to the Miniconda installation to the
``PATH`` environment variable in your ``.bashrc`` file. This is convenient, but
may lead to conflicts when working with the module system, so make sure
that you know what you are doing in either case. The line to add to your
``.bashrc`` file would be::

   export PATH="${VSC_DATA}/miniconda3/bin:${PATH}"

.. _create_python_conda_env:

Create an environment
~~~~~~~~~~~~~~~~~~~~~

First, ensure that the Miniconda installation is in your PATH
environment variable. The following command should return the full path
to the conda command::

   $ which conda

If the result is blank, or reports that conda can not be found, modify
the ``PATH`` environment variable appropriately by adding Miniconda's ``bin``
directory to ``PATH``.

You can create an environment based on the default conda channels, but
it is recommended to at least consider the Intel Python distribution.

Intel provides instructions on how to install the `Intel oneAPI Python
Distribution`_ with conda.

Alternatively, you can create a new conda environment based on the default
channels::

   $ conda create  -n science  numpy scipy matplotlib

This command creates a new conda environment called science, and
installs a number of Python packages that you will probably want to have
handy in any case to preprocess, visualize, or postprocess your data.
You can of course install more, depending on your requirements and
personal taste.

This will default to the latest Python 3 version, if you need a specific
version, e.g., Python 2.7.x, this can be specified as follows::

   $ conda create -n science  python=2.7  numpy scipy matplotlib


Work with the environment
~~~~~~~~~~~~~~~~~~~~~~~~~

To work with an environment, you have to activate it. This is done with,
e.g.,

::

   $ source activate science

Here, ``science`` is the name of the environment you want to work in.


Install an additional package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install an additional package, e.g., \`pandas`, first ensure that the
environment you want to work in is activated.

::

   $ source activate science

Next, install the package::

   $ conda install tensorflow-gpu

Note that conda will take care of all dependencies, including
non-Python libraries (e.g., cuDNN and CUDA for the example above). This
ensures that you work in a consistent environment.


Update/remove a package
~~~~~~~~~~~~~~~~~~~~~~~

Using conda, it is easy to keep your packages up-to-date. Updating a
single package (and its dependencies) can be done using::

   $ conda update pandas

Updating all packages in the environment is trivial::

   $ conda update --all

Removing an installed package::

   $ conda remove tensorflow-gpu


Deactivate an environment
~~~~~~~~~~~~~~~~~~~~~~~~~

To deactivate a conda environment, i.e., return the shell to its
original state, use the following command::

   $ source deactivate


More information
~~~~~~~~~~~~~~~~

Additional information about conda can be found on its `documentation
site <https://docs.conda.io/en/latest/>`_.
