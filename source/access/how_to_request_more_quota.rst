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

Personal storage
================

The following are general guidelines to request more storage in the personal
file systems of your VSC account:

VSC_HOME
  The storage of your home directory is small on purpose. If you need more
  storage, please switch to ``VSC_DATA``.

VSC_DATA
  On VSC sites that support :ref:`Virtual Organizations (VO)
  <virtual_organization>`, it is preferable to join a VO to get access to a
  larger ``VSC_DATA_VO``.
  If that is not the case or if in doubt, please contact :ref:`user support
  <tech support VSC>`.

VSC_SCRATCH
  On VSC sites that support :ref:`Virtual Organizations (VO)
  <virtual_organization>`, it is preferable to join a VO to get access to a
  larger ``VSC_SCRATCH_VO``.
  If that is not the case or if in doubt, please contact :ref:`user support
  <tech support VSC>`.

Virtual Organizations
=====================

VSC_DATA_VO, VSC_SCRATCH_VO
  The quota of the data storage in your :ref:`Virtual Organization (VO)
  <virtual_organization>` is managed by the moderator of the VO, who is typically
  the leader of  your research group. The moderator can manage all quotas of the VO
  in the `Edit VO <https://account.vscentrum.be/django/vo/edit>`_ tab of the VSC
  account page.

Requesting more storage space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
