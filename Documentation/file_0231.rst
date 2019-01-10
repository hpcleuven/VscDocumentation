R command line arguments in scripts
===================================

Purpose
-------

Here it is shown how to use Rscript and pass arguments to an R script.

Prerequisites
-------------

It is assumed that the reader is familiar with the use of R as well as R
scripting, and is familiar wth the linux bash shell.

Using Rscript and command line arguments
----------------------------------------

When performing computation on the cluster using R, it is necessary to
run those scripts from the command line, rather than interactively using
R's graphical user interface. Consider the following R function that is
defined in, e.g., 'logistic.R':

::

   logistic <- function(r, x) {    r*x*(1.0 - x)
   }

From R's GUI interface, you typically use this from the console as
follows:

::

   > source(\"logistic.R\")
   > logistic(3.2, 0.5)

It is trivial to write an R script 'logistic-wrapper.R' that can be run
from the command line, and that takes to arguments, the first being 'r',
the second 'x'.

::

   args <- commandArgs(TRUE)
   r <- as.double(args[1])
   x <- as.double(args[2])

   source(\"logistic.R\")

   logistic(r, x)

The first line of this script stores all arguments passed to the script
in the array 'args. The second (third) line converts the first (second)
element of that array from a string to a double precision number using
the function 'as.double', and stores it into r (x).

Now from the linux command line, one can run the script above for r =
3.2 and x = 0.5 as follows:

::

   $ Rscript logistic-wrapper.R 3.2 0.5

Note that you should have loaded the appropriate R module, e.g.,

::

   $ module load R

Suppose now that the script needs to be extended to iterate the logistic
map 'n' times, where the latter value is passed as the third argument to
the script.

::

   args <- commandArgs(TRUE)
   r <- as.double(args[1])
   x <- as.double(args[2])
   n <- as.integer(args[3])

   source(\"logistic.R\")

   for (i in 1:n) x <- logistic(r, x)
   print(x)

Note that since the the third argument represents the number of
iterations, it should be interpreted as an integer value, and hence be
converted appropriately using the function 'as.integer'.

The script is now invoked from the linux command line with three
parameters as follows:

::

   $ Rscript cl.R 3.2 0. 5 100

Note that if you pass an argument that is to be interpreted as a string
in your R program, no conversion is needed, e.g.,

::

   name <- args[4]

Here it is assumed that the 'name' is passed as the fourth command line
argument.

"
