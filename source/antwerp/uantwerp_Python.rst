.. _Antwerp Python:

Python on the UAntwerp clusters
===============================


Available modules
-----------------

Since Python support for Python 2 officially terminated on December 31, 2019 (even though some
months later a new bundle, Python 2.7.18, was released containing all patches that were 
accepted by December 31, 2019), we no longer actively support Python 2 on the UAntwerp clusters.
The already installed modules on Leibniz remain available on that cluster but will not be ported
to Vaughan, nor will new versions be installed.

Since the 2020a toolchains, we offer two Python distributions:
  * The regular Python module is compiled from sources with the Intel compilers. The modules also
    contain a lot of frequently used packages, including NumPy, SciPy, pandas, matplotlib and many
    others. These are usually one of the latest versions at the time of install, provided they
    compile without problems with the compilers that we use.
  * The IntelPython3 module is the Intel Python distribution that comes with Intel Parallel Studio XE,
    the Intel product that also contains the compilers, MPI library and several mathematical and other
    libraries on our cluster. The Intel Python distribution already comes with a lot of packages.
    Loading the IntelPython3-Packages module instead will add most packages included in the regular
    Python modules, though the version numbers may differ. Everything contained in the ``IntelPython3``
    modules (but not the ``IntelPython3-Packages`` modules) is covered by our support contract with 
    Intel. This implies that we can submit bug reports, though that requires a small piece of code 
    that demonstrates how the bug can be triggered.

Note that during the lifetime of a toolchain, we do update Intel Parallel Studio XE to have access
to the latest bugfixes. Hence the actual patch level of Python in the Intel Python distribution may also
vary. 

The following versions of Python are offered:

+-----------+----------------+--------------+
| Toolchain | Regular Python | IntelPython3 |
+-----------+----------------+--------------+
| 2020a     | 3.8.3          | 3.7.\*       |
+-----------+----------------+--------------+

Due to security concerns in a non-virtualized multi-user environment as a HPC cluster, and since
we have little local funding to support virtual workstations, IPython and packages derived from
IPython such as Jupyter are not supported. If you use them and if your account gets hacked because
of this (because you don't enable or disable proper security in those packages), it is your own
responsibility. For code development, there are other sufficiently user-friendly IDEs that work well
with the cluster in a safe manner.


Installing additional packages
------------------------------

There is a :ref:`page on Python package management <Python packages>` in this documentation. There are 
however a number of remarks specifically for the cluster at the University of Antwerp.

  * Python packages should never be installed on VSC_USER. There is simply not enough storage available
    on that file system. Python packages or distributions should be installed on VSC_DATA or VSC_SCRATCH.
      * **Users with a vsc2xxxx userid**: When working on the UAntwerp clusters, VSC_DATA is a local file
        system for you. We expect that for Python packages (and similarly for R and Perl packages), 
        VSC_DATA will give better performance than VSC_SCRATCH due to the amount of file metadata accesses
        that occur when running Python.
      * **Users with a different home institution**: VSC_DATA for you is a file system at your local
        institution. Due to the distance between our clusters and your home institution, file access to 
        VSC_DATA will have a high latency. Installing the packages that you need locally on VSC_SCRATCH
        will give much better performance.
  * The preferred method of installing Python packages on the UAntwerp cluster is using ``pip``, ``easy_install``
    or ``python setup``, depending on what the package supports. This does require that all non-Python and in 
    some cases Python dependencies are already installed. However, it installs a minimal number of additional files
    and makes maximum use of what is already installed on the systems. The apps directory (where all 
    centrally installed apps for the UAntwerp cluster are installed) is very fast, but that speed comes at
    a price that we cannot afford for user disk space. Note however that installing this way does have one
    pitfall that is also present in Conda: When you install from binaries available on
    `PyPi <https://pypi.org/>`_, they will likely not be optimized for the specific CPUs on our system.
    Moreover, not all binary wheels are compatible with the Linux version that we use (something Conda avoids
    by effectively installing its own Linux distribution in the Conda directories). The CalcUA support team
    always tries to compile packages from source using up-to-date compilers and only uses binary wheels when
    nothing else works in a reasonable time.
  * The use of Conda-variants is discouraged for various reasons and should only be used if nothing else works.
      * Conda installations avoid using libraries already present on the system. As such they consume a lot
        of disk space and can put a high load on the file system. Expect slower performance just because of that
        already.
      * The Conda repositories contain a mix of very well optimized binary packages and packages that are not at all
        optimized for modern CPUs. In some cases, multiple versions are available, but as a Conda user you need to be
        well aware of where to find these. (E.g., the Intel Python distribution with properly optimized NumPy, SciPy and
        a few other performance-critical packages is also available via Conda.) The generic CPU that is used for
        binaries that should run on everything is usually an ancient Pentium 4 or Core CPU. For some code, e.g., 
        dense linear algebra and FFT, using the newer instructions of more recent processors can give a big speed
        boost for those routines, e.g. up to a factor 4 on Leibniz and Vaughan.
      * As Conda effectively installs its own upper layers of a Linux/GNU-system and doesn't use security-sensitive
        libraries from our system, it is up to you to keep it secure by frequently updating. This is particularly 
        important for those packages that make connections of the internet. If you're not using any of these, this
        does not need to be a big concern. 
        
Our advise is to follow the instructions for "Installing packages using pip" or "Installing packages using easy_install"
on :ref:`the page "Python package management" <Python packages>` with one exception: At the time of writing this page,
that page still mentions::

      $ pip install --install-option="--prefix=${VSC_DATA}/python_lib" sphinx

as the command to install a package using ``pip``. On newer Python distributions, this will produce an error message
and the correct command to install ``sphinx`` is::

      $ pip install --prefix=${VSC_DATA}/python_lib sphinx



