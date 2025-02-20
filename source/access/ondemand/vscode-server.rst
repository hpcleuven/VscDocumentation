VS Code Server
==============

This is the browser version of Visual Studio Code (VS Code).
For more information on VS Code, check out the official `VSCode guidelines
<https://code.visualstudio.com/docs>`_.

.. include:: vscode-symlink.rst

Terminal in VS Code
-------------------

To open a terminal window in VS Code, click the three horizontal lines in the
top left corner and select 'Terminal - New Terminal'.  This will open a shell on
the node you are running your session on.  You can use this as a regular shell,
meaning that you can submit jobs, load modules and so on. Notice that, by
default, you are starting in your ``$VSC_HOME`` directory.

VS Code as an IDE
-----------------

VS Code contains many different options and menus, but we will only discuss how
to set it up as an integrated development environment (IDE) for your favorite
coding language.  For any language you want to use you need two things: an
installation of the specific interpreter or compiler, and a VS Code extension
that allows you to connect to it.  The extensions can be found in the
'extensions' menu.  In what follows, the steps for both Python and R are
described.

Python IDE
~~~~~~~~~~

There are multiple Python extensions available, but only the Microsoft 'Python'
extension has been tested by VSC support.  To install this extension, go to
'Extensions', search for 'Python', and install the one developed by 'ms-python'.

Once installed, if you open a script, you can use VS Code as an IDE and run the
lines of code from within the script (the shortkey is shift+enter).  VS Code
will start a Python session with the currently selected Python interpreter.  If
you did not specify another one, this should default to the loaded Python
module.  The 'Python' extension gives you the possibility to choose other
interpreters as well.  In the right bottom corner, you can see
<python-version-number> right next to 'Python'.  If you click that, a window
will appear where you can select your Python version.  Next to the module
version, you should see at least some system Python versions (e.g.
``/bin/python``).  You can also load other modules, or you can also use Conda
environments here (if you have any Conda environments already, you should see
them here as well).

Python modules and environments
-------------------------------

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      By default, a Python module is already loaded, which means you can use
      both Python and git from a terminal window within VS Code.

      For more information about creating customized Python environments,
      have a look at the documentation on :ref:`python packages <Python packages>`.

      .. note::

         When loading a new Python interpreter, you have to kill your current Python
         terminal before you will be able to use this new interpreter.


   .. tab-item:: VUB

      .. include:: vscode-python-modules-brussel.rst

R IDE
~~~~~

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      For full functionality, it is recommended to work with Conda environments.
      For the time being, there are some issues with using modules together with functionalities, like plotting.

      There are some package requirements if you want to use R in VS Code.
      The following command creates a functional environment (of course, add any other packages you need):

              .. code-block:: bash

               conda create -n <env_name> -c conda-forge r-base r-remotes r-languageserver r-httpgd r-jsonlite

      Once you've created your environment, go ahead and start a VS Code session on
      Open Ondemand.  On the lefthand side, click the extension menu and search for
      'R'.  You should install the 'R' extension of 'REditorSupport'.

      Now there are two ways to use the R installation inside your Conda environment:

      - Open a terminal (three horizontal lines in the upper left corner - Terminal - New Terminal),
        and activate your Conda environment.
        Now type ``R`` in the terminal and you will be able to use your scripts interactively
        (R gets attached as soon as you start it).
      - You can also set the path to the R version that needs to be attached (better if you always
        use the same Conda environment).
        Go to 'Extensions', and click the settings wheel next to the R extension.
        Select 'Extension Settings' and search for the 'R > RTerm: Linux' setting.
        Paste the path to your Conda env there (``/path/to/miniconda/envs/<env_name>/lib/R``)

      .. note::

         To run your script line-by-line, place your cursor on a desired line, and
         press the key combination 'ctrl+enter' on your keyboard.

   .. tab-item:: VUB

      (documentation not yet available)

