.. _ood_t2_leuven:
===========================================
Open Ondemand on the KULeuven Tier2 cluster
===========================================

About
-----

Open OnDemand provides a user interface to HPC clusters from within a web browser. This tool supports a range of different apps and features that not only allow the
user to easily submit jobs from within the browser session, but also provide different coding GUIs, tools for plotting and more.

You can use this interface by navigating to the `KU Leuven Open Ondemand page`_. You can log in using your KU Leuven credentials. Access for vsc users from other 
organizations is not yet supported. Once logged in, you'll notice you are connected with your VSC account. 

Open Ondemand is only available for the Tier-2 wICE cluster.

Use
---

The KU Leuven Open Ondemand page provides a range of functions:

- Exploring, adapting and creating files
- Submitting and monitoring jobs, creating job templates
- Using a shell
- Using interactive apps

All of these functionalities can be used by accessing them through the tabs at the top of the page. In the following, we will describe the different parts in some more
detail.

Files
-----

This menu provides a file explorer that allows you to navigate files by clicking. You can access your ``$VSC_HOME`` and ``$VSC_DATA`` folders. Other storage is not
available here. General file explorer options like moving, deleting, modifying and creating files or directories are available as well. You can also use this interface
to download and upload files to and from your local machine. Be aware that this is not recommended for very large files.

**Good to know:** the standard 'ctrl+s' sadly does not store your files on Open Ondemand, but will trigger a save on your local machine. Luckily, there is a quite 
obvious save button on the editor page.

Jobs
----

All jobs submitted from Open Ondemand will run on wICE. The Genius cluster is not supported. This also means that all your jobs should be submitted as **slurm** jobs.
For more detail on how to run jobs on wICE, check out our :ref:`quickstart guide <wice_t2_leuven>`_.

The jobs tab has two menus: 'Active Jobs' and 'Job Composer':

Active jobs
===========

This lists all of your running, queued and completed jobs. Completed jobs will slowly dissapear after a couple of minutes. You have a handy overview of some job
details by clicking the large arrow next to the job id, including things like the node list, the account you used, the status of the job... It also gives you the
option to open the folder of the job script in the file manager. and thus inspect the created output and error files. 

If your job is still running, you can also delete it by clicking the bin under 'Actions'. The 'Active jobs' menu does not allow re-submission of your job. How to
(re-)submit jobs will be made clear in the next chapter.

Job Composer
============

This part deserves some extra attention, as there is more to it than just simply creating and editing a .slurm file. Under the job composer tab you can find two other 
menus, namely 'Jobs' and 'Templates'. As templates are the backbone of job creation in Open Ondemand, we will start by explaining this. The 'Jobs' menu is pretty much 
self-explanitory once understanding this.

Templates
~~~~~~~~~

To enter the Templates menu, you can click on 'Templates' at the top once you are in the 'Job Composer' menu. You can also access this menu by clicking the button 'New 
Job'-'From Template'. Once in this menu, you should see a table with 3 System Templates. The resources that are requested in these scripts are the default settings. 
The templates:

- CPU job template: this is a template for CPU jobs (batch partition). This is also the default template (which you will get when clicking 'From Default Template' under the 'New Job' button in the 'Jobs' menu).
- GPU job template: a template for creating GPU jobs 
- Big memory CPU jobs: a template to create job scripts that submit to the big memory partition instead of the default batch partition

You can create your own templates from scratch or by copying one of the existing templates. In both cases you will be redirected to a page where you can provide a
name, the cluster (only wICE) and add some notes. Once you save this, you will create a new folder in the templates folder 
``$VSC_DATA/ondemand/data/sys/myjobs/templates/``. This information will be saved in the ``manifest.yml`` file that is always present in each of the template folders. 
Which other files that are present in this folder will depend on how you created your new template. If you use the 'New Template' button, it will also contain the job 
script of the default template, being the CPU job template. If you use the 'Copy Template' button, the contents of the folder will depend on the template you are
copying from. Use the system template that suit your needs the best when starting out. Once you use this more often, you can also use your own templates to create new
ones. Any file that is present in that folder, will be copied to your new one as well.

Once you've created the new template folder, you can start customizing it to your needs. You could of course immediately create a new job from it, adapt some
extra options and launch it (which will be explained in the next chapter), but you can still further costumize your template folder first. You can view the files in
the folder using the Folder Explorer (click 'View Files' on top or 'Open Dir' at the bottom). As explained above, you can edit or remove any file, create new files,
upload new files... These files will be present in each job you create from this template, which means you fully adapt this to the standard set-up you use for your
jobs.

