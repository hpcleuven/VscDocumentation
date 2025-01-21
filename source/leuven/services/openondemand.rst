.. _ood_t2_leuven:

Open OnDemand on the KULeuven Tier2 cluster
===========================================

.. sectnum::
   :depth: 3

About
=====

Open OnDemand provides a user interface to HPC clusters from within a web browser.
This tool supports a range of different apps and features that not only allow the
user to easily submit jobs from within the browser, but also provide different
coding GUIs, tools for plotting and more.
Open OnDemand is available for the Tier-2 Genius and wICE clusters.

You can use this interface by navigating to the `KU Leuven Open OnDemand page`_.
You can log in using your KU Leuven or VSC credentials.

General features
================

The KU Leuven Open OnDemand page provides a range of functions:

- Browsing, creating, transferring, viewing and/or editing files
- Submitting and monitoring jobs, creating job templates
- Opening a shell on one of the login nodes
- Using interactive apps

All of these functionalities can be used by accessing them through the tabs at the top of the page.
In the following, we will describe these in some more detail.

Files
=====

This menu provides a file explorer that allows you to navigate through your files and folders.
You can access your ``$VSC_HOME`` and ``$VSC_DATA`` folders. Other storages are not available here.
General file explorer options like moving, deleting, modifying and creating files or directories are available as well.
You can also use this interface to download and upload files to and from your local machine. Be aware that this is not recommended for very large files.

**Good to know:** the standard 'ctrl+s' does not save your edited files on Open OnDemand, but will trigger a save on your local machine. Luckily, there is a
save button in the upper left corner on the editor page.

The 'Globus' button takes you directly to the Globus login page, and upon a successful login to your Globus account
(using your KU Leuven credentials), you will land on the same sub-directory from which you clicked on the Globus button.
For more information about Globus, please refer to our documentation about the :ref:`Globus Platform<globus platform>`.

Jobs
====

All jobs submitted from Open OnDemand can run on Genius and wICE.
This also means that all your jobs should be submitted as **Slurm** jobs.
For more detail on how to run jobs on wICE, check out the
:ref:`wICE quick start guide<wice_t2_leuven>`.

The jobs tab has three menus, 'Active Jobs', 'Job Composer' and 'Projects' (which we skip here, because at the time
of this writing, it is still in development by the upstream).

Active jobs
-----------

This lists all your running, queued and completed jobs.
Completed jobs will disappear from this view after a couple of minutes.
You have a handy overview of multiple job details by clicking the large arrow next
to the job id, including things like the node list, the account you used, and
the status of the job.
It also gives you the option to open the job script directory in the file
manager, and thus inspect the created output and error files.

If your job is still running, you can also delete it by clicking the bin under 'Actions'.
The 'Active jobs' menu does not allow re-submission of your job.
How to (re-)submit jobs will be made clear in the next chapter.

Job Composer
------------

The Job Composer contains all the tools that allow you to launch your jobs. This goes from basic job script building, adding necessary files,
to building and using templates for easier job creation. Under the job composer tab you can find two other menus, namely 'Jobs' and 'Templates'.
As templates are the backbone of job creation in Open OnDemand, we will start by explaining these.
The 'Jobs' menu is pretty much self-explanatory once understanding this.

Templates
~~~~~~~~~

To enter the Templates menu, you can click on 'Templates' at the top once you are in the 'Job Composer' menu. You can also access this menu by clicking the button 'New
Job'-'From Template'. Once in this menu, you should see a table with three System Templates. The resources that are requested in these scripts are the default settings.
The templates:

- CPU job template: a template for jobs on the thin nodes (the default ``batch`` partition). This is also the default template (which you will get when clicking 'From Default Template' under the 'New Job' button in the 'Jobs' menu).
- GPU job template: a template for jobs with GPU resources (``gpu`` partition)
- Big memory CPU jobs: a template for jobs with large memory requirements (``bigmem`` partition)

You can create your own templates from scratch or by copying one of the existing templates.
In both cases you will be redirected to a page where you can provide a
name, the cluster and add some notes.
To save this, you will need to provide a path to store it in. Ondemand will create a new subdirectory
with the name of your template here.

A ``manifest.yml`` file will always be present in a template directory, It contains all the info you provided in the set-up step.
Which other files will be present in this directory depends on how you created your new template.
When using the 'New Template' button, and you don't provide a path, a copy of the default template will be created.
You can also provide a path to an existing template or job directory. In that case that directory and its contents will be copied.
This works for **any** directory on your system, so be sure to provide the correct path!

