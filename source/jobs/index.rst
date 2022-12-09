################
:fas:`gear` Jobs
################

An HPC cluster is a multi-user system.  This implies that your computations
run on a part of the cluster that will be temporarily reserved for you by
the scheduler.

.. warning::

   Do not run computationally intensive tasks on the login nodes! These
   nodes are shared among all active users, so putting a heavy load on those
   nodes will annoy other users.

Although you can :ref:`work interactively <interactive jobs>` on an HPC system,
most computations are performed in batch mode.

The workflow in the HPC is straightforward:

#. Create a job script
#. Submit it as a job to the scheduler
#. Wait for the computation to run and finish

The following sections cover all aspects related to the preparation, execution
and monitoring of your jobs in the HPC:

.. toctree::
   :maxdepth: 3

   running_jobs
   running_jobs_pbs
   ../software/software_stack
   ../software/software_development

