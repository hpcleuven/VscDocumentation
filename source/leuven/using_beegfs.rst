.. _using BeeGFS:

Using BeeGFS
============

BeeGFS is a file system that is created on the nodes on which a job runs.  As physical
storage, it relies on the node's local storage, i.e., a partition of the SSD
drive in that node.

This implies that the size of the file system is at most the partition size
on the SSD, multiplied by the number of nodes on which your job runs.

You can request the creation of such a temporary file system by adding an
attribute to your node resource specification, e.g., the following node
request would create a BeeGFS file system on the 10 nodes the job will run
on::

   -l nodes=10:ppn=36:beeond

.. warning::

   A BeeGFS file system is created when your job starts, and destroyed when
   your job finishes.  As such, you *must ensure* that all relevant data
   is copied to permanent storage such as ``$VSC_DATA`` before your job ends.

The path to the root of this file system is given by the environment variable
``$VSC_SCRATCH_JOB`` and is only defined in the process that runs your job script
on the compute node.

.. note::
   BeeGFS is a parallel file system, hence MPI applications that use MPI-I/O,
   or applications that rely on parallel HDF5 may benefit greatly from using
   it.

Links
-----

- `BeeGFS home page`_ (external)

.. include:: links.rst
