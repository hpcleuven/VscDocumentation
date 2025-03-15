.. _access methods:

#################################################
:fas:`right-to-bracket` Access VSC Infrastructure
#################################################

.. toctree::
   :hidden:

   windows_client
   macos_client
   linux_client
   ondemand/index

We provide multiple methods to access the VSC clusters and use their
computational resources. Not all options may be equally supported across all
clusters though. In case of doubt, please contact the corresponding
:ref:`support team <tech support VSC>`.

Terminal interface
==================

You can access the command line on any VSC cluster by logging in via SSH to the
corresponding login node. To this end, you will need to install and configure
some SSH client software in your computer.

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: :fab:`windows` Windows
       :columns: 12 4 4 4
       :link: windows_client
       :link-type: doc

       SSH client setup

    .. grid-item-card:: :fab:`apple` macOS
       :columns: 12 4 4 4
       :link: macos_client
       :link-type: doc

       SSH client setup

    .. grid-item-card:: :fab:`linux` Linux
       :columns: 12 4 4 4
       :link: linux_client
       :link-type: doc

       SSH client setup

.. note::

   |KUL| When logging in to a KU Leuven cluster, take a look
   at the page on :ref:`Multi Factor Authentication<mfa_leuven>`.

GUI applications on the clusters
================================

If you wish to use programs with a graphical user interface (GUI), you'll need
an X server on your client system. The available options depend on the
operating system in your computer:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: :fab:`windows` Windows
       :columns: 12 4 4 4
       :link: windows_gui
       :link-type: ref

       GUI access setup

    .. grid-item-card:: :fab:`apple` macOS
       :columns: 12 4 4 4
       :link: macos_gui
       :link-type: ref

       GUI access setup

    .. grid-item-card:: :fab:`linux` Linux
       :columns: 12 4 4 4
       :link: linux_gui
       :link-type: ref

       GUI access setup

Alternative solutions do also exist that might be more performant or cover more
specific use cases. In all cases, it is necessary to install some extra
software in your computer to be able to run graphical applications on the VSC
clusters. See below for guides on available solutions:

.. warning::

   The following options might not be equally supported across all VSC
   clusters.

.. tab-set::

   .. tab-item:: General

      .. toctree::
         :maxdepth: 1
      
         paraview_remote_visualization

   .. tab-item:: KU Leuven/UHasselt

      .. toctree::
         :maxdepth: 1
      
         nx_start_guide


VPN
===

Logging in to the login nodes of your institute's cluster may not work
if your computer is not on your institute's network (e.g., when you work
from home). In those cases you will have to set up a
:doc:`VPN (Virtual Private Networking) <vpn>` connection if your institute
provides this service.

.. toctree::

   vpn
