## This document describes each of the data sets and how they have been processed, including links to the code and links to their exploration report. 

Placeholders in this page allows the output to be shown in tables with links provided. You can add or remove placeholders as necessary and to edit you should replace the text that currently exists. To add to the table simply copy and paste an existing row, to remove delete existing rows. Be careful not to remove any formatting **symbols**. Coding can be done using your preferred language but please provide the relevant script.   

# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. Exploration of each dataset is provided in the data summary report.

For each data source, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided.

## Bronze data - raw data sources

* Dataset 1 - [Give a brief summary of the dataset, including how to access the data.  More detailed information is available in the Dataset 1 Report]
* Dataset 2 - [Give a brief summary of the dataset, including how to access the data.  More detailed information is available in the Dataset 2 Report]

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Dataset 1 | [Original Location](link/to/raw/data/source) Brief description of its original location |  [Destination Location](link/to/destination/data/storage) Brief description of its destination location | [The script used to load the data can be found here](link/to/python/script/file/in/Code) | [Dataset 1 Exploration Report](link/to/rawdata/report1)|
| Dataset 2 | [Original Location](link/to/raw/data/source) Brief description of its original location | [Destination Location](link/to/destination/data/storage) Brief description of its destination location | [The script used to load the data can be found here](link/to/R/script/file/in/Code) | [Dataset 2 Exploration Report](link/to/rawdata/report2)|


> If the raw data is not to be kept locally then replace destination location with the same link as the original location. There may not be an exploration report for the raw data but if any information on the dataset is available a link can be provided. 

## Silver data - processed data

* Processed Dataset 1 - [Give a brief summary of the processed data, including why the data was processed in this way.  More detailed information is available in the Processed Dataset 1 Report.]
* Processed Dataset 2 - [Give a brief summary of the processed data, including why the data was processed in this way.  More detailed information is available in the Processed Dataset 2 Report.]

| Processed Dataset Name | Input Dataset(s) | Destination Dataset | Data Processing Tools/Scripts | Link to Report | Data Processed by | Access Restrictions |
| ---:| ---: | ---: | ---: | ---: | ---: | ---: |
| Processed Dataset 1 | [Raw data location](link/to/input/data/storage) | [Processed Dataset 1 Location](link/to/processed/data/storage) | [The script used to process the data can be found here](link/to/python/script/file/in/Code) | [Processed Dataset 1 Exploration Report](link/to/processeddata1/report1)| Name of engineer | None or give details |
| Processed Dataset 2 | [Raw data location](link/to/input/data/storage) | [Processed Dataset 2 Location](link/to/processed/data/storage) |[The script used to process the data can be found here](link/to/R/script/file/in/Code) | [Processed Dataset 2 Exploration Report](link/to/processeddata2/report2)| Name of engineer | None or give details |

> The raw data location should match the destination location of the raw data. 


## Gold data - Feature Sets

* Feature Set 1 - [Give a description of the feature set, such as the meaning of each feature.  More detailed information is available in the Feature Set 1 Report.]
* Feature Set 2 - [Give a description of the feature set, such as the meaning of each feature.  More detailed information is available in the Feature Set 2 Report.]

| Feature Set Name | Input Dataset(s) | Feature Store | Feature Engineering Tools/Scripts | Link to Report | Data Processed by | Access Restrictions |
| ---:| ---: | ---: | ---: | ---: | ---: | ---: |
| Feature Set 1 | [Processed Dataset Location](link/to/processed/data/storage) |  [Feature 1 Dataset Location](link/to/processed/data/storage) | [The script used to process the data can be found here](link/to/R/script/file/in/Code) | [Feature Set 1 Exploration Report](link/to/report1)|  Name of engineer | None or give details |
| Feature Set 2 |[Processed Dataset Location](link/to/processed/data/storage) |  [Feature 1 Dataset Location](link/to/processed/data/storage) | [The script used to process the data can be found here](link/to/sql/script/file/in/Code) | [Feature Set 2 Exploration Report](link/to/report2)|  Name of engineer | None or give details |



 *Page created by LL - Feb 2024, based on Microsoft Team Data Science*