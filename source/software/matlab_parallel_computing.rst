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

The Matlab license of KU Leuven covers all academic users. If you would like to use Matlab, but you are not yet member of our ``lli_matlab`` group, you can request
access via the VSC account page (Use the 'New/Join Group' button).

Configuring Matlab for parallel computing
+++++++++++++++++++++++++++++++++++++++++

If you want to use the parallel toolbox, there are a couple of steps you have to do yourself:

Running Matlab with Parallel Server should be done from a compute node. Request an interactive job with minimum 4 cores (Matlab loading is quite slow with only a single core) with the
``srun`` or ``salloc`` command.

Now you can load your preferred Matlab module:

::

    $ module load <matlab_module>

We have Matlab modules available for both wICE and Genius. Use the command ``module av MATLAB`` on the compute node to check for available versions.

Now, start Matlab and use the function  ``configCluster`` to set up the cluster profile. If you do not do this, the cluster profile will default to the 'local
cluster', basically meaning that it will only detect the cores on the node you are currently on.

::

    $ matlab -nodisplay          # the '-nodisplay' option avoids launching the GUI, but you may leave this out (slow)
    $ # Within Matlab
    $ >> configCluster;

The ``configCluster`` function will request you to specify a cluster (``wice`` or ``genius``). Please choose the one you are on already.

There is a range of additional properties you can set for the cluster profile. Before you can edit these, you first need to get a handle on the cluster
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

There are two properties that have to be set to be able to submit jobs, namely ``AccountName`` and ``partition``. ``AccountName`` is the name
of your credit account.

Next to this, it is also possible to change the more standard parameters of the cluster profile. One of these is the ``JobStorageLocation`` parameter. This defaults
to a location in your ``$VSC_HOME``. It is however strongly recommended to change this to another location, e.g. ``$VSC_DATA``. Changing this, or any of
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

Submitting jobs will happen from within Matlab. This means you will have to start a Matlab instance first. You can only use the Parallel Server Toolbox (and thus submit jobs from
within Matlab) from a compute node. You can also not use the GUI from a compute node, so this means that you cannot use the GUI together with Parallel Server. 

First of all, request an interactive job. Once you are inside the interactive job, you can load your preferred module, as
explained above. You can then load the Matlab and then launch the Matlab command line (with ``matlab -nodisplay``).

With the parallel toolbox, you can now submit jobs from within Matlab to the cluster. You can start both interactive and independent batch jobs with the previously configured
cluster profile. In both cases, you request a number of threads, either using the ``parpool`` or ``batch``
function. Under the hood, Matlab launches a Slurm job to request resources of the system. Different from submitting a Slurm job yourself, there is no direct way to specify the number of nodes and cores.
Matlab just requests a number of tasks, and the system gives whatever is available, meaning that cores could be spread out over a number of nodes.

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