The 'Copy Template' button basically does the same, but with this button, Ondemand will automatically fill in the path of the
selected template in the template overview.
Once you use this more often, you can also use your own templates to create new ones.
Any file that is present in that folder, will be copied to your new one as well.

Once you've created the new template directory, you can start customizing it. You can view the content in
the directory using the Folder Explorer (click 'View Files' on top or 'Open Dir' at the bottom). As explained above, you can edit or remove any file, create new files
or upload new files.
These files will be present in each job you create from this template.

Jobs
~~~~

The functioning of creating jobs is a bit similar to how you create new templates.
Whatever method you choose, you will always create a new directory for each job, this time
located at ``$VSC_DATA/ondemand/data/projects/default/``.
The job directories will be numbered in the order you have created them.

.. warning::

   Do not change this folder name as long as you plan on using it from the job menus,
   as this will break the linking.
   When removing a job, the directory will be deleted as well.

To create a job, press the 'New Job' button and choose the option that best suits
your needs.
You will get a new item in your job list for each job you've created.
Again, you can edit, remove and add files like you want to create a custom job by
going to the File Explorer (click 'Edit Files' or 'Open Dir') or by directly clicking
the file names.
The 'Open Editor' button in the 'Submit Script' overview also allows you to edit
the job script directly.

Using the 'Job Options' button, you can add some more specifications to your job:

- Name: this will specify a name in the job composer list.
  This will not be your job name.
  The actual job name is the one that will be specified in the job script.
  If you do not specify a name there, you will see that that job gets the name
  ``sbatch`` in the 'Active Jobs' menu.
- Cluster: You can choose between ``Genius`` and ``wICE`` as a target cluster.
- Specify job script: if you have multiple job scripts in the directory, you can specify which one to run.
- Account: here you can specify which account to use. Be aware that this will overwrite the account you might have specified in your job script.
- Job array: we do not recommend using this. If you would like to use job arrays, have a look at :ref:`the worker framework<worker or atools>`.

Everything should now be set up to start a job. Any job can be started by clicking 'Submit'. You can stop it at any time by clicking 'Stop'. You cannot use the
'Submit' job to start the exact same job multiple times. You can use the 'New Job - From Selected Job' option for this. If you delete any of the jobs, you also remove
the folder that it is associated with.

Clusters
========

When selecting 'Clusters - Login Server Shell Access' you will get a terminal window in a new browser tab.
You will arrive on one of the Genius login nodes, which
you can use as you are used to, including the option to submit jobs to Genius or wICE.
As with the Genius login nodes, this means that this shell is not meant for any
calculation.
If you would like to perform calculations in an interactive job, you should be
using the :ref:`interactive shell<interactive_shell>` app.

.. _interactive-apps:

Interactive apps
================

This menu provides a range of different apps that provide a GUI.
In the background this means that you are submitting an interactive job to the cluster, in which the app will be running.

To launch any of the interactive apps, you need to fill in the resources form.
Most of the options in the resource forms are similar across all apps, but some apps require additional input from the user.
These will be explained in the specific paragraph about the apps.
A more detailed guide on how to choose your resources is available in the
:ref:`next section <choosing_your_resources>`.
Beware that by launching any app you will end up in a regular queue, so requesting a large amount of resources might result in a long queue time.

- Cluster: allows choosing between one of our :ref:`Tier-2 clusters <kul_tier2>` in production, namely Genius or wICE
- Account: the credit account you want to deduct the credits from.
  The accounts associated with your VSC number will be displayed in a dropdown menu.
- Partition: you can choose any of the existing partitions on both clusters.
  The partition names depend on your choice of cluster.
  We recommend using the ``interactive`` partition for most interactive work.
- Numbers of hours: your walltime (min 1h).
- Number of cores: the amount of cores per node. This defaults to 1.
- Required memory per core in megabytes. This defaults to 3400 MB.
- Number of GPUs. Depending on the GPU partition you have requested, you get a different device type.
  The default is 0.
  The acquired GPU will be the same as the type specified in the partition (e.g. a NVidia H100 for ``gpu_h100`` on wICE).
  For wICE, you can also request a GPU from the ``interactive`` partition.
  One GPU here is a virtual GPU slice of the available A100 GPUs.
  One GPU slice is the same as 1/7th of CUDA cores and memory of an A100 GPU.
  The interactive partition only allows you to request max 1 GPU (slice) though.
