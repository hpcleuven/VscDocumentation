.. _MATLAB parallel computing:

MATLAB parallel computing
=========================

Matlab allows you to use parallel computing on a HPC cluster using the 'Parallel Computing Toolbox <https://www.mathworks.com/products/parallel-computing.html>'_.
Only Matlab installations that have this installed, can be configured to use this. This documentation will describe how to configure this. Be aware that this has only
been tested for some installations on the KU Leuven Tier-2 clusters.

Availability
------------

The Parallel Computing Toolbox has been installed in the Matlab 2022a and 2022b on Genius. wICE support is in development at the moment. These versions have been
installed in the 2021a toolchain. We strongly recommend using Matlab 2022b installation. 

The Matlab license of KU Leuven covers all academic users. If you would like to use Matlab, but you are not part of our Matlab group and would like to use this 
software, we kindly ask you to contact our helpdesk (hpcinfo@kuleuven.be) and request access.

Configuring Matlab for parallel computing
-----------------------------------------

Using parallel computing together with Matlab does not work out of the box. You will need to follow some (simple) configurations steps, that will be explained here.

First of all, you will need some scripts that will configure Matlab for parallel use. You can download the appropriate script from this 
'repository <https://github.com/hpcleuven/matlab-remote>'_. Place this folder somewhere on your cluster storage (e.g. $VSC_DATA). Set your working directory to
the directory where you saved the scripts. Within the folder, you will see a `mdcs.rc` file. This is a configuration file that allows you to adapt the cluster
profile to your needs. There is only one setting that needs to be changed with the approach you are using here: `LocalJobStorageLocation`. This will define where
your job output will be directed to. There is no need for quotation marks when defining this path. **Be carefull**: when leaving this field blank, this location will 
default to your $VSC_HOME, which could result in quickly filling up your home directory.

Next, you'll need to load the module, and start it. It is recommended to request an interactive job for this beforehand.

   $ # Genius
   $ module use /apps/leuven/skylake/2021a/modules/all
   $ module load MATLAB/R2022b #MATLAB/R2022a if you would like to load this version
    
Once the module is loaded, start Matlab. You can start it in a terminal without the GUI by using the `-nodisplay` flag. Then, run the `configCluster` script.
This will set up the parallel configuration.  

   $ matlab -nodisplay
   
   >> rehash toolbox;
   >> configCluster;
   
You will get a message as follows if it succeeded: 'Complete.  Default cluster profile set to "<cluster_name> <matlab_version>".'. 
   
Before you will be able to submit multi-node jobs to the cluster, you will first need to get a handle on the cluster, and then set the additional properties of the 
loaded profile. Once these are saved, they will be kept in the settings of your cluster profile, but they can always be adapted again later.

   >> % get a handle on the cluster
   >> c = parcluster;
   >> % If you would prefer to use the local resources (i.e. the resources of the node you are currently on), use:
   >> c = parcluster('local');

If you would have multiple cluster profiles, you can also load the correct cluster profile with:

   >> c = parcluster("<profile_name>") % for example "Genius R2022a"
   
You can set a range of additional properties on each cluster profile. There are two properties that are required, namely `AccountName` and `WallTime`. Set any other
to your preference.

   >> % View the additional properties
   >> c.AdditionalProperties
   >> % set the required properties
   >> c.AdditionalProperties.AccountName = <account-name>;
   >> c.AdditionalProperties.WallTime = '05:00:00';
   >> % save the profile
   >> c.saveProfile
   
Now the profile is ready, and you should be able to submit multi-node jobs with Matlab now.

Submitting jobs
---------------

You can start both interactive and independent batch jobs with this profile. Here, we will show how to start these jobs from an opened Matlab session.

Interactive job
+++++++++++++++

You can start an interactive job using the `parpool` function:

    >> c = parcluster;
    >> p = parpool(64); % requesting 64 cores
    
Batch job
+++++++++

Batch jobs are started with the `batch` function. Here we will give you an example job where we query the names of the nodes Matlab is running on. Have a look
at the 'Matlab documentation <https://www.mathworks.com/help/parallel-computing/run-a-batch-job.html>'_ for more information.

    >> c = parcluster;
    >> job = c.batch(@pwd, 1, {}, 'CurrentFolder','.', 'AutoAddClientPath',false);
    >> % request the job status
    >> job.State
    >> % Get the job outputs
    >> job.fetchOutputs{:}
    >> % delete the job
    >> job.delete

If you are running multiple jobs, you can get an overview of all jobs as follows:

    >> jobs = c.Jobs;
    
To get for example the output of the second job in this list, you can use the following:

    >> job2 = c.Jobs(2);
    >> job2.fetchOutputs{:}
    
