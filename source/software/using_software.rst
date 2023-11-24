Using software
==============

Software installation and maintenance on HPC infrastructure such as the
VSC clusters poses a number of challenges not encountered on a
workstation or a departmental cluster. For many libraries and programs,
multiple versions have to be installed and maintained as some users require
specific versions of those. In turn, those libraries or executables sometimes
rely on specific versions of other libraries, further complicating the
matter.

The way Linux finds the right executable for a command, and a program
loads the right version of a library or a plug-in, is through so-called
environment variables. These can, e.g., be set in your shell
configuration files (e.g., ``.bashrc``); however, this requires a certain
level of expertise. Moreover, getting those variables right is tricky
and requires knowledge of where all files are on the cluster. Having to
manage all this by hand is clearly not an option.

We deal with this on the VSC clusters in the following way.

* First, we've defined the concept of a :ref:`toolchain <toolchains>`. 
  They consist of a set of compilers, MPI libraries and basic libraries 
  that work together well with each other. Then come a number of applications 
  and other libraries compiled with those set of tools, and hence depending
  on them. We use toolchains based on the Intel and GNU compilers. New toolchains
  which offer reasonable compute performance are regularly installed, leading to 
  version numbers like 2021a, 2021b or 2022a (for the first and second halves of 
  a given year). Some tools are installed outside a toolchain, e.g., additional 
  versions requested by a small group of users for specific experiments, or tools 
  that only depend on basic system libraries.

* Second, we use the `module system <module_system>` to manage the environment 
  variables and all dependencies and to prevent possible conflicts between various 
  programs and libraries.


!!!!!!!!HERE SHOULD COME A LINK TO THE GENERATED PAGE WITH AVAILABLE SOFTWARE!!!!!!!!!

.. toctree::
   :maxdepth: 2
   
   toolchains
   module_system
   software_stack
   ../gent/setting_up_the_environment_using_lmod_at_the_hpc_ugent_clusters

!!the specific UGent page probably can be removed!!

