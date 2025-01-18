VS Code Server
--------------

This is the browser version of Visual Studio Code.
For more information, check out `VSCode official guidelines <https://code.visualstudio.com/docs>`_.
By default, a Python and a Git module are already loaded, which means you can use both Python and git
from a terminal window within code-server.

How to open a terminal window is probably one of the first things you should know: click on the three
horizontal lines in the upper left corner, select 'Terminal - New Terminal'
This will open a shell on the node you are running your session on.
Notice that you are starting in your ``$VSC_DATA`` directory.
You can use this as a regular shell, meaning that you can submit jobs, load modules and so on.

Code-server contains many different options and menus, but only a few will be discussed here.
Feel free to explore them.
We will however discuss how to set up code-server to use any of the compatible languages,
and use code-server as an IDE.
For each of the languages you want to use you need two things: an installation of
the specific interpreter, and an extension in code-server that allows you to connect to it.
The extensions can be found in the 'extensions' menu.
In what follows, the steps for both Python and R are described.

Setup Python in Code Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are multiple Python extensions available, so feel free to try and install the extension that suits you the best.
This comes with the warning that only the Microsoft Python extension has been tested by our team.
To install this extension, go to 'Extensions' and search for 'Python'.
Install the one with as developer 'ms-python'.
If you now open a script, you can now use code-server as an IDE and run the lines of code from within
the script (the shortkey is shift+enter).
Code-server will start a Python session with the currently selected Python interpreter.
If you did not specify another one, this should default to the loaded Python module.
This Python extension gives you the possibility to choose other interpreters as well.
In the right down corner, you can see <python-version-number> right next to 'Python'.
If you click that, a window will appear where you can select your Python version.
Next to the module version, you should see at least some system Python versions (e.g. ``/bin/python``).
You can also load other modules, or you can also use Conda environments here (if you have any Conda environments
already, you should see them here as well).

If you need more information about creating your customized Python environments, have a look :ref:`here <Python packages>`.

**Remarks:**

- Whenever loading a new Python interpreter, you will have to kill your current Python terminal before
  you will be able to use this new interpreter.


Setup R in Code Server
~~~~~~~~~~~~~~~~~~~~~~

For full functionality, it is recommended to work with Conda environments.
For the time being, there are some issues with using modules together with functionalities, like plotting.

There are some package requirements if you want to use R in code-server.
The following command creates a functional environment (of course, add any other packages you need):

        .. code-block:: bash

         conda create -n <env_name> -c conda-forge r-base r-remotes r-languageserver r-httpgd r-jsonlite

Once you've created your environment, go ahead and start a code-server session on Open Ondemand.
On the lefthand side, go to the extension menu and search for 'R'.
You should install the 'R' extension of 'REditorSupport'.

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

**Remarks:**

- To run your script line-by-line, place your cursor on a desired line, and press the key combination of
  'ctrl+enter' on your keyboard.

