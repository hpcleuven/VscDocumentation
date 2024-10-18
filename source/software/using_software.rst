Using software
==============

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
   ../gent/setting_up_the_environment_using_lmod_at_the_hpc_ugent_clusters
   ../leuven/leuven_module_system


Packages with additional documentation
--------------------------------------

MATLAB (a package by `MathWorks`_)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   matlab_getting_started
   matlab_parallel_computing

R
~

.. toctree::
   :maxdepth: 2

   r_command_line_arguments_in_scripts
   r_integrating_c_functions

Programming Languages
---------------------

Some programming languages have an extensive standard library, but
optionally allow to install extra packages. For most languages, the
user can install packages in his own home directory without system
administrator intervention. Some documentation for doing this for
:ref:`Perl <Perl packages>` and :ref:`Python <Python packages>` is provided.

