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
For that, you need to consider :ref:`creating a PyCharm Python environment <pycharm_env>` which suits you best.

#PyCharm ships with a default Python (whose version depends also on the version of PyCharm you select from the form). But, such default interpreters contain only the Python standard library. To create your custom Python environment, please refer to the :ref:`Python package management <Python packages>` page.


Launching PyCharm
-----------------

To start a session, you may choose your desired version of PyCharm module. For developing a Python software and for testing a serial Python script, sticking to a single core is sufficient. However, to run, test, debug or benchmark a multi-threaded or multi-processing Python script, you may request additional cores. For running jobs using more than one node (with e.g. ``mpi4py`` or ``dask.distributed``), we recommend :ref:`submitting batch jobs <job submission>`.

Once your session starts, you may `configure your Python interpreter <https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html>`_, and eventually change it to that of your custom environment from the bottom-right menu.


: _pycharm_env:

Creating a PyCharm Python environment
-------------------------------------

Once you PyCharm session starts, you need to create a new Python interpreter or activate an existing one.
This would allow you to add all the necessary Python packages (and their dependencies) needed for your project at runtime.
For that purpose, there are three possibilities; you either use the default Python interpreter from the OnDemand container, or create a Python virtual environment or a miniconda environment.
These options are elaborated below.


.. _pycharm_default_python:

Using default Python interpreter
================================

PyCharm automatically detects the Python interpreter from the OnDemand container (currently version 3.9);
however, this default environment contains only the Python standard library.
In order to extend this environment, you need to create a new Project.
Then, PyCharm creates a virtual environment and you may add new packages to this virtual environment.
Here are the steps to take ([adopted from official PyCharm documentation](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html)):

- Click on the 'New Project' on the welcome screen, or choose 'File' -> 'New Project'.
- Choose a 'Location' for your project hierarchy starting from your ``VSC_DATA`` directory such as ``/data/leuven/3xx/vsc3xxxx/python-projects/pre-processing``. Avoid using the default/suggested path which starts with ``/user/leuven``, because that points at your ``VSC_HOME`` which will be filled up quickly.
- For the 'Interpreter type' choose 'Custum environment'.
- For the 'Environment' select 'Generate new' (and you only need to do this once).
- For the 'Type' of the environment choose 'Virtualenv'.
  At this point, the 'Base python' is already selected as ``Python 3.9`` pointing at ``/usr/bin/python3``.
- For the 'location' of your Python virual environment, choose a unique folder under your ``VSC_DATA`` directory, such as ``/data/leuven/3xx/vsc3xxxx/pycharm-venvs/pandas``.
- It is OK to select 'Inherit packages from base interpreter'.
- Click on 'Create'. At the bottom right, you see the environment name ``Python 3.9 (pandas)`` appearning.
- If you are asked about how to open the new project, you may select 'New Window'.
- To add the [``pandas`` package from Scikit-Learn](https://pypi.org/project/sklearn-pandas/), click on the 'Python Packages' icon on the left tray, and put ``pandas`` in the search box. From the long list of available packages, choose the ``sklearn-pandas`` package and click on the 'Install' button. You may choose the latest version. The installation of dependencies and preparation of the virtual environment may take a minute or two.



.. _pycharm_venv:

Using a Python virtual environment
==================================

You can use an existing Python module as a base interpreter, and create a virtual environment to include the packages you need. You may either start a new project (similar to `above <pycharm_default_python>`) or 

- Create a custom `Python virtual environment <venv_python>` under your ``VSC_DATA``
- In the 'pre-run scriptlet' text box of the PyCharm form, add e.g. ``module load Python/3.13.1-GCCcore-14.2.0``, and start your session
- On the bottm right, you see e.g. ``Python 3.9``.
  Select 'Add New Interpreter' -> 'Add Local Interpreter ...' or 'Interpreter Settings ...' buttons.
- For the 'Environment' choose the 'Select existing' option.
- For the 'Type' choose 'Python'.
- For the 'Python path' click on the browse button and browse to where you have already stored your virtual environment and choose ``bin/python``.
  Click on the 'OK' button.
  You notice that the interpreter name at the bottom right tray changes to e.g. ``Python 3.13 virtualenv .../pandas``
- To add more packages like ``pandas`` to your virtual environment (in addition to what is already in there), you can follow `the last steps above <pycharm_default_python>`.



.. _pycharm_conda:

Using the Python console
------------------------

You can use an existing Conda/Mamba environment inside PyCharm.
For that, first `create a custom Conda environment <conda for Python>`.
Note that creating a Mamba environment is similar to that of Conda by substituting the ``conda`` command with ``mamba`` or ``micromamba`` depending on which variants of Mamba you have installed.

- Click on the bottom right tray and select 'Add Python Interpreter'.
- Choose the 'Select existing' option.
- For the 'Python path', click on the browse button and choose the ``bin/python`` executable file from inside your Conda/Mamba environment directory. Click on 'OK'.


.. _pycharm_console:

Using PyCharm Python console and terminal
-----------------------------------------

To work interactively with Python in PyCharm, you may open the Python console and/or the terminal from the left tray.
If the Python console, the selected `Python interpreter <pycharm_env>` will be used, and the additional packages from your custom environment will be ready for ``import``.


.. _pycharm_terminal:

Using the terminal
------------------

If you enter the PyCharm terminal, you land on your (default) project directory.
This terminal offers minimal functionality specifically because the `cluster modules <leuven_module_system>` are unavailable there.
For that reason, we recommend using the `Interactive Shell <ood_interactive_shell>`, instead.
