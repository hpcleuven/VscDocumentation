.. _vub onedrive:

####################
Your OneDrive in VUB
####################

You can directly copy files between Hydra and your
`OneDrive in VUB <https://vub-my.sharepoint.com>`_ using the third-party sync app
`OneDrive Client for Linux <https://github.com/abraunegg/onedrive/blob/master/README.md>`_.
This method avoids any additional step to copy the files to/from OneDrive
to/your your local computer before transferring them to the HPC.

.. warning:: Several restrictions and limitations apply to OneDrive:

    * OneDrive does not discriminate capitalization in file names. Avoid having
      two files in the same folder that only differ in the capitalization.

    * OneDrive does not allow filenames that contain any of the characters
      ``\/:*?""<>|``. Files that contain any of these characters will not be
      synced.

    * The following names aren’t allowed for files or folders: .lock, CON, PRN,
      AUX, NUL, COM0 - COM9, LPT0 - LPT9, _vti_, desktop.ini, any filename
      starting with ~$.

    * "_vti_" cannot appear anywhere in a file name.

    * "forms" isn’t supported when the folder is at the root level for a
      library.

    * You can’t create a folder name in SharePoint that begins with a tilde (~).

.. seealso::

   `Restrictions and limitations in OneDrive and SharePoint <https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa>`_

Client authorization
====================

#. Start by executing the command ``onedrive`` in a terminal shell on Hydra.
   The first time it will print the following information on screen:

   .. code-block:: shell

      onedrive

   Upon execution, a URL starting with ``https://login.microsoftonline.com`` is
   shown to authorize the client to access your VUB Office 365 account. The URL
   contains the ``client_id`` of the sync app, which should be **exactly**
   ``d50ca740-c83f-4d1b-b616-12c519384f0c``:

   .. code-block:: text
      :caption: Output:

      $ onedrive
      Configuring Global Azure AD Endpoints
      Authorize this app visiting:

      https://login.microsoftonline.com/[...]

      Enter the response uri:

#. Copy/paste the full URL in your browser

#. Log in with your credentials if necessary. You should be redirected to a
   blank page in your browser

#. Copy/paste the URL of the blank page into the prompt of onedrive in Hydra

At this point, if there is no error, your client should have access to your
account. By default, the access token to Office 365 is stored in the file
``~/.config/onedrive/refresh_token``

Synchronize with personal OneDrive
==================================

#. Create a directory that will be synced with your OneDrive.

   The following command creates the sync directory ``hydra-sync`` inside
   ``$VSC_DATA/onedrive`` (avoid using ``$HOME`` as it is small).

   .. code-block:: shell

      mkdir -p $VSC_DATA/onedrive/hydra-sync

#. Create the configuration file  ``~/.config/onedrive/config``.

   The following commands generate the config file. The entry ``sync_dir`` is
   mandatory and points to the *parent directory* of the sync directory. Also,
   we recommend to skip syncing symlinks and dotfiles (files that start with a
   dot) by default to avoid unexpected data transfers unless you know that you
   need those.

   .. code-block:: shell

      config=~/.config/onedrive/config
      echo sync_dir = \"$VSC_DATA/onedrive\" > $config
      echo 'skip_symlinks = "true"' >> $config
      echo 'skip_dotfiles = "true"' >> $config

#. Create the sync_list file ``~/.config/onedrive/sync_list``.

   The following command adds the sync directory ``hydra-sync`` to the
   sync_list file. This ensures that only data inside the sync directory is
   synced.

   .. code-block:: shell

      echo hydra-sync > ~/.config/onedrive/sync_list

#. Check if the OneDrive client has been configured correctly.

   .. code-block:: shell

      onedrive --resync --synchronize --verbose --dry-run

#. If the dry-run succeeded, re-run the above command but remove the
   ``--dry-run`` option to do the real sync.

   .. code-block:: shell

      onedrive --resync --synchronize --verbose

   If the sync is successful, the sync directory (here: ``hydra-sync``) should
   show up under ``My files`` in your VUB OneDrive.

#. For subsequent synchronizations, remove also the ``--resync`` option to avoid
   any further full synchronization. A *resync* is only needed after modifying
   the configuration or ``sync_list`` file.

   .. code-block:: shell

      onedrive --synchronize --verbose

.. seealso:: 

   `Onedrive Client for Linux documentation <https://github.com/abraunegg/onedrive/blob/master/docs/USAGE.md#configuration>`_

