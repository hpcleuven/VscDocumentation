.. _vo:

####################
Virtual Organization
####################

A Virtual Organization (VO) is a special type of group. The members of a VO get
access to extra storage in the HPC cluster with shared directories between them
to easily collaborate with their colleagues. Any user can only be a member of a
single VO in each VSC institution.

VSC clusters that support Virtual Organizations:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |UG|
       :columns: 12 4 4 4

       * Tier-1 :ref:`Hortense <Hortense hardware>` [#f1]_
       * Tier-2 :ref:`All clusters <UGentT2 hardware>`

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Hydra <Hydra cluster>`
       * Tier-2 :ref:`Anansi <Anansi cluster>`

.. [#f1] partial support, only ``VSC_DATA_VO``

VO directories
==============

Members of the VO have access to additional directories in the scratch and data
storage of the cluster.

.. include:: vo-storage.rst

* ``$VSC_SCRATCH_VO`` and ``$VSC_DATA_VO``: top directory shared by all members
  of the VO

* ``$VSC_SCRATCH_VO_USER`` and ``$VSC_DATA_VO_USER``: each member of the VO has
  its own personal folder inside the VO that can only be accessed by its owner.
  Both folders can be used as alternatives to their personal ``$VSC_SCRATCH``
  and ``$VSC_DATA``.

.. _join_vo:

Joining an existing VO
======================

.. warning:: Keep in mind that users can only be a member of a single VO in the
   same VSC institution. Thus, if you are member of a VO and join another VO,
   you will lose access to the data in the first VO.

Members of the research team can make a request to join the VO of their
research group:

#. Get the ID of the VO of your research group you belong to. VO's ID in VUB
   are formed by the letters ``bvo`` followed by 5 digits.

#. Fill in the section **Join VO** of your `VSC Account - New/Join VO`_ page

   * Select the corresponding VO ID from the drop-down box below *Group*

   * Fill out the *Message* box with a message identify yourself for the
     moderator of the VO

   * Upon submission, the moderator of the VO (somebody from the research
     group) will receive and review your request

.. _create_vo:

Creating a new VO
=================

.. warning:: VO requests from (PhD) students or postdocs will be rejected. Only
   group leaders (ZAP members) are allowed to create a VO.

Group leaders (ZAP members) can make a motivated request to the HPC team to
create a new VO for their research group:

#. Make sure you have an active VSC account

   If you don't yet have a VSC account yet, follow the instructions in
   :ref:`apply for account` to request it. The process is fairly easy if you
   don't need access to the HPC cluster; in that case it's not required to
   generate an SSH key pair.

#. Go to the section **Request new VO** in your `VSC Account - New/Join VO`_ page

   * Fill out the form below *'Why do you want to request a VO'*

   * Fill out both the internal and public VO names. These cannot contain
     spaces, and should be 8-10 characters long. For example, ``genome25`` is
     a valid VO name.

   * Fill out the rest of the form and press submit. This will send a message
     to the HPC administrators, who will then review your request

#. If the request is approved, you will now be a **member and moderator** of
   your newly created VO

Requesting more storage space
=============================

VO moderators can request additional quota for the VO and its members:

#. Go to the section **Request additional quota** in your
   `VSC Account - Edit VO`_ page

   * Fill out the amount of additional storage you want for the data
     storage of your VO (named ``VSC_DATA`` in this section) and/or the
     scratch storage of your VO (named ``VSC_SCRATCH_RHEA`` in this section)

   * Add a comment explaining why you need additional storage space and submit
     the form

#. Your request will be reviewed by the HPC administrators

Setting per-member VO quota
===========================

VO moderators can tweak the share of the VO quota that each member can
maximally use. By default, this is set to 50% for each user, but a moderator
can change this: it is possible to give a particular user more than half of the
VO quota (for example 80%), or significantly less (for example 10%).

#. Go to the section **Manage per-member quota share** in your
   `VSC Account - Edit VO`_ page

   * Fill out the share (%) of the available space you want each user to be
     able to use and press confirm

#. The per-member VO quota will be updated in 30 minutes maximum

.. note:: The total percentage per-member can be above 100%. The share for any
   user indicates what he/she can maximally use, but the actual limit will then
   depend on the usage of the other members. The total storage space of the VO
   will always be respected.

