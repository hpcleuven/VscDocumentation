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

This menu provides a file explorer that allows you to navigate files by clicking. You can access your `$VSC_HOME` and `$VSC_DATA` folders. Other storage is not
available here. General file explorer options like moving, deleting, modifying and creating files or directories are available as well. You can also use this interface
to download and upload files to and from your local machine. Be aware that this is not recommended for very large files.

**Good to know:** the standard 'ctrl+s' sadly does not store your files on Open Ondemand, but will trigger a save on your local machine. Luckily, there is a quite 
obvious save button on the editor page.

Jobs
----

All jobs submitted from Open Ondemand will run on wICE. The Genius cluster is not supported. This also means that all your jobs should be submitted as **slurm** jobs.
For more detail on how to create slurm job scripts, have a look here (Add link to slurm pages).

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

This part deserves some extra attention, as there is more to it than just simply creating and editing a .slurm file. Fully using the Open 
Ondemand method requires some more configuration, but a well thought-out personal strategy will allow you to reap great benefits from this.

Under the job composer tab you can find two other menus, namely 'Jobs' and 'Templates'. As templates are the backbone of job creation in Open Ondemand, we will
start by explaining this. The 'Jobs' menu is pretty much self-explanitory once understanding this.

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
($VSC_DATA/ondemand/data/sys/myjobs/templates/). This information will be saved in the manifest.yml file that is always present in each of the templates folder. Which
other files that are present in this folder will depend on how you created your new template. If you use the 'New Template' button, it will also contain the job 
script of the default template, being the CPU job template. If you use the 'Copy Template' button, the contents of the folder will depend on the template you are
copying from. Use the system template that suit you needs the best when starting ou. Once you use this more often, you can also use your own templates to create new
ones. Any file that is present in that folder, will be copied to your new one as well.

Once you've created the new template folder,you can really start customizing it to your needs. You could of course immediately create a new job from it, adapt some
extra options and launch it (which will be explained in the next chapter), but you can still further costumize your template folder first. You can view the files in
the folder using the Folder Explorer (click 'View Files' on top or 'Open Dir' at the bottom). As explained above, you can edit or remove any file, create new files,
upload new files... These files will be present in each job you create from this template, which means you fully adapt this to the standard set-up you use for your
jobs.

Jobs
~~~~

The functioning of creating jobs is a bit similar to how you create new templates. Whatever method you choose, you will create a new folder for each job, this time
located at $VSC_DATA/ondemand/data/projects/default/. **Add part about folder naming** To create a job, press the 'New Job' button and choose the option that suits
your needs the most. You will get a new item in your job list for each job you've created. Again, you can edit, remove and add files like you want to create a custom
job by going to the File Explorer (click 'Edit Files' or 'Open Dir') or by directly clicking the file names. The 'Open Editor' button in the 'Submit Script' overview
also allows you to edit the job script directly.

Using the 'Job Options' button, you can add some more specifications to your job:
- Name: this will specify a name in the job composer list. This will not be your job name. The actual job name is the one that will be specified in the job script. If
  you do not specify a name there, you will see that that job gets the name 'sbatch' in the 'Active Jobs' menu.
- Cluster: there is no need to change this, as you only can specify 'wice'.
- Specify job script: if you have multiple job scripts in the directory, you can specify which one to run
- Account: here you can specify which account to use. **Be aware that this will overwrite the account you might have specified in your job script**

Everything should now be set up to start a job. Any job can be started by clicking 'Submit'. You can stop it at any time by clicking 'Stop'. You cannot use the 
'Submit' job to start the exact same job multiple times. You can use the 'New Job - From Selected Job' option for this. If you delete any of the jobs, you also remove
the folder that is associated with it. 

Clusters
--------

When selecting 'Clusters - Login Server Shell Access' you will get a terminal window in a new browser tab. You will arrive on one of the Genius login nodes, which
you can use as you are used to, including the option to submit jobs to wICE. **(Is this true? And will this look like a Genius login node, or will this be generalized to 'Tier2 login node?)**.
As with the Genius login nodes, this means that this shell is not meant for any calculations. If you would like an interactive shell, you should be using the 
:ref:`interactive shell<interactive_shell>`

Interactive apps
----------------

This menu provides a range of different apps that provide a GUI, while working on the interactive nodes in the background. This is an ideal environment to write, test
and debug code, do post-hoc analysis, plot... This is not meant to launch full jobs on. As you are always working on interactive nodes, you will notice
that you can only request a limited amount of resources. 

To launch any of the interactive apps, you need to fill in the resources you require. Between all the apps, most of them are the same. Some apps require specific
information. These will be explained in the specific chapter about the app. A general overview of the others can be found here:

- Account: the credit account you want to deduct the credits from. The accounts associated to your vsc number will be displayed in a dropdown.
- Partition: this field is only relevant if you or your research group has dedicated nodes. Otherwise this will always default to the interactive partition.
- Numbers of hours: your walltime (min 1h)
- Number of cores: the amount of cores per node. This defaults to 1.
- Required memory per core in megabytes. This defaults to 3400 MB.
- Number of GPUs. Every GPU is a virtual GPU slice of the available A100 GPUs. One GPU is the same as 1/7th of a A100 GPU. The default is 0. You can specify the 
  type of GPU as well: [Type]:<number> (e.g. A100:2). You can also just request a number of GPUs as <number>. Then you will be appointed the first available GPU
  types. In practice, both methods are the same for now. This might change if we would decide to add extra GPU types to the interactive partition.
  
Once you've selected all your resources, just press 'Launch' and your job will be queued. In the next part, you find an overview of the currently supported apps.

Jupyter Notebook
================

RStudio Server
==============

Tensorboard
===========

code-server
===========

cryo-sparc
==========




.. _KU Leuven Open Ondemand page: https://ondemand.hpc.kuleuven.be/ 
