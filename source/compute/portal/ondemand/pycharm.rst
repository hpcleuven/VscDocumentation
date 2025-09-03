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


Selecting a suitable Python environment
---------------------------------------

Aside from code editing, PyCharm also allows you to run your Python scripts
and use a Python console from within the IDE. By default, PyCharm will
use an available system Python installation for this purpose
(such as the Python 3.9 installation currently present in the OnDemand
container for PyCharm). Depending on your needs you can either accept this
default choice (and make other configuration changes) or select or create
a different Python environment:

* Creating a new virtual environment using the :ref:`default Python interpreter <pycharm_default_python>`
* Use an :ref:`existing Python virtual environment <pycharm_venv>` based on Python modules
* Creating a :ref:`new Conda environment <pycharm_new_conda>`
* Using an :ref:`existing Conda/Mamba environment <pycharm_conda>`

.. note::

   Make sure you do not use your ``VSC_HOME`` (starting with e.g. ``/user/leuven``) for storing your virtual environment, Mamba or Conda, because your home directory can get quickly filled up leading to possible issues with your login and/or job submission. Instead, we recommend using your ``VSC_DATA`` directory (starting with e.g. ``/data/leuven``).

.. note::

   For long-running jobs or for jobs using more than one node (with e.g.
   ``mpi4py`` or ``dask.distributed``), we recommend :ref:`submitting batch
   jobs <job submission>` instead.


.. _pycharm_default_python:

Using the default Python interpreter
====================================

The following steps (`adopted from the official PyCharm documentation
<https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html>`_)
show how you can create a PyCharm Project using the
system Python installation automatically detected by PyCharm.

.. note::

   Keep in mind that this will typically be a fairly old version of Python.
   You furthermore run the risk that your environment will no longer work
   at some point since the container's Python installation will upgrade
   as part of the maintenance cycle of the OnDemand infrastructure.

* Click on the 'New Project' on the welcome screen, or choose 'File' -> 'New Project'.
* Choose a 'Location' for your project hierarchy, preferably in your ``VSC_DATA``
  (such as ``/data/leuven/3xx/vsc3xxxx/python-projects/pre-processing``).
* For the 'Interpreter type' choose 'Custom environment'.
* For the 'Environment' select 'Generate new' (and you only need to do this once).
* For the 'Type' of the environment choose 'Virtualenv'.
  At this point, the 'Base python' is already selected as ``Python 3.9`` pointing at ``/usr/bin/python3``.
* For the 'location' of your Python virual environment, choose a new folder in your ``VSC_DATA``, such as ``/data/leuven/3xx/vsc3xxxx/pycharm-venvs/pandas``.
* It is OK to select 'Inherit packages from base interpreter'.
* Click on 'Create'. At the bottom right, you see the environment name ``Python 3.9 (pandas)`` appearing.
* If you are asked about how to open the new project, you may select 'New Window'.
* To e.g. add the ``pandas`` package from `Scikit-Learn <https://pypi.org/project/sklearn-pandas>`_, click on the 'Python Packages' icon on the left tray, and put ``pandas`` in the search box. From the long list of available packages, choose the ``sklearn-pandas`` package and click on the 'Install' button. You may choose the latest version. The installation of dependencies and preparation of the virtual environment may take a minute or two.

Once your environment is created, you can select it in any later session from the list of interpreters.


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
  You notice that the interpreter name at the bottom right tray changes to e.g. ``Python 3.13 virtualenv .../pandas``.
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


.. _pycharm_terminal:

Using the terminal
------------------

If you enter the PyCharm terminal, you land on your (default) project directory.
This terminal offers minimal functionality specifically because the :ref:`cluster modules <leuven_module_system>` are unavailable there.
For that reason, we recommend starting an :ref:`Interactive Shell <ood_interactive_shell>` session or using the integrated terminal from :ref:`VS Code Server <vscode_server>`, instead.
