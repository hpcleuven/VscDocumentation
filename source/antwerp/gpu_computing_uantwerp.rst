.. _GPU computing UAntwerp:

GPU computing @ UAntwerp
========================

Leibniz has two compute nodes each equipped with two NVIDIA Tesla P100
GPU compute cards, the most powerful cards available at the time of
installation of the system. Vaughan has one compute node equipped with 
four NVIDIA Tesla A100 GPU compute cards. We run the regular NVIDIA software stack on
those systems.

Additionally, Vaughan has two compute nodes equipped with two AMD Instinct
MI100 GPU compute cards. We run the AMD ROCm software stack on those systems.

The main goal of the system is to assess the performance of GPUs for
applications used by our researchers. We want to learn for which
applications GPU computing is economically viable. Users should realise
that these nodes carry three times the cost of a regular compute node
and might also be shorter lived (in the past, some NVIDIA GPUs have shown
to be pretty fragile). Hence these nodes should
only be used for applications that run three times faster than a regular
CPU-based equivalent and that use enough of the capacity of the available
GPUs. Also, the nodes are not meant for extensive production work but only
for the first experiments. At the VSC, more specialised hardware is only
available on certain sites as maintaining it properly requires too much
experience that not every site can have. The main GPU system for the 
VSC is integrated in the :ref:`Genius cluster at KU Leuven <Genius hardware>`.

As such we offer precedence to users who want to work with us towards
this goal and either develop high-quality GPU software or are willing to
benchmark their application on GPU and regular CPUs.

Getting access
--------------

Contact :ref:`the UAntwerp support team <user support VSC>`
to get access to the GPU compute nodes.

Users of the GPU compute nodes are expected to report back on their
experiences. We are most interested in users who can also compare with
running on regular nodes as we will use this information for future
purchase decisions.

Likewise given that modern clusters tend to be built with nodes with 
even 4 or 8 GPUs, we'd like to learn from those users who can use only
a single GPU in a node what is restricting them to use both.

Starting jobs
-------------

The GPU compute nodes are managed through a separate partition, so you will need
to explicitly specify it when submitting your job. We also configured the GPU
nodes as shared resources, so that two users could each get exclusive 
access to a single, dedicated GPU at the same time.

In total, three GPU partitions are available:

=======   ============   ==================================================
Cluster   Partition      Available nodes
=======   ============   ==================================================
Vaughan   arcturus_gpu   2 nodes with 2 AMD Instinct (Arcturus) MI100 cards
Vaughan   ampere_gpu     1 node with 4 NVIDIA (Tesla) Ampere A100 cards
Leibniz   pascal_gpu     2 nodes with 2 NVIDIA (Tesla) Pascal P100 cards
=======   ============   ==================================================
 

To submit a job on a GPU compute node belonging to a certain partition and get a single GPU, use the  ``sbatch`` command

.. code:: bash
   
    sbatch -p <partition> --gpus=1 <jobscript>

or add the lines

.. code:: bash
   
    #SBATCH -p <partition>
    #SBATCH --gpus=1

to your job script.

Using ``gpus=2`` would give you access to both GPU cards on a GPU compute node.

The defaults for the pascal_gpu nodes are set to ``--cpus-per-gpu=14`` and ``walltime=1:00:00``, so
that with using only ``-p pascal_gpu --gpus=1`` you would get a single GPU for 1 hour and all
cores belonging to the CPU that is closest to that GPU. The Vaughan GPU nodes use a similar setup.

Note that the maximum wall time is limited to 24 hours, with no exceptions made.

Monitoring GPU nodes
--------------------

Monitoring of CPU use by jobs running on the GPU nodes can be done in
the same way as for regular compute nodes.

One useful command to monitor the use of the NVIDIA GPUs is ``nvidia-smi``. It
will show information on both GPUs in the GPU node, and among others
lets you easily verify if the GPUs are used by the job.
The AMD GPUs can be monitored similarly using the ``rocm-smi`` command.

Software on the GPU
-------------------

Software is installed on demand. As these systems are new to us also, we
do expect some collaboration of the user to get software running on the
GPUs.