Jobs
~~~~

The functioning of creating jobs is a bit similar to how you create new templates. Whatever method you choose, you will create a new folder for each job, this time
located at ``$VSC_DATA/ondemand/data/projects/default/``. The job folders will be numbered according to the order you have created them in. **Do not change this folder name as long as you plan on using it from the job menus, as this will break the linking here.** When removing a job, the folder will be deleted as well. 

To create a job, press the 'New Job' button and choose the option that suits your needs the most. You will get a new item in your job list for each job you've created. 
Again, you can edit, remove and add files like you want to create a custom job by going to the File Explorer (click 'Edit Files' or 'Open Dir') or by directly clicking 
the file names. The 'Open Editor' button in the 'Submit Script' overview also allows you to edit the job script directly.

Using the 'Job Options' button, you can add some more specifications to your job:

- Name: this will specify a name in the job composer list. This will not be your job name. The actual job name is the one that will be specified in the job script. If you do not specify a name there, you will see that that job gets the name 'sbatch' in the 'Active Jobs' menu.
- Cluster: there is no need to change this, as you only can specify 'wice'.
- Specify job script: if you have multiple job scripts in the directory, you can specify which one to run
- Account: here you can specify which account to use. **Be aware that this will overwrite the account you might have specified in your job script**

Everything should now be set up to start a job. Any job can be started by clicking 'Submit'. You can stop it at any time by clicking 'Stop'. You cannot use the 
'Submit' job to start the exact same job multiple times. You can use the 'New Job - From Selected Job' option for this. If you delete any of the jobs, you also remove
the folder that it is associated with. 

Clusters
--------

When selecting 'Clusters - Login Server Shell Access' you will get a terminal window in a new browser tab. You will arrive on one of the Genius login nodes, which
you can use as you are used to, including the option to submit jobs to wICE. As with the Genius login nodes, this means that this shell is not meant for any 
calculations. If you would like to perform calculations in an interactive shell, you should be using the :ref:`interactive shell app<interactive_shell>`

Interactive apps
----------------

This menu provides a range of different apps that provide a GUI. In the background this means that you are submitting an interactive job to the cluster, in which the
app will be running.

To launch any of the interactive apps, you need to fill in the resources form. Be aware that you will end up in a regular queue, so requesting a large amount of 
resources might result in a long queueing time. Between all the apps, most of these options are the same. Some apps require specific information. These will be 
explained in the specific chapter about the app. A general overview of the others can be found here:

- Account: the credit account you want to deduct the credits from. The accounts associated with your vsc number will be displayed in a dropdown.
- Partition: you can choose any of the existing partitions. If you require a GPU, you can of course only submit jobs to the gpu or interactive partitions. For the most general use-cases we recommend that you use the interactive partition.
- Numbers of hours: your walltime (min 1h)
- Number of cores: the amount of cores per node. This defaults to 1.
- Required memory per core in megabytes. This defaults to 3400 MB.
- Number of GPUs. If you request a GPU of the gpu partition you will get a full A100 GPU. For the interactive partition, every GPU is a virtual GPU slice of the available A100 GPUs. One GPU is the same as 1/7th of a A100 GPU. The default is 0. You can specify the type of GPU as well: [Type]:<number> (e.g. A100:2). You can also just request a number of GPUs as <number>. Then you will be appointed the first available GPU types. In practice, both methods are the same for now. This might change if we would decide to add extra GPU types.
  
Once you've selected all your resources, just press 'Launch' and your job will be queued. In the next part, you find an overview of the currently supported apps.

.. _interactive_shell:
Interactive shell
=================

**Work in progress**

Jupyter Lab
================

With this app you can use and create Jupyter Notebooks. This can be handy both for R and Python coding. There are two kernels already available, being a Python and a
R kernel. The Python and R versions that are used for this, are the versions located in ``/usr/bin``. While you can use these to do some testing, it is not recommended 
to work with these. It is better to work with conda environments in this case. You can `install miniconda <https://docs.vscentrum.be/en/latest/software/python_package_management.html#install-miniconda>`_ if you have not installed it yet. When you do not have any conda 
environments and their associated kernels, both the Python and R installation will default to the ``~/miniconda3/bin/...`` installation.

To create any other kernels, first create a  `Python <https://docs.vscentrum.be/en/latest/software/python_package_management.html#create-an-environment>`_ or 
`R <https://docs.vscentrum.be/en/latest/software/r_package_management.html#creating-an-environment>`_ conda environment. The second step consists out of effectively
creating the kernel in your home folder. This starts with first of all activating your conda environment::

      source activate <env_name>
      
