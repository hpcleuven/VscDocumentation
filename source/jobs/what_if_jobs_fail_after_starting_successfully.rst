.. _job failure:

My jobs seem to run, but I don't see any output or errors?
==========================================================

Most probably, you exceeded the disk quota for your home directory,
i.e., the total file size for your home directory is just too large.

When a job runs, it needs to store temporary output and error files in
your home directory. When it fails to do so, the program will crash, and
you won't get feedback, since that feedback would be in the error file
that can't be written.

See the FAQs listed below to :ref:`check the amount of disk
space <disk usage>` you are currently using, and for a few hints on
:ref:`what data to store where <data location>`.

However, your home directory may unexpectedly fill up in two ways:

#. a running program produces :ref:`large amounts of output or
   errors <large output>`;
#. a program crashes and produces a :ref:`core dump <core dump>`.

.. note::

   that one job that produces output or a core that is too large for
   the file system quota will most probably cause all your jobs that are
   queued to fail.


.. _large output:

Large amounts of output or errors
---------------------------------

To deal with the first issue, simply redirect the standard output of the
command to a file that is in your data or scratch directory, or, if you
don't need that output anyway, redirect it to ``/dev/null``. A few examples
that can be used in your job scripts that execute, e.g., ``my-prog``, are
given below.

To send standard output to a file, you can use::

   my-prog > $VSC_DATA/my-large-output.txt

If you want to redirect both standard output and standard error, use::

   my-prog  > $VSC_DATA/my-large-output.txt \\
           2> $VSC_DATA/my-large-error.txt

To redirect both standard output and standard error to the same file,
use::

   my-prog &> $VSC_DATA/my-large-output-error.txt

If you don't care for the standard output, simply write::

   my-prog >/dev/null


.. _core dump:

Core dump
---------

When a program crashes, a core file is generated. This can be used to
try and analyze the cause of the crash. However, if you don't need cores
for post-mortem analysis, simply add the following line to your ``.bashrc``
file::

   ulimit -c 0

This can be done more selectively by adding this line to your job script
prior to invoking your program.
