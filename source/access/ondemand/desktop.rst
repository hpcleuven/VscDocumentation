Desktop
-------

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      (not available at this time)

   .. tab-item:: VUB

      The Desktop app will launch a light-weight (Xfce) desktop environment in
      an interactive job. Its main purpose is to run graphical software for
      which there isn’t (yet) an app available.

      For optimal performance, we recommend the following workflow:

      #. Launch the app in the ``Anansi`` cluster and request a GPU.
      #. In the desktop environment, open a terminal window and load the module of your graphical software
      #. Launch the executable with ``vglrun`` to enable hardware acceleration:

         .. code-block:: bash

            vglrun <executable>

