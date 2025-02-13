The following steps are required to use Python and packages from :ref:`the
software modules <module_system_basics>` in the Python IDE:

#. In 'Pre-run Scriptlet' of the resources form, ``module load`` the
   modules that you need. A common software module is ``SciPy-bundle``, a
   bundle of data science packages such as ``numpy``, ``pandas``, and
   ``scipy``.

#. In the VS Code interface, select the corresponding Python version +
   path as outlined above.

The Steps for using `virtual environments
<https://hpc.vub.be/docs/software/additional_software/#python-virtual-environments>`_
on top of loaded software modules are exactly the same. Note that
activating the virtual environment is not required if you select
the Python version + path located in the virtual environment at
``<path-to-venv>/bin/python3.x``.
