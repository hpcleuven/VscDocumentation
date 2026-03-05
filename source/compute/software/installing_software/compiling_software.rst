.. _compiling_software:

Compiling software
==================

Some software distributed as source code must be **compiled** before it can run on a computer. 
Compilation translates human-readable source code into machine code that the system can be execute.

Many scientific applications written in low-level languages such as C, C++, or Fortran require compilation. 
Other languages such as Rust or Go also compile programs into binaries, but often provide built-in tools that automate much of the process.

Common examples:

+-----------+----------------------------+----------------------+
| Language  | Compiler examples          | Package manager/tool |
+===========+============================+======================+
| Fortran   | gfortran, ifort/ifx, flang | fpm                  |
+-----------+----------------------------+----------------------+
| C         | gcc, icc/icx, clang        | conan                |
+-----------+----------------------------+----------------------+
| C++       | g++, icpc/icpx, clang      | conan                |
+-----------+----------------------------+----------------------+
| Rust      | rustc                      | cargo                |
+-----------+----------------------------+----------------------+
| Go        | go build                   | built-in             |
+-----------+----------------------------+----------------------+

Before you start
----------------

Compiling software on an HPC cluster differs from compiling on a personal machine. 
The guidelines below can help you avoid common problems.

Compile on compute nodes
^^^^^^^^^^^^^^^^^^^^^^^^

Compilation can be computationally intensive, especially for large projects. 
Compilation should be performed on **compute nodes** instead of login nodes.

If you want architecture-specific optimizations, compile on nodes with the same architecture as the nodes where the software will run.

Read the documentation
^^^^^^^^^^^^^^^^^^^^^^

Most projects include documentation describing how to build the software. 
This documentation usually lists required dependencies, build steps, and optional features.

Reading it first often prevents unnecessary troubleshooting.

Use a build environment module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On VSC clusters, build environment modules are available and can be very useful when compiling software.
These modules provide a ready-to-use development environment with a consistent compiler toolchain (for example ``foss`` or ``intel``).

It is recommended to load a build environment module before compiling software:

.. code-block:: bash

   module load buildenv/<toolchain>

Loading a build environment typically:

* Loads the compiler and common libraries (MPI, math libraries, etc.)
* Defines optimized compiler flags such as ``CFLAGS`` and ``FFLAGS``
* Sets environment variables such as ``CPATH`` and ``LIBRARY_PATH`` so build systems can find headers and libraries
* Ensures a controlled and reproducible build setup

Additional build tools can also be loaded if needed, for example ``CMake``, ``Ninja``, ``Meson``, or ``pkgconf``.

Adding binaries to your PATH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the software is compiled and the executable is available, you may want to run it from any directory without specifying its full path.
This can be done by adding the directory containing the binary to your ``PATH``.

For example:

.. code-block:: bash

   export PATH=/path/to/software/bin:$PATH

You can verify which executable is being used with ``which <command>``.


Compiling Rust software
-----------------------

Rust projects are typically built using **Cargo**, the Rust build system and package manager.

Example workflow
^^^^^^^^^^^^^^^^

Load a Rust module:

.. code-block:: bash

   module load Rust/<version>

Obtain the source code (for example from a Git repository) using ``git clone <repository-url>``. 
If needed, switch to the version you want to build using ``git switch --detach <version-tag>`` inside the cloned directory.

Rust projects normally contain a file named ``Cargo.toml``.  
This file contains metadata and dependencies for the project.

If a ``Cargo.lock`` file is not present in the project, it is recommended to generate one to ensure reproducible builds:

.. code-block:: bash

   cargo generate-lockfile

Build the project using ``cargo build --release``. 
The compiled binary is typically located in ``target/release/`` and can be executed directly with ``./target/release/<program>``.

Additional considerations
^^^^^^^^^^^^^^^^^^^^^^^^^

CPU architecture
~~~~~~~~~~~~~~~~

By default Rust builds for a **baseline architecture** such as x86-64.  
You can enable CPU-specific optimizations:

.. code-block:: bash

   export RUSTFLAGS="-C target-cpu=native"
   cargo build --release

Note that binaries optimized for a specific CPU may not run on older or different CPUs.

Home directory usage
~~~~~~~~~~~~~~~~~~~~

Cargo stores build artifacts in ``$HOME/.cargo`` by default.  
Since the home directory on HPC systems is typically small, it is recommended to redirect it:

.. code-block:: bash

   export CARGO_HOME=$VSC_DATA/cargo

or create a symbolic link:

.. code-block:: bash

   ln -s $VSC_DATA/.cargo $HOME/.cargo


Compiling Go software
---------------------

Go has a built-in build system and dependency management.

Example workflow
^^^^^^^^^^^^^^^^

Load a Go module:

.. code-block:: bash

   module load Go/1.23.6

