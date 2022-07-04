# PROJECT CODE NUMBER - PROJECT NAME

*Brief description of the project in a sentence or two.*

*Include a graphic for an overview of the project to help understand what the application is if possible. This should be broad concept only and not any specific details. GIF is best if possible.*

## Getting Started

### Prerequisites

*What needs to be installed on your system before you install this repo. E.g.*

* [Python 3](https://www.python.org/downloads/) - Python 3 (or above) interpreter
* [Visual Studio 2017](https://visualstudio.microsoft.com/) - Code editor or equivelant

### Installing

*How should they install the application. E.g. download the trunk and launch within the UnityEditor.*

*Include an image/animated GIF of what success looks like.*

### Building

*Describe how to build the application and general settings. Any specific should be included in specific guides on the wiki / pages section. What is needed to build should be already be included in prerequisites*

## Project Organization

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Default docs generation guidance and advice, derived from the IMG Digital Template.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── figures        <- Generated graphics and figures to be used in reporting
    │   │
    │   └── Analytics-plan.md   <- Document for recording and peer reviewing the project analytics plan.
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                <- makes project pip installable (pip install -e .) so src can be imported
    │
    │── python
    │    ├── src                <- Source code for use in this project.
    │    │   ├── __init__.py    <- Makes src a Python module
    │    │   │
    │    │   ├── data           <- Scripts to download or generate data
    │    │   │   └── make_dataset.py
    │    │   │
    │    │   ├── features       <- Scripts to turn raw data into features for modeling
    │    │   │   └── build_features.py
    │    │   │
    │    │   ├── models         <- Scripts to train models and then use trained models to make
    │    │   │   │                 predictions
    │    │   │   ├── predict_model.py
    │    │   │   └── train_model.py
    │    │   │
    │    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │    │           └── visualize.py
    │    │
    │    └── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │── R
    │    ├── src
    │    │   ├── ...
    │    │
    │    └── ...
    │
    │── MATLAB
    │    ├── src
    │    │   ├── ...
    │    │
    │    └── ...
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

### Coding Style

Coding style adheres to AMRC coding practices.

| Language | Standard |
| -- | -- |
<!-- | Javascript | [AirBnB](https://github.com/airbnb/javascript) | -->
| Python | [PEP-8](https://www.python.org/dev/peps/pep-0008/) |
| R | [Google's R Style Guide](https://web.stanford.edu/class/cs109l/unrestricted/resources/google-style.html) |
| MATLAB | N/A |

*Delete as appropiate for the project and where required state additional languages.
E.g. specific database technologises used and the standard being followed.*

## Deployment

*Describe how you deploy the built application. Just an .exe that is run vs pointing to specific guides on the wiki / pages.*

## Contributing

Please only contribute if assigned to work on the project.
Development practice follows [GitHub flow](https://guides.github.com/introduction/flow/).

## Versioning

This project is using [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repositiory](https://github.com/your/project/tags).

## Authors

* **Joe Smith** - *PM* - [me1num](http://amrcgithub.shef.ac.uk/me1num)
* **Laura Jones** - *Developer* - [me1num](http://amrcgithub.shef.ac.uk/me1num)

See also the list of [contributors](http://amrcgithub.shef.ac.uk/IMG/LINK_TO_PROJECT/graphs/contributors) who participated in this project.

## License

This project is funded under *name your project type*.

*Also include any links to collaberation agreements for future staff members wanting to understand if they can use the codebase.*

## Acknowledgments

*This markdown sheet is quite handy! [Link](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)*

Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience
