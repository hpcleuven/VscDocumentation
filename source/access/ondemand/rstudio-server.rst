RStudio Server
--------------

The 'RStudio Server' app allows you to run an RStudio session on the cluster.
In the 'Toolchain year and R version' drop-down menu, you can choose the version
of R module that would be loaded for your session. Additionally, the
``R-bundle-CRAN`` and ``R-bundle-Bioconductor`` modules can be loaded on top of
the base R module to provide easy access to hundreds of preinstalled packages.

It is also possible to use locally installed R packages with RStudio, see e.g.
:ref:`R package management<r_package_management_standard_lib>`.  RStudio
furthermore allows to create RStudio projects to manage your R environments.
When doing so, we recommend selecting the `renv
<https://rstudio.github.io/renv/articles/renv.html>`_ option to ensure a
completely independent R environment. Without using ``renv``, loading an RStudio
project may lead to incomplete R library paths.

For more information on how to use RStudio, check out the `official
documentation <https://docs.posit.co/ide/user/>`__.

.. note::

   - Navigating between your different directories is possible using the file
     explorer.  If you are navigating by clicking the folder, you will notice
     that you can see all user folders.  You do not have access to these, and
     you will receive an error when you try to open them.  You will also notice
     that you cannot use the same way of navigating after this.  Another
     solution is to click the three dots on the right (...) and enter your path.
   - The 'Tools-Install packages' interface does not allow you to select any
     other path than the default in your ``$VSC_HOME``.  It is recommended to
     use the ``install.packages()`` function instead.
   - By default, RStudio Server stores its cache in
     ``$VSC_HOME/.local/share/rstudio``.  This cache can get very large, and
     cause you to exceed the quota of your home directory.  To avoid this, you
     can redirect this cache to your ``$VSC_DATA`` directory by setting the
     ``$XDG_DATA_HOME`` variable in your ``~/.bashrc``:

     .. code-block:: bash

        echo "export XDG_DATA_HOME=$VSC_DATA/.local/share" >> ~/.bashrc

     |VUB| The RStudio app already this variable in your app session for you.

   - Additionally, we recommend changing the default behaviour of RStudio to
     NOT restore the ``.RData`` file (which stores your saved R objects from a
     previous session) into the workspace on startup, and to NEVER 'Save the
     workspace to ``.RData``' on exit.  You can do this via the RStudio
     interface: Tools > Global Options > General > Workspace. These user
     preferences are persistent across RStudio sessions.

     |VUB| Alternatively, you can tick the 'Clean workspace at startup' checkbox
     in the resources form. Note, however, that your user preferences (stored in
     ``$XDG_DATA_HOME/rstudio-prefs.json``, defined by the "load_workspace"
     parameter) take priority over this checkbox option.

.. _RStudio official documentation: https://docs.rstudio.com/
