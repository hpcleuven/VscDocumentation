.. _webdav_access_to_irods:

WebDAV Client Access (Davrods)
===============================

WebDAV stands for Web Distributed Authoring and Versioning, which is an extension to HTTP, the protocol that web browsers and web servers use to communicate with each other.
WebDAV can be used for remotely managing files over the internet. With WebDAV, we can access files stored in the VSC Tier-1 Data component by using the same interface as we do with our local files.

The module that we use for our iRODS connection is called `Davrods <https://github.com/UtrechtUniversity/davrods>`__. Davrods is an Apache WebDAV interface to iRODS and it provides access to iRODS servers using the WebDAV protocol. It is a bridge between the WebDAV protocol and iRODS.

For an access using Graphical User Interface (GUI) clients to iRODS, we can and will use different tools. However in this page we will see how to use mapping a network drive.

From a web browser side a simple directory index is used as an interface. Its purpose is only to list and to view. It is not intended to download and upload data.

Web Browser-Directory Index
---------------------------

A connection through Davrods is available at https://irods.hpc.kuleuven.be:8443/ address. After you click the link you can login using your vsc-account and a password, which should be obtained at https://irods.hpc.kuleuven.be/. 
To get the password you simply log in the mentioned address by passing VSC authentication layer.

Therefore the first step is to acquire password. To do so, simply click the link provided above or copy it and then “paste and search for” on your favorite web browser. 

.. image:: webdav/vsc_authentication_page.png

Once you reach the screen above, choose a login provider that is relevant to you. On the coming page you will see a very long password highlighted on the picture below. Copy this password correctly.

.. image:: webdav/password.png

After that you should go to the log in link https://irods.hpc.kuleuven.be:8443/ and see the screen below.

.. image:: webdav/davrods_access.png

Once you enter your user name and the password you saved, you will see the exact same directory structure as you see in your iRODS server.

.. image:: webdav/dir_index.png

You can now walk around directories and read the data object on your browser.