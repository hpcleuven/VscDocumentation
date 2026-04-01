.. _hpc containers:

######################
Containers (Apptainer)
######################

Introduction
============

What are containers?
--------------------

Containers provide a way to package software together with all required
dependencies so it can run in a reproducible environment.  Containers use OS
virtualization to isolate processes and control their access to system
resources.  A **container** is stored in a container **image**, which is simply
a set of files that defines the runtime environment. A container image contains
the applications, libraries, and runtime environment, while the host system
provides the kernel.

Why Apptainer?
--------------

The best-known container implementation is `Docker`_. However, Docker
typically requires root privileges, which introduces security concerns
on shared HPC systems. For this reason, Docker is generally not available
on HPC clusters.

`Apptainer`_ (formerly Singularity) provides a container solution designed
specifically for HPC environments. Containers can be executed by regular users
and integrate well with cluster resources such as shared filesystems, GPUs, and
high-performance networks.

Advantages of Apptainer:

* Containers can be executed without root privileges.
* Images are stored as a single portable and immutable file (SIF format).
* Integration with HPC resources such as GPUs, networks, and filesystems.
* Compatibility with Docker/OCI container images.
* Reproducible and verifiable images through immutable builds and
  optional image signing.

Apptainer can run containers built with Docker, and it can also build
container images on top of base Docker images.

When should I use containers?
-----------------------------

If the software you want to use is already available on the HPC system as a
:ref:`module <module_system_basics>`, it is usually preferable to use the
provided installation. HPC software is often compiled specifically for the
hardware and may offer better performance. Containers are particularly useful
in the following situations:

* Quickly testing a containerized application before starting a
  performance-optimized installation.
* Running software that is difficult to install on HPC systems.
* Using legacy applications that require outdated dependencies.
* Ensuring reproducibility of a workflow developed elsewhere.
* Running software built for a different (version of a) Linux distribution.
* Creating portable workflows that can run both on HPC systems and
  cloud platforms.
* Reducing the number of files (inodes) by packaging software into a single
  container image.

Limitations of containers
-------------------------

Containers are not always the best solution. Potential drawbacks include:

* Interaction with software outside the container can be difficult or
  infeasible (e.g. environment modules, Open OnDemand).
* MPI-based applications require compatible MPI libraries between the host
  and the container.
* To maximize portability, containers are often built for generic CPU
  architectures, which may reduce performance compared to optimized HPC builds.
* Containers built for one CPU architecture (e.g. x86-64, Intel/AMD CPUs) cannot run on
  another architecture (e.g. AArch64, Arm CPUs).
* :ref:`Security risks <apptainer_pulling_images>` arise when you don’t know
  who created a container image or exactly what software is inside it.

.. _apptainer_vsc_clusters:

Apptainer on VSC clusters
=========================

Users can both :ref:`run <apptainer_running>` and :ref:`build
<apptainer_building>` Apptainer containers on the VSC clusters.

Before starting, it is important to set environment variables for the Apptainer
cache and temporary directories. We recommend adding the following code snippet
to your ``~/.bashrc`` so these are set automatically:

.. code-block:: bash

    export APPTAINER_CACHEDIR=/tmp/$USER/apptainer_cachedir
    export APPTAINER_TMPDIR=/tmp/$USER/apptainer_tmpdir
    mkdir -p $APPTAINER_TMPDIR

``APPTAINER_CACHEDIR`` stores data that can be reused across Apptainer runs
(layers, images), while ``APPTAINER_TMPDIR`` is a temporary workspace for Apptainer.

.. note::

   Make sure to always build and/or run your containers on a compute node with
   enough available RAM memory.

   Also, images tend to be very large, so store them in a directory
   where you have sufficient quota, e.g. ``$VSC_DATA``.

.. _apptainer_pulling_images:

Pulling Apptainer images
========================

Apptainer can download or pull images directly from several sources.  However,
it is important to understand where the image comes from and what it contains.
Questions to consider include:

* Which software versions are included?
* How was the software built and configured?
* Is the source of the container trustworthy?

When pulling images from public registries such as Docker Hub, it is
recommended to use images from verified publishers whenever possible.
Here is a list of some well-known public registries:

