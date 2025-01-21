.. _t1data_metadata_tech_spec:

##########################################
Metadata schemas: technical specifications
##########################################

This article describes how the metadata schemas used in the ManGO portal
are stored and represented, from the folder structure that supports the
schemas lifecycle to the JSON format that codes the different fields and
their characteristics.

`Section 1 <#sec-lifecycle-tech>`__ gives a brief overview of the lifecycle
of a schema and how that is coded into the folder structure and filename
system. `Section 2 <#sec-json>`__ follows with a technical description
of the JSON file that represents each version of a specific schema,
followed by `Section 3 <#sec-items>`__, in which the different kinds of
fields are described. Finally, `Section 4 <#sec-full>`__ shows an
example of the JSON file for a draft version.

.. note::
    
    If you would like to design your own metadata schema for Tier-1 Data
    without using the Metadata Schema Manager, you should focus on
    `Section 3 <#sec-items>`__ and create a JSON file that matches the
    value of ``properties`` in the main JSON. On upload to Tier-1 Data, you
    will be able to provide the name and title of your schema, and the
    versioning will be taken care of in the backend.

Before we go into these sections, here is some useful vocabulary:

(metadata) schema
   A set of rules to apply metadata in a systematic way; a collection of
   *fields* with format instructions for a specific AVU.

schema version
   A specific version of a schema, with a given status. Multiple
   versions of a given schema may co-exist, only one can be in a
   ‘published’ status, meaning that it can be applied to data.

field
   A component of a schema with instructions for a specific AVU or for
   multiple AVUs that have the same name (or prefix, in the case of a
   composite field).

to apply a schema / annotate with a schema
   The action of adding or editing metadata of a data object or
   collection based on a given schema.

.. _sec-lifecycle-tech:

Lifecycle and folder structure
==============================

In the Tier-1 Data infrastructure, schemas belong to “realms”, such as
projects (other implementations of this infrastructure could extend this
to personal collections). When designing a schema, one must first
select a realm; at the moment, a schema designed within a certain realm
can only be used to apply metadata to data of that realm.

For each realm, there is a directory “schemas” that contains all the
schemas designed within it. Each schema has its own subdirectory, which
contains one JSON file for each existing version of the schema. In the
example used for illustration in this article, the directory would be
called “book”, which is also the ``schema_name`` attribute in the JSON
file of each version.

There can be any number of versions of a schema, following `semantic
versioning <https://semver.org/>`__ (although for now only major versions are supported), and each version can have
one of three states: “draft”, “published” or “archived”.

The **draft** status is the first, default state of a schema, although
it is possible to publish a schema directly without saving the draft
first. It can be edited, viewed and deleted, but it cannot be applied.

Once a draft is **published**, it cannot be edited or deleted anymore,
but it can be viewed and, more importantly, it can be applied. Attempts
to edit the published version of a schema will result in the creation of
a new draft with a higher version number. If this draft is then
published, the current published version is **archived**.
Moreover, the metadata schema manager also allows you to clone (or “copy”) a
published schema into a draft of a whole new schema with a
different name and version 1.0.0.

Archived versions cannot be edited, deleted or used. At the moment they
cannot be viewed either, but this will be addressed in the future. A
published version can also be purposefully archived, without having to
publish a draft that replaces it. You can still have data with metadata
based on an archived version of a schema, but if you try to reapply the
metadata schema you will only be able to use the current published
version, overriding any differences between the version originally used
for annotation and the current version.

`Table 1 <#tbl-lifecycle>`__ summarizes what can be done with a metadata
schema version depending on its stage.

.. list-table:: Table 1: Summary of metadata schema version states in Tier-1 Data.
    :name: tbl-lifecycle
    :header-rows: 1

    * -  
      - draft
      - published
      - archived
    * - when:
      - on creation
      - on publication
      - by archiving
    * - can be edited
      - ✔
      - ❌
      - ❌
    * - can be viewed
      - ✔
      - ✔
      - ✔
    * - can be applied
      - ❌
      - ✔
      - ❌
    * - can be deleted
      - ✔
      - ❌
      - ❌


