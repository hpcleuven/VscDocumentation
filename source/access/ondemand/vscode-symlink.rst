Before you connect
------------------

VS Code automatically creates hidden folders ``.vscode`` and ``.vscode-server``
in your ``$VSC_HOME``, which tend to become rather big, especially if you use a
lot of extensions.  To avoid filling up your ``$VSC_HOME``, we recommend
replacing those folders with symlinks to your ``$VSC_DATA``:

.. code-block:: bash

   mkdir $VSC_DATA/.vscode $VSC_DATA/.vscode-server
   ln -s $VSC_DATA/.vscode ~/.vscode
   ln -s $VSC_DATA/.vscode-server ~/.vscode-server

If you already have folders ``~/.vscode`` and ``~/.vscode-server``, you can move
them to ``$VSC_DATA`` before symlinking.

