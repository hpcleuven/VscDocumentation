.. _ood_pycharm:

PyCharm
-------

PyCharm is a well-known integrated development environment (IDE) for Python offered by `JetBrains <https://www.jetbrains.com/pycharm/>`_. We offer the PyCharm community edition (based on PyCharm modules) as a web-based app via Open OnDemand.

VSC clusters that support this app are:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`


Before you connect
------------------

In case you would like to only develop your Python code or software, you can use PyCharm as a pure editor.
However, if you want to execute your Python scripts interactively, then you need to choose a Python interpreter that contains all the packages which you need at runtime.

PyCharm ships with a default Python (whose version depends also on the version of PyCharm you select from the form). But, such default interpreters contain only the Python standard library. To create your custom Python environment, please refer to the :ref:`Python package management <Python packages>` page.


Launching PyCharm
-----------------

To start a session, you may choose your desired version of PyCharm module. For developing a Python software and for testing a serial Python script, sticking to a single core is sufficient. However, to run, test, debug or benchmark a multi-threaded or multi-processing Python script, you may request additional cores. For running jobs using more than one node (with e.g. ``mpi4py`` or ``dask.distributed``), we recommend :ref:`submitting batch jobs <job submission>`.

Once your session starts, you may `configure your Python interpreter <https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html>`_, and eventually change it to that of your custom environment from the bottom-right menu.
