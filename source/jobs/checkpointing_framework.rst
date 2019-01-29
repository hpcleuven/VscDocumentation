Checkpointing framework
=======================

What is checkpointing
---------------------

Checkpointing allows for running jobs that run for weeks or months. Each
time a subjob is running out of requested wall time, a snapshot of the
application memory (and much more) is taken and stored, after which a
subsequent subjob will pick up the checkpoint and continue.

If the compute nodes have support for BLCR, checkpointing can be used.

How to use it
-------------

Using checkpointing is very simple: just use **csub** instead of qsub to
submit a job.

The csub command creates a wrapper around your job script, to take care
of all the checkpointing stuff. In practice, you (usually) don't need to
adjust anything, except for the command used to submit your job.
Checkpointing does not require any changes to the application you are
running, and should support most software. There are a few corner cases
however (see `the BLCR Frequently Asked
Questions <https://upc-bugs.lbl.gov/blcr/doc/html/FAQ.html>`_).

The csub command
----------------

Typically, a job script is submitting with checkpointing support enabled
by running:

::

   $ csub -s job_script.sh

One important caveat is that the job script (or the applications run in
the script) should not create it's own local temporary directories.

Also note that adding PBS directives (#PBS) in the job script is
useless, as they will be ignored by csub. Controlling job parameters
should be done via the csub command line.

Help on the various command line parameters supported by csub can be
obtained using -h:

::

    $ csub -h
       csub [opts] [-s jobscript]
       
       Options:
           -h or --help               Display this message
           
           -s                         Name of jobscript used for job.
                                      Warning: The jobscript should not create it's own local temporary directories.
           
           -q                         Queue to submit job in [default: scheduler default queue]
           
           -t                         Array job specification (see -t in man qsub) [default: none]
           
           --pre                      Run prestage script (Current: copy local files) [default: no prestage]

           --post                     Run poststage script (Current: copy results to localdir/result.) [default: no poststage]

           --shared                   Run in shared directory (no pro/epilogue, shared checkpoint) [default: run in local dir]

           --no_mimic_pro_epi         Do not mimic prologue/epilogue scripts [default: mimic pro/epi (bug workaround)]
           
           --job_time=<string>        Specify wall time for job (format: <hours>:<minutes>:<seconds>s, e.g. 3:12:47) [default: 10h]

           --chkpt_time=<string>      Specify time for checkpointing a job (format: see --job_time) [default: 15m]
           
           --cleanup_after_restart    Specify whether checkpoint file and tarball should be cleaned up after a successful restart
                                      (NOT RECOMMENDED!) [default: no cleanup]
           
           --no_cleanup_chkpt         Don't clean up checkpoint stuff in $VSC_SCRATCH/chkpt after job completion [default: do cleanup]
           
           --resume=<string>          Try to resume a checkpointed job; argument should be unique name of job to resume [default: none]
           
           --chkpt_save_opt=<string>  Save option to use for cr_checkpoint (all|exe|none) [default: exe]
           
           --term_kill_mode           Kill checkpointed process with SIGTERM instead of SIGKILL after checkpointing [defailt: SIGKILL]
           
           --vmem=<string>            Specify amount of virtual memory required [default: none specified]\"

Below we discuss various command line parameters.

**--pre** and **--post**
   The --pre and --post parameters steer whether local files are copied
   or not. The job submitted using csub is (by default) runs on the
   local storage provided by a particular compute node. Thus, no changes
   will be made to the files on the shared storage (e.g. $VSC_SCRATCH).
   If the job script needs (local) access to the files of the directory
   *where csub is executed*, **--pre** should be specified. This will
   copy all the files in the job script directory to the location where
   the job script will execute.
   If the output of the job that was run, or additional output files
   created by the job in it's working directory are required, **--post**
   should be used. This will copy the entire job working directory *to
   the location where csub was executed*, in a directory named
   result.<jobname>. An alternative is to copy the interesting files to
   the shared storage at the end of the job script.
**--shared**
   If the job needs to be run *on the shared storage* and not on the
   local storage of the workernode (for whatever reason), **--shared**
   should be specified. In this case, the job will be run in a
   subdirectory of $VSC_SCRATCH/chkpt. This will also disable the
   execution of the prologue and epilogue scripts, which prepare the job
   directory on the local storage.
**--job_time** and **--chkpt_time**
   To specify the requested wall time *per subjob*, use the
   **--job-time** parameter. The default settings is 10 hours per
   subjob. Lowering this will result in more frequent checkpointing, and
   thus more subjobs.
   To specify *the time that is reserved for checkpointing* the job, use
   **--chkpt_time**. By default, this is set to 15 minutes which should
   be enough for most applications/jobs. Don't change this unless you
   really need to.
   **The total requested wall time per subjob is the sum of both
   job_time and chkpt_time.** This should be taken into account when
   submitting to a specific job queue (e.g., queues which only support
   jobs of up to 1 hour).
**--no_mimic_pro_epi**
   The option **--no_mimic_pro_epi** disables the workaround currently
   implemented for a permissions problem when using actual Torque
   prologue/epilogue scripts. Don't use this option unless you really
   know what you're doing!

Support for csub
----------------

-  **Array jobs**
   csub has support for checkpointing array jobs. Just specify \\"-t
   <spec>\" on the csub command line (see qsub for details).
-  **MPI support**
   The BLCR checkpointing mechanism behind csub has support for
   checkpointing MPI applications. However, checkpointing MPI
   applications is pretty much untested up until now. If you would like
   to use csub with your MPI applications, please :ref:`contact user
   support <contact user support>`.

Notes
-----

If you would like to time how long the complete job executes, just
prepend the main command in your job script with time, e.g.: **time
<command>**. The *real* time will not make sense as it will also include
the time passes between two checkpointed subjobs. However, the *user*
time should give a good indication of the actual time it took to run
your command, even if multiple checkpoints were performed.
