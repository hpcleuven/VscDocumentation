.. _ood_interactive_apps:

Launching interactive apps
==========================

The 'Interactive Apps' menu shows a range of different apps that provide a GUI.
When you launch an interactive app, Open OnDemand first submits an interactive
job to the cluster in your account. Once the interactive job starts, the app is
automatically launched inside the interactive session.

To launch an interactive app, you need to fill out the resources form.
Most of the options in the resources form are shared across all apps and are
explained below. The app-specific options will be detailed in their respective
sections.  See also the section on :ref:`choosing your resources
<choosing_your_resources>` for resources recommendations. Beware that launching
an app will cause your interactive job to end up in a regular queue, so
requesting a large amount of resources might result in a long queue time.

Once you've specified all your resources, press the ``Launch`` button and your
job will be queued.

.. _shared_resources:

.. list-table:: Shared resources (part 1)
   :header-rows: 1
   :widths: 20 80

   * - Resource
     - Description
   * - Cluster
     - Select one of the supported clusters.
   * - Partition
     - Select a supported partition in the selected cluster.
   * - Number of hours
     - Select the time limit (in hours) for your interactive app session.
   * - Number of nodes
     - Select the number of nodes. Only 1 node should be used in most cases,
       unless you are sure the app *can and will* use more than 1 node
       effectively.
   * - Number of cores
     - Select the number of cores per node.
   * - Number of GPUs
     - Select the number of GPUs per node. Check the :ref:`hardware` section for
       the device type that corresponds to the selected cluster/partition. Only
       request a GPU if you are sure the app *can and will* use the GPU
       effectively.
   * - Pre-run scriptlet
     - Add optional shell commands to your job before launching the app.
       For example, loading extra modules that you need within the app, sourcing a
       specific script, or defining specific environment variables.
   * - Working Directory
     - Specify the working directory for your app, or use the handy
       ``Select Path`` button below the text field to select it from a
       file browser.

.. warning::

   Be careful when using the Pre-run scriptlet, because you will be modifying
   the behavior of your session.

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      .. list-table:: Shared resources (part 2)
         :header-rows: 1
         :widths: 20 80

         * - Resource
           - Description
         * - Account
           - Select the credit account you want to deduct the credits from.  The
             accounts associated with your VSC-id will be displayed in a
             drop-down menu.
         * - Required memory per core in megabytes
           - This defaults to 3400 MB.
         * - Reservation
           - If you are part of a reservation, you can also use these nodes with
             Open Ondemand by specifying your reservation name here.
         * - Screen resolution
           - For apps which run inside a remote `noVNC`_ desktop (e.g. MATLAB,
             ParaView, etc), one may choose a resolution between 'FullHD', '2K'
             or '4K'.  After launching the app, one may still change the
             compression level and the image quality of the transferred noVNC
             frames.  E.g. opting for the lowest compression level and highest
             image quality can give you a crisp noVNC desktop.
         * - View Only (Share-able Link)
           - For `noVNC`_ apps, you can provide a view-only access to other VSC
             users.  For that, click on the 'View Only (Share-able Link)' button
             to copy the URL into your clipboard, and be able to share it with
             others.

      .. note::

         The acquired GPU will be the same as the type specified in the partition
         (e.g. a NVIDIA H100 for ``gpu_h100`` on wICE).  For wICE, you can also
         request a GPU from the ``interactive`` partition.
         One GPU here is a virtual GPU slice of the available A100 GPUs.
         One GPU slice is the same as 1/7th of CUDA cores and memory of an A100 GPU.
         The interactive partition only allows you to request max 1 GPU (slice) though.

      .. warning::

         As the end-user, you are responsible for all consequences of sharing
         your application with other VSC users.  So, think twice before
         sharing your sensitive data, sources and information by all means.


   .. tab-item:: VUB

      .. list-table:: Shared resources (part 2)
         :header-rows: 1
         :widths: 20 80

         * - Resource
           - Description
         * - Working Directory
           - Specify the working directory for your app, or use the handy
             ``Select Path`` button below the text field to select it from a
             file browser.


.. _choosing_your_resources:

Choosing your resources
-----------------------

Choosing the correct resources for your interactive session is mostly the same
as selecting them when launching regular batch jobs. For this reason, we
strongly recommend consulting the documentation on how to effectively choose
your job resources:

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      Documentation on resources is available for both :ref:`Genius
      <running_jobs_on_genius>` and :ref:`wICE <running jobs on wice>`.

      If requesting a GPU, it will be the same as the type specified in the
      partition (e.g. a NVIDIA H100 for ``gpu_h100`` on wICE).  For wICE, you
      can also request a GPU from the ``interactive`` partition.  One GPU here
      is a virtual GPU slice of the available A100 GPUs.  One GPU slice is the
      same as 1/7th of CUDA cores and memory of an A100 GPU.  The interactive
      partition only allows you to request max 1 GPU (slice) though.

      In most cases we recommend using the ``interactive`` partition on wICE for
      the interactive apps.  This partition is meant for lighter work, like code
      development, testing, debugging, visualisations, pre- and post-processing.
      Using this partition is also free, mainly to encourage you to request
      these resources for such work, instead of using any of the other
      partitions. There are however some limitations on the amount of resources
      you can request here:

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

Once you have passed the testing phase, and you want to start conducting
experiments, we recommend that you make the switch to batch jobs instead, as
they will not require your presence to start your code.

.. _noVNC: https://novnc.com/
