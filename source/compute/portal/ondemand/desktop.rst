.. _ood_desktop:

Desktop
-------

The Desktop app will launch a light-weight (Xfce) desktop environment in an
interactive job. Its main purpose is to run graphical software for which there
isn’t (yet) a dedicated app available.

VSC clusters that support the Desktop app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`


.. tip::

   Once the Desktop app is active, you can grant view-only access to other VSC
   users. In the 'My Interactive Sessions' menu, right-click the 'View Only
   (Share-able Link)' button to copy the link and share it with others. Any VSC
   user with the link can view your Desktop session in real-time, which is
   especially helpful for job troubleshooting and hands-on training.

.. tip::

   In Chromium-based browsers such as Google Chrome and Microsoft Edge,
   the clipboard in the Desktop app will have the same content as your device,
   meaning that you can copy-paste text to and from the Desktop as expected.
   Other browsers, like Firefox and Safari, do not currently support this
   and in that case you will need to transfer text through the clipboard
   in the panel on the left hand side.


.. _ood_desktop_using_applications:

Using applications in the Desktop
=================================

For improved graphics performance, we recommend the following workflow:

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      #. Select the ``interactive`` partition on the ``wICE`` cluster
         and request one GPU instance.
      #. In the desktop environment, open a terminal window and load the
         module of your graphical software.
      #. Launch the executable with ``vglrun`` to enable hardware
         acceleration:

         .. code-block:: bash

            vglrun <executable>

   .. tab-item:: VUB
      :sync: vub

      #. Select the ``Anansi`` cluster and request some fraction of a GPU.
      #. In the desktop environment, open a terminal window and load the
         module of your graphical software.
      #. Launch the executable with ``vglrun`` to enable hardware
         acceleration:

         .. code-block:: bash

            vglrun <executable>

Additional site-specific constraints are listed below.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Mainly due to security concerns, the KU Leuven OOD Desktop app is run
      within a minimalistic container. As a result some functionality is
      deliberately missing:

      - Slurm-related commands such as ``squeue``, ``sbatch``, ``srun``, ...
        and ``sam-balance``, ``sam-statement``, ... are unavailable.

      - No browser is provided within the Desktop app (see alternatives
        below).

      Some applications are currently unavailable but may be enabled in the
      future (such as ``myquota``, ``apptainer`` and archive managers such as
      ``xarchiver``).

      |

      **Using your local browser where needed**

      Certain applications expect that you have a browser at your disposal.

      The more common case is where the application starts a server to which
      you are expected to connect with a browser (examples: JupyterLab,
      Streamlit, CryoSparc). To use your local browser for this purpose,
      you only need to set up a suitable SSH tunnel with for example
      :ref:`OpenSSH <tunnel OpenSSH>` or :ref:`PuTTY <putty ssh tunnel>`.

      Some applications may produce static HTML files instead (example:
      LinaroForge). Other than simply transferring these files to your local
      device, you can also view these by starting a local HTTP server and
      applying the SSH tunnel approach described in the previous paragraph.
      An easy way to start such a server is the Python ``http`` module
      (added in Python 3.5):

      ::

          /usr/bin/python3 -m http.server -b localhost <port>

      |

      **Applications menu**

      The Applications menu on the top left will offer a number of shortcuts.
      Note that some may be missing in case you have changed the value of the
      ``XDG_DATA_HOME`` environment variable in your ``~/.bashrc`` to
      something other than ``$VSC_HOME/.local/share``.

   .. tab-item:: VUB
      :sync: vub

      (N/A)


.. _ood_desktop_tips_for_nx_users:

Tips for NoMachine users
========================

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
        :columns: 12

        If you have been using the :ref:`NoMachine <NX start guide>` desktop,
        you may need to do a few things differently when switching to the
        OnDemand Desktop:

        - For browser-related applications, see :ref:`the section above
          <ood_desktop_using_applications>`. Note that in certain cases this
          means the :ref:`Interactive Shell <ood_interactive_shell>` app may
          suffice and you may not need the Desktop app.

        - If your graphical application is available as a dedicated Interactive
          App we recommend using that instead of the Desktop app (examples:
          :ref:`MATLAB <ood_matlab>`, :ref:`ParaView <ood_paraview>`,
          :ref:`Fluent <ood_fluent>`).

        - The standard text editor is ``Mousepad`` (not ``Gedit``).

        - As an image viewer you may use the ``display`` command provided by
          the ``ImageMagick`` modules, but we would rather recommend the viewer
          that is integrated in the :ref:`File Explorer <ood_files>`.
