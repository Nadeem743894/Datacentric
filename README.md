*This repository contains all the documents and code/data directories that we expect you to require through your data-driven project. The aim is to provide a template for documentation/code/data that includes all the working links to allow full transparency and traceability, and therefore improve the quality and trust in AMRC data-driven projects, as well as increasing the accessibility to data science tools and skills whilst maintaining best practice. The development of this Github site is the result of collaboration between the [core team](/docs/0.ProjectManagement/CoreDCMTeam.md) in IMG and TMG. The team will be able to provide further guidance to using the template if needed. The IMG data science team will be regularly updating the guidance and information on our [data science wiki page](https://amrcwikijs.shef.ac.uk/en/AMRCDS) with community feedback. TMG also have developed a wiki for information on [machining data-driven projects](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing). If your own group has a relevant wiki page you can link to it [here](/link/to/your/wiki).*

# PROJECT CODE NUMBER - PROJECT NAME

> Brief description of the project in a sentence or two.

> Include a graphic for an overview of the project to help understand what the application is if possible. This should be broad concept only and not any specific details. GIF is best if possible.

## Getting Started

**To view the documentation homepage, go to https://amrcgithub.shef.ac.uk/pages/IMG/datascience-project-template/. When cloning this project, you will need to enable github pages in the repository settings where you will be given the new URL to access them. You can also view and edit the output in a suitable markdown editor, such as VS code.**

- [ ] Fill out the Project Code/Name/Description above as they become available.
- [ ] Initialise the git repository. A beginners guide to using Github is given [here](https://docs.github.com/en/get-started/start-your-journey/hello-world) although please note the repository has already been created here for you. Training is also available for AMRC staff via the UoS Research Software Engineering group and you can sign up [here](https://rse.shef.ac.uk/training/).
- [ ] Build an appropriate [programming environment](/docs/Guidance/GettingStarted.md).
- [ ] open the [project workspace in VS code](/datascience-project-template.code-workspace).

## The Workflow

<!-- replace [ ] with [x] when a workflow task has been completed -->

### [The Business Case](/docs/1.BusinessCase/README.md)

- [ ] Fill out the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document as comprehensively as possible. Work with partners and seek guidance where necessary. This document will provide the foundation for the SoW, the project plan and the data strategy as well as providing the tailored project workflow. It will also provide the information required for the TMG Lockdown Gate.
Once the project has been approved the following should be filled in. 
- [ ] Fill out the [project plan](/docs/0.ProjectManagement/ProjectPlan.md). This documents who will work on the project and any other key information that is needed for the project to run smoothly.
- [ ] Fill out the [high-level business understanding](/docs/1.BusinessCase/High-levelBusinessCase.md). This should be suitable as a public description on the SoW. 
- [ ] Fill out the [detailed business understanding](/docs/1.BusinessCase/DetailedBusinessCase.md) with further information about the need for the project. This will be used to create the SoW and will also provide a solid foundation for an introduction in a report. 

- [ ] Is the project viable? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

### [Data Acquisition and Preparation](/docs/2.DataAcquisitionAndPreparation/README.md)

- [ ] Develop [notebook code](/code/notebooks/2.DataAcquisitionAndPreparation/) to get started.
- [ ] Copy and paste the information from the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document into the [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and update where necessary. Do not edit the scoping document. 
- [ ] Ensure that the [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) contains the complete list of expected data that will be collected and produced as part of this project. 
- [ ] If required, produce an [experimental design](/docs/2.DataAcquisitionAndPreparation/ExperimentalDesign.md).
- [ ] Map the data flow in the [data pipeline](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataPipeline.txt).
- [ ] Initialise and use DVC with the [guidance](/docs/Guidance/DVC.md).
- [ ] If there is no ontology-based reference library, you should create a common dictionary of terms and naming conventions to be followed throughout and populate the [data dictionary](/docs/2.DataAcquisitionAndPreparation/Data%20Dictionaries/README.md), otherwise link to the ontology. 
- [ ] If required, complete the TMG Readiness Gate. 
- [ ] Begin data collection. 
- [ ] Define raw data sources in the [data overview](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataOverview.md).
- [ ] Clean the data ready for initial exploration creating the [silver-interim data](/data/interim-silver/).
- [ ] Define interim data sources in the [data overview](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataOverview.md).

- [ ] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/DataAcquisition/).

> **Further guidance is available on the wiki, including: storage locations, design of experiments, naming conventions, representative data**
- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/DataAcquisitionandPreparation)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/Data_Capture_and_Management)

### [Data Exploration](/docs/3.DataExploration/README.md)

- [ ] Develop [notebook code](/code/notebooks/3.DataExploration) to carry out the data exploration. 
- [ ] Produce an [exploratory data Report](/docs/3.DataExploration/DataSummaryTemplate.md) for each new dataset added to the project.
- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Do you need to review your analysis plan? 
- [ ] Move reusable code into a callable module in [this directory](/code/src/DataExploration/).

- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

> **Further guidance is available on the wiki, including: statistical summaries, EDA plots, correlation analysis, the EDA workflow, EDA questions**
- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/DataExploration)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/Experimental_Planning) - you will also find some Matlab scripts here. 