.. list-table:: Public Container Registries
   :widths: 40 60
   :header-rows: 1

   * - Container Registry
     - URI Prefix
   * - `Docker Hub <https://hub.docker.com/>`_
     - ``docker://``
   * - `NVIDIA Container Registry <https://catalog.ngc.nvidia.com/>`_
     - ``docker://nvcr.io/nvidia``
   * - `AMD Infinity Hub <https://www.amd.com/en/developer/resources/infinity-hub.html>`_
     - ``docker://rocm``
   * - `GitHub Container Registry <https://docs.github.com/packages/working-with-a-github-packages-registry/working-with-the-container-registry>`_
     - ``docker://ghcr.io``

The following example pulls an Ubuntu image from Docker Hub and saves it as an
immutable Apptainer SIF image that can be executed on the cluster:

.. code-block:: bash

   apptainer pull ubuntu-24.04.sif docker://ubuntu:24.04

Using Apptainer containers
==========================

Container startup behavior
--------------------------

Containers can be executed in several ways:

.. list-table:: Apptainer Primary Commands
   :widths: 30 70
   :header-rows: 1

   * - Command
     - Action
   * - ``apptainer shell``
     - Start an interactive shell inside the container
   * - ``apptainer exec``
     - Execute a command inside the container
   * - ``apptainer run``
     - Run the container using its ``runscript``

Containers contain startup scripts that define their environment and behavior:

Environment scripts
  * located inside the container at ``/.singularity.d/env/``
  * always executed: ``apptainer shell``, ``apptainer exec``, ``apptainer run``

Container runscript
  * located inside the container at ``/.singularity.d/runscript``
  * only executed when using ``apptainer run``

If the last line of the ``runscript`` contains ``exec "$@"`` (or equivalent), we
can also use ``apptainer run`` to execute a command inside the container, which
will execute after the runscript has run.

Inspecting containers
---------------------

We can inspect the metadata and configuration of a container image with ``apptainer
inspect``:

.. code-block:: bash

   # inspect labels
   apptainer inspect ubuntu-24.04.sif
   # inspect runscript
   apptainer inspect --runscript ubuntu-24.04.sif
   # inspect environment
   apptainer inspect --environment ubuntu-24.04.sif

.. _apptainer_running:

Running commands in a container
-------------------------------

* Executing a command inside a container can be done with ``apptainer exec``:

.. code-block:: bash

   apptainer exec ubuntu-24.04.sif <command>
   # or (if the runscript supports it)
   apptainer run ubuntu-24.04.sif <command>

   # example: get info about the container OS
   apptainer exec ubuntu-24.04.sif cat /etc/lsb-release

* Starting an interactive shell inside the container can be done with
  ``apptainer shell``.  When inside the container, the prompt changes to
  ``Apptainer>``, indicating that the container shell is ready to accept
  commands:

.. code-block:: bash

   apptainer shell ubuntu-24.04.sif
   Apptainer>

Bind mounts
-----------

By default, the user's home directory and the current working directory are
bind-mounted so they can be accessed from inside the container.  Additional
host directories can be mounted using the ``--bind`` or ``-B`` option.  For
example, to mount the ``$VSC_SCRATCH`` directory:

.. code-block:: bash

   apptainer exec -B $VSC_SCRATCH ubuntu-24.04.sif <command>

If needed, we can specify a different path inside the container. For example, to
mount ``$VSC_SCRATCH`` as ``/scratch``:

.. code-block:: bash

   apptainer exec -B $VSC_SCRATCH:/scratch ubuntu-24.04.sif <command>

VSC sites may have enabled additional default mount points, so you don't always
have to add them yourself. We can use the following command to see which paths
are currently mounted inside the container:

.. code-block:: bash

   apptainer exec ubuntu-24.04.sif findmnt -no TARGET

.. _apptainer_environment_variables:

Environment variables
---------------------

Environment variables defined on the host are automatically passed
into the container (exceptions: ``$PATH`` and ``$LD_LIBRARY_PATH``). The example
below shows that ``$MY_VAR`` is defined inside the container:

.. code-block:: bash

   export MY_VAR=my_value
   apptainer run ubuntu-24.04.sif bash -c 'echo $MY_VAR'  # prints my_value

If needed, we can set a different value inside the container using either the
``$APPTAINERENV_***`` environment variable or the ``--env`` option:

.. code-block:: bash

   APPTAINERENV_MY_VAR=other_value apptainer run ubuntu-24.04.sif bash -c 'echo $MY_VAR'  # prints other_value
   # or:
   apptainer run ubuntu-24.04.sif --env MY_VAR=other_value bash -c 'echo $MY_VAR'  # prints other_value

