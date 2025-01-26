.. _ood_job_composer:

Job Composer (KU Leuven/UHasselt)
---------------------------------

As an alternative to creating job scripts with a text editor and launching
your job from the command line, the 'Jobs - Job Composer' menu item provides
a web GUI for creating and submitting batch jobs.

The Job Composer contains all the tools that allow you to launch your jobs.
This goes from basic job script building, adding necessary files, to
building and using templates for easier job creation. Under the job composer
tab you can find two other menus, namely ‘Jobs’ and ‘Templates’. As
templates are the backbone of job creation in Open OnDemand, we will start
by explaining these. The ‘Jobs’ menu is pretty much self-explanatory once
understanding this.

Templates
~~~~~~~~~

To enter the Templates menu, you can click on 'Templates' at the top once
you are in the 'Job Composer' menu. You can also access this menu by
clicking the button 'New Job'-'From Template'. Once in this menu, you should
see a table with three System Templates. The resources that are requested in
these scripts are the default settings.  The templates:

- CPU job template: a template for jobs on the thin nodes (the default
  ``batch`` partition). This is also the default template (which you will
  get when clicking 'From Default Template' under the 'New Job' button in
  the 'Jobs' menu).
- GPU job template: a template for jobs with GPU resources (``gpu``
  partition)
- Big memory CPU jobs: a template for jobs with large memory requirements
  (``bigmem`` partition)

You can create your own templates from scratch or by copying one of the
existing templates.  In both cases you will be redirected to a page where
you can provide a name, the cluster and add some notes.  To save this, you
will need to provide a path to store it in. Ondemand will create a new
subdirectory with the name of your template here.

A ``manifest.yml`` file will always be present in a template directory, It
contains all the info you provided in the set-up step.  Which other files
will be present in this directory depends on how you created your new
template.  When using the 'New Template' button, and you don't provide a
path, a copy of the default template will be created.  You can also provide
a path to an existing template or job directory. In that case that directory
and its contents will be copied.  This works for **any** directory on your
system, so be sure to provide the correct path!

The 'Copy Template' button basically does the same, but with this button,
Ondemand will automatically fill in the path of the selected template in the
template overview.  Once you use this more often, you can also use your own
templates to create new ones.  Any file that is present in that folder, will
be copied to your new one as well.

Once you've created the new template directory, you can start customizing
it. You can view the content in the directory using the Folder Explorer
(click 'View Files' on top or 'Open Dir' at the bottom). As explained above,
you can edit or remove any file, create new files or upload new files.
These files will be present in each job you create from this template.

Creating and launching jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The functioning of creating jobs is a bit similar to how you create new
templates.  Whatever method you choose, you will always create a new
directory for each job, this time located at
``$VSC_DATA/ondemand/data/projects/default/``.  The job directories will be
numbered in the order you have created them.

.. warning::

   Do not change this folder name as long as you plan on using it from the
   job menus, as this will break the linking.  When removing a job, the
   directory will be deleted as well.

To create a job, press the 'New Job' button and choose the option that best
suits your needs.  You will get a new item in your job list for each job
you've created.  Again, you can edit, remove and add files like you want to
create a custom job by going to the File Explorer (click 'Edit Files' or
'Open Dir') or by directly clicking the file names.  The 'Open Editor'
button in the 'Submit Script' overview also allows you to edit the job
script directly.

Using the 'Job Options' button, you can add some more specifications to your
job:

- Name: this will specify a name in the job composer list.
  This will not be your job name.
  The actual job name is the one that will be specified in the job script.
  If you do not specify a name there, you will see that that job gets the name
  ``sbatch`` in the 'Active Jobs' menu.
- Cluster: You can choose between ``Genius`` and ``wICE`` as a target cluster.
- Specify job script: if you have multiple job scripts in the directory, you
  can specify which one to run.
- Account: here you can specify which account to use. Be aware that this
  will overwrite the account you might have specified in your job script.
- Job array: we do not recommend using this. If you would like to use job
  arrays, have a look at :ref:`the worker framework<worker or atools>`.

Everything should now be set up to start a job. Any job can be started by
clicking 'Submit'. You can stop it at any time by clicking 'Stop'. You
cannot use the 'Submit' job to start the exact same job multiple times. You
can use the 'New Job - From Selected Job' option for this. If you delete any
of the jobs, you also remove the folder that it is associated with.

