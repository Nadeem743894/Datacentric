
# AMRC Data Project Workflow Scoping

### Aim of the document

The aim of this document is to plan the technical aspects of a data project (including required resources) in the context of the business case and the planned end product. It is recommended that this document is filled in during project scoping (at this stage it may not be clear the project is viable or how much money/time/resource are required depending on data availability and storage options). The document is set out according to the AMRC Data-Centric Manufacturing Workflow and for viable projects will provide a strong foundation for producing a Statement of Work as well as a tailored DCM workflow for the project team to follow.  Each bullet point should be considered and basic details given at the scoping stage. 

* Project code: (if/when available)
* Harbour link: (if/when available)

* Which theme is leading this project? 

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

* What data is required for the project? How does it represent what you are trying to gain insights into? 

* Is the project data: 
  1. available as is?
  2. available but needs processing for use in this project?
  3. not currently available?

If there are different data types and sources then more than one case may apply - simply fill in the sections below as required for each data type/source and copy and paste where necessary.

* ***Are there any resource or cost limitations associated with data collection and storage?***
If yes, give details. 

> ### Data acquisition and preparation

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
  3. (Please add or delete as appropriate)
* Where will the processed data be stored and how long does it need to be stored? 
  1. Processed data step 1
  2. Processed data step 2 
  3. (Please add or delete as appropriate)
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
  3. (Please add or delete as appropriate)
* Where will the processed data be stored and how long does it need to be stored? 
  1. Processed data step 1
  2. Processed data step 2 
  3. (Please add or delete as appropriate)
> The data should be stored according the medallion structure depending on how much processing is required. Details are given in the ***Data Documentation*** when this stage of the project is reached and details confirmed.   

### Data Quality and Integrity (further guidance can be given on these as there may be no clear answer at this stage)
* How will you ensure the data is of suitable quality for the project? 
* Is there a timescale for which the data must be kept?
* How will you ensure that the data set contains enough metadata for future use?
* How will access be gained to the data in the future?
* How will you maintain the integrity of the data? 

> ### Missing data
It may not always be possible to collect the data that you require. In some cases this will means that the project is not viable, in other cases though the project can still go ahead as long as the implications of the missing data and the mitigation strategy are well understood in the context of the original problem. 
* Is there missing data? 
* What mitigation is in place if the project is to continue? 
* What are the implications of the missing data? 

> ### Synthetic data
Where 'real' data is not available it may be possible to use synthetic data, although care should be taken to ensure this is representative of real-life data. 
* Is synthetic data going to be used in this project? 
* Will you collect the synthetic data? Give details if yes. 
* Has someone else collected the synthetic data? Give details if yes.

* Where will the synthetic data be kept, stored and how will it be accessed? 


# Next steps 

> The next steps will only be considered in brief detail for now in an effort to ensure the right tools and expertise and timings are in place once the project is in delivery. Further guidance and details can be found in the relevant docs sub-directory.

## Step 3: Data Exploration (EDA)

The aim of data exploration is three-fold: 1. To check that the file contains the data that you expect, 2. To check the quality of the data before committing to more comprehensive analysis and 3. to provide some basic information and visualisations to better understand the data. 

* Who will carry out the data exploration?
* What tools will be used to explore the data?
  * Does this require a licence?
  * Does anyone require training? 
  * Have you identified the training - what are the timings and costs?
* Who will need to see the results of the data exploration? 
* How will EDA be presented? 


## Step 4: Feature Transformation

The aim of feature transformation is to ensure that only relevant bits of the data are used to build models and for further analysis. This may be annual averages, or principal components.

* Who will carry out the feature engineering? 
* What tools will be used for feature transformation?
* Does anyone require training?
  * Have you identified the training - what are the timings and costs?
* Where will the features be kept? Do you have a planned feature store? (This may be the gold level in your chosen data storage option following the medallion structure)
* How will EDA of the features be carried out?
* Who will need to see the EDA of the features and how will it be presented to them? 

## Step 5: Model building

Here the word 'model' is representative of a statistical/machine learning or AI model. The aim of model building is to get further insights from the data and to understand the statistical significance of any identified patterns so far. 

* Who will carry out the model building?
* What tools will be required to carry out model building?
  * Are licences required? Give details if yes.
* What models do you expect to use? 
* Is training required? 
  * Have you identified training, what is the cost and timing of such training? 
* Can you estimate the computer power required?
  * Will you require high performance computing?
  * Will you require cloud access?
  * Do you have access to the correct resources?
    * If no, what are the estimated costs and timescales for the required access?

## Step 6: Evaluation and reporting

To understand the insights and limitations of any data science work requires a collective of expertise and so time should be spent sharing and disseminating results to different stakeholders for feedback and discussion. 

* Who will be required to see the results of the analysis? 
  * How many different types of stakeholder are they and will they require different presentation methods? 
  * Do you need to write a report/give a presentation/etc? 
  * Who will review outputs? 
* Do outputs need marketing input? 
  * Can you give an idea of the costs/time required from the marketing team? 
* Do you have a plan/budget to publish the work if possible? 
* How will success be measured? 

## Step 7: Deployment and maintenance

For successful projects there may be a request for any software or model to become operational. This requires an understanding of MLOps and may involve the commercial team. There may be no answers to this section in the scoping but it may be considered later in the project, or even after the end.  

* Have you been made aware that this should produce operational software/models? 
  * Who will be responsible for the software/models?
  * Who will maintain the software/models? 
* Can the data/software/models be monetised?
  * If yes, give details. 














*Page created by LL - Feb 2024*