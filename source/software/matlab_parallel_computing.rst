.. _MATLAB parallel computing:

MATLAB parallel computing
=========================

General
-------

Matlab allows you to use parallel computing on a HPC cluster using the `Parallel Computing Toolbox <https://www.mathworks.com/products/parallel-computing.html>`_.
The toolbox is needed to create a cluster profile and it is this profile that will allow you to submit multi-node jobs.

KU Leuven clusters
------------------

Availability
++++++++++++

The Parallel Computing Toolbox has been enabled for all Matlab versions on the KU Leuven Tier-2 clusters.

The Matlab license of KU Leuven covers all academic users. If you would like to use Matlab, but you are not yet member of our `lli_matlab` group, you can request
access via the VSC account page (Use the 'New/Join Group' button.

Configuring Matlab for parallel computing
+++++++++++++++++++++++++++++++++++++++++

If you want to use the parallel toolbox, there are a couple of steps you have to do yourself:

Running Matlab is best done from a compute node. Request an interactive job with minimum 4 cores (Matlab loading is quite slow with only a single core) with the
`srun` or `salloc` command.

Now you can load your preferred Matlab module:

::

    $ module load <matlab_module>

We have Matlab modules available for wICE (in the 2021a toolchain) and for Genius (in the 2021a and 2018a toolchains).

Now, start Matlab and use the function  `configCluster` to set up the cluster profile. If you do not do this, the cluster profile will default to the 'local
cluster', basically meaning that it will only detect the cores on the node you are currently on.

::

    $ matlab -nodisplay          # this will avoid launching the GUI, but you can do this if you prefer (slow)
    $ # Within Matlab
    $ >> configCluster;

There is a range of additional properties that you can set on the cluster profile. Before you can edit these, you first need to get a handle on the cluster
profile:

::

    $ c=parcluster;

You can then view and edit the additional properties:

::

    $ # Access
    $ c.AdditionalProperties
    $
    $ #edit
    $ c.AdditionalProperties.<property_name> = '<property_value>'

One of these properties, you will always have to set, namely `AccountName`. Set this to the name of your credit account.

Next to this, it is also possible to change the more standard parameters of the cluster profile. One of these is the `JobStorageLocation` parameter. This defaults
to a location in your `$VSC_HOME`. It is however strongly recommended to change this to another location, e.g. `$VSC_DATA`. Changing this, or any of
the other cluster profile parameters can be done as follows:

::

    $ # Access
    $ c.JobStorageLocation = '</path/to/your/custom/jobdir>'

Both after changing any of the additional properties or the standard parameters, you will have to save that profile to keep the changes after closing your
session:

::

    $ c.saveProfile;


Submitting jobs
+++++++++++++++

Submitting jobs will happen from within Matlab. There are two ways to do this. You can start a Matlab session on a login node, or you can first request an
interactive job, where you launch your Matlab session. Which one you choose will depend on the workload you plan to have on the node before submitting a job.
As for any other work on the cluster, you can always do minor work on the login node, but for heavier calculations (before submitting your multinode job), you should
use an interactive job.

In general, we recommend to carry out the examples below via Matlab's command line interface
(as shown in the configuration section). It is also possible to use the Matlab GUI, in which case it
is best to do this via a NoMachine connection. If you then need to launch the Matlab GUI in an
interactive job, don't forget to add ``-X`` option to your `srun` or `salloc` command and keep in mind
that the GUI will necessarily be less responsive.

Now you can start both interactive and independent batch jobs with the previously configured cluster profile. Follow the steps below to submit a job.

Interactive job
***************

You can start an interactive job using the ``parpool`` function:

::

    >> c = parcluster;
    >> p = parpool(4); % requesting 4 cores

Once the job starts, all your following commands will be executed on the pool of cores you requested.


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

