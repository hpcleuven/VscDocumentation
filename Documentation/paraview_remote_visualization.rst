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

   $ qsub  -I  -l nodes=1,ppn=20

Given that remote visualization makes sense most for large data sets, 64
GB of RAM is probably the minimum you will need. To use a node with more
memory, add a memory specification, e.g., ``-l mem=120gb``. If this is
not sufficient, you should consider using Cerebro.

Once this interactive session is active, you can optionally navigate to
the directory containing the data to visualize (not shown below), load
the appropriate module, and start the server:

::

   $ module load Paraview/4.1.0-foss-2014a
   $ n_proc=$(cat $PBS_NODEFILE  |  wc  -l)
   $ mpirun  -np $n_proc pvserver  --use-offscreen-rendering \\
                                   --server-port=11111

Note the compute node's name your job is running on, you will need it in
the next step to establish the required SSH tunnel.

Establish an SSH tunnel
~~~~~~~~~~~~~~~~~~~~~~~

To connect the desktop ParaView client with the desktop with the
ParaView server on the compute node, an SSH tunnel has to be established
between your desktop and that compute node. Details for `Windows using
PuTTY <\%22/client/windows/creating-an-ssh-tunnel\%22>`__ and `Linux
using ssh <\%22/client/linux/creating-an-ssh-tunnel\%22>`__ are given in
the appropriate client software sections.

Connect to the remote server using ParaView on your desktop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since ParaView's user interface is identical on all platforms,
connecting from the client side is documented on this page. Note that
this configuration step has to be performed only once if you always use
the same local port.

-  Start ParaView on your Desktop machine;
-  From the 'File' menu, choose 'Connect', this opens the dialog below:

|\\""Choose|

-  Click the 'Add Server' button, the following dialog will appear:

|\\""Configure|

-  Enter a name in the 'Name' field, e.g., 'Thinking'. If you have used
   11111 as the local port to establish the tunnen, just click the
   'Configure' button, otherwise modify the 'Port' field appropriately
   and click 'Configure'. This opens the 'Configure Server' dialog:

|\\""Configure|

-  Set the 'Startup Type' from 'Command' to 'Manual' in the drop-down
   menu, and click 'Save'.
-  In the 'Choose Server' dialog, select the server, i.e., 'Thinking'
   and click the 'Connect' button.

|\\""Choose|

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

`More information on ParaView can be found on its
website <\%22https://www.paraview.org\%22>`__\ ` <\%22https://www.paraview.org/\%22>`__.
A `decent
tutorial <\%22https://www.vtk.org/Wiki/images/8/88/ParaViewTutorial38.pdf\%22>`__
on using Paraview is also available from the VTK public wiki.

"

.. |\\""Choose| image:: \%22/assets/113\%22
.. |\\""Configure| image:: \%22/assets/115\%22
.. |\\""Configure| image:: \%22/assets/117\%22
.. |\\""Choose| image:: \%22/assets/119\%22