Running containers in a job
---------------------------

Apptainer containers can be part of any workflow. The following job script runs
an example `tblite script
<https://github.com/vscentrum/gssi-training/blob/main/tblite/demoscripts/tblite-single-point-GFN2-xTB.py>`_
with a ``tblite`` image that was created from an :ref:`Apptainer definition
file <apptainer_build_definition_file>`:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --ntasks=1
   #SBATCH --time=30:00

   apptainer run tblite-0.4.0.sif python tblite-single-point-GFN2-xTB.py

Ensure that the container has access to all the required directories
by providing additional bindings if necessary.

Common issues with Docker images
--------------------------------

Although compatibility with Docker is high, users may experience
`issues when running Docker images with Apptainer
<https://apptainer.org/docs/user/latest/docker_and_oci.html#differences-and-limitations-vs-docker>`_.
Below are some common problems and their possible workarounds:

Applications trying to write inside the image
   Apptainer images are immutable, so writing to a directory inside the image
   will fail. There are two ways to work around this:

   * Copy or move the directory from the image to the host, and bind-mount the
     copied directory back into the container:

   .. code-block:: bash

      apptainer run --bind <host-dir>:<container-dir>

   * Use a temporary overlay which will be discarded on exit:

   .. code-block:: bash

      apptainer run --writable-tmpfs

Interference from the host environment
   Environment variables such as ``$PYTHONPATH`` may interfere with container
   software. To avoid this, users can either :ref:`override specific environment variables
   <apptainer_environment_variables>`, or run the container with a clean
   environment:

   .. code-block:: bash

      apptainer run --cleanenv

Default bind mounts
   Apptainer automatically binds directories such as ``$HOME`` into the
   container. In some cases, an application expects to find specific files installed in
   those directories inside the container, which it cannot access due to the mount. To avoid
   this, we can disable binding the home directory or disable
   all default binds and manually bind only what is needed:

   .. code-block:: bash

      apptainer run --no-home
      # or
      apptainer run --contain --bind <dir1> --bind <dir2>

Processes expecting root privileges
   Some Docker images assume that applications run as root. Apptainer provides
   a ``--fakeroot`` option that can help in these situations:

   .. code-block:: bash

      apptainer run --fakeroot

.. _apptainer_building:

Building Apptainer containers
=============================

Containers can be built in several ways:

* :ref:`interactively from a base image <apptainer_build_interactive>`
* :ref:`from an Apptainer definition file <apptainer_build_definition_file>`
* :ref:`from a Docker image via a Dockerfile <apptainer_build_dockerfile>`
* using :ref:`hpc-container-wrapper <apptainer_hpc-container-wrapper>`
* using remote build services

Many containers can be built on the VSC clusters without root privileges
using the ``--fakeroot`` build option. However, due to `inherent limitations of
fakeroot
<https://apptainer.org/docs/user/latest/fakeroot.html#restrictions-security>`_,
some containers may fail to build. In that case, you can build the
image on a local machine where you have root privileges. Apptainer only runs
under Linux, so you’ll need to use a virtual machine when using Windows (e.g.
WSL) or macOS.  For detailed instructions, see the `Apptainer Quick Start`_
guide.  Once your image is built, you can :ref:`transfer <data transfer>` it to
the VSC infrastructure.

Alternatively, you can use remote build services to build your images. The
:ref:`sylabs_remote_builder` builds images from a user-provided definition
file. The `Seqera platform <https://seqera.io/containers>`_ allows to simply
select any Conda or python packages to be built into an image.

In the following sections, we will build the `tblite
<https://tblite.readthedocs.io>`_ software package with Python bindings on the VSC
clusters. Before starting, ensure you have set the required environment
variables as explained in the :ref:`apptainer_vsc_clusters` section.

.. _apptainer_build_interactive:

Building interactively from base image
--------------------------------------

#. Download a base image and store it as a sandbox.
   A sandbox is a writable container directory structure. The following example
   creates a directory called ``my_sandbox`` and installs an Ubuntu container
   image in it:

   .. code-block:: bash

      apptainer build --sandbox my_sandbox docker://ubuntu:24.04

#. Start an interactive shell in the container.
   The ``--fakeroot`` option is required when building as non-root user on the
   VSC clusters. Inside the container, the ``my_sandbox`` directory becomes the root directory
   (``/``).  We can now make changes, such as installing packages:

   .. code-block:: bash

      apptainer shell --writable --fakeroot my_sandbox
      Apptainer> apt-get update && apt-get install python3
      Apptainer> exit  # exit the container

