TensorBoard
-----------

Tensorboard is an interactive app that allows you to visualize and measure different aspects of
your machine learning workflow.
Have a look at the `official guidelines <https://www.tensorflow.org/tensorboard/get_started>`_
for more detailed information.

TensorBoard log directory
~~~~~~~~~~~~~~~~~~~~~~~~~

Before starting the TensorBoard session, make sure to specify a log directory in
the resources form.

.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      The log directory is a relative directory starting from your ``$VSC_DATA``.

   .. tab-item:: VUB

      The log directory is an absolute path.

.. admonition:: Notes

   - Once the session is launched, you cannot change this directory.  If you
     redirect TensorBoard to a wrong folder (typo in path name or missing log
     files), TensorBoard fails to start, and your session lands on an error page
     starting with the message:

        No dashboards are active for the current data set.

   - If you experience problems with using the TensorBoard app, please consult
     the `Tensorboard FAQ
     <https://github.com/tensorflow/tensorboard/blob/master/README.md#frequently-asked-questions>`_
     before :ref:`contacting user support <user support VSC>`.


