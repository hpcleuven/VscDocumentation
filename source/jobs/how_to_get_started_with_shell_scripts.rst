How to get started with shell scripts
=====================================

Shell scripts
-------------

Scripts are basically uncompiled pieces of code: they are just text
files. Since they don't contain machine code, they are executed by what
is called a "parser" or an "interpreter". This is another program
that understands the command in the script, and converts them to machine
code. There are many kinds of scripting languages, including Perl and
Python.

Another very common scripting language is shell scripting. In a shell
script, you will put the commands you would normally type at your shell
prompt in the same order. This will enable you to execute all those
commands at any time by only issuing one command: starting the script.

Typically in the following examples they'll have on each line the next
command to be executed although it is possible to put multiple commands
on one line. A very simple example of a script may be:

::

   echo \"Hello! This is my hostname:\"
   hostname

You can type both lines at your shell prompt, and the result will be the
following:

::

   $ echo \"Hello! This is my hostname:\"
   Hello! This is my hostname:
   $ hostname
   login1

Suppose we want to call this script ``myhostname``. You open a new file
for editing, and name it ``myhostname``:

::

   $ nano myhostname

You get a \\"New File\", where you can type the content of this new
file. Help is available by pressing the 'Çtrl+G' key combination. You
may want to familiarize you with the other options at some point; now we
will just type the content of the file, save it and exit the editor.

You can type the content of the script:

::

   echo \"Hello! This is my hostname:\"
   hostname

You save the file and exit the editor by pressing the 'Ctrl+x' key
combination. Nano will ask you if you want to save the file. You should
be back at the prompt.

The easiest way to run a script is by starting the interpreter and pass
the script as parameter. In case of our script, the interpreter may
either be ``sh`` or ``bash`` (which are the same on the cluster). So start
the script:

::

   $ bash myhostname
   Hello! This is my hostname:
   login1

Congratulations, you just created and started your first shell script!

A more advanced way of executing your shell scripts is by making them
executable by their own, so without invoking the interpreter manually.
The system can not automatically detect which interpreter you want, so
you need to tell this in some way. The easiest way is by using the so
called \\"shebang\"-notation, explicitly created for this function: you
put the following line on top of your shell script
\\"#!/path/to/your/interpreter\".

You can find this path with the ``which`` command. In our case, since
we use bash as an interpreter, we get the following path:

::

   $ which bash
   /bin/bash

We edit our script and change it with this information:

::

   #!/bin/bash
   echo \"Hello! This is my hostname:\"
   hostname

Note that the \\"shebang\" must be the first line of your script! Now
the operating system knows which program should be started to run the
script.

Finally, we tell the operating system that this script is now
executable. For this we change its file attributes:

::

   $ chmod +x myhostname

Now you can start your script by simply executing it:

::

   $ ./myhostname
   Hello! This is my hostname:
   login1

The same technique can be used for all other scripting languages, like
Perl and Python.

Most scripting languages understand that lines beginning with \\"#\" are
comments, and should be ignored. If the language you want to use does
not ignore these lines, you may get strange results...

Links
-----

-  `Nano manual <https://www.nano-editor.org/dist/v2.0/nano.html>`__
