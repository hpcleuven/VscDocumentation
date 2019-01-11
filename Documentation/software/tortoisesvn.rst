TortoiseSVN
===========

Installation & setup
--------------------

#. `Download <\%22https://tortoisesvn.net/downloads.html\%22>`__ the
   approriate version for your system (32- or 64-bit) and install it.
   You may to reboot to complete the installation, do so if required.
#. Optionally, but highly recommended:
   `download <\%22http://winmerge.org/downloads/\%22>`__ and install
   `WinMerge <\%22http://winmerge.org/\%22>`__, a convenient GUI tool to
   compare and merge files.
#. Start Pageant (the SSH agent that comes with PuTTY) and load your
   private key for authentication on the VSC cluster.

Checking out a project from a VSC cluster repository
----------------------------------------------------

::

   svn+ssh://userid@svn.login.node/data/leuven/300/vsc30000/svn-repo/simulation/trunk

#. Open Windows Explorer (by e.g., the Windows-E shortcut, or from the
   Start Menu) and navigate to the directory where you would like to
   check out your project that is in the VSC cluster repository.
#. Right-click in this directory, you will notice 'SVN Checkout...' in
   the context menu, select it to open the 'Checkout' dialog.
   |\\"TortoiseSVN|
#. In the 'URL of repository' field, type the following line, replacing
   userid by your VSC user ID, and '300' with '301', '302',... as
   required (e.g., for user ID 'vsc30257', replace '300' by '302'). For
   svn.login.node, substitute the appropriate login node for the cluster
   the repository is on.
#. Check whether the suggested default location for the project suits
   you, i.e., the 'Checkout directory' field, if not, modify it.
#. Click 'OK' to proceed with the check out.

You now have a working copy of your project on your desktop and can
continue to develop locally.

Work cycle
----------

| Suppose the file 'simulation.c' is added, and 'readme.txt' is added.
  The 'simulation directory will now look as follows:
| |\\"TortoiseSVN|

Files that were changed are marked with a red exclamation mark, while
those marked in green were unchanged. Files without a mark such as
'readme.txt' have not been placed under version control yet. The latter
can be added to the repository by right-clicking on it, and choosing
'TortoiseSVN' and then 'Add...' from the context menu. Such files will
be marked with a bleu '+' sign until the project is committed.

| By right-clicking in the project's directory, you will see context
  menu items 'SVN Update' and 'SVN Commit...'. These have exactly the
  same semantics as their command line counterparts introduced above.
  The 'TortoiseSVN' menu item expands into even more command that are
  familiar, with the notable exception of 'Check for modifications',
  which is in fact equivalent to 'svn status'.
| |\\"Tortoise|

| Right-clicking in the directory and choosing 'SVN Commit...' will
  bring up a dialog to enter a comment and, if necessary, include or
  exclude files from the operation.
| |\\"TortoiseSVN|

Merging
-------

When during an update a conflict that can not be resolved automatically
is detected, TortoiseSVN behaves slightly different from the command
line client. Rather than requiring you to resolve the conflict
immediately, it creates a number of extra files. Suppose the repository
was at revision 12, and a conflict was detected in 'simulation.c', then
it will create:

-  'simulation.c': this file is similar to the one subversion would open
   for you when you choose to edit a conflict via the command line
   client (this file is marked with a warning sign);
-  'simulation.c.mine': this is the file in your working copy, i.e., the
   one that contains changes that were not committed yet;
-  'simulation.c.r12': the last revision in the repository; and
-  'simulation.c.r11': the previous revision in the repository.

You have now two options to resolve the conflict.

#. Edit 'simulation.c', keeping those modification of either version
   that you need.
#. Use WinMerge to compare 'simulation.c.mine' and 'simulation.c.r12'
   and resolve the conflicts in the GUI, saving the result as
   'simulation.c'. When two files are selected in Windows Explorer, they
   can be compared using WinMerge by right-clicking on either, and
   choosing 'WinMerge' from the context menu.
   |\\"WinMerge|

Once all conflicts have been resolved, commit your changes.

Tagging
-------

Tagging can be done conveniently by right-clicking in Windows Exploerer
and selecting 'TortoiseSVN' and then 'Branch/tag...' from the context
menu. After supplying the appropriate URL for the tag, e.g.,

::

   svn+ssh://<user-id>@<login-node>/data/leuven/300/vsc30000/svn-repo/simulation/tag/nature-submission

you click 'OK'.

Browsing the repository
-----------------------

Sometimes it is convenient to browse a subversion repository.
TortoiseSVN makes this easy, right-click in a directory in Windows
Explorer, and select 'TortoiseSVN' and then 'Repo-browser' from the
context menu.

| 
| |\\"TortoiseSVN|

Importing a local project into the VSC cluster repository
---------------------------------------------------------

| As with the command line client, it is possible to import a local
  directory on your desktop system into your subversion repository on
  the VSC cluster . Let us assume that this directory is called
  'calculation'. Right-click on it in Windows Explorer, and choose
  'Subversion' and then 'Import...' from the context menu. This will
  open the 'Import' dialog.
| |\\"TortoiseSVN|

The repository's URL would be (modify the user ID and directory
appropriately):

::

   svn+ssh://<user-id>@<login-node>/data/leuven/300/vsc30000/svn-repo/calculation/trunk

TortoiseSVN will automatically create the 'calculation' and 'trunk'
directory for you (it uses the '--parents' option).

Creating directories such as 'branches' or 'tags' can be done using the
repository browser. To invoke it, right-click in a directory in Windows
Explorer and select 'TortoiseSVN' and then 'Repo-browser'. Navigate to
the appropriate project directory and create a new directory by
right-clicking in the parent directory's content view (right pane) and
selecting 'Create folder...' from the context menu.

"

.. |\\"TortoiseSVN| image:: \%22/assets/171\%22
.. |\\"TortoiseSVN| image:: \%22/assets/173\%22
.. |\\"Tortoise| image:: \%22/assets/175\%22
.. |\\"TortoiseSVN| image:: \%22/assets/177\%22
.. |\\"WinMerge| image:: \%22/assets/179\%22
.. |\\"TortoiseSVN| image:: \%22/assets/181\%22
.. |\\"TortoiseSVN| image:: \%22/assets/183\%22

