Using software
==============

The scientific software stack on the VSC clusters is mainly exposed via
:ref:`modules <module_system_basics>`. :ref:`Toolchains <toolchains>` are
an important concept in this context.

For basic information on the module system and more site-specific information,
please consult the following pages:

.. toctree::
   :maxdepth: 1

   module_system_basics
   ../gent/setting_up_the_environment_using_lmod_at_the_hpc_ugent_clusters
   ../leuven/leuven_module_system


Background
----------

Software installation and maintenance on HPC infrastructure such as the
VSC clusters poses a number of challenges not encountered on a
workstation or a departmental cluster. For many libraries and programs,
multiple versions have to installed and maintained as some users require
specific versions of those. In turn, those libraries or executables sometimes
rely on specific versions of other libraries, further complicating the
matter.

The way Linux finds the right executable for a command, and a program
loads the right version of a library or a plug-in, is through so-called
environment variables. These can, e.g., be set in your shell
configuration files (e.g., ``.bashrc``), but this requires a certain
level of expertise. Moreover, getting those variables right is tricky
and requires knowledge of where all files are on the cluster. Having to
manage all this by hand is clearly not an option.

We deal with this on the VSC clusters in the following way. First, we've
defined the concept of a :ref:`toolchain <toolchains>`. They consist of
a set of compilers, MPI library and
basic libraries that work together well with each other, and then a
number of applications and other libraries compiled with that set of
tools and thus often dependent on those. We use tool chains based on the
Intel and GNU compilers, and refresh them twice a year, leading to
version numbers like 2014a, 2014b or 2015a for the first and second
refresh of a given year. Some tools are installed outside a toolchain,
e.g., additional versions requested by a small group of users for
specific experiments, or tools that only depend on basic system
libraries. Second, we use :ref:`modules <module_system_basics>` to manage the
environment and all dependencies and possible conflicts
between various programs and libraries.


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

