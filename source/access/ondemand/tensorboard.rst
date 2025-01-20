TensorBoard
-----------

Tensorboard is an interactive app that allows you to visualize and measure different aspects of
your machine learning workflow.
Have a look at the `official guidelines <https://www.tensorflow.org/tensorboard/get_started>`_
for more detailed information.

TensorBoard log directory
~~~~~~~~~~~~~~~~~~~~~~~~~

The TensorBoard interactive session requires you to specify a log (or project)
directory in your resource options.

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      This is a relative directory starting from your ``$VSC_DATA``.

   .. tab-item:: VUB

      This is an absolute path.

Beware that, once the session is launched, you cannot change this directory.  If
you redirect TensorBoard to a wrong folder (typo in path name or missing log
files), TensorBoard fails to start, and your session lands on an error page
starting with the message:

   No dashboards are active for the current data set.

