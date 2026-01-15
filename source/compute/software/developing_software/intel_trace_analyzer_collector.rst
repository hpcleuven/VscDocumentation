Intel Trace Analyzer & Collector
================================

.. warning::

   `Intel discontinued ITAC <https://www.intel.com/content/www/us/en/developer/archive/tools/trace-analyzer-and-collector.html>`_
   on 2022 with its last version 2022.3. Users are encouraged to transition to `Intel oneAPI VTune Profiler`_.

Purpose
-------

Debugging MPI applications is notoriously hard. The Intel Trace Analyzer
& Collector (ITAC) can be used to generate a trace while running an
application, and visualizing it later for analysis.

Prerequisities
--------------

You will need an MPI program (C/C++ or Fortran) to instrument and run.

Step by step
------------

The following steps are the easiest way to use the Intel Trace Analyzer,
however, more sophisticated options are available.

#. Load the relevant modules. The exact modules may differ from system
   to system, but will typically include the itac module and a
   compatible Intel toolchain, e.g.,

   ::

      $ module load intel/2019a
      $ module load itac/2019.2.026


.. note::

   |UA| Users of the UAntwerpen clusters should load the ``inteldevtools``
   module instead, which makes also available Intel's debugger, VTune, Advisor 
   and Inspector development tools.

#. Compile your application so that it can generate a trace:

   ::

      $ mpiicc -trace myapp.c -o myapp
          

   where myapp.c is your C/C++ source code. For a Fortran program, this
   would be:

   ::

      $ mpiifort -trace myapp.f -o myapp
          

#. Run your application using a PBS script such as this one:

   ::

      #!/bin/bash -l
      #PBS -N myapp-job
      #PBS -l walltime=00:05:00
      #PBS -l nodes=4

      module load intel/2019a
      module load itac/2019.2.026
      # Set environment variables for ITAC.
      # Unfortunately, the name of the script differs between versions of ITAC
      source $EBROOTITAC/bin/itacvars.sh

      cd $PBS_O_WORKDIR

      mpirun -trace ./myapp
          

#. When the job is finished, check whether files with names myapp.stf.\*
   have been generated, if so, start the visual analyzer using:

   ::

      $ traceanalyzer myapp.stf
          

