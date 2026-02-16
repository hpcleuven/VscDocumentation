.. _conda_based_managers:

Conda-based environment managers
================================

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment
manager which has become relatively popular for scientific software stacks.
With proper care, it can be used to install software yourself that you
want to run on HPC hardware.

.. warning::

   Using Conda is discouraged on the clusters at UAntwerpen, UGent,
   and VUB.

.. warning::

   As a rule, Conda packages cannot be used together with software that has
   been installed as a module.

Conda distributions
-------------------

The Conda approach has been implemented in different \`distributions',
of which the most common are:

* `Anaconda <https://www.anaconda.com/docs/getting-started/getting-started>`_
* `Miniconda <https://www.anaconda.com/docs/getting-started/miniconda/main>`_
* `Miniforge <https://conda-forge.org/download/>`_
* `Micromamba <https://mamba.readthedocs.io/>`_
* Conda packages can also be installed in `Pixi <https://pixi.prefix.dev/>`_
  environments

Barring any special requirements, we would recommend to use a centrally
installed ``Miniforge3`` module, for example:

.. code-block:: shell

   module load Miniforge3/25.3.0-3

This has the following advantages:

* The same base installation does not get duplicated by every user.
* You will not be able to add packages to the ``base`` environment,
  which is generally considered good practice.
* By default, Miniforge will only include the (unrestricted) ``conda-forge``
  community channel and not the default channels which are subject to
  :ref:`Anaconda's terms of service <conda_channels>`.

.. note::

   As you presumably know, loading modules in your startup source files
   :ref:`is to be avoided <module_system_basics>`. If you search a convenient
   way to enable Miniforge, consider adding an alias to your ``~/.bashrc``
   instead:

   .. code-block:: shell

      alias loadminiforge='module load Miniforge3/25.3.0-3'

The next paragraph will show how to get started with Miniforge, followed
by more advanced topics, including possible pitfalls and information on other
Conda distributions.

.. _conda_miniforge:

Getting started with Miniforge
------------------------------

Assuming you have loaded a ``Miniforge3`` module, you will first need to
configure the environment and package cache directories. Otherwise Miniforge
will use default locations in your ``$VSC_HOME``, which is clearly not ideal.
You will probably also want to shorten the prompt prefix. So a typical
configuration would proceed as follows:

.. code-block:: shell

   conda config --append envs_dirs $VSC_DATA/conda_envs
   conda config --append pkgs_dirs $VSC_SCRATCH/conda_pkgs
   conda config --set env_prompt '({name}) '

These commands only need to be executed once. You can verify their effect
using ``conda info`` or by inspecting the ``~/.condarc`` file.

Using Conda typically involves creating and activating a new Conda environment
followed by installing a set of Conda packages in it. Each environment
is self-contained, which allows to keep different software stacks isolated
from eachother. As a basic example with the *icecream* package:

.. code-block:: shell

   conda create --name mycondaenv
   source activate mycondaenv
   (mycondaenv) $ conda install icecream

Once the virtual environment is active, its name will be displayed in front
of the shell prompt (``(mycondaenv)`` in this example).

You can also ask for a specific package version. To install *tblite* version
*0.4.0*  for instance, the install command would be:

.. code-block:: shell

   (mycondaenv) $ conda install tblite=0.4.0

Once your work is finished, use ``conda deactivate`` to exit your Conda
environment:

.. code-block:: shell

   (mycondaenv) $ conda deactivate

Other typical Conda commands include:

.. code-block:: shell

   # List the available environments:
   conda env list
   # Remove an environment:
   conda env remove ...
   # List the packages installed in an environment:
   conda list
   # Search for available packages:
   conda search ...
   # Update one or several packages in an environment:
   conda update ...
   # Remove an installed package:
   conda remove ...
   # Empty the various caches (which can easily grow to tens of GBs):
   conda clean --all

.. _conda_channels:

Conda channels
--------------

Typical usage of ``conda install`` implies that Conda packages will
be downloaded from remote package repositories called 'channels', such as
`conda-forge <https://anaconda.org/conda-forge/>`_. Another popular community
channel is `bioconda <https://bioconda.github.io/>`_. Note that some other
channels of interest may not be used freely:

* The so-called `default
  <https://www.anaconda.com/docs/getting-started/working-with-conda/reference/default-channels>`_
  channels such as ``main`` and ``r`` are subject to `Anaconda's terms of service
  <https://www.anaconda.com/legal/terms/terms-of-service>`_, which include an
  EULA and the need for a paid subscription in certain contexts.
