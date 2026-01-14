.. _Python packages:

Python package management
=========================

Introduction
------------

Python comes with an extensive standard library, and you are strongly
encouraged to use those packages as much as possible, since this will
ensure that your code can be run on any platform that supports Python.

However, many useful extensions to and libraries for Python come in the form of
packages that have to be installed separately. There are a few different supported
approaches to using and installing Python packages on the VSC clusters.

Since many Python packages have been made available through the module system,
using :ref:`python_packages_from_modules` is usually the best starting point.
Given the astounding number of packages, it is however not sustainable to
install each and every one system wide, so if you need a somewhat exotic
package and/or a specific version of a package that is not available, you will
need to install it yourself.

The recommended approach in that case is to
:ref:`manage a virtual environment with pip <venv_python>` or
alternatively to make use of :ref:`the uv package manager <uv_python>`.
In order to automate support for different (micro)architectures and facilitate
building environments on top of modules, the section introducing
:ref:`vsc-venv <vsc-venv_python>` is worth reading. Finally, you can also consider to
:ref:`conda for Python`.

.. _python_packages_from_modules:

Python packages from modules
----------------------------

Before attempting to install a Python package yourself, it is worth checking
if an appropriate version of the package is already installed on the cluster.
For ``numpy`` (a package commonly used in scientific computing), the search
query and example output look as follows:

.. code-block:: shell

   $ module spider numpy

   ----------------------
     numpy:
   ----------------------
     Versions:
        numpy/1.25.1 (E)
        numpy/1.26.4 (E)
        numpy/2.3.1 (E)
   ...
     For detailed information about a specific "numpy" package (including how
     to load the modules) use the modules full name. Note that names that
     have a trailing (E) are extensions provided by other modules. For
     example:

     $ module spider numpy/2.3.1

The trailing ``(E)`` after the listed versions indicates that there is no
module named ``numpy``, but instead it is provided as an
`extension <https://lmod.readthedocs.io/en/latest/330_extensions.html>`_ of
another module, which is quite common in the case of Python packages. To get
information on which module should be loaded in order to make a specific
version of ``numpy``  available, you can use:

.. code-block:: shell

   $ module spider numpy/2.3.1

   ------------------------
     numpy: numpy/2.3.1 (E)
   ------------------------
       This extension is provided by the following modules. To access the
       extension you must load one of the following modules. Note that any
       module names in parentheses show the module location in the software
       hierarchy.

          SciPy-bundle/2025.06-gfbf-2025a

This output tells us that the module ``SciPy-bundle/2025.06-gfbf-2025a`` has
to be loaded in order to make ``numpy/2.3.1`` available. The ``SciPy-bundle``
provides many packages needed for scientific computing.

To check which Python packages are currently available, you can execute::

 python3 -m pip list -v

It will list all packages that are installed for the Python distribution you
are using, which could include those installed by you.

.. _venv_python:

Managing Python virtual environments with pip
---------------------------------------------

In case the Python package you need is not available from a module, you need
to install it yourself and this can be done in a Python virtual environment or
venv. A `Python virtual environment <https://docs.python.org/3/tutorial/venv.html>`_
is an isolated environment in which you can safely install Python packages,
independent from those installed in the system or in other virtual environments.
For example, using virtual environments is very convenient for Python developers
as it allows working on multiple software projects at the same time.

It is recommended to use the software modules already installed in the cluster
as much as possible. They provide a robust and performant base to build your
virtual environments.

In this section, we show how you can combine modules with virtual environments
in the HPC to get the best of two worlds.

.. warning::

   Since Python is an interpreted language, pure Python code is independent of
   the :ref:`CPU microarchitecture <tier2 hardware>`, i.e., Python
   scripts are identical on each machine where they are installed. There is
   however a very important caveat: many scientific Python packages do their
   heavy computational lifting inside libraries written in a lower-level
   language (typically C, C++ or Fortran) and those libraries will typically
   target one or more specific (micro)architectures. As a consequence, installed Python
   packages **can** be different depending on the hardware on which they are
   installed. To make sure your installation works and gives good performance,
   we recommend to create a virtual environment on a node with the same
   (micro)architecture as the nodes where the virtual environment will be used. This
   is especially important for heterogeneous clusters, where (micro)architecture may
   differ across login nodes and cluster partitions. To get the (micro)architecture
   of the current node, you can use the ``$VSC_ARCH_LOCAL`` environment
   variable. If you need to use an environment on multiple (micro)architectures,
   create a separate one for each. :ref:`vsc-venv_python` can help with this.

