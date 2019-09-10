.. _mmlsquota:

Total disk space on GPFS file systems
=====================================

On some parallel file systems, notably ``$VSC_SCRATCH`` on KU Leuven
infrastructure (Tier-1 and Tier-2), ``mmlsquota`` should be used to
display the total disk space you use and the limits you have.

These file system is a parallel file system, i.e., IBM Spectrum Scale (formerly
GPFS)::

      $ mmlsquota  --block-size auto  vol_ddn2:leuven_scratch
                               Block Limits                                                   |     File Limits
      Filesystem Fileset        type             KB      quota      limit   in_doubt    grace |    files   quota    limit in_doubt    grace  Remarks
      vol_ddn2   leuven_scratch  USR        1444864 1970061312 2073755648          0     none |    16494       0        0        0     none

The ``--block-size auto`` option respectively ensure that sizes are
reported in a human-readable format, rather than expressed in blocks.

The optional volume ``vol_ddn2:leuven`` is the fileset you want information
on.  You can leave out the fileset, but in that case ``mmlsquota`` will
display information on all filesets, most of which you don't have access
to.
