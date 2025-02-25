.. _specifying output files and notifications:

Specifying job name, output files and notifications
===================================================

In general, there are two ways to pass job properties to the queue manager:

#. they can be specified on the command line when executing ``qsub`` command, or
#. they can be put in the job script on lines that start with
   ``#PBS`` (so-called PBS directives).
  
In a job script, each line that is a PBS directive can contain one or
more options written in exactly the same way as on the command line for
``qsub``.

.. warning::

   These lines **have to** come at the top of the job script, before the
   first Bash statement, but after the she-bang line telling the shell that this is a
   bash script.

Both strategies can be mixed at will: some options can be
put in the job script, while others are specified on the command line.

This can be very useful, e.g., if you run a number of related jobs from
different directories using the same script. The few things that have to
change can then be specified at the command line. The options given at
the command line always overrule those in the job script in case of
conflict.


.. _job name:

Naming jobs
-----------

The default name of a job is derived from the file name of the job
script. This is not very useful if the same job script is used to launch
multiple jobs, e.g., by launching jobs from multiple directories with
different input files. It is possible to overwrite the default name of
the job with ``-N <job_name>``.


.. _output files:

Naming output files
-------------------

Most jobs on a cluster run in batch mode. This implies that they are not
connected to a terminal, so the output sent to the Linux ``stdout``
(standard output) and ``stderr`` (standard error) devices cannot be
displayed on screen.

Instead, it is captured in two files that are put in the directory where
your job was started at the end of your job. The default names of those
files are

- ``<job_name>.o<jobid>`` and
- ``<job_name>.e<jobid>``.

Hence the file names are constructed from the name of the job (the
one assigned using ``-N`` if any, or the default one) and the number of the
job ID assigned when you submit the job to the queue.

You can however change those names using the options

- ``-o <output file>`` and
- ``-e <error file>``.


.. _merge stdout and stderr:

Merging output and error
------------------------

It is also possible to merge both output streams in a single output
stream. The option ``-j oe`` will merge stderr into stdout (and hence
the ``-e`` option does not make sense), the option ``-j eo`` will merge
stdout into stderr.


.. _notifications:

Notification of job events
--------------------------

The scheduler can notify you when a job starts or ends by e-mail. Jobs
can stay queued for hours or sometimes even days before
actually starting, so it is useful to be notified so that you can
monitor the progress of your job while it runs.

You can be notified on three events relating to your job.

+----------------+--------------------------------------------------+
| event mnemonic | description                                      |
+================+==================================================+
| ``b``          | job *beginning*, i.e., job starts                |
+----------------+--------------------------------------------------+
| ``e``          | job *end*, i.e., the job finishes normally       |
+----------------+--------------------------------------------------+
| ``a``          | job *abort*, i.e., the job terminates abnormally |
+----------------+--------------------------------------------------+

Two command line options are involved in this process:

``-m <events>``
   Here, ``<events>`` is any combination of ``b``, ``e`` and ``a``.  These
   are the events you will be notified about.
``-M <mailaddress>``
  This defines the e-mail address to send the notifications to.
   On most clusters the default will be the e-mail address with which you
   registered your VSC-account, but on some clusters this fails and the option
   is required to receive the e-mail.

.. warning:

   When the resource manager attempts to start a job multiple times, you will
   receive an e-mail for each attempt when you ask for ``b`` notification.
   This may not be what you (and your mail system administrator) want.  Unless
   you really need a notification when your job starts, we would suggest to
   only use ``-m ea``.


Other options
-------------

This page describes the most used options in their most common use
cases. There are however more parameters for resource specification and
other options that can be used. For advanced users who want to know
more, we refer to the documentation of the ``qsub`` command that
mentions all options in the Torque manual on the `Adaptive Computing
documentation`_.

-  `Torque 6.0.1 documentation`_

