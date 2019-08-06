.. _specifying output files and notitications:

Specifying job name, output files and notifications
===================================================

In general, there are two ways to pass job properties to the queue manager:

#. They can be specified on the command line of the ``qsub`` command
#. Or they can be put in the job script on lines that start with
   ``#PBS`` (so-called in-PBS directives). Each line can contain one or
   more command line options written in exactly the same way as on the
   command line of qsub. These lines **have to** come at the top of the
   job script, before any command (but after the line telling the shell
   that this is a bash script).

And of course both strategies can be mixed at will: Some options can be
put in the job script, while others are specified on the command line.
This can be very useful, e.g., if you run a number of related jobs from
different directories using the same script. The few things that have to
change can then be specified at the command line. The options given at
the command line always overrule those in the job script in case of
conflict.

Naming jobs and output files
----------------------------

The default name of a job is derived from the file name of the job
script. This is not very useful if the same job script is used to launch
multiple jobs, e.g., by launching jobs from multiple directories with
different input files. It is possible to overwrite the default name of
the job with ``-N <job_name>``.

Most jobs on a cluster run in batch mode. This implies that they are not
connected to a terminal, so the output send to the Linux stdout
(standard output) and stderr (standard error) devices cannot be
displayed on screen. Instead it is captured in two files that are put in
the directory where your job was started at the end of your job. The
default names of those files are <job_name>.o<job id> and
<job_name>.e<job id> respectively, so made from the name of the job (the
one assigned with -N if any, or the default one) and the number of the
job assigned when you submit the job to the queue. You can however
change those names using ``-o <output file>`` and ``-e <error file>``.

It is also possible to merge both output streams in a single output
stream. The option ``-j oe`` will merge stderr into stdout (and hence
the -e option does not make sense), the option ``-j eo`` will merge
stdout into stderr.

Notification of job events
--------------------------

Our scheduling system can also notify you when a job starts or ends by
e-mail. Jobs can stay queued for hours or sometimes even days before
actually starting, so it is useful to be notified so that you can
monitor the progress of your job while it runs or kill it when it
misbehaves or produces clearly wrong results. Two command line options
are involved in this process:

-  ``-m abe`` or any subset of these three letters determine for which
   event you'll receive a mail notification: job start (b), job ends (e)
   or job is aborted (a). In some scenarios tis may bombard you with
   e-mail if you have a lot of jobs starting, however at other times it
   is very useful to be notified that your job starts, e.g., to monitor
   if it is running properly and efficiently.
-  With ``-M <mailadress>`` you can set the mail address to which the
   notification will be send. On most clusters the default will be the
   e-mail address with which you registered your VSC-account, but on
   some clusters this fails and the option is required to receive the
   e-mail.

Other options
-------------

This page describes the most used options in their most common use
cases. There are however more parameters for resource specification and
other options that can be used. For advanced users who want to know
more, we refer to the documentation of the ``qsub`` command that
mentions all options in the Torque manual on the `Adaptive Computing
documentation`_.

-  `Torque 6.0.1 documentation`_

.. include:: links.rst
