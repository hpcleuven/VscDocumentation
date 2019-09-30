Login infrastructure
--------------------

Direct login using SSH is possible to all login infrastructure without
restrictions.

You can access Genius through: ``login-genius.hpc.kuleuven.be``

This will loadbalance your connection to one of the 4 Genius login nodes.  
Two types of login nodes are available:

- classic login nodes, i.e., terminal SSH access:

  - ``login1-tier2.hpc.kuleuven.be``
  - ``login2-tier2.hpc.kuleuven.be``
  - ``login3-tier2.hpc.kuleuven.be``
  - ``login4-tier2.hpc.kuleuven.be``

- login node that provides a desktop environment that can be used for,
  e.g., visualization, see the :ref:`NX clients section <NX start guide>1:

  - ``nx.hpc.kuleuven.be``

.. warning::

   This node *should not* be accessed using terminal SSH, it serves only
   as a gateway to the actual login nodes your NX sessions will be running
   on.

The NX login node will start a session on a login node that has a GPU, i.e.,
either

  - ``login3-tier2.hpc.kuleuven.be``
  - ``login4-tier2.hpc.kuleuven.be``
