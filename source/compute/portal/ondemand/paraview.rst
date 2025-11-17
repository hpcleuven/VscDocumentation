ParaView
--------

`ParaView <https://www.paraview.org/>`_ is an open-source application for interactive, scientific
visualization. It supports various simulation packages, including OpenFOAM.

VSC clusters that support the ParaView app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <Genius hardware>`
       * Tier-2 :ref:`wICE <wICE hardware>`

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Similar to the :ref:`MATLAB app <ood_matlab>`, ParaView also runs inside a `noVNC`_
      desktop as a compute job.

      .. note::

         Currently, using GPUs in ParaView is not supported yet, and just the CPU-only modules are offered.

   .. tab-item:: VUB
      :sync: vub

      ParaView runs in a graphical desktop environment, similar to the
      :ref:`Desktop app <ood_desktop>`.

      .. note::

         Selecting a GPU or fraction of GPU enables improved graphics performance via hardware acceleration.

.. _noVNC: https://novnc.com/
