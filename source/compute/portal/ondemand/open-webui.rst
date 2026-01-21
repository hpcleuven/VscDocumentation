.. _ood_open_webui:

Open WebUI
----------

`Open WebUI <https://openwebui.com>`_ is an extensible, self-hosted interface for AI that adapts to your workflow, all while operating entirely offline. The 'Open WebUI' app also launches an `Ollama <https://ollama.com>`_ server inside an isolated network namespace, providing a private and offline interactive environment for running large language models. As a tradeoff you will not be able to interact with Open WebUI's online elements as there is no connection to the internet.


VSC clusters that support the Open WebUI app:

.. grid:: 3
    :gutter: 4

    .. grid-item-card:: |VUB|
       :columns: 12 4 4 4

       * Tier-2 :ref:`Anansi <Anansi cluster>`

Open WebUI runs in a graphical desktop environment, similar to the
:ref:`Desktop app <ood_desktop>`, with Firefox opened in kiosk mode. Keep in mind that for seemless copy/pasting, you should launch the Open WebUI app from a Chromium-based webbrowser (e.g., Google Chrome or Microsoft Edge).

By default the Open WebUI app will use the pre-installed Ollama models located in ``/databases/ollama``. You can change this directory and use your custom models by setting the environment variable ``OLLAMA_MODELS``.

By default the Open WebUI app stores its data and chat history in ``$VSC_HOME/.openwebui``. You can change this directory by setting the environment variable ``OPEN_WEBUI_DATA``.

.. note::

 |VUB| At the moment this app only works with GPU-enabled Ollama. In order to run it you will need to select a GPU or fraction of GPU.

Using new models
~~~~~~~~~~~~~~~~

The easiest way to populate your custom models directory is by pulling models from the `Ollama library <https://ollama.com/library>`_ or from `Hugging Face <https://huggingface.co>`_. Note that Ollama only supports GGUF models, so Hugging Face models in a different format will not work.

To download new models, follow these steps:

#. load an Ollama module, e.g. ``module load ollama/0.11.10-GCCcore-14.2.0``
#. set the ``$OLLAMA_MODELS`` environment variable to your custom directory, e.g., ``OLLAMA_MODELS=$VSC_SCRATCH/ollama``
#. run the Ollama server by executing ``ollama serve``.
#. once the server is running, open a new shell on the same node, load the Ollama module and run ``ollama pull`` to pull in new models.

- From the `Ollama library <https://ollama.com/library>`_: find the model you want, e.g., deepseek-r1:1.5b, and run ``ollama pull deepseek-r1:1.5b``.
- From `Hugging Face <https://huggingface.co>`_: find any GGUF model, e.g., microsoft/Phi-3-mini-4k-instruct-gguf, and run ``ollama pull hf.co/microsoft/Phi-3-mini-4k-instruct-gguf``.

These models will now be available in the Open WebUI app if you use the same ``OLLAMA_MODELS`` directory.