Obtain the source code (for example from a Git repository) using ``git clone <repository-url>``. 
If needed, switch to the version you want to build using ``git switch --detach <version-tag>`` inside the cloned directory.

Go projects contain a ``go.mod`` file describing dependencies.

Prepare dependencies:

.. code-block:: bash

   go mod tidy

Compile the software:

.. code-block:: bash

   go build -o ./bin/<program> ./

Additional considerations
^^^^^^^^^^^^^^^^^^^^^^^^^

Architecture
~~~~~~~~~~~~

Go builds typically target a baseline architecture (for example ``amd64``), producing binaries that run on most systems rather than being optimized for a specific CPU.

Home directory usage
~~~~~~~~~~~~~~~~~~~~

Go stores build data in ``$HOME`` by default.  
To avoid filling your home directory:

.. code-block:: bash

   export GOPATH=$VSC_DATA/go
   export GOCACHE=$VSC_DATA/go-build


Manual compilation
------------------

Compiling software manually (without build tools) is uncommon and usually only done by developers.

It involves:

* compiling each source file
* resolving dependencies manually
* linking object files into an executable

Example:

.. code-block:: bash

   gcc -O2 -c functions.c
   gcc -O2 -c program.c
   gcc program.o functions.o -o program

Real scientific software is significantly more complex and rarely built this way.


Build systems
-------------

Many projects use **build systems** to automate compilation.

Make
^^^^

One of the oldest and most widely used build systems is **GNU Make**.

Projects using Make typically contain a ``Makefile`` in the project directory.  
To compile the software, it is often enough to run ``make`` in that directory.

CMake
^^^^^

CMake is a build system generator that creates build files such as Makefiles or Ninja scripts.

Projects using CMake usually contain a file called ``CMakeLists.txt`` in the project directory.

A common workflow is to create a separate build directory, configure the project with ``cmake``, and then compile it:

.. code-block:: bash

   mkdir build
   cd build
   cmake ..
   make

Recognizing build systems
-------------------------

The files present in a project directory can often indicate which commands should be used to build the software. 
The table below shows some common examples, but real projects may vary.

+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| Files in the source directory | Configure step            | Build step                   | Install step                 | Module(s) to load|
+===============================+===========================+==============================+==============================+==================+
| configure / Makefile          | ``./configure``           | ``make``                     | ``make install``             | make             |
|                               | *(needs configure script)*|                              |                              |                  |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| build.ninja                   | *(None)*                  | ``ninja``                    | ``ninja install``            | Ninja            |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| CMakeLists.txt                | ``cmake`` /               | ``make`` /                   | ``make install`` /           | CMake +          |
|                               | ``cmake -G Ninja``        | ``ninja``                    | ``ninja install``            | make/Ninja       |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| SConstruct                    |                       ``scons``                          | ``scons install``            | SCons *          |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| meson.build                   | ``meson setup builddir``  | ``meson compile -C builddir``| ``meson install -C builddir``| Meson            |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| Cargo.toml                    |                           | ``cargo build --release``    | ``cargo install``            | Rust             |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| go.mod                        |                      ``go build``                        | ``go install``               | Go               |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+
| setup.py /                    |                           | ``pip install``              |                              | Python           |
| requirements.txt /            |                           |                              |                              |                  |
| pyproject.toml                |                           |                              |                              |                  |
+-------------------------------+---------------------------+------------------------------+------------------------------+------------------+

\*Not available on all VSC clusters

Example: building with CMake and Ninja
--------------------------------------

Example installation workflow:

.. code-block:: bash

   git clone https://github.com/tblite/tblite.git
   cd tblite
   git switch --detach v0.5.0

Load required modules:

.. code-block:: bash

   module load buildenv/default-foss-2024a
   module load Ninja/1.12.1-GCCcore-13.3.0
   module load CMake/3.31.8-GCCcore-13.3.0

Configure the build:

.. code-block:: bash

   cmake -B _build -G Ninja \
     -DCMAKE_INSTALL_PREFIX=$VSC_SCRATCH/my_software/tblite

Compile and install:

.. code-block:: bash

   ninja -C _build
   ninja -C _build install

Add the binaries to your PATH:

.. code-block:: bash

   export PATH=$VSC_SCRATCH/my_software/tblite/bin:$PATH


When to contact support
-----------------------

Building software from source can be challenging because:

* dependencies may be missing
* the correct compiler toolchain may not be obvious
* the build system may require cluster-specific configuration

If you are unable to build a package yourself, please contact the HPC support team.  
The correct contact address depends on the cluster you are using; see
`the VSC contact page <https://docs.vscentrum.be/contact_vsc.html>`_ for the appropriate support email.

When contacting support, please include:

* a link to the source code
* the version you want to build
* the error messages from the build process
