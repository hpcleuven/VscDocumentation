.. _basic linux:

Basic Linux usage
=================

All the VSC clusters run the Linux operating system:

-  KU Leuven: Red Hat Enterprise Linux ComputeNode release 6.5
   (Santiago), 64 bit
-  UAntwerpen: CentOS 7.x
-  UGent: CentOS 7.x
-  VUB: CentOS 7.x

This means that, when you connect to one of them, you get a command line
interface, which looks something like this:

::

   vsc30001@login1:~>

When you see this, we also say you are inside a \\"shell\". The shell
will accept your commands, and execute them.

Some of the most often used commands include:

+------+----------------------------------------------------+
| ls   | Shows you a list of files in the current directory |
+------+----------------------------------------------------+
| cd   | Change current working directory                   |
+------+----------------------------------------------------+
| rm   | Remove file or directory                           |
+------+----------------------------------------------------+
| joe  | Text editor                                        |
+------+----------------------------------------------------+
| echo | Prints its parameters to the screen                |
+------+----------------------------------------------------+

Most commands will accept or even need parameters, which are placed
after the command, separated by spaces. A simple example with the 'echo'
command:

::

   $ echo This is a test
   This is a test

Important here is the \\"$\" sign in front of the first line. This
should not be typed, but is a convention meaning \\"the rest of this
line should be typed at your shell prompt\". The lines not starting with
the \\"$\" sign are usually the feedback or output from the command.

More commands will be used in the rest of this text, and will be
explained then if necessary. If not, you can usually get more
information about a command, say the item or command 'ls', by trying
either of the following:

::

   $ ls --help
   $ man ls
   $ info ls

(You can exit the last two \\"manuals\" by using the 'q' key.)

Tutorials
---------

For more exhaustive tutorials about Linux usage, please refer to the
following sites:



-  `Linux Tutorials YouTube Channel`_ 
-  `Linux Basics on Lifewire`_
-  `Linux Newbie Administrator Guide`_
-  We organise regular Linux introductory courses, see the
   `VSC website <VSC training_>`_. 

.. include:: links.rst 
