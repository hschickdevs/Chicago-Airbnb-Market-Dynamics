import streamlit as st

from util import handle_env

handle_env()

st.set_page_config(
    page_title="Overview",
    page_icon="🏠",
)

st.sidebar.success("☝️ Select an analysis theme above to explore.")

st.markdown(
"""
# 🌎 Data Management Final Project - Chicago Airbnb Market Analysis 📊
"""
)

st.image("https://miro.medium.com/v2/resize:fit:1358/0*NChTo-XqLOxLabIW")

st.markdown(
"""
## Project Selection & Motivations

Welcome to our comprehensive analysis of the Airbnb market in Chicago. This project was chosen due to the dynamic and diverse nature of the Chicago Airbnb landscape, which presents a unique opportunity to explore various aspects of urban hospitality and economics. Chicago, known for its rich cultural heritage and vibrant neighborhoods, offers a plethora of data that can yield insights into both the short-term rental market and the city's socioeconomic dynamics.

The motivation behind this project stems from a desire to understand:

1. **The impact of external factors** such as local events and crime rates on the short-term rental market.
2. **Host behavior and strategies**, which can influence guest experiences and rental success.
3. **Neighborhood dynamics**, exploring how different areas of the city compare in terms of pricing, popularity, and guest satisfaction.
4. **Economic implications** for both hosts and renters in the context of the larger Chicago economy.

By dissecting these elements, we aim to provide valuable insights for hosts, guests, and local policymakers.

## Questions We Are Trying to Answer

Our analysis is structured around several key questions, each designed to unravel a different facet of the Airbnb experience in Chicago:

1. **Market Dynamics:** How do listing prices and review frequencies change over time? What external factors, like crime rates, influence these dynamics?
2. **Host Insights:** What characterizes successful hosts in terms of number of listings, profile completeness, and status as a superhost?
3. **Neighborhood Analysis:** Which neighborhoods are most and least expensive? How do safety and local amenities influence pricing?
4. **Price and Reviews Correlation:** How do guest reviews relate to pricing strategies? Does a higher price correlate with better ratings?
5. **Listing Characteristics:** What impact do room types and amenities have on listing prices?
6. **Host Experience and Pricing:** Is there a relationship between a host's tenure on the platform and the pricing of their listings?

Through these questions, we aim to paint a comprehensive picture of the Airbnb market in Chicago, offering insights that can benefit hosts, guests, and analysts alike.

## Data Acquisition

We obtained the data for our project from 2 sources, http://insideairbnb.com/get-the-data/ and https://data.cityofchicago.org/. From the airbnb dataset, we downloaded the detailed listings csv (listings.csv) for airbnbs in Chicago, the associated reviews csv for those listings (reviews.csv), and the calendar csv containing pricing data for listings over time (calendar.csv). From the Chicago dataset we downloaded the crime reports csv data for Chicago for the entire year of 2020 (crimes_2020.csv), and the geospatial boundary data for every unique Chicago neighborhood (boundaries_neighborhoods.geojson).

The largest challenge we faced from getting acquiring the data was loading the calendars.csv file from the airbnb database because the zip file would not unzip on MacOS. To remedy this, we used Windows to unzip the data and process the data.

## Data Sampling
"""
)

st.image("https://drive.google.com/uc?export=view&id=1vaXGXW-6aqXb-hlHTQEFQfcaPrIS7wCs")
st.image("https://drive.google.com/uc?export=view&id=13yjSbRyCM4c70JmTnlLkPCGsur-JM5eH")
st.image("https://drive.google.com/uc?export=view&id=14LE_tnSKHNl5knflnPeV_-TgKHEKNqca")
st.image("https://drive.google.com/uc?export=view&id=1n6A46KB2hXGSt9AykqHWozDQlXNy5U6q")

st.markdown(
    """
    ## Data Cleaning

    The main ETL tools we used were Python Jupyter notebooks for data extraction and transformation and the Snowflake console wizard for data loading.

    Our cleaning startegy began with extracting only the relevant columns from the listings.csv (columns that pertained to data collection, unnecessary web links, and columns that lacked any data). Then we cleaned up columns with false but relevant data pertaining to information on bed, bedrooms, and bathrooms counts. We were able to ressed these columns with values that were extracted from another column that contained the listing name which had the actual value counts for these columns. We also encoded columns with categorical variables by creating new columns with numerical values that mapped to those categories; these columns included. The next thing we did to clean this data was fix NaN values in numerical columns by imputing those values with the columnar mean. 

    After working on the listings.csv we moved onto the reviews.csv and calendars.csv of which we removed columns that were not relevant such as reviewer first names since those names did not have a context and could be repeated for different people. Then, since the reviews, calendar, and listings data all contained primary and foreign key values that mapped to each other but were extremely large, we decided to map those values and reset their sequences to start from 1 - this would help us drastically reduce the data size of our tables.

    The next piece of work was to process the Chicago crime data by mapping a json list of Chicago neighborhoods to the their neighborhood numbers in the crime dataset. We then grouped by the communities in the crime data to compute a relative crime rate to produce a new communities.csv that contained the community number, community name, relative crime rate, and geospatial boundaries. After we mapped community names to community numbers, we went back to the listings.csv to impute a column to hold community numbers that corresponded to the communities where the listings were hosted. 

    The last piece of transformation was to break down the reviews.csv and calendars.csv files into smaller chunks since they exceeded the 50MB loading capacity of the Snowflake Console Wizard.

    Once those CSVs were broken down, we used the Snowflake Console Wizard to create tables within a database instance and schema inside of Snowflake and automatically generate a table schema for those listings, reviews, calendar, and communities tables.

    To complete loading, we then loaded any CSV files that were broken into chunks into their corresponding tables, the Snowflake Console Wizard was able to resolve any row and column header conflicts for us.
    """
)

st.image("https://drive.google.com/uc?export=view&id=1hhI7bCGNpDuOr9DdfbnQM9H6iPZYkHN2", caption="Snowflake Data Import")