.. _MATLAB parallel computing:

MATLAB parallel computing
=========================

MATLAB allows you to use parallel computing on a HPC cluster using the `Parallel Computing Toolbox <https://www.mathworks.com/products/parallel-computing.html>`_.


|kuluh| The toolbox is needed to create a cluster profile and it is this profile that will allow you to submit multi-node jobs.

|vub| The VUB cluster is not set up to submit Slurm jobs using the parallel computing toolbox or to run multi-node jobs. It can however still be used to spawn workers that make use of the resources of your single-node job.


Availability
++++++++++++

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      The Parallel Computing Toolbox has been enabled for all MATLAB versions on the KU Leuven Tier-2 clusters.

      The MATLAB license of KU Leuven covers all academic users. If you would like to use MATLAB, but you are not yet member of our ``lli_matlab`` group, you can request
      access via the VSC account page (Use the 'New/Join Group' button).

   .. tab-item:: VUB
      :sync: vub

      MATLAB and the Parallel Computing Toolbox are available to all users and on all nodes of the Hydra and Anansi clusters.

Configuring MATLAB for parallel computing
+++++++++++++++++++++++++++++++++++++++++

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      If you want to use the parallel toolbox, there are a couple of steps you have to do yourself:

      Running MATLAB with Parallel Server should be done from a compute node. Request an interactive job with minimum 4 cores (MATLAB loading is quite slow with only a single core) with the
      ``srun`` or ``salloc`` command.

      Now you can load your preferred MATLAB module:

      ::

          $ module load <matlab_module>

      We have MATLAB modules available for both wICE and Genius. Use the command ``module av MATLAB`` on the compute node to check for available versions.

      Now, start MATLAB and use the function  ``configCluster`` to set up the cluster profile. If you do not do this, the cluster profile will default to the 'local
      cluster', basically meaning that it will only detect the cores on the node you are currently on.

      ::

          $ matlab -nodisplay          # the '-nodisplay' option avoids launching the GUI, but you may leave this out (slow)
          $ # Within MATLAB
          $ >> configCluster;

      The ``configCluster`` function will request you to specify a cluster (``wice`` or ``genius``). Please choose the one you are on already.

      There is a range of additional properties you can set for the cluster profile. Before you can edit these, you first need to get a handle on the cluster
      profile:

      .. code-block:: matlabsession

          >> c=parcluster;

      You can then view and edit the additional properties:

      .. code-block:: matlabsession

          >> % Access
          >> c.AdditionalProperties
          >>
          >> % Edit
          >> c.AdditionalProperties.<property_name> = '<property_value>'

      There are two properties that have to be set to be able to submit jobs, namely ``AccountName`` and ``partition``. ``AccountName`` is the name
      of your credit account.

      Next to this, it is also possible to change the more standard parameters of the cluster profile. One of these is the ``JobStorageLocation`` parameter. This defaults
      to a location in your ``$VSC_HOME``. It is however strongly recommended to change this to another location, e.g. ``$VSC_DATA``. Changing this, or any of
      the other cluster profile parameters can be done as follows:

      .. code-block:: matlabsession

          >> % Access
          >> c.JobStorageLocation = '</path/to/your/custom/jobdir>'

      Both after changing any of the additional properties or the standard parameters, you will have to save that profile to keep the changes after closing your
      session:

      .. code-block:: matlabsession

          >> c.saveProfile;

   .. tab-item:: VUB
      :sync: vub

      If you want to use the parallel toolbox, there are a couple of steps you have to do yourself:

      Running MATLAB should be done from a compute node. Request an interactive job with minimum 4 cores (MATLAB loading is quite slow with only a single core) with the
      ``srun`` or ``salloc`` command or load the Open OnDemand MATLAB app.

      Now you can load your preferred MATLAB module:

      ::

          $ module load <matlab_module>

      The first thing needed to configure MATLAB for parallel computing is to create a `parallel.Cluster <https://nl.mathworks.com/help/parallel-computing/parallel.cluster.html>`_ object. This object allows us to create pools of workers or independent batch jobs.

      .. code-block:: matlabsession

          >> c = parcluster("Processes");

      This creates a ``parallel.Cluster`` object ``c`` with the ``"Processes"`` profile. Its properties can then be viewed and edited. To view:

      .. code-block:: matlabsession

          >> % Access
          >> c.JobStorageLocation

      One of the parameters is the ``JobStorageLocation`` parameter. This defaults
      to a location in your ``$VSC_HOME``. It is however strongly recommended to change this to another location, e.g. ``$VSC_DATA``. Changing this, or any of
      the other cluster profile parameters can be done as follows:

      .. code-block:: matlabsession

          >> % Edit
          >> c.JobStorageLocation = '</path/to/your/custom/jobdir>'

      Useful parameters to set:

      * ``c.NumThreads`` Number of computational threads to use on each job.
      * ``c.JobStorageLocation`` Folder where job data is stored on the client.
      * ``c.PreferredPoolNumWorkers`` Preferred number of workers to start in a parallel pool.

      Both after changing any of the additional properties or the standard parameters, you will have to save that profile to keep the changes after closing your
      session. We can save it under the name ``MyProfile``:

      .. code-block:: matlabsession

          >> c.saveAsProfile("MyProfile");

      In our next session we can then load the saved profile using:

      .. code-block:: matlabsession

          >> c = parcluster("MyProfile");

