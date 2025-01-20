JupyterLab
----------

With this app you can write and run
`Jupyter <official JupyterLab documentation>`_ notebooks containing
annotated Python, R or Julia code (among other languages). IPython consoles are
available as well. One of the benefits of JupyterLab is that it supports
different types of user-defined environments, as will become clear below.

**Remarks:**

- The top-level notebook directory is by default ``$VSC_DATA``.
- At the moment, we do not support installing extensions in JupyterLab.

Pure module environment
~~~~~~~~~~~~~~~~~~~~~~~

In the app resource form, besides the :ref:`shared resources <shared_resources>`,
you can also choose between different 'Toolchain and Python versions' from a drop-down menu.
An example would be '2023a and ``Python/3.11.3-GCCcore-12.3.0``'.
Based on that choice, the corresponding JupyterLab module will be loaded together with its
dependencies (such as the listed Python module).

Furthermore, you may choose to load ``SciPy-bundle`` (for widely used packages like ``scipy``,
``numpy``, ``pandas`` and more) and/or ``matplotlib`` modules from the same toolchain.

Once you launch a JupyterLab session, a default kernel called ``Python 3 (ipykernel)`` is already available in your session.
This kernel, in addition to the Python standard library, would enable using extra packages from
``SciPy-bundle`` and/or ``matplotlib``, if you selected them in the resource form.

.. warning::

   If you use JupyterLab in this way, remember to be consistent in your choice of toolchain version
   as this e.g. determines the version of Python that will be used.

User-defined kernels
~~~~~~~~~~~~~~~~~~~~

If the pure module environment does not provide all Python packages that you need,
then you can locally install these extra packages, followed by installing the corresponding
Jupyter kernel either from a :ref:`Python Conda environment<py-conda-kernel>`, or from a
:ref:`Python virtual environment<py-venv-kernel>`.
For R, you may create your customized environment using :ref:`Conda environments for R<r-conda-kernel>`.

.. note::

   User kernels are stored by default in ``${VSC_HOME}/.local/share/jupyter/kernels``.
   To override this and store your kernel specifications in a non-default location,
   you may drop the following line in your ``${VSC_HOME}/.bashrc``::

      export XDG_DATA_HOME=${VSC_DATA}/.local/share

   When the ``${XDG_DATA_HOME}`` variable is set, subsequent kernel installations
   (for both Python and R) will reside in ``${XDG_DATA_HOME}/jupyter/kernels``.
   To remove a kernel, find and delete the corresponding folder inside the ``kernels``
   subdirectory.
   We strongly advice you to stay away from modifying the contents of this folder,
   unless you are aware of the consequences.

.. _py-conda-kernel:

Conda environments for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have not installed Conda in your account yet, please refer to the
:ref:`install Miniconda <install_miniconda_python>` page.

Assuming you have created a Conda environment for :ref:`Python <create_python_conda_env>`,
the corresponding kernel needs to be installed for use with JupyterLab.
Note that the minimum supported version for Python for our JupyterLab setup is Python 3.7.
First activate the Conda environment, install the ``ipykernel`` package (which should be at
least version 6.19.2) and finally the kernel itself::

    source activate <env_name>
    conda install ipykernel
    python -m ipykernel install --user --env PYTHONPATH "" --name <env_name> --display-name <kernel_name>

These commands should be excecuted from a shell (e.g. using 'Login Server Shell Access'),
and only need to be done once for a given environment.
When launching a new JupyterLab session, this kernel should then show up in the overview
of available kernels.
In case you encounter issues such as freezing or crashing JupyterLab sessions with a previously
existing kernel, then reinstalling that kernel may help.

.. _py-venv-kernel:

Python virtual environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A similar procedure applies for Python virtual environments associated with
a centrally installed Python module. Note that the chosen Python module needs
to be in the list of 'Toolchain and Python versions' of the JupyterLab form
(e.g. ``2023a and Python/3.11.3-GCCcore-12.3.0``). The commands below show
how creating such a virtual environment and installing the corresponding kernel
would typically look like (to be done from a shell, e.g. using 'Login Server Shell Access'):

.. code-block :: bash

    cd ${VSC_DATA}
    # the line below is needed if you use the 'Interactive Shell' app
    module use /apps/leuven/${VSC_OS_LOCAL}/${VSC_ARCH_LOCAL}${VSC_ARCH_SUFFIX}/2023a/modules/all
    module load Python/3.11.3-GCCcore-12.3.0
    python -m venv <venv_name>
    source <venv_name>/bin/activate
    pip install ipykernel <any additional packages you may need>
    # note that unlike for Conda environments the "--env ..." argument is not needed below
    python -m ipykernel install --user --name <kernel_name> --display-name <kernel_name>

On the JupyterLab form, choose a partition to your liking and select the same
toolchain as above. Once you connect to your session, your new kernel will be
ready to use. To verify your setup, you can execute ``import sys; sys.executable``
in your notebook, and the resulting path should point to the location of your
virtual environment.

**Remarks:**

- The above example assumes that your virtual environment can be used on
  different CPU and/or GPU architectures than the ones present on the node
  on which you created the environment and installed the extra packages.
  This is normally the case for typical ``pip`` usage where precompiled 'wheels'
  get downloaded and installed and which can therefore be used on any
  architecture.
- If however one your package installation steps involves compiling source code,
  then you might only be able to use your virtual environment on the same
  architecture where the compilation was carried out. If this is the case we
  recommend to consider the suggestions in the
  :ref:`wICE advanced guide<wice_compilation>`.

.. _r-conda-kernel:

Conda environments for R
~~~~~~~~~~~~~~~~~~~~~~~~

For R, you need both the ``jupyter_client`` and the ``irkernel`` Conda packages installed.
With the following command you can create the kernel::

      Rscript -e 'IRkernel::installspec(name="<env_name>", displayname="<kernel_name>")'

Once the kernel is created, you will see it in the 'Launcher' menu.
You can now start working in your own customized environment.

For more general information, please refer to the `official JupyterLab documentation`_.

.. _official JupyterLab documentation: https://docs.jupyter.org/en/latest/
