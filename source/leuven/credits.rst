.. _KU Leuven credits:

Credits to use KU Leuven infrastructure
=======================================

KU Leuven uses a credit system to do accounting on the HPC systems it hosts.
This is the case for its Tier-2 clusters, as well as the Tier-1 infrastructure.

Information on how to use the credit system can be found in the :ref:`documentation
on credit system basics <credit system basics>`.


How do I request credits on the KU Leuven Tier-2 systems
--------------------------------------------------------

KU Leuven users
~~~~~~~~~~~~~~~
You can request two types of job credits: introduction credits and project
credits.

Introduction credits
   This is a limited amount of free credits for test and development purposes.
Project credits
   These are job credits used for actual research and production runs.

You will find the relevant information to apply for both types of credits,
including pricing, in the `Service Catalog`_ (login required).

UHasselt users
~~~~~~~~~~~~~~
If you would like credits for a new project, please fill out the
`credit request form`_.

.. warning::

   Please read and follow the instructions in that form carefully!

If you require additional credits for an existing project, please contact
your VSC coordinator `Geert Jan Bex`_.

Other users
~~~~~~~~~~~

Please contact your VSC coordinator/contact or your :ref:`local support staff
<Contact VSC>`.


Job cost calculation
~~~~~~~~~~~~~~~~~~~~

The cost of a job depends on the resources it consumes. Generally
speaking, one credit buys the user one hour of walltime on one reference
node. The resources that are taken into account to charge for a job are
the walltime it consumed, and the number and type of compute nodes it
ran on. The following formula is used:

0.000278 \* *nodes* \* *walltime* \* *nodetype*

Where

-  *nodes* is the number of compute nodes the job ran on;
-  *walltime* the effective duration of the job, expressed in seconds;
-  *nodetype* is the factor representing the node type's performance as
   listed in the table below.

The Tier-2 cluster has several types of compute nodes, none of which
is actually a reference node. The values for the different types are
listed at the following links:

- :ref:`Genius <running jobs on genius>`

The difference in cost between different machines/processors reflects
the performance difference between those types of nodes. The total cost
of a job will typically be the same on any compute nodes, but the
walltime will be different, depending on the performance of the nodes.

In the examples below, you run your jobs on a ``skylake`` node, for which
we charge 10 credits per hour.

An example of a job running on multiple nodes and cores is given below::

   $ qsub  -A lp_astrophysics_014  -l nodes=2:ppn=36:skylake  simulation_3415.pbs

If this job finished in 2.5 hours (i.e., walltime is 9000 seconds), the user
will be charged:

0.000278 \* 2 \* 9000 \* 10 = 50.0 credits


How do I get credits to use the Tier-1 infrastructure
-----------------------------------------------------

Access to the Tier-1 is project-based, if you have a starting grant or
an approved project, or you pay for your compute time, you should have
received information on your job credits.  If not, please :ref:`contact
support <Contact VSC>`.


.. _Geert Jan Bex: mailto:geertjan.bex@uhasselt.be
.. _credit request form:  https://admin.kuleuven.be/icts/onderzoek/hpc/request-project-credits
.. include:: ../jobs/links.rst
.. include:: links.rst
