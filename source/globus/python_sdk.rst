.. _sdk:

============================
Python SDK
============================

The Python Software Development Kit (SDK) allows users to manage data via their own scripts or tools built on Globus.  
This provides a lot of opportunities for automating workflows.  


Getting started with the Python SDK
-----------------------------------

1. Registering your app

Before creating your own scripts or tools on top of Globus, you first need to register them.  

To do so, go to the `developers page <https://developers.globus.org/>`_ and click on 'Register your app with Globus'. 

First, you register your project, or select an existing one. 
A project is a collection of clients with a shared list of administrators. Projects let you share the administrative burden of a collection of apps.

Then, on the dropdown next to this project, click on 'Add new app'.  
Give your app a name and, except if your app is a web app hosted on a secure server, check the box 'Native App'.  

For more information about settings when registering an app, see `Registering an App <https://docs.globus.org/api/auth/developer-guide/#register-app>`_.

When you register an app, it gets a **client ID**. This will be used to authenticate in the next steps.  

2. Installation

The Python SDK can be installed with pip as follows::

      pip install globus-sdk

Authentication
--------------

To start working with the Globus SDK, you need to instantiate a NativeAppAuthClient object with your client ID::

      import globus_sdk
      auth_client = globus_sdk.NativeAppAuthClient("<your_ID>")

The Python SDK needs formal consent to take any actions for a user.
By default, this is handled by Globus itself.
The following code snippet provides a link for the user to log in and fetch an authentication code::

      auth_client.oauth2_start_flow()
      authorize_url = auth_client.oauth2_get_authorize_url()
      print(f"Please go to this URL and login:\n\n{authorize_url}\n")
      auth_code = input("Please enter the code here: ").strip()
      

From this, tokens can be derived for further actions::

      token_response = auth_client.oauth2_exchange_code_for_tokens(auth_code)
      globus_transfer_data = token_response.by_resource_server["transfer.api.globus.org"]
      TRANSFER_TOKEN = globus_transfer_data["access_token"]  


Searching collections
---------------------

To manage data in a certain collection, you need to have the collection ID. 
This can be done via the Python SDK as well. 

.. Note::
      You can also look up the ID of collections via the :ref:`globus-web` or the :ref:`cli`.

We wrap the transfer token we acquired earlier in an authorizer object::

      authorizer = globus_sdk.AccessTokenAuthorizer(TRANSFER_TOKEN)

Next, we create a TransferClient object::

      transfer_client = globus_sdk.TransferClient(authorizer=authorizer)

With this object, we can search for endpoints and collections.
We can search for specific keywords::

      print("Found endpoints:")
      for ep in transfer_client.endpoint_search(filter_fulltext="VSC KU Leuven"):
            print("[{}] {}".format(ep["id"], ep["display_name"]))

Or we can list all of our own endpoints::

      print("My Endpoints:")
      for ep in transfer_client.endpoint_search(filter_scope="my-endpoints"):
            print("[{}] {}".format(ep["id"], ep["display_name"]))

This way, you can find the ID's of collections, which are needed for transferring data to/from them. 

.. warning::

    The search function of the Globus Python SDK shows both endpoints and collections matching your query.

    While collections are directly accessible, endpoints are not, and this might cause confusion.

    Therefore, if you search for endpoints managed by the VSC, we recommend you search for the names in the table of :ref:`globus-available-collections`. 



Adding scopes
---------------------------

In the section 'Authentication', you saw how to request consent of the user.  
However, this consent was general.  

To transfer data between managed collections (like those of the VSC), we have to request the user's consent for both collections specifically.
This is done by creating a scope object to be used by the authentication process. 

.. Note::
      You only have to create scope objects for collections that require extra authentication (which is most managed collections).  
      There are some collections to which every user has access by default:
      
      - Globus tutorial endpoint 1
      - Globus tutorial endpoint 2
      - Their own local endpoints
      - ...

      If during this section, you get an error that looks like this::

            client_id=<your_client_id> requested unknown scopes: ['https://auth.globus.org/scopes/ddb59aef-6d04-11e5-ba46-22000b92c6ec/data_access']
      
      it is likely that you have requested a scope for a collection you didn't need it for. 


