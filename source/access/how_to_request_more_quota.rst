.. _more quota:

##################################
How can I request more disk quota?
##################################

If the current quota limits of your :ref:`personal storage <data location>` or
:ref:`Virtual Organization (VO) <virtual_organization>` are not large enough to
carry out your research project, it might be possible to increase them. This
option depends on data storage policies of the site managing your VSC account,
VO or Tier-1 project as well as on current capacity of the storage system.

Before requesting more storage, please check carefully the
:ref:`current data usage of your VSC account <quota>` and identify which
file system needs a larger quota.

.. _more quota personal:

Personal storage
================

The storage of personal VSC file systems (``VSC_HOME``, ``VSC_DATA`` and
``VSC_SCRATCH``) are managed by your home institute. In case of doubt, please
contact the corresponding :ref:`helpdesk <tech support VSC>` for your VSC
account.

VSC_HOME
  The storage of your home directory is small on purpose. If you need more
  storage, please switch to ``VSC_DATA``.

VSC_DATA, VSC_SCRATCH
  Policies on these file systems depend on your home institute:

  * KU Leuven/Hasselt University: follow instructions in
    `HPC Service Catalog <https://icts.kuleuven.be/sc/onderzoeksgegevens/HPC-storage>`_
  * Ghent University: larger storage quotas are preferably provided through
    :ref:`Virtual Organizations <more quota vo>`. If it is not possible for you
    to join a VO, please contact hpc@ugent.be 
  * University of Antwerp: contact hpc@uantwerpen.be for further information
  * Vrije Universiteit Brussel: larger storage quotas are preferably provided through
    :ref:`Virtual Organizations <more quota vo>`. If it is not possible for you
    to join a VO, please contact hpc@vub.be 

.. _more quota vo:

Virtual Organizations
=====================

VSC_DATA_VO, VSC_SCRATCH_VO
  The storage quotas of your :ref:`Virtual Organization (VO) <virtual_organization>`
  are managed by the moderator of the VO, who is typically the leader of your
  research group. The moderator can manage all quotas of the VO in the
  `Edit VO <https://account.vscentrum.be/django/vo/edit>`_ tab of the VSC
  account page.

Requesting more storage space
-----------------------------

VO moderators can request additional quota for ``VSC_DATA_VO`` and ``VSC_SCRATCH_VO``:

#. Go to the section **Request additional quota** in the
   `Edit VO <https://account.vscentrum.be/django/vo/edit>`_ tab

#. Fill in the amount of additional storage you want for ``VSC_DATA_VO``
   (labelled ``VSC_DATA`` in this section) and/or ``VSC_SCRATCH_VO`` (labelled
   ``VSC_SCRATCH_XXX`` in this section)

#. Add a comment explaining why you need additional storage space

#. Submit the request by clicking on the *Submit request* button

#. Your request will be reviewed by the HPC administrators

Setting per-member VO quota
---------------------------

VO moderators can tweak the share of the VO quota that each member can
maximally use. By default, this is set to 50% of the total quota for each user.

#. Go to the section **Request additional quota** in the
   `Edit VO <https://account.vscentrum.be/django/vo/edit>`_ tab

#. Adjust the share (%) of the available space available to each user

#. Submit the request by clicking on the *Confirm* button

#. The per-member VO quota will be updated in 30 minutes maximum

.. note::

   The sum of all user quotas in your VO can be above 100%. The share
   for any user indicates what he/she can maximally use, but the actual limit
   will then depend on the usage of the other members. The total storage quota
   of the VO will always be respected.

Tier-1 project
==============

The scratch storage of your project in tier-1 is managed by the institute
hosting the tier-1 HPC infrastructure. Your project directory will have the
quota granted to your project, which should be sufficient to complete all
computational tasks in tier-1. If that is not the case, please contact the
tier-1 helpdesk at compute@vscentrum.be.
