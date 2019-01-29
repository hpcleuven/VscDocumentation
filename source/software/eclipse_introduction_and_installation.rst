.. _Eclipse intro:

Eclipse introduction and installation
=====================================

Software development on clusters
--------------------------------

`Eclipse`_ is an extensible IDE for
program development. The basic IDE is written in Java for the
development of Java programs, but can be extended through packages. The
IDE was originally developed by IBM, but open-sourced and has become
very popular. There are some interesting history tidbits on `the
WikiPedia entry for Eclipse <https://en.wikipedia.org/wiki/Eclipse_(software)>`_.

Some attractive features
~~~~~~~~~~~~~~~~~~~~~~~~

-  Multi-platform: Available for Windows, OS X and Linux, and works
   mostly the same on all these platforms.
-  Support for C/C++ (via de CDT plugin) and Fortran (via the Photran
   plugin) development. This goes far beyond syntax coloring and
   includes things like code refactoring, build process management, etc.
-  Support for the development of parallel applications on a cluster,
   including automatic synchronisation of the source files on your
   laptop with one or more cluster accounts. So you can easily do code
   development while off-line. Eclipse is heavily promoted (and actively
   developed) within the XSEDE collaboration of supercomputer centres in
   the USA.
   If you have suitable compilers and libraries on your local machine,
   you may even be able to do part of the testing and debugging on your
   local machine, avoiding delays caused by the job queueing system.
   Another advantage of running Eclipse locally rather than on the
   cluster is that the GUI has all of the responsiveness of a local
   program, not influenced by network delays.
-  It integrates with most popular version control system (offering a
   GUI to them also).

Caveat
~~~~~~

The documentation of the Parallel Tools Platform also tells you how to
launch and debug programs on the cluster from the Eclipse IDE. However,
this is for very specific cluster configurations and we cannot support
this on our clusters at the moment. You can use features such as
syncrhonised projects (where Eclipse puts a copy of the project files
from your desktop on the cluster, and even synchronises back if you
change them on the cluster) or opening a SSH shell from the IDE to
directly enter commands on the cluster.

Release policy
~~~~~~~~~~~~~~

The eclipse project works with a \\"synchronised release policy\". Major
new versions of the IDE and a wide range of packages (including the
C/C++ development package (CDT), Parallel Tools Platform (PTP) and the
Fortran development package (Photran) which is now integrated in the
PTP) occur simultaneously in June of each year which guarantees that
there are no compatibility problems between packages if you upgrade your
whole installation at once. Bug fixes are of course released in between
version updates. Each version has its own code name and the code name
has become more popular than the actual version number (as version
numbers for the packages differ). E.g., the whole June 2013 release
(base IDE and packages) is known as the "Kepler" release (version
number 4.3), the June 2014 release as the "Luna" release (version
number 4.4), the June 2015 as the " Mars" release (version number
4.5) and the June 2016 release as "Neon".  The latest release at the time
of writing is simply called 2018-12.

Getting eclipse
---------------

The best place to get Eclipse is the the official `Eclipse download
page`_. That site contains
various pre-packaged versions with a number of extension packages
already installed. The most interesting one for C/C++ or Fortran
development on clusters is \\"Eclipse for Parallel Application
Developers\". The installation instructions depend on the machine you're
installing on, but typically it is not more than unpacking some archive
in the right location. You'll need a sufficiently recent Java IDE on
your machine though. Instructions are available on the `Eclipse
Wiki <http://wiki.eclipse.org/Eclipse/Installation>`_.

The CDT, Photran and PTP plugins integrate with compilers and libraries
on your system. For Linux, it uses the gcc compiler on your system. On
OS X it integrates with gcc and on Windows, you need to install
`Cygwin`_ and its GCC toolchain.

The Eclipse documentation is also available on-line on the `Eclipse`_ website.

-  Check out some :ref:`macOS specific issues here <Eclipse macOS>`.

Basic concepts
--------------

-  A workspace is a place where eclipse stores a set of projects. It
   corresponds to a folder on file. The actual files of project can but
   do not need to be in that folder. However, all internal data that
   eclipse maintains will be. A user can have more than one workspace.
   Eclipse will ask at the start which workspace to use for the current
   session. Workspaces are not easily portable between computers. They
   are simply a way to organise your projects on your local computer.
-  Each workspace can contain one or more projects. Each project is a
   collection of resources, e.g., C files or Fortran files, and
   typically has a releasable component that can be build from those
   resources, e.g., an executable. It is a good idea to use workspaces
   to group a number of related projects. A project also corresponds to
   a folder in the file system. That folder does not have to be
   contained in the workspace folder. Projects can be transported easily
   from one workstation to another.
-  A perspective defines the (initial) layout of views and editors for a
   particular task. E.g., the C/C++ perspective shows an editor to edit
   C/C++-files and views to quickly navigate in the code, check
   definitions, etc. The Debug perspective is used to debug an
   application. The PTP also has a system monitoring perspective to
   monitor jobs.

Interesting bits in the documentation
-------------------------------------

-  `Basic Eclipse user guide with a getting started
   section <http://help.eclipse.org/neon/topic/org.eclipse.platform.doc.user/gettingStarted/intro/overview.htm?cp=0_0>`_
-  Parallel Tools Platform:

   -  `Parallel Development User Guide - Introduction to PTP Project
      Types -
      Synchronized <http://help.eclipse.org/neon/topic/org.eclipse.ptp.doc.user/html/localVsRemote.html?cp=62_4_1#sync>`_
      explains the advantages and disadvantages of the "Synchronized
      project type".
   -  The PTP also supports modules to configure the remote shell before
      actually building the application: `Parallel Development User
      Guide - Configuring Environment
      Modules <http://help.eclipse.org/neon/topic/org.eclipse.ptp.doc.user/html/modules.html?cp=62_8>`_.
   -  `The PTP Wiki <http://wiki.eclipse.org/PTP>`_

.. include:: links.rst
.. include:: ../access/links.rst
