.. _ood_matlab_app:

MATLAB
------

To launch MATLAB via OnDemand, you need to additionally specify your desired version of the software
from the drop-down menu on the resource form.
Given that our current MATLAB installations automatically detect GPU devices and CUDA libraries,
you may also request GPU(s) as resources, if needed.

Once you launch the session, a remote `noVNC`_ desktop will start on a compute node.
Once the session starts, the selected MATLAB module will be loaded, and eventually the MATLAB GUI
will pop up (after waiting for few seconds).

.. note::

   Only vsc3* users (affiliated with KU Leuven) who are members of the ``lli_matlab`` group
   have rights to use the MATLAB module (hence the MATLAB app). If you are not already member
   of the group, contact the :ref:`KU Leuven supprt team<user support VSC>` for an invitation,
   or :ref:`request joining this group<join groups>` via your VSC account page.

.. _noVNC: https://novnc.com/
