.. _ood_pycharm:

PyCharm
-------

PyCharm is a well-known integrated development environment (IDE) for Python offered by `JetBrains <https://www.jetbrains.com/pycharm/>`_. We offer the PyCharm community edition (based on PyCharm modules) as a web-based app via Open OnDemand.

VSC clusters that support this app are:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`


Before you connect
------------------

In case you would like to only develop your Python code or software, you can use PyCharm as a pure editor.
However, if you want to execute your Python scripts interactively, then you need to choose a Python interpreter that contains all the packages which you need at runtime.
For that, you need to consider :ref:`creating and using a Python environment <pycharm_env>` which suits you best.


Launching PyCharm
-----------------

To start a session, you may choose your desired version of PyCharm module.
For developing a Python software and for testing a serial Python script, sticking to a single core is sufficient.
However, to run, test, debug or benchmark a multi-threaded or multi-processing Python script, you can request additional cores.
For long-running jobs or for jobs using more than one node (with e.g. ``mpi4py`` or ``dask.distributed``), we recommend :ref:`submitting batch jobs <job submission>`.


.. _pycharm_env:

Setting up a PyCharm Python environment
---------------------------------------

Once you PyCharm session starts, you need to choose a Python interpreter.
This would allow you to use and/or add all the necessary Python packages (and their dependencies) needed for your project at runtime.
For that purpose, there are multiple possibilities which are elaborated below: 

* Creating a new virtual environment using the :ref:`default Python interpreter <pycharm_default_python>`
* Use an :ref:`existing Python virtual environment <pycharm_venv>` based on Python modules
* Creating a :ref:`new Conda environment <pycharm_new_conda>`
* Using an :ref:`existing Conda/Mamba environment <pycharm_conda>`

.. note::

   Make sure you do not use your ``VSC_HOME`` (starting with e.g. ``/user/leuven``) for storing your virtual environment, Mamba or Conda, because your home directory can get quickly filled up leading to possible issues with your loging and/or job submission. Instead, we recommend using your ``VSC_DATA`` directory (starting with e.g. ``/data/leuven``).


.. _pycharm_default_python:

Using default Python interpreter
================================

PyCharm automatically detects the Python interpreter from the OnDemand container (currently version 3.9);
however, this default environment contains only the Python standard library.
In order to extend this environment, you need to create a new virtual environment to add new packages.
Here are the steps to take `(adopted from the official PyCharm documentation) <https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html>`_:

* Click on the 'New Project' on the welcome screen, or choose 'File' -> 'New Project'.
* Choose a 'Location' for your project hierarchy starting from your ``VSC_DATA`` directory such as ``/data/leuven/3xx/vsc3xxxx/python-projects/pre-processing``.
* For the 'Interpreter type' choose 'Custum environment'.
* For the 'Environment' select 'Generate new' (and you only need to do this once).
* For the 'Type' of the environment choose 'Virtualenv'.
  At this point, the 'Base python' is already selected as ``Python 3.9`` pointing at ``/usr/bin/python3``.
* For the 'location' of your Python virual environment, choose a unique folder under your ``VSC_DATA`` directory, such as ``/data/leuven/3xx/vsc3xxxx/pycharm-venvs/pandas``.
* It is OK to select 'Inherit packages from base interpreter'.
* Click on 'Create'. At the bottom right, you see the environment name ``Python 3.9 (pandas)`` appearning.
* If you are asked about how to open the new project, you may select 'New Window'.
* To add the ``pandas`` package from `Scikit-Learn <https://pypi.org/project/sklearn-pandas>`_, click on the 'Python Packages' icon on the left tray, and put ``pandas`` in the search box. From the long list of available packages, choose the ``sklearn-pandas`` package and click on the 'Install' button. You may choose the latest version. The installation of dependencies and preparation of the virtual environment may take a minute or two.


Once your environment is created, you may reuse it in any later session from the list of interpreters.


.. _pycharm_venv:

Using an existing Python virtual environment
============================================

