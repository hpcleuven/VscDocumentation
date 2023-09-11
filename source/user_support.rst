.. _user support VSC:

User support
============

Each of the major VSC-institutions has its own user support:

.. include:: user_support_addresses.rst

What information should I provide when contacting user support?
---------------------------------------------------------------

When you submit a support request, it helps if you always provide:

#. your VSC user ID (or VUB netID),
#. contact information - it helps to specify your preferred mail address
   and phone number for contact,
#. an informative subject line for your request,
#. the time the problem occurred,
#. the steps you took to resolve the problem.

.. warning::

   If you are working in a terminal, please *do not* provide a screenshot,
   simply copy/paste the text in your terminal.  This is easier to read for
   support staff, and allows them to copy/paste information, rather than
   having to retype, e.g., paths.

Below, you will find more useful information you can provide for various
categories of problems you may encounter. Although it may seem like more
work to you, it will often save a few iterations and get your problem
solved faster.

If you have problems logging in to the system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please provide the following information:

#. your operating system (e.g., Linux, Windows, macOS, ...),
#. your client software (e.g., PuTTY, OpenSSH, ...),
#. your location (e.g., on campus, at home, abroad),
#. whether the problem is systematic (how many times did you try, over
   which period) or intermittent,
#. any error messages shown by the client software, or an error log if
   it is available.

Logging information can easily be obtained from the
:ref:`OpenSSH client <troubleshoot_openssh>`,
:ref:`PuTTY <troubleshoot_putty>` and
:ref:`MobaXTerm <troubleshoot_mobaxterm>`.

If installed software malfunctions/crashes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please provide the following information:

#. the name of the cluster your are working on,
#. the name of the application (e.g., Ansys, Matlab, R, ...),
#. the module(s) you load to use the software (e.g.,
   R/3.1.2-intel-2015a),
#. the error message the application produces, as well as the location of the
   output and error files if this ran as a job,
#. whether the error is reproducible,
#. if possible, a procedure and data to reproduce the problem,
#. if the application was run as a job, the jobID(s) of (un)successful
   runs.

If your own software malfunctions/crashes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please provide the following information:

#. the location of the source code,
#. the error message produced at build time or runtime, as well as the location
   of the output and error files if this ran as a job,
#. the toolchain and other module(s) you load to build the software
   (e.g., intel/2015a with HDF5/1.8.4-intel-2015a),
#. if possible and applicable, a procedure and data to reproduce the
   problem,
#. if the software was run as a job, the jobID(s) of (un)successful
   runs.
