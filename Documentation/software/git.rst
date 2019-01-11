Git
===

This tutorial explains some of the basic use of the git command line
client. It does not aim to be a complete tutorial on git but rather a
brief introduction explaining some of the issues and showing you how to
house your git repository at the VSC. At the end of this text, we
provide some links to further and more complete documentation.

Preparing your local machine for using git
------------------------------------------

It is best to first configure git on your local machine using git
config.

::

   git config --global user.name \"Kurt Lust\"
   git config --global user.email kurt.lust@uantwerpen.be
   git config --global core.editor vi

These settings are stored in the file .gitconfig in your home directory
(OS X, Linux, Cygwin). The file is a simple user-editable text file.

Some remarks on accessing a remote repository using command line tools
----------------------------------------------------------------------

Many cloud git hosting services offer a choice between ssh and https
access to a repository through the git command line tools. If you want
to use one of the VSC clusters for a remote repository, you'll have to
use the ssh protocol.

Https access
~~~~~~~~~~~~

Https access uses your account and password of the cloud service. Every
time you access the remote repository, the git command-line client will
ask for the password. This can be solved by using a credential manager
in recent versions of the git client (1.7.9 and newer).

-  On Windows, the `Git Credential Manager for
   Windows <\%22https://github.com/Microsoft/Git-Credential-Manager-for-Windows\%22>`__
   can be used to safely store your password in the Windows credential
   store.
-  The Apple OS X version of git comes with the credential manager comes
   with credential-osxkeychain to store your credentials in the OS X
   keychain. Enable it using
   ``git config --global credential.helper osxkeychain``
-  There are also various solutions for Linux systems, e.g., using the
   gnome keyring. To tell git to use it, use:
   ``git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring``
   This of course depends on the setup of your Linux machine. The
   program might not be installed or might be installed in a different
   directory.
-  Various GUI clients may have their own way of managing the
   credentials.

Ssh access
~~~~~~~~~~

The git command line client uses the standard ssh mechanism to manage
ssh keys. It is sufficient to use an ssh agent (as you are probably
using already when you log on to the VSC clusters) and load the key for
the service in the agent (using ssh-add).

Setting up a new repository
---------------------------

Getting an existing code base into a local repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git stores its repository with your code in a hidden directory.

#. Go to the top directory of what has to become your repository (most
   likely the top directory of the files that you want to version
   control) and run ``git init`` This wil create a hidden .git
   subdirectory with the local repository database.
#. Now you can add the files to your new repository, e.g., if you want
   to add all files ``git add .`` (don't forget the dot at the end, it
   means add the current directory!)
#. Next you can do your first commit:
   ``git commit -m \"Project brought under Git control\"``
#. And you're done! The current version of your files is now stored in
   your local repository. Try, e.g., ``git show``
   ``git status`` to get some info about the repository.

Bringing an existing local repository into a cloud service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we assume that you have a local repository and now want to put it
into a cloud service to collaborate with others on a project.

*You may want to make a backup of your local repository at this point in
case things go wrong.*

#. Create an empty project on your favorite cloud service. Follow the
   instructions provided by the service.
#. Now you'll need to learn your local repository about the remote one.
   Most cloud services have a button to show you the URL to the remote
   repository that you have just set up, either using the http or the
   ssh-based protocol. E.g.,
   ``git remote add origin ssh://git@bitbucket.org/username/myproject.git``
   connects to the repository myproject on Bitbucket. It will be known
   on your computer with the short name origin. The short name saves you
   from having to use the full repository URL each time you want to
   refer to it
#. Push the code from your local repository into the remote repository.
   ``git push -u --mirror origin`` will create a mirror of your local
   repository on the local site. Use the --mirror option with care, as
   it may destroy part of your remote repositiory if that one is not
   empty and contains information that is not contained in your local
   repository!

