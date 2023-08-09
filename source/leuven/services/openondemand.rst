.. _ood_t2_leuven:
===========================================
Open OnDemand on the KULeuven Tier2 cluster
===========================================

About
-----

Open OnDemand provides a user interface to HPC clusters from within a web browser. 
This tool supports a range of different apps and features that not only allow the
user to easily submit jobs from within the browser session, but also provide different 
coding GUIs, tools for plotting and more.
Open OnDemand is available for the Tier-2 Genius and wICE clusters.

You can use this interface by navigating to the `KU Leuven Open OnDemand page`_. 
You can log in using your KU Leuven or VSC credentials. 
Access is only granted to VSC3 users at the moment.
Once logged in, you'll notice you are connected with your VSC account. 

Use
---

The KU Leuven Open OnDemand page provides a range of functions:

- Exploring, adapting and creating files
- Submitting and monitoring jobs, creating job templates
- Opening a shell on one of the login nodes
- Using interactive apps

All of these functionalities can be used by accessing them through the tabs at the top of the page. In the following, we will describe the different parts in 
some more detail.

Files
-----

This menu provides a file explorer that allows you to navigate files by clicking. You can access your ``$VSC_HOME`` and ``$VSC_DATA`` folders. Other storage is not
available here. General file explorer options like moving, deleting, modifying and creating files or directories are available as well. You can also use this interface
to download and upload files to and from your local machine. Be aware that this is not recommended for very large files.

**Good to know:** the standard 'ctrl+s' sadly does not store your files on Open OnDemand, but will trigger a save on your local machine. Luckily, there is a quite 
obvious save button on the editor page.

Jobs
----

All jobs submitted from Open OnDemand can run on Genius and wICE. 
This also means that all your jobs should be submitted as **Slurm** jobs.
For more detail on how to run jobs on wICE, check out our 
:ref:`quickstart guide <wice_t2_leuven>`.

The jobs tab has two menus: 'Active Jobs' and 'Job Composer':

Active jobs
===========

This lists all of your running, queued and completed jobs. 
Completed jobs will disappear after a couple of minutes. 
You have a handy overview of some job details by clicking the large arrow next 
to the job id, including things like the node list, the account you used, and 
the status of the job. 
It also gives you the option to open the folder of the job script in the file 
manager, and thus inspect the created output and error files. 

If your job is still running, you can also delete it by clicking the bin under 'Actions'. The 'Active jobs' menu does not allow re-submission of your job. How to
(re-)submit jobs will be made clear in the next chapter.

Job Composer
============

The Job Composer contains the tools that allow you to set everything up for launching your jobs. This goes from basic job script building, adding necessary files, 
to building and using templates for easier job creation. Under the job composer tab you can find two other menus, namely 'Jobs' and 'Templates'. As templates are the 
backbone of job creation in Open OnDemand, we will start by explaining this. The 'Jobs' menu is pretty much self-explanatory once understanding this.

Templates
~~~~~~~~~

To enter the Templates menu, you can click on 'Templates' at the top once you are in the 'Job Composer' menu. You can also access this menu by clicking the button 'New 
Job'-'From Template'. Once in this menu, you should see a table with 3 System Templates. The resources that are requested in these scripts are the default settings. 
The templates:

- CPU job template: a template for jobs on the thin nodes (the default ``batch`` partition). This is also the default template (which you will get when clicking 'From Default Template' under the 'New Job' button in the 'Jobs' menu).
- GPU job template: a template for jobs with GPU resources (``gpu`` partition) 
- Big memory CPU jobs: a template for jobs with large memory requirements (``bigmem`` partition)

You can create your own templates from scratch or by copying one of the existing templates. 
In both cases you will be redirected to a page where you can provide a
name, the cluster and add some notes. 
Once you save this, you will create a new folder in the templates folder 
``$VSC_DATA/ondemand/data/sys/myjobs/templates/``. 
This information will be saved in the ``manifest.yml`` file that is always present 
in each of the template folders. 
Which other files will be present in this folder depends on how you created your new template. 
If you use the 'New Template' button, it will also contain the job 
script of the default template, being the CPU job template. 
If you use the 'Copy Template' button, the contents of the folder will depend on the 
template you are copying from. 
Use the system template that suit your needs the best when starting out. 
Once you use this more often, you can also use your own templates to create new ones. 
Any file that is present in that folder, will be copied to your new one as well.

