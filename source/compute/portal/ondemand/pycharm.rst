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
* Using an :ref:`existing Conda environment <pycharm_conda>`

For more advanced configuration options, see also the `JetBrains documentation
<https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html>`_.

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

Assuming you e.g. have a :ref:`local Miniconda installation <install_miniconda_python>`,
you may create a new Conda environment in PyCharm after you start a 'New Project'
by following the steps below. Make sure you *do not* install Miniconda
via PyCharm because it will end up in your ``VSC_HOME`` which is strongly discouraged.

* Select a 'Location' starting in your ``VSC_DATA``.
* For the 'Interpreter type' choose 'Custom environment'.
* For the 'Environment' choose 'Generate new'.
* For the 'Type' choose 'Conda'.
* For the 'Python version' pick one that suits your needs.
* For the 'Name' again choose a unique and representative (e.g. ``conda-pandas``).
* For the 'Path to conda' set the path to your ``conda`` executable
  (a typical location would be ``/data/leuven/xxx/xxxxx/miniconda3/bin/conda``).
* Click on the 'Create' button and wait for a minute.
  Eventually, the interpreter at the bottom right tray will show e.g. ``conda-pandas``.

Once your environment is created, you may use it in any later session.


.. _pycharm_conda:

Using an existing Conda environment
===================================

You can also let PyCharm use Conda (or
`Mamba <https://mamba.readthedocs.io/en/latest/index.html>`_) environments
that you :ref:`created outside PyCharm <conda for Python>`. The steps are
the same as in the previous paragraph, except:

* For the first 'Environment' box, choose 'Select existing'.
* For the second 'Environment' box, choose your Conda or Mamba
  environment from the list.


.. _pycharm_terminal:

Using the terminal
------------------

If you enter the PyCharm terminal, you land on your (default) project directory.
This terminal offers minimal functionality specifically because the :ref:`cluster modules <leuven_module_system>` are unavailable there.
For that reason, we recommend starting an :ref:`Interactive Shell <ood_interactive_shell>` session or using the integrated terminal from :ref:`VS Code Server <vscode_server>`, instead.
