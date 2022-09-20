.. _winscp_access_irods.rst:

Using WinSCP for Accessing to iRODS
===================================

Another tool to upload/download data to/from iRODS through Graphical User Interface (GUI) is WinSCP (Windows Secure Copy). WinSCP is an open source free (SFTP client, FTP client, WebDAV client, S3 client and SCP client) for Windows. Its main function is file transfer between a local and a remote computer.

Installing and First Time Configuration of WinSCp
-------------------------------------------------

- Visit the official site at https://winscp.net/eng/index.php.

- Click the download icon.

.. image:: winscp/winscp1.png

- Open the WinSCP.exe file and follow the installation procedure at the following link https://winscp.net/eng/docs/guide_install. Complete your install in accordance with your institution’s application installation policy.

- After you complete your installation, run the program.

<<<<<<< HEAD
- Choose the required options and fill the blank fields with the corresponding information as you see on the screen below. Write the password that you will get at https://irods.hpc.kuleuven.be/.

.. note:: Since the password you obtained is temporary, you need to get every time a new one after your password is expired.
=======
- Choose the required options and fill the blank fields with the corresponding information as you see on the screen below. Write the password that you will get at https://vsc-passwd.icts.kuleuven.be .
>>>>>>> data_M

.. image:: winscp/winscp2.png

- The first time you make the connection, you will be asked to ‘Continue connecting and add host key to the cache’; select ‘Yes’.

- You can choose/set your remote directory for easiness. 


.. image:: winscp/winscp2.png


Upload/Download Data to/from iRODS using WinSCp
-----------------------------------------------

- On the WinSCP screen, the right pane shows our connection to iRODS, and the left pane shows our local directories.

- To upload data from local to iRODS, we simply drag a file or a folder on the left pane and drop it in the place we want on the right pane.

- To upload data from iRODS to our local directory, we drag data object or a collection(s) on the right pane and drop it in the place we want on the left pane.

.. image:: winscp/winscp3.png

- We can use WinSCP on both local and iRODS to create/delete/rename a file or folder.

<<<<<<< HEAD
- Also we can edit a file which gives GUI conform to change content. This is not possible with iCommands. 
=======
- Also we can edit a file which gives GUI conform to change content. This is not possible with iCommands. 
>>>>>>> data_M