### [Feature Transformation](/docs/4.FeatureTransformation/README.md)

- [ ] Are you creating features from the data? If yes, define feature sets in the [data overview](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataOverview.md).
- [ ] Develop [notebook code](/code/notebooks/4.FeatureTransformation) to create your features.
- [ ] Move reusable code into a callable module in [this directory](./code/src/FeatureTransformation/).
- [ ] Create a feature data dictionary using the [template](/docs/2.DataAcquisitionAndPreparation/Data%20Dictionaries/amrc-data-dictionary.xlsx).
- [ ] Summarise how the features will help meet the business objectives in a [short report](/docs/4.FeatureTransformation/FeatureSummaryReport.md).
- [ ] Log new features for version control with [DVC](/docs/Guidance/DVC.md).

- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

> **Further guidance is available on the wiki, including: common features, dimension reduction, signal processing**
- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/FeatureTransformation)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/)

### [Model Building](/docs/5.ModelBuilding/README.md) 

- [ ] Develop [notebook code](./code/notebooks/5.ModelBuilding) for model building.
- [ ] Remember to move reusable code into a callable module in [this directory](./code/src/ModelBuilding/) as you develop the model code.
- [ ] Track models and experiments with [DVC](/docs/Guidance/DVC.md).
- [ ] Describe the [modelling strategy](/docs/5.ModelBuilding/ModellingStrategy.md). Some of this information can be copied from the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document.
- [ ] Produce a [baseline report](/docs/5.ModelBuilding/Model/Baseline/Baseline%20Model.md) for the first model developed.
- [ ] Produce a [model report](/docs/5.ModelBuilding/Model/Model%201/ModelReport.md) for each model iteration. This should contain information on the changes to the model and the reasoning. 
- [ ] Complete a [Final Report](/docs/5.ModelBuilding/Model/FinalModelReport.md) for the best model identified/evaluated on the hold-out test set.
- [ ] Log new models for version control with [DVC](/docs/Guidance/DVC.md), stored in the [model directory](/models/README.md).
- [ ] Track experiments with [DVC](/docs/Guidance/DVC.md).

- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

**Further guidance is available on the wiki, including: analysis tools, descriptive v predictive analysis, statistics and probability**
- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/ModelBuilding)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/)
- Guidance on [DVC](/docs/Guidance/DVC.md) is available on Github to preserve coding links. 

### [Evaluation and Reporting](/docs/6.InterpretationAndReporting/README.md)

- [ ] Develop [notebook code](./code/notebooks/6.EvaluationAndReporting) for evaluation and reporting.
- [ ] Move reusable code into a callable module in [this directory](./code/src/EvaluationAndReporting/).
- [ ] Identify stakeholders and the required reports and dashboards. These can be listed [here](/docs/6.InterpretationAndReporting/Stakeholders.md). 
- [ ] Build a dashboard with the [plotly templates](./code/dashboard/) and [guidance](/docs/Guidance/Dashboarding.md).
- [ ] Extract required content from [docs folder](/docs/) for your agreed reporting format (AMRC technical report, presentation etc.).
- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and ensure it is an accurate reflection of the data used in the project.
- [ ] Have you successfully met the business objectives? Document the [insights and actions](/docs/6.InterpretationAndReporting/ActionsAndInsights.md) that can result from this work.
- [ ] What are the [lessons learned](/docs/6.InterpretationAndReporting/LessonsLearned.md) from this work. 
- [ ] If there is no deployment required, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

**Further guidance is available on the wiki, including: visualisation best practice, the importance of knowing the audience**
- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/ModelBuilding).
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/).
- Guidance on [Dashboarding](/docs/Guidance/Dashboarding.md) is available on Github to preserve coding links. 
- AMRC final project report guidelines are available on Harbour. 

### [Deployment and Maintenance](/docs/7.DeploymentAndMaintenance/README.md)

- [ ] Develop [notebook code](./code/notebooks/7.DeploymentAndMaintenance/).
- [ ] Move reusable code into a callable module in [this directory](./code/src/DeploymentAndMaintenance/).
- [ ] Deploy a dockerised application with the [docker compose file](docker-compose.yml) and [guidance](/docs/Guidance/Docker.md).
- [ ] Complete the [deployment strategy](/docs/7.DeploymentAndMaintenance/DeploymentStrategy.md).
- [ ] Complete the [maintenance strategy](/docs/7.DeploymentAndMaintenance/MaintenanceStrategy.md).


## Other useful features

- [ ] Update a conda environment via the [environment.yml file](/code/environment.yml) and [guidance](/docs/Guidance/GettingStarted.md).
- [ ] [IMG DCM wiki](https://amrcwikijs.shef.ac.uk/en/AMRCDS) and [TMG DCM wiki](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing) information portals. 
- [ ] Check the [cheatsheets](/docs/Guidance/Cheatsheets/Cheatsheets.md) relevant to this template.
*This markdown sheet is quite handy! [Link](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)*
- [ ] Manage [environment variables](/code/environment_variables/README.md) across your project.


*Page created by LL & TR - Mar 24*

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
