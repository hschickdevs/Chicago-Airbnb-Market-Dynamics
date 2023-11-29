"""
Distribution of hosts by number of listings (Srishti's code)
How many hosts have a profile pic and/or are a superhost (Srishti's code)
Is a host being a superhost correlated with more monthly reviews? (Srishti's code)
"""
import streamlit as st
import pandas as pd
import plotly.express as px

# Custom imports
from data import SnowflakeConnector
from util import handle_env

# Set up page configuration
st.set_page_config(page_title="👤 Chicago Airbnb Host Insights", page_icon="👤")

# Markdown for the page
st.markdown("# 👤 Chicago Airbnb Host Insights")
st.sidebar.header("👤 Chicago Airbnb Host Insights")

# Description
st.markdown(
    """
    In this section we aim to uncover the trends and patterns in listing prices and reviews over time in Chicago.
    
    ### 🗂️ Dataset Used:
    
    For this analysis, we are querying the `calendar.csv` dataset, stored in Snowflake due to its astronomical size. Each row of the data represents the airbnb price for each day each each listing on airbnb for the past year.
    
    The `calendar.csv` dataset contains the following columns (data head shown below): 
    
    | listing_id | date      | available | price   | adjusted_price | minimum_nights | maximum_nights |
    |------------|-----------|-----------|---------|----------------|----------------|----------------|
    | 2384       | 9/12/2023 | f         | $125.00 | $125.00        | 3              | 1125           |
    | 2384       | 9/13/2023 | f         | $125.00 | $125.00        | 3              | 1125           |
    | 2384       | 9/14/2023 | f         | $125.00 | $125.00        | 3              | 1125           |
    | 2384       | 9/15/2023 | f         | $100.00 | $100.00        | 3              | 1125           |
    | 2384       | 9/16/2023 | f         | $100.00 | $100.00        | 3              | 1125           |
    """
)

# Set up environment and database connection
handle_env()
snowflake_cxn = SnowflakeConnector()