* The `intel channel
  <https://www.intel.com/content/www/us/en/developer/articles/technical/get-started-with-intel-distribution-for-python.html>`_
  can be worth looking into for optimal performance on Intel hardware.
  Using packages from this channel is subject to the EULA for Intel software.

Non-Conda packages
------------------

In principle you may try to install packages in a Conda environment
using tools other than ``conda install``, such as ``pip``. However, it is
`recommended to use conda install wherever possible
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-non-conda-packages>`_.

Microarchitectural optimizations
--------------------------------

``conda install`` will select Conda packages that have been precompiled for
the platform you are working on, i.e., the combination of the operating system
and CPU architecture. For all current VSC clusters the platform is ``linux-64``
(a Linux OS on ``x86-64`` CPUs).

It is important to note that Conda packages are primarily produced for
different CPU *architectures*. Whether a certain Conda package can make the
most of your CPU's *microarchitecture*, is therefore not guaranteed.
Conda packages built for the ``linux-64`` platform, for example, will often
only use 'baseline' instructions that are common to all ``x86-64`` CPUs.
Many numerical applications, however, can only achieve optimal performance
on modern CPUs by leveraging SIMD extensions such as AVX, AVX2 and AVX512.

We therefore encourage you to verify that performance-critical parts of your
Conda-based software stack display an appropriate level of microarchitectural
optimization:

* In certain dedicated numerical packages this is handled by the package
  itself through CPU detection and runtime dispatch, in which case you can
  normally expect good support for your microarchitecture. Examples of such
  packages are as OpenBLAS, Intel MKL, BLIS, NumPy, PyTorch and TensorFlow.

* Conda also supports `microarchitecture-optimized builds
  <https://conda-forge.org/docs/maintainer/knowledge_base/#microarch>`_,
  which is used by some Conda packages.

GPU acceleration
----------------

Conda packages may offer GPU acceleration `either as a compile-time or as a
run-time choice
<https://www.anaconda.com/docs/getting-started/working-with-conda/packages/gpu-packages#gpu-compatibility>`_
(if any). In the former case, make sure that Conda actually installs the
GPU-enabled version of the package and not the CPU-only version.

Conda packages built for NVIDIA GPUs will typically `rely on specific CUDA
versions <https://www.anaconda.com/docs/getting-started/working-with-conda/packages/gpu-packages#software-requirements>`_.
Keep in mind that newer CUDA versions also tend to require sufficiently recent
NVIDIA drivers. This should however rarely be an issue on the VSC clusters.

BLAS and LAPACK implementations
-------------------------------

If a Conda package depends on libraries such as BLAS or LAPACK,
then these will typically be provided by OpenBLAS. While this is a reasonable
default, you may want to verify the performance of other implementations.
Conda makes it fairly easy to `switch between BLAS/LAPACK implementations
<https://conda-forge.org/docs/maintainer/knowledge_base/#switching-blas-implementation>`_.

MPI programs
------------

Along the same lines, we recommend to verify the communication overhead in the
case of MPI applications. MPI binaries installed by Conda may for example
`lack features needed for optimal performance
<https://conda-forge.org/docs/user/tipsandtricks/#using-external-message-passing-interface-mpi-libraries>`_
or may in some cases be unable to initiate communication across different nodes.
If needed, switching between MPI implementations can be done in a similar way
as with BLAS, for example to change to Open MPI:

.. code-block:: shell

   conda install "mpi=*=openmpi*"

Storage requirements
--------------------

Be aware that Conda environments tend to grow rather large, both in terms of
disk usage and number of files (easily reaching several GB and tens of
thousands of files). :ref:`Containerizing your Conda environment
<conda_containers>` may help with the latter, though not with the former.

Exporting and importing environments
------------------------------------

You can use `conda export
<https://docs.conda.io/projects/conda/en/stable/commands/export.html>`_
to get an overview of installed packages (typically in YAML format),
which you may use to recreate the environment at a later point:

.. code-block:: shell

   # Exporting:
   (mycondaenv) $ conda export > mycondaenv.yaml

   # Importing:
   conda env create -f mycondaenv.yaml

You may of course also use this approach to recreate the environment
on a different machine (such as your local device). If that other machine
belongs to a different platform, however, you will need to use
``conda export --no-builds`` so that the platform-specific build strings
are not included. The same also applies if both platforms are the same
but one of the Conda packages is a microarchitecture-optimized build
that uses features that are not supported by the other machine's CPU.
A similar remark can be made regarding CUDA versions and NVIDIA drivers.

