Using software
==============

The best way to get a complete list of all available software in a
particular cluster can be obtained by typing:

::

   $ module av

In order to use those software packages, the user should work with the
:ref:`module system <module system basics>`. On the newer
systems, we use the same naming conventions for packages on all systems.
Due to the ever expanding list of packages, we've also made some
adjustments and don't always show all packages, so be sure to check out
the page on :ref:`the module system <module system basics>` again to
:ref:`learn how you can see specialized software modules
<specialized software stacks>`.

| Note: Since August 2016, a different implementation of the module
  system has been implemented on the UGent, the VUB,
  the UAntwerpen Tier-2
  systems and KU Leuven's Genius cluster, called `Lmod`_. Though highly
  compatible with the system used on the other clusters, it offers
  :ref:`a lot of new commands <Lmod commands Gent>`, and
  :ref:`some key differences <Lmod key differences>`.

Packages with additional documentation
--------------------------------------

-  MATLAB (a package by `MathWorks`_)

   -  :ref:`MATLAB getting started`
   -  :ref:`Parallel computing with MATLAB <MATLAB parallel computing>`

-  R

   -  :ref:`Accessing command line arguments in R scripts <R command
      line arguments>`
   -  :ref:`Integrating C functions in R <R integrating C functions>`

-  Some programming languages have an extensive standard library, but
   optionally allow to install extra packages. For most languages, the
   user can install packages in his own home directory without system
   administrator intervention. Some documentation for doing this for
   :ref:`Perl <Perl packages>` and :ref:`Python <Python packages>` is provided.