You can also use the procedure to create a so-called bare remote
repository in your account on the VSC clusters. A bare repository is a
repository that does not also contain its own source file tree, so you
cannot edit directly in that directory and also use it as a local
repository on the cluster. However, you can push to and pull from that
repositiory, so it will work just like a repository on one of the
hosting services. The access to the repository will be through ssh. The
first two steps have to be modified:

#. To create an empty repository, log in to your home cluster and go to
   the directory where you want to store the repository. Now create the
   repository (assuming its name is repository-name):
   ``git init --bare repository-name`` This will create the directory
   repositiory-name that stores a lot of files which together are your
   git repository.
#. The URL to the repository will be of the form
   vscXXXXX@vsc.login.node:<full path to the repository>, e.g., if
   you're vsc20XYZ (a UANtwerpen account) and the repository is in the
   subdirectory testrepository of your data directory, the URL is
   vsc20XYZ@login.hp.uantwerpen.be:/data/antwerpen/20X/vsc20XYZ/testrepository.
   So use this URL in the git remote add command. You don't need to
   specify ssh:// in the URL if you use the scp-syntax as we did in this
   example above.

The access to this repository will be regulated through the file access
permissions for that subdirectory. Everybody who has read and write
access to that directory, can also use the repository (but using his/her
own login name in the URL of course as VSC accounts should not be shared
by multiple users).

NOTE: Technically speaking, git can also be used in full peer-to-peer
mode where all repos also have a source directory in which files can be
edited. It does require a good organisation of the work flow. E.g.,
different people in the team should not be working in the same branch as
one cannot push changes to a repo for the branch that is active (i.e.,
mirrored in the source files) as this may create an inconsistent state.
So our advise is that if you want to use the cluster as a git server and
also edit files on the cluster, you simply use two repositories: one
that you use as a local repository in which you also work and one that
is only used as a central repository to which various users push changes
to and pull changes from.

As a clone from an existing local or remote repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another way to create a new repository is from an existing repository on
your local machine or on a remote service. The latter is useful, e.g.,
if you want to join an existing project and create a local copy of the
remote repository on your machine to do your own work. This can be
accomplished through cloning of a repository, a very easy operation in
git as there is a command that combines all necessary steps in a single
command:

#. Go to the directory were you want to store the repository and
   corresponding source tree (in a subdirectory of that directory called
   directoryname).
#. You have to know the URL to the repository that you want to clone.
   But once you know the URL, all you need to do is
   ``git clone URL directoryname`` where you replace URL with the URL of
   the repository that you want to clone.

Note: If you start from scratch and want to use a remote repository in
one of the cloud services, it might be easiest to first a repository
over there using the instructions of the server system or cloud service,
and then clone that (even if it is still empty) to a local repository on
which you actually work.

Working with your local repository
----------------------------------

If you are only using a local repository, the basic workflow to add the
modifications to the git database is fairly simple:

#. Edit the files.
#. Add the modified files to the index using: ``git add filename`` This
   process is called staging.
#. You can continue to further edit files if you want and also stage
   them.
#. Commit all staged files to the repository: ``git commit`` Git will
   ask you to enter a message describing the commit, or you can specify
   a message with the ``-m`` option.

This is not very exciting though. Version control becomes really useful
once you want to return to a previous version, or create a branch of the
code to try something out or fix a bug without immediately changing the
main branch of the code (that you might be using for production use).
You can then merge the modifications back into you main code. Branching
and merging branches are essential in all this. In fact, if you use git
to collaborate with others you'll be confronted with branches sooner
rather than later. In fact, every git repository has at least one
branch, the main branch, as

``git status``

shows.

Assume you want to start a new branch to try something without affecting
your main code, e.g., because you also want to further evolve your main
code branch while you're working. You can create a branch (let's assume
we name it branch2) with

``git branch branch2``

And then switch to it with

``git checkout branch2``

Or combine both steps with

``git checkout -b branch2.``