The name of a file corresponding to a version of a schema includes the
name, version and (unless archived) the status, accordign to the
following convention: ``{schema_name}-v{version}(-{status}).json``, with
``status`` being one of “draft” or “published”. For example, when we
first create the “book” schema used for illustration in this document, a
file will be created called “book-v1.0.0-draft.json”, which will be
stored inside the “book” subdirectory of the “schemas” directory. As
shown in `Section 2 <#sec-json>`__, the version and status are also
registered as attributes inside the JSON file. Once we are ready to make
it available for annotation, we can publish the version in the metadata
schema manager, which will update the status inside the JSON file and
rename the file itself as “book-v1.0.0-published.json”. If we want to
create a new version, this will generate a new file
“book-v2.0.0-draft.json”, which will have the same name, title and realm
as the previous version but a different version number and status.
Publishing this new version will change its status and rename the file
as “book-v2.0.0-published.json”, but it will also archive the first
version. This means that the older file will become “book-v1.0.0.json”
(without a suffix indicating the status) and change the ``status``
inside the JSON file to “archived”.

As mentioned above, if we have already annotated data using version
1.0.0 of the “book” schema, that metadata will remain unchanged unless
we try to update it. In that case, fields that have not changed between
versions will be untouched, whereas fields that were deleted in version
2.0.0 will be permanently deleted, and those that were added will become
available.

.. _sec-json:

JSON format
===========

A specific version of a metadata schema will be stored in a json file
with a series of key-value pairs.

.. code-block:: 

   {
       "schema_name" : "book",
       "version" : "1.0.0",
       "status" : "draft",
       "properties" : {...},
       "title" : "Book schema as an example",
       "edited_by" : "username",
       "realm" : "project_collection",
       "parent" : ""
   }

The ``schema_name`` attributes indicates the name or ID of the schema,
i.e. the namespace of the AVUs assigned via this schema. In this
example, all the attribute names generated with this schema will be
prefixed with ``mgs.book.``, where ``mgs`` refers to “ManGO schema”. The
``status`` attribute refers to the state in the lifecycle as described
in `Section 1 <#sec-lifecycle-tech>`__, and with ``version`` they constitute
the main characteristics to distinguish between versions of a schema.

The ``title`` of a schema is used in the UI of the schema manager and
when implementing schemas as a the user-facing label. The ``edited-by``
attribute is self-explanatory. As introduced above, ``realm`` refers to
the space (such as a project) to which the schema belongs and in which
it can be used. The ``parent`` attribute is relevant when a schema has
been initialized as clone of an existing schema; in that case, it
records the name and version of the schema it originated from.

The value of the ``properties`` element is itself a series of key-value
pairs indicating fields of the metadata schema. The key is the ID of the
field (how it is defined in the namespace of the schema) and the value
is itself a series of key-value pairs describing the field. The format
of these objects is documented in `Section 3 <#sec-items>`__.

The order of the attributes is not important, but the order of the
*fields* inside ``properties`` will define the order they take
when rendering the form used to assing metadata from the schema.

.. _sec-items:

Schema fields
=============

There are three main kinds of fields that can be included in a metadata
schema: simple fields, multiple-choice fields and composite fields.
Simple fields, described in `Section 3.2 <#sec-simple>`__, include any
form of text or numeric input for which a pattern or range may be
defined but not, strictly speaking, the possible values. It also
includes single (boolean) checkboxes. Multiple-choice fields
(`Section 3.3 <#sec-multiple>`__) include any field that provides a
specific, limited selection of possible values. Finally, the composite
fields, described in `Section 3.4 <#sec-object>`__, are mini-schemas:
collections of fields of other kinds related to each other.

Each field is represented by a key-value pair in the ``properties``
element of the schema JSON. Before going through the specific
characteristics of each kind of field, `Section 3.1 <#sec-attr>`__
offers an overview of their common attributes.

