.. _user_access:

User Access to iRODS
====================

Since Tier-1 Data Service platform is currently on the pilot phase, users of the system are consisted of volunteers. Thus, if you are invited or have an interest in, please contact with FOZ team.

To be able to log on and to use Tier-1 Data Service platform, you need to have an iRODS account. Make sure that before claiming an iRODS account, a VSC account should be acquired. However not all VSC users might get an iRODS account. To this end you have to have a convenient project. 

After the above mentioned points are assured, you can ask for an iRODS account via an email to FOZ.

As soon as your user account is created by iRODS admin you will be notified. Keep in mind that your iRODS account will be exactly same as your VSC account.

To reach out the iRODS you can use any login nodes of HPC system. As known well, when you log on to VSC system, the directory where you arrive by default is “VSC_HOME” that has a limited capacity, only for the typical configuration files etc. Therefore it is strongly advised to operate iRODS system in data directory which is pointed by the environment variable “VSC_DATA”. So first go to the “VSC_DATA” directory. 

There to be able to log on to the iRODS, execute only the following::

$ ssh irods.hpc.kuleuven.be | bash

Now you are in iRODS. Whenever the system asks you a new log in or password/authentication related error, execute the same command.

At the moment you are logged on you will be on your iRODS home, which is for instance “/kuleuven_tier1_pilot/home/vsc33586”. You will be able to see and use by default public location like the following “/kuleuven_tier1_pilot/home/public”. This location is anonymous for everybody. Any data that is loaded here will be accessed by all even with third parties, e.g. non iRODS users. In addition to these two default location, if you are added to a project then you will have access to that place too, like this example “/kuleuven_tier1_pilot/home/lt1_es2020”.
