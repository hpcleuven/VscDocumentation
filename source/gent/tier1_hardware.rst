Tier-1 (Hortense) @ HPC-UGent
-----------------------------

.. warning::
    (2021-11-15) This documentation is still being completed,
    as Hortense is being prepared for testing.

    More information and details will be added in the coming days.

General information
==================

*"Hortense"* is the 3rd VSC Tier-1 cluster, following *muk* (hosted by HPC-UGent, 2012-2016)
and *BrENIAC* (hosted by HPC-Leuven, 2016-2022).

The Hortense Tier-1 cluster is available since 2021, is hosted by Ghent University, and maintained and supported by the HPC-UGent team.

Hardware details
================

Hortense consists of 3 partitions:
- The ``cpu_rome`` partition:
   - 294 workernodes, each with:
       - 2x 64-core AMD Epyc 7H12 CPU 2.6 GHz (128 cores per node)
       - 256 GiB RAM (~2GB/core)
- The ``cpu_rome_512`` partition:
   - 42 workernodes, each with:
       - 2x 64-core AMD Epyc 7H12 CPU 2.6 GHz (128 cores per node)
       - 512 GiB RAM (~4GB/core)
- The ``gpu_rome_a100`` partition:
   - 20 workernodes, each with:
       - 2x 24-core AMD Epyc 7402 CPU 2.8 GHz (48 cores per node)
       - 4x NVIDIA A100-SXM4 (40 GB GPU memory), NVLink3
       - 256 GiB RAM (~5GB/CPU core)

Shared infrastructure:
- 3 PB shared scratch storage (Lustre)
- all nodes and storage are interconnected via InfiniBand HDR-100


Support contact
===============

For questions and problems related to Tier-1 Hortense, please contact the central
support address for Tier-1 compute: <a href="mailto:compute@vscentrum.be">compute@vscentrum.be</a>.
