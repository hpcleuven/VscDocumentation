.. _compute portal:

.. _ood:

#####################################
:fas:`circle-play` Access: Web Portal
#####################################

Open OnDemand web portal provides a user interface to HPC clusters from within a
web browser.  It supports a range of different apps and features that not only
allow the user to easily submit jobs from within the browser, but also provide
different coding GUIs, tools for plotting and more.

VSC OnDemand Portals
====================

VSC clusters that support an Open OnDemand web portal:

.. grid:: 4
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 6 6 3 3
       :padding: 2 2 1 1

       :fas:`circle-play` `KU Leuven OnDemand`_

       | Tier-2 :ref:`Genius <Genius hardware>`
       | Tier-2 :ref:`Superdome <Superdome hardware>`
       | Tier-2 :ref:`wICE <wICE hardware>`

    .. grid-item-card:: |UA|
       :columns: 6 6 3 3
       :padding: 2 2 1 1

       :fas:`circle-play` `UAntwerp OnDemand`_

       | Tier-2 :ref:`Vaughan <Vaughan hardware>`
       | Tier-2 :ref:`Leibniz <Leibniz hardware>`
       | Tier-2 :ref:`Breniac <Breniac hardware UAntwerp>`

    .. grid-item-card:: |UG|
       :columns: 6 6 3 3
       :padding: 2 2 1 1

       :fas:`circle-play` `UGent OnDemand`_

       Consult the `UGent OnDemand docs <https://docs.hpc.ugent.be/web_portal/>`_

    .. grid-item-card:: |VUB|
       :columns: 6 6 3 3
       :padding: 2 2 1 1

       :fas:`circle-play` `VUB OnDemand`_

       | Tier-2 :ref:`Anansi <Anansi cluster>`
       | Tier-2 :ref:`Hydra <Hydra cluster>`

.. _KU Leuven OnDemand: https://ondemand.hpc.kuleuven.be/
.. _UAntwerp OnDemand: https://portal.hpc.uantwerpen.be/
.. _UGent OnDemand: https://login.hpc.ugent.be/
.. _VUB OnDemand: https://portal.hpc.vub.be/

You can log in using the credentials of your home institution or your VSC
credentials. SSH keys are not required to use the web portal.

Portal features
===============

The VSC OnDemand web portals provide a range of functions:

- Browsing, creating, transferring, viewing and/or editing files
- Opening a shell on one of the login nodes
- Submitting and monitoring jobs, creating job templates
- Using interactive apps

All of these functionalities can be accessed via the menu bar at the top of the
web portal.

General features
----------------

.. toctree::
   :maxdepth: 1

   ondemand/files
   ondemand/login-shell
   ondemand/active-jobs
   ondemand/interactive-apps

Interactive apps
----------------

.. toctree::
   :maxdepth: 1

   ondemand/desktop
   ondemand/fluent
   ondemand/gaussview
   ondemand/igv-web
   ondemand/interactive-shell
   ondemand/jupyterlab
   ondemand/matlab
   ondemand/open-webui
   ondemand/paraview
   ondemand/pycharm
   ondemand/rstudio-server
   ondemand/tensorboard
   ondemand/vscode-server
   ondemand/vscode-tunnel

