import pandas as pd
import numpy as np
import streamlit as st
import requests
import plotly.express as px
import json
import time

time.sleep(2) # rest for 2 seconds


# Instructions
# Choose a COVID-19 API of your choice that contains both valuable data and noise.
# Use Python to gather the data from the API and store it in a Pandas DataFrame.
# Clean the data by removing any irrelevant columns, null values, or duplicates.
# Pre-process the data by normalizing and scaling the numerical data.
# Perform EDA to identify trends, correlations, and patterns in the data. Use visualizations such as histograms, scatter plots, and heatmaps to help you understand the data better.
# Choose the best-suited supervised algorithm to predict the future number of cases. Use techniques such as train-test split, cross-validation, and grid search to optimize the model's performance.
# Once you have chosen the best-suited model, deploy it using Streamlit. Create a user-friendly interface that allows users to input data and view the model's predictions.
# Deploy your streamlit app with streamlit share


# Choose a COVID-19 API of your choice that contains both valuable data and noise.
southAfrica_url = 'https://api.covid19api.com/total/dayone/country/south-africa'
usa_url = 'https://api.covid19api.com/total/dayone/country/usa'
italy_url = 'https://api.covid19api.com/total/dayone/country/italy'
uk_url = 'https://api.covid19api.com/total/dayone/country/uk'
germany_url = 'https://api.covid19api.com/total/dayone/country/germany'


# Use Python to gather the data from the API and store it in a Pandas DataFrame.
def to_dataframe(url_name):
    response = requests.get(url_name)
    data = response.json()
    df = pd.DataFrame(data,index=None)
    return df 

usa = to_dataframe(usa_url)
italy = to_dataframe(italy_url)
southAfrica = to_dataframe(southAfrica_url)
time.sleep(5) # rest for 5 seconds
germany = to_dataframe(germany_url)
uk = to_dataframe(uk_url)


# Clean the data by removing any irrelevant columns, null values, or duplicates.
from datetime import datetime
def dataframe_cleaner(dataframe):
    dataframe = dataframe[['Confirmed', 'Deaths', 'Recovered', 'Active', 'Date']]
    # convert the datetime to a python date format
    for i in range(len(dataframe['Date'])):
        dataframe['Date'][i] = datetime.strptime(dataframe['Date'][i], "%Y-%m-%dT%H:%M:%SZ").date()

    # To determine the distinct values per time from a column with accumulated values over time
    for col in dataframe.columns[:-1]u:
        diffs = dataframe[col].diff()
        dataframe[f'{col}_Distinct'] = diffs.where(diffs > 0, other=0)
        dataframe[f'{col}_Distinct'][0] = dataframe[col][0]

    dataframe = dataframe.iloc[:, 4:] 
    return dataframe

usa_cln = dataframe_cleaner(usa)
italy_cln = dataframe_cleaner(italy)
southAfrica_cln = dataframe_cleaner(southAfrica)
uk_cln = dataframe_cleaner(uk)
ger_cln = dataframe_cleaner(germany)

# Pre-process the data by normalizing and scaling the numerical data.









# container = []

# count = 0
# for i in data.column:
#     while count <= len(data.column):
#         container.append(data.column.iloc[i]-data.column.iloc[i+1])
#         count =+