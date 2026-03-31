.. _julia_package_management:

Julia package management
========================

Julia is a dynamic, high-performance programming language that is particularly
well-suited for scientific computing and numerical analysis.

How to find available Julia packages?
-------------------------------------

* The software module called ``Julia`` provides a standard installation of
  Julia without any extra packages
* Some specific Julia packages can be provided with their own software modules
  (*e.g.* IJulia)

Installing Julia packages
-------------------------

The Julia installations loaded by the *Julia software modules* in our HPC
clusters provide a base installation of Julia that allows installing your own
packages on top of it.

Loading a Julia software module will enable the ``julia`` command to launch the
Julia shell or execute commands in Julia. Then you can use the ``Pkg.add()``
command in Julia as usual to install additional packages. New packages will be
installed in the active project environment, which by default is the shared
environment in your personal *depot* (``~/.julia``).

1. Load a Julia module

   .. code-block:: console

      $ module load Julia/1.11.6-linux-x86_64

2. Basic package installation in Julia

   .. code-block:: console

      julia> using Pkg
      julia> Pkg.add("PackageName")

Your personal *depot* (located in ``~/.julia``) or any custom project
environments in your account will continue to be usable as long as they were
created with the same major and minor version of Julia as the loaded module.
For example, if you load ``Julia/1.10.3-linux-x86_64``, all project
environments for version 1.10 will be usable.

|Recommended| Software installations of Julia packages can be heavy. Installing
many packages or a single package that pulls many dependencies can quickly fill
the :ref:`storage quota of your home directory <quota>`.
We recommend to move your personal *depot* to your ``$VSC_SCRATCH`` and link
``~/.julia`` to it.

.. code-block:: bash

   mkdir -p ~/.julia
   mv -i ~/.julia $VSC_SCRATCH/julia
   ln -s $VSC_SCRATCH/julia ~/.julia

Julia environments
------------------

The best approach to install Julia packages is by making Julia environments.
These are self-contained collections of packages that can be activated
on-the-fly for each different project and easily shared with colleagues.

1. Load a Julia module

   .. code-block:: console

      $ module load Julia/1.11.6-linux-x86_64

2. Create a project directory

   .. code-block:: console

      $ mkdir MyProject

3. Start Julia and create an environment

   .. code-block:: console

      $ julia
      julia> using Pkg
      julia> Pkg.activate("MyProject")
        Activating new project at `/home/user/julia/MyProject`

4. Add software to your Julia environment:

   .. code-block:: console

      julia> Pkg.add("TightBindingToolkit")
        Resolving package versions
        [...]

Using software in Julia
-----------------------

Once packages are installed in your environment in Julia , you need to *load*
them before they can be used in your Julia shell or scripts.

Loading a package in Julia is done with the ``using`` keyword:

.. code-block:: console

    julia> using PackageName

Using existing Julia modules
----------------------------

You might find software modules in the central library of our VSC clusters that
provide additional Julia packages. Those modules can bundle one or more Julia
packages and will automatically load any dependencies needed for their correct
function, including a Julia base module.

Once you load a software module with Julia packages in it, they will become
usable through the Julia command ``using``, as usual. Moreover, your own Julia
packages installed in your *depot* will continue to be usable as well with
``using``.

.. code-block:: console

   $ module load Circuitscape/5.12.3-Julia-1.9.2
   $ julia -e 'using Circuitscape'

.. warning::

   Julia packages loaded through software modules like
   ``Circuitscape/5.12.3-Julia-1.9.2`` will be usable in Julia, but they will
   **not be part of your project environment**. This means that you are free to
   install your own versions of any of the Julia packages provided by the
   loaded software module.

Julia environment on top of software module
-------------------------------------------

Julia environments can be created on top of a software module, inheriting all
Julia packages available in it.

1. Load the *base* software module

   .. code-block:: console

      $ module load Circuitscape/5.12.3-Julia-1.9.2

2. Create a new environment based on the module's environment

   .. code-block:: console

      $ base_project=$(julia -E 'Base.load_path()[end]')
      $ cp -r "$(dirname ${base_project:1:-1})" myNewEnv

3. Check that the new environment does have the packages from the module

   .. code-block:: console

      $ julia -e 'using Pkg; Pkg.activate("myNewEnv"); Pkg.status()'
        Activating project at /vscmnt/brussel_pixiu_data/_data_brussel/vo/000/bvo00005/vsc10122/tests/julia/myNewEnv
        Status /vscmnt/brussel_pixiu_data/_data_brussel/vo/000/bvo00005/vsc10122/tests/julia/myNewEnv/Project.toml
        [...]
        [2b7a1792] Circuitscape v5.12.3 /apps/brussel/<OS>/<arch>/software/Circuitscape/5.12.3-Julia-1.9.2/packages/Circuitscape
        [...]

Once this new environment is *active*, installations of new Julia packages will
take into account the packages already provided by the loaded modules. For
instance, the following example installs *CSV* on top of the packages provided
by ``Circuitscape/5.12.3-Julia-1.9.2``, which results in only 8 new packages
installed, compared to the 22 installed on an empty environment.

.. code-block:: console

   $ module load Circuitscape/5.12.3-Julia-1.9.2
   $ julia -e 'using Pkg; Pkg.activate("myNewEnv"); Pkg.add("CSV")'
     Activating project at /vscmnt/brussel_pixiu_data/_data_brussel/vo/000/bvo00005/vsc10122/tests/julia/myNewEnv
      Resolving package versions...
       Updating /vscmnt/brussel_pixiu_data/_data_brussel/vo/000/bvo00005/vsc10122/tests/julia/myNewEnv/Project.toml
     [336ed68f] + CSV v0.10.13
       Updating /vscmnt/brussel_pixiu_data/_data_brussel/vo/000/bvo00005/vsc10122/tests/julia/myNewEnv/Manifest.toml
     [336ed68f] + CSV v0.10.13
     [...]
   Precompiling project...
     7 dependencies successfully precompiled in 53 seconds. 100 already precompiled.

