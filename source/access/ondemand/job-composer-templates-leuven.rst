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