Micromamba
----------

If you need to install a Conda distribution yourself, we would suggest to
consider `Micromamba <https://mamba.readthedocs.io/>`_, as its installation
consists only of a single `micromamba` executable of small size.
Micromamba may also potentially be faster than Miniforge at solving package
dependencies and installing packages. We recommend the following installation
procedure:

1. Choose a folder to store the Micromamba binary in (here we will assume
   that it is ``$VSC_DATA/bin``). Make sure that the chosen folder
   is in your ``$PATH``.

2. Download the binary, skipping the configuration:

   .. code-block:: shell

      curl -fsSL https://micro.mamba.pm/install.sh | BIN_FOLDER=$VSC_DATA/bin INIT_YES=no sh

3. Finalize the configuration, for example:

   .. code-block:: shell

      micromamba config append envs_dirs $VSC_DATA/conda_envs
      micromamba config append pkgs_dirs $VSC_SCRATCH/conda_pkgs
      micromamba config set env_prompt '({name}) '

4. Create an alias to easily initialize Micromamba in your shell when needed:

   .. code-block:: shell

      # Add this to your ~/.bashrc file and restart your shell
      alias loadmicromamba='eval "$(micromamba shell hook -s posix)"'

Compared to Miniforge, using Micromamba mostly boils down to replacing
``conda ...`` with ``micromamba ...``, for example:

.. code-block:: shell

   loadmicromamba
   micromamba create --name mycondaenv
   micromamba activate mycondaenv
   (mycondaenv) $ micromamba install icecream
   (mycondaenv) $ micromamba deactivate

Pixi
----

`Pixi <https://pixi.prefix.dev/>`_ can be an interesting alternative
if you are looking for a `workspace-centric approach
<https://pixi.prefix.dev/latest/switching_from/conda/>`_. Furthermore,
in contrast to Conda environments, adding PyPI packages to Pixi environments
is fully supported.

.. warning::

   At the time of writing, Pixi `does not allow to install micro-architecture
   optimized Conda packages <https://github.com/prefix-dev/pixi/issues/5285>`_.

The Pixi installation itself also consists of a single executable plus
configuration:

1. Choose a folder to store the Pixi binary in (here we will assume
   that it is ``$VSC_DATA/bin``). Make sure that the chosen folder
   is in your ``$PATH``.

2. Download the binary:

   .. code-block:: shell

      curl -fsSL https://pixi.sh/install.sh | PIXI_HOME=$VSC_DATA sh

   This will have added ``export PATH="/data/xxxxx/xxx/vscxxxxx/bin:$PATH"``
   to the bottom of your ``~/.bashrc``.

3. Finalize the configuration:

   .. code-block:: shell

      # Add this to your ~/.bashrc file and restart your shell
      export PIXI_CACHE_DIR="$VSC_SCRATCH/pixi_cache"

In the basic example below, we will assume that you want to use a
``$VSC_SCRATCH/myworkspace`` folder as workspace, but that you want to store
the Pixi environments in ``$VSC_DATA/myworkspace_envs``.

.. code-block:: shell

   # Create the workspace
   mkdir $VSC_SCRATCH/myworkspace
   cd $VSC_SCRATCH/myworkspace
   pixi init .

   # Note that Pixi always expects you to execute workspace-related
   # Pixi commands from within the workspace (not from other directories)

   # Specify a different location for the Pixi environments
   pixi config set detached-environments $VSC_DATA/myworkspace_envs

   # Add a package to the default environment of the workspace
   pixi add icecream

   # To e.g. run some command that needs the default environment:
   pixi run python -c 'import icecream'

If needed, you can create additional environments for this workspace.
Pixi bundles the packages for such non-default environments together in
\`features'. If you for example want to add an environment which shares
dependencies with the default environment, but includes an additional
``tblite`` package, you could go about it as follows:

.. code-block:: shell

   pixi add --feature mylabel tblite
   pixi workspace environment add --feature mylabel mypixienv
   pixi install -e mypixienv

If you want to create a wholy independent environment instead,
add ``--no-default-feature`` to the ``pixi workspace environment add`` command.
To remove the newly created environment:

.. code-block:: shell

   pixi workspace environment remove mypixienv
   pixi clean

For more information, please check out the `Pixi documentation
<https://pixi.prefix.dev/latest/>`_.
