Desktop
-------

The Desktop app will launch a light-weight (Xfce) desktop environment in an
interactive job. Its main purpose is to run graphical software for which there
isn’t (yet) an app available.

VSC clusters that support the Desktop app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       .. TODO use links

       * Tier-2 Hydra
       * Tier-2 Anansi


For optimal performance, we recommend the following workflow:

#. Launch the app in the ``Anansi`` cluster and request a GPU.
#. In the desktop environment, open a terminal window and load the module of
   your graphical software
#. Launch the executable with ``vglrun`` to enable hardware acceleration:

   .. code-block:: bash

      vglrun <executable>

.. tip::

   Once the Desktop app is running, you can provide view-only access to other
   VSC users. In the 'My Interactive Sessions' menu, right-click the 'View Only
   (Share-able Link)' button to copy the link and share it with others. This
   feature can be very useful for tasks like troubleshooting, pair programming,
   and trainings.