For Python you will need the ``ipykernel`` package installed in your conda environment. Then you can create the kernel as follows::

      python -m ipykernel install  --prefix=${VSC_HOME}/.local/ --name '<env_name>'
      
For R, you need both the ``jupyter_client`` and the ``irkernel`` package installed. With the following command you can create the kernel::
      
      Rscript -e 'IRkernel::installspec(prefix="${VSC_HOME}/.local/", name="<env_name>", displayname="<kernel_name>")'
      
Once the kernel is created, you will see it in the 'Launcher' menu. You can now start working in your own customized environment.

For more general information concerning Jupyter Lab, go to their ´official documentation <https://docs.jupyter.org/en/latest/>´_.

**Remarks:**

- For now, the default location is ``$VSC_HOME``.

RStudio Server
==============

This interactive app allows you to run an RStudio session on the cluster. You will be running RStudio with R 4.2.1. For more information on how to use RStudio, check 
out the ´official documentation <https://docs.rstudio.com/>´_. 

The use is very similar to regular RStudio. It is recommended to install packages in a folder on your ``$VSC_DATA`` instead of the default location though, to
avoid clogging your ``$VSC_HOME``. You can do this by using the ``lib`` argument for both the ``install.packages`` and the ``library`` function.

**Remarks:**

- Navigating between your different directories is possible using the file explorer. If you are navigating by clicking the folder, you will notice that you can see all user folders. You do not have access to these, and you will receive an error when you try to open them. You will also notice that you cannot use the same way of navigating after this. Another solution is to click the three dots on the right (...) and enter your file location.
- The 'Tools-Install packages' interface does not allow you to select any other path than the default in your ``$VSC_HOME``. It is recommended to use the ``install.packages`` function instead.

Tensorboard
===========

Tensorboard is an app that allows you to visualize and measure different ascpects of your machine learning workflow. Have a look at the `official guidelines <https://www.tensorflow.org/tensorboard/get_started>`_ for more detailed information. 

The Tensorboard interactive session requires you to specify a project (or log) directory in your submission options. This is a relative directory starting from your 
``$VSC_DATA``. It is not possible to navigate to the correct folder from within the app.

code-server
===========

This is the browser version of Visual Studio Code. For more information, check out `the official guidelines <https://code.visualstudio.com/docs>`_. As a default,
a Python and a Git module are already loaded, which means you can use both Python and git from a terminal window within code-server. How to open a terminal
window is probably one of the first things you should know: click on the three horizontal lines in the upper left corner, select 'Terminal - New Terminal'. This will
open a shell on the node you are running your session on. Notice that you are start in your ``$VSC_DATA`` folder. You can use this as a regular shell, meaning that you
can submit jobs, load modules and so on. 

Code-server contains many different options and menus, which we won't discuss all. Feel free to explore them. We will however discuss how to set up code-server to use 
any of the compatible languages and use code-server as an IDE. For each of the languages you want to use you need two things: an installation of the specific 
interpreter and an extension in code-server that allows you to connect to it. The extensions can be found in the 'extensions' menu. In what follows, the steps for
both Python and R are described. 

Python
++++++

There are multiple Python extensions available, so feel free to try and install the extension that suits you the best. This comes with the warning that only the
Microsoft Python extension has been tested by our team. To install this extension, go to 'Extensions' and search for 'Pythonn'. Install the one with as developer
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
++++

While there are also multiple extensions for using R in code-server, these don't all work as they should. The main issue here is that these extensions were not
built with use on a cluster/server in mind. Also, these extensions are often built with the idea that you are only using one R version in the background, which
sadly limits the flexibility to switch between different environments, as you can do with Python environments. 

Even with these limitations, there is still a way to work with R in code-server. For this, you need to install the 'R' extension created by Ikuyadeu. Once this
is installed, you can specify the path in the settings (click the settings wheel of the extension, then click on 'Extension settings'): search for 'R > Rterm: Linux'
and add the path to your preferred R installation. This can as well be a miniconda R installation. The packages in the environment will then also be available to you.
If you would need to switch R versions, you need to change this path and restart your terminal. Sadly, there is no direct way to change versions.

cryo-sparc
==========

**Work in progress**

ParaViewWeb
===========

**Work in progress**

.. _KU Leuven Open Ondemand page: https://ondemand.hpc.kuleuven.be/ 
