.. _putty ssh tunnel:

SSH tunnel with PuTTY
=====================

Prerequisites
-------------

:ref:`PuTTY <terminal putty>` must be installed on your computer, and you
should be able to connect via SSH to your VSC cluster of choice.

Background
----------

Because of one or more firewalls between your desktop and the HPC
clusters, it is generally impossible to communicate directly with a
process on the cluster from your desktop except when the network
managers have given you explicit permission (which for security reasons
is not often done). One way to work around this limitation is SSH
tunneling.

There are several cases where this is usefull:

* Running X applications on the cluster: The X program cannot directly
  communicate with the X server on your local system. In this case, the
  tunneling is easy to set up as PuTTY will do it for you if you select
  the right options on the X11 settings page as explained on the
  :ref:`page about text-mode access using PuTTY <terminal putty>`.

* Running a server application on the cluster that a client on the
  desktop connects to. One example of this scenario is :ref:`ParaView in
  remote visualization mode <Paraview>`,
  with the interactive client on the desktop and the data processing
  and image rendering on the cluster. How to set up the tunnel for that
  scenario is also :ref:`explained on that page <Paraview>`.

* Running clients on the cluster and a server on your desktop. In this
  case, the source port is a port on the cluster and the destination
  port is on the desktop.

Procedure: Tunnel from a local client to a server on the cluster
------------------------------------------------------------------

#. Log in on the login node of your VSC cluster as usual

#. Start a job on the compute node running the server, take note of the name of
   the compute node (*e.g.* ``r1i3n5``), as well as the port the server is
   listening on (*e.g.* 44444)

#. Open PuTTY on your computer to set up the tunnel

#. Right-click in PuTTY's title bar, and select "Change Settings..."

#. In the "Category" pane, expand "Connection" -> "SSH", and select
   'Tunnels' as show below:

   .. figure:: putty_ssh_tunnel/putty_tunnel_config.png

#. In the "Source port" field, enter the local port to use (*e.g.*
   11111)

#. In the "Destination" field, enter ``<hostname>:<server-port>`` (*e.g.*
   ``r1i3n5:44444`` as in the example above)

#. Click the "Add" button
#. Click the "Apply" button

The tunnel is now ready to use.

