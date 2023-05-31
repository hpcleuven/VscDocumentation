.. _access_data_transfer:

###############################################
:fas:`right-to-bracket` Login and Data Transfer
###############################################

Before you can really start using one of the clusters, there are several
things you need to do or know:


Login to a cluster
==================

You need to log on to a cluster via an ssh-client to one of the
login nodes. This will give you a command line. The software you'll
need to use on your client system depends on its operating system:

.. toctree::
   :maxdepth: 2

   windows_client
   macos_client
   linux_client

.. note::

   |KUL| When logging in to a KU Leuven cluster, take a look
   at the page on :ref:`Multi Factor Authentication<mfa_leuven>`.

GUI applications on the clusters
================================

Optionally, if you wish to use programs with a graphical user
interface, you'll need an X server on your client system. Again, this
depends on the latter's operating system:

- :ref:`Windows <Windows gui>`
- :ref:`Linux <Linux gui>`
- :ref:`macOS <macOS gui>`

Alternative solutions do also exist that might be more performant or cover more specific use cases. In all cases, it is necessary to install some extra software in your computer to be able to run graphical applications on the VSC clusters. See below for guides on available solutions:

.. warning::

   The following options might not be equally supported across all VSC
   clusters.

.. tab-set::

   .. tab-item:: General

      .. toctree::
         :maxdepth: 1
      
         paraview_remote_visualization
         turbovnc_start_guide

   .. tab-item:: KU Leuven/UHasselt

      .. toctree::
         :maxdepth: 1
      
         nx_start_guide
         ../leuven/services/openondemand

VPN
===

Logging in to the login nodes of your institute's cluster may not work
if your computer is not on your institute's network (e.g., when you work
from home). In those cases you will have to set up a
:doc:`VPN (Virtual Private Networking) <vpn>` connection if your institute
provides this service.

.. toctree::

   vpn
