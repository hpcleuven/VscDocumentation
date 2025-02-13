VS Code Tunnel
--------------

The VS Code Tunnel app provides tunnel access to an interactive job from your
*locally installed* VS Code application. This is handy if you already have many
extensions installed locally, or if you want to easily switch between local and
remote work within a single application. The downside is the number of steps
involved to connect (although mostly point-and-click).

For more information on VS Code, check out the official `VSCode guidelines
<https://code.visualstudio.com/docs>`_.

VSC clusters that support the VS Code Tunnel app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       .. TODO use links

       * Tier-2 Hydra
       * Tier-2 Anansi

Before you connect
~~~~~~~~~~~~~~~~~~

VS Code automatically creates folders ``.vscode`` and ``.vscode-server`` in your
``$VSC_HOME``, which tend to become rather big quickly, especially if you use a
lot of extensions.  To avoid filling up your ``$VSC_HOME``, we recommend
replacing those folders with symlinks to your ``$VSC_DATA``:

.. code-block:: bash

   mkdir $VSC_DATA/.vscode $VSC_DATA/.vscode-server
   ln -s $VSC_DATA/.vscode ~/.vscode
   ln -s $VSC_DATA/.vscode-server ~/.vscode-server

If you already have folders ``~/.vscode`` and ``~/.vscode-server``, you can move
them to ``$VSC_DATA`` before symlinking.

How to connect
~~~~~~~~~~~~~~

#. In the web portal, under the 'Interactive Apps' menu, choose 'VS Code
   Tunnel', select the resources and launch your job by clicking the ``Launch``
   button. Once your job has started, connect by clicking the ``Connect``
   button.

#. A first browser tab or window opens, showing a terminal session, and you are
   asked 'How would you like to log in to Visual Studio Code?'. Select 'Microsoft
   Account' using the arrow keys on your keyboard and click Enter.

#. An URL and an authentication code are shown, which you will need to sign in
   to VS Code. Copy the code by holding the Shift key while selecting it, and
   click the URL to open it.

#. A second browser tab or window opens. Enter the copied code, select your
   Microsoft account, and click the ``continue`` button. The tunnel is now ready
   to be used.

#. Launch VS Code on your local computer, and click the blue button in the
   bottom left of the window that says 'Open a Remote Window'.

#. In the command palette, you are asked to 'Select an option to open a Remote
   Window'. Select 'Tunnel', which will automatically install the 'Remote -
   Tunnels' extension. If the extension was already installed, click 'Connect to
   Tunnel..'.

#. Again in the command palette, you are asked 'What type of account did you use
   to start this tunnel?'. Select 'Microsoft Account'.

#. In the pop-up that says "The extension 'Remote - Tunnels' wants to sign in
   using Microsoft", click ``Allow``.

#. A third browser tab or window opens. Again, select your Microsoft account.

#. Again in the command palette, select the tunnel with the format
   ``vsc-<VSC-id>-<cluster>``, where ``<VSC-id>`` is your VSC-id, and
   ``<cluster>`` is the cluster that you selected in the resources form.

#. That’s it, you are now connected to your VS Code Tunnel session!

.. note::

   - In case of authentication problems, it may be necessary to tick the
     'Cleanup previous VS Code Tunnel login data' checkbox in the resources
     form.
   - To close the remote connection, click again the blue button in the bottom
     left, and select 'Close Remote Connection' in the command palette.

Python modules and environments
...............................

.. include:: vscode-python-modules-brussel.rst



