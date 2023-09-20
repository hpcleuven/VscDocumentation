.. _dataremoval:

############
Data removal
############

*************
Removing data 
*************
When a collection or data object does not need to be in Tier-1 Data any more, it can be removed.
This can only be done by an user with 'own' permission on the data object or collection in question.

You can remove data in two ways:

- Moving it to the :ref:`trash collection <trash>` which is the default behavior. From there, you still have some time to recover the data, in case you made a mistake.

- Some clients allow you to specify that you want to force the removal of the data: this means that it is removed permanently, without being moved to the trash collection, and it cannot be recovered.

If you remove a collection, you need to do so recursively in order to remove all its contents as well.

As mentioned :ref:`earlier <architecture>`, Tier-1 Data keeps two copies of each data object (one in Heverlee and one in Leuven) as a protection against hardware failure. 
However, if you remove a data object, all copies of it are removed.  

.. _trash:

********************
The trash collection
********************

When you remove data without force, they are moved to your personal trash collection.
This collection is located at ``/<zone>/trash/home/<username>``.

Inside your trash, the path of the data object(s) or collection you removed is reproduced.
For example, if you remove ``/<zone>/home/chemistry/results.csv``, you can find it back in ``/<zone>/trash/home/<username>/chemistry/results.csv``.

If you remove a data object or collection and an object with the same name and path is already in your trash, 
Tier-1 Data appends a dot and a random number to the filename of the most recently removed object.  

Tier-1 Data automatically removes any objects that remain in trash for more than 14 days.
You can also clean out your trash collection yourself:

- Most clients have a command to remove everything from your trash collection permanently. An example is the ``irmtrash`` command from iCommands. 

- You can also manually remove data from your trash collection as you would from any other collection. This is always considered a forceful removal. 

**********************
Restoring removed data
**********************

If you want to retrieve data from your trash collection, you can move it from the trash to your destination of choice.
Both metadata and permissions will be preserved. 

.. note::
  At the moment, restoring data from trash is not yet possible in the :ref:`mango-portal`.

***************
Troubleshooting
***************

- To remove a collection, you need 'own' access on it and all its contents.
  If you lack 'own' access on any of the contents, the collection cannot be removed entirely.
  However, the process will still try to remove all parts you have 'own' access to.

  In the following example, since Chris doesn't have 'own' access on results.csv,
  only the data object 'data.csv' and the collection 'input' will be removed:

  - chemistry (Chris - own)

    - input (Chris - own)
  
      - data.csv (Chris - own)
  
    - output (Chris - own)
  
      - results.csv (Chris - read)

