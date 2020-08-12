.. role:: raw-html(raw)
    :format: html
    
.. _Antwerp Slurm_convert_from_PBS:

Converting PBS/Torque options to Slurm
======================================

**This is preliminary documentation for the pilot users. It will be further refined as the pilot progresses.**


Common tasks in Torque/Moab and Slurm
-------------------------------------

==========================================  ==================  =======================
Task                                        Torque/Moab         Slurm equivalent
==========================================  ==================  =======================
Submit a job                                qsub                sbatch
Cancel a job                                qdel                scancel
List jobs in the queue                      qstat, showq        squeue
==========================================  ==================  =======================


#PBS / qsub command line options
--------------------------------

When specified in a Torque job script, the line specifying the option should start with ``#PBS``. 
In Slurm, such lines start with ``#SBATCH``.

===================================  =====================
PBS/Torque                           Slurm equivalent
===================================  =====================
-L tasks=\ **<X>**:lprocs=\ **<Y>**  --ntasks=\ **<X>** --cpus-per-task=\ **<Y>**
-l walltime=\ **<time>**             -t **<time>**\ , --time=\ **<time>**
-N **<jobname>**                     -J **<jobname>**\, --job-name=\ **<jobname>**
-o **<file>**                        -o **<file template>**\ , --output=\ **<file template>**
-e **<file>**                        -e **<file template>**\ , --error=\ **<file template>**\ , default is sending stderr to stdout
-m abe                               --mail-type=FAIL,BEGIN,END
-M **<mailadress>**                  --mail-user=\ **<mailadress>**
-v **<variable list>**               --export=\ **<variable list>**
===================================  =====================


Environment variables
---------------------

========================  ================================
PBS variable              Slurm variable
========================  ================================
PBS_JOBID                 SLURM_JOB_ID :raw-html:`<br />`
                          SLURM_JOBID (for backward compatibility)
PBS_JOBNAME               SLURM_JOB_NAME :raw-html:`<br />`
                          %j in filename templates
PBS_NODENUM
PBS_NODEFILE              Replaced by a variable specifying the nodes rather than a node file: SLURM__JOB_NODELIST, SLURM_NODELIST (for backward compatibility)
PBS_NUM_NODES             SLURM_JOB_NUM_NODES :raw-html:`<br />`
                          SLURM_NNODES (for backward compatibility)
PBS_NUM_PPN
PBS_NP
PBS_O_WORKDIR             Slurm executes the job in the directory from which the job was submitted (unless otherwise specified) rather than the home dir.
PBS_WALLTIME              No equivalent.
========================  ================================

