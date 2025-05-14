.. _MATLAB getting started:

MATLAB getting started
======================

MATLAB has to be loaded using the module utility prior to running it.
This ensures that the environment is correctly set. Get the list of
available versions of MATLAB using::

   $ module avail matlab

(KU Leuven clusters) or::

   $ module avail MATLAB

(UAntwerpen and VUB clusters).

Load a specific version by specifying the MATLAB version in the command::

   $ module load matlab/R2014a

or::

   $ module load MATLAB/2014a

depending on the site you're at.


Interactive use
---------------

-  Interactive use is possible, but is not the preferred way of using
   on the cluster! Use batch processing of compiled MATLAB code
   instead.
-  If there is an X Window System server installed on your PC (as is by
   default the case under :ref:`linux_client`; you can use
   XMing Server under :ref:`windows_client` or XQuartz
   on :ref:`macOS/OS X <macos_client>`), the full graphical
   MATLAB Desktop is available. If the speed is acceptable to you - much
   of the MATLAB user interface is coded in Java and Java programs are
   known to be slow over remote X connections - this is the recommended
   way to start MATLAB for short testing purposes, simple calculations,
   writing programs, visualizing data. Please avoid doing extensive
   calculations this way, as you would be abusing the resources of the
   shared login-node. Your program will disturb other users, and other
   users will slow down execution of your program. Moreover, only a
   limited amount of CPU time is available to you, after which your
   session will be killed (with possible data loss).
-  With ``matlab -nodesktop`` you can start MATLAB without the full
   desktop, while you are still able to use the visualization features.
   The ``helpwin``, ``helpdesk`` and ``edit`` commands also work and
   open GUI-style help windows or a GUI-based editor. Of course this
   also requires a X server.
-  You can always, i.e., without X-Window server, start MATLAB in
   console-mode, via::

      $ matlab -nodisplay

   You get a MATLAB command prompt, from where you can start m-files,
   but have no access to the graphical facilities. The same limitations
   as above on CPU time apply.

-  For intensive calculations you want to run interactively, it is
   possible to use the PBS Job system to reserve a node for your
   exclusive use, while still having access to, e.g., the graphical
   capabilities of MATLAB, by forwarding the X output (``qsub -X -I``).
-  WARNING: an interactive MATLAB session on a compute node can be very
   slow. A workaround (found at `hpc.uark.edu <https://hpc.uark.edu/>`_) is:

   -  launch an interactive session ``qsub -I -X``
   -  once the interactive session is started, (say it starts on
      ``r2i0n15``), start another connection to that compute node (``ssh -X
      r2i0n15``). In this second connection, start MATLAB, and it will
      work at normal speed.


Batch use
---------

For any non-trivial calculation, it is strongly suggested that you use
the PBS batch system.

Running a MATLAB script
~~~~~~~~~~~~~~~~~~~~~~~

You first have to write a MATLAB m-file that executes the required
calculation. Make sure the last command of this m-file is ``quit`` or
``exit``, otherwise MATLAB might wait forever for more commands ...

Example (to be saved, e.g., in ``testmatlabscript.m``)::

   ndim = 600;
   a = rand(600,1)*10;
   b = rand(1,600)*100;
   c = a * b;
   d = max(c);
   e = min(d);
   save('testmatlab', 'd', 'e');
   exit;

You can now run this program (as a test, still on the login node, from
the directory where you saved the file ``testmatlabscript.m``)::

   matlab  -nodisplay -r testmatlabscript

The next thing is to write a small shell script, to be sent to the PBS
Job System, so that the program can be executed on a compute node,
rather than on the login node.

For information on how to run jobs on the VSC cluster, see the :ref:`documentation
of the job system <running jobs>`.  Below you will find a quick run through
for the impatient, but make sure to familiarize yourself with the details.

A simple example follows (to be saved in, e.g.,  ``testmatlabscript.sh``)::

   #!/bin/bash -l
   # The maximum duration of the program,
   #   in the format [days:]hours:minutes:seconds
   #PBS -l walltime=01:00:00
   # the requested amount of RAM
   #PBS -l pmem=950mb
   # The name of your job (used in mail, outputfile, showq,...)
   #PBS -N matlab_test_job
   # Set the correct environment for MATLAB
   module load matlab
   # Go into the directory from where 'qsub' was run
   cd $PBS_O_WORKDIR
   # Start MATLAB, specify the correct command-file ...
   matlab -nojvm -nodisplay -r test

Now you submit your job with::

   $ qsub testmatlabscript.sh

and you get the job ID that was assigned to your job. You get an overview
of the status of your jobs using::

   $ qstat

When the job has run,
output will be available in the file ``<jobname>.o<jobid>`` in the directory
where you submitted the job from. In the case of the file
``testmatlabscript.m`` above, a file ``testmatlabscript.mat`` will have been
created, with the calculated data ``d`` and ``e``, you can load the resulting
file into MATLAB for further processing.


Running a MATLAB function
~~~~~~~~~~~~~~~~~~~~~~~~~

If instead of a script, a MATLAB function is used, parameters can be
passed into the function.

Example (to be saved, e.g., in ``testmatlabfunction.m``)::

   function testmatlabfunction(input1,input2)
   % source: https://wiki.inf.ed.ac.uk/ANC/MatlabComputing
   % change arguments to numerics if necessary - only when compiling code
   if ~isnumeric(input1)
      input1n = str2num(input1);
      input2n = str2num(input2);
   else
      input1n = input1;
      input2n = input2;
   end
   sumofinputs = input1n + input2n;
   outputfilename = ['testfunction_' num2str(input1n) '_' num2str(input2n)];
   save(outputfilename, 'input1n', 'input2n', 'sumofinputs');
   exit;

