Using Pageant
=============

Getting started with Pageant
----------------------------

`Pageant <\%22https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html\%22>`__
is an SSH authentication agent that you can use for Putty and Filezilla.
Before you run Pageant, you need to have a private key in PKK format
(filename ends on ``.pkk``). See `our page on generating keys with
PuTTY <\%22/client/windows/keys-putty\%22>`__ to find out how to
generate and use one. When you run Pageant, it will put an icon of a
computer wearing a hat into the System tray. It will then sit and do
nothing, until you load a private key into it. If you click the Pageant
icon with the right mouse button, you will see a menu. Select ‘View
Keys’ from this menu. The Pageant main window will appear. (You can also
bring this window up by double-clicking on the Pageant icon.) The
Pageant window contains a list box. This shows the private keys Pageant
is holding. When you start Pageant, it has no keys, so the list box will
be empty. After you add one or more keys, they will show up in the list
box.

To add a key to Pageant, press the ‘Add Key’ button. Pageant will bring
up a file dialog, labelled ‘Select Private Key File’. Find your private
key file in this dialog, and press ‘Open’. Pageant will now load the
private key. If the key is protected by a passphrase, Pageant will ask
you to type the passphrase. When the key has been loaded, it will appear
in the list in the Pageant window.

Now start PuTTY (or Filezilla) and open an SSH session to a site that
accepts your key. PuTTY (or Filezilla) will notice that Pageant is
running, retrieve the key automatically from Pageant, and use it to
authenticate. You can now open as many PuTTY sessions as you like
without having to type your passphrase again.

When you want to shut down Pageant, click the right button on the
Pageant icon in the System tray, and select ‘Exit’ from the menu.
Closing the Pageant main window does *not* shut down Pageant.

You can find more info `in the on-line
manual <\%22http://the.earth.li/~sgtatham/putty/0.63/htmldoc/Chapter9.html\%22>`__.

| *SSH authentication agents are very handy as you no longer need to
  type your passphrase every time that you try to log in to the cluster.
  It also implies that when someone gains access to your computer, he
  also automatically gains access to your account on the cluster. So be
  very careful and lock your screen when you're not with your computer!
  It is your responsibility to keep your computer safe and prevent easy
  intrusion of your VSC-account due to an obviously unprotected PC!*

"
