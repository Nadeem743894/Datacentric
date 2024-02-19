# DVC (Data Version Control)

The guidance provided in this page is taken from the [DVC documentation](https://dvc.org/doc/start), and edited to match the utilities provided in this template. The guidance here is intended to get you set up and running with minimal effort and prior knowledge, so make sure to go through the documentation and other resources available online to improve your capabilities once you feel comfortable with the basics.

## Installation on Windows

To use DVC as a [Python library](https://dvc.org/doc/api-reference), you can install it with conda or with pip (below).

See [Running DVC on Windows](https://dvc.org/doc/user-guide/how-to/run-dvc-on-windows) for important tips to improve your experience on Windows.

Note: DVC only commits a tiny metadata file to git instead of the actual data files. The guidance below assumes that you are managing and keeping your data/models locally within the project directory, if you require remote storage (for e.g., through a cloud provider such as Azure, or on the K: Drive) see the [remote storage documentation](https://dvc.org/doc/user-guide/data-management/remote-storage) on the DVC web page.

### Install with conda

Requires Miniconda or Anaconda Distribution.

You can use conda from [Anaconda Prompt](https://docs.anaconda.com/free/anaconda/getting-started/), a POSIX-like command line terminal in Windows.

    conda install -c conda-forge mamba # installs much faster than conda
    mamba install -c conda-forge dvc

### Install with pip

We strongly recommend creating a virtual environment or using pipx to encapsulate your local environment.

Note that Python 3.8+ is needed to get the latest version of DVC.

    pip install dvc

### Windows installer

A quick way is to use the self-contained, executable installer (binary), which is available from the big "Download" button on the [home page](https://dvc.org/).

You'll need to download and run the installer again each time you want to update DVC. You may use Windows Uninstaller to remove the program.

Note that this method by default enables symlink permissions for all users, so they can use them to optimize DVC operations.

## Initialising a project

Inside your chosen directory, we will use our current working directory as a DVC project. Let's initialize it by running dvc init inside a Git project:

    dvc init
A few internal files are created that should be added to Git:

    $ git status
    Changes to be committed:
            new file:   .dvc/.gitignore
            new file:   .dvc/config
           ...
    $ git commit -m "Initialize DVC"

Now you're ready to DVC!