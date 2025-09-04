VS Code Tunnel
==============

The VS Code Tunnel app provides tunnel access to an interactive job from your
*locally installed* VS Code application. This is handy if you already have many
extensions installed locally, or if you want to easily switch between local and
remote work within a single application. The downside is the number of steps
involved to connect (although mostly point-and-click and authentication).

VSC clusters that support the VS Code Tunnel app:

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      .. grid:: 3
         :gutter: 4

         .. grid-item-card:: |KUL| |UH|
            :columns: 12 4 4 4

            * Tier-2 :ref:`Genius <Genius cluster>`
            * Tier-2 :ref:`wICE <Wice cluster>`

   .. tab-item:: VUB
      :sync: vub

      .. grid:: 3
         :gutter: 4

         .. grid-item-card:: |VUB|
            :columns: 12 4 4 4

            * Tier-2 :ref:`Anansi <Anansi cluster>`
            * Tier-2 :ref:`Hydra <Hydra cluster>`

How to connect
--------------

To connect to the VS Code tunnel, follow these steps:

#. In the web portal, under the 'Interactive Apps' menu, choose 'VS Code
   Tunnel', select the resources and click the ``Launch`` button to launch your
   job. Once your job has started, click the ``Connect`` button to connect.

#. A first browser tab or window opens, showing a terminal session, and you are
   asked 'How would you like to log in to Visual Studio Code?'. Select 'Microsoft
   Account' using the arrow keys on your keyboard and press Enter.

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

.. admonition:: Notes

   - In case of authentication problems, it may be necessary to tick the
     'Cleanup previous VS Code Tunnel login data' checkbox in the resources
     form.
   - To close the remote connection, click again the blue button in the bottom
     left, and select 'Close Remote Connection' in the command palette.

Usage
-----
Usage of the VS Code Tunnel app is very similar to the :ref:`vscode_server` app.
