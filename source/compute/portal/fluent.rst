.. _ood_fluent:

ANSYS Fluent
------------

The Fluent app launches a session limited to a single node for computational fluid dynamics (CFD) simulations using `ANSYS Fluent <https://www.ansys.com/products/fluids/ansys-fluent>`_. Using this app is more interesting for interactive runs or when visualization is involved. If you need to use more than one node, please consider launching Fluent via :ref:`batch jobs <job submission>`.

The VSC clusters that support the Fluent app are:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`


Who can use Fluent
------------------

All VSC users who are member of one of the KU Leuven/UHasselt license groups for Fluent have the rights to use Fluent. Once a VSC user joins one of such groups, he/she will also be automatically added to the ``leuven_fluent`` autogroup. You may verify that by executing the ``groups | grep leuven_fluent`` command. Once that happens, the logo of the ANSYS Fluent app will appear in the user's OnDemand dashboard.


Before you connect
------------------

|KUL| You need to know the address of an ANSYS license server in the form of ``port@hostname``. The license server must be reachable from KU Leuven Tier-2 clusters. Contact your supervisor and/or your local IT services to provide you with such details. Make sure that your license allows you to run Fluent on the KU Leuven Tier-2 hardware. You also need to make sure that the license server can deliver sufficient tokens for your compute job (depending on the number of cores/processes you want to launch).


Launching Fluent
----------------

|KUL| To start a Fluent session, you may choose your desired version of the Fluent module from the drop-down list.
Depending on the problem at hand and the desired numerical precision, you may also choose the type of solver from the next drop-down menu.
It is mandatory to provide the ANSYS license server address in the text box for the ``ANSYSLMD_LICENSE_FILE`` environment variable. Depending on the configuration of the license server, some users might need to additionally specify the ``ANSYSLI_SERVERS`` in the next field.
Your Fluent sessions will be limited to using a single node, but it can be interesting to test whether your application runs sufficiently faster on different node architectures (see the technical specifications of :ref:`Genius <genius hardware>` and :ref:`wICE <wice hardware>` clusters) and for various core counts.
