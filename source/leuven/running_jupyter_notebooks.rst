How to run a Jupyter notebook on a compute node
===============================================

Jupyter notebooks provide a very convenient way for Python programmers
to explore and visualize data interactively, or do exploratory programming.
Typically, a notebook server runs on your own computer, and you connect
to it using a web browser (actually, the web browser will be started
automatically).

Although this is very convenient and easy to use, for more computationally
intensive work you may want to run the notebook server on a compute node
of a VSC cluster.


Prerequisites
-------------

The most convenient way to install Jupyter, and any other Python packages
you require is using conda.  In case you're not familiar with conda, please
check out the information on :ref:`managing Python packages using conda
<conda for Python>`.  In this how-to, we will assume that the conda
environment's name that has Jupyter installed is ``science``.  We will also
assume that the ``$VSC_DATA/miniconda3/bin`` directory is in your ``PATH``
variable.


Using a notebook on an NX node
------------------------------

Prerequisite: NoMachine
~~~~~~~~~~~~~~~~~~~~~~~

Although alternatives exist, the easiest approach is to use the NX login nodes, since this provides a GUI environment on a cluster login node.  The installation and setup of the NoMachine software on your computer is documented in the :ref:`quick start guide <NX start guide>`.  Once NoMachine is installed and configured, you can connect to the cluster.

Starting the server
~~~~~~~~~~~~~~~~~~~

The first step is to run a Jupyter notebook server, since this has to be done on a compute node, we first start an interactive job.

::

   $ qsub  -I  -l walltime=4:00:00

The ``-I`` flag specifies this is an interactive job, and we request 4 hours walltime.  Note that you would probably have to add the `-A` option with the project to debit for credits.

Once your job starts, you'll see the name of the node the job is running on in the shell prompt.  In this tutorial, we will assume it is ``r5i1n7``.

Navigate to the relevant directory where your notebook is stored, or where you intend to create a new one.

Load the conda environment, `science` in this tutorial:

::

   $ source activate science


Start a Jupyter notebook server:

::

   $ jupyter notebook  --ip $(hostname)  --port ${USER:3}

The port is set to the digits of you user name so that there will be no conflict when two users try
and run a notebook on the same compute node.

When Jupyter has started, the first URL below the line reading
``Jupyter Notebook X.Y.Z is running at:`` should look similar to this:
::

   http://r5i1n7:30140/?token=56262fe0755d2321911f96df8c3c98e651f24238452035d9

You can right-click this link and open the URL in a browser on the NX login node.



Using a notebook by tunneling from a Linux machine to a genius GPU node
-----------------------------------------------------------------------

Assumptions:

  1. The local machine's name is ``local``.
  2. The VSC account is vsc30140, replace with your own.
  3. The project to charge is ``lp_my_project``, replace with your own.
  4. The port number is 30140, replace with the numerical part of your VSC account.
  5. The conda environment in which Jupyter notebook is installed is ``machine_learning``, again, replace with your own.
  6. The GPU node the job is running on is ``r23g36``, replace with the hostname of the node your job runs on.


Start a job & a notebook
~~~~~~~~~~~~~~~~~~~~~~~~

First, start an interactive job on a compute node, and launch Jupyter
notebook.


Detailed steps:

    1. Log in the the genius login node using ssh:
       ::

          local$ ssh vsc30140@login3-tier2.hpc.kuleuven.be

    2. Start an interactive job on a GPU node:
       ::
        
          login3$ qsub -I -A lp_my_project -l nodes=1:ppn=9:gpus=1 \
                       -l partition gpu -l walltime=03:00:00
       
    3. When the job is running on the GPU node, activate your environment:  
       ::

          r23g36$ source activate machine_learning

    4. Go to the relevant directory, e.g., ``$VSC_DATA``.
    5. Start the Jupyter notebook, use a unique port number:
       ::

          r23g36$ jupyter notebook --port 30140

Set up SSH tunnel
~~~~~~~~~~~~~~~~~

Next, you set up a first tunnel from your machine to the GPU node on the SSH port of the GPU node.

Detailed steps:

::

   local$ ssh -J vsc30140@login1-tier2.hpc.kuleuven.be \
              -L 30140:localhost:30140                 \
              vsc30140@r23g36

**Note:** this command will not exit, if you like to do everything in one
terminal, put the process in the background using `&`.


Open the interface to Jupyter notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, open your web browser on your local machine, copy/paste the
link that Jupyter notebook displays into your browser, and *presto!*
