Using pre-installed software
============================

A lot of scientific software is centrally available on the VSC clusters. To
avoid conflicts between different software packages, the installations are
offered as :ref:`modules <module_system_basics>`. The executables, libraries,
headers, ... of a certain module can only be used after that module has been
loaded. By loading a certain set of modules, you can easily set up an
environment that has precisely the software you need.

:ref:`Toolchains <toolchains>` are an important concept in this context.
A toolchain consists of a set of compilers, MPI library and
basic libraries that work together well with each other, and then a
number of applications and other libraries compiled with that set of
tools and thus often dependent on those. We use toolchains based on the
Intel and GNU compilers, and refresh them up to twice a year, leading to
version numbers like 2023a and 2023b for the first and second
refresh of a given year. Some tools are installed outside a toolchain,
e.g., additional versions requested by a small group of users for
specific experiments, or tools that only depend on basic system
libraries.

For basic information on the module system and more site-specific information,
please consult the following pages:

.. toctree::
   :maxdepth: 1

   module_system_basics
   cluster_modules
   requesting_software
   using_eessi
