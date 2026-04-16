.. _Perl packages:

Perl package management
=======================

Introduction
------------

(**Note:** *the Perl community uses the term 'modules' rather than
'packages', however, in the documentation, we use the term 'packages' to
try and avoid confusion with the module system for loading software.*)

Perl comes with an extensive standard library, and you are strongly
encouraged to use those packages as much as possible, since this will
ensure that your code can be run on any platform that supports Perl.

However, many useful extensions to and libraries for Perl come in the
form of packages that can be installed separately. Some of those are part
of the Perl modules available on VSC infrastructure.

Given the astounding number of packages, it is not sustainable to
install each and everyone system wide. :ref:`This section <perl-install-own-packages>`
explains shows how users can install Perl packages themselves.

Checking for installed Perl packages
------------------------------------

To check which Perl packages are installed, the ``cpan`` utility is
useful. It will list all packages that are installed for the Perl
distribution you are using, including those installed by you, i.e.,
those in your ``PERL5LIB`` environment variable.

#. Load the module for the Perl version you wish to use, e.g., ::

      $ module load Perl/5.40.0-GCCcore-14.2.0

#. In general it is recommended to also load the corresponding
   ``Perl-bundle-CPAN`` module, which makes a lot of Perl packages available
   (note it is also sufficient to only load this module, since the correct
   ``Perl`` module will be loaded automatically as a dependency) ::

      $ module load Perl-bundle-CPAN/5.40.0-GCCcore-14.2.0

#. Run cpan (this will provide a lot of output): ::

      $ cpan  -l

.. _perl-install-own-packages:

Installing your own Perl packages
---------------------------------

Setting up your own package repository for Perl is straightforward. For
this purpose, the ``cpan`` utility first needs to be configured.

#. Load the appropriate Perl module(s), e.g., ::

      $ module load Perl-bundle-CPAN/5.40.0-GCCcore-14.2.0

#. Create a directory to install in, i.e., ::

      $ mkdir ${VSC_DATA}/perl5

#. Run cpan: ::

      $ cpan

   The first time you run ``cpan`` it will propose to configure as much as
   possible automatically. This should be largely fine, but be careful when
   the script proposes to add environment variables to your ``~/.bashrc`` file,
   since the steps below will still modify those variables.

#. Configure internet access and mirror sites: ::
   
      cpan[1]> o conf init connect_to_internet_ok urllist

#. Set the install base, i.e., directory created above: ::

      cpan[2]> o conf makepl_arg INSTALL_BASE=${VSC_DATA}/perl5

#. Set the preference directory path: ::

      cpan[3]> o conf prefs_dir ${VSC_HOME}/.cpan/prefs

#. Commit changes so that they are stored in ``~/.cpan/CPAN/MyConfig.pm``, i.e., ::

      cpan[4]> o conf commit

#. Quit cpan: ::

      cpan[5]> q

Now Perl packages can be installed easily, e.g., ::

   $ cpan Acme::Meta

Note that this will install all dependencies as needed, though you may
be prompted.

In order to make Perl pick up your locally installed packages, execute ::

   $ export PERL5LIB=${VSC_DATA}/perl5/lib/perl5:${PERL5LIB}
   $ export PATH=${VSC_DATA}/perl5/bin:${PATH}

After this you can use locally installed packages ::

   $ perl -e "use Acme::Meta"
