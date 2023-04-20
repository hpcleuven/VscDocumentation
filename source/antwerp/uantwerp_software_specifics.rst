.. _UAntwerp software specifics:

UAntwerp-specific software instructions
=======================================

Slurm Workload Manager
----------------------

Both Leibniz and Vaughan run Slurm Workload Manager as the resource manager and scheduler.
The Slurm documentation is work-in-progress
as we are still refining the setup.

- An overview of Slurm concepts and commands:
    - The :ref:`running jobs` page contains the 
      minimum that we expect a user to know.
    - The :ref:`job advanced` page contains
      some more advanced commands and additional ways to request resources. Check those
      if you feel the basic information is not enough.
- You can also have a look at our 
  :ref:`quick PBS-to-Slurm conversion tables <Slurm_convert_from_PBS>` which will
  help you convert your PBS job scripts to Slurm.
- :ref:`A list of important differences between Torque and Slurm <Slurm_PBS_differences>`


Software installed on the UAntwerp clusters
-------------------------------------------

- :ref:`Python on the UAntwerp clusters <Antwerp Python>`

.. toctree::
   :maxdepth: 1

   the_2017a_toolchains_on_the_uantwerp_clusters
   uantwerp_software_2020a
   licensed_software_on_the_uantwerp_clusters

Instructions for the special node types
---------------------------------------

- :ref:`Vector computing on the NEC SX Aurora TSUBASA node <UAntwerp NEC SX Aurora>`
- :ref:`Using the hopper nodes in leibniz <Hopper hardware>`
    
.. toctree::
   :maxdepth: 1

   remote_visualization_uantwerp
   gpu_computing_uantwerp
