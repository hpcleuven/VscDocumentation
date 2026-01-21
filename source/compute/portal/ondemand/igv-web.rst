.. _ood_igv_web:

IGV-Web
=======

``IGV-Web`` is the web version of the
`Integrative Genomics viewer (IGV) <https://igv.org/>`_, which is a
visualization tool for genomical data.

VSC clusters that support this app are:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |KUL|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Genius <genius hardware>`
       * Tier-2 :ref:`wICE <wice hardware>`


Accessing data on HPC storage
-----------------------------

Compared to the web application that is available at `igv.org/app`_,
the ``IGV-Web`` OnDemand app has been customized to facilitate access to
data on (VSC) HPC storage.

If you for example have an (indexed) FASTA file on your ``VSC_SCRATCH``,
you can select it as a reference genome through ``Genome > URL ...``
by entering the absolute file paths in the ``Genome URL`` and ``Index URL``
fields.

The same approach also applies to the other file types in ``IGV-Web``,
such as track files, sample info files and session files. Note that

* environment variables are not expanded and so for example
  ``${VSC_SCRATCH}`` cannot be used as part of those URL inputs,

* exported session URLs and JSON sesion files contain the paths
  to your selected genome and track files,

* in this app you can only *read* from HPC storage, not *write* to it
  (session files therefore can only be stored on your local device),

* the app does not provide access to ``VSC_HOME``.


Saving sessions
---------------

Similar to the instance hosted by the IGV team (`igv.org/app`_),
the ``IGV-Web`` app will not save your current progress automatically,
which means that reloading the tab or closing your browser will clear
your session. You can save your current session in different ways:

* Through the ``Session > Save`` menu, to store it as a JSON file
  on your local device. You can then reopen it later via
  ``Session > Local File ...`` (or via ``Session > URL ...`` in case
  you transferred the file to an HPC storage location).

* Through the ``Share`` menu: copy the generated session URL and save it
  somewhere. Paste the URL in ``Session > URL ...`` to reopen it
  (pasting the URL in a new browser tab will not work).

* Through the ``Bookmark`` menu, which allows you to create a bookmark for
  the generated session URL. Also in this case directly opening the URL
  will not work and you will need to use the ``Session > URL ...`` menu
  instead.


Sharing sessions
----------------

If needed, you may even share such session URLs and session JSON files with
co-workers who also use the present ``IGV-Web`` OnDemand app. This will,
of course, only work if they can also access the associated datasets. On the
Tier-2 clusters at KU Leuven, this typically means that the data needs to be
stored in a shared ``staging`` folder.


Good to know
------------

* As the analysis and rendering work happens in your browser, the Slurm job
  for the app only needs very few resources. These jobs are therefore
  restricted to run on a single core and with only limited memory
  and we recommend that you select a suitable partition such as the
  ``interactive`` partition on ``wICE``.

* You only need a single ``IGV-Web`` session in OnDemand even if you want to
  work with ``IGV-Web`` in multiple tabs. Every time you hit 'Connect', a new
  independent tab will open.


.. _igv.org/app: https://igv.org/app/
