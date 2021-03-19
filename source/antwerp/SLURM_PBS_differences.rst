.. _Antwerp Slurm_PBS_differences:

Important differences between Slurm and Torque
==============================================

**This is preliminary documentation for the pilot users. It will be further refined as the pilot progresses.**

- **Environment at job start:**
   - Torque does by default start with the login environment of a user.
   - Slurm starts by default with the environment from which the job was submitted 
     (essentially the effect of ``qsub -V`` in Torque). 
     This can have unexpected results, e.g., if you resubmit the job from a different 
     environment or if some things are in different directories on the login and cluster 
     nodes which does sometimes happen when we do a silent upgrade of the cluster.
       - ``--export=NONE`` will start the job with a very empty environment*
       - ``--export=NONE --get-user-env`` will give an environment pretty equivalent
         to what you would get on Torque.*
- **Redirection of stdout and stderr:**
   - In Torque, stdout and stderr go to different files by default. Both streams can be merged 
     in a single file as in Slurm by specifying ``-j oe`` in the job script or at the qsub command line.
   - In Slurm, stdout and stderr are merged into a single file by default. You can change the behaviour 
     by specifying a filename for stderr using ``--output-err``.