#. Start by launching an interactive job (click :ref:`here <job_type_interactive>`
   when working on a Slurm cluster and :ref:`here <interactive jobs>` when
   working on a Torque cluster for more information) in the
   :ref:`cluster partition<slurm_partition>` of choice, for example in the
   *zen4* partition. Make sure to apply the options appropriate for the
   specific cluster you are working on.

   .. code-block:: shell

      srun --partition=zen4 --pty bash -l

#. Load a Python module as base of the virtual environment. Choose a Python
   version that is suitable for the additional Python packages that will be
   installed in the virtual environment:

   .. code-block:: shell

      module load Python/3.11.3-GCCcore-12.3.0

#. |Optional| Load other modules with additional Python packages:

   .. code-block:: shell

      module load SciPy-bundle/2023.07-gfbf-2023a

   The *Python* software modules in the HPC include a very limited list of
   Python packages, but many other modules are also available. A common
   software module is ``SciPy-bundle``, a bundle of data science packages such
   as ``numpy``, ``pandas``, and ``scipy``. Use the method discussed in
   :ref:`python_packages_from_modules` to search for packages you need as
   dependencies.

#. Create your virtual environment.

   .. warning::

      Avoid creating your virtual environments in your home directory. The
      :ref:`storage space of your home <storage hardware>` is very small and can
      quickly become filled up with installation files. Use a folder in your
      personal ``$VSC_SCRATCH`` or ``$VSC_DATA`` storage; or in your VO if you are
      part of one. Also take into account that a virtual environment typically
      contains many small files and parallel file systems are not suited to
      handle this well. If the large number of files becomes problematic, it
      is worthwhile to look into :ref:`containerizing <hpc containers>` your
      virtual environment.

   This example code block creates a new virtual environment in the
   *venv-zen4* directory. The *-zen4* suffix in the name is used to indicate
   the (micro)architecture on and for which (micro)architecture this environment was created.

   .. code-block:: shell

      python3 -m venv venv-zen4 --system-site-packages

   The option ``--system-site-packages`` ensures using the Python packages already
   available via the loaded modules instead of installing them in the virtual
   environment.

#. Before we can use the virtual environment, we must `activate` it:

   .. code-block:: shell

      source venv-zen4/bin/activate

   Once the virtual environment is active, its name will be displayed in front
   of the shell prompt (``(venv-zen4)`` in this example). Make sure to keep this
   virtual environment activated when executing the following steps.

#. We recommend to always upgrade ``pip`` to the latest version:

   .. code-block:: shell

      (venv-zen4) $ python3 -m pip install pip --upgrade

#. Now we can install additional Python packages inside the active virtual
   environment, for example the *icecream* package:

   .. code-block:: shell

      (venv-zen4) $ python3 -m pip install icecream --no-cache-dir --no-build-isolation

   The option ``--no-cache-dir`` ensures installing the most recent compatible
   versions of the dependencies, ignoring the versions available in your cache.

   The option ``--no-build-isolation`` ensures using the Cython compiler and other
   (build) dependencies from loaded modules instead of building in an isolated
   environment.

   It is possible to specify a specific version of package, for instance to
   install *tblite* version *0.4.0* the command becomes:

   .. code-block:: shell

      (venv-zen4) $ python3 -m pip install tblite==0.4.0 --no-cache-dir --no-build-isolation


#. Once your work is finished, use the command ``deactivate`` to deactivate your
   virtual environment:

   .. code-block:: shell

      (venv-zen4) $ deactivate

Reactivating your virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Whenever you want to go back to any of your virtual environments make sure to:

#. Launch an interactive job in the same partition you used when creating the
   virtual environment (or add the sbatch ``--partition`` option to your job
   script)::

    srun --partition=zen4 --pty bash -l

#. Load the same software modules that you used in the creation of the virtual
   environment::

    module load Python/3.11.3-GCCcore-12.3.0 SciPy-bundle/2023.07-gfbf-2023a

#. Reactivate the virtual environment::

    source venv-zen4/bin/activate

Recreating an environment
~~~~~~~~~~~~~~~~~~~~~~~~~

It is common that you want to recreate an environment, for instance to install
it for a different (micro)architecture or to allow other people to have exactly the
same package versions. This can be easily achieved by making use of
*pip list*, which produces a list of currently available packages and their
version:

.. code-block:: shell

   $ source venv-zen4/bin/activate
   (venv-zen4) $ python3 -m pip list --format=freeze
   ...
   icecream==2.1.8
   ...
   numpy==1.25.1
   ...

By saving the listed packages to a file::

 (venv-zen4) $ python3 -m pip list --format=freeze > requirements.txt

it becomes easy to recreate the environment, in the following example for
another (micro)architecture:

