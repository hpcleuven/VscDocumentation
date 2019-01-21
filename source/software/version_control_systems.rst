.. _version control systems:

Version control systems
======================

Why use a version control system?
---------------------------------

A version control systems (VCS) help you manage the changes to the
source files of your project, and most systems also support team
development. Since it remembers the history of your files, you can
always return to an earlier version if you've screwed up making changes.
By adding comments when you store a new version in the VCS it also
becomes much easier to track which change was made for what purpose at
what time. And if you develop in a team, it helps to organise making
coordinated changes to the code base, and it supports co-development
even across file system borders (e.g., when working with a remote
partner).

Most Integrated Development Environments (IDE) offer support for one or
more version control systems. E.g., Eclipse, the IDE which we recommend
for the development of C/C++ or Fortran codes on clusters, supports all
of the systems mentioned on this page, some out-of-the-box and others by
adding an additional package. The systems mentioned on this page are all
available on Linux, OS X and Windows (through the UNIX emulation layer
cygwin and all except RCS also in at least one native implementation).

Types of version control systems
--------------------------------

An excellent introduction to the various types of version control
systems can be found in `the book Pro GIT by Scott Chacon and Ben
Straub <\%22https://git-scm.com/book/en/v2\%22>`__.

Local systems
~~~~~~~~~~~~~

These first generation systems use a local database that stores previous
versions of files. One of the most popular examples of this type is the
venerable RCS (Revision Control System) system, distributed with many
UNIX-like systems. It works by keeping patch sets (differences between
various versions of a file) in a special format on disk. It can then
return to a previous version of a file by adding up all the patches.

RCS and other \\"local systems\" are very outdated. Hence we advise you
to use one of the systems from the next two categories.

Links:

-  `Wikipedia
   page <\%22https://en.wikipedia.org/wiki/Revision_Control_System\%22>`__
-  `GNU RCS <\%22https://www.gnu.org/software/rcs/rcs.html\%22>`__

Centralised systems
~~~~~~~~~~~~~~~~~~~

Centralised version control systems were developed to enable people to
collaborate on code and documents with people on different systems that
may not share a common file system. The version files are now maintained
by a server to which multiple clients can connect and check out files,
and the systems help to manage concurrent changes to a file by several
users (through a copy-modify-merge procedure). Popular examples of this
type are CVS (Concurrent Versions System) and SVN (Subversion). Of those
two, SVN is the more recent system while CVS is no longer further
developed and less and less used.

Links:

-  `CVS Wikipedia
   page <\%22https://en.wikipedia.org/wiki/Concurrent_Versions_System\%22>`__
-  `SVN Wikipedia
   page <\%22https://en.wikipedia.org/wiki/Apache_Subversion\%22>`__
-  CVS implementations

   -  A command-line client is included in most Linux distributions. On
      Windows, the cygwin UNIX emulation layer also has a svn package.
      On OS X, it is available (though no longer maintained) through the
      MacPorts project.
   -  The eclipse IDE comes with built-in support for CVS.

-  SVN implementations

   -  Command-line clients are included in most Linux distributions and
      OS X. On Windows, the cygwin UNIX emulation layer also has a svn
      package. The command line client is also available on the VSC
      clusters.
   -  `TortoiseSVN <\%22/client/windows/tortoisesvn\%22>`__ (or `go
      straight to the TortoiseSVN web
      site <\%22https://tortoisesvn.net/\%22>`__) is a popular Windows
      native GUI client that integrates well with the explorer. However,
      if you google on \\" SVN GUI\" you'll find a plethora of other
      choices, not only for Windows but also for macOS and Linux
   -  SVN can be integrated with the eclipse IDE through the ¨Subversive
      SVN team provider¨ plugin which can be installed through the
      \\"Install New Software\" panel in the help menu. More information
      and instructions are available on the `subversive subsite of the
      main eclipse web
      site <\%22http://www.eclipse.org/subversive/\%22>`__.

Distributed systems
~~~~~~~~~~~~~~~~~~~

The weak point of the centralised systems is that they require you to be
online to checkout a file or to commit a revision. In a distributed
system, the clients mirror the complete repository and not just the
latest version of each file. When online, the user can then synchronise
the local repository with the copy on a server. In a single-user
scenario you can still keep all your files in the local repository
without using a server, and hence it doesn't make sense anymore to still
use one of old local-only version control systems. The disadvantage of a
distributed system is that you are not forced to synchronise after every
commit, so that the local repositories of various users on a project can
be very much out-of-sync with each other, making the job harder when
those versions have to be merged again.

Popular examples of systems of this type are Git (originally developed
to manage the Linux kernel project) and Mercurial (sometimes abbreviated
as Hg, chemists will understand why).

Links:

-  `Git on
   Wikipedia <\%22https://en.wikipedia.org/wiki/Git_(software)\%22>`__
-  `Main Git web page <\%22https://git-scm.com/\%22>`__
-  `Mercurial on
   Wikipedia <\%22https://en.wikipedia.org/wiki/Mercurial\%22>`__
