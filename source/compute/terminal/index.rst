.. _terminal interface:

##########################################
:fas:`terminal` Access: Terminal Interface
##########################################

.. toctree::
   :hidden:

   windows_client
   macos_client
   linux_client

We provide multiple methods to access the VSC clusters and use their
computational resources. Not all options may be equally supported across all
clusters though. In case of doubt, please contact the corresponding
:ref:`support team <tech support VSC>`.

.. _terminal ssh:

Secure Shell Connection
=======================

You can open a terminal with a command prompt on any VSC cluster by logging in
via the `Secure Shell`_ (SSH) protocol to the corresponding login node of that
cluster. To this end, you will need to install and configure some SSH client
software in your computer.

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

   |KUL| Logging in to a KU Leuven cluster with SSH requires
   :ref:`Multi Factor Authentication<mfa_leuven>`.

.. _terminal linux system:

Linux System
============

All VSC clusters run the `Linux kernel`_ and a `GNU`_ operating system,
so-called GNU/Linux or often just referred as Linux. Specifically, all our
HPC clusters currently run some flavor of `Red Hat Enterprise Linux`_, which
means that all clusters share a common toolbox that can be used across VSC
sites.

Once you connect to the terminal interface of a VSC cluster, you will be
presented by a command line prompt that accepts Linux commands. It is hence
necessary to have some knowledge on how to use the terminal in Linux to be able
to perform any task in the system. The terminal might look daunting at first,
as you have to known what commands to type to carry out even the simplest
operations, like making folders and moving files. But making the effort to
master the terminal is a guaranteed good investment of your time, as it is a
very powerful tool that allows to extensively automate your workflows.

The following sections provide an introduction to the Linux terminal.

.. toctree::
   :maxdepth: 2

   basic_linux
   shell_scripts

.. _terminal gui apps:

Graphical applications on the terminal
======================================

.. include:: recommend_web_portal.rst

Launching programs with a graphical user interface (GUI) through the terminal
interface of the cluster requires additional support on your SSH client. You
need some software component that can encrypt and transfer through the network
the graphical data of your application running on the cluster and display it on
your screen.

.. _terminal x11:

X Server
--------

Most SSH clients provide integration with a so called `X Server`_. This is a
client/server solution that uses the X Window System protocol to display
graphics on local or remote screens.

.. toctree::
   :hidden:

   Xming X Server <windows_xming>
   NoMachine NX <nx_start_guide>

.. tab-set::
   :sync-group: operating-system

   .. tab-item:: Windows
      :sync: win

      Displaying graphical applications running on the Linux system of the VSC
      cluster on your Windows system can be done by setting up an X Server on
      your computer:

      * |Recommended| :ref:`MobaXterm <terminal mobaxterm>` provides an X
        Server, :ref:`enable X11-Forwarding <mobaxterm advanced options>` on
        your SSH connections to use graphical applications with it.

      * :ref:`PuTTY <terminal putty>` provides an X Server, :ref:`enable
        X11-Forwarding <putty x11 forwarding>` to use graphical applications on
        all your SSH connections.

      * Install a standalone X server such as :ref:`Xming <Xming>`.

   .. tab-item:: macOS
      :sync: mac

      You can display remote graphical applications on your Mac with an X
      server. The recommended options is `XQuartz <https://www.xquartz.org/>`__
      which is an X Window System implementation freely available and supported
      by Apple.

      Once XQuartz is installed and running on your Mac, you can simply open a
      terminal window and connect to a VSC cluster with
      :ref:`SSH enabling support for graphics <openssh x11 forwarding>`.

   .. tab-item:: Linux
      :sync: lin

      The `X server`_ is available on all popular Linux distributions, and most
      often installed by default as well. You just need to use the appropriate
      options with the ``ssh`` command to :ref:`connect with support for
      graphics <openssh x11 forwarding>`.

.. _terminal remote desktop:

Remote Desktop Environment
--------------------------

You can launch a full-fledge remote desktop environment running on a remote VSC
cluster with the `VNC`_ system. This solution generates a video stream of the
remote graphical display, encrypts it and sends it over the SSH connection to
your computer for visualization.

In this case all graphical processing occurs on the remove VSC cluster and your
computer is only used for visualization and input. This can be useful in
scenarios where you need heavy processing of graphics with the GPUs of the
cluster.

Different options exist that provide a VNC-like solution. The available options
depend on the operating system in your computer and the VSC cluster that you
want to use:

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      On the KUL clusters, users can use NX :ref:`NX start guide`.

   .. tab-item:: UAntwerpen
      :sync: ua

      On the UAntwerp clusters, TurboVNC is supported on all regular login
      nodes (without OpenGL support) and on the visualization node of Leibniz
      (with OpenGL support through VirtualGL).

      See the page :ref:`Remote visualization UAntwerp` for instructions.

   .. tab-item:: UGent
      :sync: ug

      VNC is supported through the :ref:`hortense_web_portal` interface.

   .. tab-item:: VUB
      :sync: vub

      On the VUB clusters, TigerVNC is supported on all nodes. See the
      documentation on `remote desktop sharing <https://hpc.vub.be/docs/software/graphical_apps/#remote-desktop-sharing>`_
      for instructions.

Applications supporting SSH
---------------------------

Some graphical applications provide their own functionality to run on
remote servers through SSH. This can be used to run the GUI of such
applications locally while the heavy lifting of the computation is done on a
VSC cluster.

* :ref:`Eclipse for remote development <Eclipse as remote editor>`

VPN
===

Some institutes may have security policies forbidding the access to login nodes
of your institute's cluster from outside of the institute's network (*e.g.*
when you work from home) or from abroad. In such case, you will need to set up
a :doc:`VPN (Virtual Private Networking) <vpn>` connection to your institute's
network (if your institute provides this service) to be able to login to those
VSC clusters.

.. toctree::

   vpn

