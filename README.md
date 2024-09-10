*This repository contains all the documents and code/data directories that we expect you to require through your data-driven project. The aim is to provide a template for documentation/code/data that includes all the working links to allow full transparency and traceability, and therefore improve the quality and trust in AMRC data-driven projects, as well as increasing the accessibility to data science tools and skills whilst maintaining best practice. The development of this Github site is the result of collaboration between the [core team](/docs/0.ProjectManagement/CoreDCMTeam.md) in IMG and TMG. The team will be able to provide further guidance to using the template if needed. The IMG data science team will be regularly updating the guidance and information on our [data science wiki page](https://amrcwikijs.shef.ac.uk/en/AMRCDS) with community feedback. TMG have also developed a wiki for information on [machining data-driven projects](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing). If your own group has a relevant wiki page you can link to it [here](/link/to/your/wiki).*

# AS2382 - Assessing the energy usage of Boeings Flight Simulation Centers


>This project focuses on reducing the carbon footprint of Boeing flight simulation centers by mapping energy usage, identifying areas for optimization, and exploring the integration of renewable energy solutions to enhance sustainability.

> ![img.png](Logical_pipeline.png)

## Getting Started

**To view the documentation homepage, go to https://amrcgithub.shef.ac.uk/pages/IMG/datascience-project-template/. This page is best viewed in an Integrated Developmment Environment (IDE), which will enable all the links to directly open the guidance documents, directories and example scripts for you to edit seamlessly. We recommend [VS code](https://code.visualstudio.com/), but alternatives which support both coding and markdown - such as [Jetbrains PyCharm](https://www.jetbrains.com/pycharm/?var=1) - should also work fine, if you prefer.**

**Alternatively, you can view the the documentation as a [GitHub pages website](https://pages.github.com/); to enable this, when cloning this project, you will need to enable github pages in the repository settings where you will be given the new URL to access them.**

To tick off the boxes on this page as you progress through the workflow, replace [ ] with [x] (in the README.md source file) when a task has been completed.

- [x] In VS code, use `CTRL + SHIFT + P` to access the command pallette and search for `Markdown: Open Preview to Side` to view the formatted markdown pages.
- [x] Fill out the Project Code/Name/Description above as they become available.
- [x] Initialise the git repository. A beginners guide to using Github is given [here](https://docs.github.com/en/get-started/start-your-journey/hello-world) although please note the repository has already been created here for you. Training is also available for AMRC staff via the UoS Research Software Engineering group.
- [x] Build an appropriate [programming environment](/docs/Guidance/GettingStarted.md).
- [x] Open the [project workspace in VS code](/datascience-project-template.code-workspace).

## The Workflow

### [The Business Case](/docs/1.BusinessCase/README.md)

- [x] Fill out the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document as comprehensively as possible. Work with partners and seek guidance where necessary. This document will provide the foundation for the SoW, the project plan and the data strategy as well as providing the tailored project workflow. It will also provide the information required for the TMG Scoping gate.
Once the project has been approved the following should be filled in.
- [x] Fill out the [project plan](/docs/0.ProjectManagement/ProjectPlan.md). This documents who will work on the project and any other key information that is needed for the project to run smoothly. This will provide the information for the TMG Launch gate.
- [x] Fill out the [high-level business understanding](/docs/1.BusinessCase/High-levelBusinessCase.md). This should be suitable as a public description on the SoW.
- [x] Fill out the [detailed business understanding](/docs/1.BusinessCase/DetailedBusinessCase.md) with further information about the need for the project. This will be used to create the SoW and will also provide a solid foundation for an introduction in a report.

- [] Is the project viable? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).
- [x] If the project is viable and if required, complete the TMG Lockdown gate.

### [Data Acquisition and Preparation](/docs/2.DataAcquisitionAndPreparation/README.md)

- [x] Develop [notebook code](/code/notebooks/2.DataAcquisitionAndPreparation/2.1-me1xxx-data-acquisition-example.ipynb) to get started. Name each notebook with the following format:
  
  `<step>-<me1xxx>-<description>.ipynb`, e.g. `2.1-me1tjr-data-cleaning.ipynb`

- [x] Copy and paste the information from the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document into the [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and update where necessary. Do not edit the scoping document.
- [x] Ensure that the [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) contains the complete list of expected data that will be collected and produced as part of this project.
- [x] If required, produce an [experimental design](/docs/2.DataAcquisitionAndPreparation/ExperimentalDesign.md).
- [x] Map the data flow in the [data pipeline](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataPipeline.txt).
- [x] Initialise and use DVC with the [guidance](/docs/Guidance/DVC.md).
- [x] If there is no ontology-based reference library, you should create a common dictionary of terms and naming conventions to be followed throughout and populate the [data dictionary](/docs/2.DataAcquisitionAndPreparation/Data%20Dictionaries/README.md), otherwise link to the ontology.
- [x] If required, complete the TMG Readiness Gate.
- [x] Begin data collection.
- [x] Define raw data sources in the [data overview](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataOverview.md).
- [x] For collection of large data sets you should choose a suitable point early on to check the data is being collected correctly. If necessary, complete the TMG Data Collection and Review gate.
- [x] Clean the data ready for initial exploration creating the [silver-interim data](/data/interim-silver/).
- [] Define interim data sources in the [data overview](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataOverview.md).

- [x] Don't Repeat Yourself! Move reusable code into a callable module in [this directory](./code/src/DataAcquisition/).

#### Further guidance is available on the wiki, including: storage locations, design of experiments, naming conventions, representative data

- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/DataAcquisitionandPreparation)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/Data_Capture_and_Management)

### [Data Exploration](/docs/3.DataExploration/README.md)

- [ x] Develop [notebook code](/code/notebooks/3.DataExploration/3.1-me1xxx-data-exploration-example.ipynb) to carry out the data exploration. Name each notebook with the following format:
  
  `<step>-<me1xxx>-<description>.ipynb`, e.g. `3.1-me1tjr-data-exploration.ipynb`

- [ x] Produce an [exploratory data report](/docs/3.DataExploration/DataSummaryTemplate.md) for each new dataset added to the project.
- [ x] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ x] Do you need to review your analysis plan?
- [ x] Move reusable code into a callable module in [this directory](/code/src/DataExploration/).

