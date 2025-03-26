ParaView
--------

`ParaView <https://www.paraview.org/>`_ is an open-source application for interactive, scientific
visualization. It supports various simulation packages, including OpenFAOM.

VSC clusters that support the ParaView app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <Genius hardware>`
       * Tier-2 :ref:`wICE <wICE hardware>`

Similar to the :ref:`MATLAB app <ood_matlab>`, ParaView also runs inside a `noVNC`_
desktop as a compute job.

.. note::

   Currently, using GPUs in ParaView is not supported yet, and just the CPU-only modules are offered.

.. _noVNC: https://novnc.com/
