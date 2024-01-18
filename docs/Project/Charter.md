# Project Charter

## Business background

* Who is the client?
* What business domain the client is in.
* What business problems are we trying to address?

## Scope

* What data science solutions are we trying to build?
* What will we do?
* How is it going to be consumed by the customer?

## Personnel

* Who are on this project:
  * Our team:
    * Project lead
    * PM
    * Data scientist(s)
    * Account manager
  * Client:
    * Data administrator
    * Business contact

## Metrics

* What are the qualitative objectives? (e.g. reduce user churn)
* What is a quantifiable goal metric?  (e.g. reduce the fraction of users with 4-week inactivity)
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the fraction of users with 4-week inactivity by 20%)
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; comparison of performance after implementation to baseline)

## Plan

* Phases (milestones), timeline, short description of what will be done in each phase.

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
