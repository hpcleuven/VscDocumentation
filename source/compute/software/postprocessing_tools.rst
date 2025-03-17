#####################
Post-processing tools
#####################

*This section is still rather empty. It will be expanded over time.*

Visualization software
======================

.. _Paraview:

Paraview
--------

`ParaView <https://www.paraview.org/>`__ is a free
visualization package. It can be used in three modes:

* *Installed on your desktop*: you have to transfer your data to your desktop
  system

* *Interactive process on the cluster*: this option is available only for
  :ref:`NoMachine NX users <NX start guide>` (go to Applications menu -> HPC ->
  Visualisation -> Paraview).

* *In client-server mode*: The interactive application of ParaView runs on your
  desktop, while its server component runs on the cluster. The server reads the
  data, renders the images (no GPU required as ParaView also contains a
  software OpenGL renderer) and sends the rendered images to the Paraview
  application on your desktop. Setting up ParaView for this scenario is
  explained in the following chapters:

  .. toctree::
     :maxdepth: 2
  
     paraview_remote_visualization
