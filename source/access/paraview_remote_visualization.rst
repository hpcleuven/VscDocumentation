.. _Paraview:

Paraview remote visualization
=============================

Prerequisits
------------

You should have ParaView installed on your desktop, and know how to use
it (the latter is outside the scope of this page). **Note**: the client
and server version should match to avoid problems!

Overview
--------

Working with ParaView to remotely visualize data requires the following
steps which will be explained in turn in the subsections below:

#. start ParaView on the cluster;
#. establish an SSH tunnel;
#. connect to the remote server using ParaView on your desktop; and
#. terminating the server session on the compute node.

Start ParaView on the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, start an interactive job on the cluster, e.g.,

::

   $ qsub  -I  -l nodes=1,ppn=36

Given that remote visualization makes sense most for large data sets, you
may have high memory requirements. If the regular nodes do not satisfy your
memory needs, you should consider using the bigmem or superdome partition.

Once this interactive session is active, you can optionally navigate to
the directory containing the data to visualize (not shown below), load
the appropriate module, and start the server:

::

   $ module load Paraview/5.4.1-foss-2018a
   $ n_proc=$(cat $PBS_NODEFILE  |  wc  -l)
   $ mpirun  -np $n_proc pvserver  --use-offscreen-rendering \\
                                   --server-port=11111

Note the compute node's name your job is running on, you will need it in
the next step to establish the required SSH tunnel.

Establish an SSH tunnel
~~~~~~~~~~~~~~~~~~~~~~~

To connect the desktop ParaView client with the desktop with the
ParaView server on the compute node, an SSH tunnel has to be established
between your desktop and that compute node. Details for :ref:`Windows using
PuTTY <text mode access using PuTTY>` and :ref:`Linux using ssh
<OpenSSH access>` are given in the appropriate client software sections.

Connect to the remote server using ParaView on your desktop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since ParaView's user interface is identical on all platforms,
connecting from the client side is documented on this page. Note that
this configuration step has to be performed only once if you always use
the same local port.

#. Start ParaView on your Desktop machine;
#. From the 'File' menu, choose 'Connect', this opens the dialog below:

   |paraview 1 choose server|

#. Click the 'Add Server' button, the following dialog will appear:

   |paraview 2 configure server|

#. Enter a name in the 'Name' field, e.g., 'HPC'. If you have used
   11111 as the local port to establish the tunnel, just click the
   'Configure' button, otherwise modify the 'Port' field appropriately
   and click 'Configure'. This opens the 'Configure Server' dialog:

   |paraview 3 configure server|

#. Set the 'Startup Type' from 'Command' to 'Manual' in the drop-down
   menu, and click 'Save'.
#. In the 'Choose Server' dialog, select the server, i.e., 'HPC'
   and click the 'Connect' button.

   |paraview 4 connect|

You can now work with ParaView as you would when visualizing local
files.

Terminating the server session on the compute node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you've quit ParaView on the desktop the server process will
terminate automatically. However, don't forget to close your session on
the compute node since leaving it open will consume credits.

::

   $ logout

Further information
-------------------

More information on ParaView can be found on the `Paraview website`_
A decent `Paraview tutorial`_ on is also available from the VTK public wiki.

.. |paraview 1 choose server| image:: paraview_remote_visualization/paraview_remote_visualization_01.png
.. |paraview 2 configure server| image:: paraview_remote_visualization/paraview_remote_visualization_02.png
.. |paraview 3 configure server| image:: paraview_remote_visualization/paraview_remote_visualization_03.png
.. |paraview 4 connect| image:: paraview_remote_visualization/paraview_remote_visualization_04.png

