Tensorboard
-----------

Tensorboard is an interactive app that allows you to visualize and measure different aspects of
your machine learning workflow.
Have a look at the `official guidelines <https://www.tensorflow.org/tensorboard/get_started>`_
for more detailed information.

The Tensorboard interactive session requires you to specify a project (or log) directory in
your submission options.
This is a relative directory starting from your ``$VSC_DATA``.
Beware that you cannot change this directory, once the session is launched.
If you redirect Tensorboard to a wrong folder (typo in path name or missing log files),
Tensorboard fails to start, and your session lands on an error page starting with the message:
'No dashboards are active for the current data set.'.

