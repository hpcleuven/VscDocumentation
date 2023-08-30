# Style Guide

The VSC documentation is written in reStructuredText (RST) format and rendered
into HTML with Sphinx. This system has two main advantages:

* the web pages can be fully formatted in text, allowing for simple version control
* the render results in a folder with a collection of static HTML pages

## Features

There are a few extensions and customizations added to Sphinx that provide the
following features:

1. **[PyData Theme](https://pydata-sphinx-theme.readthedocs.io)**
    - modern responsive theme for Sphinx
    - adapts to different screen formats
    - top bar with custom navigation, search box and links
    - left side-bar showing the `toctree` navigation and that can be fully customized
    - right side-bar showing in-page navigation
    - includes and supports [FontAwesome](https://fontawesome.com)
1. **[Sphinx-Design](https://sphinx-design.readthedocs.io)**:
    - provides extra directives to organize/present information in the document
    - adds directives `tab-set` and `tab-item` to add tabbed content
    - adds directives `grid` and `card` to create groups of cards
    - adds directive `button-link` to create colorful buttons, which can be
      used for special links
    - adds the role `bdg` to add colorful badges with text
    - adds the role `fas` to insert icons from [FontAwesome](https://fontawesome.com)
1. **[sphinx-reredirects](https://documatt.gitlab.io/sphinx-reredirects/)**
    - creation of redirect URLs in the documentation
1. **[sphinx-notfound-page](https://sphinx-notfound-page.readthedocs.io/)**
    - custom 404 page

## Documentation Structure

Every document in the documentation must be included in the TOC tree to be part
of its structure. This makes the documents visible in the navigation elements
of the website, allowing users to organically find them.

Therefore, any new document added to the document must also be listed in the
[toctree directive](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree)
of some other document.

Simplified structure of the documentation

* **Accounts and access** (folder `access`)

    Main location for information related to VSC accounts, authentication
    methods, connecting to platforms and account management.

* **Research data** (folder `data`)

    Main location for information about data management. Description of storage
    solutions in VSC, moving data in and out of our platforms and sharing data
    with other users. 

* **Compute**

    Information about the HPC platform of VSC. Tier-1 and tier-2 clusters on all sites.

    * Infrastructure (folders per site)

        Description of the hardware and policies in application on each VSC site.

    * Jobs (folder `jobs`)

        Documentation about job scripts and job management in the clusters.

    * Software (folder `software`)

        Documentation about how to use specific software in the HPC.

* **T1-Cloud** (folder `cloud`)

    Main location for the documentation of the T1-Cloud platform.

* **T1-Data** (folder `data`)

    Direct access to the documentation of the T1-Data platform. Part of the
    *Research Data* section in the `data` folder.

* **FAQs**

    Page with links to documents answering common issues and questions.
    Documents explaining a FAQ are specific to the FAQ section, *i.e.* they are
    part of the TOC tree of the main `faq.rst` document. However, each of those
    documents is located inside one the folders of one the aforementioned
    section, depending on the subject they cover. For instance, documents with
    FAQs about VSC accounts and access are located inside the `access` folder,
    although they are part of the FAQ TOC tree.

## Site-specific information

There are two main ways to organize and show information that is specific to
some VSC sites:

* [Tabbed panels](#tabbed-panels) are useful for situations where there is
  information to be shown for many VSC sites and each site can have specific
  information.

  Example: [Applying for your VSC account](source/access/vsc_account.rst?plain=1#L19)

* [Badges](#badges) are useful for situations where information that is general
  needs a remark that a applies to one or a few VSC site. We have pre-defined
  one badge for each VSC site: `|KUL|` for KU Leuven, `|UA|` for UAntwerp,
  `|UG|` for UGent and `|VUB|` for VUB.

  Example in a note: [TurboVNC](source/access/turbovnc_start_guide.rst?plain=1#L23)

  Example in text: [MFA](source/access/mfa_login.rst?plain=1#L6)

# Code formatting

All Sphinx formatting options can be applied in all RST documents of the
documentation. The basics are covered in the
[reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

## Headers

Sphinx is flexible on the formatting of headers. Hence, we defined the
following convention to homogenize the headers in the VSC docs:

```
###########################
Document title - Top header
###########################

****************
Sub-title Header
****************

Section Header
==============

Sub-section header
------------------
```

Note: Prepending [FA icons](#fontawesome) is safe, they do **not** count as
characters of the header and will not be part of their anchors.

## Lists

⚠️ Warning: indentation is very strict!

In Sphinx indentation has to follow the spacing established by the top element
of the current group. In the case of lists, this means that different types of
lists have different indentations:

* unordered list `* `: 2 spaces
* ordered list `1. `: 3 spaces
* definitions `some_text`: 4 spaces

```
definition A
    explanation text

definition B
    explanation text

    1. order item one
       * unorder item one
         * nested item one
       * unorder item two
       * unorder item three
    2. order item two
```

## Links

Automatic generation of implicit targets is disabled to avoid name collisions.
There are already multiple sub-sections in different parts of the documentation
that happen to have the same header. Therefore, all targets have to be
explicitly defined.

```
.. _intro_to_sphinx:

Introduction to Sphinx
======================

```

Once the section has a unique target, it can be linked to (*aka* referenced)
using ``:ref:`target_name` `` or ``:ref:`link_label <target_name>` ``.

Links to external websites can be directly added inline with `` `link_label
<https://url.com>`_ ``. This will also add a target for this URL, which might
also collide with existing targets. In such a case, use a double `__` at the
end. This will disable the target for this link. *e.g.*
`` `link_label <https://url.com>`__ ``

URLs that are used multiple times can be defined a single time in
[`conf.py`](source/conf.py) as a named reference that can be reused
in the documentation files.

```
[conf.py]

.. _VSC account page: https://account.vscentrum.be/
```

Then you can inject that link directly in the text and it will be rendered as a
link to the defined URL using the name of the reference as label.


```
[example.rst]

Check the `VSC account page`_.
```

Using the URL from a named reference but changing its label is also possible.

```
[example.rst]

Check `your account page <VSC account page_>`_.
```

### Link Buttons

It is also possible to create link buttons. This is useful for special links.
The configuration of link buttons is described in the
[Link Buttons](https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#buttons)
documentation of sphinx-design.

## Code Blocks

We use the following convention to distinguish between two types of code blocks

* Commands in a shell: use a regular code block with an optional caption
  describing its contents

```
.. code-block::
   :caption: Example to list all modules of Python

   module spider Python
```

* Contents of a file: use a code block with line numbers (and optional caption)

```
.. code-block:: text
   :caption: Example of job epilog showing job resources
   :linenos:

   Resources Requested: walltime=00:05:00,nodes=1:ppn=1,mem=1gb,neednodes=1:ppn=1
   Resources Used: cput=00:01:19,vmem=105272kb,walltime=00:01:22,mem=17988kb,energy_used=0
```

Code highlighting in code blocks is defined globally in many documents to
*shell*. This can be done with the `highlight` directive:

```
.. highlight:: shell
```

The code highlight can be set individually in the `code-block` directive as
well (overwrites global `highlight`):

```
.. code-block:: python
   :linenos:

   import matplotlib
   matplotlib.use('TkAgg')
```

⚠️ Warning: indentation is very strict!

In Sphinx indentation has to follow the distance established by the top element
of the block. In this case, `.. code-block::` is a directive and the
indentation set by all directives is 3 spaces. Any extra spaces will be shown
inside the codeblock, before each code line, which will make it hard to copy
paste the code out of the documentation.

## Figures

Images should be always added to the document with the `.. figure:` directive.
Figure are automatically centered, scaled and can have captions.

```
.. figure:: some_figure.png
   :alt: some figure

   Capion of some figure

```

⚠️ Avoid using the `.. image:` directive, which can cause rendering issues.

## Tabbed Panels

Information can be organized in tabs using the `tab-set::` directive. This is
specially useful to show site-specific information in a compact manner.

```
.. tab-set::

   .. tab-item:: KU Leuven/UHasselt

      Information specific to KU Leuven/UHasselt 

   .. tab-item:: UGent

      Information specific to UGent

   .. tab-item:: UAntwerp (AUHA)

      Information specific to UAntwerp

   .. tab-item:: VUB

      Information specific to VUB
```

## Grids and Cards

It is possible to present some information inside its own frame. These frames
(*aka* cards) can be customized and easily organized in a flexible grid. Each
card in a grid can contain any amount of text formatted in the same way as any
other part of the document (including lists and code blocks). Optionally, cards
can have a header and a footer; colored backgrounds and images.

All formatting options are described in the documentation of Sphinx-Design:
* [Grids](https://sphinx-design.readthedocs.io/en/latest/grids.html#grids)
* [Cards](https://sphinx-design.readthedocs.io/en/latest/cards.html#cards)

Examples in our documentation are:

* [grid of sections in the front page](source/index.rst)
* [grid of supported features per site](source/jobs/clusters_slurm.rst)
* [grid of sections per OS](source/access/generating_keys.rst?plain=1#L51)

## Level of severity

There are two main ways to convey messages with different levels of severities,
such as warnings, important notes or optional instructions.

### Admonitions

Renders the text in box with a header element indicating the type of
message. Added with specific directives in the code.

* Note: `.. note::`
* Warning: `.. warning::`
* See also: `.. seealso::`

Example:

```
.. note::

   Some additional information giving more insight.

```

### Badges
    
Badges are in-line elements with a very short text and colored background.
They serve to flag in a clear way any special trait of the text following
the badge.

All configuration options are described in
[Badges](https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#badges)
in the documentation of sphinx-design.

We have set the following global substitutions for badges to harmonize their
use in our website:

* `|Recommended|`: a recommended option
* `|Optional`: an optional step in a instruction list
* `|Example|`: an example
* `|Warning|`: a warning message less prominent than the `.. warning::` admonition
* `|Alert|`: an alert
* `|Info|`: a note less prominent than the `.. note::` admonition

## FontAwesome

[FontAwesome](https://fontawesome.com) is a CSS font with more than a thousand
icons. CSS fonts are purely applied as part of the style of the web page and do
**not** alter the contents of the document (as any regular text with a font
would do). This allows to easily add graphical content to our web pages without
having to work with image files or complex CSS instructions. Moreover, since
FontAwesome is a font, it is inserted as an in-line element of the document,
which fits very well with the structure of our documents in RST.

* The theme PyData includes a copy of the icon library and automatically uses
  it for icons in navigation elements and admonitions (note, tip, warning...)
* Sphinx-Design provides the `fas` role to insert any icon as an in-line
  element of the document. For instance, to prepend an email address with a
  mail icon

    ```
    :fas:`envelope` name.surname@vscentrum.be
    ```

The name of each icon can be found in the [FontAwesome Icon
Gallery](https://fontawesome.com/icons).

## Web Customizations

### Sidebar Templates

Templates are the method to customize the sidebar of the web site. Those are
small pieces of HTML code that can be selectively added to the sidebar of some
pages. They have to be places in the `source/_templates` folder. 

The display of templates can be configured per document. This configuration is
set in `html_sidebars` in the `conf.py` file.

### Theme CSS

The style of the web can be changed in almost any way we want. Any CSS rules
added to the file [vsc.css](source/_static/css/vsc.css] will be added to the
main stack of CSS styles and can overwrite those.

The additional CSS style sheets are added in `conf.py` through the parameters
`html_static_path` and `html_css_files`.

### PyData Configuration

The Sphinx PyData theme is very flexible. Most of its configuration options are
set through the `html_theme_options` parameter. The configuration guide can be
found in the [PyData User Guide](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html).

### Not found page

The website shows a custom 404 page with the site navigation. This is done with
the `sphinx-notfound-page` extension, which uses the
[404.html](source/_templates/404.html) template.