You can then switch between this branch and the master branch with

``git checkout master``

and

``git checkout branch2``

at will and make updates to the active branch using the regular git add
and git commit cycle.

The second important operation with branches, is merging them back
together. One way to do this is with git merge. Assume you want to merge
the branch branch2 back in the master branch. You'd do this by first
switching to the master branch using

``git checkout master``

and then ask git to merge both branches:

``git merge branch2``

Git will do a good effort to merge both sets of modifications since
their common ancestor, but this may not always work, especially if
you've made changes to the same area of a file on both branches. Git
will then warn you that there is a conflict for certain files, after
which you can edit those files (the conflicts zones will be clearly
marked in the files), add them to the index and commit the modifications
again.

When learning to work with this mechanism, it is very instructive to use
a GUI that depicts all commits and branches in a graphical form, e.g.,
the program SourceTree mentioned before.

Synchronising with a remote repository
--------------------------------------

If you want to collaborate with other people on a project, you need
multiple repositories. Each person has his or her own local repository
on his or her computer. The workflow is the simplest if you also have a
repository that is used to collect all contributions. The collaboration
mechanism though synchronisation of repositories relies very much on the
branching mechanism to resolve conflicts if several contributors have
made modifications to the repository.

-  To push modifications that you have made in your local repository to
   a different repository, use ``git push -u remote_name`` where you
   replace remote_name with the shorthand for the remote repository.
   This process may fail however if someone else had made modifications
   to the same branch in the repository that you're pushing. Git will
   then warn you and ask you to first fetch the modifications that
   others have made and merge them into your code before trying another
   pull.
-  The opposite of push is fetch and merge or pull. You'll need to do
   this to see and integrate modifications that others have made to the
   repository. The first step is to update your repository with the
   contents of the remote repository. Assume the remote repository has
   the shorthand name origin. ``git fetch origin`` will get all the
   information from the repositiory origin in your local repositiory,
   but it will not change your work files. If you try ``git branch -av``
   To get an overview of all branches in your local repository and
   information about the latest commit for each branch, you'll see that
   there might be a number of branches with a name that starts with
   origin/ in the repository. That means that there were commits in the
   remote repository that were newer than the data you last synchronised
   with, and you'll need to merge them into your working code base.
   E.g., if you're working on the branch master and someone else has
   made changes to that branch also, there will now be a branch
   origin/master in your repository with a more recent commit. You merge
   it again into your code with ``git merge origin/master`` (and you may
   have to resolve some conflicts here which you'd have to resolve and
   commit as before).
-  After a git fetch you may also note that someone else has added a new
   branch. Assume, e.g., that git branch -av tells you there is now a
   branch origin/branch3 and that you want to collaborate to that branch
   also. Before you can do so, you'll first have to create a local
   so-called tracking branch, by using
   ``git checkout -b branch3 origin/branch3`` which will also switch to
   that branch and update the files in your workspace accordingly, or if
   you just want to create the tracking branch for later use without
   switching to it now, ``git branch branch3 origin/branch3``

Further information
-------------------

We have only covered the bare essentials of git (and even less then
that). Due to its power, it is also a fairly complicated system to use.
If you want to know more about git or need a more complete tutorial, we
suggest you check out the following links:

-  There are some good books about git freely available on the internet:

   -  `Git Pro <\%22https://git-scm.com/book/en/v2\%22>`__
   -  `Git
      Workflows <\%22http://documentup.com/skwp/git-workflows-book\%22>`__
   -  `PeepCode Git
      Internals <\%22https://github.com/pluralsight/git-internals-pdf/releases\%22>`__

-  There is also a `full command reference available on the
   web <\%22https://git-scm.com/docs\%22>`__ for the command-line git
   tool.
-  And you can also find good git tutorials on the web, e.g., on `the
   \\"External Links\" page of the main git web
   site <\%22https://git-scm.com/doc/ext\%22>`__.

"