.. code-block:: shell

   $ srun --partition=zen5 --pty bash -l
   $ module load Python/3.11.3-GCCcore-12.3.0 SciPy-bundle/2023.07-gfbf-2023a
   $ python3 -m venv venv-zen5 --system-site-packages
   $ source venv-zen5/bin/activate
   (venv-zen5) $ python3 -m pip install -r requirements.txt

.. _vsc-venv_python:

The vsc-venv utility
--------------------

As discussed earlier, it is recommended to create separate Python virtual
environments for separate architectures. Together with the fact that exactly
the same modules that were used during the environment creation need to be
loaded whenever the environment is used, managing Python virtual environments
on VSC clusters can become tedious. This is where the ``vsc-venv`` script
comes to the rescue: it encapsulates the creation and management of Python
virtual environments and avoids multiple issues with the default ``venv``
included in Python. The ``vsc-venv`` command manages multiple virtual
environments for different clusters in a transparent way, while guaranteeing
the same module environment.

Usage
~~~~~

A virtual environment can be activated by running the following command:

.. code-block:: shell

   $ module load vsc-venv
   $ source vsc-venv --activate --requirements requirements.txt [--modules modules.txt]

Here, ``requirements.txt`` is the path to a file containing the Python
dependencies to install in the virtual environment. For more information on
the ``requirements.txt`` file, see the `pip documentation <https://pip.pypa.io/en/stable/reference/requirements-file-format/>`_
The optional ``--modules`` option can be used to provide a ``modules.txt`` file
that lists the modules to load before activating the virtual environment.

Automatically, the modules are loaded and the environment is activated.
When running this command for the first time, the dependencies from the
requirements file are installed.

Now, the software can be run and Python packages installed in the virtual
environment can be used, along with software provided via centrally
installed modules.

You can get insights on the current environment using the following commands:

.. code-block:: shell

   $ python --version    # Python version
   $ pip list            # List of installed Python packages
   $ module list         # List of loaded modules

To deactivate the virtual environment, run:

.. code-block:: shell

   $ source vsc-venv --deactivate

Example
~~~~~~~

For this example, it is assumed the following files are present in the current
directory:

**modules.txt:**

.. code-block:: shell

   SciPy-bundle/2023.11-gfbf-2023b
   Pillow/10.2.0-GCCcore-13.2.0

and **requirements.txt:**

.. code-block:: shell

   beautifulsoup4==4.12.3

We run the following commands create and activate the environment:

.. code-block:: shell

   $ module load vsc-venv
   $ source vsc-venv --activate --requirements requirements.txt --modules modules.txt

As this creates the virtual environment for the first time, a ``venvs``
subdirectory is created in the current directory. Within ``venvs/``, an
additional subdirectory is created for the virtual environment:
for example ``venv-RHEL8-zen2`` (note that the name will depend on the type of node
you are working on, it is automatically determined based on environment
variables like ``$VSC_ARCH_LOCAL`` and ``$VSC_OS_LOCAL``).

Now, Python 3.12 is loaded and the ``numpy`` (provided by the ``SciPy-bundle``
module), ``PIL`` (provided by the ``Pillow`` module), and ``bs4`` Python
packages can be used.

To deactivate the virtual environment, run:

.. code-block:: shell

   $ source vsc-venv --deactivate

If we want to create a virtual environment for another (micro)architecture, simply
repeat the steps above on a node of that (micro)architecture. After this, the
``venvs`` directory will contain an additional subdirectory with the virtual
environment for the new (micro)architecture.

.. _uv_python:

uv as Python package manager
----------------------------

The discussion thus far made use of *pip* as the package manager, but there
other options available. This section will in particular show how
`uv <https://docs.astral.sh/uv/>`_ (an extremely fast Python package and
project manager written in Rust) can be used. Some advantages of uv over pip
are that it can resolve dependencies much faster and that it can provide any
desired Python version (whereas pip relies on existing Python installations).

The first step is getting uv itself, which usually can be done conveniently
on the cluster by loading a module, for instance::

 $ module load uv/0.4.20-GCCcore-13.3.0

uv provides a so-called `pip interface <https://docs.astral.sh/uv/pip/>`_,
which makes it very easy to use uv if you are familiar with pip. For instance
to create a virtual environment with uv similar to the one discussed in a
:ref:`previous section <venv_python>`, you can use the following commands:

.. code-block:: shell

   $ uv venv venv-zen4 --python 3.11
   $ source venv-zen4/bin/activate
   $ uv pip install icecream --no-cache-dir --no-build-isolation
   $ deactivate

Most of the remarks and warnings from before apply to uv as
well. For more specific uv information, please consult the
`uv documentation pages <https://docs.astral.sh/uv>`_
