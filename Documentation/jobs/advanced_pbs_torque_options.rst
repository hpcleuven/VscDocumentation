Advanced PBS/Torque options
===========================

**This page is outdated. Please check our updated \\"\ \ **\ `Running
jobs <\%22/cluster-doc/running-jobs\%22>`__\ **\ \\" section on the user
portal. If you came to this page following a link on a web page of this
site (and not via a search) you can help us improve the documentation by
mailing the URL of the page that brought you here
to\ **\ `kurt.lust@uantwerpen.be <\%22mailto:kurt.lust@uantwerpen.be\%22>`__\ **\ .**

Resource management: PBS/Torque
-------------------------------

The resource manager has to be aware of available resources so that it
can start the users' jobs on the appropriate compute nodes. These
resources include, but are not limited to, the number of compute nodes,
the number of cores in each node, as well as their type, and the amount
of memory in each node. In addition to the hardware configuration, the
resource manager has to be aware of resources that are in currently in
use (configured, but occupied by or reserved for running jobs) and
currently available resources.

The software we use for this is called PBS/Torque (Portable Batch
System):

*TORQUE Resource Manager provides control over batch jobs and
distributed computing resources. It is an advanced open-source product
based on the original PBS project\* and incorporates the best of both
community and professional development. It incorporates significant
advances in the areas of scalability, reliability, and functionality and
is currently in use at tens of thousands of leading government,
academic, and commercial sites throughout the world. TORQUE may be
freely used, modified, and distributed under the constraints of the
included license.*

*TORQUE can integrate with Moab Workload Manager to improve overall
utilization, scheduling and administration on a cluster. Customers who
purchase Moab family products also receive free support for TORQUE.*

*(*\ `http://www.adaptivecomputing.com/products/open-source/torque/ <\%22http://www.adaptivecomputing.com/products/open-source/torque/\%22>`__\ *)*

To make sure that the user's job obtains the appropriate resources to
run, the user has to specify these requirements using PBS directives.
PBS directives can either be specified on the command line when using
'qsub', or in a PBS script.

PBS directives for resource management
--------------------------------------

Walltime
~~~~~~~~

By default, the scheduler assumes a run time for a job of one hour. This
can be seen in the \\"Resource List\" line in the standard output file,
the wall time was set to one hour, unless specified otherwise by the
user:

::

   Resource List: neednodes=1:ppn=1,nodes=1:ppn=1,walltime=01:00:00

For many jobs, the default wall time will not be sufficient: some will
need multiple hours or even days to complete. However, when a job
exceeds the specified wall time, it will be automatically killed by the
scheduler, and, unless the job saves intermediate results, all
computations will be lost. On the other hand, a shorter wall time may
move your job forward in the queue: the scheduler may notice that there
is a gap of 30 minutes between two bigger jobs on a node, and decide to
insert a shorter job (this process is called backfilling).

To specify a wall time of ten minutes, you can use the following
parameter (or directive) for 'qsub':

::

   $ qsub -l walltime=00:10:00 job.pbs

The walltime is specified as (H)HH:MM:SS, so a job that is expected to
run for two days can described using

::

   $ qsub -l walltime=48:00:00 job.pbs

Characteristics of the compute nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+---------------+----------------+---------------+-----------+
| site      | architecture  | np             | installed mem | avail mem |
+===========+===============+================+===============+===========+
| KU Leuven | Ivy Bridge    | 20             | 64 GB         | 60 GB     |
+-----------+---------------+----------------+---------------+-----------+
| KU Leuven | Ivy Bridge    | 20             | 128 GB        | 120 GB    |
+-----------+---------------+----------------+---------------+-----------+
| KU Leuven | harpertown    | 8              | 8 GB          | 7 GB      |
+-----------+---------------+----------------+---------------+-----------+
| KU Leuven | nehalem       | 8              | 24 GB         | 23 GB     |
+-----------+---------------+----------------+---------------+-----------+
| KU Leuven | nehalem (fat) | 16\ :sup:`(*)` | 74 GB         | 73 GB     |
+-----------+---------------+----------------+---------------+-----------+
| KU Leuven | westmere      | 12             | 24 GB         | 23 GB     |
+-----------+---------------+----------------+---------------+-----------+
| UA        | harpertown    | 8              | 16 GB         | 15 GB     |
+-----------+---------------+----------------+---------------+-----------+
| UA        | westmere      | 24\ :sup:`(*)` | 24 GB         | 23 GB     |
+-----------+---------------+----------------+---------------+-----------+

:sup:`(*)`: These nodes have hyperthreading enabled. They have only 8
(nehalem) or 12 (westmere) physical cores, but create the illusion of 16
or 24 \\"virtual\" cores effectively running together (i.e., 16 or 24
simultaneous threads). Some programs benefit from using two threads per
physical core, some do not.

