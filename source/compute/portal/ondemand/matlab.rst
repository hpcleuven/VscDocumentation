.. _ood_matlab:

MATLAB
------

Who can use MATLAB
~~~~~~~~~~~~~~~~~~

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Only vsc3* users (affiliated with KU Leuven) who are members of the
      ``lli_matlab`` group have rights to use the MATLAB module (hence the
      MATLAB app). If you are not already member of the group, contact the
      :ref:`KU Leuven supprt team<user support VSC>` for an invitation, or
      :ref:`request joining this group<join groups>` via your VSC account page.

   .. tab-item:: VUB
      :sync: vub

      Only vsc1* users (affiliated with VUB) who are members of the
      ``brusselall`` group have rights to use the MATLAB app.

Before you connect
~~~~~~~~~~~~~~~~~~

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      MATLAB automatically generates several hidden folders in your ``$VSC_HOME``,
      including the folder ``.MathWorks``, which can become quite big over time. To
      prevent ``$VSC_HOME`` from filling up, we recommend creating symlinks to
      redirect this folder to your ``$VSC_DATA`` directory. If this folder already
      exists, you can safely delete it. Execute the following commands to automate the
      process:

      .. code-block:: bash

         rm -rv ~/.MathWorks
         mkdir -pv $VSC_DATA/.MathWorks
         ln -sv $VSC_DATA/.MathWorks ~/.MathWorks

      In case you're trying this on a login node and you previously ran Matlab
      on that login node, you might have to kill any existing MathWorksServiceHost
      processes running there:

      .. code-block:: bash
          
         # look for the PID of the MathWorksServiceHost process
         ps x
         kill <process_id>


   .. tab-item:: VUB
      :sync: vub

      MATLAB automatically generates several hidden folders in your ``$VSC_HOME``,
      including the folder ``.MathWorks``, which can become quite big over time. To
      prevent ``$VSC_HOME`` from filling up, we recommend creating symlinks to
      redirect this folder to your ``$VSC_DATA`` directory. If this folder already
      exists, you can safely delete it. Execute the following commands to automate the
      process:

      .. code-block:: bash

         rm -rv ~/.MathWorks
         mkdir -pv $VSC_DATA/.MathWorks
         ln -sv $VSC_DATA/.MathWorks ~/.MathWorks

Launching MATLAB
~~~~~~~~~~~~~~~~

To launch MATLAB via the OnDemand web portal, select your desired MATLAB version from the
drop-down menu in the resources form.  Given that our current MATLAB
installations automatically detect GPU devices and CUDA libraries, you may also
request GPU(s) as resources, if needed.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Once you launch the session, a remote `noVNC`_ desktop will start on a
      compute node.  Once the session starts, the selected MATLAB module will be
      loaded, and eventually the MATLAB GUI will pop up (after waiting for a few
      seconds).

   .. tab-item:: VUB
      :sync: vub

      Upon launching the session, the selected MATLAB module is loaded and the
      MATLAB Proxy starts, which then launches MATLAB and provides web-based
      access to it (after waiting for a few minutes).

.. _noVNC: https://novnc.com/
