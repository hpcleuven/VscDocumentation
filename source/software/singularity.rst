Can I run containers on the HPC systems?
========================================

The best-known container implementation is doubtlessly `docker`_.  However,
due to security concerns HPC sites typically don't allow users to run
Docker containers.

Fortunately, `Singularity`_ addresses container related security issues,
so Singularity images can be used on the cluster.  Since a Singularity
image can be built from a docker container, that should not be a severe
limitation.


When should I use containers?
-----------------------------

If the software you intend to use is available on the VSC infrastructure,
don't use containers.  This software has been built to use specific
hardware optimizations, while software deployed via containers is
typically built for the common denominator.

Good use cases include:

- Containers can be useful to run software that is hard to install
  on HPC systems, e.g., GUI applications, legacy software, and so on.
- Containers can be useful to deal with compatibility issues between
  Linux flavors.
- You want to create a workflow that can run on VSC infrastructure,
  but can also be burst to a third-party compute cloud (e.g., AWS
  or Microsoft Azure) when required.
- You want to maximize the period your software can be run in a
  reproducible way.


How can I create a Singularity image?
-------------------------------------

You have three options to build images, locally on your  machine, in the
cloud or on the VSC infrastructure.


Building on VSC infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given that most build procedures require superuser privileges, your options
on the VSC infrastructure are limited.  You can build an image from a docker
container, e.g., to build an image that contains a version of TensorFlow 
and has jupyter as well, use::

   $ export SINGULARITY_TMPDIR=$VSC_SCRATCH/singularity_tmp
   $ mkdir -p $SINGULARITY_TMPDIR
   $ export SINGULARITY_CACHEDIR=$VSC_SCRATCH/singularity_cache
   $ mkdir -p $SINGULARITY_CACHEDIR
   $ singularity build tensorflow.sif docker://tensorflow/tensorflow:latest-jupyter

.. warning::

   Don't forget to define and create the ``$SINGULARITY_TMPDIR`` and
   ``$SINGULARITY_CACHEDIR`` since if you fail to do so, Singularity
   will use directories in your home directory, and you will exceed
   the quota on that file system.

   Also, images tend to be very large, so store them on in a directory
   where you have sufficient quota, e.g., ``$VSC_DATA``.


This approach will serve you well if you can use either prebuilt images
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
build your image file ``my_image.sif``::

   your_machine> singularity build my_image.sif my_image.def

Once your image is built, you can :ref:`transfer <Transferring data>`
it to the VSC infrastructure to use it.

.. warning::

   Since Singularity images can be very large, build your image
   in a directory where you have sufficient quota, e.g.,
   ``$VSC_DATA``.


Remote builds
~~~~~~~~~~~~~

You can build images on the Singularity website, and download
them to the VSC infrastructure.  You will have to create an account
at Sylabs.  Once this is done, you can use `Sylabs Remote Builder`_
to create an image based on a :ref:`Singularity definition 
<Singularity definition files>`.  If the build succeeds, you can
pull the resulting image from the library::

   $ export SINGULARITY_CACHEDIR=$VSC_SCRATCH/singularity_cache
   $ mkdir -p $SINGULARITY_CACHEDIR
   $ singularity pull library://gjbex/remote-builds/rb-5d6cb2d65192faeb1a3f92c3:latest

.. warning::

   Don't forget to define and create the ``$SINGULARITY_CACHEDIR``
   since if you fail to do so, Singularity will use directories in
   your home directory, and you will exceed the quota on that file
   system.

   Also, images tend to be very large, so store them on in a directory
   where you have sufficient quota, e.g., ``$VSC_DATA``.

Remote builds have several advantages:

- you only need a web browser to create them, so this approach is
  platform-independent,
- they can easily be shared with others.

However, local builds still offer more flexibility, especially when
some interactive setup is required.


.. _Singularity definition files:

Singularity definition files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example of a Singularity definition file::

   Bootstrap: docker
   From: ubuntu:xenial
   
   %post
       apt-get update
       apt-get install -y grace
               
   %runscript
       /usr/bin/grace

The resulting image will be based on the Ubuntu Xenial Xerus distribution
(18.04).  Once it is bootstrapped, the command in the ``%post`` section of
the definition file will be executed.  For this example, the Grace plotting
package will be installed.

.. note::

   This example is intended to illustrate that very old software that
   is no longer maintained can successfully be run on modern infrastructure.
   It is by no means intended to encourage you to start using Grace.

Singularity definition files are very flexible, for more details,
we refer you to the `Singularity definition file documentation`_.

An important advantage of definition files is that they can easily
be shared, and improve reproducibility.


How can I run a Singularity image?
----------------------------------

Once you have an image, there are several options to run the container.

#. You can invoke any application that is in the ``$PATH`` of the
   container, e.g., for the image containing Grace::

   $ singularity  exec  grace.sif  xmgrace

#. In case the definition file specified a ``%runscript`` directive,
   this can be executed using::

   $ singularity  run  grace.sif

#. The container can be run as a shell::

   $ singularity  shell  grace.sif

By default, your home directory in the container will be mounted
with the same path as it has on the host.  The current working
directory in the container is that on the host in which you
invoked ``singularity``.

.. note::

   Although you can move to a parent directory of the current working
   directory in the container, you will not see its contents on the host.
   Only the current working directory and its sub-directories on the host
   is mounted.

Additional host directories can be mounted in the container as well by
using the ``-B`` option.  Mount points are created dynamically (using
overlays), so they do not have to exist in the image.  For example,
to mount the ``$VSC_SCRATCH`` directory, you would use::

   $ singularity  exec  -B $VSC_SCRATCH:/scratch  grace.sif  xmgrace

Your ``$VSC_SCRATCH`` directory is now accessible from within the
image in the directory ``/scratch``.

.. note::

   If you want existing scripts to work from within the image without
   having to change paths, it may be convenient to use identical
   mount points in the image and on the host, e.g., for the
   ``$VSC_DATA`` directory::

      $ singularity  exec  -B $VSC_DATA:$VSC_DATA  grace.sif  xmgrace

   Or, more concisely::

      $ singularity  exec  -B $VSC_DATA  grace.sif  xmgrace

   The host environment variables are defined in the image, hence
   scripts that use those will work.


Can I use singularity images in a job?
--------------------------------------

Yes, you can.  Singularity images can be part of any workflow, e.g.,
the following script would create a plot in the Grace container::

   #!/bin/bash –l
   #PBS –l nodes=1:ppn=1
   #PBS –l walltime=00:30:00
   
   cd $PBS_O_WORKDIR
   singularity exec grace.sif gracebat –data data.dat \
                                       -batch plot.bat
   
Ensure that the container has access to all the required directories
by providing additional bindings if necessary.


Can I run parallel applications using a Singularity image?
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

   For distributed application you may expect some mild performance
   degradation.


Can I run a service from a Singularity image?
---------------------------------------------

Yes, it is possible to run services such as databases or web
applications that are installed in Singularity images.

For this type of scenario, it is probably best to contact :ref:`user
support <user support VSC>`.


.. _Singularity installation documentation: https://sylabs.io/guides/3.2/user-guide/installation.html#
.. _Singularity definition file documentation: https://sylabs.io/guides/3.2/user-guide/definition_files.html
.. _Sylabs Remote Builder: https://cloud.sylabs.io/builder

.. include:: links.rst