PyCharm cannot trivially detect a loaded Python module; hence, you cannot readily create a Python virtual environment in PyCharm. Instead, you need to use an existing Python virtual environment (based on a Python module), and you may optionally add/remove packages to/from this environment using PyCharm. 

* Create a custom :ref:`Python virtual environment <venv_python>` under your ``VSC_DATA`` (e.g. in an Interactive Shell)
* Click on the 'New Project' on the welcome screen, or choose 'File' -> 'New Project'.
* Choose a 'Location' for your project hierarchy starting from your ``VSC_DATA`` directory such as ``/data/leuven/3xx/vsc3xxxx/python-projects/pre-processing``.
* For the 'Interpreter type' choose 'Custum environment'.
* For the 'Environment' choose 'Select existing'.
* For the 'Type' of the environment choose 'Python'.
* For the 'Python path' use the browse button to choose ``bin/python`` from the location where you have saved your virtual environment.
* Click on the 'OK' button. 
  You notice that the interpreter name at the bottom right tray changes to e.g. ``Python 3.13 virtualenv .../pandas``
* To add more packages like ``pandas`` to your virtual environment (in addition to what is already in there), you can follow :ref:`the last steps above <pycharm_default_python>`.



.. _pycharm_new_conda:

Creating a new Conda environment in PyCharm
===========================================

You may create a new Conda environment in PyCharm after you start a 'New Project' by following these steps:

* Select a 'Location' starting from your ``VSC_DATA``.
* For the 'Interpreter type' choose 'Custom environment'.
* For the 'Environment' choose 'Generate new'.
* For the 'Type' choose 'Conda'.
* For the 'Python version' pick e.g. the latest.
* For the 'Name' put a representative name for your environment which distinguishes its purpose and its way of creation, such as ``conda-pandas``.
  If you see the 'No conda executable found' warning, then 'Select path' to your existing ``conda`` executable. Make sure you *do not* 'Install Miniconda' via PyCharm, because such new installations end up by default in your ``VSC_HOME`` which is strongly discouraged.
* Click on the 'Create' button and wait for a minute. Eventually, the interpreter at the bottom right tray will show e.g. ``conda-pandas``. 

Once your environment is created, you may use it in any later session.


.. _pycharm_conda:

Using an existing Conda/Mamba environment
=========================================

You can use an existing Conda/Mamba environment inside PyCharm.
For that, first :ref:`create a custom Conda environment <conda for Python>` outside PyCharm, or use :ref:`PyCharm to create a new Conda environment <pycharm_new_conda>`.


* Click on the bottom right tray and choose a relevant Conda environment by name from the list. 
* If the Conda/Mamba environment name is not listed, then 
  
    * select 'Add Python Interpreter'
    * Choose the 'Select existing' option.
    * For the 'Python path', click on the browse button and choose the ``bin/python`` executable file from inside your Conda/Mamba environment directory. Click on 'OK'.


.. note::

   `Mamba <https://mamba.readthedocs.io/en/latest/index.html>`_ is a Python package manager similar to Conda.
   Creating a new Mamba environment is similar to that of Conda by substituting the ``conda`` command with ``mamba`` or ``micromamba`` depending on which variants of Mamba you have installed.


.. note::

   For more advanced configurations regarding your Python interpreter or for switching your Python interpreter when needed, please refer to the `official PyCharm documentation <https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html>`_.


.. _pycharm_console:

Using PyCharm Python console
----------------------------

To work interactively with Python in PyCharm, you may open the Python console from the left tray.
In this console, the selected :ref:`Python interpreter <pycharm_env>` will be used, and the additional packages from your custom environment will be ready for ``import``.


.. _pycharm_terminal:

Using the terminal
------------------

If you enter the PyCharm terminal, you land on your (default) project directory.
This terminal offers minimal functionality specifically because the :ref:`cluster modules <leuven_module_system>` are unavailable there.
For that reason, we recommend starting an :ref:`Interactive Shell <ood_interactive_shell>` session or using the integrated terminal from :ref:`VS Code Server <vscode_server>`, instead.
