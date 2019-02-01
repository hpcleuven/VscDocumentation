.. _scp and sftp:

Data transfer with scp/sftp
===========================

Prerequisite: OpenSSH
---------------------

See the page on :ref:`generating keys <generating keys linux>`.

Using scp
---------

Files can be transferred with scp, which is more or less a cp
equivalent, but then to or from a remote machine.

For example, to copy the (local) file localfile.txt to your home
directory on the cluster (where <vsc-loginnode> is a loginnode), use:

::

   scp localfile.txt <vsc-account>@<vsc-loginnode>:

Likewise, to copy the remote file remotefile.txt from your home
directory on the cluster to your local computer, use:

::

   scp <vsc-account>@<vsc-loginnode>:localfile.txt .

The colon is required!

Using sftp
----------

The sftp is an equivalent of the ftp command, but it uses the secure ssh
protocol to connect to the clusters.

One easy way of starting a sftp session is

::

   sftp <vsc-account>@<vsc-loginnode>

Links
-----

-  `scp manual page`_ (external)
-  `sftp manual page`_ (external)

.. include:: links.rst
