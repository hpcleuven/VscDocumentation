How can I run containers on the HPC systems?
============================================

The best-known container implementation is doubtlessly `docker`_.  However,
due to security concerns HPC sites typically don't allow users to run
Docker containers.

Fortunately, `Singularity`_ addresses container related security issues,
so Singularity images can be used on the cluster.  Since a Singularity
image can be built from a docker container, that should not be a severe
limitation.


How can I create an image?
--------------------------

You have three options to build images, locally on your  machine, in the
cloud or on the VSC infrastructure.


Building on VSC infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given that most build procedures require superuser privileges, your options
on the VSC infrastructure are limited.  You can build an image from a docker
container, e.g., to build an image that contains a version of tensorflow that
can be used on GPUs, and has jupyter as well, use::

   $ export SINGULARITY_TMPDIR=$VSC_SCRATCH/singularity_tmp
   $mkdir -p $SINGULARITY_TMPDIR
   $ export SINGULARITY_CACHEDIR=$VSC_SCRATCH/singularity_cache
   $mkdir -p $SINGULARITY_CACHEDIR
   $ singularity build tensorflow.simg docker://tensorflow/tensorflow:latest-gpu-jupyter

.. warning::

   Don't forget to define and create the ``$SINGULARITY_TMPDIR`` and
   ``$SINGULARITY_CACHEDIR`` since if you fail to do so, Singularity
   will use directories in your home directory, and you will exceed
   the quota on that file system.

   Also, images tend to be very large, so store them on in a directory
   where you have sufficient quota, e.g., ``$VSC_DATA``.


This approach will serve you well when you can use either prebuild images
or docker containers.  If you need to modify an existing image or
container, you should consider the alternatives.

.. note::

   Creating image files may take considerable time and resources, it is good
   practice to do this on a compute node, rather than on a login node.


Local builds
~~~~~~~~~~~~

The most convenient way to create an image is on your own machine, since
you will have superuser privileges, and hence the most options to chose
from.  At this point, Singularity only runs under Linux, so you would
to use a virtual machine when using Windows or MacOS.  For detailed
instructions, see the `Singularity installation documentation`_.

Besides building images from docker containers, you have the option to
create them from a definition file, which allows you to completely customize
your image.  We provide a brief :ref:`introduction to Singularity definition files
<Singularity definition files>`, but for more details, we refer you to the
`Singularity definition file documentation`_.

When you have a Singularity definition file, e.g., ``my_image.def``, you can
build your image file ``my_image.simg``::

   $ singularity build my_image.simg my_image.def

.. warning::

   Since Singularity images can be very large, build your image
   in a directory where you have sufficient quota, e.g.,
   ``$VSC_DATA``.


.. _Singularity definition files:

Singularity definition files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example of a Singularity defintion file::

    BootStrap: docker
    From: ubuntu:disco

    %post
        dpkg --add-architecture i386
        apt-get update
        apt-get install -y wine32
        apt-get -y install wine
        apt-get -y install winetricks

The resulting image will be based on the Ubuntu Disco Dingo distribution (19.04).
Once it is boostrapped, the command in the ``%post`` section of the definition
file will be executed.  For this example, the wine Windows emulation software
package will be installed.

Singularity definition files are very flexible, for more details, we refer you
to the `Singularity defintion file documentation`_.



How to run a singularity container?
-----------------------------------

To do.


.. _Singularity installation documentation: https://sylabs.io/guides/3.2/user-guide/installation.html#
.. _Singularity defintion file documentation: https://sylabs.io/guides/3.2/user-guide/definition_files.html

.. include:: links.rst