Submitting jobs
+++++++++++++++

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Submitting jobs will happen from within MATLAB. This means you will have to start a MATLAB instance first. You can only use the Parallel Server Toolbox (and thus submit jobs from
      within MATLAB) from a compute node. You can also not use the GUI from a compute node, so this means that you cannot use the GUI together with Parallel Server. 

      First of all, request an interactive job. Once you are inside the interactive job, you can load your preferred module, as
      explained above. You can then launch the MATLAB command line (with ``matlab -nodisplay``).

      With the parallel toolbox, you can now submit jobs from within MATLAB to the cluster. You can start both interactive and independent batch jobs with the previously configured
      cluster profile. In both cases, you request a number of threads, either using the ``parpool`` or ``batch``
      function. Under the hood, MATLAB launches a Slurm job to request resources of the system. Different from submitting a Slurm job yourself, there is no direct way to specify the number of nodes and cores.
      MATLAB just requests a number of tasks, and the system gives whatever is available, meaning that cores could be spread out over a number of nodes.

   .. tab-item:: VUB
      :sync: vub

      .. note:: Using the ``"Processes"`` profile will not submit **Slurm jobs** but will create **MATLAB batch jobs** that use the resources available to the current job.

      First of all, request an interactive job. Once you are inside the interactive job, you can load your preferred module, as
      explained above. You can then launch the MATLAB command line (with ``matlab -nodisplay``). Alternatively, you can use the Open OnDemand MATLAB app and use the GUI.

      With the parallel toolbox, you can now start both interactive and independent batch jobs with the previously configured
      cluster profile. In both cases, you request a number of threads, either using the ``parpool`` or ``batch``
      function. The ``"Processes"`` profile is able to use the resources you requested for the Slurm job that is running MATLAB.

Interactive job
***************

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      You can start an interactive job using the ``parpool`` function:

      .. code-block:: matlabsession

          >> c = parcluster;
          >> p = parpool(4); % requesting 4 cores

      Once the job starts, all your following commands will be executed on the pool of cores you requested.

   .. tab-item:: VUB
      :sync: vub

      You can start an interactive job using the ``parpool`` function with the profile ``MyProfile`` that we saved earlier.

      .. code-block:: matlabsession

          >> c = parcluster("MyProfile");
          >> p = c.parpool(4); % requesting 4 cores

      Starts a pool with 4 workers. Omit the number of cores to start a pool with ``c.PreferredPoolNumWorkers`` workers or if this is set to ``Inf`` with ``c.NumWorkers`` workers (which by default is the number of cores in your Slurm job.)

      You can then execute commands on these workers using for example the `parfeval <https://www.mathworks.com/help/matlab/ref/parfeval.html>`_ and the `parfor <https://www.mathworks.com/help/matlab/ref/parfor.html>`_ commands.

      For example, using the worker to populate an array:

      .. code-block:: matlabsession

          % Run a parfor over 4 iterations
          >> parfor idx = 1:4
              a(idx) = idx
          end

      The parallel pool can be deleted as follows.

      .. code-block:: matlabsession

         >> p.delete

      .. note::
          If you use a ``parallel.Cluster`` object with the ``Processes`` profile inside your single-node job and only use ``parpool``, then a threads pool is often the better choice since in such a parallel pool the workers share memory.
          See the following `blogpost <https://blogs.mathworks.com/matlab/2025/03/27/parallel-computing-in-matlab-have-you-tried-threadpools-yet>`_ for more information.

          A threads pool can be started with:

          .. code-block:: matlabsession

              >> p = parpool("Threads", 4) % 4 workers

          Note that you do not need (and cannot use) a ``parallel.Cluster`` object to initialise a threads pool.

Batch job
*********

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Batch jobs are started with the ``batch`` function. Here we will give you an example job where we query the working directories of each of the threads MATLAB is using.
      Have a look at the `MATLAB documentation <https://www.mathworks.com/help/parallel-computing/run-a-batch-job.html>`_ for more information.

      .. code-block:: matlabsession

          >> c = parcluster;
          >> job = c.batch(@pwd, 1, {}, 'CurrentFolder','.', 'AutoAddClientPath',false);
          >> % request the job status
          >> job.State
          >> % Get the job outputs
          >> job.fetchOutputs{:}
          >> % delete the job
          >> job.delete

      If you are running multiple jobs, you can get an overview of all jobs as follows:

      .. code-block:: matlabsession

          >> jobs = c.Jobs;

      To get for example the output of the second job in this list, you can use the following:

      .. code-block:: matlabsession

          >> job2 = c.Jobs(2);
          >> job2.fetchOutputs{:}

   .. tab-item:: VUB
      :sync: vub

      Batch jobs are started with the ``batch`` function. Here we will give you an example job where we query the working directories of each of the threads MATLAB is using.
      Have a look at the `MATLAB documentation <https://www.mathworks.com/help/parallel-computing/run-a-batch-job.html>`_ for more information.

      .. code-block:: matlabsession

          >> c = parcluster("MyProfile");
          >> job = c.batch(@pwd, 1, {}, 'CurrentFolder','.', 'AutoAddClientPath',false);
          >> % request the job status
          >> job.State
          >> % Get the job outputs
          >> job.fetchOutputs{:}
          >> % delete the job
          >> job.delete

      If you are running multiple jobs, you can get an overview of all jobs as follows:

      .. code-block:: matlabsession

          >> jobs = c.Jobs;

      To get for example the output of the second job in this list, you can use the following:

      .. code-block:: matlabsession

          >> job2 = c.Jobs(2);
          >> job2.fetchOutputs{:}

