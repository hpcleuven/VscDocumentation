.. _Hopper hardware:

######
Hopper
######

.. note:: Hopper was a UAntwerp Tier-2 cluster, which was decommissioned in 2023. 
 This page is obsolete, and we keep it only for future reference.
 For the currently active UAntwerp Tier-2 clusters, see 
 :ref:`UAntwerp hardware`.

The Hopper compute nodes were used for:

* Jobs that used old software that could not be properly compiled to benefit from the
  extensions in the instruction sets of :ref:`Leibniz<Leibniz hardware>` and 
  :ref:`Vaughan<Vaughan hardware>`, or that lack enough parallelism 
  to fully exploit the :ref:`Leibniz<Leibniz hardware>` or 
  :ref:`Vaughan<Vaughan hardware>` compute nodes (even taking 
  into account that multiple jobs launched nearly simultaneously can still make
  it possible to use the full capacity of a :ref:`Leibniz<Leibniz hardware>` or 
  :ref:`Vaughan<Vaughan hardware>` compute node).
* Jobs that needed more than 128 GB of memory to run properly and that did not need
  more than 20 cores per node.
* Batches of single core jobs (that could not run on your own computer).
* Jobs that did not fit in a maximum wall time of 3 days and could not be restarted cheaply.

*********************
Compute nodes
*********************

When submitting a job with ``sbatch`` or using ``srun``, you could choose to specify
the partition your job was submitted to.
When the option was omitted, your job was submitted to the default partition (**ivybridge**).

The maximum execution wall time for jobs was **7 days** (168 hours).

===============  ======  ============================================  ======  ==========  ========
Slurm partition  nodes   processors per node                           memory  local disk  network
===============  ======  ============================================  ======  ==========  ========
**ivybridge**    23      2x 10-core `Intel Xeon E5-2680v2`_ \@2.8 GHz  256 GB  500 GB      FDR10-IB
===============  ======  ============================================  ======  ==========  ========

*******
History
*******

Hopper was a compute cluster at UAntwerp in operation from late 2014 till the
summer of 2020. The cluster had 168 compute nodes with
dual 10-core `Intel Xeon E5-2680v2`_ Ivy Bridge generation CPUs connected
through an InfiniBand FDR10 network, 144 of these compute nodes having 64 GB
RAM and 24 having 256 GB RAM.

When the cluster was moved out in the summer of 2020 to make space for the
installation of :ref:`Vaughan<Vaughan hardware>`, the 24 nodes with 256 GB RAM
were recovered for further use.
These nodes were finally decommissioned in the summer of 2023. They were replaced
by the :ref:`Breniac<Breniac hardware UAntwerp>` cluster, re-using nodes previously
belonging to the decommissioned :ref:`KU Leuven Tier-1 Breniac cluster<breniac hardware>`.

Origin of the name
==================

Hopper was named after `Grace Hopper <https://en.wikipedia.org/wiki/Grace_Hopper>`_.
Grace Hopper was an American mathematician turned computer scientist and United States Navy
rear admiral. She worked as a programmer of some of the first computer systems and devised
the theory of machine independent programming languages. Her work laid at the base of the 
programming language COBOL.
