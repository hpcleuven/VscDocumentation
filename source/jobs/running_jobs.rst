Running jobs
============

The basics of the job system
----------------------------

-  `What is a job system and why do we need
   it? <\%22/cluster-doc/running-jobs/job-system-what-why\%22>`__
-  `Specifying resources, output files and
   notifications <\%22/cluster-doc/running-jobs/specifying-requirements\%22>`__
-  `Starting programs in your
   job <\%22/cluster-doc/running-jobs/starting-programs-in-job\%22>`__
-  `Submitting and managing
   jobs <\%22/cluster-doc/running-jobs/submitting-managing-jobs\%22>`__

Common problems
---------------

-  `Why doesn't my job start
   immediately? <\%22/cluster-doc/running-jobs/job-start-failure\%22>`__
   A story about scheduling policies and priorities.
-  `Job failure after a successful
   start <\%22/cluster-doc/running-jobs/job-failure-after-start\%22>`__

Advanced topics
---------------

-  `Credit system
   basics <\%22/cluster-doc/running-jobs/credit-system-basics\%22>`__:
   credits are used on all clusters at the KU Leuven (including the
   Tier-1 system BrENIAC) to control your compute time allocation
-  `Monitoring memory and CPU usage of
   programs <\%22/cluster-doc/running-jobs/monitoring-memory-and-cpu-usage-of-programs\%22>`__,
   which helps to find the right parameters to improve your
   specification of the job requirements
-  `Worker
   framework <\%22/cluster-doc/running-jobs/worker-framework\%22>`__: To
   manage lots of small jobs on a cluster. The cluster scheduler isn't
   meant to deal with tons of small jobs. Those create a lot of
   overhead, so it is better to bundle those jobs in larger sets.
-  The `checkpointing
   framework <\%22/cluster-doc/running-jobs/checkpointing-framework\%22>`__
   can be used to run programs that take longer than the maximum time
   allowed by the queue. It can break a long job in shorter jobs, saving
   the state at the end to automatically start the next job from the
   point where the previous job was interrupted.
-  Running jobs on GPU or Xeon Phi nodes: The procedure is not
   standardised across the VSC, so we refer to the pages for each
   cluster in the \\"\ `Available
   hardware <\%22/infrastructure/hardware\%22>`__\\" section of this web
   site

   -  `KU Leuven GPU and Xeon Phi
      nodes <\%22/infrastructure/hardware/k20x-phi-hardware\%22>`__

"