Once you've created the new template folder, you can start customizing it to your needs. You could of course immediately create a new job from it, adapt some
extra options and launch it (which will be explained in the next chapter), but you can still further customize your template folder first. You can view the files in
the folder using the Folder Explorer (click 'View Files' on top or 'Open Dir' at the bottom). As explained above, you can edit or remove any file, create new files,
upload new files. 
These files will be present in each job you create from this template, which means you fully adapt this to the standard set-up you use for your
jobs.

Jobs
~~~~

The functioning of creating jobs is a bit similar to how you create new templates. 
Whatever method you choose, you will create a new folder for each job, this time
located at ``$VSC_DATA/ondemand/data/projects/default/``.
The job folders will be numbered in the order you have created them. 
**Do not change this folder name as long as you plan on using it from the job menus, as this will break the linking.** 
When removing a job, the folder will be deleted as well. 

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
- Account: here you can specify which account to use. **Be aware that this will overwrite the account you might have specified in your job script.**
- Job array: we do not recommend using this. If you would like to use job arrays, have a look `here <https://docs.vscentrum.be/en/latest/jobs/worker_or_atools.html>`_.

Everything should now be set up to start a job. Any job can be started by clicking 'Submit'. You can stop it at any time by clicking 'Stop'. You cannot use the 
'Submit' job to start the exact same job multiple times. You can use the 'New Job - From Selected Job' option for this. If you delete any of the jobs, you also remove
the folder that it is associated with. 

Clusters
--------

When selecting 'Clusters - Login Server Shell Access' you will get a terminal 
window in a new browser tab. 
You will arrive on one of the Genius login nodes, which
you can use as you are used to, including the option to submit jobs to Genius or wICE. 
As with the Genius login nodes, this means that this shell is not meant for any 
calculations. 
If you would like to perform calculations in an interactive job, you should be 
using the :ref:`interactive shell app<interactive_shell>`

Interactive apps
----------------

This menu provides a range of different apps that provide a GUI. In the background this means that you are submitting an interactive job to the cluster, in which the
app will be running.

To launch any of the interactive apps, you need to fill in the resources form. Be aware that you will end up in a regular queue, so requesting a large amount of 
resources might result in a long queue time. Between all the apps, most of these options are the same. Some apps require specific information. These will be 
explained in the specific paragraph about the app. A general overview of the others can be found below. A more detailed guide on how to choose your resources
is available in the next chapter.

- Account: the credit account you want to deduct the credits from. The accounts associated with your VSC number will be displayed in a dropdown.
- Partition: you can choose any of the existing partitions on both clusters. We recommend using the ``interactive`` partition for most interactive work on wICE. Be aware that this partition is not available on Genius. There it is recommended to just request the regular ``batch`` partition.
- Numbers of hours: your walltime (min 1h).
- Number of cores: the amount of cores per node. This defaults to 1.
- Required memory per core in megabytes. This defaults to 3400 MB.
- Number of GPUs. If you request a GPU of the ``gpu`` partition you will get a full A100 GPU. For the ``interactive`` partition, every GPU is a virtual GPU slice of the available A100 GPUs. One GPU is the same as 1/7th of a A100 GPU. The default is 0. You can specify the type of GPU as well: [Type]:<number> (e.g. A100:2). You can also just request a number of GPUs as <number>. Then you will be appointed the first available GPU types. In practice, both methods are the same for now. This might change if we would decide to add extra GPU types. **The interactive partition only allows you to request max 1 GPU (slice) though.**
- Reservation: if you are part of a reservation, you can also use these nodes with Open Ondemand by specifying your reservation name here.
- Pre-run scriptlet: this allows you to add bash commands to your job before launching the app. This can be used for example for loading extra modules that you need within the app. **Be aware that this feature is still somewhat experimental, and its functionality also depends on the app you are running (mainly RStudio Server has some issues here). If you would like to use this feature, but you run into problems, please contact our helpdesk.**
  
Once you've selected all your resources, just press 'Launch' and your job will be queued. In the next part, you find an overview of the currently supported apps.

Choosing your resources
=======================