- Reservation: if you are part of a reservation, you can also use these nodes with Open Ondemand by specifying your reservation name here.
- Pre-run scriptlet: this allows you to add bash commands to your job before launching the app.
  This can be used for example for loading extra modules that you need within the app, sourcing a specific script
  or defining specific environment variable(s).

  .. warning::

     Be careful in using this feature, because you will be modifying the behavior of your session.

- Screen resolution: for apps which run inside a remote `noVNC`_ desktop (e.g. MATLAB, ParaView, etc), one
  may choose a resolution between 'FullHD', '2K' or '4K'.
  After launching the app, one may still change the compression level and the image quality of the
  transferred noVNC frames.
  E.g. opting for the lowest compression level and highest image quality can give you a crisp noVNC desktop.
- View Only (Share-able Link): for `noVNC`_ apps, you can provide a view-only access to other VSC users.
  For that, click on the 'View Only (Share-able Link)' button to copy the URL into your clipboard,
  and be able to share it with others.

  .. warning::

     As the end-user, you are responsible for all consequences of sharing your application with other
     VSC users.
     So, think twice before sharing your sensitive data, sources and information by all means.

Once you've specified all your resources, just press 'Launch' and your job will be queued.

.. _choosing_your_resources:

Choosing your resources
-----------------------

Choosing the correct resources for your interactive session is mostly the same as selecting them when
launching regular batch jobs.
For this reason, we strongly recommend you to have a look at how to specify your resources for using
both :ref:`Genius <running_jobs_on_genius>` and :ref:`wICE <running jobs on wice>`.

As mentioned above, in most cases we recommend using the 'interactive' partition on wICE for the interactive apps.
This partition is meant for lighter work, like code development, testing, debugging, visualisations,
pre- and post-processing.
Using this partition is also free, mainly to encourage you to request these resources for such work, instead
of using any of the other partitions. There are however some limitations on the amount of resources you can request here:

- Max 1 node
- Max 8 cores
- Max 1 virtual GPU slice
- Max 16h of walltime

This is put in place to ensure that these resources are kept for their original purpose, namely the interactive work.

If for some reason some of these limitations are too strict for you, or you need resources that are not available on
the interactive nodes (e.g. a full GPU, big memory nodes), you can always request nodes from another partition.
Remember however that these interactive apps are not meant for running full jobs.
If you indeed need multiple nodes or full GPUs to test your code/program, go ahead and request the resources for
your interactive app from a more suitable partition.
In the case that you have passed the testing phase, and you want to start conducting experiments,
we recommend that you make the switch to batch jobs instead, as they will not require your presence to start your code.

.. _interactive_shell:

Interactive shell
-----------------

This app will launch a shell on (one of) the requested node(s), allowing you to use these compute resources
from within a Linux terminal.
This is different than the shell you get in the "Clusters - Login Server Shell Access" menu,
which directs you towards one of the login nodes.

Currently, the :ref:`cluster modules <cluster_modules>` are not automatically loaded when your session starts.
In order to use modules, one needs to explicitly load the cluster module that adheres to the choice of
cluster and partition for his or her job.
For instance, if your job starts on wICE interactive partition, one needs to execute the following command::

    module load cluster/wice/interactive

The same applies for other choices of partitions on Genius or wICE clusters.

JupyterLab
-----------

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

In the app resource form, besides the normal choices (:ref:`listed above <interactive-apps>`),
you can also choose from different 'Toolchain and Python versions' from a drop-down menu.
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

