.. _hpc containers:

#############################
Containers on the HPC systems
#############################

The best-known container implementation is undoubtedly `Docker`_.  However,
Docker needs to run as the *root* superuser of the system which has several
security implications. Hence, HPC sites do not typically allow users to run
Docker containers.

Fortunately, `Apptainer`_ provides an alternative and safer approach for
containers that can be used by any regular user without *root* permissions.
Since Apptainer also provides the options to build images from Docker container
files, it is a suitable replacement for Docker itself. Therefore, Apptainer is
fully supported on all VSC clusters.


When should I use containers?
=============================

If the software you intend to use is available on the VSC infrastructure,
don't use containers.  This software has been built to use specific
hardware optimizations, while software deployed via containers is
typically built for the common denominator.

Good use cases include:

* Containers can be useful to run software that is hard to install
  on HPC systems, e.g., GUI applications, legacy software, and so on.

* Containers can be useful to deal with compatibility issues between
  Linux flavors.

* You want to create a workflow that can run on VSC infrastructure,
  but can also be burst to a third-party compute cloud (e.g., AWS
  or Microsoft Azure) when required.

* You want to maximize the period your software can be run in a
  reproducible way.


How can I create a Apptainer image?
===================================

You have three options to build images, locally on your  machine, in the
cloud or on the VSC infrastructure.


Building on VSC infrastructure
------------------------------

Before starting, let's first set environment variables for the Apptainer cache
and temporary directories:

.. code-block:: bash

   $ export APPTAINER_TMPDIR=$VSC_SCRATCH/apptainer_tmp
   $ mkdir -p $APPTAINER_TMPDIR
   $ export APPTAINER_CACHEDIR=$VSC_SCRATCH/apptainer_cache
   $ mkdir -p $APPTAINER_CACHEDIR

.. warning::

   Don't forget to define and create the ``$APPTAINER_TMPDIR`` and
   ``$APPTAINER_CACHEDIR`` since if you fail to do so, Apptainer
   will use directories in your home directory, and you will exceed
   the quota on that file system. It’s recommended to add this to your
   ``~/.bashrc``.

   Also, images tend to be very large, so store them in a directory
   where you have sufficient quota, e.g., ``$VSC_DATA``.

You can build an immutable SIF image from a Docker container. For example, to
build an image that contains a version of TensorFlow and has Jupyter as well,
use:

.. code-block:: bash

   $ apptainer build tensorflow.sif docker://tensorflow/tensorflow:latest-jupyter

If you need to modify an existing image or container, we recommend building it
from a definition file, which allows you to completely customize your image in a
reproducible way.  We provide a brief :ref:`introduction to Apptainer definition
files <apptainer_definition_files>`, but for more details, we refer you to the
documentation on `Apptainer Definition Files`_.

When you have a Apptainer definition file, e.g., ``my_image.def``, you can build
your image file ``my_image.sif``. While users don’t have root priviliges on VSC
infrastructure, you can use the ``--fakeroot`` option to build your container as
a normal user with the effect of building as root:

.. code-block:: bash

   $ apptainer build --fakeroot my_image.sif my_image.def

.. note::

   Creating image files may take considerable time and resources. It is good
   practice to do this on a compute node, rather than on a login node.


Local builds
------------

If the ``--fakeroot`` build option fails because of certain `known limitations
<https://apptainer.org/docs/user/latest/fakeroot.html#restrictions-security>`_,
you can instead build the image on a local machine where you have superuser
privileges.  Apptainer only runs under Linux, so you’ll have to use a virtual
machine when using Windows or macOS.  For detailed instructions, see the
`Apptainer Quick Start`_ guide.

Once your image is built, you can :ref:`transfer <data transfer>`
it to the VSC infrastructure to use it.

.. warning::

   Since Apptainer images can be very large, transfer your image
   to a directory where you have sufficient quota, e.g.,
   ``$VSC_DATA``.


Remote builds
-------------

You can build images on the Sylabs cloud website, and download them to the VSC
infrastructure. You will have to create an account at Sylabs.  Once this is
done, you can use `Sylabs Remote Builder`_ to create an image based on an
:ref:`Apptainer definition file <apptainer_definition_files>`.  This service uses
SingularityCE, a fork of Apptainer that is highly compatible with Apptainer. If
the build succeeds, you can pull the resulting image from the library:

.. code-block:: bash

   $ export APPTAINER_CACHEDIR=$VSC_SCRATCH/apptainer_cache
   $ mkdir -p $APPTAINER_CACHEDIR
   $ apptainer pull library://gjbex/remote-builds/rb-5d6cb2d65192faeb1a3f92c3:latest

.. warning::

   Don't forget to define and create the ``$APPTAINER_CACHEDIR``
   since if you fail to do so, Apptainer will use directories in
   your home directory, and you will exceed the quota on that file
   system.

   Also, images tend to be very large, so store them in a directory
   where you have sufficient quota, e.g., ``$VSC_DATA``.