Choosing the correct resources for your interactive session is mostly the same as selecting them when launching regular batch jobs. For this reason we strongly
recommend you to have a look at how to specify your resources both on `Genius <https://docs.vscentrum.be/en/latest/leuven/genius_quick_start.html#running-jobs-on-genius>`_ and `wICE <https://docs.vscentrum.be/en/latest/leuven/wice_quick_start.html#running-jobs-on-wice>`_.

As mentioned above, in most cases we recommend using the ``interactive`` partition on wICE for your interactive apps. This partition is meant for lighter work, like
visualisations, testing and pre- and postprocessing. Using this partition is also free, mainly to encourage you to request these resources for such work, instead
of using any of the other partitions. There are however some limitations on the amount of resources you can request here:

- Max 1 node
- Max 8 cores
- Max 1 virtual GPU slice
- Max 16h of walltime

This is put in place to ensure that these resources are kept for their original purpose, namely the interactive work.

If for some reason some of these limitations are too strict for you, or you need resources that are not available on the interactive nodes (e.g. a full GPU, big 
memory nodes), you can always request nodes from another partition. Remember however that these interactive apps are not meant for running full jobs. If you
indeed need multiple nodes or full GPUs to test your code/program, go ahead and request the resources for your interactive app. In the case that you have passed
the testing phase and you want to start conducting experiments, we recommend that you make the switch to batch jobs instead, as they will not require
your presence to start your code.

.. _interactive_shell:
Interactive shell
=================

This app will launch a shell on (one of the) requested nodes, allowing you to use these compute resources from within a Linux terminal. This is different
than the shell you get in the "Clusters" menu, which directs you towards one of the login nodes.

Jupyter Lab
================

With this app you can use and create Jupyter Notebooks. This can be handy both for R and Python coding. There are two kernels already available, being a Python and a
R kernel. The Python and R versions that are used for this, are the versions located in ``/usr/bin``. While you can use these to do some testing, it is not recommended 
to work with these. It is better to work with conda environments in this case. You can `install miniconda <https://docs.vscentrum.be/en/latest/software/python_package_management.html#install-miniconda>`_ if you have not installed it yet. When you do not have any conda 
environments and their associated kernels, both the Python and R installation will default to the ``~/miniconda3/bin/...`` installation.

To create any other kernels, first create a  `Python <https://docs.vscentrum.be/en/latest/software/python_package_management.html#create-an-environment>`_ or 
`R <https://docs.vscentrum.be/en/latest/software/r_package_management.html#creating-an-environment>`_ conda environment. The second step consists out of effectively
creating the kernel in your ``$VSC_HOME/.local`` folder, as Jupyter will look for kernels in this location. The following commands should be excecuted from a shell, 
and only need to be done once for the set-up of each new kernel. This starts with first of all activating your conda 
environment::

      source activate <env_name>
      
For Python you will need the ``ipykernel`` package installed in your conda environment. Then you create the kernel as follows::

      python -m ipykernel install  --prefix=${VSC_HOME}/.local/ --name '<env_name>'
      
For R, you need both the ``jupyter_client`` and the ``irkernel`` package installed. With the following command you can create the kernel::
      
      Rscript -e 'IRkernel::installspec(prefix="${VSC_HOME}/.local/", name="<env_name>", displayname="<kernel_name>")'
      
Once the kernel is created, you will see it in the 'Launcher' menu. You can now start working in your own customized environment.

For more general information concerning Jupyter Lab, go to their `official documentation <https://docs.jupyter.org/en/latest/>`_.

**Remarks:**

- The start location is `$VSC_DATA`
- At the moment, we do not support installing extensions in Jupyter Lab

RStudio Server
==============

This interactive app allows you to run an RStudio session on the cluster. You will be running RStudio with R 4.2.1. For more information on how to use RStudio, check 
out the `official documentation <https://docs.rstudio.com/>`_. 

The use is very similar to regular RStudio. It is recommended to install packages in a folder on your ``$VSC_DATA`` instead of the default location though, to
avoid clogging your ``$VSC_HOME``. You can do this by using the ``lib`` argument for both the ``install.packages`` and the ``library`` function.

**Remarks:**

