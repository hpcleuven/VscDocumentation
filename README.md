# VscDocumentation

This repository contains user-level documentation for the VSC infrastructure.  It is deployed on [ReadTheDocs](https://vlaams-supercomputing-centrum-vscdocumentation.readthedocs-hosted.com/en/latest/).

When a commit is done on the repository's master branch, the documentation is rebuilt automatically on ReadTheDocs, and is immediately live.  Hence you may prefer to work on a branch for major updates.

## Prerequisites

You will need to clone the repository, i.e.,
```bash
$ git clone git@github.com:hpcleuven/VscDocumentation.git
$ cd VscDocumentation
```

Your life will be substantially easier if you can preview your changes locally.  A conda environment has be defined to install all the required software

Downloads and installation instructions for Miniconda can be found on [conda's website](https://docs.conda.io/en/latest/miniconda.html).

The YAML environment description file is [``sphinx.yml``](sphinx.yml).  The environment can be created using
```bash
$ conda env create -f environment.yml
```


## What is the status of improvements/fixes?

Feel free to open issues to get fixes or improvements on the agenda.  To get an overview of work that is planned or in progress, check out the [project overview](https://github.com/hpcleuven/VscDocumentation/projects/1).


## Workflow

### Activate the environment

The ``sphinx`` environment can be activated by
```bash
$ source activate sphinx
```


### Creating a feature branch

Do not make changes in the master branch directly, but create feature/bugfix branches as required, e.g.,
```bash
$ git switch master
$ git switch -c feature/new_stuff
```


### Running a local sphinx server

The repository contains a make file that has a target to run the sphinx server.  The latter will monitor the ``source`` directory for changes, and serve the documentation to a web browser that is opened automatically.
```bash
$ make web
```


### Edit content

You can now edit the content to your heart's content, making commits to your feature branch as you go.  You can push your feature branch to the Github repository whenever you like.
```bash
$ git push origin feature/new_stuff
```


### Pull request

When you are done, create a pull request on GitHub.

You will have to ask others to review your pull request (at least two approvals before a merge is even possible).  Direct pushes to the master branch are not possible.


## Repository structure

1. source: directory containing the source to be rendered into HTML (e.g., rST and PNG files).
1. images: directory containing source documents for images (e.g., ODG files).
1. Makefile & make.bat: make files to render the documentation, and run a local web server.
1. sphinx.yml: conda environment definition.

The other files and directories are part of the migration, and may be removed at some
later stage.


## Documentation usage

Note that ReadTheDocs has a very convenient feature.  It lets you copy an URL
to a (sub)section of the documentation to make it easy to refer via email.  Simply
copy the link represented by the paragraph icon that appears next to the (sub)section
 title when you hover near it.

![copy documentation link](img/links.png)
