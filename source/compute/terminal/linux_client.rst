.. _linux_client:

########################################
:fab:`linux` Terminal Interface on Linux
########################################

If you are using a Linux system on your own computer, then you already have all
the tools to start a terminal interface on the VSC clusters. You just need to
open your favorite terminal and the ``ssh`` command, which is available by
default on most Linux distributions.

All VSC clusters run on a :ref:`terminal linux system` as well, so you will
find at ease once you connect to our clusters. Most commands will work in the
same way as they do on your computer. The biggest difference you might
experience is just that you are a regular user on the VSC cluster without
superuser (*root*) permissions.

Getting ready to login
======================

Before you can log in to a VSC cluster using SSH, you need to
check which authentication method the cluster supports.

For clusters that support :ref:`mfa_login`, SSH keys are not required.

For clusters that do not support MFA, you need to generate an SSH key pair and
upload the public key to your VSC account on your your `VSC Account - Edit
Account`_ page before logging in. You can generate SSH keys on Linux using
`OpenSSH`_. See :ref:`generating keys linux` for instructions.


Connecting to the cluster
=========================

OpenSSH
    `OpenSSH`_ is a reputable suite of secure networking utilities based on the
    `Secure Shell`_ (SSH) protocol. OpenSSH is open-source software and is readily
    available on all popular Linux distributions, and most often installed by
    default as well.

    .. toctree::
       :maxdepth: 2

       openssh_access

