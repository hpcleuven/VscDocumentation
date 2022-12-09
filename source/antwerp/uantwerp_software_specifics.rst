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
  :ref:`quick PBS-to-Slurm conversion tables <Antwerp Slurm_convert_from_PBS>` which will
  help you convert your PBS job scripts to Slurm.
- :ref:`A list of important differences between Torque and Slurm <Antwerp Slurm_PBS_differences>`


Software installed on the UAntwerp clusters
-------------------------------------------

- The :ref:`Intel toolchain <Antwerp 2017a intel>` is set up in slightly different
  way from other VSC sites since the 2017a version.
- The :ref:`2020a toolchain family <Antwerp software 2020a>` is our base toolchain for Vaughan. 
  Software in older toolchains will not be made available on Vaughan unless experience shows a serious
  performance degradation when compiled in the newer toolchain.
- :ref:`Overview of licensed software at UAntwerp <licensed software UAntwerp>` and instructions on how to
  get access.
- :ref:`Python on the UAntwerp clusters <Antwerp Python>`


Instructions for the special node types
---------------------------------------

- :ref:`Using remote visualisation <remote visualization UAntwerp>`. VNC-based remote visualisation is
  fully supported on the visualisation node and partly supported on the regular login nodes.
- :ref:`Working on the GPU nodes <GPU computing UAntwerp>`
- :ref:`Vector computing on the NEC SX Aurora TSUBASA node <UAntwerp NEC SX Aurora>`
- :ref:`Using the hopper nodes in leibniz <UAntwerp hopper nodes>`
    
