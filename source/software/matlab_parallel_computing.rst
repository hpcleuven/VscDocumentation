.. _MATLAB parallel computing:

MATLAB parallel computing
=========================

General
-------

Matlab allows you to use parallel computing on a HPC cluster using the `Parallel Computing Toolbox <https://www.mathworks.com/products/parallel-computing.html>`_.
This toolbox may not be included for all Matlab installations. Try ``help distcomp`` to see if the toolbox is installed for the Matlab installation that you are using. The toolbox is needed to create a cluster profile and it is this profile that will allow you to submit multi-node jobs.

KU Leuven clusters
------------------

Availability
++++++++++++

The Parallel Computing Toolbox has been enabled for the Matlab 2022a and 2022b modules on Genius. wICE support is under development at the moment. These versions 
have been installed in the 2021a toolchain. We strongly recommend using the Matlab 2022b installation. 

The Matlab license of KU Leuven covers all academic users. If you would like to use Matlab, but you are not part of our Matlab group and would like to use this 
software, we kindly ask you to contact our helpdesk and request access.

Configuring Matlab for parallel computing
+++++++++++++++++++++++++++++++++++++++++

Using parallel computing together with Matlab does not work out of the box. Matlab needs a 'cluster profile', specifically for the 'cluster-matlab version' combination
you are planning to use. This cluster profile contains information like the amount of nodes, the resource manager, the way to submit jobs on that cluster... 
Configuring these settings can be done by running the correct script once. Next to this, there are some user-specific options that can be defined. 

Configuring a cluster profile
*****************************

We have provided some scripts that will allow to easily set up such a profile. You can download them from this 
`repository <https://github.com/hpcleuven/matlab-remote>`_. Clone this folder somewhere on your personal storage (e.g. ``$VSC_DATA``). Set your working directory to
the cloned repository:

::
    $ cd <your_preferred_location>
    $ git clone https://github.com/hpcleuven/matlab-remote.git
    $ cd <your_preferred_location>/matlab-remote

Within the folder, you will see a ``mdcs.rc`` file. This is a configuration file that allows you to adapt the cluster profile to your needs. There is only one setting 
that needs to be changed here: ``LocalJobStorageLocation``. This will define where your job output will be directed to. This script will not create the folder for you, 
so be sure to create it yourself if it does not exist yet. There is no need for quotation marks when defining this path. 

> **_NOTE:_**  Be careful: when leaving this field blank, this location will default to your ``$VSC_HOME``, which could result in quickly filling up your home directory.

Next, you'll need to load your preferred module, and start it. It is recommended to do this via an interactive job.

::

   $ # Genius
   $ module use /apps/leuven/skylake/2021a/modules/all
   $ module load MATLAB/R2022b #MATLAB/R2022a if you would like to load this version
    
Once the module is loaded, start Matlab. You can start it in a terminal without the GUI by using the ``-nodisplay`` flag. Then, run the ``configCluster`` script.
This will set up the parallel configuration.  

::

   $ matlab -nodisplay

::

   >> rehash toolbox;
   >> configCluster;
   
You will get a message as follows if it succeeded: 'Complete.  Default cluster profile set to "<cluster_name> <matlab_version>".'. You have now created a cluster
profile.

Configuring additional properties
*********************************

It is possible to set some user-specific properties and save them in your cluster profile. You can always adapt these and save the profile again, without performing
the previous step again. All of these properties are available in the ``AdditionalProperties`` property of your cluster profile. 
   
Before you will be able to adapt these properties, you first need to get a handle on the cluster:

::

   >> c = parcluster;
   
``c = parcluster`` will automatically load the correct profile based on the Matlab module you have loaded. So if you would have a profile for both R2022a and R2022b,
the correct profile will be chosen when using this command.

If you would prefer to use the local resources (i.e. the resources of the node you are currently on), use:

::

   >> c = parcluster('local');

You can set a range of additional properties on each profile. There are two properties that are required, namely ``AccountName`` and ``WallTime``. Set any 
other to your preference. Once these are saved, they will be kept in the settings of your cluster profile, but they can always be adapted again later.

::

   >> % View the additional properties
   >> c.AdditionalProperties
   >> % set the required properties
   >> c.AdditionalProperties.AccountName = <account-name>;
   >> c.AdditionalProperties.WallTime = '05:00:00';
   >> % save the profile
   >> c.saveProfile
   
Now the profile is ready, and you should be able to submit multi-node jobs with Matlab now.

Submitting jobs
+++++++++++++++

Submitting jobs will happen from within Matlab. There are two ways to do this. You can start a Matlab session on a login node, or you can first request an
interactive job, where you launch your Matlab session. Which one you choose will depend on the workload you plan to have on the node before submitting a job.
As for any other work on the cluster, you can always do minor work on the login node, but for heavier calculations (before submitting your multinode job), you should
use an interactive job. 

It is possible to use the Matlab GUI as well, on all login nodes. It is strongly recommended though to use NoMachine if you want to use the GUI though (login node
3 and 4), as starting the GUI from any other login node will be extremely slow. If you want to use a GUI on a compute node, you'd need to submit your interacive job
with X forwarding. You'll need to ``-X`` to your qsub command. Note that this is also quite slow. 

Now you can start both interactive and independent batch jobs with the previously configured cluster profile. Follow the steps below to submit a job.

Interactive job
***************

You can start an interactive job using the ``parpool`` function:

::

    >> c = parcluster;
    >> p = parpool(64); % requesting 64 cores
    
Once the job has started, you'll receive output like this:

::

    Starting parallel pool (parpool) using the 'genius R2022a' profile ...

    additionalSubmitArgs =

        '-l nodes=2:ppn=32 -l pmem=4gb -A '<account_name>' -l walltime=00:30:00'

    Connected to the parallel pool (number of workers: 64).

    ans =

        ClusterPool with properties:

                Connected: true
               NumWorkers: 64
                     Busy: false
                  Cluster: genius R2022a
            AttachedFiles: {}
        AutoAddClientPath: true
                FileStore: [1x1 parallel.FileStore]
               ValueStore: [1x1 parallel.ValueStore]
              IdleTimeout: 30 minutes (30 minutes remaining)
              SpmdEnabled: true
     EnvironmentVariables: {}

    >> <start typing your commands here>

    
Batch job
*********

Batch jobs are started with the ``batch`` function. Here we will give you an example job where we query the working directories of each of the threads Matlab is using. 
Have a look at the `Matlab documentation <https://www.mathworks.com/help/parallel-computing/run-a-batch-job.html>`_ for more information.

::

    >> c = parcluster;
    >> job = c.batch(@pwd, 1, {}, 'CurrentFolder','.', 'AutoAddClientPath',false);
    >> % request the job status
    >> job.State
    >> % Get the job outputs
    >> job.fetchOutputs{:}
    >> % delete the job
    >> job.delete

If you are running multiple jobs, you can get an overview of all jobs as follows:

::

    >> jobs = c.Jobs;
    
To get for example the output of the second job in this list, you can use the following:

::

    >> job2 = c.Jobs(2);
    >> job2.fetchOutputs{:}
    
