.. _job failure:

My jobs seem to run, but I don't see any output or errors?
==========================================================

.. _walltime exceeded:

You ran out of time
-------------------

It is possible the job exceeded the walltime that was specified as
part of the required resources, or the default value otherwise.

If this is the case, the resource manager will terminate your job,
and the job's output file will contain a line similar to::

   =>> PBS: job killed: walltime <value in seconds> exceeded limit <value in seconds>

Try to submit your job :ref:`specifying a larger walltime <walltime>`.


.. _quota exceeded:

You ran out of disk space
-------------------------

You may have exceeded the disk quota for your home directory,
i.e., the total file size for your home directory is just too large.

When a job runs, it needs to store temporary output and error files in
your home directory. When it fails to do so, the program will crash, and
you won't get feedback, since that feedback would be in the error file
that can't be written.

See the FAQs listed below to :ref:`check the amount of disk
space <storage usage>` you are currently using, and for a few hints on
:ref:`what data to store where <data location>`.

However, your home directory may unexpectedly fill up in two ways:

#. a running program produces :ref:`large amounts of output or
   errors <large output>`;
#. a program crashes and produces a :ref:`core dump <core dump>`.

.. note::

   That one job that produces output or a core dump that is too large for
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

   my-prog  > $VSC_DATA/my-large-output.txt \
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

You can find all the core dumps in your home directory using::

   $ find  $VSC_HOME  -name "core.*"

They can be removed (make sure that only unwanted core files are removed by
checking with the command above) using::

   $ find  $VSC_HOME  -name "core.*"  -exec rm {} +


.. _memory exceeded:

You ran out of memory (RAM)
---------------------------

The resource manager monitor the memory usage of your application, and will
automatically terminate your job when that memory exceeds a limit.  This limit
is either the value specified in the resource request using ``pmem`` or ``pvmem``,
or the default value.

You may find an indication that this may be the case by looking at the job's
output file.  The epilogue information lists the resources used by the job,
including memory.

::

   Resources Used : cput=00:00:00,vmem=110357kb,walltime=00:34:02,mem=984584kb

If the value of ``mem`` is close to the limit, this may indicate that the
application used too much memory.

The used resources are just a rough indication, and the reported value can
be lower than the actual value if the application's memory usage rapidly
increased.  Hence it is prudent to :ref:`monitor the memory consumption of your
job in more detail <monitoring memory and cpu>`.

You can try to resubmit your job :ref:`specifying more memory per core <pmem>`.
