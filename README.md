# PROJECT CODE NUMBER - PROJECT NAME

*Brief description of the project in a sentence or two.*

*Include a graphic for an overview of the project to help understand what the application is if possible. This should be broad concept only and not any specific details. GIF is best if possible.*

## Getting Started

The data science team will be able to provide further guidance if needed. 

- [ ] Fill out the Project Code/Name/Description above
- [ ] Initialise the git repository ***Need an instruction sheet for this***
- [ ] Build an appropriate [programming environment](/docs/Guidance/GettingStarted.md)
- [ ] open the [project workspace in VS code](/datascience-project-template.code-workspace)

## The Workflow

<!-- replace [ ] with [x] when a workflow task has been completed -->

### [The Business Case](/docs/1.BusinessCase/)

- [ ] Fill out the [Project Scoping](/docs/0.ProjectManagement/ProjectScoping.md) document as comprehensively as possible. Work with partners and seek guidance where necessary. This document will provide the foundation for the SoW, the project plan and the data strategy as well as providing the tailored project workflow. 
Once the project has been approved the following should be filled in. 
- [ ] Fill out the [Project Plan](/docs/0.ProjectManagement/ProjectPlan.md). This documents who will work on the project and any other key information that is needed for the project to run smoothly.
- [ ] Fill out the [high-level business understanding](/docs/1.BusinessCase/High-levelBusinessCase.md). This should be suitable as a public description on the SoW. 
- [ ] Fill out the [detailed business understanding](/docs/1.BusinessCase/DetailedBusinessCase.md) with further information about the need for the project. This will be used to create the SoW and will also provide a solid foundation for an introduction in a report. 
- [ ] Is the project viable? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

### [Data Acquisition and Preparation](/docs/2.DataAcquisitionAndPreparation/)

- [ ] Copy and paste the information from the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document into the [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and update where necessary. Do not edit the scoping document. 
- [ ] Develop [notebook code](./code/notebooks/DataAcquisition/) to get started
- [ ] Map the data flow in the [Data Pipeline](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataPipeline.txt)
- [ ] Initialise and use DVC with the [guidance](/docs/Guidance/DVC.md)
- [ ] Populate the [Data Dictionary](/docs/2.DataAcquisitionAndPreparation/Data%20Dictionaries/README.md) 
- [ ] Define raw data sources in the [Data Definitions](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataDefinition.md)
- [ ] Clean the data ready for initial exploration creating the [silver-interim data](/data/interim-silver/)
- [ ] Define interim data sources in the [Data Definitions](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataDefinition.md)

- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/DataAcquisition/)

> **Guidance is available on:**
- [Storage locations](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/DataAcquisitionandPreparation/DataStorage){:target="_blank"}
- [Storage formats](/docs/Guidance/StorageFormats.md)

### [Data Exploration](/docs/3.DataExploration/)

- [ ] Develop [notebook code](./code/notebooks/DataExploration)
- [ ] Produce a [Data Report](/docs/Data%20Reports/DataSummaryReport.md) for each new dataset added to the project.
- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Do you need to review your analysis plan? 
- [ ] Move reusable code into a callable module in [this directory](./code/src/DataExploration/)

- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md)

> **Guidance is available on:**
- [Statistical summaries](/docs/Guidance/StatisticalSummaries.md)
- [EDA plots](/docs/Guidance/EDAplots.md)
- [Correlation Analysis](/docs/Guidance/correlationanalysis.md)
- [An EDA workflow](/docs/Guidance/EDAWorkflow.md)
- [The questions to ask during an EDA](/docs/Guidance/EDAQuestions.md)

### [Feature Transformation](/docs/4.FeatureTransformation/README.md)

- [ ] Are you creating features from the data? If yes, define feature sets in the [Data Definitions](/docs/Data%20Reports/Data%20Defintion.md)
- [ ] Develop [notebook code](./code/notebooks/FeatureTransformation) to create your features.
- [ ] Move reusable code into a callable module in [this directory](./code/src/FeatureTransformation/)
- [ ] Create a feature data dictionary using the [template](/docs/2.DataAcquisitionAndPreparation/Data%20Dictionaries/amrc-data-dictionary.xlsx)
- [ ] Summarise how the features will help meet the business objectives in a [short report](/docs/4.FeatureTransformation/FeatureSummaryReport.md).
- [ ] Log new features for version control with [DVC](/docs/Guidance/DVC.md)

- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

**Guidance is available on:**
- [Common features](/docs/Guidance/CommonFeatures.md)
- [Dimension reduction](/docs/Guidance/DimensionReduction.md) 
- [Signal processing](/docs/Guidance/SignalProcessing.md)


### Model Building

- [ ] Develop [notebook code](./code/notebooks/ModelBuilding)
- [ ] Move reusable code into a callable module in [this directory](./code/src/ModelBuilding/)
- [ ] Track models and experiments with [DVC](/docs/Guidance/DVC.md)
- [ ] Produce a [Baseline Report](/docs/Model/Baseline/Baseline%20Model.md) for the first model developed
- [ ] Produce a [Model Report](/docs/Model/Model%201/Model%20Report.md) for each model iteration
- [ ] Log new models for version control with [DVC](/docs/Guidance/DVC.md), stored in the [model directory](/models/README.md)
- [ ] Track experiments with [DVC](/docs/Guidance/DVC.md)
- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

### Evaluation and Reporting

- [ ] Develop [notebook code](./code/notebooks/EvaluationAndReporting)
- [ ] Move reusable code into a callable module in [this directory](./code/src/EvaluationAndReporting/)
- [ ] Build a dashboard with the [plotly templates](./code/dashboard/) and [guidance](/docs/Guidance/Dashboarding.md)
- [ ] Complete a [Final Report](/docs/Model/Final%20Report.md) for the best model identified/evaluated on the hold-out test set
- [ ] Complete the [Exit Report](/docs/Project/Exit%20Report.md)
- [ ] Define the [System Architecture](/docs/Project/System%20Architecture.docx)
- [ ] Extract required content from [docs folder](/docs/) for your agreed reporting format (AMRC technical report, presentation etc.)
- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and ensure it is an accurate reflection of the data used in the project.

### Deployment and Maintenance

- [ ] Develop [notebook code](./code/notebooks/DeploymentAndMaintenance)
- [ ] Move reusable code into a callable module in [this directory](./code/src/DeploymentAndMaintenance/)
- [ ] Deploy a dockerised application with the [docker compose file](docker-compose.yml) and [guidance](/docs/Guidance/Docker.md)

### Guidance and cheat sheets 

* [Possible impacts of data representation.](/docs/Guidance/MissingData.md)

## Other useful features

- [ ] Update a conda envirinment via the [environment.yml file](/code/environment.yml) and [guidance](/docs/Guidance/GettingStarted.md)
- [ ] Check the [cheatsheets](/docs/Guidance/Cheatsheets/Cheatsheets.md) relevant to this template
- [ ] Manage [environment variables](/code/environment_variables/README.md) across your project
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
