Job submission and credit reservations
======================================

When you submit a job, a reservation is made. This means that the number
of credits required to run your job is marked as reserved. Of course,
this is the number of credits that is required to run the job during the
walltime specified, i.e., the reservation is computed based on the
requested walltime.

Hence, if you submit a largish number of jobs, and the walltime is
overestimated, reservation will be made for a total that is potentially
much larger than what you'll actually be debited for upon job completion
(you're only debited for the walltime used, not the walltime requested).

Now, suppose you know that your job will most probably end within 24
hours, but you specify 36 hours to be on the safe side (which is a good
idea). Say, by way of example, that the average cost of a single job
will be 300 credits. You have 3400 credits, so you can probably run at
least 10 such jobs, so you submit all 10.

Here's the trap: for each job, a reservation is made, not of 300
credits, but of 450. Hence everything goes well for the first 7 (7*450 =
3150 < 3400), but for the 8th up to the 10th job, your account no longer
has sufficient credits to make a reservation. Those 3 jobs will be
blocked by a SystemHold, and never execute (unless additional credits
are requested, and a sysadmin releases them as will happen now).

We actually have a nice tool to compute the maximum number of credits a
job can take. It is called gquote, and you can use it as follows. Suppose
that you submit your job using, e.g.:

::

   $ qsub  -l walltime=4:00:00 my_job.pbs

Then you can compute its cost (before actually doing the qsub) by:

::

   $ module load accounting
   $ gquote  -l walltime=4:00:00  my_job.pbs

If this is a worker job, and you submit it as, e.g.:

::

   $ wsub  -data data.csv  -batch my_job.pbs  -l nodes=4:ppn=20

Then you can compute its cost (before actually doing the qsub) by:

::

   $ module load accounting
   $ gquote  -l nodes=4:ppn=20  my_job.pbs

As you can see, gquote takes the same arguments as qsub (so if you use
wsub, don't use the -batch for the actual job script). It will use both
the arguments on the command line and the PBS directives in your script
to compute the cost of the job in the same way PBS Torque is computing
the resources for your job.

You will notice when using gquote that it will give you quotes that are
more expensive than you expect. This typically happens when you don't
specify the processor attribute for the nodes resource. gquote will
assume that you job is executed on the most expensive processor type,
which inflates prices.

The price of a processor is of course proportional to its performance,
so when the job finishes, you will be charged approximately the same
regardless of the processor type the job ran on. (It ran for a shorter
time on a more faster, and hence more expensive processor.)
