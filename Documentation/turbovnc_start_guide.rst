TurboVNC start guide
====================

TurboVNC is a good way to provide access to remote visualization
applications that works together with VirtualGL - a popular package for
remote visualization.

Installing TurboVNC client (viewer)
-----------------------------------

-  Download the most recent version of the client from the `TurboVNC
   download page on
   SourceForge <\%22https://sourceforge.net/projects/turbovnc/files/\%22>`__.
-  Continue with configuration of your client.

TurboVNC client Configuration & Start Guide
-------------------------------------------

*Note: These instructions are for the KU Leuven visualization nodes
only. The UAntwerp visualization node also uses TurboVNC, but the setup
is different as the visualization node is currently not in the job
queueing system and as TurboVNC is also supported on the regular login
nodes (but without OpenGL support). Specific instructions for the use of
TurboVNC on the UAntwerp clusters can be found on the page
\\"\ *\ `Remote visualization @
UAntwerp <\%22/infrastructure/hardware/hardware-ua/visualization\%22>`__\\".

#. Request an interactive job on visualization partition:

   ::

      $ qsub -I -X -l partition=visualization    -l pmem=6gb -l nodes=1:ppn=20
          

#. Once you are on one of visualization nodes (r10n3 or r10n4) load the
   TurboVNC module:

   ::

      $ module load TurboVNC/1.2.3-foss-2014a
          

#. Create password to authenticate your session:

   ::

      $ vncpasswd
          

   In case of problems with saving your password please create the
   appropriate path first:

   ::

      $ mkdir .vnc; touch .vnc/passwd; vncpasswd
          

#. Start VNC server on the visualization node (optionally with geometry
   settings):

   ::

      $ vncserver (-depth 24 -geometry 1600x1000)
          

   As a result you will get the information about the display <d> that
   you are using (r10n3:), e.g.for <d>=1

   ::

      Desktop 'TurboVNC: r10n3:1 (vsc30000)' started on display r10n3:1
          

#. | Establish the ssh tunnel connection:
   | In Linux/ Mac OS:

   ::

           $ ssh -L 590<d>:host:590<d> -N vsc30000@login.hpc.kuleuven.be
      e.g. $ ssh -L 5901:r10n3:5901 -N vsc30000@login.hpc.kuleuven.be
          

   | 
   | In Windows:
   | In putty go to Connection-SSH-Tunnels tab and add the source port
     590<d> (e.g. 5901) and destination host:590<d> (e.g. r10n3:5901).
   | |\\"TVNC|
   | Once the tunnel is added it will appear in the list of forwarded
     ports:
   | |\\"TVNC|
   | With that settings continue `login to the
     cluster <\%22/client/windows/console-putty\%22>`__.

#. Start VNC viewer connection
   Start the client: VSC server as localhost:<d> (where <d> is display
   number), e.g. localhost:1
   |\\"TVNC|
   Authenticate with your password
   |\\"TVNC|
#. After your work is done do not forget to close your connection:

   ::

           $ vncserver -kill :<d>; exit
      e.g. $ vncserver -kill :1; exit
          

How to start using visualization node?
--------------------------------------

#. TurboVNC works with the tab Window Manager twm (more info on how to
   use it can be found on the `Wikipedia twm
   page <\%22https://en.wikipedia.org/wiki/Twm\%22>`__ or on the `twm
   man page <\%22https://linux.die.net/man/1/twm\%22>`__).
   |\\"twm\"|
#. To start a new terminal use left click of the mouse and choose xterm
   |\\"twm\"|
#. Load the appropriate visualization module (Paraview, VisIt, VMD,
   Avizo, e.g.

   ::

      $ module load Paraview
          

#. Start the application. In general the application has to be started
   using VirtualGL package, e.g.

   ::

      $ vglrun –d :0 paraview
          

   but to make it easier we created scripts (starting with capital
   letters: Paraview, Visit, VMD) that can execute the necessary
   commands and start the application, e.g.

   ::

      $ Paraview
          

#. For checking how much GPUs are involved in your visalization you may
   execute gpuwatch in the new terminal:

   ::

      $ gpuwatch
          

Attached documents
------------------

`Slides from the lunchbox
session <\%22https://www.vscentrum.be/assets/1005\%22>`__

"

.. |\\"TVNC| image:: \%22/assets/1007\%22
.. |\\"TVNC| image:: \%22/assets/1009\%22
.. |\\"TVNC| image:: \%22/assets/1011\%22
.. |\\"TVNC| image:: \%22/assets/1013\%22
.. |\\"twm\"| image:: \%22/assets/1015\%22
.. |\\"twm\"| image:: \%22/assets/1017\%22

