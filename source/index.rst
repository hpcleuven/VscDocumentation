:html_theme.sidebar_secondary.remove:

.. VSC documentation documentation master file, created by
   sphinx-quickstart on Fri Jan 11 14:38:46 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Specific CSS style rules for frontpage as it does not have any sidebars
.. raw:: html

   <style type="text/css">
       html[data-theme="light"] .bd-container { background: var(--pst-color-background); }
       html[data-theme="dark"] .bd-container { background: var(--pst-color-background); }
   </style>


################################
Welcome to the VSC documentation
################################

The VSC documentation offers extensive *how-to* guides and technical
information about the services provided by the `Vlaams Supercomputer Centrum
<https://www.vscentrum.be>`_.

.. toctree::
   :hidden:

   about_vsc
   contact_vsc
   Accounts <access/index>
   Data <data/index>
   Compute <compute>
   Cloud <cloud/index>
   FAQs <faq>

.. grid:: 3
   :gutter: 4

   .. grid-item-card:: :fas:`user-circle` Accounts
      :columns: 12
      :link: access/index
      :link-type: doc
      :class-title: h3

      How to get your VSC account to use the different VSC services and platforms.

   .. grid-item-card:: :fas:`rocket` :doc:`Compute <compute>`
      :columns: 12 12 4 4
      :class-title: h3
   
      The high-performance computing (HPC) platform provides multiple tiers
      of parallel processing enabling researchers to run advanced application
      programs efficiently, reliably and quickly.

      +++

      .. grid:: 2
         :gutter: 2

         .. grid-item-card:: Tier-1
            :text-align: center
            :class-card: text-dark bg-warning opacity-75
            :link: hardware-tier1
            :link-type: doc
   
         .. grid-item-card:: Tier-2
            :text-align: center
            :class-card: text-dark bg-info opacity-75
            :link: hardware-tier2
            :link-type: doc
   
         .. grid-item-card:: Web
            :text-align: center
            :class-card: text-dark bg-danger opacity-75
            :link: leuven/services/openondemand
            :link-type: doc
   
   .. grid-item-card:: :fas:`floppy-disk` :doc:`Data <data/index>`
      :columns: 12 12 4 4
      :class-title: h3
   
      The VSC Data component enables research data to remain close to the
      computing infrastructure during the active phase of the data life
      cycle.

      +++

      .. grid:: 2
         :gutter: 2

         .. grid-item-card:: Tier-1
            :text-align: center
            :class-card: text-dark bg-warning opacity-75
            :link: data/tier1_data_service
            :link-type: doc

   
         .. grid-item-card:: Tier-2
            :text-align: center
            :class-card: text-dark bg-info opacity-75
            :link: data/storage
            :link-type: doc
   
         .. grid-item-card:: Globus
            :text-align: center
            :class-card: text-dark bg-success opacity-75
            :link: globus/index
            :link-type: doc
   
   .. grid-item-card:: :fas:`cloud` :doc:`Cloud <cloud/index>`
      :columns: 12 12 4 4
      :class-title: h3
   
      The VSC Cloud component provides *on-demand* resources in a more
      flexible and cloud-like manner.
   
   .. grid-item-card:: :fas:`question-circle` FAQs
       :columns: 12
       :link: faq
       :link-type: doc
       :class-title: h3

       Collection of frequently asked questions.

