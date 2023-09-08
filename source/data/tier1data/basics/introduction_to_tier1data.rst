###########################
Introduction to Tier-1 Data
###########################


More and more VSC users have computational tasks that make intensive use of large data sets. 
The Tier-1 Data platform of the VSC enables researchers to store their data close to the computing infrastructure during the active phase of their research projects.
Additionally, it gives them tools to manage data in a `FAIR <https://www.kuleuven.be/rdm/en/guidance/fair>`_ and efficient way from start to finish.  

The Tier-1 Data platform is based on the open source software iRODS.
Researchers can manage data via different clients, such as a command-line interface, a Python API or a web interface.  

Tier-1 Data provides four core competencies:

-  **Storage**

   Data is stored securely in the data centers of KU Leuven.  
   Of each file, two copies are stored: one in the datacenter of Heverlee, and one in the datacenter of Leuven. 
   

-  **Metadata**

   Data can be described by adding metadata, either on the file or folder level.
   This metadata can serve multiple purposes:

   - Provide context to the data  
   - Make data findable via the search interface  
   - Play a role in workflow automation

   Metadata can be added manually, but also via automation (e.g. extraction of metadata from file headers) or by using metadata schema's in the web interface.  

-  **Automation**

   Tier-1 Data has a a Python API and a command-line interface, which can be integrated easily into your existing code and jobscripts.
   This way, you can easily integrated data movement and data management actions in your existing HPC workflow. 

   Tier-1 Data's servers also have event triggers called Policy Enforcement Points (PEPs), which trigger every time a certain type of action is taken (e.g. a user uploads a file).
   Administrators can define processes that run each time one of these PEPs is triggered. This allows us to work together with users and 
   create powerful, automated workflows that help to save time and prevent human errors.

-  **Secure Collaboration**

   In Tier-1 Data, you can share data with users and user groups via a system of permissions.  
   Permissions can be managed on file and folder level, allowing for detailed access control.
   If you have collaborators without a VSC account, data in Tier-1 Data can be shared via the tool Globus. 


