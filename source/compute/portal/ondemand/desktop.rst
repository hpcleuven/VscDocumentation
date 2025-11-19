.. _ood_desktop:

Desktop
-------

The Desktop app will launch a light-weight (Xfce) desktop environment in an
interactive job. Its main purpose is to run graphical software for which there
isn’t (yet) a dedicated app available.

VSC clusters that support the Desktop app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`

For improved graphics performance, we recommend the following workflow:

#. Select the ``Anansi`` cluster (VUB) or the ``interactive`` partition on
   ``wICE`` (KU Leuven / UHasselt) and request some fraction of a GPU.
#. In the desktop environment, open a terminal window and load the module of
   your graphical software.
#. Launch the executable with ``vglrun`` to enable hardware acceleration:

   .. code-block:: bash

      vglrun <executable>

.. tip::

   Once the Desktop app is active, you can grant view-only access to other VSC
   users. In the 'My Interactive Sessions' menu, right-click the 'View Only
   (Share-able Link)' button to copy the link and share it with others. Any VSC
   user with the link can view your Desktop session in real-time, which is
   especially helpful for job troubleshooting and hands-on training.

.. tip::

   In certain browsers (e.g. Google Chrome), the clipboard in the Desktop app
   will have the same content as your device, meaning that you can copy-paste
   text to and from the Desktop as expected. Other browsers, like Firefox,
   do not currently support this and in that case you will need to transfer
   text through the clipboard in the panel on the left hand side.

.. tip::

   The Applications menu on the top left will offer a number of shortcuts.
   Note that some may be missing in case you have changed the value of the
   ``XDG_DATA_HOME`` environment variable in your ``~/.bashrc`` to something
   other than ``$VSC_HOME/.local/share``.
