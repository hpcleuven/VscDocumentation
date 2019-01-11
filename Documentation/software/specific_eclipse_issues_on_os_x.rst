Specific Eclipse issues on OS X
===============================

Installation
------------

Eclipse doesn't come with its own compilers. By default, it relies on
the Apple gcc toolchain. You can install this toolchain by installing
the Xcode package from the App Store. This package is free, but since it
takes quite some disk space and few users need it, it is not installed
by default on OS X (though it used to be). After installing Xcode, you
can install Eclipse according to the instructions on the Eclipse web
site. Eclipse will then use the gcc command from the Xcode distribution.
The Apple version of gcc is really just the gcc front-end layered on top
of a different compiler, LLVM, and might behave differently from gcc on
the cluster.

If you want a regular gcc or need Fortran or MPI or mathematical
libraries equivalent to those in the `foss
toolchain <\%22/cluster-doc/development/toolchain-foss\%22>`__ on the
cluster, you'll need to install additional software. We recommend `using
MacPorts <\%22https://www.macports.org/\%22>`__ for this as it contains
ports to macOS of most tools that we include in our toolchains. Using
MacPorts requires some familiarity with the bash shell, so you may have
a look at `our \\"Using Linux\"
section <\%22/cluster-doc/using-linux\%22>`__ or search the web for a
good bash tutorial (one in a Linux tutorial will mostly do). E.g.,
you'll have to add the directory where MacPort installs the applications
to your PATH enviroment variable. For a typical MacPorts installation,
this directory is /opt/local/bin.

After installing MacPorts, the following commands will install a
libraries and tools that are very close to those of the foss2016b
toolchain (tested September 2016):

::

   sudo port install gcc5
   sudo port select --set gcc mp-gcc5
   sudo port install openmpi-gcc5 +threads
   sudo port select --set mpi openmpi-gcc5-fortran
   sudo port install OpenBLAS +gcc5 +lapack
   sudo port install scalapack +gcc5 +openmpi
   sudo port install fftw-3 +gcc5 +openmpi

Some components may be slightly newer versions than provided in the
foss2015a toolchain, while the MPI library is an older version (at least
when tested in September 2016).

If you also want a newer version of subversion that can integrate with
the \\"Native JavaHL connector\" in Eclipse, the following commands will
install the appropriate packages:

::

   sudo port install subversion
   sudo port install subversion-javahlbindings

At the time of writing, this installed version 1,9,4 of subversion which
has a compatielbe \\"Native JavaHL connector\" in Eclipse.

Configurating Eclipse for other compilers
-----------------------------------------

Eclipse uses the PATH environment variable to find other software it
uses, such as compilers but also some commands that give information on
where certain libraries are stored or how they are configured. In a
regular UNIX/Linux system, you'd set the variable in your shell
configuration files (e.g., ``.bash_profile`` if you use the bash shell).
This mechanism also works on OS X, but not for applications that are not
started from the shell but from the Dock or by clicking on their icon in
the Finder.

Because of security concerns, Apple has made it increasingly difficult
to define the path for GUI applications that are not started through a
shell script.

-  In 10.7 and earlier, one could define environment variables for GUI
   applications in ``~/.MacOSX/environment.plist``.
-  In 10.8 and 10.9 one had to modify the ``Info.plist`` file in the
   so-called application bundle.

Both tricks are explained in the `Photran installation instructions on
the Eclispe
wiki <\%22https://wiki.eclipse.org/PTP/photran/documentation\%22>`__.
However, in OS X 10.10 (Yosemite) neither mechanism works for setting
the path.

Our advise is to:

-  Configure your bash shell so that you can find the gfortran
   executable and the corresponding gcc executable. (E.g., try
   ``gfortran --version`` and <code>gcc --version and check the output
   of these commands).
-  Then start Eclipse also from a terminal window.

   -  Use the full path, for the default install procedure this is very
      likely ``/Application/eclipse/eclipse``,
   -  or add the path to Eclipse to the PATH environment variable (so
      you likely have to add ``/Application/eclipse`` to the path),
   -  or define an alias to start Eclipse, e.g., by adding the line
      ``alias start-eclipse='/Applications/eclipse/eclipse >&/dev/null &'``
      to your ``.bashrc`` file. This line defines a new command
      ``start-eclipse``.

   This should work for all OS X versions.

"
