.. _iron-CLI:

iron CLI Client
===============

Introduction
------------

iron is a Go-based client for interacting with Tier-1 Data (and other iRODS systems) that provides both a programmatic API and a command-line interface. This documentation covers the CLI usage for end users.

Iron is a platform-independent command-line interface that provides reliable data transfer and serves as both an alternative iRODS client and a generic ManGO authentication tool. Its built-in PAM interactive authentication eliminates the need for extra packages, making a single installation sufficient for all requirements.


Installation
------------

The CLI binary can be downloaded from https://github.com/kuleuven/iron/releases/latest. e.g. on a Linux system, macOS or Windows WSL. Linux users can execute the snippet below to install iron CLI.

.. code:: sh

   VERSION=$(curl -Ls -w %{url_effective} -o /dev/null https://github.com/kuleuven/iron/releases/latest | sed 's/.*\/v//')
   mkdir -p .local/bin/
   curl -L -s "https://github.com/kuleuven/iron/releases/download/v${VERSION}/iron_${VERSION}_linux_amd64.tar.gz" | tar zxvf - -C .local/bin/

Linux and Windows users can install iron directly using the dedicated installer.

Installation Steps for Linux(Debian) Uers:

- Download the installer (iron_{VERSION}_amd64.deb ) from: https://icts-p-coz-iron-releases.cloud.icts.kuleuven.be/

.. code:: sh

   wget https://icts-p-coz-iron-releases.cloud.icts.kuleuven.be/iron/{VERSION}_amd64.deb

- Install the downloaded package

.. code:: sh

   sudo dpkg -i iron_{VERSION}_amd64.deb

- If you wish you can remove the downloaded package

.. code:: sh

   rm iron_{VERSION}_amd64.deb

Installation Steps for Windows Uers:

- Download the installer (iron_installer.exe) from: https://icts-p-coz-iron-releases.cloud.icts.kuleuven.be/

- Double-click `iron_installer.exe` to begin installation and follow the on-screen steps.

If prompted for administrator rights during installation, you may need to move the installer to a folder that doesn't require administrator rights and run it from there.

**Note:** The iron installer will soon be available in the Software Center for KU Leuven Windows users.

After installation is completed, you verify with:

.. code:: sh

   iron version


Authentication
--------------

To authenticate using iron, first obtain your connection details from the `ManGO portal <https://mango.vscentrum.be/>`__ and then run the snippet below.

.. code:: sh

   iron auth irods_user_name irods_zone_name irods_host

If you connected earlier to a ManGO zone already, you can simply run
 
.. code:: sh

   iron auth
 
to reconnect to the last zone.

For jobs with a long runtime that may exceed the iRODS session timeout, you can handle re-authentication programmatically.

Include the `iron auth --non-interactive` command in your script's exception-handling logic to automatically re-establish the session if it expires during execution. This command performs silent re-authentication without a login prompt, provided the underlying OIDC session is still valid.

You can manage your iRODS session duration via OIDC session controls at the authentication portal and the `iron auth` command.

- After authentication, you can revoke, extend, or reactivate your OIDC session directly at https://auth.vscentrum.be/.

- Use the `iron auth` command to manage your iRODS session.

Once the auth command generates the authentication link displayed in your terminal click it and complete the steps on https://auth.vscentrum.be/.

Interactive Shell
-----------------

iron provides an interactive shell, enabling you to run all data management commands directly without prefixing them with `iron` each time. You can also access your local file system using the `local` command.

A key advantage of the iron shell is its built-in tab completion, which reduces the need to type commands and paths in full. To get an interactive shell:

.. code:: sh

   iron shell

or;

.. code:: sh

   iron


How to use iron
---------------

You can discover all supported operations and their corresponding commands by running `iron --help`, as shown in the example below.

.. code:: sh

    iron --help
    
    Golang client for iRODS
    
    Usage:
    iron [command]
    
    Available Commands:
      auth        Authenticate against the irods server.
      cat         Stream a data object to stdout
      cd          Change the current working directory
      checksum    Compute or get the checksum of a file
      chmod       Change permissions
      completion  Generate the autocompletion script for the specified shell
      cp          Copy a data object or a collection
      create      Create a data object without content
      download    Download a data object or a collection to the local path
      exit        Exit the interactive shell.
      head        Print the first lines of a data object to stdout
      help        Help about any command
      inherit     Change permission inheritance
      local       Run a local command
      ls          List the contents of a collection or information about a data object
      meta        Run a metadata command
      mkdir       Create a collection
      mv          Move a data object or a collection
      pwd         Print the current working directory
      query       Run a generic query
      rm          Remove a data object or collection
      rmdir       Remove a empty collection
      save        Stream the standard input to a data object.
      stat        Get information about an object or collection
      touch       Touch a data object
      tree        Print the full tree structure beneath a collection
      upload      Upload a local file or directory to the destination path
      version     Print the version number of iron
    
    Flags:
        --admin            Enable admin access
    -v, --debug count      Enable debug output
    -h, --help             help for iron
        --native           Use native protocol
        --ttl duration     TTL in case pam authentication is used (default 168h0m0s)
        --workdir string   Working directory
    
    Use "iron [command] --help" for more information about a command.