- [ x] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

#### Further guidance is available on the wiki, including: statistical summaries, EDA plots, correlation analysis, the EDA workflow, EDA questions

- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/DataExploration)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/Experimental_Planning) - you will also find some Matlab scripts here.

### [Feature Transformation](/docs/4.FeatureTransformation/README.md)

- [ ] Are you creating features from the data? If yes, define feature sets in the [data overview](/docs/2.DataAcquisitionAndPreparation/Data%20Pipeline/DataOverview.md).
- [ ] Develop [notebook code](/code/notebooks/4.FeatureTransformation/4.1-me1xxx-feature-transformation-example.ipynb) to create your features. Name each notebook with the following format:
  
  `<step>-<me1xxx>-<description>.ipynb`, e.g. `4.3-me1tjr-statistical-feature-engineering.ipynb`

- [ ] Move reusable code into a callable module in [this directory](./code/src/FeatureTransformation/).
- [ ] Create a feature data dictionary using the [template](/docs/2.DataAcquisitionAndPreparation/Data%20Dictionaries/amrc-data-dictionary.xlsx).
- [ ] Summarise how the features will help meet the business objectives in a [short report](/docs/4.FeatureTransformation/FeatureSummaryReport.md).
- [ ] Log new features for version control with [DVC](/docs/Guidance/DVC.md).
- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

#### Further guidance is available on the wiki, including: common features, dimension reduction, signal processing

- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/FeatureTransformation)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/)

### [Model Building](/docs/5.ModelBuilding/README.md)

- [ ] Develop [notebook code](./code/notebooks/5.ModelBuilding/5.1-me1xxx-model-building-example.ipynb) for model building. Name each notebook with the following format:
  
  `<step>-<me1xxx>-<description>.ipynb`, e.g. `5.6-me1tjr-svm-model-building.ipynb`