Exporting Jupyter Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the native ``.ipynb`` format, Jupyter notebooks can be [exported to various other formats](
https://jupyterlab.readthedocs.io/en/stable/user/export.html#exporting-notebooks).
Directly exporting to PDF will however not work in this app. Instead, first export
the notebook in ``LaTex`` format (to for example a ``notebook.tex`` file) and then execute
``xelatex notebook.tex`` in a terminal, which will produce the corresponding PDF file.
You may need to first load a ``texlive`` module in order to get hold of ``xelatex``.

RStudio Server
--------------

This interactive app allows you to run an RStudio session on the cluster.
In the 'Toolchain year and R version' drop-down menu, you can choose the version
of R module that would be loaded for your session (such as `R/4.2.2-foss-2022b`).
Additionally, the `R-bundle-CRAN` and `R-bundle-Bioconductor` modules can be loaded
on top of the base R module to provide easy access to hundreds of preinstalled packages.

It is also possible to use locally installed R packages with RStudio, see :ref:`R package management<r_package_management_standard_lib>`.
RStudio furthermore allows to create RStudio projects to manage your
R environments. When doing so, we recommend to select the
`renv <https://rstudio.github.io/renv/articles/renv.html>`_ option
to ensure a completely independent R environment. Without `renv`,
loading an RStudio project may lead to incomplete R library paths.

For more information on how to use RStudio, check out the `official documentation <https://docs.posit.co/ide/user/>`__.

**Remarks:**

- Navigating between your different directories is possible using the file explorer.
  If you are navigating by clicking the folder, you will notice that you can see all user folders.
  You do not have access to these, and you will receive an error when you try to open them.
  You will also notice that you cannot use the same way of navigating after this.
  Another solution is to click the three dots on the right (...) and enter your path.
- The 'Tools-Install packages' interface does not allow you to select any other path than the default in your ``$VSC_HOME``.
  It is recommended to use the ``install.packages()`` function instead.
- RStudioServer will by default store the RStudio cache in ``$VSC_HOME/.local/share/rstudio``.
  This cache can get very large, and cause you to exceed the quota of your home directory.
  To avoid this, you can redirect this cache to your data directory by setting the ``$XDG_DATA_HOME``
  variable in your ``~/.bashrc``:

  .. code-block:: bash

    echo "export XDG_DATA_HOME=$VSC_DATA/.local/share" >> ~/.bashrc

- Additionally, it is advised to change the default behaviour of RStudio to not restore .RData
  into the workspace on start up and to never Save the workspace to .RData on exit.
  You can do this via the RStudio interface:
  Tools > Global Options > General > Workspace

Tensorboard
-----------

Tensorboard is an interactive app that allows you to visualize and measure different aspects of
your machine learning workflow.
Have a look at the `official guidelines <https://www.tensorflow.org/tensorboard/get_started>`_
for more detailed information.

The Tensorboard interactive session requires you to specify a project (or log) directory in
your submission options.
This is a relative directory starting from your ``$VSC_DATA``.
Beware that you cannot change this directory, once the session is launched.
If you redirect Tensorboard to a wrong folder (typo in path name or missing log files),
Tensorboard fails to start, and your session lands on an error page starting with the message:
'No dashboards are active for the current data set.'.

Code Server
-----------

This is the browser version of Visual Studio Code.
For more information, check out `VSCode official guidelines <https://code.visualstudio.com/docs>`_.
As a default, a Python and a Git module are already loaded, which means you can use both Python and git
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


.. _ood_matlab_app:

MATLAB
------

To launch MATLAB via OnDemand, you need to additionally specify your desired version of the software
from the drop-down menu on the resource form.
Given that our current MATLAB installations automatically detect GPU devices and CUDA libraries,
you may also request GPU(s) as resources, if needed.

Once you launch the session, a remote `noVNC`_ desktop will start on a compute node.
Once the session starts, the selected MATLAB module will be loaded, and eventually the MATLAB GUI
will pop up (after waiting for few seconds).

.. note::

   Only vsc3* users (affiliated with KU Leuven) who are members of the ``lli_matlab`` group
   have rights to use the MATLAB module (hence the MATLAB app). If you are not already member
   of the group, contact the :ref:`KU Leuven supprt team<user support VSC>` for an invitation,
   or :ref:`request joining this group<join groups>` via your VSC account page.

ParaView
--------

For visualization purposes, you may use the `ParaView app <https://www.paraview.org/>`_.
Similar to the :ref:`MATLAB app <ood_matlab_app>`, ParaView also runs inside a `noVNC`_
desktop as a compute job.

**Remarks:**

- Currently, using GPUs in ParaView is not supported yet, and just the CPU-only modules are offered.


.. _KU Leuven Open OnDemand page: https://ondemand.hpc.kuleuven.be/
.. _official JupyterLab documentation: https://docs.jupyter.org/en/latest/
.. _RStudio official documentation: https://docs.rstudio.com/
.. _noVNC: https://novnc.com/

