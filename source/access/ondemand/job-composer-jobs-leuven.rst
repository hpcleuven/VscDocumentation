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
