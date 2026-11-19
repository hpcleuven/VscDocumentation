Location Access Restrictions
============================

Depending on your institution and location, additional network access
restrictions may apply when connecting to VSC clusters.

.. tab-set::
   :sync-group: vsc-sites

   .. tab-item:: KU Leuven/UHasselt
      :sync: kuluh

      Since March 2026, the firewall access to the HPC cluster is resolved by the global KU Leuven firewall rules. This impacts connections to the Tier-2 cluster.

      There is a difference between connecting from a managed KU Leuven laptop and unmanaged laptops.

      KU Leuven managed laptops
         Use MFA (certificate) for connections both from Belgium and from abroad. No need to request :ref:`additional firewall login <additional_firewall>`.

      Non-managed laptops
         There are several possibilities to connect to the KU Leuven VSC clusters:

         * From all locations (connecting from VPN B zone, from other VSC universities, from other Belgian IP addresses and from abroad): open the firewall page (https://firewall.vscentrum.be) and request a certificate. The firewall page only needs to be active when making new connections to the cluster.
         * Exception for connections from within VSC network (*i.e.* other VSC clusters) - certificate is sufficient

   .. tab-item:: UAntwerpen
      :sync: ua

      All UAntwerpen clusters are behind a firewall, which is configured by default to block all traffic from abroad.
      If you want to access any VSC cluster from abroad, it is necessary that you first authorize your own connection on the `VSC Firewall`_.
      Once your connection is authorized, you can proceed as usual.

      .. note::

         The `VSC Firewall`_ page only needs to be active when making new connections to the VSC cluster.

   .. tab-item:: UGent
      :sync: ug

      All UGent clusters are behind a firewall, which is configured by default to block all traffic from abroad.
      If you want to access any VSC cluster from abroad, it is necessary that you first authorize your own connection on the `VSC Firewall`_.
      Once your connection is authorized, you can proceed as usual.

      .. note::

         The `VSC Firewall`_ page only needs to be active when making new connections to the VSC cluster.

   .. tab-item:: VUB
      :sync: vub

      .. rubric:: Portal access

      The VUB-HPC Tier-2 OnDemand portal can be accessed from abroad without authorization on the VSC Firewall.

      .. rubric:: SSH access

      All VUB-HPC Tier-2 clusters are gated behind a firewall, which is configured by default to block all SSH traffic from abroad.
      If you want to access a VSC cluster via SSH from abroad, you must first authorize your own connection on the `VSC Firewall`_.
      Once your connection is authorized, you can proceed as usual.

      .. note::

         The `VSC Firewall`_ page only needs to be active when making new connections to the VSC cluster.

