# Getting Started

## Prerequisites

*What needs to be installed on your system before you install this repo. E.g.*

* [Python 3](https://www.python.org/downloads/) - Python 3 (or above) interpreter
* [Visual Studio 2017](https://visualstudio.microsoft.com/) - Code editor or equivelant

## Setting up a virtual environment

### Python (conda)

Resources are provided within this template to quickly set up your python virtual environment. The chosen package manager is conda - either Anaconda or Miniconda should work.

Edit the [environment.yml](/code/environment.yml) file in the root directory with your environment name, python version and any specific package requirements for the project.

In the terminal, run the following command to create the virtual enviroment:

    conda env create --file code/environment.yml --prefix ./env

This will create the new enviroment in a sub-directory /env of the project root directory. If you prefer to manage conda environments centrally, and activate them via the given name (environments stored in a local project directory will need to be activated by pointing to their absolute path, as opposed to the given name), remove the --prefix ./env tag:

    conda env create --file code/environment.yml --prefix {path to your Anaconda/Miniconda installation, e.g. C:/Users/me1xxx/Anaconda3/envs/{name of your environment}

If/when your package requirements change (for e.g., you've found a new package you want to use which wasn't included on first build), update the package requirements in environment.yml and run the following command to update the virtual enviroment:

    conda env update --file code/environment.yml  --prune --prefix ./env

Updating packages this way, rather than installing new packages manually, allows you to track dependencies and manage version control much easier. You can also choose to recreate the enviroment from scratch for the same effect, with the command:

    conda env create --file code/environment.yml --prefix ./env --force

To activate your local enviroment run:

    conda activate ./env

*Page created by TR - Mar 24*