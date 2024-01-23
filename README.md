# VscDocumentation

Repository of the [VSC documentation website](https://docs.vscentrum.be).

## How to contribute?

Improving the documentation is quite simple, all documents can be edited with a
simple text editor. You standard workflow to contribute changes is:

1. Clone this repository
2. Make corrections/improvements to any document
3. Push you changed to a new branch
4. Open a pull request to the `master` branch of this repo

⚠️ Follow our [style guide](styleguide.md) to edit the VSC documentation.

## What is the status of improvements/fixes?

Feel free to open issues to get fixes or improvements on the agenda.  To get an
overview of work that is planned or in progress, check out the [project
overview](https://github.com/hpcleuven/VscDocumentation/projects/1).

## Workflow

### Prerequisites

You will need to clone the repository, i.e.,
```bash
$ git clone git@github.com:hpcleuven/VscDocumentation.git
```

Your life will be substantially easier if you can preview your changes locally.
For this you'll need to install the required packages in a self-contained
environment such as a Python virtual environment (*venv*) or Conda.
The packages are listed in the `requirements.txt` file in this repo.

Such environments should preferably use the same Python version as the one
specified in the `.readthedocs.yaml` file. Note that older Python versions
(<= v3.7 at the time of writing) may not be able to install the requirements.

#### Python venv

This is an example setup for a Python virtual environment:

```bash
$ python -m venv /path/to/new/venv
$ source /path/to/new/venv/bin/activate
$ cd VscDocumentation
$ python -m pip install -r requirements.txt
```

#### Conda

This is an example setup for a Conda environment:

```bash
$ conda create -n vscdocs python=3.11
$ source activate vscdocs
$ pip install -r requirements.txt
```

Downloads and installation instructions for Miniconda can be found on [conda's
website](https://docs.conda.io/en/latest/miniconda.html).


### Creating a feature branch

Do not make changes in the `master` or `development` branches directly. Create
your own feature/bugfix branch as needed.

```bash
$ cd VscDocumentation
$ git checkout master
$ git checkout -b feature/new_stuff
```

### Running a local sphinx server

The repository contains a make file that has a target to run the sphinx server.
The latter will monitor the `source` directory for changes, and serve the
documentation to a web browser that is opened automatically.

```bash
$ make web
```

### Edit content

You can now edit the content to your heart's content, making commits to your
feature branch as you go. You can push your feature branch to the Github
repository whenever you like.

```bash
$ git add source/some_documentation_file.rst
$ git commit -m "some new stuff added to VSC docs"
$ git push origin feature/new_stuff
```

### Pull request

When you are done, create a pull request to the `master` branch of this
repository on GitHub.

Changes to the documentation require the positive review from the documentation
maintainers of your pull request. Pay attention to the review in case there
would be remarks to address.

Once the pull request has been merged, the branch will be deleted from GitHub.
At this point, all that is left to do is delete your local feature branch.

```bash
$ git fetch origin
$ git checkout master
$ git pull origin master
$ git branch -d feature/new_stuff
```
