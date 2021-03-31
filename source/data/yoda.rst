.. _yoda:

Yoda Portal Client for VSC Users
================================

`Yoda <https://yoda.uu.nl/yoda-uu-nl/what-is-yoda/index.html>`__ is a research data management solution on top of iRODS developed by Utrecht University. Yoda portal is a web application for performing data management activities, such as managing access to your data and changing metadata. It allows users to deploy and manage their research data.

You can reach the Yoda portal by clicking `yoda portal <https://icts-p-hpc-yoda-portal.cloud.icts.kuleuven.be/user/login>`__.
You will need to authenticate with your institutional account and then the password request will be done automatically.

In VSC-Yoda portal, there are two main workspaces, “research” and “vault”.

**Research**: Collaboration workspace for a research group. No restrictions on the organization of data in folders. Metadata can be added to a folder. When all required metadata has been added a folder can be archived. You can view/edit/add metadata for a dataset that will be placed in the vault.

VSC users are expected to use mostly this space.

**Vault**: This area has a 'deposit' functionality which VSC users will not use. Tier-1 Data service users will use this area as an output of research area and an input to compute system. 

**Group Manager**: To keep data in a secure way Yoda allows you to put the data in data compartments, which can only be accessed by members. The Group Manager can create category/subcategory/group as data compartments and their members. People with a “group manager” role can add members to a data compartment, remove them, and change their roles.

.. image:: yoda/yoda_general.png

Use the Research menu item to manage your data. Each data compartment has two main folders:

The main folder (“research-…”) contains current research data that researchers collaborate on. Data is kept in subfolders. The subfolders can be organized according to the needs of the researcher.

Use the “Submit” button to deposit the subfolder. This will copy the contents of the subfolder to the Vault folder as a new data package (see below). Before doing so, the subfolder must be described with metadata, which can be entered by clicking on the Metadata button. The folder named “vault-…” contains deposited data packages. Once deposited, data cannot be removed. Therefore the vault can be used to account for data in a research project to comply with FAIR principles.

**Note**: If a collection is created in iRODS, we can see it with its content in Yoda but we cannot edit anything. A collection created first in Yoda can be seen/edited both in Yoda and iRODS.

To allow different communities to share the same Yoda implementation the concept of categories and subcategories were introduced. Every group has a category and subcategory. Within the group-manager groups are grouped into a tree of categories and subcategories.