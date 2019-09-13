How can I run many similar computations?
========================================

It is often necessary to run the same application on many input files,
or with many different parameter values.  You can of course manage such
jobs by hand, or write scripts to do that for you.  However, this is a
very common scenario, so we developed software to do that for you.

Two general purpose software packages are available:

- the `worker framework`_ and
- `atools <atools documentation>`_.

Both are designed to handle this use case, but with distinct twists.


What features do atools and worker have?
----------------------------------------

Both software packages will do the bookkeeping for you, i.e.,

- keep track of the computations that were completed;
- monitor the progress of a running job; 
- allow you to resume computations in case you underestimated
  the walltime requirements;
- provide an overview of the computations that succeeed, failed,
  or were not completed;
- aggregate output of individual computations;
- analyse the efficiency of a finished job.

Both software packages have been designed with simplicity in mind,
one of the design goals is to make them as easy to use as possible.

For a detailed overview of the features, see the `atools documentation`_
and the `worker documentation`_.


What to use: atools or worker?
------------------------------

That depends on a few things such as

- what are the job policies of the cluster you want to run on?
- how much walltime is required by an individual computation?
- is an individual computation sequential, multi-threaded or
  even distributed?


Job policies
~~~~~~~~~~~~

The following job policies are currently in effect on various VSC clusters.

Shared
   Multiple jobs from multiple users are allowed to run concurrently
   on a node.
Single user
   Multiple jobs from a single user are allowed to run concurrently
   on a node.
Single job
   Only a single job can run on a compute node.

On some clusters, credits are required to run jobs, and that policy may
also influence your choice.

The table below provides an overview of the policies in effect on the
various cluster/partitions.

+----------+--------------------+-----------+-------------+------------+
| VSC hub  | cluster            | partition | policy      | accounting |
+==========+====================+===========+=============+============+
| Antwerp  | any                | any       | single user | no         |
+----------+--------------------+-----------+-------------+------------+
| Brussels | any                | any       | shared      | no         |
+----------+--------------------+-----------+-------------+------------+
| Ghent    | any                | any       | shared      | no         |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | thinking           | default   | single user | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | default   | single user | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | bigmem    | single user | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | gpu       | shared      | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | genius             | superdome | shared      | yes        |
+----------+--------------------+-----------+-------------+------------+
| Leuven   | breniac (Tier-1)   | default   | single job  | yes        |
+----------+--------------------+-----------+-------------+------------+


On some cluster, a single user per node policy is in place
