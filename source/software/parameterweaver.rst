ParameterWeaver
===============

Introduction & motivation
-------------------------

When working on the command line such as in the Bash shell, applications
support command line flags and parameters. Many programming languages
offer support to conveniently deal with command line arguments out of
the box, e.g., Python. However, quite a number of languages used in a
scientific context, e.g., C/C++, Fortran, R, Matlab do not. Although
those languages offer the necessary facilities, it is at best somewhat
cumbersome to use them, and often the process is rather error prone.

Quite a number of libraries have been developed over the years that can
be used to conveniently handle command line arguments. However, this
complicates the deployment of the application since it will have to rely
on the presence of these libraries.

ParameterWeaver has a different approach: it generates the necessary
code to deal with the command line arguments of the application in the
target language, so that these source files can be distributed along
with those of the application. This implies that systems that don't have
ParameterWeaver installed still can run that application.

Using ParameterWeaver is as simple as writing a definition file for the
command line arguments, and executing the code generator via the command
line. This can be conveniently integrated into a standard build process
such as make.

ParameterWeaver currently supports the following target languages:

-  C/C++
-  Fortran 90
-  R

High-level overview & concepts
------------------------------

Parameter definition files
~~~~~~~~~~~~~~~~~~~~~~~~~~

A parameter definition file is a CSV text file where each line defines a
parameter. A parameter has a type, a name, a default values, and
optionally, a description. To add documentation, comments can be added
to the definition file. The types are specific to the target language,
e.g., an integer would be denoted by ``int`` for C/C++, and by
``integer`` for Fortran 90. The supported types are documented for each
implemented target language.

By way of illustration, a parameter definition file is given below for C
as a target language, additional examples are shown in the target
language specific sections:

::

   int,numParticles,1000,number of particles in the system
   double,temperature,273,system temperature in Kelvin
   char*,intMethod,'newton',integration method to use

Note that this parameter definition file should be viewed as an integral
part of the source code.

Code generation
~~~~~~~~~~~~~~~

ParameterWeaver will generate code to

#. initialize the parameter variables to the default values as specified
   in the parameter definition file;
#. parse the actual command line arguments at runtime to determine the
   user specified values, and
#. print the values of the parameters to an output stream.