You can now run this program (as a test, still on the login node, from
the directory were you saved the file ``testmatlabfunction.m``)::

   $ matlab  -nodisplay -r "testmatlabfunction 3 6"

.. note::

   - The quotes around the function name and the parameters are required;
   - the function name does not include the ``*.m`` extension.


MATLAB compiler
---------------

Each job requires a MATLAB license while running. If you start lots of
jobs, you'll use lots of licenses. When all licenses are in use, your
further jobs will fail, and you'll block access to MATLAB for other
people at your site.

However, when compiling your MATLAB program, no more runtime licenses
are needed.

Compilation of MATLAB files is relatively easy with the MATLAB 'mcc'
compiler. It works for 'function m-files' and for 'script m-files'.
'function m-files' are however preferred.

To deploy a MATLAB program as a standalone application, load the module
for MATLAB as a first step and compile the code in a second step with
the mcc command.

If we want to compile a MATLAB program 'main.m', the corresponding
command line should be::

   $ mcc  -v  -R -singleCompThread  -m  main.m

Where the options are:

-  ``-m``: generate a standalone application
-  ``-v``: verbose display of the compilation steps
-  ``-R``: runtime options, useful ones are: ``-singleCompThread``, ``-nodisplay``,
   ``-nojvm``

The deployed executable is compiled to run using a single thread via
the option ``-singleCompThread``. This is important when a number of processes
are to run concurrently on the same node (e.g., worker framework).

In addition to the MATLAB executable (``main`` in this example), the compiler
also generates a wrapper file (``run_main.sh`` in this example) that can be
used to invoke the MATLAB executable. It sets environment variable LD_LIBRARY_PATH
to make sure that the MATLAB runtime libraries can be found by the executable,
and next runs the executable.

The wrapper expects a first argument that provides the rootdir of the MATLAB
installation that is being used. With a MATLAB module, that rootdir is given
by environment variable EBROOTMATLAB. Additional arguments are passed on to the 
compiled executable.

.. note::

   -  Parameters are always considered as strings, and thus have to be
      converted to, e.g., numbers inside your function when needed. You can
      test with ``isdeployed`` or ``isstr`` MATLAB functions (see examples).
   -  The function is allowed to return a value, but that value is *not*
      returned to the shell. Thus, to get results out, they have to be
      written to the screen, or saved in a file.
   -  Not all MATLAB functions are allowed in compiled code (`see the
      "Compiler Support for MATLAB and Toolboxes" page at the
      MathWorks <https://nl.mathworks.com/products/compiler/supported/compiler_support.html>`__).

Example 1: Simple MATLAB script file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file ``fibonacci.m`` contains::

   function a = fibonacci(n)
   % FIBONACCI Calculate the fibonacci value of n.
   % When complied as standalone function,
   % arguments are always passed as strings, not numbers ...
   if (isstr(n))
       n = str2num(n);
   end;
   if (length(n)~=1) || (fix(n) ~= n) || (n < 0)
       error(['MATLAB:factorial:NNotPositiveInteger', ...
              'N must be a positive integer.']);
   end
   first = 0;second = 1;
   for i=1:n-1
       next = first+second;
       first=second;
       second=next;
   end
   % When called from a compiled application, display result
   if (isdeployed)
       disp(sprintf('Fibonacci %d -> %d' , n,first))
   end
   % Also return the result, so that the function remains usable
   % from other MATLAB scripts.
   a=first;

Run the compiler::

    $ mcc -m fibonacci

This creates MATLAB executable file ``fibonacci`` and wrapper file
``run_fibonnacci.sh``.

You can now run your application as follows::

   $ ./run_fibonacci.sh $EBROOTMATLAB 6
   Fibonacci 6 -> 5
   $ ./run_fibonacci.sh $EBROOTMATLAB 8
   Fibonacci 8 -> 13
   $ ./run_fibonacci.sh $EBROOTMATLAB 45
   Fibonacci 45 -> 701408733


Example 2 : Function that uses other MATLAB files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file ``multi_fibo.m`` contains::

   function multi_fibo()
   %MULTIFIBO Calls FIBONACCI multiple times in a loop
   % Function calculates Fibonacci number for a matrix by calling the
   % fibonacci function in a loop. Compiling this file would automatically
   % compile the fibonacci function also because dependencies are
   % automatically checked.
   n=10:20
   if max(n)<0
       f = NaN;
   else
       [r c] = size(n);
       for i = 1:r %#ok
           for j = 1:c %#ok
               try
                   f(i,j) = fibonacci(n(i,j));
               catch
                   f(i,j) = NaN;
               end
           end
       end
   end

Compile the file::

   $ mcc -m multi_fibo

Run the executable::

   ./run_multi_fibo.sh $EBROOTMATLAB
   n =
       10    11    12    13    14    15    16    17    18    19    20
   Fibonacci 10 -> 34
   Fibonacci 11 -> 55
   Fibonacci 12 -> 89
   Fibonacci 13 -> 144
   Fibonacci 14 -> 233
   Fibonacci 15 -> 377
   Fibonacci 16 -> 610
   Fibonacci 17 -> 987
   Fibonacci 18 -> 1597
   Fibonacci 19 -> 2584
   Fibonacci 20 -> 4181
   f =
             34          55          89         144         233         
   377         610         987        1597        2584        4181


Example 3 : Function that used other MATLAB files in other directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your script uses MATLAB files (e.g., self-made scripts, compiled
mex files) other than those part of the MATLAB-distribution, include
them at compile time as follows::

   $ mcc -m  -I /path/to/MyMatlabScripts1/  -I /path/to/MyMatlabScripts2 .... \
             -I /path/to/MyMatlabScriptsN multi_fibo


More info on the MATLAB Compiler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`MATLAB compiler documentation`_ on the Mathworks website. 

