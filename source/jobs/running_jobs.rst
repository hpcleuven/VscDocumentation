Running jobs
============

The basics of the job system
----------------------------

.. toctree::

   What is a job system and why do we need it? <the_job_system_what_and_why>
   Specifying resources, output files and notifications <specifying_resources_output_files_and_notifications>
   Starting programs in your job <starting_programs_in_a_job>
   Submitting and managing jobs <submitting_and_managing_jobs_with_torque_and_moab>


Common problems
---------------

.. toctree::

   Why doesn't my job start immediately? A story about scheduling policies and priorities. <why_doesn_t_my_job_start>
   Job failure after a successful start <what_if_jobs_fail_after_starting_successfully>


Advanced topics
---------------

-  `Credit system basics <credit_system_basics>`__:
   credits are used on all clusters at the KU Leuven (including the
   Tier-1 system BrENIAC) to control your compute time allocation
-  `Monitoring memory and CPU usage of
   programs <monitoring_memory_and_cpu_usage_of_programs>`__,
   which helps to find the right parameters to improve your
   specification of the job requirements
-  `Worker framework <worker_framework>`__: To
   manage lots of small jobs on a cluster. The cluster scheduler isn't
   meant to deal with tons of small jobs. Those create a lot of
   overhead, so it is better to bundle those jobs in larger sets.
-  The `checkpointing
   framework <checkpointing_framework>`__
   can be used to run programs that take longer than the maximum time
   allowed by the queue. It can break a long job in shorter jobs, saving
   the state at the end to automatically start the next job from the
   point where the previous job was interrupted.
-  Running jobs on GPU or Xeon Phi nodes: The procedure is not
   standardised across the VSC, so we refer to the pages for each
   cluster

   -  `KU Leuven GPU and Xeon Phi
      nodes <../leuven/nvidia_k20x_intel_xeon_phi_cluster>`__

"