- [ ] Remember to move reusable code into a callable module in [this directory](./code/src/ModelBuilding/) as you develop the model code.
- [ ] Track models and experiments with [DVC](/docs/Guidance/DVC.md).
- [ ] Describe the [modelling strategy](/docs/5.ModelBuilding/ModellingStrategy.md). Some of this information can be copied from the [project scoping](/docs/0.ProjectManagement/ProjectScoping.md) document.
- [ ] Produce a [baseline report](/docs/5.ModelBuilding/Model/Baseline/Baseline%20Model.md) for the first model developed.
- [ ] Produce a [model report](/docs/5.ModelBuilding/Model/Model%201/ModelReport.md) for each model iteration. This should contain information on the changes to the model and the reasoning.
- [ ] Complete a [final report](/docs/5.ModelBuilding/Model/FinalModelReport.md) for the best model identified/evaluated on the hold-out test set.
- [ ] Log new models for version control with [DVC](/docs/Guidance/DVC.md), stored in the [model directory](/models/README.md).
- [ ] Track experiments with [DVC](/docs/Guidance/DVC.md).

- [ ] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and make changes where necessary.
- [ ] Can the project continue? If not, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).

#### Further guidance is available on the wiki, including: analysis tools, descriptive v predictive analysis, statistics and probability

- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/ModelBuilding)
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/)
- Guidance on [DVC](/docs/Guidance/DVC.md) is available on Github to preserve coding links.

### [Evaluation and Reporting](/docs/6.InterpretationAndReporting/README.md)

- [x] Develop [notebook code](./code/notebooks/6.EvaluationAndReporting/6.1-me1xxx-evaluation-example.ipynb) for evaluation and reporting. Name each notebook with the following format:
  
  `<step>-<me1xxx>-<description>.ipynb`, e.g. `6.1-me1tjr-results-reporting.ipynb`

- [x] Move reusable code into a callable module in [this directory](./code/src/EvaluationAndReporting/).
- [x] Identify stakeholders and the required reports and dashboards. These can be listed [here](/docs/6.InterpretationAndReporting/Stakeholders.md).
- [ ] Build a dashboard with the [plotly templates](./code/dashboard/) and [guidance](/docs/Guidance/Dashboarding.md).
- [x] Extract required content from [docs folder](/docs/) for your agreed reporting format (AMRC technical report, presentation etc.).
- [x] Review your [data strategy](/docs/2.DataAcquisitionAndPreparation/DataStrategy.md) and ensure it is an accurate reflection of the data used in the project.
- [ x] Have you successfully met the business objectives? Document the [insights and actions](/docs/6.InterpretationAndReporting/ActionsAndInsights.md) that can result from this work.
- [ ] What are the [lessons learned](/docs/6.InterpretationAndReporting/LessonsLearned.md) from this work.
- [ ] If there is no deployment required, complete the [closure form](/docs/0.ProjectManagement/ClosureReport.md).
- [ ] If required, complete the TMG Project Completion Gate.

#### Further guidance is available on the wiki, including: visualisation best practice, the importance of knowing the audience

- [IMG - Data science guidance](https://amrcwikijs.shef.ac.uk/en/AMRCDS/Guidance/ModelBuilding).
- [TMG - Machining DCM guidance](https://amrcwikijs.shef.ac.uk/en/AMRC/TMG/Data_Centric_Manufacturing/).
- Guidance on [Dashboarding](/docs/Guidance/Dashboarding.md) is available on Github to preserve coding links.
- AMRC final project report guidelines are available on Harbour.

### [Deployment and Maintenance](/docs/7.DeploymentAndMaintenance/README.md)

- [ ] Develop [notebook code](./code/notebooks/7.DeploymentAndMaintenance/7.1-me1xxx-deployment-example.ipynb). Name each notebook with the following format:
  
  `<step>-<me1xxx>-<description>.ipynb`, e.g. `7.2-me1tjr-deployed-api-testing.ipynb`

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