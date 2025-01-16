.. _interactive-apps:

Interactive apps
================

The 'Interactive Apps' menu shows a range of different apps that provide a GUI.
When you launch an interactive app, Open Ondemand uses your account to submit an
interactive job to the cluster, in which the app will be running.

To launch any of the interactive apps, you need to fill out the resources form.
Most of the options in the resource forms are similar across all apps, but some
apps require additional input from the user.  These will be explained in the
app-specific sections.  See also the section on :ref:`choosing your resources
<choosing_your_resources>` for more details.  Beware that by launching any app
your interactive job will end up in a regular queue, so requesting a large
amount of resources might result in a long queue time.

Once you've specified all your resources, press the ``Launch`` button and your
job will be queued.

*Resources common to all institutions*:

- Cluster: allows choosing between one of the supported clusters.
- Partition: you can choose any of the existing partitions on both clusters.
  The partition names depend on your choice of cluster.

  |KUL| We recommend using the ``interactive`` partition for most interactive work.

- Numbers of hours: the time limit of your interactive app (min 1h).
- Number of nodes: the amount of nodes (default = 1).
- Number of cores: the amount of cores per node (default = 1).
- Number of GPUs. Depending on the GPU partition you have requested, you get a different device type.
  The default is 0.
- Pre-run scriptlet: this allows you to add bash commands to your job before launching the app.
  This can be used for example for loading extra modules that you need within the app, sourcing a specific script
  or defining specific environment variable(s).

  .. warning::

     Be careful when using this feature, because you will be modifying the behavior of your session.

*Resources specific for each institution*:

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      - Account: the credit account you want to deduct the credits from.
        The accounts associated with your VSC number will be displayed in a dropdown menu.
      - Required memory per core in megabytes. This defaults to 3400 MB.
      - The acquired GPU will be the same as the type specified in the partition (e.g. a NVidia H100 for ``gpu_h100`` on wICE).
        For wICE, you can also request a GPU from the ``interactive`` partition.
        One GPU here is a virtual GPU slice of the available A100 GPUs.
        One GPU slice is the same as 1/7th of CUDA cores and memory of an A100 GPU.
        The interactive partition only allows you to request max 1 GPU (slice) though.
      - Reservation: if you are part of a reservation, you can also use these nodes with Open Ondemand by specifying your reservation name here.
      - Screen resolution: for apps which run inside a remote `noVNC`_ desktop (e.g. MATLAB, ParaView, etc), one
        may choose a resolution between 'FullHD', '2K' or '4K'.
        After launching the app, one may still change the compression level and the image quality of the
        transferred noVNC frames.
        E.g. opting for the lowest compression level and highest image quality can give you a crisp noVNC desktop.
      - View Only (Share-able Link): for `noVNC`_ apps, you can provide a view-only access to other VSC users.
        For that, click on the 'View Only (Share-able Link)' button to copy the URL into your clipboard,
        and be able to share it with others.

        .. warning::

           As the end-user, you are responsible for all consequences of sharing your application with other
           VSC users.
           So, think twice before sharing your sensitive data, sources and information by all means.

   .. tab-item:: VUB

      (no specific resources)


.. _choosing_your_resources:

Choosing your resources
-----------------------

Choosing the correct resources for your interactive session is mostly the same
as selecting them when launching regular batch jobs. For this reason, we
strongly recommend you to have a look at how to specify your resources.

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      Documentation on resources is available for both :ref:`Genius
      <running_jobs_on_genius>` and :ref:`wICE <running jobs on wice>`.

      As mentioned above, in most cases we recommend using the 'interactive'
      partition on wICE for the interactive apps.  This partition is meant for
      lighter work, like code development, testing, debugging, visualisations,
      pre- and post-processing.  Using this partition is also free, mainly to
      encourage you to request these resources for such work, instead of using
      any of the other partitions. There are however some limitations on the
      amount of resources you can request here:

      - Max 1 node
      - Max 8 cores
      - Max 1 virtual GPU slice
      - Max 16h of walltime

      This is put in place to ensure that these resources are kept for their
      original purpose, namely the interactive work.

      If for some reason some of these limitations are too strict for you, or
      you need resources that are not available on the interactive nodes (e.g. a
      full GPU, big memory nodes), you can always request nodes from another
      partition.  Remember however that these interactive apps are not meant for
      running full jobs.  If you indeed need multiple nodes or full GPUs to test
      your code/program, go ahead and request the resources for your interactive
      app from a more suitable partition.

   .. tab-item:: VUB

      Documentation on resources is available in the section on `job submission
      <https://hpc.vub.be/docs/job-submission/>`_.

      For light-weight (testing) work, we recommend using the ``Anansi``
      cluster, which also contains 4 shared GeForce GTX 1080 Ti GPUs for
      improved rendering performance.

In the case that you have passed the testing phase, and you want to start
conducting experiments, we recommend that you make the switch to batch jobs
instead, as they will not require your presence to start your code.

.. _noVNC: https://novnc.com/