- Navigating between your different directories is possible using the file explorer. If you are navigating by clicking the folder, you will notice that you can see all user folders. You do not have access to these, and you will receive an error when you try to open them. You will also notice that you cannot use the same way of navigating after this. Another solution is to click the three dots on the right (...) and enter your file location.
- The 'Tools-Install packages' interface does not allow you to select any other path than the default in your ``$VSC_HOME``. It is recommended to use the ``install.packages`` function instead.

Tensorboard
===========

Tensorboard is an app that allows you to visualize and measure different aspects of your machine learning workflow. Have a look at the `official guidelines <https://www.tensorflow.org/tensorboard/get_started>`_ for more detailed information. 

The Tensorboard interactive session requires you to specify a project (or log) directory in your submission options. This is a relative directory starting from your 
``$VSC_DATA``. It is not possible to navigate to the correct folder from within the app.

code-server
===========

This is the browser version of Visual Studio Code. For more information, check out `the official guidelines <https://code.visualstudio.com/docs>`_. As a default,
a Python and a Git module are already loaded, which means you can use both Python and git from a terminal window within code-server. How to open a terminal
window is probably one of the first things you should know: click on the three horizontal lines in the upper left corner, select 'Terminal - New Terminal'. This will
open a shell on the node you are running your session on. Notice that you are start in your ``$VSC_DATA`` folder. You can use this as a regular shell, meaning that you
can submit jobs, load modules and so on. 

Code-server contains many different options and menus, but only a few will be discussed here. Feel free to explore them. We will however discuss how to set up 
code-server to use, any of the compatible languages and use code-server as an IDE. For each of the languages you want to use you need two things: an installation of 
the specific interpreter and an extension in code-server that allows you to connect to it. The extensions can be found in the 'extensions' menu. In what follows, the 
steps for both Python and R are described. 

Python
~~~~~~

There are multiple Python extensions available, so feel free to try and install the extension that suits you the best. This comes with the warning that only the
Microsoft Python extension has been tested by our team. To install this extension, go to 'Extensions' and search for 'Python'. Install the one with as developer
'ms-python'. If you now open a script, you can now use code-server as an IDE and run the lines of code from within the script (the shortkey is shift+enter).
Code-server will start a Python session with the currently selected Python interpreter. If you did not specify another one, this should default to the loaded Python
module. This Python extension gives you the possibility to choose other interpreters as well. In the right down corner, you can see <python-version-number> right next
to 'Python'. If you click that, a window will appear where you can select your Python version. Next to the module version, you should see at least some system Python
versions (/bin/python). You can also load other modules, or you can also use conda environments here (if you have any conda environments already, you should see
them here as well).

If you need more information about creating your customized Python environments, have a look `here <https://docs.vscentrum.be/en/latest/software/python_package_management.html>`_. 

**Remarks:**

- Whenever loading a new Python interpreter,you will have to kill your current Python terminal before you will be able to use this new interpreter.


R
~~~~~~

For full functionality, it is recommended to work with conda environments. For the time being, there are some issues with using modules together with
functionalities, like plotting. 

There are some package requirements if you want to use R in code-server. The following command creates a functional environment (of course, add any other
packages you need):

`conda create -n <env_name> -c conda-forge r-base r-remotes r-languageserver r-httpgd r-jsonlite`

Once you've created your environment, go ahead and start a code-server session on Open Ondemand. On the lefthand side, go to the extension menu and search
for 'R'. You should install the 'R' extension of 'REditorSupport'.

Now there are two ways to use the R installation inside your conda environment:

- Open a terminal (three horizontal lines in the upper left corner - Terminal - New Terminal), and activate your conda environment. Now type 'R' in the terminal and you will be able to use your scripts interactively (R gets attached as soon as you start it).
- You can also set the path to the R version that needs to be attached (better if you always use the same conda environment). Go to 'Extensions', and click the settings wheel next to the R extension. Select 'Extension Settings' and search for the 'R > RTerm: Linux' setting. Paste the path to your conda env there (`/path/to/miniconda/envs/<env_name>/lib/R`)

**Remarks:**

- Running lines of code is 'ctrl+enter' for R.

cryo-sparc
==========

**Work in progress**

ParaViewWeb
===========

**Work in progress**

.. _KU Leuven Open OnDemand page: https://ondemand.hpc.kuleuven.be/ 