+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Package       | **Module**                                                   | Description                                                  |
+===============+==============================================================+==============================================================+
| Amber         | Amber/20-intel-2020a-AmberTools-20-patchlevel-6-10           |                                                              |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `CP2K`_       | CP2K/5.1-intel-2017a-bare-GPU-noMPI                          | GPU-accelerated version of CP2K. The ``-GPU-noMPI-versions`` |
|               |                                                              | are ssmp binaries                                            |
|               |                                                              | without support for                                          |
|               |                                                              | MPI, so they can only                                        |
|               |                                                              | be used on a single                                          |
|               |                                                              | GPU node. The                                                |
|               |                                                              | binaries are compiled                                        |
|               |                                                              | with equivalent                                              |
|               |                                                              | options to the                                               |
|               |                                                              | corresponding ``-bare-multiver``                             |
|               |                                                              | modules for CPU-only                                         |
|               |                                                              | computations.                                                |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `CUDA`_       | - CUDA/8.0.61                                                | Various versions of                                          |
|               | - CUDA/9.0.176                                               | the CUDA development                                         |
|               | - CUDA/9.1.85                                                | kit                                                          |
|               | - CUDA/9.2.148.1                                             |                                                              |
|               | - CUDA/10.0.130                                              |                                                              |
|               | - CUDA/10.0.130                                              |                                                              |
|               | - CUDA/10.2.89                                               |                                                              |
|               | - CUDA/11.1.0                                                |                                                              |
|               | - CUDA/11.2.1                                                |                                                              |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `cuDNN`_      | - cuDNN/6.0-CUDA-8.0.61                                      | The CUDA Deep Neural                                         |
|               | - cuDNN/7.0.5-CUDA-8.0.61                                    | Network library,                                             |
|               | - cuDNN/7.0.5-CUDA-9.0.176                                   | version 6.0 and 7.0,                                         |
|               | - cuDNN/7.0.5-CUDA-9.1.85                                    | both installed from                                          |
|               | - cuDNN/7.4.1.5-CUDA-9.0.176                                 | standard NVIDIA                                              |
|               | - cuDNN/7.4.1.5-CUDA-10.0.130                                | tarballs but in the                                          |
|               | - cuDNN/7.6.5.32-CUDA-10.0.130                               | directory structure                                          |
|               | - cuDNN/7.6.5.32-CUDA-10.1.243                               | of our module system.                                        |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Darknet       | - Darknet/20180326-intel-2017a-GPU-noOpenCV                  |                                                              |
|               | - Darknet/20180326-intel-2017a-GPU-OpenCV                    |                                                              |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `GROMACS`_    | - GROMACS/2016.4-foss-2017a-GPU-noMPI                        | GROMACS with GPU                                             |
|               | - GROMACS/2016.4-intel-2017a-GPU-noMPI                       | acceleration. The                                            |
|               | - GROMACS/2018.3-intel-2018b-UArecipe-CUDA                   | ``-GPU-noMPI-versions``                                      |
|               | - GROMACS/2019.1-intel-2018b-UArecipe-CUDA                   | are ssmp binaries                                            |
|               | - GROMACS/2019.2-intel-2018b-UArecipe-CUDA                   | without support for                                          |
|               |                                                              | MPI, so they can only                                        |
|               |                                                              | be used on a single                                          |
|               |                                                              | GPU node.                                                    |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `Keras`_      | Keras/2.1.3-intel-2018a-GPU-Python-3.6.4                     | Keras with TensorFlow                                        |
|               |                                                              | as the backend (1.4                                          |
|               |                                                              | for Keras 2.1.3),                                            |
|               |                                                              | using the                                                    |
|               |                                                              | GPU-accelerated                                              |
|               |                                                              | version of                                                   |
|               |                                                              | Tensorflow.                                                  |
|               |                                                              | For comparison                                               |
|               |                                                              | purposes there is a                                          |
|               |                                                              | identical version                                            |
|               |                                                              | using the CPU-only                                           |
|               |                                                              | version of TensorFlow                                        |
|               |                                                              | 1.4.                                                         |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `NAMD`_       |                                                              | Work in progress                                             |
|               |                                                              |                                                              |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| OpenCV        | OpenCV/3.3.1-intel-2017a-GPU-noGUI                           |                                                              |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| `TensorFlow`_ | - Tensorflow/1.3.0-intel-2017a-GPU-Python-3.6.1              | GPU versions of                                              |
|               | - Tensorflow/1.4.0-intel-2018a-GPU-Python-3.6.4              | Tensorflow 1.3 and                                           |
|               | - TensorFlow/1.12.0-intel-2018a-GPU-Python-3.6.6             | 1.4. Google-provided                                         |
|               | - TensorFlow/1.12.0-intel-2018b-GPU-Python-3.6.8-Keras-2.2.4 | binaries were used                                           |
|               | - TensorFlow/1.14.0-intel-2018b-GPU-Python-3.6.8-keras-2.3.1 | for the installation.                                        |
|               | - TensorFlow/1.15.0-intel-2019b-GPU-Python-3.7.4-keras-2.3.1 | There are CPU-only                                           |
|               | - TensorFlow/2.1.0-intel-2019b-GPU-Python-3.7.4-keras-2.3.1  | equivalents of those                                         |
|               | - TensorFlow/2.2.0-intel-2020a-GPU-Python-3.8.3              | modules for                                                  |
|               |                                                              | comparison. The 1.3                                          |
|               |                                                              | version was installed                                        |
|               |                                                              | from the standard                                            |
|               |                                                              | PyPi wheel which is                                          |
|               |                                                              | not well optimized                                           |
|               |                                                              | for modern                                                   |
|               |                                                              | processors, the 1.4                                          |
|               |                                                              | version was installed                                        |
|               |                                                              | from a Python wheel                                          |
|               |                                                              | compiled by Intel                                            |
|               |                                                              | engineers and should                                         |
|               |                                                              | be well-optimized for                                        |
|               |                                                              | all our systems.                                             |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+
| TensorRT      | TensorRT/6.0.1.5-CUDA-10.1.243-cuDNN-7.6.5.32                | Needed for recent TensorFlow  versions.                      |
+---------------+--------------------------------------------------------------+--------------------------------------------------------------+

