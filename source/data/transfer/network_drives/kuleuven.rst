.. _KU Leuven network drives:

#########################################
Data transfer on KU Leuven network drives
#########################################

On clusters hosted at KU Leuven it is possible to transfer data to
and from KU Leuven network drives to which you may have access.
These need to be accessed through the CIFS protocol and there are
different tools that can be used for this purpose. Here we will
describe ``GIO`` and ``smbclient``.

In these instructions you will need to replace ``unumber`` with your
u-number and ``drivename`` with the drive you want to access:

- ``users`` for the personal network drive (I-drive)
- ``shares`` for the shared network drive (J-drive)
- ``lvs`` for the Large Volume Storage (L-drive)

.. note::

   The location of your I-drive will not correspond to the mount point
   itself, but to a ``unumber`` subdirectory of the mount point.

GIO
===

Mounting the drives via GIO can be convenient but only works on specific
login nodes and not on the compute nodes. Keep in mind that the CPU time
limitations on the login nodes may cause long transfers to get interrupted.
GIO can be used both via a GUI and the CLI.

.. note::

   Don't forget to unmount the drives after your transfers have finished.

Via the GUI (NoMachine)
-----------------------

#. Open a NoMachine connection (see the :ref:`NX start guide<NX start guide>`)
#. Click on e.g. ``Places`` -> ``Home Folder`` to open the default file
   manager (Thunar).
#. Replace the ``/user/...`` location with
   ``smb://unumber@shares.kuleuven.be/drivename``
   (substituting ``unumber`` and ``drivename`` as explained above).
#. When asked for the password for your account, also change the
   domain name from ``SAMBA`` to ``luna``.
#. The file manager will now show the contents of the drive.
   Mounted drives will remain visible in the file manager's Network section
   in the panel on the left.
#. To unmount the drive afterwards, right-click on the drive name in the
   Network section and select ``Unmount``.

Via the CLI
-----------

#. Open an SSH connection to ``login3-tier2.hpc.kuleuven.be`` or
   ``login4-tier2.hpc.kuleuven.be`` or start a terminal in your NoMachine
   session.
#. Start a D-Bus session and then mount the network drive::

     dbus-run-session bash
     gio mount smb://unumber@shares.kuleuven.be/drivename

#. When asked for the domain name, enter ``luna``.
#. When asked for a password, enter your u-number password.
#. File transfers also need to happen via ``gio``, e.g.::

     gio copy /path/to/local/dir/file.txt smb://unumber@shares.kuleuven.be/drivename/path/to/remote/dir/

#. To unmount the drive afterwards, repeat the same ``gio mount`` command
   with an additional ``--unmount`` flag.

smbclient
=========

Larger transfers are best done via a job on a compute node, where ``GIO`` is not
available and ``smbclient`` can be used instead.

.. note::

   This specifically needs to happen via an interactive job, not in batch jobs.
   The reason is that you need to provide your u-number password, which we strongly
   recommend to **never** store in text files such as a job script.

Using ``smbclient`` is similar to :ref:`sftp<scp and sftp>`. You can for example
launch an interactive prompt like this::

  smbclient --user=unumber --workgroup=luna \\\\shares.kuleuven.be\\drivename
  Enter LUNA\unumber's password:
  smb: \>

It can sometimes be more convenient to pass a set of commands instead of using
the prompt. For example::

  cd $VSC_SCRATCH
  smbclient --user=unumber --workgroup=luna \\\\shares.kuleuven.be\\drivename \
            -c "cd /path/to/remote/dir/; get file.txt"

Limitations
===========

Because the network drives need to be accessed via the CIFS protocol, it is
not possible to transfer all file attributes from Unix-like file systems.
File ownerships, permissions and symlinks can for example not be transferred.

If it is necessary to retain all metadata, an easy workaround is to first create
an (compressed or uncompressed) archive and then transfer this archive file::

  tar -cv --file=archive.tar /path/to/directory

For large directories it can be convenient to split the archive into smaller chunks,
for example::

  tar -cv -M -L 10G --file=archive.tar.{000..100} /path/to/directory

Afterwards the directory can be reconstructed as follows::

  tar -xv -M --file=../archive.tar.{000..100}