#. Make changes from the host.
   From the host, we can also make changes by traversing the sandbox directory
   structure (e.g. updating the ``runscript``):

   .. code-block:: bash

      nano my_sandbox/.singularity.d/runscript

#. Create immutable SIF image from sandbox.
   When we’re finished making changes, we can convert the sandbox to a SIF
   image:

   .. code-block:: bash

      apptainer build my_image.sif my_sandbox

.. _apptainer_build_definition_file:

Building from Apptainer definition file
---------------------------------------

For reproducibility, containers should ideally be built from `Apptainer
Definition Files`_. A definition file specifies the base image and the commands
required to build the container. See also the
:ref:`example_apptainer_definition_files` section.

Another advantage of definition files is that they can be shared easily.

.. note::

   A definition file does not guarantee reproducibility by itself. It is
   important to specify the exact versions for the base container and any
   installed software packages. Additionally, downloading files during
   installation risks breaking reproducibility if those external resources
   become unavailable.

In the example below, we’ll create a container for tblite. The definition file
can be found in the *gssi-training* repo at `tblite-0.4.0.def
<https://github.com/vscentrum/gssi-training/blob/main/tblite/building_apptainer_containers/apptainer_definition_file/tblite-0.4.0.def>`_.

#. Create or download Apptainer definition file.

#. Create Apptainer image from the definition file.
   We can create the image in one step, or in two steps via a sandbox to verify
   the container before finalizing the SIF image file:

   .. code-block:: bash

      # option1: in one step
      apptainer build --fakeroot tblite-0.4.0.sif tblite-0.4.0.def

      # option2: in two steps via sandbox
      apptainer build --fakeroot --sandbox my_sandbox tblite-0.4.0.def
      apptainer build tblite-0.4.0.sif my_sandbox

.. _apptainer_build_dockerfile:

Building from Docker image via Dockerfile
-----------------------------------------

Users familiar with `Dockerfiles
<https://docs.docker.com/build/concepts/dockerfile/>`_ can create a Docker
image from a Dockerfile and then convert it to Apptainer. This method requires
a machine with Docker (and root privileges) or Podman.  Windows users can use
WSL.

#. Write Dockerfile

#. Create Docker image from the Dockerfile

   .. code-block:: bash

      sudo docker build . -t my_docker_image

#. Create Docker archive from Docker image

   .. code-block:: bash

      sudo docker save my_docker_image -o my_docker_archive.tar
      sudo chown $USER:$USER my_docker_archive.tar

#. Create Apptainer image from Docker archive
   We can create the image in one step, or in two steps via a sandbox to verify
   the container before finalizing the SIF image file:

   .. code-block:: bash

      # option1: in one step
      apptainer build my_image.sif docker-archive:my_docker_archive.tar

      # option2: in two steps via sandbox
      apptainer build --sandbox my_sandbox docker-archive:my_docker_archive.tar
      apptainer build my_image.sif my_sandbox

.. _apptainer_hpc-container-wrapper:

Building with hpc-container-wrapper
-----------------------------------

`hpc-container-wrapper <https://github.com/CSCfi/hpc-container-wrapper>`_ is a
tool that automates the creation of an Apptainer image and provides wrapper scripts to
call executables within the container environment. It supports building both
Conda and Pip packages.

In the example below, we’ll create a container for ``tblite`` with conda.

#. Create Conda environment file ``environment.yml``:

   .. code-block:: yaml

      # environment.yaml
      name: tblite
      channels:
      - conda-forge
      dependencies:
      - tblite-python=0.4.0

#. Load ``hpc-container-wrapper`` environment module:

   .. code-block:: bash

      module load hpc-container-wrapper/<VERSION>

#. Create Apptainer container and wrappers in new ``tblite-0.4.0`` directory:

   .. code-block:: bash

      conda-containerize new --prefix tblite-0.4.0 environment.yml

Example wrappers usage

.. code-block:: bash

   # Add path to bin directory to $PATH
   export PATH="$PWD/tblite-0.4.0/bin:$PATH"

   # Verify that tblite and python executables from the image are used
   which tblite
     $PWD/tblite-0.4.0/bin/tblite
   which python
     $PWD/tblite-0.4.0/bin/python

   # Verify that tblite python package from image is used
   python -c 'import tblite; print(tblite.__file__)'
     /LOCAL_TYKKY_QcubNaZ/miniforge/envs/env1/lib/python3.13/site-packages/tblite/__init__.py