Remote builds have several advantages:

- you only need a web browser to create them, so this approach is
  platform-independent,
- they can easily be shared with others.

However, local builds still offer more flexibility, especially when
some interactive setup is required.


.. _apptainer_definition_files:

Apptainer definition files
==========================

Below is a minimal example of an Apptainer definition file::

   Bootstrap: docker
   From: ubuntu:22.04

   %post
       apt-get update
       apt-get install -y grace

   %runscript
       /usr/bin/xmgrace

The resulting image will be based on Ubuntu 22.04.  Once it is bootstrapped,
the command in the ``%post`` section of the definition file will be executed.
For this example, the Grace plotting package will be installed.

.. note::

   This example is intended to illustrate that very old software that is no
   longer maintained can successfully be run on modern infrastructure.  It is
   not intended to encourage you to use Grace in this container.

Apptainer definition files are very flexible. For more details,
we refer you to the documentation on `Apptainer Definition Files`_.

An important advantage of definition files is that they can easily
be shared, and improve reproducibility.


Conda environment in a definition file
--------------------------------------
:ref:`Conda environments<conda for Python>`
are a convenient solution when it comes to handling own Python-dependent
software installations. Having a containerized conda environment is often
useful for groups when working collectively on a common project.
One way to have a conda environment in a container is to create it from
an existing environment YAML file. If we have a conda environment exported
in a YAML format file called, e.g., ``user_conda_environment.yml``, then
from that file one can recreate the same environment in a Apptainer definition file::

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

The ``exec "$@"`` line will accept the user's input command, e.g.,
``python --version`` or ``R --version``, when running the container.

.. note::

   Creating a container with a conda environment in it can ask for a lot of memory.
   Therefore, that procedure might be best done on a compute node and not
   on the cluster login nodes.


How can I run a Apptainer image?
================================

Once you have an image, there are several options to run the container.

#. You can invoke any application that is in the ``$PATH`` of the
   container, e.g., for the image containing Grace:

   .. code-block:: bash

      $ apptainer exec grace.sif xmgrace

#. If the ``xmgrace`` command is executed in the Apptainer ``runscript`` (as
   specified in the ``%runscript`` directive of the :ref:`Apptainer definition
   file <apptainer_definition_files>`), you can run the container as follows:

   .. code-block:: bash

      $ apptainer run grace.sif

#. You can also run an interactive shell inside the container:

   .. code-block:: bash

      $ apptainer shell grace.sif

By default, your home directory in the container will be mounted
with the same path as it has on the host.  The current working
directory in the container is that on the host in which you
invoked ``apptainer``.

.. note::

   Although you can move to a parent directory of the current working
   directory in the container, you will not see its contents on the host.
   Only the current working directory and its sub-directories on the host
   are mounted.

Additional host directories can be mounted in the container as well by
using the ``-B`` option.  Mount points are created dynamically (using
overlays), so they do not have to exist in the image.  For example,
to mount the ``$VSC_SCRATCH`` directory, you would use:

.. code-block:: bash

   $ apptainer exec -B $VSC_SCRATCH:/scratch grace.sif xmgrace

Your ``$VSC_SCRATCH`` directory is now accessible from within the
image in the directory ``/scratch``.

.. note::

   If you want existing scripts to work from within the image without
   having to change paths, it may be convenient to use identical
   mount points in the image and on the host, e.g., for the
   ``$VSC_DATA`` directory:

   .. code-block:: bash

      $ apptainer exec -B $VSC_DATA:$VSC_DATA grace.sif xmgrace

   Or, more concisely:

   .. code-block:: bash

      $ apptainer exec -B $VSC_DATA grace.sif xmgrace

   The host environment variables are defined in the image, hence
   scripts that use those will work.


Can I use apptainer images in a job?
------------------------------------

Yes, you can.  Apptainer images can be part of any workflow, e.g.,
the following script would create a plot in the Grace container:

.. code-block:: bash

   #!/bin/bash -l
   #PBS -l nodes=1:ppn=1
   #PBS -l walltime=00:30:00
   
   cd $PBS_O_WORKDIR
   apptainer exec grace.sif gracebat -data data.dat -batch plot.bat
   
Ensure that the container has access to all the required directories
by providing additional bindings if necessary.


Can I run parallel applications using a Apptainer image?
----------------------------------------------------------

For shared memory applications there is absolutely no problem.

For distributed applications it is highly recommended to use
the same implementation and version of the MPI libraries on
the host and in the image.  You also want to install the
appropriate drivers for the interconnect, as well as the
low-level communication libraries, e.g., ibverbs.

For this type of scenario, it is probably best to contact :ref:`user
support <user support VSC>`.

.. note::

   For distributed applications you may expect some mild performance
   degradation.


Can I run a service from a Apptainer image?
---------------------------------------------

Yes, it is possible to run services such as databases or web
applications that are installed in Apptainer images.

For this type of scenario, it is probably best to contact :ref:`user
support <user support VSC>`.


