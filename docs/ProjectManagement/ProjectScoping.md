
# AMRC Data Project Workflow Scoping

### Aim of the document

The aim of this document is to plan the technical aspects of a data project (including required resources) in the context of the business case and the planned end product. It is recommended that this document is filled in during project scoping (at this stage it may not be clear the project is viable or how much money/time/resource are required depending on data availability and storage options). The document is set out according to the AMRC Data-Centric Manufacturing Workflow for viable projects will provide a strong foundation for producing a Statement of Work.  Each bullet point should be considered and basic details given at the scoping stage. 

* Project code: (if/when available)
* Harbour link: (if/when available)

## Step 1: Business Understanding

> ### Why are you doing this project? 

#### What is the business case? 

* What is the project aiming to achieve? 
* What benefit will it bring to the AMRC? 
* Are any partners involved? Who, and what is the benefit for them? 
* Which sector will the project be centred on? 

### What does the end product look like? Headlines

* What is the planned solution and what does it look like? 
* How will the solution be achieved?


## Step 2: Data Acquisition and Preparation

> ### Data availability and readiness

* What data is required for the project? 
* Is the project data: 
  1. available as is?
  2. available but needs processing for use in this project?
  3. not currently available?

If there are different data types and sources then more than one case may apply - simply fill in the sections below as required for each data type/source and copy and paste where necessary.

* ***Are there any resource or cost limitations associated with data collection and storage?***
If yes, give details. 

> ### Data acquisition 

#### Case 1: Data is available as is

* Data type
* Where is the data and do you have access to it?
* Does the data need to be copied locally?  
  * If yes, where will the data be kept and what storage is required? 
  * If no, what link is required to get access the data? Do you need to apply for access?

#### Case 2: Data is available but needs to be prepared for use in this project

* Data type
* Where is the data and do you have access to it? 
* Does the raw data need to be copied locally?
  * If yes, where will the data be kept and what storage is required? 
  * If no, what link is required to get access the data? Do you need to apply for access?
* What processing needs to be done to the data? 
  1. Processing step 1
  2. Processing step 2 
  3. (Please delete as appropriate)
* Where will the processed data be stored and how long does it need to be stored? 
  1. Processed data step 1
  2. Processed data step 2 
  3. (Please delete as appropriate)
> The data should be stored according the medallion structure depending on how much processing is required. Details are given in the ***Data Documentation*** when this stage of the project is reached and details confirmed.   

#### Case 3: Data is not currently available

* Data type
* How will the data be acquired? 
* What processes are required to run for data collection? 

  * Is machine time required?
  * Are other groups/partners needed to support the collection of data?
  * How long will it take to collect data?

* What machines/sensors/tools are required to collect the data? 

  * If the data collection tools are available, how will they be set-up to collect the correct data?
  * If the data colleciton tools are not available, how will they be acquired and set-up to collect the data? 
  * How long will it take to set-up tools to collect the data?
 
* Where will the raw data be kept, stored and accessed?
* If the data requires further processing, what processing needs to be done to the data? 
  1. Processing step 1
  2. Processing step 2 
  3. (Please delete as appropriate)
* Where will the processed data be stored and how long does it need to be stored? 
  1. Processed data step 1
  2. Processed data step 2 
  3. (Please delete as appropriate)
> The data should be stored according the medallion structure depending on how much processing is required. Details are given in the ***Data Documentation*** when this stage of the project is reached and details confirmed.   







> -------------------------------------------
## Metrics

* What are the qualitative objectives? (e.g. reduce user churn)
* What is a quantifiable goal metric?  (e.g. reduce the fraction of users with 4-week inactivity)
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the fraction of users with 4-week inactivity by 20%)
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; comparison of performance after implementation to baseline)



## Architecture

* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, etc.)
* Data movement tools to move either:
  * all the data,
  * some data after pre-aggregation
  * raw sampled data sufficient for modeling

* What tools and data storage/analytics resources will be used in the solution?
* How will the end solution (e.g. a dashboard or operationalized web service) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions?
  * Data movement pipeline in production
  * Make a one-slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication

* How will we keep in touch with each other and the client? Weekly meetings?
* Who are the contact persons on both sides?


<!-- ---------------------------------------------------------------------------------------------------- -->
## Analytics Plan

*Fill out this document before starting an analysis, and update periodically as and when circumstances change*
*This should serve as a useful clarity tool for you, the analyst, as well as someone not familiar with the work as a quickstart semantic guide*
*The aim of this document is to get you thinking about the whole data science process and help you to avoid some common pitfalls*
*The plan should be reviewed by another data-experienced peer following the initial completion and and subsequent updates*

### Research Question

*What are you trying to answer?*
*what is the objective of the analysis?*
*Why is it important?*

### Data

*What does the data describe? What are the variables?*
*What format is the data?*
*How will it be ingested into the pipeline?*
*How big/small is the dataset?*
*Are the classes balanced/imbalanced?*

### Exploration

*How will you explore the data?*
*What type of plots/analyses are most appropriate for this data?*
*Will you use any specific tools to explore the data?*

### Transformations/Feature Engineering

*What transformations are applied during in the pipeline?*
*Can you use a feature store or do you need to custom build your own features?*
*What features will you engineer and how do they relate to the raw data and ouput?*

### Modelling

*What modelling approach will you take? Why?*
*What package/s are you using for the modelling?*
*What assumptions does your modelling method/algorithm depend on?*
*Does your data/analysis meet the assumptions?*

### Evaluation

*How are you evaluating your model?*
*What metric will you use?*
*Is your metric appropriate? (considering the data, objective and class imbalance)*

### Reporting/visualisation

*How will you report this analysis - written tech report, journal paper, powerpoint pres, custom dashboard, proprietary dashboard etc.?*
*Who are the stakeholders that will be consuming this report, what method is most appropriate for the audience?*
*What tools will you use? (matplotlib, Dash, PowerBI etc)*

### Deployment

*Will this analysis be deployed in a production environment?* 
*Have you considered model monitoring, concept drift & MLOps?*


## Checklist
*note - checkbox rendering in VS code requires the markdown-all-in-one extension (available on the marketplace)*

Have you completed:
*replace the [ ] with [x] for each item you have completed*

### Project set up

- [x] Research Plan
- [ ] Data Dictionary
- [ ] Initialised github repo
- [ ] Initialised environment

### Project delivery

- [ ] Packaged environment
- [ ] Tested notebooks
- [ ] Tested scripts
- [ ] Completed documentation
- [ ] 



*Page created by LL - Feb 2024*