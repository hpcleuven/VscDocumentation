.. _ood_matlab:

MATLAB
------

Who can use MATLAB
~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      Only vsc3* users (affiliated with KU Leuven) who are members of the
      ``lli_matlab`` group have rights to use the MATLAB module (hence the
      MATLAB app). If you are not already member of the group, contact the
      :ref:`KU Leuven supprt team<user support VSC>` for an invitation, or
      :ref:`request joining this group<join groups>` via your VSC account page.

   .. tab-item:: VUB

      Only vsc1* users (affiliated with VUB) who are members of the
      ``brusselall`` group have rights to use the MATLAB module (hence the
      MATLAB app). For more info, please contact the VUB HPC team at hpc@vub.be.

Launching the MATLAB app
~~~~~~~~~~~~~~~~~~~~~~~~

To launch MATLAB via OnDemand, select your desired MATLAB version from the
drop-down menu on the resource form.  Given that our current MATLAB
installations automatically detect GPU devices and CUDA libraries, you may also
request GPU(s) as resources, if needed.

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      Once you launch the session, a remote `noVNC`_ desktop will start on a
      compute node.  Once the session starts, the selected MATLAB module will be
      loaded, and eventually the MATLAB GUI will pop up (after waiting for a few
      seconds).

   .. tab-item:: VUB

      Upon launching the session, the selected MATLAB module is loaded and the
      MATLAB Proxy starts, which then launches MATLAB and provides web-based
      access to it (after waiting for a few minutes).

.. _noVNC: https://novnc.com/
