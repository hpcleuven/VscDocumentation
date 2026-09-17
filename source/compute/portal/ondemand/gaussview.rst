GaussView
---------

The GaussView app will launch `GaussView <https://gaussian.com/gaussview6>`_
in a minimal desktop environment in an interactive job.

VSC clusters that support the GaussView app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`
       * Tier-2 :ref:`Hydra <Hydra cluster>`

Who can use GaussView
~~~~~~~~~~~~~~~~~~~~~

|VUB| Only vsc1* users (affiliated with VUB) who are members of the
``brusselall`` group have rights to use the GaussView app.

Launching GaussView
~~~~~~~~~~~~~~~~~~~

All documentation for the :ref:`ood_desktop` app also applies to the GaussView app.

.. note::

   There is an issue with the GaussView graphical interface when setting
   the compression level to zero, causing it to crash when performing certain
   actions. Make sure to set the compression level to a value that is higher
   than zero to avoid this issue.
