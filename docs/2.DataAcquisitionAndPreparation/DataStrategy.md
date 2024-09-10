# The data strategy

This document sets out your data strategy and should be carried out before any data is collected or analysed. The first draft of the data strategy can be copied from the [project scoping document](/docs/0.ProjectManagement/ProjectScoping.md). This, however, should be a live document and maintained and updated as the project progresses. It should also provide information on the data that will be created during the process and how it will be stored and accessed in the future. This document will also act as your data management plan.

## Data acquired and used in the project - update as required 

## Data Capture & Analysis (Work Package 1)
*The AMRC North West will monitor the overall power usage of the site(s) in question via the distribution cabinet (access
and installation support to be provided by Boeing building management and maintenance engineers).
Utilising AI driven deep learning and analytics, the AMRC North West will monitor the overall energy usage on site at
the training centre and create a map of energy usage by specific asset. This data can be used to tweak individual
parameters.
To begin training the system, the AMRC North West will utilise  data captured directly from a flight simulator via off the shelf monitoring equipment (to be
installed alongside the main distribution sensors).*



## Naming conventions

* The folder  is created by following the project number and the name of the project.
* The file naming convention is project number with version 
* Kilo-Watt-Hours, Amp-Hours, Phase 1, Phase 2, Phase 3, Temperature, Light. 

## Data created during the project

* What data is being created in the project? 
* The project mainly highlights the three phase current data captured from boeing flight simulators and detecting their temperature and light variations on the gatwick site. 

#### Data description 1 *copy and paste for each data set created* 
* What is this data? Provide a short description and a data dictionary (provide a link to the data dictionary).
* The project mainly highlights the three phase current data captured from boeing flight simulators and detecting their temperature and light variations on the gatwick site. 
* How is the data being created?
* The data is being created by using off-the shelf three phase current clamps, temperature and light sensors. The Current sensors are used to monitor the current consumption of flight simulators. The Temperature and light sensors were used to record the temperature and light changes in boeing vacinity.  
* Where will this data be kept? Provide a link. 
* \datascience-project-template\data\Data
* What size is the data?
* The total size of the data is approx 20 MB. This means for all flight simulators with temperature and light data.
* What format is the data in? 
* The data is stored in the csv format. 
* What metadata is required? How will this be stored?
* No metadata required for the projec. This data is stored in the csv format and each sample is recorded and processed accordingly
* How will data quality be recorded?
* The quality is recorded by checking the calibration of the sensors and these sensors are precalibrated and provide the accurate readings.
* How will any limitations/short comings of the data be recorded? 
* The short comings for the data gathering might be (Internet dependency and LoRAWAN Setup), some of the data might get lost if intenet is distrupted within the vacinity. 
* How are the data linked to the analysis for transparency and lineage? 
* The data plays a vital role to analyse the behaviour of the flight simulators so both customer and the AMRC were aware about the features of the data.
* Is the data sensitive?
* No, the data cannot be categorised as the sensitive information.
* Are there any data ethics issues? 
* N/A
* Any other details/restrictions.
* N/A

# Back-up and retention

#### Data description 1 *copy and paste for each data set created*
* How is the data being backed up?
* The data is stored on the iMonnit cloud and is redily available to download and analysis purpose.
* Is fast access to the data required?  
* As the main platform to access data is iMonnit cloud services and this data is   readily available depends on the users grant to access the platform.
* How long is the data to be kept?
* The data is captured for almost 3 months. This period is very optimal to analyse the behaviour of the machines and detect the rate of change in temperature and light constrains.
* How is quality maintained in the long-term?#
* The sensors used to detect data (Current, Temperature and Light) are pre-calibrated and if by chance the calibration failed, the sensors are compared with the calibrated data to maintain the data quality for the long time. 
* How is security of the data maintained?
* The data from the sensors are end-to-end encypted and therefore only the two end entities will be able to understand the data, this encryption method can make data tranfer more secure and reliable. 

# Data sharing and reuse

#### Data description 1 *copy and paste for each data set created*
* Who owns the data IP and any IP coming from the use of the data?
* The AMRC NW and the Customer 
* Will the data be published? If so, how and where?
* N/A
* Who will have access to this data? 
* AMRC NW and the Customer.
* How will others access the data?
* N/A
* How will the data be cited? 
* N/A



 *Page created by LL - Feb 2024*

