GPU computing @ UAntwerp
========================

Leibniz has two compute nodes each equipped with two NVIDIA Tesla P100
GPU compute cards, the most powerful cards available at the time of
installation of the system. We run the regular NVIDIA software stack on
those systems

The main goal of the system is to assess the performance of GPUs for
applications used by our researchers. We want to learn for which
applications GPU computing is economically viable. Users should realise
that these nodes carry three times the cost of a regular compute node
and might also be shorter lived (in the past, some NVIDA GPUs have shown
to be pretty fragile). So these nodes are only interesting and should
only be used for applications that run three times faster than a regular
CPU-based equivalent.

As such we offer precedence to users who want to work with us towards
this goal and either develop high-quality GPU software or are willing to
benchmark their application on GPU and regular CPUs.

Getting access
--------------

Contact :ref:`the UAntwerp support team <user support VSC>`
to get access to the Xeon Phi node.

Users of the GPU compute nodes are expected to report back on their
experiences. We are most interested in users who can also compare with
running on regular nodes as we will use this information for future
purchase decisions.

Currently the nodes are not yet integrated in the job system, you can
log on manually to the node but need to check if noone else is using the
node.

Monitoring GPU nodes
--------------------

Monitoring of CPU use by jobs running on the GPU nodes can be done in
the same way as for regular compute nodes.

One useful command to monitor the use of the GPUs is ``nvidia-smi``. It
will show information on both GPUs in the GPU node, and among others
lets you easily verify if the GPUs are used by the job.

Software on the GPU
-------------------

Software is installed on demand. As these systems are new to us also, we
do expect some collaboration of the user to get software running on the
GPUs.

+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| Package               | **Module**                                                                    | Description                                                      |
+=======================+===============================================================================+==================================================================+
| `CP2K`_               | CP2K/5.1-intel-2017a-bare-GPU-noMPI                                           | GPU-accelerated version of CP2K. The ``-GPU-noMPI-versions``     |
|                       |                                                                               | are ssmp binaries                                                |
|                       |                                                                               | without support for                                              |
|                       |                                                                               | MPI, so they can only                                            |
|                       |                                                                               | be used on a single                                              |
|                       |                                                                               | GPU node. The                                                    |
|                       |                                                                               | binaries are compiled                                            |
|                       |                                                                               | with equivalent                                                  |
|                       |                                                                               | options to the                                                   |
|                       |                                                                               | corresponding ``-bare-multiver``                                 |
|                       |                                                                               | modules for CPU-only                                             |
|                       |                                                                               | computations.                                                    |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| `CUDA`_               | CUDA/8.0.61                                                                   | Various versions of                                              |
|                       | CUDA/9.0.176                                                                  | the CUDA development                                             |
|                       | CUDA/9.1.85                                                                   | kit                                                              |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| `cuDNN`_              | cuDNN/6.0-CUDA-8.0.61                                                         | The CUDA Deep Neural                                             |
|                       | cuDNN/7.0.5-CUDA-8.0.                                                         | Network library,                                                 |
|                       | 61                                                                            | version 6.0 and 7.0,                                             |
|                       | cuDNN/7.0.5-CUDA-9.0.                                                         | both installed from                                              |
|                       | 176                                                                           | standard NVIDA                                                   |
|                       | cuDNN/7.0.5-CUDA-9.1.                                                         | tarbals but in the                                               |
|                       | 85                                                                            | directory structure                                              |
|                       |                                                                               | of our module system.                                            |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| `GROMACS`_            | GROMACS/2016.4-foss-2                                                         | GROMACS with GPU                                                 |
|                       | 017a-GPU-noMPI                                                                | acceleration. The                                                |
|                       | GROMACS/2016.4-intel-                                                         | -GPU-noMPI-versions                                              |
|                       | 2017a-GPU-noMPI                                                               | are ssmp binaries                                                |
|                       |                                                                               | without support for                                              |
|                       |                                                                               | MPI, so they can only                                            |
|                       |                                                                               | be used on a single                                              |
|                       |                                                                               | GPU node.                                                        |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| `Keras`_              | Keras/2.1.3-intel-201                                                         | Keras with TensorFlow                                            |
|                       | 7c-GPU-Python-3.6.3                                                           | as the backend (1.4                                              |
|                       |                                                                               | for Keras 2.1.3),                                                |
|                       |                                                                               | using the                                                        |
|                       |                                                                               | GPU-accelerated                                                  |
|                       |                                                                               | version of                                                       |
|                       |                                                                               | Tensorflow.                                                      |
|                       |                                                                               | For comparison                                                   |
|                       |                                                                               | purposes there is a                                              |
|                       |                                                                               | identical version                                                |
|                       |                                                                               | using the CPU-only                                               |
|                       |                                                                               | version of TensorFlow                                            |
|                       |                                                                               | 1.4.                                                             |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| `NAMD`_               |                                                                               | Work in progress                                                 |
|                       |                                                                               |                                                                  |
|                       |                                                                               |                                                                  |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| `TensorFlow`_         | Tensorflow/1.3.0-inte                                                         | GPU versions of                                                  |
|                       | l-2017a-GPU-Python-3.                                                         | Tensorflow 1.3 and                                               |
|                       | 6.1                                                                           | 1.4. Google-provided                                             |
|                       | Tensorflow/1.4.0-inte                                                         | binaries were used                                               |
|                       | l-2017c-GPU-Python-3.                                                         | for the installation.                                            |
|                       | 6.3                                                                           | There are CPU-only                                               |
|                       |                                                                               | equivalents of those                                             |
|                       |                                                                               | modules for                                                      |
|                       |                                                                               | comparison. The 1.3                                              |
|                       |                                                                               | version was installed                                            |
|                       |                                                                               | from the standard                                                |
|                       |                                                                               | PyPi wheel which is                                              |
|                       |                                                                               | not well optimized                                               |
|                       |                                                                               | for modern                                                       |
|                       |                                                                               | processors, the 1.4                                              |
|                       |                                                                               | version was installed                                            |
|                       |                                                                               | from a Python wheel                                              |
|                       |                                                                               | compiled by Intel                                                |
|                       |                                                                               | engineers and should                                             |
|                       |                                                                               | be well-optimized for                                            |
|                       |                                                                               | all our systems.                                                 |
+-----------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+

.. include:: ../software/links.rst
