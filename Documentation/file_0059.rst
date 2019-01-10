Access and data transfer
========================

Before you can really start using one of the clusters, there are several
things you need to do or know:

#. You need to log on to the cluster via an ssh-client to one of the
   login nodes. This will give you a command line. The software you'll
   need to use on your client system depends on its operating system:

   -  `Windows <\%22/client/windows#connecting\%22>`__
   -  `Linux <\%22/client/linux\%22>`__
   -  `macOS/OS X <\%22/client/macosx\%22>`__

#. Your account also comes with a certain amount of data storage
   capacity in at least three subdirectories on each cluster. You'll
   need to familiarise yourself with

   -  the storage policies: `where should which data be
      stored? <\%22/cluster-doc/access-data-transfer/where-store-data\%22>`__,
   -  and the `tools to check your disk
      usage <\%22/cluster-doc/account-management/managing-disk-usage\%22>`__.

#. Before you can do some work, you'll have to transfer the files that
   you need from your desktop or department to the cluster. At the end
   of a job, you might want to transfer some files back. The preferred
   way to do that, is by using an sftp client. It again requires some
   software on your client system which depends on its operating system:

   -  `Windows <\%22/client/windows#connecting\%22>`__
   -  `Linux <\%22/client/linux\%22>`__
   -  `macOS/OS X <\%22/client/macosx\%22>`__

#. Optionally, if you wish to use programs with a graphical user
   interface, you'll need an X server on your client system. Again, this
   depends on the latter's operating system:

   -  `Windows <\%22/client/windows\%22>`__
   -  `Linux <\%22/client/linux\%22>`__
   -  `macOS/OS X <\%22/client/macosx\%22>`__

#. Often several versions of software packages and libraries are
   installed, so you need to select the ones you need. To manage
   different versions efficiently, the VSC clusters use so-called
   modules, so you'll need to `select and load the modules that you
   need <\%22/cluster-doc/software/modules\%22>`__.

Logging in to the login nodes of your institute's cluster may not work
if your computer is not on your institute's network (e.g., when you work
from home). In those cases you will have to `set up a VPN (Virtual
Private Network)
connection <\%22/cluster-doc/access-data-transfer/vpn\%22>`__ if your
institute provides this service.

"
