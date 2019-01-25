.. _disk usage:

Managing disk usage
===================

Total disk space used on filesystems with quota      
-----------------------------------------------
                                  
On filesystems with 'quota enabled', you can check the amount of disk space that
is available for you, and the amount of disk space that is in use by   
you. Unfortunately, there is not a single command that will give   
you that information for all file systems in the VSC.               
                                  
-  ``quota`` is the standard command to request your disk   
   quota. Its output is in 'blocks', but can also be      
   given in MB/GB if you use the ``-s`` option.                   
-  But it does not work on GPFS file systems. On those you     
   have to use ``mmlsquota``.  This is the case for the       
   scratch space at the KU Leuven or on the Tier-1.              
-  On some clusters, these commands are currently disabled.
-  Also, using these commands on another cluster than the one   
   in your home institution, will fail to return information     
   about the quota on your VSC_HOME and VSC_DATA          
   directories and will show you  the quota for your VSC_SCRATCH 
   directory on that system.      
                                  
::                                
                                  
   quota -s
   Disk quotas for user vsc31234 (uid 123456):
     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
     nas2-ib1:/mnt/home
                     648M   2919M   3072M            3685       0       0
                     nas2-ib1:/mnt/data
                                   20691M  24320M  25600M            134k       0       0
                                   nas1-ib1:/mnt/site_scratch
                                                      0  24320M  25600M               1       0       0

Each line represents a file system you have access to,$VSC_HOME, $VSC_DATA,
and, for this particular example, $VSC_SCRATCH_SITE. The blocks     
column shows your current usage, quota is the usage above which    
you will be warned, and limit is "hard", i.e., when your usage  
reaches this limit, no more information can be written to the 
file system, and programs that try will fail.                    
                                  
Some file systems have limits on the number of files that can be   
stored, and those are represented by the last four columns. The     
number of files you currently have is listed in the column      
files, quota and limit represent  the soft and hard limits for the  
number of files.                  
                                  
Diskspace used by individual directories         
----------------------------------------
                                  
The command to check the size of  all subdirectories in the current 
directory is ``du``
                                  
::                                
                                  
   $ du -h                        
   4.0k      ./.ssh               
   0         ./somedata/somesubdir  
   52.0k     ./somedata             
   56.0k   .                      
                                  
                                  
This shows you first the aggregated size of all subdirectories, and
finally the total size of the current directory \\".\" (this includes   
files stored in the current directory). The -h option ensures 
that sizes are displayed in human readable form, omitting it will   
show sizes in bytes.              
                                  
If the number of lower level subdirectories starts to grow too 
big, you may not want to see the information at that depth; you    
could just ask for a summary of the current directory:            
                                  
::                                
                                  
   du -s                          
   54864 .                        
                                  
If you want to see the size of any file or top level subdirectory in the current
directory, you could use the      following command:                
                                  
::                                
                                  
   du -s *                        
   12      a.out                  
   3564    core                   
   4       mpd.hosts              
   51200   somedata               
   4       start.sh               
   4       test                   
                                  
                                  
Finally, if you don't want to know the size of the data in your 
current directory, but in some other directory (eg. your data    
directory), you just pass this directory as a parameter. If you  
also want this size to be "human readable" (and not      
always the total number of        kilobytes), you add the parameter ``-h``:
                                  
::                                
                                  
   du -h -s $VSC_DATA/*           
   50M     /data/leuven/300/vsc30001/somedata                      