The implementation and features of the resulting code fragments are
specific to the target language, and try to be as close as possible to
the idioms of that language. Again, this is documented for each target
language specifically. The nature and number of these code fragments
varies from one target language to the other, again trying to match the
language's idioms as closely as possible. For C/C++, a declaration file
(``.h``) and a definition file (``.c``), while for Fortran 90 a single
file (``.f90`` will be generated that contains both declarations and
definitions.

Language specific documentation
-------------------------------

C/C++ documentation
~~~~~~~~~~~~~~~~~~~

Data types
^^^^^^^^^^

For C/C++, ParameterWeaver supports the following data types:

#. ``int``
#. ``long``
#. ``float``
#. ``double``
#. ``bool``
#. ``char *``

Example C program
^^^^^^^^^^^^^^^^^

Suppose we want to pass command line parameters to the following C
program:

::

   #include 
   #include 
   #include 
   int main(int argc, char *argv[]) {
       FILE *fp;
       int i;
       if (strlen(out) > 0) {
           fp = fopen(out, \"w\");
       } else {
           fp = stdout;
       }
       if (verbose) {
           fprintf(fp, \"# n = %d\\n\", n);
           fprintf(fp, \"# alpha = %.16f\\n\", alpha);
           fprintf(fp, \"# out = '%s'\\n\", out);
           fprintf(fp, \"# verbose = %s\\n\", verbose);
       }
       for (i = 0; i < n; i++) {
           fprintf(fp, \"%d\\t%f\\n\", i, i*alpha);
       }
       if (fp != stdout) {
           fclose(fp);
       }
       return EXIT_SUCCESS;
   }

We would like to set the number of iterations ``n``, the factor
``alpha``, the name of the file to write the output to ``out`` and the
verbosity ``verbose`` at runtime, i.e., without modifying the source
code of this program.

Moreover, the code to print the values of the variables is error prone,
if we later add or remove a parameter, this part of the code has to be
updated as well.

Defining the command line parameters in a parameter definition file to
automatically generate the necessary code simplifies matters
considerably.

Example parameter definition file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following file defines four command line parameters named ``n``,
``alpha``, ``out`` and ``verbose``. They are to be interpreted as
``int``, ``double``, ``char`` pointer and ``bool`` respectively, and if
no values are passed via the command line, they will have the default
values ``10``, ``0.19``, ``output.txt`` and false respectively. Note
that a string default value is quoted. In this case, the columns in the
file are separated by tab characters. The following is the contents of
the parameter definition file ``param_defs.txt``:

::

   int n   10
   double  alpha   0.19
   char *  out 'output.txt'
   bool    verbose false

This parameter definition file can be created in a text editor such as
the one used to write C program, or from a Microsoft Excel worksheet by
saving the latter as a CSV file.

As mentioned above, boolean values are also supported, however, the
semantics is slightly different from other data types. The default value
of a logical variable is always false, regardless of what is specified
in the parameter definition file. As opposed to parameters of other
types, a logical parameter acts like a flag, i.e., it is a command line
options that doesn't take a value. Its absence is interpreted as false,
its presence as true. Also note that using a parameter of type ``bool``
implies that the program will have to be complied as C99, rather than
C89. All modern compiler fully support C99, so that should not be an
issue. However, if your program needs to adhere strictly to the C89
standard, simply use a parameter of type ``int`` instead, with ``0``
interpreted as false, all other values as true. In that case, the option
takes a value on the command line.

Generating code
^^^^^^^^^^^^^^^

Generating the code fragments is now very easy. If appropriate, load the
module (VIC3):

::

   $ module load parameter-weaver

Next, we generate the code based on the parameter definition file:

::

   $ weave -l C -d param_defs.txt

A number of type declarations and functions are generated, the
declarations in the header file ``cl_params.h``, the definitions in the
source file ``cl_params.c``.

#. data structure: a type ``Params`` is defined as a ``typedef`` of a
   ``struct`` with the parameters as fields, e.g.,

   ::

      typedef struct {
          int n;
          double alpha;
          char *out;
          bool verbose;
      } Params;
          

#. Initialization function: the default values of the command line
   parameters are assigned to the fields of the ``Params`` variable, the
   address of which is passed to the function
#. Parsing: the options passed to the program via the command line are
   assigned to the appropriate fields of the ``Params`` variable.
   Moreover, the ``argv`` array containing the remaining command line
   arguments, the ``argc`` variable is set appropriately.
#. Dumper: a function is defined that takes three arguments: a file
   pointer, a prefix and the address of a ``Params`` variable. This
   function writes the values of the command line parameters to the file
   pointer, each on a separate line, preceeded by the specified prefix.
#. Finalizer: a function that deallocates memory allocated in the
   initialization or the parsing functions to avoid memory leaks.

Using the code fragments
^^^^^^^^^^^^^^^^^^^^^^^^

The declarations are simply included using preprocessor directives:

::

     #include \"cl_params.h\"

A variable to hold the parameters has to be defined and its values
initialized:

::

     Params params;
     initCL(&params);

Next, the command line parameters are parsed and their values assigned:

::

     parseCL(&params, &argc, &argv);

The dumper can be called whenever the user likes, e.g.,

::

     dumpCL(stdout, \"\", &params);

The code for the program is thus modified as follows:

::

   #include 
   #include 
   #include 
   #include \"cl_params.h\"
   int main(int argc, char *argv[]) {
       FILE *fp;
       int i;
       Params params;
       initCL(&params);
       parseCL(&params, &argc, &argv);
       if (strlen(params.out) > 0) {
           fp = fopen(params.out, \"w\");
       } else {
           fp = stdout;
       }
       if (params.verbose) {
           dumpCL(fp, \"# \", &params);
       }
       for (i = 0; i < params.n; i++) {
           fprintf(fp, \"%d\\t%f\\n\", i, i*params.alpha);
       }
       if (fp != stdout) {
           fclose(fp);
       }
       finalizeCL(&params);
       return EXIT_SUCCESS;
   }

Note that in this example, additional command line parameters are simply
ignored. As mentioned before, they are available in the array ``argv``,
``argv[0]`` will hold the programs name, subsequent elements up to
``argc - 1`` contain the remaining command line parameters.

Fortran 90 documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. _data-types-1:

Data types
^^^^^^^^^^

For Fortran 90, ParameterWeaver supports the following data types:

#. ``integer``
#. ``real``
#. ``double precision``
#. ``logical``
#. ``character(len=1024)``

Example Fortran 90 program
^^^^^^^^^^^^^^^^^^^^^^^^^^

Suppose we want to pass command line parameters to the following Fortran
program:

::

   program main
   use iso_fortran_env
   implicit none
   integer :: unit_nr = 8, i, istat
   if (len(trim(out)) > 0) then
       open(unit=unit_nr, file=trim(out), action=\"write\")
   else
       unit_nr = output_unit
   end if
   if (verbose) then
       write (unit_nr, \"(A, I20)\") \"# n = \", n
       write (unit_nr, \"(A, F24.15)\") \"# alpha = \", alpha
       write (unit_nr, \"(A, '''', A, '''')\") \"# out = \", out
       write (unit_nr, \"(A, L)\") \"# verbose = \", verbose
   end if
   do i = 1, n
       write (unit_nr, \"(I3, F5.2)\") i, i*alpha
   end do
   if (unit_nr /= output_unit) then
       close(unit=unit_nr)
   end if
   stop
   end program main

We would like to set the number of iterations ``n``, the factor
``alpha``, the name of the file to write the output to ``out`` and the
verbosity ``verbose`` at runtime, i.e., without modifying the source
code of this program.

Moreover, the code to print the values of the variables is error prone,
if we later add or remove a parameter, this part of the code has to be
updated as well.

Defining the command line parameters in a parameter definition file to
automatically generate the necessary code simplifies matters
considerably.

.. _example-parameter-definition-file-1:

Example parameter definition file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following file defines four command line parameters named ``n``,
``alpha``, ``out`` and ``verbose``. They are to be interpreted as
``integer``, ``double precision``, ``character(len=1024)`` pointer and
``logical`` respectively, and if no values are passed via the command
line, they will have the default values ``10``, ``0.19``, ``output.txt``
and false respectively. Note that a string default value is quoted. In
this case, the columns in the file are separated by tab characters. The
following is the contents of the parameter definition file
``param_defs.txt``:

::

   integer n   10
   double precision    alpha   0.19
   character(len=1024) out 'output.txt'
   logical verbose false

This parameter definition file can be created in a text editor such as
the one used to write the Fortran program, or from a Microsoft Excel
worksheet by saving the latter as a CSV file.

As mentioned above, logical values are also supported, however, the
semantics is slightly different from other data types. The default value
of a logical variable is always false, regardless of what is specified
in the parameter definition file. As opposed to parameters of other
types, a logical parameter acts like a flag, i.e., it is a command line
options that doesn't take a value. Its absence is interpreted as false,
its presence as true.

.. _generating-code-1:

Generating code
^^^^^^^^^^^^^^^

Generating the code fragments is now very easy. If appropriate, load the
module (VIC3):

::

   $ module load parameter-weaver

Next, we generate the code based on the parameter definition file:

::

   $ weave -l Fortran -d param_defs.txt

A number of type declarations and functions are generated in the module
file ``cl_params.f90``.

#. data structure: a type ``params_type`` is defined as a ``structure``
   with the parameters as fields, e.g.,

   ::

          type :: params_type
              integer :: n
              double precision :: alpha
              character(len=1024) :: out
              logical :: verbose
          end type params_type
          

#. Initialization function: the default values of the command line
   parameters are assigned to the fields of the ``params_type`` variable
#. Parsing: the options passed to the program via the command line are
   assigned to the appropriate fields of the ``params_type`` variable.
   Moreover, the ``next`` variable of type ``integer`` will hold the
   index of the next command line parameter, i.e., the first of the
   remaining command line parameters that was not handled by the parsing
   function.
#. Dumper: a function is defined that takes three arguments: a unit
   number for output, a prefix and the ``params_type`` variable. This
   function writes the values of the command line parameters to the
   output stream associated with the unit number, each on a separate
   line, preceded by the specified prefix.

.. _using-the-code-fragments-1:

Using the code fragments
^^^^^^^^^^^^^^^^^^^^^^^^

The module file is included by the ``use`` directive:

::

     use cl_parser

A variable to hold the parameters has to be defined and its values
initialized:

::

     type(params_type) :: params
     call init_cl(params)

Next, the command line parameters are parsed and their values assigned:

::

       integer :: next
       call parse_cl(params, next)

The dumper can be called whenever the user likes, e.g.,

::

     call dump_cl(output_unit, \"\", params)

The code for the program is thus modified as follows:

::

   program main
   use cl_params
   use iso_fortran_env
   implicit none
   type(params_type) :: params
   integer :: unit_nr = 8, i, istat, next
   call init_cl(params)
   call parse_cl(params, next)
   if (len(trim(params % out)) > 0) then
       open(unit=unit_nr, file=trim(params % out), action=\"write\")
   else
       unit_nr = output_unit
   end if
   if (params % verbose) then
       call dump_cl(unit_nr, \"# \", params)
   end if
   do i = 1, params % n
       write (unit_nr, \"(I3, F5.2)\") i, i*params % alpha
   end do
   if (unit_nr /= output_unit) then
       close(unit=unit_nr)
   end if
   stop
   end program main

Note that in this example, additional command line parameters are simply
ignored. As mentioned before, they are available using the standard
``get_command_argument`` function, starting from the value of the
variable ``next`` set by the call to ``parse_cl``.

R documentation
~~~~~~~~~~~~~~~

.. _data-types-2:

Data types
^^^^^^^^^^

For R, ParameterWeaver supports the following data types:

#. ``integer``
#. ``double``
#. ``logical``
#. ``string``

Example R script
^^^^^^^^^^^^^^^^

Suppose we want to pass command line parameters to the following R
script:

::

   if (nchar(out) > 0) {
       conn <- file(out, 'w')
   } else {
       conn = stdout()
   }
   if (verbose) {
       write(sprintf(\"# n = %d\\n\", n), conn)
       write(sprintf(\"# alpha = %.16f\\n\", alpha), conn)
       write(sprintf(\"# out = '%s'\\n\", out), conn)
       write(sprintf(\"# verbose = %s\\n\", verbose), conn)
   }
   for (i in 1:n) {
       write(sprintf(\"%d\\t%f\\n\", i, i*alpha), conn)
   }
   if (conn != stdout()) {
       close(conn)
   }

We would like to set the number of iterations ``n``, the factor
``alpha``, the name of the file to write the output to ``out`` and the
verbosity ``verbose`` at runtime, i.e., without modifying the source
code of this script.

Moreover, the code to print the values of the variables is error prone,
if we later add or remove a parameter, this part of the code has to be
updated as well.

Defining the command line parameters in a parameter definition file to
automatically generate the necessary code simplifies matters
considerably.

.. _example-parameter-definition-file-2:

Example parameter definition file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following file defines four command line parameters named ``n``,
``alpha``, ``out`` and ``verbose``. They are to be interpreted as
``integer``, ``double``, string and ``logical`` respectively, and if no
values are passed via the command line, they will have the default
values ``10``, ``0.19``, ``output.txt`` and false respectively. Note
that a string default value is quoted, just as it would be in R code. In
this case, the columns in the file are separated by tab characters. The
following is the contents of the parameter definition file
``param_defs.txt``:

::

   integer n   10
   double  alpha   0.19
   string  out 'output.txt'
   logical verbose F

This parameter definition file can be created in a text editor such as
the one used to write R scripts, or from a Microsoft Excel worksheet by
saving the latter as a CSV file.

As mentioned above, logical values are also supported, however, the
semantics is slightly different from other data types. The default value
of a logical variable is always false, regardless of what is specified
in the parameter definition file. As opposed to parameters of other
types, a logical parameter acts like a flag, i.e., it is a command line
options that doesn't take a value. Its absence is interpreted as false,
its presence as true.

.. _generating-code-2:

Generating code
^^^^^^^^^^^^^^^

Generating the code fragments is now very easy. If appropriate, load the
module (VIC3):

::

   $ module load parameter-weaver

Next, we generate the code based on the parameter definition file:

::

   $ weave -l R -d param_defs.txt

Three code fragments are generated, all grouped in a single R file
``cl_params.r``.

#. Initialization: the default values of the command line parameters are
   assigned to global variables with the names as specified in the
   parameter definition file.
#. Parsing: the options passed to the program via the command line are
   assigned to the appropriate variables. Moreover, an array containing
   the remaining command line arguments is created as ``cl_params``.
#. Dumper: a function is defined that takes two arguments: a file
   connector and a prefix. This function writes the values of the
   command line parameters to the file connector, each on a separate
   line, preceded by the specified prefix.

.. _using-the-code-fragments-2:

Using the code fragments
^^^^^^^^^^^^^^^^^^^^^^^^

The code fragments can be included into the R script by sourcing it:

::

     source(\"cl_parser.r\")

The parameter initialization and parsing are executed at this point, the
dumper can be called whenever the user likes, e.g.,

::

     dump_cl(stdout(), \"\")

The code for the script is thus modified as follows:

::

   source('cl_params.r')
   if (nchar(out) > 0) {
       conn <- file(out, 'w')
   } else {
       conn = stdout()
   }
   if (verbose) {
       dump_cl(conn, \"# \")
   }
   for (i in 1:n) {
       cat(paste(i, \"\\t\", i*alpha), file = conn, sep = \"\\n\")
   }
   if (conn != stdout()) {
       close(conn)
   }

Note that in this example, additional command line parameters are simply
ignored. As mentioned before, they are available in the vector
``cl_params`` if needed.

Octave documentation
~~~~~~~~~~~~~~~~~~~~

.. _data-types-3:

Data types
^^^^^^^^^^

For Octave, ParameterWeaver supports the following data types:

#. ``double``
#. ``logical``
#. ``string``

Example Octave script
^^^^^^^^^^^^^^^^^^^^^

Suppose we want to pass command line parameters to the following Octave
script:

::

   if (size(out) > 0)
       fid = fopen(out, \"w\");
   else
       fid = stdout;
   end
   if (verbose)
       fprintf(fid, \"# n = %.16f\\n\", prefix, params.n);
       fprintf(fid, \"# alpha = %.16f\\n\", alpha);
       fprintf(fid, \"# out = '%s'\\n\", out);
       fprintf(fid, \"# verbose = %1d\\n\", verbose);
   end
   for i = 1:n
       fprintf(fid, \"%d\\t%f\\n\", i, i*alpha);
   end
   if (fid != stdout)
       fclose(fid);
   end

We would like to set the number of iterations ``n``, the factor
``alpha``, the name of the file to write the output to ``out`` and the
verbosity ``verbose`` at runtime, i.e., without modifying the source
code of this script.

Moreover, the code to print the values of the variables is error prone,
if we later add or remove a parameter, this part of the code has to be
updated as well.

Defining the command line parameters in a parameter definition file to
automatically generate the necessary code simplifies matters
considerably.

.. _example-parameter-definition-file-3:

Example parameter definition file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following file defines four command line parameters named ``n``,
``alpha``, ``out`` and ``verbose``. They are to be interpreted as
``double``, ``double``, string and ``logical`` respectively, and if no
values are passed via the command line, they will have the default
values ``10``, ``0.19``, ``output.txt`` and false respectively. Note
that a string default value is quoted, just as it would be in Octave
code. In this case, the columns in the file are separated by tab
characters. The following is the contents of the parameter definition
file ``param_defs.txt``:

::

   double  n   10
   double  alpha   0.19
   string  out 'output.txt'
   logical verbose F

This parameter definition file can be created in a text editor such as
the one used to write Octave scripts, or from a Microsoft Excel
worksheet by saving the latter as a CSV file.

As mentioned above, logical values are also supported, however, the
semantics is slightly different from other data types. The default value
of a logical variable is always false, regardless of what is specified
in the parameter definition file. As opposed to parameters of other
types, a logical parameter acts like a flag, i.e., it is a command line
options that doesn't take a value. Its absence is interpreted as false,
its presence as true.

.. _generating-code-3:

Generating code
^^^^^^^^^^^^^^^

Generating the code fragments is now very easy. If appropriate, load the
module (VIC3):

::

   $ module load parameter-weaver

Next, we generate the code based on the parameter definition file:

::

   $ weave -l octave -d param_defs.txt

Three code fragments are generated, each in its own file, i.e.,
``init_cl.m``, ``parse_cl.m``, and ``dump_cl.m``.r.

#. Initialization: the default values of the command line parameters are
   assigned to global variables with the names as specified in the
   parameter definition file.
#. Parsing: the options passed to the program via the command line are
   assigned to the appropriate variables. Moreover, an array containing
   the remaining command line arguments is returned as the second value
   from ``parse_cl``.
#. Dumper: a function is defined that takes two arguments: a file
   connector and a prefix. This function writes the values of the
   command line parameters to the file connector, each on a separate
   line, preceded by the specified prefix.

.. _using-the-code-fragments-3:

Using the code fragments
^^^^^^^^^^^^^^^^^^^^^^^^

The generated functions can be used by simply calling them from the main
script. The code for the script is thus modified as follows:

::

   params = init_cl();
   params = parse_cl(params);
   if (size(params.out) > 0)
       fid = fopen(params.out, \"w\");
   else
       fid = stdout;
   end
   if (params.verbose)
       dump_cl(stdout, \"# \", params);
   end
   for i = 1:params.n
       fprintf(fid, \"%d\\t%f\\n\", i, i*params.alpha);
   end
   if (fid != stdout)
       fclose(fid);
   end

Note that in this example, additional command line parameters are simply
ignored. As mentioned before, they are can be obtained as the second
return value from the call to ``parse_cl``.

Future work
-----------

The following features are planned in future releases:

-  Additional target languages:

   -  Matlab
   -  Java

   Support for Perl and Python is not planned, since these language have
   facilities to deal with command line arguments in their respective
   standard libraries.
-  Configuration files are an alternative way to specify parameters for
   an application, so ParameterWeaver will also support this in a future
   release.

Contact & support
-----------------

Bug reports and feature request can be sent to `Geert Jan
Bex <mailto:geertjan.bex@uhasselt.be>`__.
