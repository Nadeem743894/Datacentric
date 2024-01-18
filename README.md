# PROJECT CODE NUMBER - PROJECT NAME

*Brief description of the project in a sentence or two.*

*Include a graphic for an overview of the project to help understand what the application is if possible. This should be broad concept only and not any specific details. GIF is best if possible.*

## Getting Started

- [ ] Fill out the Project Code/Name/Description above
- [ ] Build an appropriate [programming environment](/docs/Guidance/GettingStarted.md)

## The Workflow

<!-- replace [ ] with [x] when a workflow task has been completed -->

### Business Understanding

- [ ] Fill out the project Charter document with input from the customer

### Data Acquisition and Preparation

- [ ] Develop [notebook code](./code/notebooks/DataAcquisition/) to get started
- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/DataAcquisition/)
- [ ] Map the data flow in the [Data Pipeline](/docs/Data%20Reports/Data%20Pipeline.txt)
- [ ] Produce a [Data Report](/docs/Data%20Reports/DataSummaryReport.md) for each new dataset added to the project
 
### Data Exploration

- [ ] Develop notebook code [here](./code/notebooks/DataExploration)
- [ ] Define raw data sources in the [Data Definition](/docs/Data%20Reports/Data%20Defintion.md)

### Feature Transformation

- [ ] Develop notebook code [here](./code/notebooks/FeatureTransformation)
- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/FeatureTransformation/)
- [ ] Define raw data sources in the [Data Definition](/docs/Data%20Reports/Data%20Defintion.md)


### Model Building

- [ ] Develop notebook code [here](./code/notebooks/ModelBuilding)
- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/ModelBuilding/)

### Evaluation and Reporting

- [ ] Develop notebook code [here](./code/notebooks/EvaluationAndReporting)
- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/EvaluationAndReporting/)
- [ ] Build a dashboard with the [code utility](./code/dashboard/) and [guidance](/docs/Guidance/Dashboarding.md).

### Delivery, Deployment and Maintenance

- [ ] Develop notebook code [here](./code/notebooks/DeploymentAndMaintenance)
- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/DeploymentAndMaintenance/)
- [ ] Deploy a dockerised application with the [docker compose file](docker-compose.yml) and [guidance](/docs/Guidance/Docker.md).

## Other useful features

- [ ] Update a conda envirinment via the [environment.yml file](/code/environment.yml) and [guidance](/docs/Guidance/GettingStarted.md)

<!-- ### Building

*Describe how to build the application and general settings. Any specific should be included in specific guides on the wiki / pages section. What is needed to build should be already be included in prerequisites* -->

<!-- ## Project Organization

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
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │           └── visualize.py
    │
    │── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io -->

<!-- ### Coding Style

Coding style adheres to AMRC coding practices.

| Language | Standard |
| -- | -- |
| Javascript | [AirBnB](https://github.com/airbnb/javascript) |
| Python | [PEP-8](https://www.python.org/dev/peps/pep-0008/) |
| R | [Google's R Style Guide](https://web.stanford.edu/class/cs109l/unrestricted/resources/google-style.html) |
| MATLAB | N/A |

*Delete as appropiate for the project and where required state additional languages.
E.g. specific database technologises used and the standard being followed.* -->

<!-- ## Deployment

*Describe how you deploy the built application. Just an .exe that is run vs pointing to specific guides on the wiki / pages.* -->
<!-- 
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

Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience -->