.. _sec-attr:

General Attributes
------------------

The following attributes are used in at least two different kinds of
fields.

title
   All fields in a metadata schema must include the ``title`` attribute,
   which provides a user-facing, human-readable label. While the ID or
   name of the field is used in the AVU itself, the title is used in the
   schema manager, during annotation and when we inspect the existing
   metadata in the ManGO portal.

type
   All fields need a ``type`` attribute indicating the kind of field
   they represent. The possible values are discussed in the sections
   dedicated to each type of field.

required
   Simple fields and single-value multiple-choice fields may contain an
   optional boolean ``required`` attribute indicating whether the field
   is required when assigning metadata from the schema. A required field
   needs to be filled for the metadata form to be submitted. If this
   attribute is missing, it is read as “false”.

default
   Simple fields and single-value multiple-choice fields, *if required
   is true*, may also contain a ``default`` attribute providing a
   default value for the field.

In the metadata schema manager, the ``title``, id and (if relevant)
``default`` attributes are provided via text input fields and
``required`` via a switch button. In contrast, ``type`` is defined by
the choice of field in the metadata schema manager, except for simple
fields, in which there is an additional dropdown to select among its
various subtypes.

.. _sec-simple:

Simple fields
-------------

The prototypical example of a simple field is a text field, such as the
example below. They key “title” indicates that, when assigning metadata
via this field, the name will be ``msg.book.title``.

.. code-block:: 

   "title" : {
       "type" : "text",
       "title" : "Book title",
       "required" : true
   }

The ``type`` attribute can have one of several different values, to be
selected from a dropdown menu when designing an instance of this field.
Next to the basic “text” value, other standard inputs are available that
provide minimal validation: “date”, “time”, “email”, or “url”. For a
longer-form, non-restricted text output, the “textarea” value is also an
option; in that case, it is not longer possible to provide a default
value.

For numeric inputs, the possible types are “integer” or “float”. Fields
with these types also have two optional key-value pairs indicating the
range of allowed values:

.. code-block:: 

   "copies_published": {
       "type": "integer",
       "title": "Number of copies published",
       "minimum": "100"
   },
   "market_price": {
       "type": "float",
       "title": "Market price (in euros)",
       "minimum": "0.99",
       "maximum": "999.99"
   }

Finally, it is also possible to create an individual checkbox (with
``type`` “checkbox”), which takes the value “true” when checked and no
value when unchecked.

Except for the “checkbox”, all the other simple field types can
additionally have a ``repeatable`` attribute. If “true”, the field can
be copied when assinging the metadata to a collection or data object, in
order to generate multiple AVUs with the same attribute name and
different values.

In the metadata schema manager, minimum and maximum values for numeric
types can be provided via numeric input fields, whereas the
``repeatable`` attribute is selected via a switch button.

.. _sec-multiple:

Multiple-choice
---------------

Multiple-choice fields are indicated by providing the “select” value to
the ``type`` attribute. They are characterized by a restricted selection
of possible values for the metadata field they define. These values are
indicated as a list in the ``values`` attribute:

.. code-block:: 

   "ebook": {
       "type": "select",
       "multiple": false,
       "ui": "radio",
       "values": [
           "Available",
           "Unavailable"
           ],
       "title": "Is there an e-book?",
       "required": true
   }

The metadata schema manager offers two types of multiple-choice fields:
single-value and multiple-value. The former represents radio buttons and
classic dropdowns in which the user must choose up to one of the
possible options. The latter, in contrast, represents checkboxes and
dropdowns in which the user may choose more than one of the possible
options. This choice is coded in the ``multiple`` attribute, which takes
the “false” value in the first case and “true” in the second.

In addition, the ``ui`` attribute indicates what the field will look
like in the form used to apply the schema. Its value can be “dropdown”,
“checkbox” (if ``multiple`` is “true”) or “radio” (if ``multiple`` is
“false”). This choice is made via a switch button in the metadata schema
manager.

In the metadata schema manager, each value of the list of options must
be provided manually and then can be edited, deleted or reordered. It is
not yet possible to import a list of values from an external source.

.. _sec-object:

Composite field
---------------

Composite fields are miniature schemas nested inside schemas (or other
composite fields) and are meant to bring together multiple fields that
conceptually come together. They take the ``type`` “object”, which is
assigned when the composite field is selected in the metadata schema
manager. Like for schemas, they have a ``properties`` attribute
describing the fields it is composed of.

.. code-block:: 

   "author": {
       "type": "object",
       "title": "Author",
       "properties": {
           "name": {
               "type": "text",
               "title": "Name and Surname",
               "required": true
           },
           "age": {
               "type": "integer",
               "title": "Age",
               "minimum": "12",
               "maximum": "99"
           },
           "email": {
               "type": "email",
               "title": "Email address",
               "required": true,
               "repeatable": true
           }
       }
   }

Composite fields cannot be required: this is a property of their
components. Currently, they cannot be repeatable either, but that might
change in the future.

In practical terms, composite fields generate a nested namespace for the
AVUs they contain. As an example, the fields shown in
`Section 3.2 <#sec-simple>`__ would be coded with the names
``msg.book.title``, ``msg.book.copies_published`` and
``msg.book.market_price``, and the one shown in
`Section 3.3 <#sec-multiple>`__ as ``msg.book.ebook``. In contrast, the
composite field shown above results in AVUs with attribute names
``msg.book.author.name``, ``msg.book.author.age`` and
``msg.book.author.email``.

.. _sec-full:

Full example
============

This section contains the full example of a JSON file that represents a
schema draft.

.. code-block:: sh
   :linenos:

   {
       "schema_name": "book",
       "version" : "1.0.0",
       "status" : "draft",
       "properties": {
           "title": {
               "type": "text",
               "title": "Book title",
               "required": true
           },
           "cover_colors": {
               "type": "select",
               "multiple": true,
               "ui": "checkbox",
               "title": "Colors in the cover",
               "values": [
                   "red",
                   "blue",
                   "green",
                   "yellow"
               ]
           },
           "publisher": {
               "type": "select",
               "multiple": false,
               "ui": "dropdown",
               "values": [
                   "Penguin House",
                   "Tor",
                   "Corgi",
                   "Nightshade books"
               ],
               "title": "Publishing house",
               "required": true
           },
           "author": {
               "type": "object",
               "title": "Author",
               "properties": {
                   "name": {
                       "type": "text",
                       "title": "Name and Surname",
                       "required": true
                   },
                   "age": {
                       "type": "integer",
                       "title": "Age",
                       "minimum": "12",
                       "maximum": "99"
                   },
                   "email": {
                       "type": "email",
                       "title": "Email address",
                       "required": true,
                       "repeatable": true
                   }
               }
           },
           "ebook": {
               "type": "select",
               "multiple": false,
               "ui": "radio",
               "values": [
                   "Available",
                   "Unavailable"
               ],
               "title": "Is there an e-book?",
               "required": true
           },
           "genre": {
               "type": "select",
               "multiple": true,
               "ui": "dropdown",
               "values": [
                   "Speculative fiction",
                   "Mystery",
                   "Non-fiction",
                   "Encyclopaedia",
                   "Memoir",
                   "Literary fiction"
               ],
               "title": "Genre"
           },
           "publishing_date": {
               "type": "date",
               "title": "Publishing date",
               "required": true,
               "repeatable": true
           },
           "copies_published": {
               "type": "integer",
               "title": "Number of copies published",
               "minimum": "100"
           },
           "market_price": {
               "type": "float",
               "title": "Market price (in euros)",
               "minimum": "0.99",
               "maximum": "999.99"
           },
           "website": {
               "type": "url",
               "title": "Website"
           },
           "synopsis": {
               "type": "textarea",
               "title": "Synopsis"
           }
       },
       "title": "Book schema as an example",
       "edited_by" : "username",
       "realm" : "project_collection",
       "parent" : ""
   }

