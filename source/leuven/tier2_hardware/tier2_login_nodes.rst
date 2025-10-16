.. _tier2_login_nodes:

Tier-2 access
-------------

Currently, Genius and wICE are the two Tier-2 clusters in production at KU Leuven.
The access to both machines is possible

- either via the Genius login nodes (see below), as wICE itself has no
  dedicated login node

- or via the :ref:`Open OnDemand <ood>` on your web browser

Login infrastructure
--------------------

Direct login using SSH is possible to all login infrastructure without
restrictions.

You can access the KU Leuven Tier-2 either through ``login.hpc.kuleuven.be`` or
``login-genius.hpc.kuleuven.be``.
This will loadbalance your connection to one of the 4 Genius login nodes.

Two types of login nodes are available:

- classic login nodes, i.e., terminal SSH access:

  - ``login1-tier2.hpc.kuleuven.be``
  - ``login2-tier2.hpc.kuleuven.be``
  - ``login3-tier2.hpc.kuleuven.be``
  - ``login4-tier2.hpc.kuleuven.be``

- login node that provides a desktop environment on Genius that can be used for,
  e.g., visualization, see the :ref:`NX clients section <NX start guide>`:

  -  ``nx.hpc.kuleuven.be``

     .. warning::

        This node *should not* be accessed using terminal SSH, it serves only
        as a gateway to the actual login nodes your NX sessions will be running
        on.

     The NX login node will start a session on a login node that has a GPU, i.e.,
     one of

       - ``login3-tier2.hpc.kuleuven.be``
       - ``login4-tier2.hpc.kuleuven.be``