-  `Main Mercural web page <\%22https://www.mercurial-scm.org\%22>`__
-  Git implementations

   -  If you have a Linux system, Git is most likely already installed
      on your system. On OS X, git is available through Xcode, though it
      is not always the most recent version. On Windows, there is a
      Git-package in the UNIX emulation layer Cygwin. Downloads for all
      systems are also available on `the download section of the main
      git web site <\%22https://git-scm.com/download\%22>`__. That page
      also contains links to a number of GUI options. Most if not all
      GUI tools store projects in a way that is fully compatible with
      the command line tools, so you can use both simultaneously. The
      command line client is also available on the VSC clusters.
   -  `TortoiseGit <\%22https://tortoisegit.org/\%22>`__ is an
      explorer-integrated interface to Git on Windows similar to
      TortoiseSVN.
   -  Another nice GUI application is
      `SourceTree <\%22https://www.atlassian.com/software/sourcetree\%22>`__
      produced by `Atlassian <\%22https://www.atlassian.com/\%22>`__.
      Atlassian is the company behind the Bitbucket cloud service, but
      their tool also works well with GitHub, one of their main
      competitors. It has a very nice way of representing the history of
      a local repository.
   -  The Eclipse IDE comes with built-in support for Git through the
      standard plug-in EGit. More recent versions of this plugin may be
      available through the `Eclipse
      Marketplace <\%22https://marketplace.eclipse.org/\%22>`__.
   -  `CollabNet
      GitEye <\%22https://www.collab.net/products/giteye\%22>`__ is a
      Git GUI for Windows, OS X and Linux build on top of a number of
      Eclipse libraries, but you don/t need to install Eclipse to be
      able to use it. It is a nice way though to browse through your Git
      repositories outside of the Eclipse environment. GitEye itself is
      free and integrates with several git cloud services and
      bugtracking services.

-  Mercurial (Hg) implementations

   -  Mercurial is written in Python and hence runs on most systems.
      Most Linux distributions offer a mercurial package. `Windows and
      OS X command line utilities are also
      available <\%22https://www.mercurial-scm.org/\%22>`__.
   -  `TortoiseHg <\%22https://tortoisehg.bitbucket.io/\%22>`__ is an
      explorer-integrated interface to the Mercurial VCS on Windows
      similar to TortoiseSVN. There is also an OS X and Linux version
      available. The latter integrates with Gnome/Nautilus.
   -  The eclipse IDE supports Mercurial through the `optional
      MercurialEclipse
      plugin <\%22https://marketplace.eclipse.org/content/mercurialeclipse\%22>`__
      available on the `Eclipse
      Marketplace <\%22https://marketplace.eclipse.org/\%22>`__.

Cloud services
--------------

Many companies offer hosting services for SVN, Git or Mercurial
repositories in the cloud. Google, e.g., for `subversion hosting
service <\%22https://www.google.be/webhp?#q=subversion+hosting+service\%22>`__,
`git hosting
service <\%22https://www.google.be/search?q=git+hosting+service\%22>`__
or `mercurial hosting
service <\%22https://www.google.be/search?q=mercurial+hosting+service\%22>`__.
Several offer free public hosting for Open Source projects or have free
access for academic accounts. Some noteworthy ones that are popular for
academic projects are:

-  `Github (github.com) <\%22https://github.com/\%22>`__ offers free Git
   and Subversion hosting for Open Source projects. We use this service
   for some VSC in-house tools development. It is also possible to host
   private projects if you subscribe to one of their paying plans.
-  `Bitbucket (bitbucket.org) <\%22https://bitbucket.org/\%22>`__ offers
   both git and mercurial services. It also supports private projects
   with a limited number of users in free accounts (and has a special
   deal for academic institutions, allowing unlimited users) while the
   other services mentioned on this page only support open source
   projects for free.
-  `SourceForge <\%22https://sourceforge.net/\%22>`__ is a very well
   known service for hosting Open Source projects. It currently supports
   projects managed through Subversion, Git, Mercurial and a few other
   systems.

However, we urge you to always carefully check the terms-of-use of these
services to assure that, e.g., the way they deal with intellectual
property is in line with your institute's requirements.

Which one should I use?
-----------------------

It is not up to us to make this choice for you, but here are a number of
elements that you should take into account:

-  Subversion, Git and Mercurial are all recent systems that are well
   maintained and supported by several hosting services.
-  Subversion and Git are installed on most VSC systems. We use Git
   ourselves for some of our in-house development.
-  Centralised version management systems have a simpler concept than
   the distributed ones, but if you expect prolonged periods that you
   are offline, you have to keep in mind that you cannot make any
   commits during that period.
-  As you have only a single copy of the repository in a centralised
   system, a reliable hosting service or a good backup strategy is
   important. In a distributed system it would still be possible to
   reconstruct the contents of a repository from the other repositories.
-  If you want to use an IDE, it is good to check which systems are
   supported by the IDE. E.g., Eclipse supports Git out-of-the-box, and
   Subversion and Mercurial though a plug-in. Visual Studio also
   supports all three of these systems.

"
