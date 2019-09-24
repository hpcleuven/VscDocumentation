Login infrastructure
--------------------

Direct login using SSH is possible to all login infrastructure without
restrictions.

You can access Genius through::

   login-genius.hpc.kuleuven.be

This will loadbalance your connection to one of the 4 Genius login nodes.  
Two types of login nodes are available:

- classic login nodes, i.e., SSH access.

    - ``login1-tier2.hpc.kuleuven.be``
    - ``login2-tier2.hpc.kuleuven.be``

- login nodes with GPUs for visualization, and :ref:`NX clients
  <NX start guide>`.

  .. note:

     the nodes listed below can only directly be accessed using SSH,
     use ``nx.hpc.kuleuven.be`` as hostname in the NX client configuraton.

    - ``login3-tier2.hpc.kuleuven.be``
    - ``login4-tier2.hpc.kuleuven.be``
