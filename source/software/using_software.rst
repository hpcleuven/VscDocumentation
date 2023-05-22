Using software
==============

The best way to get a complete list of all available software in a
particular cluster can be obtained by typing:

::

   $ module av

In order to use the software stack in the HPC cluster, the user should work
with the :ref:`module system <module system basics>`.

.. toctree::
   :maxdepth: 2

   software_stack

On the newer systems, we use the same naming conventions for packages on all
systems. Due to the ever expanding list of packages, we've also made some
adjustments and don't always show all packages. Be sure to check out
:ref:`how you can see specialized software modules
<specialized software stacks>`.


.. seealso::

   Since August 2016, a different implementation of the module system has been
   implemented on UGent, VUB, UAntwerpen Tier-2 systems and KU Leuven's Genius
   cluster, called `Lmod`_. Though highly compatible with the aforementioned
   module system used on the other clusters, it has some extra capabilities and
   differences:


   .. toctree::
      :maxdepth: 2
   
      ../gent/setting_up_the_environment_using_lmod_at_the_hpc_ugent_clusters

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

