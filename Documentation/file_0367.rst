Eclipse with PTP and version control
====================================

*If you're not familiar with Eclipse, read*\ `our introduction
page <\%22/client/multiplatform/eclipse-intro\%22>`__\ *first.*

Eclipse also supports several version control systems out of the box or
through optional plug-ins.

The PTP (Parallel Tools Platform) strongly encourages a model where you
run eclipse locally on your workstation and let Eclipse synchronise the
project files with your cluster account. If you want to use version
control in this scenario, the PTP manual advises to put your *local*
files under version control (which can be done through Eclipse also) and
synchronise that with some remote repository (e.g., one of the hosting
providers), and to not put the automatically synchronised version of the
code that you use for compiling and running on the cluster also under
version control. In other words,

-  The version control system is used to version manage your files on
   your local workstation,
-  And Eclipse PTP is then used to manage the files on the cluster.

If you still want to use the cluster file space as a remote repository,
we strongly recommend that you do this in a different directory from
where you let Eclipse synchronise the files, and don't touch the files
in that repository directly.

For experts
-----------

The synchronised projects feature in Eclipse internally uses the Git
version control system to take care of the synchronisation. That's also
the reason why the Parallel Software Development bundle of Eclipse comes
with the EGit plug-in included. It does this however in a way that does
not interfere with regular git operations. In both your local and remote
project directory, you'll find a hidden .ptp-sync directory which in
fact is a regular git repository, but stored in a different subdirectory
rather than the standard .git subdirectory. So you can still have a
standard Git repository besides it and they will not interfere if you
follow the guidelines on this page.

"
