.. _mmlsquota:

Total disk space on GPFS file systems
=====================================

On the parallel file system ``$VSC_SCRATCH`` on KU Leuven Tier-1
infrastructure, ``mmlsquota`` can be used to
display the total disk space you use and the limits you have.

This file system is a parallel file system, i.e., IBM Spectrum Scale (formerly
GPFS)::

      $ mmlsquota  --block-size auto  nec_vol1:leuven_scratch
                               Block Limits                                                   |     File Limits
      Filesystem Fileset        type             KB      quota      limit   in_doubt    grace |    files   quota    limit in_doubt    grace  Remarks
      nec_vol1   leuven_scratch  USR        1444864 1970061312 2073755648          0     none |    16494       0        0        0     none

The ``--block-size auto`` option ensures that sizes are
reported in a human-readable format, rather than expressed in blocks.

The optional volume ``nec_vol1:leuven_scratch`` in the example above is the fileset
you want information on.  You can leave out the fileset, but in that case
``mmlsquota`` will display information on all filesets, most of which you
don't have access to.

Total disk space on Lustre file systems
=======================================

On the parallel file system ``$VSC_SCRATCH`` on KU Leuven Tier-2
infrastructure, ``lfs`` can be used to display the total disk
space you use and the limits you have. For instance, to show the
usage for user ``vsc33716`` in a human-readable format::

      $ lfs quota -hp 33716 /lustre1
      Disk quotas for prj 33716 (pid 33716):
           Filesystem    used   quota   limit   grace   files   quota   limit   grace
             /lustre1  828.1G    950G   1000G       -  418274       0       0       -
      pid 33716 is using default file quota setting
