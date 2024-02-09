.. _mfa_leuven:

Multi Factor Authentication (MFA)
=================================

|KUL| Multi Factor Authentication (MFA) is an augmented level of security which, as
the name suggests, requires multiple steps when authenticating. The following
two factors are necessary to connect to the KU Leuven clusters:

- A valid private key (except when connecting via :ref:`Open OnDemand portal<ood_t2_leuven>`)
- Access to a VSC-associated university/institution account

This approach ensures that if your private key is compromised, the person who
has unauthorized access to it will still not be able to abuse your VSC account.
This document provides two methods to connect to the KU Leuven clusters with
MFA. The first method, *without* an agent, is easier to get started with, but requires
some repetitive steps with each connection. The second method, *with* an agent,
requires some more effort to set up initially but will be easier when you need
multiple connections or you are using some specific GUI applications to connect. 

.. toctree::

  mfa_quickstart
  mfa_guide

