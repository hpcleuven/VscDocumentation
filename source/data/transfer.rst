.. _data transfer:

###############################
:fas:`left-right` Data Transfer
###############################

Before you can do some work, you'll have to transfer any files or data sets
that you need for your research from your personal or department computer to
the :ref:`storage of VSC clusters <data location>`. Then, once you get your
results, you might want to transfer some files back. 

.. important::

   |Recommended| The preferred way to transfer data to/from the VSC clusters is
   the :ref:`globus platform`.

.. _data transfer external comp:

Data transfer on external computers
===================================

For those systems not supporting :ref:`Globus <globus platform>`, we provide
instructions on alternative transfer methods that can be used to transfer data
between your computer and VSC clusters:

.. toctree::
   :hidden:

   transfer/windows
   transfer/mac
   transfer/linux

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: :fab:`windows` Windows
       :columns: 12 4 4 4

       * :ref:`FileZilla <FileZilla>`
       * :ref:`WinSCP <WinSCP transfer>`

    .. grid-item-card:: :fab:`apple` macOS
       :columns: 12 4 4 4

       * :ref:`Cyberduck <Cyberduck data transfer>`
       * :ref:`FileZilla <FileZilla data transfer mac>`
       * :ref:`Terminal <terminal data transfer mac>`

    .. grid-item-card:: :fab:`linux` Linux
       :columns: 12 4 4 4

       * :ref:`scp and sftp <scp and sftp>`

.. _data transfer net drives:

Data transfer on network drives
===============================

Some VSC clusters provide specific integration with network storage platforms
available in their home institution.

.. toctree::
   :hidden:

   transfer/network_drives/kuleuven
   transfer/network_drives/vub_onedrive

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      On clusters hosted at KU Leuven it is possible to transfer data to
      and from KU Leuven network drives to which you may have access.

      Follow the instructions in: :ref:`KU Leuven network drives`

   .. tab-item:: UAntwerpen
      :sync: ua

      *No specific integration*

   .. tab-item:: UGent
      :sync: ug

      *No specific integration*

   .. tab-item:: VUB
      :sync: vub

      You can directly copy files between the :ref:`Hydra cluster` and your
      OneDrive from VUB.

      Follow the instructions in: :ref:`vub onedrive`