If needed, we can also update an image created with ``hpc-container-wrapper``.
The following example adds the ``beautifulsoup4`` conda package:

#. Write ``update.sh`` script:

   .. code-block:: bash

      # update.sh
      conda install -c conda-forge beautifulsoup4

#. Update image installed in ``tblite-0.4.0`` directory:

   .. code-block:: bash

      conda-containerize update --post-install update.sh tblite-0.4.0

.. _example_apptainer_definition_files:

Example Apptainer definition files
----------------------------------

Minimal example
~~~~~~~~~~~~~~~

Below is a minimal example of an Apptainer definition file:

.. code-block:: none

   Bootstrap: docker
   From: ubuntu:22.04

   %post
       apt-get update
       apt-get install -y grace

   %runscript
       /usr/bin/xmgrace

The resulting image will be based on Ubuntu 22.04. Once bootstrapped,
the commands in the ``%post`` section are executed to install the
Grace plotting package.

.. note::

   This example is intended to illustrate that very old software that is no
   longer maintained can successfully be run on modern infrastructure.  It is
   not intended to encourage you to use Grace in this container.

Conda environment
~~~~~~~~~~~~~~~~~

In the following example, the Conda environment file ``user_conda_environment.yml``
is used to create a Conda environment in an Apptainer container:

.. code-block:: none

   Bootstrap: docker
   From: continuumio/miniconda3

   %files
       user_conda_environment.yml

   %post
       /opt/conda/bin/conda env create -n user_conda_environment -f user_conda_environment.yml

   %runscript
       . /opt/conda/etc/profile.d/conda.sh
       conda activate user_conda_environment
       exec "$@"

The ``exec "$@"`` line at the bottom of the runscript allows ``apptainer run``
to accept user commands, such as ``python --version``.

.. _sylabs_remote_builder:

Sylabs Remote Builder
---------------------

We can build images on the Sylabs cloud website and download them to the
VSC infrastructure. This requires a Sylabs account. Once created,
use the `Sylabs Remote Builder`_ to generate an image from an
Apptainer definition file. This service uses SingularityCE, which
is highly compatible with Apptainer.

If the build succeeds, pull the image using the library URI, 

.. code-block:: bash

   apptainer pull library://<username>/<project>/<image_name>:<tag>

Remote builds offer several advantages:

* They are platform-independent and only require a web browser.
* They can be easily shared with other users.

However, local builds offer more flexibility, particularly when
interactive setup is required.

GPU-enabled containers
======================

Apptainer can run `GPU-enabled containers
<https://apptainer.org/docs/user/latest/gpu.html>`_ by exposing GPU devices,
drivers, and libraries (CUDA/ROCm) from the host system.

* NVIDIA GPUs: ``apptainer run --nv``
* AMD GPUs: ``apptainer run --rocm``

Requirements when building or running GPU containers:

* The GPU applications in the container must match the host GPU and driver's
  supported CUDA/ROCm version and compute capability.
* The container OS should be from a similar generation as the host OS.

Recommendations for VSC clusters:

* Use a prebuilt CUDA or ROCm container image as a base image, which can be
  obained by pulling from a suitable :ref:`container registry <apptainer_pulling_images>`.
* Select a container built for a CUDA version that matches one of the available CUDA
  environment modules on the cluster.

By default, all GPUs visible on the host node are also visible inside the
container.

MPI-enabled containers (advanced)
=================================

Running `MPI applications in containers
<https://apptainer.org/docs/user/latest/mpi.html>`_ requires compatibility
between the MPI implementation in the container and on the host.
Two common approaches are:

Hybrid model
   * The MPI library is installed inside the container.
   * The MPI implementation inside the container and on the host must be
     compatible.

.. code-block:: bash

   mpirun -n $SLURM_NTASKS apptainer exec <image_name> <executable>

Bind model
   * The MPI library is not included in the container but is bind-mounted
     from the host system.
   * The MPI library used to compile the application in the container
     must be compatible with the host library.

.. code-block:: bash

   MPI_DIR=/path/to/MPI-libraries
   mpirun -n $SLURM_NTASKS apptainer exec --bind "$MPI_DIR" <image_name> <executable>

.. note::

   For MPI applications you may expect some mild performance
   degradation.

For help with MPI-enabled containers, contact :ref:`user
support <user support VSC>`.

