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
   Accounts <accounts/index>
   Compute <compute/index>
   Data <data/index>
   Cloud <cloud/index>
   FAQs <faq>

.. grid:: 3
   :gutter: 4

   .. grid-item-card:: :fas:`user-circle` VSC Accounts
      :columns: 12
      :link: accounts/index
      :link-type: doc
      :class-title: fs-3

      How to get your VSC account to use the different VSC services and platforms.

   .. grid-item-card:: :fas:`rocket` Compute
      :class-body: nested-card-container
      :columns: 12 12 4 4
      :link: compute/index
      :link-type: doc
      :class-title: fs-3

      The high-performance computing (HPC) platform provides multiple tiers
      of parallel processing enabling researchers to run advanced application
      programs efficiently, reliably and quickly.

      .. grid:: 2
         :gutter: 2

         .. grid-item-card:: Tier-1 HPC
            :class-item: nested-card-top nested-card-tier1
            :text-align: center
            :link: compute/tier1
            :link-type: doc

         .. grid-item-card:: Tier-2 HPC
            :class-item: nested-card-top nested-card-tier2
            :text-align: center
            :link: compute/tier2
            :link-type: doc

         .. grid-item-card:: Terminal Interface
            :columns: 12 12 12 12
            :class-item: nested-card-top nested-card-term
            :text-align: center
            :link: compute/terminal/index
            :link-type: doc

         .. grid-item-card:: Web Portal
            :class-item: nested-card-top nested-card-web
            :text-align: center
            :link: compute/portal/index
            :link-type: doc

         .. grid-item-card:: Job Queue
            :class-item: nested-card-top nested-card-jobs
            :text-align: center
            :link: compute/jobs/index
            :link-type: doc

         .. grid-item-card:: Scientific Software
            :columns: 12 12 12 12
            :class-item: nested-card-top nested-card-soft
            :text-align: center
            :link: compute/software/index
            :link-type: doc

   .. grid-item-card:: :fas:`floppy-disk` Data
      :class-body: nested-card-container
      :columns: 12 12 4 4
      :link: data/index
      :link-type: doc
      :class-title: fs-3

      The VSC Data component enables research data to remain close to the
      computing infrastructure during the active phase of the data life
      cycle.

      .. grid:: 1
         :gutter: 2

         .. grid-item-card:: Tier-1 Data
            :class-item: nested-card-top nested-card-tier1
            :text-align: center
            :link: data/tier1_data_service
            :link-type: doc

         .. grid-item-card:: Tier-2 Storage
            :class-item: nested-card-top nested-card-tier2
            :text-align: center
            :link: data/storage
            :link-type: doc

         .. grid-item-card:: Globus
            :class-item: nested-card-top nested-card-globus
            :text-align: center
            :link: globus/index
            :link-type: doc

   .. grid-item-card:: :fas:`cloud` Cloud
      :class-body: nested-card-container
      :columns: 12 12 4 4
      :link: cloud/index
      :link-type: doc
      :class-title: fs-3

      The VSC Cloud component provides *on-demand* resources in a more
      flexible and cloud-like manner.

      .. grid:: 1
         :gutter: 2

         .. grid-item-card:: Virtual Machines
            :class-item: nested-card-top nested-card-vms
            :text-align: center
            :link: cloud/manage_images
            :link-type: doc

         .. grid-item-card:: VMs with GPUs
            :class-item: nested-card-top nested-card-vmsgpu
            :text-align: center
            :link: cloud/gpus
            :link-type: doc

         .. grid-item-card:: Orchestration
            :class-item: nested-card-top nested-card-orch
            :text-align: center
            :link: cloud/terraform
            :link-type: doc

   .. grid-item-card:: :fas:`question-circle` FAQs
       :columns: 12
       :link: faq
       :link-type: doc
       :class-title: fs-3

       Collection of frequently asked questions.

