.. _tier2_login_nodes:

Tier-2 access
-------------

Currently, wICE and Mindwell are the Tier-2 clusters in production at KU Leuven.
Both clusters run on the Rocky Linux 9.6 operating system. The access to both
machines is possible

- either via the wICE login nodes (see below), as Mindwell has no
  dedicated login nodes

- or via the :ref:`Open OnDemand <ood>` portal in your web browser

Login infrastructure
--------------------

.. note::

   Restrictions apply for direct login using SSH. Make sure to read the
   section on :ref:`access restrictions <location_access_restrictions>`
   before proceeding.

You can access the KU Leuven Tier-2 through ``login.hpc.kuleuven.be``. 
This will loadbalance your connection to one of the 4 wICE login nodes.
