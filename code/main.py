# Create a main.py script for a Dockerised application
##############################################
### Import packages

import pandas as pd
import os 
import time 

##############################################
### Logging example + verification

# Logging example, this will populate the logs in /code/logs/
import logging
logging.basicConfig(filename='./logs/example.log', level=logging.INFO)

logging.info("python-app script running")

# Load the example data file from /data/external/ and log the result to /code/logs/
df_static = pd.read_csv('../data/external/example_data.csv')
logging.info('Example data:')
logging.info(df_static)

# Load an environment variable from /code/environment_variables/python-app.env and log the result to /code/logs/
logging.info('Environment variable: ' + str(os.environ['APP_VARIABLE_1']))

##############################################
### Your code here...

# Wait 60 seconds before restarting container
time.sleep(60)