There is more information on the specific characteristics of the compute
nodes in the various VSC clusters on the hardware description page for
each cluster in the \\"\ `Available
hardware <\%22/infrastructure/hardware\%22>`__\\" section.

Number of processors
~~~~~~~~~~~~~~~~~~~~

By default, only one core (or CPU, or processor) will be assigned to a
job. However, parallel jobs need more than one core, e.g., MPI or openMP
applications. After deciding on the number of cores, the \\"layout\" has
to be choosen: can all cores of a node be used simultaneously, or do
memory requirements dictate that only some of the cores of nodes can be
used? The layout can be specified using the 'nodes' and 'ppn'
attributes.

The following example assumes that 16 cores will be used for the job,
and that all cores on a compute node can be used simultaneoulsy:

::

   $ qsub -l nodes=2:ppn=8 job.pbs

There's no point in requesting more cores per node than are available.
The maximum available ppn is processor dependent and is shown in the
table above. On the other hand, due to memory consumption or memory
access patterns, it may be necessary to restrict the number of cores per
node, e.g.,

::

   $ qsub -l nodes=4:ppn=4 job.pbs

As in the previous example, this job requires 16 cores, but now only 4
out of the 8 available cores per compute node will be used.

It is very important to note that the resource manager may put any
multiple of the requested 'ppn' on one node (this is called
\\"packing\") as long as the total is smaller than 8. E.g., when the job
description specifies 'nodes=4:ppn=2', the system may actually assign it
4 times the same node: 2 x 4 = 8 cores. This behavior can be
circumvented by setting the memory requirements appropriately.

Note that requesting multiple cores does not run your script on each of
these cores! The system will start your script on one core only (the
\\"mother superior\") and provide it with a list of nodes that have
cores available for you to use. This list is stored in a file
'$PBS_NODEFILE'. You now have to \\"manually\" start your program on
these nodes. Some of this will be done automatically for you when you
use MPI (see the section about `Message Passing
Interfaces <\%22/cluster-doc/development/mpi\%22>`__).

Processor type
~~~~~~~~~~~~~~

As seen in the table above, we have different architectures and
different amount of memory in different kinds of nodes. In some
situations, it is convenient or even necessary to request a specific
architecture for a job to run on. This is easily accomplished by adding
a feature to the resource description, e.g.,

::

   $ qsub -l nodes=1:nehalem job.pbs

Here, a single node is requested, but it should be equipped with a
Nehalem Intel processor. The following example specifies job running on
2 x 4 cores of type 'harpertown'.

::

   $ qsub -l nodes=2:ppn=4:harpertown job.pbs

Memory
~~~~~~

Besides the number of processors, the required amount of memory for a
job is an important resource. This can be specified in two ways, either
for the job in its entirety, or by individual process, i.e., per core.
The following directive requests 2 Gb of RAM for each core involved in
the computation:

::

   $ qsub -l nodes=2:ppn=4,pmem=2gb job.pbs

Note that a request for multiple resources, e.g., nodes and memory, are
comma separated.

As indicated in the table above, not all of the installed memory is
available to the end user for running jobs: also the operating system,
the cluster management software and, depending on the site also the file
system, require memory. This implies that the memory specification for a
single compute node should not exceed the figures shown in the table. If
the memory requested exceeds the amount of memory available in a single
compute node, the job can not be executed, and will remain in the queue
indefinitely. The user is informed of this when he runs 'checkjob'.

Note that specifying 'pmem' judiciously will prevent unwanted packing,
mentioned in the previous section.

Similar to the required memory per core, it is also possible to specify
the total memory required by the job using the 'mem' directive.

Non-resource related PBS directives
-----------------------------------

PBS/Torque has a number of convinient features that are not related to
resource management as such.

Notification
~~~~~~~~~~~~

Some users like to be notified when their jobs are done, and this can be
accomplished using the appropriate PBS directives.

::

   $ qsub -m ae -M albert.einstein@princeton.edu job.pbs

Here, the user indicates that he wants to be notified either when his
job is aborted ('a') by PBS/Torque (when, e.g., the requested walltime
was exceeded), or when his jobs ends ('e'). The notification will be
send to the email address specified using the '-M' flag.

Apart from the abort ('a') and end ('e') events, a notification can also
be sent when the job begins ('b') execution.

Job name
~~~~~~~~

By default, the name of a job is that of the PBS script that defines it.
However, it may be easier to keep track of multiple runs of the same job
script by assigning a specific name to each. A name can be specified
explicitly by the '-N' directive, e.g.,

::

   $ qsub -N 'spaceweather' job.pbs

Note that this will result in the standard output and error files to be
named 'spaceweather.o<nnn>' and 'spaceweather.e<nnn>'.

In-script PBS directives
------------------------

Given all these options, specifying them for each individual job
submission on the command line soon gets a trifle unwieldy. As an
alternative to passing PBS directives as command line arguments to
'qsub', they can be specified in the script that is being submitted. So
instead of typing:

::

   qsub -l nodes=8:ppn=2 job.pbs

the 'job.pbs' script can be altered to contain the following:

::

   #!/bin/bash -l
   #PBS -l nodes=8:ppn=2
   ...

The \\"#PBS\" prefix indicates that a line contains a PBS directive.
Note that PBS directives should preceed all commands in your script,
i.e., they **have to be** listed immediately after the '#!/bin/bash -l'
line!

If this PBS script were submitted as follows, the command line resource
description would override that in the 'job.pbs' script:

::

   $ qsub -l nodes=5:ppn=2 job.pbs

The job would run on 5 nodes, 2 cores each, rather than on 8 nodes, 2
cores each as specified in 'job.pbs'.

Any number of PBS directives can be listed in a script, e.g.,

::

   #!/bin/bash -l
   # Request 8 nodes, with 2 cores each
   #PBS -l nodes=8:ppn=2
   # Request 2 Gb per core
   #PBS -l pmem=2gb
   # Request a walltime of 10 minutes
   #PBS -l walltime=00:10:00
   # Keep both standard output, standard error
   #PBS -j oe
   #
   ...

"