In the section 'Authentication', we started the authentication without explictly providing a scope::
      
      auth_client.oauth2_start_flow()

When we want to transfer from e.g. 'VSC VUB Tier2' to 'VSC KU Leuven tier2 scratch', we need to create a scope which includes these two collections.

We start from a TransferScopes object and make it mutable. Then, we add consent for data access to the two collections::

      from globus_sdk.scopes import GCSCollectionScopeBuilder, TransferScopes

      transfer_scope = TransferScopes.make_mutable("all")

      # we need the ID's of both endpoints
      KULeuven_tier2_scratch = "872a58ab-02b9-4233-a3e0-f017ed8ab090"
      VUB_tier2 = "2d1d4873-a849-4b9c-bd34-2034a2163003"

      # adding the endpoints to the scope
      transfer_scope.add_dependency(
            GCSCollectionScopeBuilder(KULeuven_tier2_scratch).data_access, optional=True
      )
      transfer_scope.add_dependency(
            GCSCollectionScopeBuilder(VUB_tier2).data_access, optional=True
      )

Now, we can use this scope to initiate our session::

      auth_client.oauth2_start_flow(requested_scopes=[transfer_scope])

Apart from this, the authentication process remains the same as seen earlier.  


Transferring data
----------------

To transfer data from one collection to another, we first need to authenticate and require consent for the source and destination collection, as show in the sections 'Authentication' and 'Adding Scopes'.   
 
Next, we instantiate an authorizer and transfer client::

      authorizer = globus_sdk.AccessTokenAuthorizer(TRANSFER_TOKEN)
      transfer_client = globus_sdk.TransferClient(authorizer=authorizer)

After that, we create a transfer task::

      task_data = globus_sdk.TransferData(
            # we specify the transfer client, source collection and destination collecion
            transfer_client, VUB_tier2, KULeuven_tier2_scratch
      )

Then, we add data to the transfer::

      task_data.add_item(
            "/path/to/file/on/VUB/tier2",  # source
            "/path/to/destination/on/Kuleuven/tier2",  # destination
      )

Instead of files, you can also transfer entire directories.  
In that case, you need to add `recursive=True` to the `add_item` method::

      task_data.add_item(
            "/path/to/directory/on/VUB/tier2",  # source
            "/path/to/destination/on/Kuleuven/tier2",  # destination
            recursive=True
      )

Lastly, we submit the transfer request, and print the task ID::

      task_doc = transfer_client.submit_transfer(task_data)

      # we can also get the ID of the task
      task_id = task_doc["task_id"]
      print(f"submitted transfer, task_id={task_id}")


This transfer can be followed up via the 'Activity' tab of the `Web Interface`_.


Acquiring longer authentication
--------------

In the workflow we have shown so far, users need to log in to Globus every time they use the script/client in question to acquire a token.

These tokens have a short lifespan, but should be enough for any process running shorter than a day. 

If you want to be able to use your client multiple times without authenticating again every time, you can try to store the tokens and reuse them to authenticate.
Globus has created a TokenStorage class to handle this. For more information, see the `documentation page on TokenStorage <https://globus-sdk-python.readthedocs.io/en/stable/tokenstorage.html>`_.

If you store the tokens, they will still be invalid after a day. 
To solve this, you can use refresh tokens.
Clients that use refresh tokens will automatically request a new token once the previous one expired, without manual intervention.  
This mechanism can also be combined with the aforementioned TokenStorage.

You can find more information about refresh tokens on the `tutorial page of the documentation <https://globus-sdk-python.readthedocs.io/en/stable/tutorial.html#step-5-do-a-login-flow-with-refresh-tokens>`_.  


.. warning::

    Storing tokens poses a risk, since intercepted tokens allow others to manage your data without authenticating.  

    Therefore, we only recommend using these mechanisms

      - If you have a process which runs longer than a day.
      - If you have a process which needs to run regularly without human intervention. 

    Tokens always need to be stored in a secure way. 

More information
--------------

This short guide only demonstrated part of what the Globus Python SDK is capable of. 

For more documentation about the globus Python SDK, see the official `Globus Python SDK documentation`_.

You can also find useful `example scripts <https://globus-sdk-python.readthedocs.io/en/stable/examples/index.html>`_ there. 


.. include:: links.rst