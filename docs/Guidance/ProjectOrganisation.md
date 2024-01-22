
    ├── code      
    │   ├── dashboard               <- Utility for creating a Plotly dashboard.
    │   │   └── ...
    │   ├── environment_variables   <- Directory for storing environment variables.
    │   │   └── ...
    │   ├── logs                    <- Directory for storing software logs.
    │   │   └── ...
    │   │── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │   └── ...               the creator's initials, and a short `-` delimited description, e.g.
    │   │                         `1.0-jqp-initial-data-exploration`. Sub-directories provided to 
    │   │                         organise notebooks by the workflow steps.
    │   │
    │   ├── src                 <- Source code for use in this project, organised with conformance to the workflow. 
    │   │   └── ...                Includes an __init__.py to make it a Python Module.
    │   │                         
    │   ├── Dockerfile          <- Dockerfile for creating a containerised application.
    │   ├── environment.yml     <- YAML file for managing a virtual environment with conda.
    │   ├── requirements.txt    <- txt file for managing a virtual environment with pip.
    │   ├── setup.py            <- makes project pip installable (pip install -e .) so src can be imported
    │   └── tox.ini             <- tox file with settings for running tox; see tox.readthedocs.io
    │
    ├── data
    │   ├── external        <- Data from third party sources.
    │   │   └── ...
    │   ├── interim-silver  <- Intermediate data that has been transformed. The silver layer in the Medallion architecture.
    │   │   └── ...
    │   ├── processed-gold  <- The final, canonical data sets for modeling. The gold layer in the Medallion architecture.
    │   │   └── ...
    │   └── raw-bronze      <- The original, immutable data dump. The bronze layer in the Medallion architecture.
    │       └── ...
    ├── docs
    |   ├── Data Dictionaries
    │   │   └── ...
    |   ├── Data Reports
    |   |   ├── DataDefinition.md
    |   |   ├── DataPipeline.txt
    |   |   └── DataSummaryReport.md
    │   │
    |   ├── Figures                     <- A directory to store figures, images or graphs for reporting.
    │   │   └── ...
    |   ├── Guidance
    |   |   ├── Cheatsheets             <- Directory of useful cheatsheets for coding/analytics.
    |   |   |   └── ...
    |   |   ├── Dashboarding.md         <- Guidance for using the included dashboard script templates. (WIP)
    |   |   ├── Docker.md               <- Guidance for deploying the project with Docker. (WIP)
    |   |   ├── DVC.md                  <- Guidance for utilising DVC in this project. (WIP)
    |   |   ├── GettingStarted.md       <- Guidance for setting up and initially configuring the project.
    |   |   └── ProjectOrganisation.md  <- This organisation chart.
    │   │
    |   ├── Model
    |   |   ├── Baseline
    |   |   |   └── BaselineModel.md    <- Comprehensive report structure for the baseline (first) model iteration.
    |   |   └── Model 1
    |   |   |   └── ModelReport.md      <- Comprehensive report structure for each model iteration. 
    |   |   └── FinalModelReport.md     <- Comprehensive report structure for the final (best) model iteration.
    │   │
    |   ├── Project
    │   │   ├── figures                 <- Generated graphics and figures to be used in reporting.
    |   │   ├── Charter.md              <- Initial scope capture/plan document to define the project activities. (WIP)
    |   │   ├── ExitReport.md           <- Final report for delivery to the customer (reporting should follow AMRC 
    │   │   │                              quality processes, you may wish to draft in this markdown doc or 
    │   │   │                              consider the headings when writing though)
    |   │   └── SystemArchitecture.docx <- Definition/map of the system architecture developed or proposed.
    │   │
    |   └── References                  <- A directory to save any useful references, papers, manuals etc.
    │       └── ...
    ├── models                          <- Trained and serialized models, model predictions, or model summaries, 
    │   └── ...                            tracked with DVC.
    │  
    ├── docker-compose.yml              <- Docker compose file for deploying a containerised application.
    └── README.md                       <- The top-level README for analysts using this project,             
                                           outlining the workflow and useful features included in the template.


